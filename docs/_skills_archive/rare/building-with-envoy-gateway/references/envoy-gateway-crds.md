# Envoy Gateway CRD Reference

## BackendTrafficPolicy

Controls traffic from gateway to backend services.

### Rate Limiting

#### Global Rate Limit (Redis-backed)

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: BackendTrafficPolicy
metadata:
  name: global-rate-limit
spec:
  targetRefs:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: api-route

  rateLimit:
    type: Global
    global:
      rules:
      # Rule 1: Per-user limit (distinct header values)
      - clientSelectors:
        - headers:
          - type: Distinct
            name: x-user-id
        limit:
          requests: 100
          unit: Minute

      # Rule 2: Anonymous limit (header not present)
      - clientSelectors:
        - headers:
          - name: x-user-id
            invert: true
        limit:
          requests: 10
          unit: Minute

      # Rule 3: Admin users (specific value, higher limit)
      - clientSelectors:
        - headers:
          - name: x-role
            value: admin
        limit:
          requests: 1000
          unit: Minute
```

#### Local Rate Limit (Per-Proxy)

```yaml
rateLimit:
  type: Local
  local:
    rules:
    - limit:
        requests: 100
        unit: Second
```

#### Cost-Based Rate Limiting (v1.3.0+)

```yaml
rateLimit:
  type: Global
  global:
    rules:
    - limit:
        requests: 1000
        unit: Hour
      cost: 10  # Each request costs 10 units
```

### Retry Policy

```yaml
retry:
  numRetries: 3
  perRetryTimeout: 5s
  retryOn:
  - "5xx"                    # Server errors
  - "reset"                  # Connection reset
  - "connect-failure"        # Connection failed
  - "retriable-4xx"          # 409 conflict, etc.
  - "gateway-error"          # 502, 503, 504
  backoff:
    baseInterval: 100ms
    maxInterval: 10s
```

### Circuit Breaker / Health Check

```yaml
healthCheck:
  active:
    type: HTTP
    http:
      path: /health
      expectedStatuses:
      - 200
      - 204
    interval: 10s
    timeout: 1s
    unhealthyThreshold: 3
    healthyThreshold: 1

circuitBreaker:
  maxConnections: 100
  maxPendingRequests: 50
  maxRequests: 1000
  maxRetries: 3
```

### Load Balancing

```yaml
loadBalancer:
  type: RoundRobin     # RoundRobin, LeastRequest, Random, ConsistentHash

  # For ConsistentHash
  consistentHash:
    type: Header
    header:
      name: x-user-id
```

### Timeouts

```yaml
timeout:
  tcp:
    connectTimeout: 10s
  http:
    connectionIdleTimeout: 1h
    requestTimeout: 30s
```

### Fault Injection (Testing)

```yaml
faultInjection:
  delay:
    fixedDelay: 500ms
    percentage: 10        # 10% of requests delayed
  abort:
    httpStatus: 503
    percentage: 5         # 5% of requests aborted
```

## ClientTrafficPolicy

Controls client-to-gateway connections.

### TLS Configuration

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: ClientTrafficPolicy
metadata:
  name: tls-policy
spec:
  targetRefs:
  - group: gateway.networking.k8s.io
    kind: Gateway
    name: main-gateway

  tls:
    minVersion: "1.2"
    maxVersion: "1.3"
    ciphers:
    - ECDHE-RSA-AES128-GCM-SHA256
    - ECDHE-RSA-AES256-GCM-SHA384
    alpnProtocols:
    - h2
    - http/1.1
```

### Connection Timeouts

```yaml
timeout:
  http:
    requestReceivedTimeout: 30s
    requestSendTimeout: 30s
```

### TCP Keepalive

```yaml
tcpKeepalive:
  probes: 3
  idleTime: 10m
  interval: 10s
```

### Client IP Detection

```yaml
clientIPDetection:
  xForwardedFor:
    numTrustedHops: 1
  customHeader:
    name: X-Real-IP
    failOpen: true
```

### HTTP Settings

```yaml
http1Settings:
  http10Compatible: false
  preserveHeaderCase: true

http2Settings:
  initialConnectionWindowSize: 1048576
  initialStreamWindowSize: 65536
  maxConcurrentStreams: 100
```

### Proxy Protocol

```yaml
proxyProtocol:
  version: V2
```

## SecurityPolicy

Authentication, authorization, and access control.

### JWT Authentication

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: SecurityPolicy
metadata:
  name: jwt-policy
spec:
  targetRefs:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: api-route

  jwt:
    providers:
    - name: auth0
      issuer: https://your-tenant.auth0.com/
      audiences:
      - https://api.example.com
      remoteJWKS:
        uri: https://your-tenant.auth0.com/.well-known/jwks.json
        timeout: 10s
        backoff:
          baseInterval: 1s
          maxInterval: 10s
      claimToHeaders:
      - claim: sub
        header: x-user-id
      - claim: permissions
        header: x-permissions
      - claim: email
        header: x-user-email
