# Keycloak HA Runbook

This runbook explains how to verify high availability for the Keycloak deployment.

## Pod Failure

1. Delete one of the Keycloak pods:
   ```bash
   kubectl delete pod -l app=keycloak -n keycloak --force
   ```
2. Ensure a replacement pod becomes Ready within 60 seconds.
3. Verify sessions remain active by accessing the application.

## RDS Failover

1. Trigger an RDS failover from the AWS console or CLI.
2. Monitor Keycloak logs for reconnection messages. Average login latency should remain below 5 seconds.

## Alerts

Prometheus alerts `KeycloakUnavailable` should remain below 1 firing instance. Investigate any alert immediately using `kubectl logs` and the RDS monitoring dashboard.
