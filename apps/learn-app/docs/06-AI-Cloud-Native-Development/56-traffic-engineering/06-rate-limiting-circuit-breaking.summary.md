### Core Concept
BackendTrafficPolicy protects services from abuse and overload through rate limiting (per-user quotas), circuit breakers (connection limits), and retry policies, with local rate limiting per proxy instance or global via Redis.

### Key Mental Models
- **Local vs Global Rate Limiting**: Local limits per proxy (3 replicas x 100 = 300 total); Global uses Redis for exact cluster-wide limits
- **Per-User Descriptors**: Header-based `clientSelectors` give each user their own quota bucket
- **Circuit Breaker States**: Closed (normal) -> Open (503 immediately) -> Recovery (probing)
- **Exponential Backoff**: Increasing delays between retries (100ms, 200ms, 400ms) to avoid overwhelming recovering services

### Critical Patterns
- Use `clientSelectors` with `headers` for per-user limits
- Use `invert: true` to match requests WITHOUT a header (anonymous users)
- Set circuit breaker `maxParallelRequests` based on backend capacity
- Configure retries only for idempotent operations and retriable status codes (502, 503, 504)

### AI Collaboration Keys
- Generate BackendTrafficPolicy with tiered rate limits (authenticated vs anonymous)
- Design circuit breaker thresholds based on backend capacity
- Configure retry policy with appropriate backoff intervals

### Common Mistakes
- Using global rate limiting without Redis backend configured
- Retrying non-idempotent POST requests (may create duplicates)
- Setting circuit breaker too aggressive for normal traffic patterns

### Connections
- **Builds on**: Lesson 5 (HTTPRoute) defining routes to attach policies
- **Leads to**: Lesson 7 (TLS Termination) for encrypted traffic
