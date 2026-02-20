### Core Concept
Manage secrets with external stores and least-privilege access—never bake secrets into images or plain manifests.

### Key Mental Models
- **Out-of-cluster sources**: Use external secret managers (ESO/CSI) instead of Kubernetes Secrets as system of record.
- **Scoped access**: Bind secrets to specific ServiceAccounts/Namespaces; audit and rotate regularly.
- **Runtime injection**: Inject via env/volumes at deploy time; avoid committing values.

### Critical Patterns
- Configure External Secrets Operator (or CSI driver) to pull from cloud stores and create namespaced secrets.
- Restrict who can read secrets via RBAC and component scopes; mount secrets only where needed.
- Enable encryption at rest and set short TTLs/rotation policies; avoid logging secret values.

### Common Mistakes
- Storing secrets in Git or embedding in images.
- Broad RBAC allowing any pod to read secrets in a namespace.
- Failing to rotate credentials or to revoke unused secrets.

### Connections
- **Builds on**: RBAC and NetworkPolicies.
- **Leads to**: Pod Security Standards, supply chain scanning, and Dapr security where secret scopes matter.
