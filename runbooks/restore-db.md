# Database Restore Drill Runbook

This runbook describes how to test database point-in-time recovery.

1. Execute the restore drill script:
   ```bash
   SRC_DB=keycloak-prod DRILL_BUCKET=my-drills ./scripts/restore-drill.sh
   ```
2. Wait for the script to report completion.
3. Inspect the uploaded log in the S3 bucket for duration and status.
4. Terminate the temporary database once verified:
   ```bash
   aws rds delete-db-instance --db-instance-identifier <TMP_DB> --skip-final-snapshot
   ```
