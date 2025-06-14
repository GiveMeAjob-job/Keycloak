# Infrastructure Setup

This directory contains Terraform code used to provision the development environment for the Keycloak identity service.

## Prerequisites

- Terraform >= 1.5
- An AWS account with permissions to create VPCs, EC2 instances, S3 buckets and CloudTrail

## Usage

1. Copy `terraform.tfvars.example` to `terraform.tfvars` and fill in the required variables.
2. Run `terraform init` to download providers.
3. Execute `terraform apply` to create the resources.

The infrastructure includes:

- A new VPC with public and private subnets
- A bastion EC2 instance with your provided SSH key
- Security groups for Keycloak and SSH access
- S3 buckets for backups and CloudTrail logs
- A CloudTrail trail for auditing API calls

Destroy the environment with `terraform destroy` when finished.
