# CI/CD and Monitoring

This document outlines the GitHub Actions workflows and Kubernetes monitoring stack.

## Workflows

- **frontend.yml** – installs dependencies with PNPM, runs ESLint and Vitest and caches the build output.
- **backend.yml** – installs the Python package and executes PyTest with coverage. The coverage.xml artifact can be used by reporting tools.
- **docker.yml** – builds multi-architecture images for Bear Review and Mech‑Exo using Buildx. Images are pushed to GHCR and mirrored to ECR.
- **kind-test** – provisions a local kind cluster, deploys the manifests under `k8s/dev/` and verifies the `/health` endpoint.

The Helm charts under `charts/` are linted and packaged via `make helm-package` and published to `oci://ghcr.io/org/charts`.

Prometheus, Loki and Grafana can be installed with:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack -f monitoring/prom-stack-values.yaml
helm install loki grafana/loki-stack --values monitoring/loki-values.yaml --set promtail.enabled=true
```

## Troubleshooting

- Ensure PNPM and Python versions match the project configuration.
- If the Docker build fails, check the BuildKit secret values for `PIP_INDEX_URL` and `NPM_TOKEN`.
- Use `make kind-test` locally to reproduce the Kubernetes deployment step.
