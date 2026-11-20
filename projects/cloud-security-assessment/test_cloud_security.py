import unittest
from cloud_security import analyze


class CloudSecurityTests(unittest.TestCase):
    def test_public_ssh(self):
        plan = {"resource_changes": [{"address": "sg", "type": "aws_security_group",
            "change": {"after": {"ingress": [{"protocol": "tcp", "from_port": 22,
            "to_port": 22, "cidr_blocks": ["0.0.0.0/0"]}]}}}]}
        self.assertEqual(analyze(plan)[0]["rule"], "PUBLIC_ADMIN_PORT")

    def test_restricted_ssh(self):
        plan = {"resource_changes": [{"address": "sg", "type": "aws_security_group",
            "change": {"after": {"ingress": [{"protocol": "tcp", "from_port": 22,
            "to_port": 22, "cidr_blocks": ["10.0.0.0/8"]}]}}}]}
        self.assertEqual(analyze(plan), [])

    def test_deleted_resource(self):
        self.assertEqual(analyze({"resource_changes": [{"type": "aws_iam_policy",
            "change": {"after": None}}]}), [])


if __name__ == "__main__":
    unittest.main()
