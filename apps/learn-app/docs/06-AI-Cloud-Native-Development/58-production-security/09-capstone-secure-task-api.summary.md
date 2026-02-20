### Core Concept
The capstone secures the Task API end to end by applying all Chapter 58 controls—RBAC, NetworkPolicies, PSS, secrets, supply chain, Dapr security, and compliance evidence—into a production-ready deployment.

### Key Mental Models
- **Defense-in-depth integration**: Multiple layers must be enabled together; gaps in one layer weaken all.
- **Validate and prove**: Security isn’t done until controls are tested and evidence captured.
- **Operational acceptance**: Security checks become part of deployment criteria (SLA/SLO + security gates).

### Critical Patterns
- Deploy Task API with dedicated SA, least-privilege Roles/Bindings, default-deny NetworkPolicies, and PSS enforcement.
- Use external secrets + scoped components, signed/scanned images, and Dapr mTLS with component scopes.
- Add compliance artifacts: audit logs enabled, control matrix updated, exceptions tracked.
- Run verification: `kubectl auth can-i`, policy dry-runs, admission tests, and penetration/negative tests before sign-off.

### Common Mistakes
- Treating capstone as documentation-only without enforcing policies in the cluster.
- Skipping verification of mTLS/scopes or leaving default service accounts/ingress open.
- Ignoring evidence collection, leaving compliance gaps despite controls.

### Connections
- **Builds on**: All Chapter 58 lessons.
- **Leads to**: Operational resilience and cost/disaster readiness in Chapter 59, and real cloud deployment in Chapter 60.
