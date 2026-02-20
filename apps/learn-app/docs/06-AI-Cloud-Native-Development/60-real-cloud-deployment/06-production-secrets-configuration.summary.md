### Core Concept
Configure production secrets securely in the cloud using external stores and scoped access, ensuring the Task API and supporting services only receive what they need.

### Key Mental Models
- **Externalize and scope**: Secrets live in managers (not manifests) with least-privilege access.
- **Separation by env**: Different namespaces/projects get distinct secrets and credentials.
- **Secure injection**: Deliver secrets at deploy time via CSI/ESO with auditability.

### Critical Patterns
- Set up External Secrets/CSI to pull from cloud secret stores; map to app namespaces.
- Lock down access with RBAC/service identities and component scopes.
- Rotate and audit secrets; avoid logging or shipping them with images.

### Common Mistakes
- Sharing secrets across environments or storing them in Git/Helm values.
- Over-permissive secret access for service accounts.
- Failing to rotate credentials or test secret updates in running pods.

### Connections
- **Builds on**: DO cluster/app deployment; security practices from Chapter 58.
- **Leads to**: Checklist verification and capstone production release.
