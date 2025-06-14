# Scaling and Security Hardening

This document covers the high availability setup for Keycloak and the security controls deployed in phase T7.

## Keycloak High Availability

Two replicas of Keycloak run under the Keycloak Operator. Sessions are stored in the embedded Infinispan cache and data is persisted to an external Postgres RDS instance. The service monitor is enabled for Prometheus scraping.

```yaml
spec:
  instances: 2
  enableServiceMonitor: true
  cache:
    stack: infinispan
    type: embedded
```

## Nginx Ingress WAF

The ingress controller is configured with ModSecurity and the OWASP CRS. Requests per IP are limited to **20 r/s** via the ConfigMap value `limit-req`. Authentication headers `X-Auth-User` and `X-Auth-Email` are passed to upstream services.

## OIDC Header Injection

`oauth2-proxy` is deployed as a sidecar authentication layer. Upstream applications read `X-User-Id` and `X-Role` headers after authentication.

## Image and Dependency Scanning

- **Trivy** scans container images and blocks releases with HIGH or CRITICAL findings.
- **Snyk** monitors JavaScript and Python dependencies with a GitHub Action gate.

## Load Testing

k6 scripts under `k6/scripts/` ensure the 95th percentile latency stays below 250&nbsp;ms and the failure rate is under 0.1%.
