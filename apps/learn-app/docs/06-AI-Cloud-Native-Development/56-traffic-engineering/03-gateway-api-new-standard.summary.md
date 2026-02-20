### Core Concept
Gateway API is the official Kubernetes standard replacing Ingress, organizing traffic configuration into three tiers (GatewayClass, Gateway, HTTPRoute) that enable role separation, RBAC granularity, and vendor portability without annotation rewrites.

### Key Mental Models
- **Three-Tier Resource Model**: Infrastructure (GatewayClass) -> Platform (Gateway) -> Application (HTTPRoute)
- **Role Separation**: Cluster admins own GatewayClass, platform teams own Gateway, developers own HTTPRoute
- **Portability**: Switching controllers requires changing only `gatewayClassName`, not routes
- **Rich Status Reporting**: Detailed conditions show Accepted, Programmed, and attached route counts

### Critical Patterns
- GatewayClass is cluster-scoped; usually created by Helm chart, not manually
- Gateway defines listeners (ports, protocols, TLS); namespace-scoped
- HTTPRoute uses `parentRefs` to attach to Gateway, matches on path/headers/query
- ReferenceGrant allows cross-namespace routing (target namespace grants access)

### AI Collaboration Keys
- Generate Gateway + HTTPRoute from service requirements
- Map team structure to Gateway API role separation
- Create ReferenceGrant for shared services in different namespaces

### Common Mistakes
- Creating GatewayClass manually instead of letting Helm chart handle it
- Missing ReferenceGrant when routing to services in other namespaces
- Using annotations instead of native features (traffic splitting, header matching)

### Connections
- **Builds on**: Lesson 2 (Traefik) concepts with Traefik-specific implementation
- **Leads to**: Lesson 4 (Envoy Gateway Setup) for installing the controller that implements Gateway API
