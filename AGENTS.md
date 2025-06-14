# AGENTS Instructions

This repository contains infrastructure and application code for a unified identity service built with Keycloak, plus two SaaS applications: **Bear Review** and **Mech-Exo**. Development follows the phased roadmap below. Follow these guidelines when contributing:

## General Guidelines

- Keep code well documented and modular.
- Run `pytest -q` before each commit (even if no tests are present) to ensure nothing is broken.
- Format Terraform files with `terraform fmt` and validate with `terraform validate` when applicable.
- Do not commit Terraform state files or other secrets.

## Roadmap Phases

### Phase T0 – Architecture Baseline & Environment Initialization
- Draw system architecture diagrams (components, data flows, network topology).
- Provision cloud infrastructure: VPC, subnets, security groups, S3/OSS backup bucket.
- Create IaC (Terraform or Pulumi) repo and automatically deploy the dev environment.
- Configure a bastion host with SSH key management and enable CloudTrail / Cloud Audit Logs.

### Phase T1 – Unified Identity Service MVP
- Use Docker Compose to run Keycloak with PostgreSQL using persistent volumes.
- Customize realm, client, and email verification templates; enable OIDC/PKCE.
- Implement JWT validation middleware for Node.js and Python with unit tests.
- Write the initial Terraform module for future auto-scaling deployments.

### Phase T2 – CI/CD & Monitoring Base
- Set up GitHub Actions pipelines for the frontend (PNPM) and backend (PyTest).
- Build multi-arch Docker images using Buildx and push to GHCR/ECR.
- Provide Helm charts / Kubernetes manifests and validate on a local kind cluster.
- Deploy Prometheus, Grafana, Loki for logging, plus a Slack alert webhook.

### Phase T3 – Bear Review Backend Service
- Design the database ER diagram for Review, Tag, Tomato, XP, Notification tables.
- Implement FastAPI CRUD endpoints and a Celery queue with Redis broker.
- Provide a pluggable notification layer supporting Sendgrid email and Expo push.
- Achieve ≥80% unit/integration test coverage and generate Swagger docs.

### Phase T4 – Bear Review Frontend SPA
- Create a React + Vite + Tailwind project skeleton with dark mode and i18n.
- Implement OIDC login, token refresh, and global React context management.
- Build the dashboard, review editor, and pomodoro timer using a WebWorker animation.
- Ensure Lighthouse score ≥90 and add Cypress E2E scripts.

### Phase T5 – Mech-Exo Data Pipeline & ML Service
- Implement data fetchers (yfinance/AlphaVantage) to a raw data bucket.
- Perform Pandas ETL and calculate indicators (EMA, RSI, F-Score).
- Train and save PyTorch models, deploying them via TorchServe.
- Provide a backtesting engine using vectorbt and cache results in RedisGraph.

### Phase T6 – Mech-Exo Frontend Dashboard
- Build a Next.js SSR dashboard with Recharts candlestick components and dark theme toggle.
- Add custom chart tooltips and strategy parameter forms.
- Provide watchlist management with WebSocket market data pushes.
- Include Playwright visual regression tests.

### Phase T7 – Scaling & Security Hardening
- Deploy Keycloak on Kubernetes with the Keycloak Operator (2 replicas, external RDS).
- Use Nginx Ingress with WAF, rate limiting, and OIDC header injection.
- Scan Docker images with Trivy and monitor dependencies with Snyk.
- Perform k6 load testing targeting P95 latency <250ms and failure rate <0.1%.

### Phase T8 – Disaster Recovery, Observability & Release
- Implement blue-green deployment scripts supporting fast rollback.
- Schedule daily DB snapshots with S3 cross-region backups; practice restores in ≤30min.
- Create Grafana dashboards for basic monitoring, app metrics, and business KPIs.
- Enable CDN acceleration for frontend assets and Brotli compression.

### Phase T9 – Production Launch & Ops Handover
- Write an SRE runbook with alert levels and on-call schedules.
- Generate developer docs and API SDK via Confluence/MkDocs.
- Perform a gradual rollout from canary to full release; tag version v1.0.0.
- Conduct a retrospective and plan the next roadmap.

