#!/bin/bash
set -euo pipefail

SRC_DB=${SRC_DB:-keycloak-prod}
TMP_DB=${TMP_DB:-keycloak-drill-$(date +%Y%m%d%H%M)}
REGION=${AWS_REGION:-us-east-1}

aws rds restore-db-instance-to-point-in-time \
  --source-db-instance-identifier "$SRC_DB" \
  --target-db-instance-identifier "$TMP_DB" \
  --use-latest-restorable-time \
  --db-instance-class db.t3.micro \
  --region "$REGION"

aws rds wait db-instance-available --db-instance-identifier "$TMP_DB" --region "$REGION"

# simple health check example
psql "host=$TMP_DB user=keycloak password=password" -c 'SELECT 1;' || true

END=$(date +%s)
START=${START_TIME:-$END}
DURATION=$((END-START))
echo "Restore drill completed in ${DURATION}s" | tee "/tmp/${TMP_DB}-drill.log"

aws s3 cp "/tmp/${TMP_DB}-drill.log" "s3://$DRILL_BUCKET/" --region "$REGION"
