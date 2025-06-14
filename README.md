# Keycloak Identity Service

This repository hosts the configuration and infrastructure files to run a Keycloak instance that will serve as the unified authentication service for Bear_Review and Mech-Exo.

## Getting Started

1. Install Docker and Docker Compose.
2. Execute `./scripts/kc-up.sh` to start the stack.
3. Open `http://localhost:8080/` and log in with user **admin** / **admin**.

The development setup uses a Postgres container to persist data. The `keycloak/realm-export.json` file contains a minimal realm that will be imported on startup.
Backups can be created with `./scripts/backup_kc.sh` which dumps the database to `./backups/`.

## Project Overview

This Keycloak instance is planned to integrate with multiple SaaS applications. For more details see the project plan in the repository history.
Documentation for the identity service is available at [docs/identity-service.md](docs/identity-service.md).

## Architecture

The [architecture diagram](docs/architecture.md) illustrates the main components and network layout used in the development environment. A Draw.io source is also provided at `docs/system-arch-v1.drawio` for further editing.


## Infrastructure Deployment

Terraform files under [`infra/`](infra/) provision a VPC, subnets, a bastion host, security groups, S3 buckets for backups and CloudTrail logging. Refer to `infra/README.md` for usage instructions.

## Initialization

1. Enable MFA on the AWS root account and create separate `dev` and `prod` accounts within your organization.
2. Configure billing alarms to avoid unexpected charges.
3. Prepare an S3 bucket and DynamoDB table for the Terraform state backend.
4. Log in via the AWS CLI (MFA session) and run `terraform init` inside [`infra/`](infra/) to set up the remote state.
5. Apply the configuration with `terraform apply`.

