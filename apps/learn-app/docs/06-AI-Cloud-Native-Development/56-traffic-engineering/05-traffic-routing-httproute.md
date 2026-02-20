---
sidebar_position: 5
title: "Traffic Routing with HTTPRoute"
description: "Master HTTPRoute matching patterns for production traffic routing"
keywords: [httproute, gateway api, traffic routing, path matching, header routing, traffic splitting, canary, grpcroute, kubernetes]
chapter: 56
lesson: 5
duration_minutes: 40
proficiency_level: B1

skills:
  - name: "HTTPRoute Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student can create HTTPRoute with multiple matching rules"

  - name: "Traffic Pattern Design"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student can design routing rules for multi-service architectures"

  - name: "Canary Deployment Patterns"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student can configure traffic weights for gradual rollouts"

  - name: "gRPC Routing"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student can create GRPCRoute for gRPC services"

learning_objectives:
  - objective: "Configure path-based routing with Exact, PathPrefix, and RegularExpression"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Different paths route to correct backends"
    three_role_integration:
      ai_as_teacher: "Learn regex pattern best practices from AI"
      ai_as_student: "Specify Task API endpoint structure clearly"
      ai_as_coworker: "Test and refine path matching together"

  - objective: "Configure header-based routing for versioned API access"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "x-version header routes to correct service"
    three_role_integration:
      ai_as_teacher: "Discover header routing patterns for API versioning"
      ai_as_student: "Define version strategy requirements"
      ai_as_coworker: "Iterate on header matching logic"

  - objective: "Implement traffic weights for canary deployment patterns"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Traffic splits correctly between backends"
    three_role_integration:
      ai_as_teacher: "Learn progressive rollout percentages from AI"
      ai_as_student: "Specify risk tolerance for canary strategy"
      ai_as_coworker: "Design weight progression together"

  - objective: "Configure GRPCRoute for gRPC services"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "gRPC traffic routes through Gateway"
    three_role_integration:
      ai_as_teacher: "Learn gRPC-specific routing differences"
      ai_as_student: "Describe gRPC service definitions"
      ai_as_coworker: "Validate GRPCRoute configuration"

cognitive_load:
  new_concepts: 7
  assessment: "Seven concepts: path matching types, header matching, query matching, method matching, traffic weights, multiple rules, GRPCRoute"

differentiation:
  extension_for_advanced: "Implement request mirroring for shadow testing"
  remedial_for_struggling: "Focus on PathPrefix matching only"
---

# Traffic Routing with HTTPRoute

Your Gateway is listening. Envoy proxies are running. External traffic can reach the cluster. But right now, every request goes to the same place. In production, you need sophisticated routing: API version 2 requests go to the new service, beta users get experimental features, 10% of traffic tests the canary deployment.

HTTPRoute is where the real routing logic lives. The Gateway defines the entry point. HTTPRoute defines what happens next—matching requests by path, headers, query parameters, or HTTP method, then directing them to the right backend.

This lesson covers the complete HTTPRoute matching vocabulary. By the end, you will route traffic based on any request characteristic and implement canary deployment patterns using traffic weights.

---

## Path Matching Types

Path matching is the most common routing pattern. Gateway API provides three match types, each serving different use cases.

### Exact Matching

Exact matches the path exactly—character for character. No trailing slash tolerance, no prefix matching.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-exact
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: Exact
            value: /api/v1/tasks
      backendRefs:
        - name: task-api
          port: 8000
```

**Test the route:**

```bash
# This matches
curl http://localhost:8080/api/v1/tasks

# This does NOT match (trailing slash)
curl http://localhost:8080/api/v1/tasks/

# This does NOT match (different path)
curl http://localhost:8080/api/v1/tasks/123
```

**Output:**

```
# Matching request
{"tasks": [...]}

# Non-matching requests
404 Not Found
```

**When to use Exact**: Health check endpoints, specific API actions, webhooks that must match precisely.

### PathPrefix Matching

PathPrefix matches any path starting with the specified prefix. This is the most common match type.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-prefix
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/v1/
      backendRefs:
        - name: task-api
          port: 8000
```

**Test the route:**

```bash
# All of these match
curl http://localhost:8080/api/v1/
curl http://localhost:8080/api/v1/tasks
curl http://localhost:8080/api/v1/tasks/123
curl http://localhost:8080/api/v1/tasks/123/comments
```

**Output:**

```
{"version": "v1", ...}
{"tasks": [...]}
{"task": {"id": 123, ...}}
{"comments": [...]}
```

