---
sidebar_position: 12
title: "Capstone: Production Traffic for Task API"
description: "Integrate all traffic engineering patterns for production-ready Task API"
keywords: [capstone, production traffic, gateway api, envoy gateway, rate limiting, tls, keda, autoscaling, traffic engineering, kubernetes]
chapter: 56
lesson: 12
duration_minutes: 60
proficiency_level: B1

skills:
  - name: "Traffic Engineering Integration"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student produces production-ready traffic configuration"

  - name: "Specification-Driven Configuration"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student writes clear spec before implementation"

  - name: "System Integration"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student composes multiple patterns into working system"

  - name: "Production Validation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student validates configuration against success criteria"

learning_objectives:
  - objective: "Write specification for complete traffic configuration"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "spec.md with clear acceptance criteria"

  - objective: "Compose all L00-L11 patterns into integrated solution"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Gateway + HTTPRoute + policies applied successfully"

  - objective: "Validate production configuration against success criteria"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "All SC-001 to SC-007 criteria met"

  - objective: "Finalize traffic-engineer skill with all patterns"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Skill generates complete traffic stack"

cognitive_load:
  new_concepts: 0
  assessment: "Integration of existing concepts, no new concepts introduced"

differentiation:
  extension_for_advanced: "Add observability dashboards for traffic metrics"
  remedial_for_struggling: "Focus on Gateway + HTTPRoute + rate limiting only"
---

# Capstone: Production Traffic for Task API

You have learned Gateway API fundamentals, configured Envoy Gateway, written HTTPRoutes, applied rate limiting, set up TLS, implemented traffic splitting, configured autoscaling with KEDA, and explored Envoy AI Gateway for LLM traffic. Each lesson added a pattern to your traffic-engineer skill. Now you will compose all these patterns into a production-ready traffic stack for your Task API.

This capstone follows the specification-first approach. You will write a specification defining what "production-ready" means for your deployment, then use your traffic-engineer skill to generate configurations that meet those criteria. The goal is not just working configuration—it is configuration you can validate, defend, and evolve.

By the end, you will have a complete traffic engineering stack protecting your Task API: external access through Gateway, rate limiting per user, TLS termination, and autoscaling based on demand. You will also finalize your traffic-engineer skill as a reusable component for any future AI agent deployment.

---

## Phase 1: Write Your Specification

Before generating any YAML, define what you are building. Create a file named `traffic-spec.md` in your project:

```markdown
# Production Traffic Specification: Task API

## Overview

Configure production-ready traffic management for Task API running
in the task-api namespace on Docker Desktop Kubernetes.

## Business Goals

- External users can reach Task API from their browsers
- Abusive users cannot exhaust resources for others
- Communication is encrypted (HTTPS)
- System scales automatically with demand

## Success Criteria

### SC-001: External Access
Users can reach Task API at http://localhost:8080/api/tasks
from outside the cluster.

**Validation:**
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/api/tasks
# Expected: 200
```

### SC-002: Rate Limiting Active
Each user (identified by x-user-id header) is limited to 100 requests/minute.
Anonymous users are limited to 10 requests/minute.

**Validation:**
```bash
# Authenticated user: 100 requests succeed, then 429
for i in {1..110}; do
  curl -s -o /dev/null -w "%{http_code}\n" \
    -H "x-user-id: test" http://localhost:8080/api/tasks
done | grep 429 | wc -l
# Expected: 10 (requests 101-110 rejected)
```

### SC-003: TLS Termination
HTTPS access works with a valid (self-signed for local) certificate.

**Validation:**
```bash
curl -k -s -o /dev/null -w "%{http_code}" https://localhost:8443/api/tasks
# Expected: 200
```

### SC-004: Autoscaling Active
KEDA ScaledObject scales pods from 1-10 based on request rate.
Scale-to-zero disabled (minimum 1 replica for availability).

**Validation:**
```bash
kubectl get scaledobject task-api-scaler -n task-api
# Expected: READY=True, MIN=1, MAX=10
```

