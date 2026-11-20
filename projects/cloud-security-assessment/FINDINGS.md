# Sample Cloud Security Assessment — Synthetic Data

**Scope:** `sample-plan.json`, which is a fabricated Terraform plan fragment. No AWS resources were provisioned.

## Method

The analyzer evaluates the planned `after` state and reports selected high-risk conditions. Run:

```bash
python3 cloud_security.py sample-plan.json
```

## Expected findings

| Rule | Synthetic asset | Severity | Why it matters | Suggested fix |
| --- | --- | --- | --- | --- |
| PUBLIC_ADMIN_PORT | aws_security_group.admin_demo | HIGH | Public SSH exposure enlarges attack surface | Restrict sources or use managed access |
| S3_PUBLIC_ACCESS_BLOCK_DISABLED | aws_s3_bucket_public_access_block.demo | HIGH | One protective block is set to false | Enable appropriate public-access blocks |
| IAM_ALLOW_ALL_ACTIONS_RESOURCES | aws_iam_policy.admin_demo | CRITICAL | Unrestricted IAM permissions violate least privilege | Scope actions and resources |

**Expected total:** 3 findings. These are static example expectations, not independently captured test-run output.

## Review questions

1. Is SSH intentionally exposed for a disposable sandbox, or is it an unapproved exception?
2. Do bucket policies or other resource settings create actual data exposure? A disabled public-access block alone does not prove that a bucket is publicly readable.
3. Where and how is the IAM policy attached? The risky policy text does not establish effective permissions without attachment context.

## Results and limitations

The expected detections are based on inspecting synthetic input. No production scan or remediation verification has been completed. Next, add known-safe negative cases and compare output against an established IaC scanner.
