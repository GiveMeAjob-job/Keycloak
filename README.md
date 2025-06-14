# Keycloak Identity Service

This repository hosts the configuration and infrastructure files to run a Keycloak instance that will serve as the unified authentication service for Bear_Review and Mech-Exo.

## Getting Started

1. Install Docker and Docker Compose.
2. Run `docker compose up -d` in this directory.
3. Open `http://localhost:8080/` and log in with user **admin** / **admin**.

The development setup uses a Postgres container to persist data. The `keycloak/realm-export.json` file contains a minimal realm that will be imported on startup.

## Project Overview

This Keycloak instance is planned to integrate with multiple SaaS applications. For more details see the project plan in the repository history.

## Architecture

The [architecture diagram](docs/architecture.md) illustrates the main components and network layout used in the development environment.

## Infrastructure Deployment

Terraform files under [`infra/`](infra/) provision a VPC, subnets, a bastion host, security groups, S3 buckets for backups and CloudTrail logging. Refer to `infra/README.md` for usage instructions.