### SC-005: Versioned API Paths
Traffic routes to correct backends based on path prefix:
- /api/v1/* -> task-api-v1 service
- /api/v2/* -> task-api-v2 service (if deployed)

**Validation:**
```bash
curl -s http://localhost:8080/api/v1/tasks | jq .version
# Expected: "v1"
```

### SC-006: Circuit Breaker Protection
Backend protected from overload with max 50 concurrent connections.

**Validation:**
```bash
kubectl get backendtrafficpolicy task-api-protection -n task-api -o yaml | grep maxConnections
# Expected: maxConnections: 50
```

### SC-007: Skill Produces Valid Configuration
Traffic-engineer skill generates all required resources from this spec.

**Validation:**
```bash
# Skill generates YAML that passes dry-run
kubectl apply --dry-run=client -f generated-config.yaml
# Expected: All resources created (dry run)
```

## Constraints

- Docker Desktop Kubernetes (no cloud load balancer)
- Self-signed TLS certificates (no external CA)
- Prometheus available at prometheus.monitoring.svc.cluster.local:9090
- KEDA installed in keda namespace

## Non-Goals

- Multi-cluster routing
- External DNS integration
- Production certificate management (covered in real deployments)
- Global rate limiting with Redis (local rate limiting sufficient)
```

**Output:**

```
traffic-spec.md created (2847 bytes)
```

This specification answers the key questions: What are you building? How will you know it works? What constraints exist?

---

## Phase 2: Generate Configuration with Your Skill

With specification in hand, use your traffic-engineer skill to generate configuration.

### Step 1: Generate Gateway and HTTPRoute

Ask your skill to create the entry point:

```
Using my traffic-engineer skill, generate Gateway and HTTPRoute for Task API:

From traffic-spec.md:
- Gateway listening on ports 80 (HTTP) and 443 (HTTPS)
- HTTPRoute for /api/v1/* to task-api service on port 8000
- Running in task-api namespace
- Docker Desktop Kubernetes (gatewayClassName: eg)
```

**Review AI's output.** Check these specifics:

- Does Gateway use `gatewayClassName: eg` (Envoy Gateway)?
- Does Gateway have two listeners (http on 80, https on 443)?
- Does HTTPRoute use `parentRefs` pointing to the Gateway?
- Does HTTPRoute match `/api/v1` path prefix?

**Expected Gateway structure:**

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
    - name: https
      protocol: HTTPS
      port: 443
      tls:
        mode: Terminate
        certificateRefs:
          - name: task-api-tls
```

**Output:**

```
gateway.gateway.networking.k8s.io/task-api-gateway created (dry run)
```

### Step 2: Generate Rate Limiting Policy

Request BackendTrafficPolicy matching SC-002:

```
Generate BackendTrafficPolicy for Task API rate limiting:

- 100 requests/minute per authenticated user (x-user-id header)
- 10 requests/minute for anonymous users (no x-user-id header)
- Local rate limiting (no Redis dependency)
- Apply to task-api-route HTTPRoute
```

**Review AI's output.** Check these specifics:

- Does policy use `clientSelectors` with header matching?
- Does anonymous rule use `invert: true`?
- Are limits set correctly (100 vs 10)?

**Expected structure:**

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: BackendTrafficPolicy
metadata:
  name: task-api-ratelimit
  namespace: task-api
spec:
  targetRefs:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      name: task-api-route
  rateLimit:
    local:
      rules:
        # Authenticated users
        - clientSelectors:
            - headers:
                - name: x-user-id
                  value: "*"
          limit:
            requests: 100
            unit: Minute
        # Anonymous users
        - clientSelectors:
            - headers:
                - name: x-user-id
                  value: "*"
                  invert: true
          limit:
            requests: 10
            unit: Minute
```

**Output:**

```
backendtrafficpolicy.gateway.envoyproxy.io/task-api-ratelimit created (dry run)
```

### Step 3: Generate Circuit Breaker Policy

Request protection against backend overload:

```
Add circuit breaker to the BackendTrafficPolicy:

- Maximum 50 concurrent connections
- Maximum 25 parallel requests
- Maximum 5 pending requests (fail fast)
```

**Review AI's output.** Ensure circuit breaker is added to existing policy, not a separate resource:

```yaml
circuitBreaker:
  maxConnections: 50
  maxParallelRequests: 25
  maxPendingRequests: 5
```

**Output:**

```
backendtrafficpolicy.gateway.envoyproxy.io/task-api-protection created (dry run)
```

### Step 4: Generate TLS Configuration

Request self-signed certificate setup:

```
Generate TLS configuration for local development:

- Self-signed certificate for localhost
- Certificate stored in task-api-tls Secret
- Gateway configured for TLS termination
```

**Review AI's output.** For local development, you need:

1. Certificate generation commands
2. Secret containing cert and key
3. Gateway listener referencing the secret

**Certificate generation:**

```bash
# Generate self-signed certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key -out tls.crt \
  -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

# Create Kubernetes secret
kubectl create secret tls task-api-tls \
  --cert=tls.crt --key=tls.key \
  -n task-api
```

**Output:**

```
secret/task-api-tls created
```

### Step 5: Generate KEDA ScaledObject

Request autoscaling configuration matching SC-004:

```
Generate KEDA ScaledObject for Task API:

- Scale based on request rate from Prometheus
- Minimum 1 replica (no scale-to-zero for availability)
- Maximum 10 replicas
- Scale up when requests exceed 50/second
- Prometheus at prometheus.monitoring.svc.cluster.local:9090
```

**Review AI's output.** Check these specifics:

- Is `minReplicaCount` set to 1 (not 0)?
- Is the Prometheus query correct for your metrics?
- Is the threshold appropriate?

**Expected structure:**

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: task-api-scaler
  namespace: task-api
spec:
  scaleTargetRef:
    name: task-api
  minReplicaCount: 1
  maxReplicaCount: 10
  pollingInterval: 15
  cooldownPeriod: 300
  triggers:
    - type: prometheus
      metadata:
        serverAddress: http://prometheus.monitoring.svc.cluster.local:9090
        metricName: task_api_request_rate
        query: sum(rate(http_requests_total{service="task-api"}[2m]))
        threshold: "50"
```

**Output:**

```
scaledobject.keda.sh/task-api-scaler created (dry run)
```

---

## Phase 3: Apply Configuration

With all configurations generated and reviewed, apply them to your cluster in the correct order.

### Step 1: Create Namespace and Prerequisites

```bash
# Create namespace if not exists
kubectl create namespace task-api --dry-run=client -o yaml | kubectl apply -f -

# Verify Envoy Gateway is running
kubectl get pods -n envoy-gateway-system
```

**Output:**

```
namespace/task-api configured
NAME                                        READY   STATUS    RESTARTS   AGE
envoy-gateway-7b9c4d6f5-xxxxx              1/1     Running   0          1h
```

### Step 2: Create TLS Secret

```bash
# Generate certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key -out tls.crt \
  -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

# Create secret
kubectl create secret tls task-api-tls \
  --cert=tls.crt --key=tls.key \
  -n task-api
```

**Output:**

```
Generating a RSA private key
...
secret/task-api-tls created
```

### Step 3: Apply Gateway and HTTPRoute

```bash
# Apply Gateway first (HTTPRoute depends on it)
kubectl apply -f gateway.yaml

# Wait for Gateway to be ready
kubectl wait --for=condition=Programmed gateway/task-api-gateway -n task-api --timeout=60s

# Apply HTTPRoute
kubectl apply -f httproute.yaml
```

**Output:**

```
gateway.gateway.networking.k8s.io/task-api-gateway created
gateway.gateway.networking.k8s.io/task-api-gateway condition met
httproute.gateway.networking.k8s.io/task-api-route created
```

### Step 4: Apply Traffic Policies

```bash
# Apply BackendTrafficPolicy (rate limiting + circuit breaker)
kubectl apply -f backend-traffic-policy.yaml
```

**Output:**

```
backendtrafficpolicy.gateway.envoyproxy.io/task-api-protection created
```

### Step 5: Apply KEDA ScaledObject

```bash
# Apply ScaledObject
kubectl apply -f scaledobject.yaml

# Verify KEDA recognized it
kubectl get scaledobject -n task-api
```

**Output:**

```
scaledobject.keda.sh/task-api-scaler created
NAME              SCALETARGETKIND      SCALETARGETNAME   MIN   MAX   TRIGGERS     READY   ACTIVE
task-api-scaler   apps/v1.Deployment   task-api          1     10    prometheus   True    True
```

---

## Phase 4: Validate Against Success Criteria

Run each validation from your specification.

### SC-001: External Access

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/api/tasks
```

**Output:**

```
200
```

Result: PASS

### SC-002: Rate Limiting

```bash
# Test authenticated user limit (100/min)
for i in {1..110}; do
  curl -s -o /dev/null -w "%{http_code}\n" \
    -H "x-user-id: test-user" http://localhost:8080/api/tasks
done | sort | uniq -c
```

**Output:**

```
    100 200
     10 429
```

Result: PASS (100 succeeded, 10 rate limited)

```bash
# Test anonymous limit (10/min)
for i in {1..15}; do
  curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/api/tasks
done | sort | uniq -c
```

**Output:**

```
     10 200
      5 429
```

Result: PASS (10 succeeded, 5 rate limited)

### SC-003: TLS Termination

```bash
curl -k -s -o /dev/null -w "%{http_code}" https://localhost:8443/api/tasks
```

**Output:**

```
200
```

Result: PASS

### SC-004: Autoscaling Active

```bash
kubectl get scaledobject task-api-scaler -n task-api
```

**Output:**

```
NAME              SCALETARGETKIND      SCALETARGETNAME   MIN   MAX   TRIGGERS     READY   ACTIVE
task-api-scaler   apps/v1.Deployment   task-api          1     10    prometheus   True    True
```

Result: PASS (READY=True, MIN=1, MAX=10)

### SC-005: Versioned API Paths

```bash
curl -s http://localhost:8080/api/v1/tasks | jq .version
```

**Output:**

```
"v1"
```

Result: PASS

### SC-006: Circuit Breaker Protection

```bash
kubectl get backendtrafficpolicy task-api-protection -n task-api -o yaml | grep -A3 circuitBreaker
```

**Output:**

```yaml
  circuitBreaker:
    maxConnections: 50
    maxParallelRequests: 25
    maxPendingRequests: 5
```

Result: PASS

### SC-007: Skill Produces Valid Configuration

```bash
kubectl apply --dry-run=client -f generated-config.yaml
```

**Output:**

```
gateway.gateway.networking.k8s.io/task-api-gateway created (dry run)
httproute.gateway.networking.k8s.io/task-api-route created (dry run)
backendtrafficpolicy.gateway.envoyproxy.io/task-api-protection created (dry run)
scaledobject.keda.sh/task-api-scaler created (dry run)
```

Result: PASS

### Validation Summary

| Criterion | Result |
|-----------|--------|
| SC-001: External Access | PASS |
| SC-002: Rate Limiting | PASS |
| SC-003: TLS Termination | PASS |
| SC-004: Autoscaling Active | PASS |
| SC-005: Versioned API Paths | PASS |
| SC-006: Circuit Breaker | PASS |
| SC-007: Skill Valid Output | PASS |

All success criteria met. Your Task API has production-ready traffic engineering.

---

## Phase 5: Finalize Your Skill

Your traffic-engineer skill has accumulated patterns from all 12 lessons. Review and finalize it.

### Complete Decision Tree

Your skill should include this decision logic:

| Question | If Yes | If No |
|----------|--------|-------|
| Need external access? | Configure Gateway + HTTPRoute | Use ClusterIP Service |
| Multiple API versions? | Path-based routing in HTTPRoute | Single backend |
| Per-user quotas needed? | Header-based rate limiting | Global rate limit |
| Protect backend from overload? | Add circuit breaker | Skip for low-traffic |
| TLS required? | Configure listener with certificateRefs | HTTP only |
| Event-driven workload? | KEDA with appropriate scaler | HPA on CPU |
| Cost-sensitive? | KEDA with scale-to-zero | Minimum replicas |
| LLM/AI traffic? | Envoy AI Gateway with token limits | Standard rate limiting |

### Complete Template Library

Your skill should include templates for:

**1. Gateway with HTTP and HTTPS:**

```yaml
# Template: gateway-dual-listener
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: {{ name }}-gateway
  namespace: {{ namespace }}
spec:
  gatewayClassName: eg
  listeners:
    - name: http
      protocol: HTTP
      port: {{ http_port | default(80) }}
    - name: https
      protocol: HTTPS
      port: {{ https_port | default(443) }}
      tls:
        mode: Terminate
        certificateRefs:
          - name: {{ tls_secret }}
```

**2. HTTPRoute with versioned paths:**

```yaml
# Template: httproute-versioned
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: {{ name }}-route
  namespace: {{ namespace }}
spec:
  parentRefs:
    - name: {{ gateway }}
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/v1
      backendRefs:
        - name: {{ service }}-v1
          port: {{ port }}
    - matches:
        - path:
            type: PathPrefix
            value: /api/v2
      backendRefs:
        - name: {{ service }}-v2
          port: {{ port }}
```

**3. BackendTrafficPolicy with rate limiting and circuit breaker:**

```yaml
# Template: backend-traffic-policy-complete
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: BackendTrafficPolicy
metadata:
  name: {{ name }}-protection
  namespace: {{ namespace }}
spec:
  targetRefs:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      name: {{ route }}
  rateLimit:
    local:
      rules:
        - clientSelectors:
            - headers:
                - name: x-user-id
                  value: "*"
          limit:
            requests: {{ authenticated_limit | default(100) }}
            unit: Minute
        - clientSelectors:
            - headers:
                - name: x-user-id
                  value: "*"
                  invert: true
          limit:
            requests: {{ anonymous_limit | default(10) }}
            unit: Minute
  circuitBreaker:
    maxConnections: {{ max_connections | default(50) }}
    maxParallelRequests: {{ max_parallel | default(25) }}
    maxPendingRequests: {{ max_pending | default(5) }}
```

**4. KEDA ScaledObject:**

```yaml
# Template: scaledobject-prometheus
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: {{ name }}-scaler
  namespace: {{ namespace }}
spec:
  scaleTargetRef:
    name: {{ deployment }}
  minReplicaCount: {{ min_replicas | default(1) }}
  maxReplicaCount: {{ max_replicas | default(10) }}
  pollingInterval: {{ polling_interval | default(15) }}
  cooldownPeriod: {{ cooldown | default(300) }}
  triggers:
    - type: prometheus
      metadata:
        serverAddress: {{ prometheus_url }}
        metricName: {{ metric_name }}
        query: {{ query }}
        threshold: "{{ threshold }}"
```

### Troubleshooting Guide

Add this to your skill:

| Symptom | Check | Likely Cause |
|---------|-------|--------------|
| 404 on all requests | HTTPRoute parentRefs correct? | Gateway name mismatch |
| No rate limiting | BackendTrafficPolicy targetRefs? | Route name mismatch |
| TLS handshake fails | Secret exists? Certificate valid? | Missing or expired cert |
| KEDA not scaling | Prometheus query returns data? | Query syntax or no metrics |
| 503 under low load | Circuit breaker too aggressive? | Increase maxParallelRequests |
| Cold start too slow | minReplicaCount = 0? | Set minimum 1 for availability |

### Skill Verification

Run this test to verify your skill handles the complete workflow:

```bash
# Ask skill to generate complete config from spec
# Then validate

kubectl apply --dry-run=client -f complete-config.yaml
# All resources should pass validation
```

---

## Reflect on Your Skill

Your traffic-engineer skill is now complete. It should handle:

- Gateway setup (single and dual listener)
- HTTPRoute configuration (paths, headers, query params)
- Rate limiting (global, per-user, tiered)
- Circuit breaker protection
- TLS termination (with self-signed or CA certs)
- Traffic splitting (canary, blue-green, A/B)
- Autoscaling (HPA, KEDA with various scalers)
- LLM traffic (token-based limiting, provider fallback)

Consider what edge cases need documentation:

- **Multi-tenant deployments**: How do you isolate traffic between tenants?
- **Gradual rollouts**: What traffic split percentages work for your canary process?
- **Disaster recovery**: How quickly can you fail over to a secondary backend?

This skill becomes part of your Digital FTE portfolio. When deploying future AI agents, invoke this skill to generate production-ready traffic configurations in minutes rather than hours.

### Submit Your Skill

Your traffic-engineer skill is ready for your skills portfolio:

```bash
# Verify skill structure
ls -la .claude/skills/traffic-engineer/

# Expected:
# SKILL.md          - Core patterns and decision trees
# templates/        - YAML templates for all resources
# references/       - Links to official documentation
```

Commit your finalized skill:

```bash
cd .claude/skills/traffic-engineer
git add .
git commit -m "feat(skill): finalize traffic-engineer with complete patterns"
```

You now own a production-tested traffic engineering skill that transforms any AI agent deployment from "pod running in cluster" to "production service ready for users."
