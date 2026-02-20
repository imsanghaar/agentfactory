### Core Concept
Harden Dapr with mTLS, scoped components, and access controls so sidecars and apps communicate securely and only with intended backends.

### Key Mental Models
- **mTLS by default**: Sidecar-to-sidecar trust is enforced via certificates.
- **Component scoping**: Limit which apps/actors can use specific state stores, pub/sub, and bindings.
- **Network + identity layers**: Combine NetworkPolicies with Dapr app-ids and tokens for defense in depth.

### Critical Patterns
- Enable/verify Dapr mTLS; rotate certs on schedule.
- Set `scopes` on components and secure secrets via external stores; avoid broad access.
- Require app tokens/sidecar auth for service invocation; lock down allowed methods/routes.
- Pair with NetworkPolicies to restrict ingress/egress to sidecars and control plane.

### Common Mistakes
- Leaving components unscoped, letting any app read/write sensitive stores.
- Assuming mTLS alone is enough without network isolation.
- Exposing Dapr HTTP ports publicly or skipping token validation on invocation.

### Connections
- **Builds on**: NetworkPolicies, secrets, PSS, and supply-chain controls.
- **Leads to**: Capstone secure Task API and actor security patterns.
