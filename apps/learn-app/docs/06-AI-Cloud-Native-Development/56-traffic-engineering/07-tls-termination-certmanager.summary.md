### Core Concept
cert-manager automates the TLS certificate lifecycle using ACME protocol to obtain certificates from Let's Encrypt, storing them in Kubernetes Secrets that Envoy Gateway uses for TLS termination without manual renewal.

### Key Mental Models
- **ACME HTTP-01 Challenge**: cert-manager creates temporary HTTPRoute serving token; Let's Encrypt verifies domain control
- **ClusterIssuer**: Cluster-scoped resource defining certificate authority and solver configuration
- **Certificate Lifecycle**: Gateway annotation triggers Certificate -> CertificateRequest -> Order -> Challenge -> Secret
- **Staging vs Production**: Always test with staging endpoint first; production has strict rate limits (50 certs/week/domain)

### Critical Patterns
- Install cert-manager with `--set config.enableGatewayAPI=true` for Gateway integration
- Create ClusterIssuer with `gatewayHTTPRoute` solver pointing to your Gateway
- Add `cert-manager.io/cluster-issuer` annotation to Gateway with HTTPS listener
- Certificate auto-renews 30 days before expiration; Secret updates without restarts

### AI Collaboration Keys
- Generate ClusterIssuer for Let's Encrypt with correct Gateway reference
- Configure Gateway with both HTTP (for ACME challenges) and HTTPS listeners
- Troubleshoot Certificate stuck at Pending status

### Common Mistakes
- Using production endpoint during testing (rate limits can lock you out for a week)
- Missing HTTP listener needed for ACME HTTP-01 challenges
- Not enabling Gateway API support in cert-manager installation

### Connections
- **Builds on**: Lesson 6 (BackendTrafficPolicy) for complete traffic protection
- **Leads to**: Lesson 8 (Traffic Splitting Patterns) for deployment strategies
