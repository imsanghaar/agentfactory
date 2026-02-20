### Core Concept
NetworkPolicies enforce pod-level traffic controls so only approved ingress/egress paths are allowed, containing blast radius for compromised workloads.

### Key Mental Models
- **Default deny**: Start closed; explicitly allow required sources/destinations.
- **Selectors + policy types**: Pod/namespace selectors paired with `ingress`/`egress` rules define scope.
- **Defense in depth**: Layer NetworkPolicies with RBAC and mTLS to block lateral movement.

### Critical Patterns
- Create namespace-scoped policies that allow only gateway → app ingress and app → dependencies egress.
- Use labels consistently on pods/namespaces; avoid broad `0.0.0.0/0` or empty selectors.
- Test reachability with `kubectl exec`/`curl` and Cilium/Calico policy verdict tools.

### Common Mistakes
- Forgetting a default deny baseline, leaving pods wide open.
- Relying on DNS names without matching IP blocks when the CNI lacks egress DNS support.
- Missing egress rules for needed services (DNS, metrics), causing hidden outages.

### Connections
- **Builds on**: RBAC and 4C model.
- **Leads to**: Secrets hardening, PSS, and Dapr security where traffic policy underpins trust.