**When to use PathPrefix**: Routing entire API versions to a service, namespace-based routing, catch-all patterns.

### RegularExpression Matching

RegularExpression provides maximum flexibility using RE2 syntax.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-regex
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: RegularExpression
            value: "/api/v[0-9]+/tasks"
      backendRefs:
        - name: task-api
          port: 8000
```

**Test the route:**

```bash
# These match
curl http://localhost:8080/api/v1/tasks
curl http://localhost:8080/api/v2/tasks
curl http://localhost:8080/api/v99/tasks

# This does NOT match
curl http://localhost:8080/api/beta/tasks
```

**Output:**

```
{"version": "v1", "tasks": [...]}
{"version": "v2", "tasks": [...]}
{"version": "v99", "tasks": [...]}

404 Not Found
```

**When to use RegularExpression**: Version-flexible routing, complex patterns, user ID extraction. Use sparingly—regex matching has performance overhead.

---

## Header-Based Routing

Route requests based on HTTP headers. This enables API versioning, beta features, and premium user routing without changing URLs.

### Exact Header Matching

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-header-version
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    # Route x-version: 2 to v2 backend
    - matches:
        - path:
            type: PathPrefix
            value: /api/
          headers:
            - name: x-version
              value: "2"
      backendRefs:
        - name: task-api-v2
          port: 8000

    # Default to v1 backend
    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api-v1
          port: 8000
```

**Test the routes:**

```bash
# Goes to v2 backend
curl -H "x-version: 2" http://localhost:8080/api/tasks

# Goes to v1 backend (no header)
curl http://localhost:8080/api/tasks

# Goes to v1 backend (different header value)
curl -H "x-version: 1" http://localhost:8080/api/tasks
```

**Output:**

```
{"version": "v2", "tasks": [...]}
{"version": "v1", "tasks": [...]}
{"version": "v1", "tasks": [...]}
```

### RegularExpression Header Matching

Match headers using patterns:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-premium
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    # Premium API keys get dedicated backend
    - matches:
        - path:
            type: PathPrefix
            value: /api/
          headers:
            - name: x-api-key
              type: RegularExpression
              value: "^premium-.*"
      backendRefs:
        - name: task-api-premium
          port: 8000

    # Standard requests
    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api-standard
          port: 8000
```

**Test the routes:**

```bash
# Premium backend
curl -H "x-api-key: premium-abc123" http://localhost:8080/api/tasks

# Standard backend
curl -H "x-api-key: basic-xyz789" http://localhost:8080/api/tasks
```

**Output:**

```
{"tier": "premium", "rate_limit": 10000, ...}
{"tier": "standard", "rate_limit": 1000, ...}
```

### Beta User Routing

Route beta testers to experimental features:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-beta
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/
          headers:
            - name: x-beta-user
              value: "true"
      backendRefs:
        - name: task-api-beta
          port: 8000

    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api-stable
          port: 8000
```

---

## Query Parameter Matching

Route based on URL query parameters. Useful for feature flags, debug modes, and tier selection.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-query
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    # Debug mode goes to debug-enabled backend
    - matches:
        - path:
            type: PathPrefix
            value: /api/
          queryParams:
            - name: debug
              value: "true"
      backendRefs:
        - name: task-api-debug
          port: 8000

    # Premium tier parameter
    - matches:
        - path:
            type: PathPrefix
            value: /api/
          queryParams:
            - name: tier
              value: "premium"
      backendRefs:
        - name: task-api-premium
          port: 8000

    # Default
    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api
          port: 8000
```

**Test the routes:**

```bash
# Debug backend
curl "http://localhost:8080/api/tasks?debug=true"

# Premium backend
curl "http://localhost:8080/api/tasks?tier=premium"

# Default backend
curl "http://localhost:8080/api/tasks"
```

**Output:**

```
{"debug_info": {...}, "tasks": [...]}
{"premium_features": true, "tasks": [...]}
{"tasks": [...]}
```

### Combining Path and Query Matching

Match both path and query parameters:

```yaml
rules:
  - matches:
      - path:
          type: PathPrefix
          value: /api/v2/
        queryParams:
          - name: experimental
            value: "enabled"
    backendRefs:
      - name: task-api-experimental
        port: 8000
