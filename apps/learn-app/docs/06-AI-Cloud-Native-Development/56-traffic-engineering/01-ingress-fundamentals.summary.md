### Core Concept
Kubernetes creates a private network invisible to the outside world; understanding the progression from ClusterIP to NodePort to LoadBalancer to Ingress reveals why Gateway API was created to replace Ingress's annotation chaos and lack of role separation.

### Key Mental Models
- **External Access Problem**: ClusterIP addresses exist only inside the cluster; external browsers cannot reach internal IPs
- **Service Type Progression**: ClusterIP (internal) -> NodePort (ports 30000-32767) -> LoadBalancer (cloud IPs) -> Ingress (L7 routing)
- **Annotation Chaos**: Every Ingress controller uses different annotation syntax for rate limiting, timeouts, and TLS
- **Gateway API Solution**: Three-tier resources (GatewayClass, Gateway, HTTPRoute) enabling role separation and portability

### Critical Patterns
- Use ClusterIP for internal services only (databases, caches)
- Use NodePort for development/testing quick access
- Use LoadBalancer for single-service cloud deployments
- Use Gateway API for multiple services with complex routing needs

### AI Collaboration Keys
- Ask AI to map your scenario to the appropriate Service type
- Use AI to compare annotation syntax between different Ingress controllers
- Generate the decision tree for choosing between Ingress and Gateway API

### Common Mistakes
- Using LoadBalancer per service (expensive: 10 services = 10 monthly charges)
- Assuming port-forward is a production solution (stops when terminal closes)
- Rewriting all annotations when switching Ingress controllers (vendor lock-in)

### Connections
- **Builds on**: Kubernetes Service concepts from Chapter 50
- **Leads to**: Lesson 2 (Traefik Ingress Controller) for simpler routing before Gateway API complexity
