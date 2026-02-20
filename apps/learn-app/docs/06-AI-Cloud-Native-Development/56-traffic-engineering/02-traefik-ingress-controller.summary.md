### Core Concept
Traefik provides a simpler ingress experience with IngressRoute CRDs and Middleware resources that replace Ingress annotations with structured YAML, offering fast time-to-first-route while preparing you for Gateway API's more powerful abstractions.

### Key Mental Models
- **EntryPoints -> Routers -> Middlewares -> Services**: Request flow through Traefik's four components
- **IngressRoute CRD**: Cleaner syntax than Ingress annotations with explicit match rules and middleware chains
- **Middleware Composition**: Rate limiting, path stripping, and header modification as chainable components
- **Traefik vs Gateway API Trade-off**: Faster setup but vendor lock-in vs. portable configurations

### Critical Patterns
- Install Traefik with Helm: `helm install traefik traefik/traefik -n traefik --create-namespace`
- Match rules use expression syntax: `PathPrefix('/api/v1/tasks') && Method('POST')`
- Middlewares attach to routes in order: rate-limit -> strip-prefix -> headers
- Enable dashboard for route debugging: `helm upgrade --set dashboard.enabled=true`

### AI Collaboration Keys
- Generate IngressRoute with specific match expressions
- Design Middleware chains for request transformation
- Compare Traefik configuration to equivalent Gateway API

### Common Mistakes
- Using Traefik CRDs in production when Gateway API portability is needed
- Forgetting to chain Middlewares in correct order (rate limit before path strip)
- Not enabling dashboard for debugging routing issues

### Connections
- **Builds on**: Lesson 1 (Ingress Fundamentals) understanding of routing concepts
- **Leads to**: Lesson 3 (Gateway API - The New Standard) for portable, role-separated routing
