# Portfolio Documentation Guide

This document explains the files included in each of the three portfolio projects, how a reviewer should use them, and the evidence boundaries.

## File-by-file guide

| File | Purpose | How to interpret |
| --- | --- | --- |
| `README.md` | Main narrative: goals, scope, setup, technologies, steps, risks, and roadmap | Read first to understand what was built and what was not built. |
| `ARCHITECTURE.md` | Text architecture diagram showing data source, parser, rules, findings and decision points | Shows the system's data flow and trust boundaries; it does not document a deployed enterprise topology. |
| `FINDINGS.md` | Written assessment of synthetic findings and suggested remediations | Example analyst report based on fabricated input, not evidence of a production vulnerability. |
| `SCREENSHOTS.md` | Real local CLI run and unit-test evidence | Captures of executable Python demonstrations using synthetic fixtures, not enterprise activity. |
| `screenshots/verified-local-*.png` | Genuine locally captured terminal screenshots | Python sample output and unit tests were actually executed; no cloud or directory systems were accessed. |
| Main `*.py` script | Executable, dependency-free defensive analyzer | Run it locally on the included fabricated sample to independently reproduce behavior. |
| `sample-*.csv` / `sample-*.json` | Minimal harmless input records | These synthetic datasets enable repeatable demonstrations without exposing customer information. |
| `test_*.py` | Unit tests for selected detection and validation cases | Useful for understanding expected behavior and catching regressions; does not prove complete security coverage. |
| `projects/.gitignore` | Local generated files and secret hygiene | Helps avoid committing temporary outputs, but does not replace review before pushing. |
| `projects/SECURITY.md` | Scope-of-authorization and privacy rules | Establishes safe handling guidelines for any future real-world testing. |
| `.github/workflows/cybersecurity-projects.yml` | CI checks on supported Python versions | Runs unit tests and smoke tests after changes; consult the Actions page for actual run results. |

## Evidence tiers

**Tier 1 — Source code:** Clear, reviewable implementations. All three projects provide this.

**Tier 2 — Reproducible demonstration:** Fabricated input, documented expected outputs, automated tests, and visual explanations. All three projects provide this.

**Tier 3 — Captured local execution:** The three Python scripts and their existing tests were executed on synthetic sample files; six genuine Xterm screen captures of program and unit-test output are included. **Not an AWS, vulnerability scanner, or Active Directory integration lab.**

**Tier 4 — Verified operational outcome:** Before/after security measurements, owner-approved remediation, and independent validation. **Not included yet.**

## What can be claimed on a resume

You can accurately describe writing Python prototypes that analyze sample Terraform plans, rank sample vulnerability records, and audit sanitized identity exports. Do not claim enterprise rollout, actual vulnerability remediation, cloud hardening, or Active Directory access reviews without performing and documenting those activities.

## Suggested next steps

Perform an authorized lab exercise for each project, capture authentic output with privacy review, add metrics, and document the limits of the assessment. This closes the gap between a functional portfolio prototype and a fully evidenced practical security project.
