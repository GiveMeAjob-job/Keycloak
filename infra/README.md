# Infrastructure Setup

This directory contains Terraform code used to provision the development environment for the Keycloak identity service.

## Prerequisites

- Terraform >= 1.5
- An AWS account with permissions to create VPCs, EC2 instances, S3 buckets and CloudTrail

## Usage

1. Copy `terraform.tfvars.example` to `terraform.tfvars` and fill in the required variables, including the S3 bucket and DynamoDB table used for remote state.
2. Run `terraform init` to download providers and configure the backend.



The infrastructure includes:

- A new VPC with three public and three private subnets across multiple AZs
- A NAT gateway for outbound internet access
- A bastion EC2 instance (managed via Session Manager) with your provided SSH key
- Security groups for Keycloak, Kubernetes workloads and the database
- S3 buckets for backups and CloudTrail logs (versioned and encrypted)
- CloudTrail and GuardDuty for auditing API calls and threats
- A placeholder EKS cluster with zero nodes
rail for auditing API calls

Destroy the environment with `terraform destroy` when finished.
