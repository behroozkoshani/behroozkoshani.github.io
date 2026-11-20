# Cybersecurity Engineering Portfolio

**Behrooz Koshani | Security engineering · Risk management · Identity security**

This is a collection of three **independently runnable projects** developed as portfolio demonstrations. Each subdirectory has its own README, Python code, synthetic test data, tests, project architecture, and findings report. The structure follows the evidence-first approach of my [Metasploit attack-simulation lab](https://github.com/behroozkoshani/metasploit-attack-simulation-lab).

> **Project status:** Demonstration implementations using *fabricated* data. The scripts perform offline checks; no live AWS infrastructure, enterprise vulnerability scanner, or domain controller was accessed. Reports and illustrations are examples, not screenshots of real security operations.

## Projects

| Project | Security domain | Deliverable | Source |
| --- | --- | --- | --- |
| [Cloud Security Configuration Analyzer](cloud-security-assessment/) | Cloud / Terraform / IAM | Three configuration detection checks plus remediations | [Code](cloud-security-assessment/cloud_security.py) |
| [Vulnerability Prioritization Engine](vulnerability-management/) | Vulnerability management / risk | Risk-ranked patch backlog, CSV export | [Code](vulnerability-management/prioritize.py) |
| [Active Directory Account Security Audit](active-directory-security/) | IAM / Windows security | Policy and risky-account findings | [Code](active-directory-security/audit_ad.py) |

## Reproduce the demonstrations

Prerequisite: Python 3.10+; no external packages or credentials required.

```bash
cd projects/cloud-security-assessment
python3 cloud_security.py sample-plan.json
python3 -m unittest discover -p 'test_*.py' -v

cd ../vulnerability-management
python3 prioritize.py sample-vulnerabilities.csv --output prioritized.csv
python3 -m unittest discover -p 'test_*.py' -v

cd ../active-directory-security
python3 audit_ad.py sample-users.csv
python3 -m unittest discover -p 'test_*.py' -v
```

A [GitHub Actions workflow](../.github/workflows/cybersecurity-projects.yml) also runs unit tests and smoke tests when relevant files change.

## How to evaluate these projects

Inspect the source and tests, run the sample data, compare output with each project’s `FINDINGS.md`, and review the limitations. These are deliberately small, transparent prototypes meant to be extended with approved real-world integrations—not representations of completed enterprise deployments.

## Security and privacy

Use only authorized environments. Terraform plans and real scan/identity exports may contain sensitive information; do not commit production data. All provided example files use fictitious values.

## Next-stage engineering work

- Cloud: recognize additional AWS resource schemas, produce SARIF, validate against Checkov.
- Vulnerability management: import scanner exports, CISA KEV/EPSS enrichment, rescan verification.
- Active Directory: read-only lab exporter, nested-group assessment, exception handling and remediation validation.