```

This matches `/api/v2/tasks?experimental=enabled` but not `/api/v1/tasks?experimental=enabled`.

---

## Method-Based Routing

Route based on HTTP method. A common pattern: send read operations to read replicas, write operations to the primary.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-method
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    # Read operations to read replicas
    - matches:
        - path:
            type: PathPrefix
            value: /api/
          method: GET
      backendRefs:
        - name: task-api-read-replica
          port: 8000

    # Write operations to primary
    - matches:
        - path:
            type: PathPrefix
            value: /api/
          method: POST
      backendRefs:
        - name: task-api-primary
          port: 8000

    - matches:
        - path:
            type: PathPrefix
            value: /api/
          method: PUT
      backendRefs:
        - name: task-api-primary
          port: 8000

    - matches:
        - path:
            type: PathPrefix
            value: /api/
          method: DELETE
      backendRefs:
        - name: task-api-primary
          port: 8000
```

**Test the routes:**

```bash
# Read replica
curl http://localhost:8080/api/tasks

# Primary (write)
curl -X POST -d '{"title":"New task"}' http://localhost:8080/api/tasks
curl -X PUT -d '{"title":"Updated"}' http://localhost:8080/api/tasks/1
curl -X DELETE http://localhost:8080/api/tasks/1
```

**Output:**

```
{"source": "read-replica", "tasks": [...]}
{"source": "primary", "created": {...}}
{"source": "primary", "updated": {...}}
{"source": "primary", "deleted": true}
```

---

## Traffic Weights for Canary Deployments

Traffic weights enable gradual rollouts. Send most traffic to the stable version, a small percentage to the canary.

### Basic Traffic Split

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-canary
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api-stable
          port: 8000
          weight: 90
        - name: task-api-canary
          port: 8000
          weight: 10
```

**Traffic distribution:**

```
90% → task-api-stable
10% → task-api-canary
```

**Test with multiple requests:**

```bash
for i in {1..20}; do
  curl -s http://localhost:8080/api/version | jq -r '.version'
done
```

**Output:**

```
stable
stable
stable
stable
canary
stable
stable
stable
stable
stable
canary
stable
...
```

Approximately 2 out of 20 requests go to canary.

### Progressive Rollout

Gradually increase canary traffic as confidence grows:

```yaml
# Stage 1: 5% canary
backendRefs:
  - name: task-api-stable
    port: 8000
    weight: 95
  - name: task-api-canary
    port: 8000
    weight: 5
```

```yaml
# Stage 2: 25% canary
backendRefs:
  - name: task-api-stable
    port: 8000
    weight: 75
  - name: task-api-canary
    port: 8000
    weight: 25
```

```yaml
# Stage 3: 50% canary
backendRefs:
  - name: task-api-stable
    port: 8000
    weight: 50
  - name: task-api-canary
    port: 8000
    weight: 50
```

```yaml
# Stage 4: Complete rollout
backendRefs:
  - name: task-api-canary
    port: 8000
    weight: 100
```

### Blue-Green Deployment

For instant cutover, change weights from 100/0 to 0/100:

```yaml
# Before cutover
backendRefs:
  - name: task-api-blue
    port: 8000
    weight: 100
  - name: task-api-green
    port: 8000
    weight: 0

# After cutover
backendRefs:
  - name: task-api-blue
    port: 8000
    weight: 0
  - name: task-api-green
    port: 8000
    weight: 100
```

---

## Request Mirroring

Mirror traffic to a shadow service for testing without affecting production responses. The shadow service receives copies of requests, but its responses are discarded.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-mirror
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api
          port: 8000
      filters:
        - type: RequestMirror
          requestMirror:
            backendRef:
              name: task-api-shadow
              port: 8000
```

**How it works:**

```
Client Request
      │
      ├──────────────────┐
      │                  │
      ▼                  ▼
task-api (primary)   task-api-shadow
      │                  │
      │                  └── Response discarded
      │
      ▼
Response to Client
```

**Use cases:**
- Testing new AI model versions with production traffic
- Validating performance of refactored services
- Collecting training data from production requests

**Verify mirroring:**

```bash
# Check shadow service logs
kubectl logs -l app=task-api-shadow -n task-api --tail=10
```

**Output:**

```
2025-12-30T10:00:00Z Received mirrored request: GET /api/tasks
2025-12-30T10:00:01Z Received mirrored request: POST /api/tasks
2025-12-30T10:00:02Z Received mirrored request: GET /api/tasks/123
```

---

## Multiple Rules and Ordering

Rules are evaluated in order. More specific rules should come first.

### Rule Precedence

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: task-api-ordered
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    # Most specific: urgent tasks endpoint
    - matches:
        - path:
            type: Exact
            value: /api/v1/tasks/urgent
      backendRefs:
        - name: task-api-urgent
          port: 8000

    # Specific: single task by ID pattern
    - matches:
        - path:
            type: RegularExpression
            value: "/api/v1/tasks/[0-9]+"
      backendRefs:
        - name: task-api-read
          port: 8000

    # General: all tasks endpoints
    - matches:
        - path:
            type: PathPrefix
            value: /api/v1/tasks
      backendRefs:
        - name: task-api
          port: 8000

    # Catch-all: everything else
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: default-backend
          port: 8000
