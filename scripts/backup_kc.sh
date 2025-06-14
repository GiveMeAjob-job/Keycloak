#!/bin/bash
set -e
BACKUP_DIR="$(dirname "$0")/../backups"
mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
docker compose -f docker-compose.keycloak.yml exec -T kc-db pg_dump -U keycloak keycloak > "$BACKUP_DIR/keycloak-$TIMESTAMP.sql"
