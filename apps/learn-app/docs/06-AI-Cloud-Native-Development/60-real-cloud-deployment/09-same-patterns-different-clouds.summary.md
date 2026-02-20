### Core Concept
Cloud deployment patterns are portable: the same specs for networking, security, secrets, and observability apply across providers with provider-specific tweaks.

### Key Mental Models
- **Abstractions first**: Keep manifests/IaC modular; swap provider settings (LB, DNS, storage) per cloud.
- **Consistency**: Enforce the same security/observability standards everywhere.
- **Config, not code changes**: Adjust values/overlays, not core app logic.

### Critical Patterns
- Parameterize region, storage class, LB/DNS, and credentials per provider.
- Use provider-agnostic tools (Helm, ArgoCD, Terraform modules) with cloud-specific inputs.
- Maintain parity checklists to ensure features (TLS, RBAC, NetworkPolicy, secrets) are present in each environment.

### Common Mistakes
- Hardcoding provider endpoints/IDs in manifests.
- Letting standards drift between clouds, creating inconsistent security or reliability.
- Assuming managed services behave identically without validating limits and SLAs.

### Connections
- **Builds on**: Production checklist verification and provider-specific setups.
- **Leads to**: Final capstone deployment across target clouds.
