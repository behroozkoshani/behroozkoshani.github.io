# Architecture and Data Flow

```text
Isolated Terraform environment
          |
          | terraform plan -out=plan.out
          | terraform show -json plan.out
          v
   Terraform plan JSON
          |
          v
 cloud_security.py --json
          |
     detection rules
   /       |        \
 Public   S3 block   IAM wildcard
 admin    controls   permissions
 ports
   \       |        /
          v
    JSON findings / CLI
          |
          v
 analyst review -> update Terraform -> repeat scan
```

**Trust boundaries:** The parser runs locally and does not contact AWS. Treat the input JSON as sensitive and validate results independently. A 'no findings' response only means none of the **implemented patterns** were matched. The sample input is hand-authored and is not a deployed environment.

**Selected checks:** `PUBLIC_ADMIN_PORT`, `S3_PUBLIC_ACCESS_BLOCK_DISABLED`, `IAM_ALLOW_ALL_ACTIONS_RESOURCES`.

**Trade-offs:** A small explainable detector makes evaluation easy but has narrow coverage. For production programs use maintained scanning engines and cloud-native evidence sources in addition to configuration reviews.
