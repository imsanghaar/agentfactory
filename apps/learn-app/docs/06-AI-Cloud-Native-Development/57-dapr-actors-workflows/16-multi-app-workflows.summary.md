### Core Concept
Multi-app workflows coordinate across services and clusters, using standardized workflow definitions and activities that call out to external APIs or other Dapr apps.

### Key Mental Models
- **Cross-app orchestration**: Workflows act as the conductor; services remain focused on domain logic.
- **Connectivity and identity**: Securely address remote apps with app-ids, auth, and network policies.
- **Failure isolation**: External calls can fail; retries/timeouts and fallbacks are mandatory.

### Critical Patterns
- Design activities that call remote services via service invocation or HTTP with proper auth.
- Use configuration to route to environments (dev/stage/prod) without changing workflow code.
- Handle partial availability with circuit breakers/backoff and compensating steps.
- Capture correlation IDs and propagate tracing across app boundaries.

### Common Mistakes
- Hardcoding endpoints or credentials inside workflows, breaking portability and security.
- Ignoring latency/timeout budgets when orchestrating many services.
- Missing auth scopes, causing unauthorized calls or over-privileged access.

### Connections
- **Builds on**: Combining actors/workflows.
- **Leads to**: Namespaced actors and security considerations for distributed deployments.
