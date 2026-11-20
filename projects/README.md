# Cybersecurity Engineering Portfolio — Behrooz Koshani

A set of three **runnable defensive security projects** demonstrating cloud configuration review, vulnerability risk triage, and Active Directory identity auditing.

> **Evidence status:** These are working offline Python demonstrations using synthetic datasets. Local executions and unit tests were captured on November 19, 2026 (EST); the captures do **not** show live AWS, enterprise scanner, or Active Directory systems. See [Documentation Guide](DOCUMENTATION-GUIDE.md).

| Project | Core deliverable | Visual walkthrough | Detailed documentation |
| --- | --- | --- | --- |
| [Cloud Security Assessment](cloud-security-assessment/) | Terraform JSON configuration analyzer | [2 verified terminal screenshots](cloud-security-assessment/SCREENSHOTS.md) | [Architecture](cloud-security-assessment/ARCHITECTURE.md) · [Findings](cloud-security-assessment/FINDINGS.md) |
| [Vulnerability Management Engine](vulnerability-management/) | Risk ranking and remediation queue | [2 verified terminal screenshots](vulnerability-management/SCREENSHOTS.md) | [Architecture](vulnerability-management/ARCHITECTURE.md) · [Findings](vulnerability-management/FINDINGS.md) |
| [Active Directory Security Audit](active-directory-security/) | Identity inventory rules and review flags | [2 verified terminal screenshots](active-directory-security/SCREENSHOTS.md) | [Architecture](active-directory-security/ARCHITECTURE.md) · [Findings](active-directory-security/FINDINGS.md) |

## Run the implementations

Python 3.10 or newer; no external dependencies or cloud credentials:

```bash
cd projects/cloud-security-assessment
python3 cloud_security.py sample-plan.json
python3 -m unittest discover -p 'test_*.py' -v

cd ../vulnerability-management
python3 prioritize.py sample-vulnerabilities.csv
python3 -m unittest discover -p 'test_*.py' -v

cd ../active-directory-security
python3 audit_ad.py sample-users.csv
python3 -m unittest discover -p 'test_*.py' -v
```

## Documentation and test coverage

Each directory contains a main README, architecture overview, findings report, screenshots guide, two captured local execution screenshots, source, synthetic data, and tests. [GitHub Actions](../../actions) runs Python tests on changes. Check its actual execution status rather than assuming all runs pass.

## Security boundary

No live AWS deployment, external vulnerability scanning, or directory administration is conducted by these scripts. Only run any future real-world tests in explicitly authorized environments. Review [SECURITY.md](SECURITY.md) before using sensitive scan exports or IAM inventories.

## Captured local demonstrations

Each project now contains real Xterm screenshots of its **local Python execution** and **unit tests**, plus an [evidence report](DOCUMENTATION-GUIDE.md). The data is fabricated and does not imply access to deployed cloud or domain environments.
