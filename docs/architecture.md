# System Architecture

```mermaid
graph TD
  subgraph Networking
    VPC(VPC)
    Public[Public Subnet]
    Private[Private Subnet]
  end

  subgraph Clients
    Browser(Browser)
    Mobile(Mobile App)
  end

  subgraph Services
    KC(Keycloak)
    DB[(Postgres)]
    S3[(S3 Backup Bucket)]
    Bastion[Bastion Host]
  end

  Browser-->|OIDC/HTTPS|KC
  Mobile-->|OIDC/HTTPS|KC
  KC-->|JDBC|DB
  KC-->|Backups|S3
  Bastion-->|SSH|KC
  Bastion-->|SSH|DB

  VPC-->Public
  VPC-->Private
  Bastion-->|Public IP|Public
  KC-->|Private IP|Private
  DB-->|Private IP|Private
```

This diagram outlines the initial infrastructure for the authentication service. Traffic from clients reaches Keycloak through public endpoints, while the database and backups remain within private subnets. A bastion host manages SSH access. CloudTrail is enabled to audit API calls.