```

### OIDC Authentication

```yaml
oidc:
  provider:
    issuer: https://accounts.google.com
    authorizationEndpoint: https://accounts.google.com/o/oauth2/v2/auth
    tokenEndpoint: https://oauth2.googleapis.com/token
  clientID: "123456.apps.googleusercontent.com"
  clientSecret:
    name: google-oauth
    key: client-secret
  redirectURL: https://app.example.com/oauth2/callback
  logoutPath: /logout
  cookieSameSite: Lax
  cookieDomain: .example.com
  scopes:
  - openid
  - profile
  - email
```

### Basic Auth

```yaml
basicAuth:
  users:
    name: basic-auth-secret
```

### API Key

```yaml
apiKeyAuth:
  extractFrom:
    headers:
    - name: x-api-key
    - name: Authorization  # Bearer <api-key>
  credentialsSecret:
    name: api-keys
```

### Authorization Rules

```yaml
authorization:
  defaultAction: Deny
  rules:
  # Allow admin users
  - name: admin-access
    action: Allow
    principal:
      jwt:
        provider: auth0
        claims:
        - name: role
          values: ["admin"]

  # Allow internal IPs
  - name: internal-access
    action: Allow
    principal:
      ipAddress:
      - "10.0.0.0/8"
      - "172.16.0.0/12"

  # Allow specific paths without auth
  - name: public-paths
    action: Allow
    principal:
      ipAddress:
      - "0.0.0.0/0"
    match:
      - path:
          type: Exact
          value: /health
```

### CORS

```yaml
cors:
  allowOrigins:
  - type: Exact
    value: https://app.example.com
  - type: RegularExpression
    value: https://.*\.example\.com
  allowMethods:
  - GET
  - POST
  - PUT
  - DELETE
  - OPTIONS
  allowHeaders:
  - Authorization
  - Content-Type
  - X-Request-ID
  exposeHeaders:
  - X-Request-ID
  maxAge: 86400s
  allowCredentials: true
```

### External Authorization

```yaml
extAuth:
  grpc:
    backendRef:
      name: ext-authz-service
      port: 9000
    timeout: 10s

  # OR HTTP
  http:
    backendRef:
      name: ext-authz-service
      port: 8080
    path: /authorize
    headersToBackend:
    - Authorization
    - X-Request-ID
```

## EnvoyProxy

Proxy deployment and lifecycle configuration.

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: EnvoyProxy
metadata:
  name: custom-proxy
  namespace: envoy-gateway-system
spec:
  provider:
    type: Kubernetes
    kubernetes:
      envoyDeployment:
        replicas: 3
        container:
          resources:
            requests:
              cpu: 500m
              memory: 512Mi
            limits:
              cpu: 2000m
              memory: 2Gi
        pod:
          affinity:
            podAntiAffinity:
              preferredDuringSchedulingIgnoredDuringExecution:
              - weight: 100
                podAffinityTerm:
                  labelSelector:
                    matchLabels:
                      gateway.envoyproxy.io/owning-gateway-name: main-gateway
                  topologyKey: kubernetes.io/hostname

      envoyService:
        type: LoadBalancer
        annotations:
          service.beta.kubernetes.io/aws-load-balancer-type: nlb

  telemetry:
    metrics:
      prometheus:
        enabled: true
    accessLog:
      settings:
      - format:
          type: JSON
        sinks:
        - type: File
          file:
            path: /dev/stdout

  backendTLS:
    clientCertificateRef:
      kind: Secret
      name: backend-client-cert
```

## Backend

Advanced endpoint configuration.

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: Backend
metadata:
  name: external-api
spec:
  endpoints:
  - fqdn:
      hostname: api.external-service.com
      port: 443

  # OR IP-based
  - ip:
      address: 10.0.0.100
      port: 8080

  tls:
    # Client cert for mTLS
    clientCertificateRef:
      kind: Secret
      name: client-cert

    # CA to verify backend
    caCertificateRefs:
    - kind: ConfigMap
      name: backend-ca

    # SNI for TLS handshake
    sni: api.external-service.com
```

## EnvoyExtensionPolicy

Custom extensions (Wasm, Lua).

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: EnvoyExtensionPolicy
metadata:
  name: custom-extension
spec:
  targetRefs:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: api-route

  wasm:
  - name: custom-auth
    rootID: auth_filter
    code:
      type: HTTP
      http:
        url: https://example.com/wasm/auth.wasm
        sha256: abc123...
    config:
      "@type": type.googleapis.com/google.protobuf.StringValue
      value: '{"key": "value"}'
```

## Policy Attachment and Merging

### Policy Hierarchy

1. **Route-level** overrides **Gateway-level**
2. Multiple policies can target same resource with merging

### Merge Types

```yaml
# On BackendTrafficPolicy
spec:
  targetRefs:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: api-route

  # How to merge with Gateway-level policy
  # Replace: completely replace (default)
  # StrategicMerge: merge rules
  mergeType: StrategicMerge
```

### Target Selection

```yaml
# By name
targetRefs:
- group: gateway.networking.k8s.io
  kind: HTTPRoute
  name: specific-route

# By label (dynamic)
targetSelectors:
- matchLabels:
    app: task-api
    tier: frontend
```
