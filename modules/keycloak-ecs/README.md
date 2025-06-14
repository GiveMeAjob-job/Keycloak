# keycloak-ecs Terraform Module

This module deploys a Keycloak service on ECS Fargate behind an Application Load Balancer.

## Inputs
- `cpu`/`memory`: Fargate task sizing
- `desired_count`: number of tasks
- `db_password_ssm_key`: SSM parameter name storing the DB password
- `execution_role`: IAM role for the task
- `image`: container image
- `admin_password`: admin password
- `subnets`: list of ALB subnets

## Outputs
- `alb_dns`: DNS name of the ALB
- `keycloak_admin_url`: Admin console URL
