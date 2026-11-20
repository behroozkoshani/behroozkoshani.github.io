# Identity Security Audit — Synthetic Account Inventory

**Scope:** The fabricated `sample-users.csv`; account names do not correspond to real employees.

## Reproduction

```bash
python3 audit_ad.py sample-users.csv --json
```

## Expected findings

| Account | Rule | Severity | Suggested investigation |
| --- | --- | --- | --- |
| admin.demo | STALE_PRIVILEGED_ACCOUNT | HIGH | Verify administrator still requires access |
| admin.demo | PRIVILEGED_PASSWORD_NEVER_EXPIRES | HIGH | Review rotation/managed-identity approach |
| legacy.demo | KERBEROS_PREAUTH_DISABLED | HIGH | Review exception, require preauthentication |
| legacy.demo | STALE_ENABLED_ACCOUNT | MEDIUM | Validate inactivity and ownership |

**Expected total:** 4 findings. These are expectations based on the sample file, not real domain results. `disabled.demo` should not be reported because it is disabled.

## Analyst notes

A privileged stale account creates a potentially unnecessary access path, but the recommendation should be reviewed with system owners. Disabling Kerberos preauthentication can increase offline password-guessing risk, but this inventory flag is not evidence of active exploitation. Review account type, exception process, lastLogonTimestamp caveats, and effective group membership before making access changes.

## Limitations

No domain controller was accessed. No live account was changed. Current privilege status is supplied by input and is not independently verified.