```

**Request routing:**

| Request | Matches Rule | Backend |
|---------|--------------|---------|
| `/api/v1/tasks/urgent` | Rule 1 (Exact) | task-api-urgent |
| `/api/v1/tasks/123` | Rule 2 (Regex) | task-api-read |
| `/api/v1/tasks` | Rule 3 (PathPrefix) | task-api |
| `/api/v1/tasks/new` | Rule 3 (PathPrefix) | task-api |
| `/health` | Rule 4 (Catch-all) | default-backend |

### Common Ordering Mistakes

**Wrong order (specific rule never matches):**

```yaml
rules:
  # This catches everything starting with /api/
  - matches:
      - path:
          type: PathPrefix
          value: /api/
    backendRefs:
      - name: task-api
        port: 8000

  # This NEVER matches (caught by rule above)
  - matches:
      - path:
          type: Exact
          value: /api/health
    backendRefs:
      - name: health-checker
        port: 8000
```

**Correct order:**

```yaml
rules:
  # Specific rule first
  - matches:
      - path:
          type: Exact
          value: /api/health
    backendRefs:
      - name: health-checker
        port: 8000

  # General rule second
  - matches:
      - path:
          type: PathPrefix
          value: /api/
    backendRefs:
      - name: task-api
        port: 8000
```

---

## GRPCRoute for gRPC Services

For gRPC services, use GRPCRoute instead of HTTPRoute. GRPCRoute understands gRPC semantics like service and method matching.

### When to Use GRPCRoute

| Protocol | Route Type |
|----------|------------|
| HTTP/1.1, HTTP/2 REST | HTTPRoute |
| gRPC (HTTP/2 with protobuf) | GRPCRoute |
| gRPC-Web | HTTPRoute or GRPCRoute |

### GRPCRoute Example

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: task-grpc-route
  namespace: task-api
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    # Route by gRPC service name
    - matches:
        - method:
            service: task.TaskService
      backendRefs:
        - name: task-grpc-service
          port: 50051

    # Route by specific method
    - matches:
        - method:
            service: task.TaskService
            method: CreateTask
      backendRefs:
        - name: task-grpc-write
          port: 50051

    # Route by method prefix
    - matches:
        - method:
            service: task.TaskService
            method: Get*
            type: RegularExpression
      backendRefs:
        - name: task-grpc-read
          port: 50051
```

**Verify GRPCRoute:**

```bash
kubectl get grpcroute task-grpc-route -n task-api
```

**Output:**

```
NAME              HOSTNAMES   AGE
task-grpc-route   []          1m
```

### Gateway Listener for gRPC

Your Gateway needs a listener that accepts HTTP/2 for gRPC:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: task-api-gateway
  namespace: task-api
spec:
  gatewayClassName: eg
  listeners:
    - name: http
      protocol: HTTP
      port: 80
    - name: grpc
      protocol: HTTP
      port: 50051
```

Note: gRPC uses HTTP/2, but the protocol field is `HTTP`. The actual HTTP version negotiation happens at the transport layer.

---

## Exercises

### Exercise 1: Create HTTPRoute with PathPrefix

Create an HTTPRoute that routes all `/api/` requests to the Task API:

```bash
kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: exercise-pathprefix
  namespace: default
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api
          port: 8000
EOF
```

**Verify:**

```bash
kubectl get httproute exercise-pathprefix
```

**Expected Output:**

```
NAME                 HOSTNAMES   AGE
exercise-pathprefix  []          1m
```

### Exercise 2: Add Header-Based Routing

Extend your HTTPRoute to route `x-version: 2` requests to task-api-v2:

```bash
kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: exercise-header
  namespace: default
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/
          headers:
            - name: x-version
              value: "2"
      backendRefs:
        - name: task-api-v2
          port: 8000
    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api-v1
          port: 8000
EOF
```

**Test (if services exist):**

```bash
curl -H "x-version: 2" http://localhost:8080/api/tasks
curl http://localhost:8080/api/tasks
```

### Exercise 3: Configure 90/10 Traffic Split

Create a canary deployment with 90% stable, 10% canary:

```bash
kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: exercise-canary
  namespace: default
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api-stable
          port: 8000
          weight: 90
        - name: task-api-canary
          port: 8000
          weight: 10
