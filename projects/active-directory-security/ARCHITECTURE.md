# Architecture and Data Flow

```text
Lab AD inventory (future) / synthetic CSV (current)
                         |
                   sanitized export
                         |
                         v
                      audit_ad.py
                         |
                enabled-account filter
                         |
          +--------------+---------------+
          |              |               |
     stale/admin     password flag   preauth flag
          |              |               |
          +--------------+---------------+
                         |
                         v
                CLI / JSON findings
                         |
                         v
           access review -> approved fix -> re-audit
```

**Current scope:** The script examines a pre-prepared identity inventory CSV; it does not connect to AD or execute PowerShell. `privileged` must be accurately computed by the export process. This prototype does not infer nested group memberships or detect real Kerberoasting activity.

**Risk decisions:** Flagged accounts require human review. Some service accounts and emergency accounts have documented exceptions, and last-logon signals may be incomplete.

**Future extension:** Write a read-only PowerShell exporter for a disposable Windows domain lab; include privileged group inheritance, managed service accounts, and exception approvals.
