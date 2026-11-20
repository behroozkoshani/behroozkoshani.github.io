#!/usr/bin/env python3
"""Audit exported (sanitized) identity data for selected AD account risks."""
import argparse
import csv
import json
from pathlib import Path

FIELDS = ("sam_account_name", "enabled", "privileged", "password_never_expires",
          "preauth_required", "last_logon_days_ago")


def boolean(value):
    normalized = value.strip().lower()
    if normalized not in ("true", "false"):
        raise ValueError(f"Expected true/false, got {value!r}")
    return normalized == "true"


def audit(rows):
    findings = []
    for row in rows:
        user = row["sam_account_name"]
        enabled = boolean(row["enabled"])
        privileged = boolean(row["privileged"])
        never_expires = boolean(row["password_never_expires"])
        preauth_required = boolean(row["preauth_required"])
        days = int(row["last_logon_days_ago"])
        if days < -1:
            raise ValueError("last_logon_days_ago must be -1 or nonnegative")
        if not enabled:
            continue
        checks = []
        if privileged and days >= 90:
            checks.append(("HIGH", "STALE_PRIVILEGED_ACCOUNT",
                           f"Privileged enabled account idle {days} days",
                           "Review owner; disable if unused after approval."))
        if privileged and never_expires:
            checks.append(("HIGH", "PRIVILEGED_PASSWORD_NEVER_EXPIRES",
                           "Privileged account configured with password never expires",
                           "Review managed identity or rotation controls and exception policy."))
        if not preauth_required:
            checks.append(("HIGH", "KERBEROS_PREAUTH_DISABLED",
                           "Kerberos preauthentication disabled",
                           "Require Kerberos preauthentication unless an approved exception exists."))
        if days >= 90 and not privileged:
            checks.append(("MEDIUM", "STALE_ENABLED_ACCOUNT",
                           f"Enabled account idle {days} days",
                           "Review ownership and disable unused account after approval."))
        for severity, rule, evidence, remediation in checks:
            findings.append({"account": user, "severity": severity, "rule": rule,
                             "evidence": evidence, "remediation": remediation})
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Sanitized account inventory CSV")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    with args.input.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not set(FIELDS).issubset(reader.fieldnames or []):
            parser.error("Missing required CSV columns: " + ", ".join(FIELDS))
        findings = audit(reader)
    if args.json:
        print(json.dumps({"finding_count": len(findings), "findings": findings}, indent=2))
    else:
        for f in findings:
            print(f"[{f['severity']}] {f['account']} | {f['rule']}: {f['evidence']}")
            print(f"  Review: {f['remediation']}")
        print(f"Total findings: {len(findings)}")


if __name__ == "__main__":
    main()
