# Operability Guide

This document describes operational procedures for disaster recovery,
observability and releases.

## Deployment Workflow
Blue-green deployments are performed using the `bluegreen_deploy.sh`
script which gradually shifts traffic using Nginx canary annotations.
Rollbacks use `make rollback` wrapping `helm rollback`.

## Backup Strategy
RDS instances are configured with automated snapshots retained for
seven days and copied cross-region via AWS Backup plans.

## Restore Drills
Monthly restore drills run `restore-drill.sh` to create a temporary
instance from the latest snapshot and validate application health.

## Monitoring and Alerts
Grafana dashboards located in `monitoring/grafana/provisioning/dashboards/`
track business KPIs along with system metrics. Alerts are routed via
Alertmanager to PagerDuty and Slack based on severity. Service level
objectives include HTTP success rate above 99.9% and login latency
below 250ms.

## CDN & Compression
Static assets are served through CloudFront with Brotli compression
enabled via Lambda@Edge.
