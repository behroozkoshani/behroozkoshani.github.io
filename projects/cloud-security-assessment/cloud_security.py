#!/usr/bin/env python3
"""Analyze selected AWS security risks in Terraform plan JSON (offline)."""
import argparse
import json
from pathlib import Path

PUBLIC_CIDRS = {"0.0.0.0/0", "::/0"}
PROTECTIONS = ("block_public_acls", "block_public_policy", "ignore_public_acls", "restrict_public_buckets")


def analyze(plan):
    findings = []
    for resource in plan.get("resource_changes", []):
        address = resource.get("address", "(unknown)")
        kind = resource.get("type")
        after = (resource.get("change") or {}).get("after")
        if not isinstance(after, dict):
            continue
        if kind == "aws_security_group":
            for rule in after.get("ingress", []) or []:
                if not isinstance(rule, dict) or rule.get("protocol") not in ("tcp", "6", "-1"):
                    continue
                lo, hi = rule.get("from_port"), rule.get("to_port")
                if not isinstance(lo, int) or not isinstance(hi, int):
                    continue
                cidrs = set(rule.get("cidr_blocks") or []) | set(rule.get("ipv6_cidr_blocks") or [])
                if cidrs & PUBLIC_CIDRS:
                    for port in (22, 3389):
                        if lo <= port <= hi:
                            findings.append({"severity": "HIGH", "resource": address,
                                             "rule": "PUBLIC_ADMIN_PORT", "evidence": f"TCP/{port} open to public CIDR",
                                             "remediation": "Restrict source CIDRs or use a managed access path."})
        elif kind == "aws_s3_bucket_public_access_block":
            disabled = [flag for flag in PROTECTIONS if after.get(flag) is False]
            if disabled:
                findings.append({"severity": "HIGH", "resource": address,
                                 "rule": "S3_PUBLIC_ACCESS_BLOCK_DISABLED",
                                 "evidence": "Disabled controls: " + ", ".join(disabled),
                                 "remediation": "Enable all four S3 public access block controls where appropriate."})
        elif kind == "aws_iam_policy":
            raw = after.get("policy")
            try:
                policy = json.loads(raw) if isinstance(raw, str) else raw
            except json.JSONDecodeError:
                continue
            if not isinstance(policy, dict):
                continue
            statements = policy.get("Statement", [])
            if isinstance(statements, dict):
                statements = [statements]
            for statement in statements:
                if not isinstance(statement, dict) or statement.get("Effect") != "Allow":
                    continue
                actions = statement.get("Action", [])
                resources = statement.get("Resource", [])
                actions = [actions] if isinstance(actions, str) else actions
                resources = [resources] if isinstance(resources, str) else resources
                if "*" in actions and "*" in resources:
                    findings.append({"severity": "CRITICAL", "resource": address,
                                     "rule": "IAM_ALLOW_ALL_ACTIONS_RESOURCES",
                                     "evidence": "IAM Allow with Action=* and Resource=*",
                                     "remediation": "Scope actions/resources to least privilege."})
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, help="Terraform plan JSON")
    parser.add_argument("--json", action="store_true", help="Emit JSON findings")
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    if not isinstance(plan, dict) or not isinstance(plan.get("resource_changes"), list):
        parser.error("Expected Terraform plan JSON containing a resource_changes array.")
    findings = analyze(plan)
    if args.json:
        print(json.dumps({"finding_count": len(findings), "findings": findings}, indent=2))
    else:
        for item in findings:
            print(f"[{item['severity']}] {item['rule']} @ {item['resource']}: {item['evidence']}")
            print(f"  Fix: {item['remediation']}")
        print(f"Total findings: {len(findings)}")


if __name__ == "__main__":
    main()
