### Core Concept
Namespaced actors scope identities and routing by namespace, preventing collisions across environments or tenants while keeping actor APIs consistent.

### Key Mental Models
- **Namespace as boundary**: ActorId uniqueness is enforced per namespace, enabling multi-tenant or multi-env separation.
- **Routing + isolation**: Requests resolve within the specified namespace; policies and components can differ per namespace.
- **Config-driven**: Namespace selection is controlled via annotations/config, not code changes.

### Critical Patterns
- Configure Dapr to enable namespaced actors and set namespace annotations on deployments.
- Use namespace-aware ActorIds or routing when invoking to target the correct tenant/env.
- Align state stores and components with namespaces to keep data isolated.
- Monitor per-namespace actor metrics to detect noisy-neighbor issues.

### Common Mistakes
- Reusing global actor IDs without namespaces, causing collisions between envs.
- Pointing multiple namespaces to the same state store unintentionally, breaking isolation.
- Forgetting to propagate namespace in invocation calls, leading to “actor not found” errors.

### Connections
- **Builds on**: Multi-app workflows and actor patterns.
- **Leads to**: Actor security and capstone, where isolation and tenancy are enforced.