EOF
```

**Verify weights:**

```bash
kubectl get httproute exercise-canary -o yaml | grep -A5 backendRefs
```

**Expected Output:**

```yaml
      backendRefs:
      - name: task-api-stable
        port: 8000
        weight: 90
      - name: task-api-canary
        port: 8000
        weight: 10
```

### Exercise 4: Add Query Parameter Matching

Route debug requests to a debug-enabled backend:

```bash
kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: exercise-query
  namespace: default
spec:
  parentRefs:
    - name: task-api-gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/
          queryParams:
            - name: debug
              value: "true"
      backendRefs:
        - name: task-api-debug
          port: 8000
    - matches:
        - path:
            type: PathPrefix
            value: /api/
      backendRefs:
        - name: task-api
          port: 8000
EOF
```

**Test (if services exist):**

```bash
curl "http://localhost:8080/api/tasks?debug=true"
```

---

## Reflect on Your Skill

You built a `traffic-engineer` skill in Lesson 0. Based on what you learned about HTTPRoute:

### Add Routing Templates

Your skill should now generate HTTPRoute for common patterns:

**Path-based template:**

```yaml
# Template: path-based routing
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: {{ service }}-route
  namespace: {{ namespace }}
spec:
  parentRefs:
    - name: {{ gateway }}
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: {{ path_prefix }}
      backendRefs:
        - name: {{ service }}
          port: {{ port }}
```

**Header-based template:**

```yaml
# Template: header-based version routing
rules:
  - matches:
      - path:
          type: PathPrefix
          value: /api/
        headers:
          - name: {{ header_name }}
            value: {{ header_value }}
    backendRefs:
      - name: {{ versioned_service }}
        port: {{ port }}
```

**Traffic splitting template:**

```yaml
# Template: canary deployment
rules:
  - matches:
      - path:
          type: PathPrefix
          value: /
    backendRefs:
      - name: {{ stable_service }}
        port: {{ port }}
        weight: {{ stable_weight }}
      - name: {{ canary_service }}
        port: {{ port }}
        weight: {{ canary_weight }}
```

### What Rule Ordering Should Your Skill Follow?

When generating multiple rules, your skill should order them:

1. **Exact matches first** (most specific)
2. **RegularExpression matches second**
3. **PathPrefix matches third**
4. **Catch-all last** (least specific)

This ordering prevents more specific rules from being shadowed by general ones.

### Consider GRPCRoute

Your skill should ask about protocol:

| User says | Generate |
|-----------|----------|
| "REST API" | HTTPRoute |
| "gRPC service" | GRPCRoute |
| "Both REST and gRPC" | HTTPRoute + GRPCRoute |

---

## Try With AI

### Generate Multi-Service Routing

Ask your traffic-engineer skill to generate routing:

```
Using my traffic-engineer skill, generate HTTPRoute configuration for my
Task API with these requirements:

- /tasks goes to task-api service on port 8000
- /users goes to user-api service on port 8001
- /notifications goes to notification-api service on port 8002

All services are in the task-api namespace.
```

**What you're learning**: AI generates routing rules from requirements. Review the output—did AI use the correct path matching type? Are the backend ports correct? Did it order rules appropriately?

### Evaluate the Generated Route

Check AI's output:

- Are `parentRefs` correctly pointing to your Gateway?
- Did AI use `PathPrefix` for catch-all patterns and `Exact` for specific endpoints?
- Are all services in the specified namespace?

If the route does not match your requirements, tell AI what needs to change:

```
The HTTPRoute looks good, but I need /tasks/urgent to route to a different
service: urgent-task-api on port 8003. Add this as a higher priority rule.
```

### Add Canary Traffic Splitting

Extend the configuration:

```
Add a canary deployment pattern to the /tasks route:
- 95% traffic to task-api-stable
- 5% traffic to task-api-canary

Both services run on port 8000.
```

**What you're learning**: AI adapts existing configurations. Review the weights—do they sum correctly? Is the canary service defined with the right port?

### Review and Apply

Compare AI's final output to what you learned in this lesson:

- Do more specific rules come before general rules?
- Are header matchers using the correct syntax?
- Would `kubectl apply --dry-run=client` accept this YAML?

This iteration—specifying requirements, evaluating output, refining with constraints—is how production configurations emerge.

### Safety Note

When deploying HTTPRoute changes in production, test with `kubectl apply --dry-run=client` first. Incorrect routing rules can send traffic to wrong services or drop requests entirely. For canary deployments, start with small weights (1-5%) and monitor error rates before increasing.
