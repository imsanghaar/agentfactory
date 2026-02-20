### Core Concept
Expose services securely with cloud load balancers and DNS, wiring ingress endpoints to stable domain names with TLS.

### Key Mental Models
- **Ingress chain**: Service → LB → DNS → TLS; each must be configured and secured.
- **Separation of concerns**: LB handles traffic, DNS resolves names, certs handle trust.
- **Idempotent setup**: Manage via IaC/Helm to avoid drift.

### Critical Patterns
- Provision cloud LBs (or ingress controllers) and point DNS records to LB addresses.
- Obtain/automate TLS certificates (Let’s Encrypt/cert-manager); enforce HTTPS.
- Restrict LB access (firewalls/allowed CIDRs) and ensure health checks align with app readiness.

### Common Mistakes
- Leaving HTTP open or misconfigured TLS leading to mixed content/insecure access.
- Manual DNS/LB changes without IaC, causing drift and outages.
- Wrong health checks/ports causing LB flaps.

### Connections
- **Builds on**: Cluster provisioning.
- **Leads to**: Deploying Task API with secrets/config in cloud.
