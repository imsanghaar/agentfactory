### Core Concept
Traffic splitting divides incoming requests between multiple backend services using HTTPRoute weight fields, enabling canary (gradual rollout), blue-green (instant switch), and A/B testing (header-based routing) deployment patterns for risk reduction.

### Key Mental Models
- **Relative Weights**: Weights are proportional (90/10 = 9/1); total does not need to equal 100
- **Canary Progressive Delivery**: Start at 5%, increase to 25%, 50%, 100% as confidence builds
- **Blue-Green Instant Switch**: Both environments running; flip weights 100/0 to 0/100 for immediate cutover or rollback
- **Header-Based A/B Testing**: Deterministic routing where x-beta-user header always reaches test version, unlike random canary percentage

### Critical Patterns
- Use canary for gradual feature rollouts with progressive weight increases (5% -> 25% -> 50% -> 100%)
- Use blue-green for database migrations or breaking API changes requiring instant switch
- Combine patterns: protect premium users with header matching while canary-testing standard users
- Monitor error rates per version using `kubectl logs -l version=canary` to detect issues

### AI Collaboration Keys
- Generate HTTPRoute with weighted backendRefs for canary deployment
- Design header-based routing for beta user programs
- Create rollback commands as kubectl patch for instant weight reversal

### Common Mistakes
- Forgetting weights are relative (3/1 = 75/25, not 3% and 1%)
- Not monitoring error rates between versions during canary
- Using blue-green when gradual rollout would reduce risk

### Connections
- **Builds on**: Lesson 7 (TLS Termination) for complete traffic protection
- **Leads to**: Lesson 9 (Autoscaling with HPA, VPA & KEDA) for capacity management
