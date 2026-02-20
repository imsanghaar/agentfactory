### Core Concept
Actor security combines platform controls (mTLS, auth, network policies) with least-privilege state access and input validation to protect stateful identities.

### Key Mental Models
- **mTLS everywhere**: Sidecar-to-sidecar traffic is authenticated/encrypted; service invocation honors app identity.
- **Least privilege**: Limit what actors can reach (components, APIs) and what callers can invoke.
- **Defense in depth**: NetworkPolicy, RBAC, and component scopes all enforce boundaries.

### Critical Patterns
- Enable Dapr mTLS and component scoping so actors access only needed state/pubsub.
- Apply NetworkPolicies around actor apps and gateways; restrict ingress/egress.
- Validate/authorize inputs at actor boundaries; avoid trusting caller data.
- Protect secrets via external stores and rotate credentials used by actors.

### Common Mistakes
- Leaving component scopes open, allowing any app/actor to use sensitive stores.
- Relying solely on Dapr mTLS without NetworkPolicies, exposing lateral movement risks.
- Skipping input validation, leading to stored XSS/injection in actor state.

### Connections
- **Builds on**: Namespaced actors and security model from Chapter 58.
- **Leads to**: Capstone stateful agent and final skill refinement.
