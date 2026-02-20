# Gateway API Patterns

## HTTPRoute Matching Reference

### Path Matching Types

| Type | Syntax | Matches | Example |
|------|--------|---------|---------|
| **PathPrefix** | `/api` | `/api`, `/api/`, `/api/users` | Most common for API routes |
| **Exact** | `/health` | Only `/health` exactly | Health checks, specific endpoints |
| **RegularExpression** | `^/api/v[0-9]+/.*` | `/api/v1/users`, `/api/v2/tasks` | Version patterns |

### Header Matching

```yaml
# Exact header match
matches:
- headers:
  - name: x-api-key
    value: secret123

# Header exists (any value)
matches:
- headers:
  - name: Authorization
    type: RegularExpression
    value: ".*"

# Header prefix match
matches:
- headers:
  - name: Content-Type
    type: RegularExpression
    value: "application/json.*"
```

### Query Parameter Matching

```yaml
# Exact match
matches:
- queryParams:
  - name: version
    value: "2"

# Regex match
matches:
- queryParams:
  - name: page
    type: RegularExpression
    value: "[0-9]+"
```

### Method Matching

```yaml
# Specific HTTP method
matches:
- method: POST
  path:
    type: PathPrefix
    value: /api/tasks

# Multiple methods
rules:
- matches:
  - method: GET
    path: {type: PathPrefix, value: /api/tasks}
  - method: POST
    path: {type: PathPrefix, value: /api/tasks}
  backendRefs:
  - name: task-api
    port: 8000
```

### Combined Matching (AND Logic)

```yaml
# All conditions must match
matches:
- path:
    type: PathPrefix
    value: /admin
  headers:
  - name: x-role
    value: admin
  method: DELETE
```

### Multiple Rules (OR Logic)

```yaml
rules:
# Rule 1: Admin users
- matches:
  - headers:
    - name: x-role
      value: admin
  backendRefs:
  - name: admin-api
    port: 8000

# Rule 2: Regular users (fallback)
- matches:
  - path:
      type: PathPrefix
      value: /api
  backendRefs:
  - name: user-api
    port: 8000
```

## Traffic Splitting Patterns

### Canary Deployment (Gradual Rollout)

```yaml
# Start with 5%, increase to 100%
rules:
- matches:
  - path: {type: PathPrefix, value: /api}
  backendRefs:
  - name: api-v1
    port: 8000
    weight: 95
  - name: api-v2
    port: 8000
    weight: 5
```

### Blue-Green with Header Switch

```yaml
# Blue (current production)
- matches:
  - path: {type: PathPrefix, value: /api}
  backendRefs:
  - name: api-blue
    port: 8000

# Green (new version) - header activated
- matches:
  - path: {type: PathPrefix, value: /api}
    headers:
    - name: x-version
      value: green
  backendRefs:
  - name: api-green
    port: 8000
```

### A/B Testing by User Segment

```yaml
# Beta users (10% of traffic)
- matches:
  - headers:
    - name: x-user-segment
      value: beta
  backendRefs:
  - name: api-experimental
    port: 8000

# Control group (90% of traffic)
- matches:
  - path: {type: PathPrefix, value: /}
  backendRefs:
  - name: api-stable
    port: 8000
```

## GRPCRoute Patterns

### Basic gRPC Service Routing

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: grpc-route
spec:
  parentRefs:
  - name: grpc-gateway
  hostnames:
  - grpc.example.com
  rules:
  - matches:
    - method:
        service: tasks.TaskService
        method: CreateTask
    backendRefs:
    - name: task-grpc
      port: 50051
```

### gRPC with Reflection

```yaml
rules:
# Reflection service (for grpcurl discovery)
- matches:
  - method:
      service: grpc.reflection.v1alpha.ServerReflection
  backendRefs:
  - name: task-grpc
    port: 50051

# Main service
- matches:
  - method:
      service: tasks.TaskService
  backendRefs:
  - name: task-grpc
    port: 50051
```

## Cross-Namespace Routing

### ReferenceGrant for Cross-Namespace Backend

```yaml
# In target namespace (where Service lives)
apiVersion: gateway.networking.k8s.io/v1beta1
kind: ReferenceGrant
metadata:
  name: allow-route-access
  namespace: backend-ns
spec:
  from:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    namespace: frontend-ns
  to:
  - group: ""
    kind: Service
    name: backend-service
```

### HTTPRoute Referencing Cross-Namespace Service

```yaml
# In frontend-ns
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: frontend-route
  namespace: frontend-ns
spec:
  parentRefs:
  - name: main-gateway
    namespace: gateway-ns
  rules:
  - backendRefs:
    - name: backend-service
      namespace: backend-ns  # Cross-namespace reference
      port: 8080
```

## URL Rewriting

### Path Prefix Replacement

```yaml
rules:
- matches:
  - path:
      type: PathPrefix
      value: /v1/api
  filters:
  - type: URLRewrite
    urlRewrite:
      path:
        type: ReplacePrefixMatch
        replacePrefixMatch: /api
  backendRefs:
  - name: api
    port: 8000
# /v1/api/tasks -> /api/tasks
```

### Full Path Replacement

```yaml
filters:
- type: URLRewrite
  urlRewrite:
    path:
      type: ReplaceFullPath
      replaceFullPath: /new-path
```

### Hostname Rewrite

```yaml
filters:
- type: URLRewrite
  urlRewrite:
    hostname: internal.example.com
```

## Redirects

### HTTP to HTTPS Redirect

```yaml
rules:
- matches:
  - path:
      type: PathPrefix
      value: /
  filters:
  - type: RequestRedirect
    requestRedirect:
      scheme: https
      statusCode: 301
```

### Domain Redirect

```yaml
filters:
- type: RequestRedirect
  requestRedirect:
    hostname: new-domain.example.com
    statusCode: 301
```

## Request/Response Header Manipulation

### Add Headers

```yaml
filters:
- type: RequestHeaderModifier
  requestHeaderModifier:
    add:
    - name: x-request-id
      value: ${request_id}
    - name: x-forwarded-proto
      value: https
```

### Set/Override Headers

```yaml
filters:
- type: RequestHeaderModifier
  requestHeaderModifier:
    set:
    - name: Host
      value: internal-api.example.com
```

### Remove Headers

```yaml
filters:
- type: RequestHeaderModifier
  requestHeaderModifier:
    remove:
    - x-internal-header
    - x-debug
```

### Response Headers

```yaml
filters:
- type: ResponseHeaderModifier
  responseHeaderModifier:
    add:
    - name: X-Content-Type-Options
      value: nosniff
    - name: Strict-Transport-Security
      value: max-age=31536000
```
