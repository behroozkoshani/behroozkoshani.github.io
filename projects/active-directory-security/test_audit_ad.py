import unittest
from audit_ad import audit


def row(**overrides):
    account = {"sam_account_name": "demo", "enabled": "true", "privileged": "false",
               "password_never_expires": "false", "preauth_required": "true",
               "last_logon_days_ago": "0"}
    account.update(overrides)
    return account


class ADAuditTests(unittest.TestCase):
    def test_privileged_stale(self):
        results = audit([row(privileged="true", last_logon_days_ago="100")])
        self.assertIn("STALE_PRIVILEGED_ACCOUNT", [finding["rule"] for finding in results])

    def test_disabled_not_reported(self):
        self.assertEqual(audit([row(enabled="false", preauth_required="false")]), [])

    def test_preauth_disabled(self):
        self.assertEqual(audit([row(preauth_required="false")])[0]["rule"],
                         "KERBEROS_PREAUTH_DISABLED")


if __name__ == "__main__":
    unittest.main()
