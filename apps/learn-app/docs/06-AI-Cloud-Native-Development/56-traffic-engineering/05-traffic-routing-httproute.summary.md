### Core Concept
HTTPRoute defines sophisticated routing logic with path matching (Exact, PathPrefix, RegularExpression), header matching, query parameter matching, and traffic weights for canary deployments, making it the application developer's primary resource.

### Key Mental Models
- **Match Specificity**: Exact > RegularExpression > PathPrefix; order rules from most to least specific
- **Header-Based Versioning**: Route `x-version: 2` to v2 backend without changing URLs
- **Traffic Weights**: Relative weights (90/10) split traffic for canary deployments
- **Request Mirroring**: Copy traffic to shadow backend for testing; responses discarded

### Critical Patterns
- Use PathPrefix for API namespace routing (`/api/v1/`)
- Use Exact for specific endpoints (`/health`)
- Use header matching for API versioning without URL changes
- Use weights for gradual rollouts: 95/5 -> 75/25 -> 50/50 -> 100/0

### AI Collaboration Keys
- Generate multi-service HTTPRoute with different path prefixes
- Design header-based routing for beta users
- Configure canary deployment with progressive weight adjustments

### Common Mistakes
- Placing PathPrefix rule before Exact rule (general catches all, specific never matches)
- Forgetting weights must be relative (9/1 = 90/10 split)
- Using request mirroring for non-idempotent operations

### Connections
- **Builds on**: Lesson 4 (Envoy Gateway Setup) with running controller
- **Leads to**: Lesson 6 (Rate Limiting & Circuit Breaking) for traffic policy controls
