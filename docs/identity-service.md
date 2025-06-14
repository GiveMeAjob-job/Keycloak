# Identity Service

This document describes the local Keycloak setup and client configuration.

## Installation

```bash
./scripts/kc-up.sh
```

Access `http://localhost:8080` with credentials `admin/admin`.

## Export & Backup

To export the realm or create a backup run:

```bash
./scripts/backup_kc.sh
```

Backups are stored in `./backups/`.

## Realm Structure

- Realm: `unified-apps-realm` with email verification enabled
- Clients:
  - `bear-review-spa` (public)
  - `mech-exo-api` (confidential)

## Client Registration

Register new clients via the admin console or import an updated `realm-export.json`.
