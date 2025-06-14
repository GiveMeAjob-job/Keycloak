# Blue-Green Deployment Runbook

This runbook explains how to perform a blue-green deployment and rollback.

## Deployment
1. Run the deployment script specifying the new color:
   ```bash
   COLOR=green ./scripts/bluegreen_deploy.sh
   ```
2. Monitor the rollout with `kubectl rollout status`.

## Rollback
1. Determine the previous revision with `helm history keycloak`.
2. Execute:
   ```bash
   make rollback ENV=prod REVISION=<REV>
   ```
3. Verify traffic is restored.
