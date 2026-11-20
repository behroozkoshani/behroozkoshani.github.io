# Cybersecurity Engineering Projects

Three portfolio-ready **starter implementations** by Behrooz Koshani. These projects demonstrate reproducible offline analysis using synthetic datasets; they are **not claims of enterprise deployment or live penetration testing**.

| Project | Focus | Run |
| --- | --- | --- |
| [Cloud Configuration Risk Analyzer](cloud-security-assessment/) | AWS Terraform plan analysis | `python3 cloud_security.py sample-plan.json` |
| [Vulnerability Prioritization Engine](vulnerability-management/) | Exposure-aware triage and remediation SLA | `python3 prioritize.py sample-vulnerabilities.csv` |
| [Active Directory Identity Audit](active-directory-security/) | Risky account configuration detection | `python3 audit_ad.py sample-users.csv` |

Each project includes working Python source, synthetic inputs, reproducible instructions, limitations, and specific ideas for extending it into a full lab. All scripts use the Python 3 standard library and do not make network calls.

**Ethics:** Run assessments against systems and data you own or are authorized to test. Do not include real credentials, customer data, or proprietary logs in a public repository.
