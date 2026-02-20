# Chapter 56 Implementation Plan: Traffic Engineering

**Source Spec**: `specs/001-ch56-traffic-engineering/spec.md`
**Expertise Skill**: `.claude/skills/building-with-envoy-gateway/SKILL.md`
**Planning Date**: 2025-12-30
**Constitution**: v7.0.0 (Agent Factory Paradigm, Reasoning-Activated)
**Status**: Ready for Implementation

---

## Summary

This plan structures a 13-lesson chapter teaching traffic engineering for Kubernetes using Gateway API, Envoy Gateway, KEDA autoscaling, and Envoy AI Gateway. The chapter follows the Skill-First pattern: L00 creates the student's `traffic-engineer` skill, and each subsequent lesson tests and improves it. All lessons respect B1 cognitive load limits (7-10 concepts) and use varied teaching modalities. The capstone (L12) integrates all patterns for production Task API traffic management.

---

## Chapter Identity & Context

**Part**: 7 (AI Cloud Native Development) - Tier 2: Enterprise
**Chapter Number**: 56
**Target Audience**: B1 tier (students with Kubernetes, Helm, observability from Ch49-55)
**Prerequisites**: Completed Ch49-55, Task API deployed on Docker Desktop K8s
**Proficiency Tier**: B1 (Intermediate)
**Hardware Tier**: Docker Desktop Kubernetes (no cloud provider dependencies)
**Duration**: ~8 hours (13 lessons, 480 minutes)

### Agent Factory Contribution

This chapter produces:
- **Student-Owned Skill**: `traffic-engineer` skill encapsulating Gateway API, rate limiting, TLS, autoscaling patterns
- **Digital FTE Component**: Reusable traffic management automation for AI agent deployments
- **Two Paths Alignment**: General Agent (Claude Code) helps build traffic-engineer skill; skill becomes Custom Agent component

---

## Pedagogical Architecture

### Learning Arc (13 Lessons)

| # | Lesson | Layer | Duration | Concepts | Purpose | Modality |
|---|--------|-------|----------|----------|---------|----------|
| L00 | Build Your Traffic Engineering Skill | L1 | 25 min | 4 | **Skill Creation** | Skill-First Discovery |
| L01 | Ingress Fundamentals | L1 | 30 min | 5 | **Foundation** | Socratic Dialogue |
| L02 | Traefik Ingress Controller | L1 | 35 min | 6 | **Foundation** | Hands-On Discovery |
| L03 | Gateway API - The New Standard | L1->L2 | 40 min | 7 | **Foundation->Application** | Specification-First |
| L04 | Envoy Gateway Setup | L2 | 35 min | 6 | **Application** | Guided Installation |
| L05 | Traffic Routing with HTTPRoute | L2 | 40 min | 7 | **Application** | Hands-On Creation |
| L06 | Rate Limiting & Circuit Breaking | L2 | 45 min | 8 | **Application** | Error Analysis |
| L07 | TLS Termination with CertManager | L2 | 40 min | 6 | **Integration** | Iterative Configuration |
| L08 | Traffic Splitting Patterns | L2 | 35 min | 5 | **Integration** | Collaborative Debugging |
| L09 | Autoscaling with HPA, VPA & KEDA | L2 | 45 min | 8 | **Integration** | Hands-On Discovery |
| L10 | Resilience Patterns | L2->L3 | 40 min | 7 | **Integration->Intelligence** | Pattern Recognition |
| L11 | Envoy AI Gateway for LLM Traffic | L3 | 45 min | 6 | **Intelligence** | AI Collaboration |
| L12 | Capstone - Production Traffic for Task API | L4 | 60 min | Integration | **Mastery** | Spec-Driven Project |

### Layer Progression Mapping

**L00-L02 (L1: Manual Foundation)**:
- Build skill, understand vocabulary, explore manual approaches
- NO AI assistance yet (except for skill creation in L00)
- Students develop mental models for evaluation

**L03-L06 (L1->L2: Manual to Collaboration)**:
- Transition from manual Gateway API configuration to AI-assisted patterns
- Three Roles begin: AI suggests patterns, student refines
- Layer 2 lessons include "Reflect on Your Skill" sections

**L07-L09 (L2: Collaboration)**:
- Full AI collaboration with TLS, traffic splitting, autoscaling
- Bidirectional learning: student teaches AI their constraints
- Each lesson improves the student's traffic-engineer skill

**L10-L11 (L2->L3: Collaboration to Intelligence)**:
- Recognize patterns worth encoding
- Create reusable resilience and AI-specific traffic patterns
- Student skill gains production-ready components

**L12 (L4: Orchestration/Capstone)**:
- Specification-first approach
- Compose all accumulated intelligence
- Produce production-ready Traffic API configuration as Digital FTE component

### Teaching Modality Variation

Each lesson uses distinct modality to prevent convergence:

1. **L00**: Skill-First Discovery (Context7 docs -> skill creation)
2. **L01**: Socratic Dialogue (Why north-south traffic? Why not Service directly?)
3. **L02**: Hands-On Discovery (Install Traefik, observe behavior)
4. **L03**: Specification-First (Gateway API spec BEFORE implementation)
5. **L04**: Guided Installation (Helm install with verification)
6. **L05**: Hands-On Creation (Write HTTPRoute from requirements)
7. **L06**: Error Analysis (Exceed rate limit -> observe 429 -> configure correctly)
8. **L07**: Iterative Configuration (CertManager -> test -> refine)
9. **L08**: Collaborative Debugging (Traffic split issues -> AI helps debug)
10. **L09**: Hands-On Discovery (KEDA triggers, observe scaling)
11. **L10**: Pattern Recognition (Identify retry/timeout/PDB patterns worth encoding)
12. **L11**: AI Collaboration (Token-based limiting, provider fallback with AI guidance)
13. **L12**: Spec-Driven Project (Write spec -> compose skills -> implement -> validate)

---

## Detailed Lesson Plans

### L00: Build Your Traffic Engineering Skill

**Purpose**: Skill-First pattern - students create their `traffic-engineer` skill BEFORE learning content, establishing ownership of learning outcome as Digital FTE asset.

**Learning Objectives** (Bloom's: Apply, Create):
- Clone skills-lab fresh (no state assumptions)
- Write LEARNING-SPEC.md for traffic engineering
- Fetch official Envoy Gateway docs via Context7
- Create initial traffic-engineer skill using /skill-creator

**Concepts** (4 total):
1. LEARNING-SPEC.md structure (intent, success criteria)
2. Context7 documentation fetching
3. Skill structure (SKILL.md, allowed-tools)
4. Grounded knowledge vs. AI memory

**Teaching Modality**: Skill-First Discovery

**Hands-On Exercises**:
1. Clone fresh skills-lab repository
2. Write LEARNING-SPEC.md with:
   - What: Gateway API + rate limiting + autoscaling skill
   - Why: Control external traffic to AI agents
   - Success: Skill generates valid Gateway+HTTPRoute YAML
3. Fetch docs: `/fetching-library-docs envoy-gateway`
4. Create skill: `/skill-creator traffic-engineer`
5. Test: Generate sample Gateway YAML, apply to cluster, verify acceptance

**Student Skill Output**:
```
.claude/skills/traffic-engineer/
  SKILL.md (initial version)
  references/ (fetched documentation)
```

**Assessment**: Student has working skill that generates syntactically valid Kubernetes Gateway API resources

**Prerequisites**: Fresh clone of skills-lab, Docker Desktop K8s enabled

**Reflect on Your Skill**: "What patterns from the official docs did your skill capture? What's missing that you'll add as you learn more?"

---

### L01: Ingress Fundamentals

**Purpose**: Build vocabulary and mental model for north-south traffic patterns.

**Learning Objectives** (Bloom's: Understand, Analyze):
- Explain difference between ClusterIP, NodePort, LoadBalancer, and Ingress
- Identify why Ingress (and Gateway API) exist
- Analyze Ingress limitations that motivated Gateway API
- Articulate the "annotation chaos" problem

**Concepts** (5 total):
1. North-south vs. east-west traffic
2. Service types (ClusterIP, NodePort, LoadBalancer)
3. Ingress resource (L7 routing)
4. Ingress annotations (provider-specific)
5. Ingress limitations (no role separation, vendor lock-in)

**Teaching Modality**: Socratic Dialogue
- "Why can't ClusterIP expose your API to the internet?"
- "Why does LoadBalancer work but isn't ideal for 50 services?"
- "What happens when you need rate limiting with Ingress?"

**Hands-On Exercises**:
1. Examine Task API Service (ClusterIP) - why can't we access from browser?
2. Try kubectl port-forward - what's the limitation?
3. Look at Ingress annotation examples - count the vendor-specific fields
4. Articulate: "If I switch from NGINX to Traefik, what breaks?"

**Assessment**: Student can explain why Ingress exists and articulate 3+ limitations

**Prerequisites**: Task API deployed on K8s (from Ch50)

**Reflect on Your Skill**: "What decision logic should your skill include for choosing Service type vs Ingress vs Gateway API?"

---

### L02: Traefik Ingress Controller

**Purpose**: Experience a simpler Ingress solution before the full Gateway API complexity.

**Learning Objectives** (Bloom's: Apply, Analyze):
- Install Traefik via Helm
- Create IngressRoute for Task API
- Configure Middleware (rate limiting, headers)
- Compare Traefik approach to Gateway API

**Concepts** (6 total):
1. Helm installation for Traefik
2. IngressRoute CRD (Traefik-specific)
3. Middleware concept
4. Rate limiting with Traefik
5. Dashboard access
6. Traefik vs Gateway API comparison

**Teaching Modality**: Hands-On Discovery

**Hands-On Exercises**:
1. Install Traefik: `helm install traefik traefik/traefik`
2. Create IngressRoute for Task API (/api/v1/tasks)
3. Access Task API via Traefik (port 80)
4. Add rate limiting Middleware (10 requests/minute)
5. Test: exceed limit, observe 429
6. Compare: What's Traefik-specific? What's portable?

**Assessment**: Task API accessible via Traefik, rate limiting functional

**Prerequisites**: L01

**Reflect on Your Skill**: "Your skill should recommend Traefik when: [fill in]. It should recommend Gateway API when: [fill in]."

---

### L03: Gateway API - The New Standard

**Purpose**: Understand Gateway API as the Kubernetes-standard replacement for Ingress.

**Learning Objectives** (Bloom's: Understand, Apply):
- Explain GatewayClass, Gateway, HTTPRoute hierarchy
- Understand role separation (infra admin vs app developer)
- Apply Gateway API to Task API routing
- Compare portability: Gateway API vs Ingress annotations

**Concepts** (7 total):
1. GatewayClass (cluster-scoped, like StorageClass)
2. Gateway (namespace-scoped, listeners)
3. HTTPRoute (L7 routing rules)
4. GRPCRoute (gRPC-specific routing)
5. ReferenceGrant (cross-namespace access)
6. Role separation (platform team vs app team)
7. Controller implementation (Envoy, Traefik, Kong)

**Teaching Modality**: Specification-First
- Show Gateway API resource hierarchy BEFORE writing YAML
- Students understand the WHAT before the HOW

**Hands-On Exercises**:
1. Read Gateway API spec for GatewayClass
2. Write GatewayClass YAML (envoy-gateway controller)
3. Write Gateway YAML (HTTP listener on port 80)
4. Write HTTPRoute YAML (route /api/v1/* to task-api Service)
5. Apply all three resources
6. Access Task API via Gateway

**Assessment**: Student explains role separation, has working Gateway routing

**Prerequisites**: L02 (Traefik comparison context)

**Reflect on Your Skill**: "Add Gateway API pattern generation to your skill. What's the minimum valid configuration?"

---

### L04: Envoy Gateway Setup

**Purpose**: Install and configure Envoy Gateway as the production-grade Gateway API implementation.

**Learning Objectives** (Bloom's: Apply):
- Install Envoy Gateway via Helm
- Understand Envoy Gateway architecture (control plane + data plane)
- Verify xDS protocol functioning
- Configure EnvoyProxy settings

**Concepts** (6 total):
1. Envoy Gateway Helm chart
2. Control plane components (Gateway Translator, xDS Server, Infra Manager)
3. Data plane (Envoy proxies)
4. xDS protocol (dynamic configuration)
5. EnvoyProxy CRD (deployment customization)
6. Gateway API CRD installation

**Teaching Modality**: Guided Installation
- Step-by-step Helm install with verification checkpoints
- Troubleshooting common issues

**Hands-On Exercises**:
1. Install Gateway API CRDs
2. Install Envoy Gateway: `helm install eg oci://docker.io/envoyproxy/gateway-helm --version v1.6.1 -n envoy-gateway-system --create-namespace`
3. Wait for deployment: `kubectl wait --for=condition=Available deployment/envoy-gateway -n envoy-gateway-system`
4. Verify GatewayClass created: `kubectl get gatewayclass`
5. Examine Envoy pods: `kubectl get pods -n envoy-gateway-system`
6. Check logs for xDS activity

**Assessment**: Envoy Gateway running, GatewayClass available

**Prerequisites**: L03

**Reflect on Your Skill**: "Add Envoy Gateway installation commands to your skill. What verification steps are essential?"

---

### L05: Traffic Routing with HTTPRoute

**Purpose**: Master HTTPRoute matching patterns for production routing.

**Learning Objectives** (Bloom's: Apply, Analyze):
- Configure path-based routing
- Configure header-based routing
- Configure query parameter matching
- Implement traffic weights for backend splitting
- Create GRPCRoute for gRPC services

**Concepts** (7 total):
1. Path matching (Exact, PathPrefix, RegularExpression)
2. Header matching (Exact, Distinct)
3. Query parameter matching
4. Method matching
5. Traffic weights (backendRefs with weight)
6. Multiple rules ordering
7. GRPCRoute basics

**Teaching Modality**: Hands-On Creation
- Given requirements, write HTTPRoute from scratch
- Test each matching pattern

**Hands-On Exercises**:
1. Create HTTPRoute with path matching:
   - /api/v1/tasks -> task-api Service
   - /health -> task-api Service (different path handling)
2. Add header-based routing: x-version: v2 -> task-api-v2
3. Add query parameter matching: ?debug=true -> debug endpoint
4. Configure traffic weights: 90% stable, 10% canary
5. Test all patterns with curl

**Assessment**: All routing patterns functional, student can write HTTPRoute from requirements

**Prerequisites**: L04

**Reflect on Your Skill**: "Your skill should now generate HTTPRoute for common patterns. Add templates for: path-based, header-based, traffic splitting."

---

### L06: Rate Limiting & Circuit Breaking

**Purpose**: Protect services from abuse and cost overruns with BackendTrafficPolicy.

**Learning Objectives** (Bloom's: Apply, Analyze, Evaluate):
- Configure local rate limiting
- Configure global rate limiting (with Redis)
- Implement per-user rate limits via headers
- Configure circuit breaker patterns
- Observe rate limit behavior through Envoy metrics

**Concepts** (8 total):
1. BackendTrafficPolicy CRD
2. Local rate limiting (per-proxy bucket)
3. Global rate limiting (shared quota via Redis)
4. Rate limit descriptors (headers, paths)
5. Per-user limits (x-user-id header)
6. Circuit breaker configuration
7. Health checks for circuit breaker
8. Policy merging (Gateway + HTTPRoute)

**Teaching Modality**: Error Analysis
- Deliberately exceed rate limit
- Observe 429 responses
- Configure correctly based on observed behavior

**Hands-On Exercises**:
1. Create BackendTrafficPolicy with rate limit: 100 requests/minute
2. Apply to HTTPRoute
3. Generate traffic: `for i in {1..150}; do curl -s -o /dev/null -w "%{http_code}\n" http://gateway/api/v1/tasks; done`
4. Observe: 429 after 100 requests
5. Add per-user limit using x-user-id header
6. Test: different x-user-id values have independent quotas
7. Configure circuit breaker: maxConnections 100, maxPendingRequests 50
8. View Envoy metrics for rate limit decisions

**Assessment**: Rate limiting functional, per-user limits working, circuit breaker configured

**Prerequisites**: L05

**Reflect on Your Skill**: "Add rate limiting patterns to your skill. Include decision logic: When to use local vs global rate limiting?"

---

### L07: TLS Termination with CertManager

**Purpose**: Secure traffic with TLS, automated certificate management.

**Learning Objectives** (Bloom's: Apply):
- Install CertManager via Helm
- Create ClusterIssuer for Let's Encrypt (staging)
- Create Certificate resource
- Configure Gateway with TLS listener
- Verify HTTPS access

**Concepts** (6 total):
1. CertManager Helm installation
2. ClusterIssuer (cluster-wide certificate authority)
3. Let's Encrypt ACME protocol
4. Certificate resource (auto-renewal)
5. Gateway TLS listener configuration
6. TLS secret management

**Teaching Modality**: Iterative Configuration
- Install -> Configure -> Test -> Troubleshoot -> Refine

**Hands-On Exercises**:
1. Install CertManager: `kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.16.0/cert-manager.yaml`
2. Create ClusterIssuer (Let's Encrypt staging to avoid rate limits)
3. Create Certificate for tasks.example.com (using staging)
4. Verify TLS secret created: `kubectl get secrets | grep tls`
5. Update Gateway with HTTPS listener (port 443, TLS mode Terminate)
6. Access via HTTPS: `curl -k https://localhost/api/v1/tasks` (self-signed for Docker Desktop)
7. Troubleshoot if certificate not issued

**Assessment**: HTTPS listener functional, certificate auto-generated

**Prerequisites**: L06

**Reflect on Your Skill**: "Add TLS configuration patterns. Include staging vs production issuer decision logic."

---

### L08: Traffic Splitting Patterns

**Purpose**: Implement canary, blue-green, and A/B testing deployment patterns.

**Learning Objectives** (Bloom's: Apply, Evaluate):
- Implement canary deployment with traffic weights
- Implement header-based A/B testing
- Implement blue-green switching
- Evaluate rollback strategies

**Concepts** (5 total):
1. Canary deployment (gradual rollout)
2. Traffic weights (90/10, 80/20, etc.)
3. Header-based routing for A/B testing
4. Blue-green deployment (instant switch)
5. Rollback patterns (weight 0 for failed canary)

**Teaching Modality**: Collaborative Debugging
- Deploy canary version
- Observe unexpected behavior
- Debug with AI assistance (HTTPRoute configuration issues)

**Hands-On Exercises**:
1. Deploy task-api-v2 (canary version)
2. Configure HTTPRoute: 90% v1, 10% v2
3. Generate traffic and observe both versions receive requests
4. Add header-based routing: x-beta-user: true -> always v2
5. Test header routing: `curl -H "x-beta-user: true" http://gateway/api/v1/tasks`
6. Simulate failed canary: update weights to 100% v1, 0% v2
7. Verify immediate rollback

**Assessment**: Traffic splitting functional, header routing working, rollback demonstrated

**Prerequisites**: L07

**Reflect on Your Skill**: "Add deployment pattern templates. Include decision framework: When to use canary vs blue-green?"

---

### L09: Autoscaling with HPA, VPA & KEDA

**Purpose**: Intelligent capacity management based on demand.

**Learning Objectives** (Bloom's: Apply, Analyze):
- Configure HPA for CPU-based scaling
- Understand VPA for vertical scaling
- Install KEDA for event-driven scaling
- Configure ScaledObject with Prometheus scaler
- Configure ScaledObject with Kafka scaler
- Observe scale-to-zero behavior

**Concepts** (8 total):
1. HPA (Horizontal Pod Autoscaler)
2. Metrics Server requirement
3. VPA (Vertical Pod Autoscaler)
4. KEDA architecture
5. ScaledObject CRD
6. Prometheus scaler
7. Kafka scaler (consumer lag)
8. Scale-to-zero and activation

**Teaching Modality**: Hands-On Discovery
- Install KEDA
- Configure scalers
- Generate load and observe scaling

**Hands-On Exercises**:
1. Verify metrics-server installed (for HPA)
2. Create HPA: target 70% CPU
3. Generate load: `hey -z 2m -c 50 http://gateway/api/v1/tasks`
4. Observe pods scaling up
5. Install KEDA: `helm install keda kedacore/keda -n keda --create-namespace`
6. Create ScaledObject with Prometheus scaler
7. Generate traffic, observe KEDA scaling
8. Wait idle, observe scale-to-zero

**Assessment**: HPA scales on CPU, KEDA scales on custom metrics, scale-to-zero observed

**Prerequisites**: L08, Prometheus from Ch55

**Reflect on Your Skill**: "Add autoscaling patterns. Include: HPA for simple cases, KEDA for event-driven, scale-to-zero for cost savings."

---

### L10: Resilience Patterns

**Purpose**: Production-grade resilience with retries, timeouts, PDB, and probes.

**Learning Objectives** (Bloom's: Apply, Analyze, Evaluate):
- Configure retry policies with backoff
- Configure timeout settings
- Create PodDisruptionBudget
- Configure liveness and readiness probes
- Implement graceful shutdown

**Concepts** (7 total):
1. Retry policy (numRetries, retryOn conditions)
2. Backoff strategy (exponential)
3. Timeout configuration (request, idle)
4. PodDisruptionBudget (minAvailable)
5. Liveness vs readiness probes
6. Graceful shutdown (preStop hook)
7. Outlier detection

**Teaching Modality**: Pattern Recognition
- Identify which patterns are worth encoding into skill
- Recognize production-essential vs nice-to-have

**Hands-On Exercises**:
1. Configure BackendTrafficPolicy retry: 3 attempts, 5xx and connect-failure
2. Add backoff: baseInterval 100ms, maxInterval 10s
3. Configure timeout: 30s request timeout
4. Create PDB: minAvailable 1
5. Verify: delete pod, observe PDB protection
6. Configure graceful shutdown in deployment (preStop hook)
7. Test graceful shutdown: kubectl drain

**Assessment**: Retries working, PDB protecting, graceful shutdown verified

**Prerequisites**: L09

**Reflect on Your Skill**: "Which resilience patterns should ALWAYS be included? Which are situational? Update your skill's decision logic."

---

### L11: Envoy AI Gateway for LLM Traffic

**Purpose**: AI-specific traffic management for cost control and reliability.

**Learning Objectives** (Bloom's: Apply, Evaluate, Create):
- Understand token-based vs request-based rate limiting
- Configure token budgets per user
- Implement provider fallback (OpenAI -> Anthropic)
- Configure model-specific routing
- Evaluate cost implications

**Concepts** (6 total):
1. Envoy AI Gateway architecture
2. Token-based rate limiting
3. Token budget (per-user, per-minute)
4. Provider fallback chain
5. Model routing (gpt-4 -> priority chain)
6. Cost engineering for LLM traffic

**Teaching Modality**: AI Collaboration (Three Roles INVISIBLE)

**CRITICAL IMPLEMENTATION NOTE**:
This lesson demonstrates bidirectional learning. The Three Roles framework is INTERNAL to planning - INVISIBLE in student-facing content.

**Hands-On Exercises**:

**Part 1: Initial Request**
- Ask AI: "Configure rate limiting for my LLM proxy that limits tokens, not requests"
- Review output
- Reflection: What's different from request-based limiting?

**Part 2: Critical Evaluation**
- Does token limiting work for my budget constraints?
- What happens when budget exhausted?
- How does this affect user experience?

**Part 3: Constraint Teaching**
- Tell AI: "We have a $100/day budget across all users"
- AI adapts configuration
- Observe: How did AI translate dollars to token limits?

**Part 4: Provider Fallback**
- Ask AI: "Add fallback from OpenAI to Anthropic when rate limited"
- Review model name mapping (gpt-4 -> claude-3-opus)
- Test fallback logic

**Part 5: Reflection**
- Compare initial to final configuration
- What did collaboration achieve?
- What patterns should your skill encode?

**Assessment**: Token limiting configured, provider fallback working, cost implications understood

**Prerequisites**: L10

**Reflect on Your Skill**: "Add LLM-specific patterns to your skill. Include: token budgets, provider fallback, cost calculation."

---

### L12: Capstone - Production Traffic for Task API

**Purpose**: Integrate all patterns for production-ready Task API traffic management.

**Learning Objectives** (Bloom's: Create, Evaluate):
- Write specification for complete traffic configuration
- Compose all L00-L11 techniques
- Build production-grade gateway configuration
- Validate against success criteria
- Finalize traffic-engineer skill

**Concepts** (Integration across 12 lessons):
- Specification-driven approach
- End-to-end workflow
- Composition of accumulated intelligence
- Production validation

**Teaching Modality**: Spec-Driven Project

**Project Structure**:

**Phase 1: Specification Writing** (15-20 min)
Write spec.md answering:
- What traffic configuration does Task API need for production?
- What are the success criteria (TLS, rate limiting, autoscaling)?
- What constraints exist (Docker Desktop K8s, no cloud LB)?
- Which accumulated patterns apply?

**Phase 2: Skill Composition** (20-25 min)
Apply your traffic-engineer skill to generate:
- GatewayClass + Gateway configuration
- HTTPRoute for Task API with versioned paths
- BackendTrafficPolicy for rate limiting
- TLS configuration (self-signed for local)
- KEDA ScaledObject for autoscaling

**Phase 3: Implementation** (15-20 min)
1. Apply all resources to cluster
2. Verify Gateway accepts traffic
3. Test rate limiting (exceed threshold, observe 429)
4. Test TLS (HTTPS access)
5. Generate load, observe KEDA scaling

**Phase 4: Validation** (5-10 min)
1. External access: `curl http://localhost/api/v1/tasks` returns 200
2. Rate limiting: Exceeding threshold returns 429
3. HTTPS: `curl -k https://localhost/api/v1/tasks` works
4. Autoscaling: Pods scale under load

**Phase 5: Skill Finalization** (5-10 min)
- Review skill against all 12 lessons
- Add missing patterns discovered during capstone
- Document decision logic for common scenarios
- Commit final skill version

**Hands-On Deliverables**:
1. spec.md (150-200 words, clear acceptance criteria)
2. Production Gateway + HTTPRoute configuration
3. BackendTrafficPolicy with rate limiting
4. KEDA ScaledObject
5. Finalized traffic-engineer skill with all patterns

**Assessment**:
- SC-001: External access via Gateway works
- SC-002: Rate limiting rejects requests exceeding threshold
- SC-003: HTTPS access functional
- SC-004: KEDA scales pods under load
- SC-005: Student owns tested traffic-engineer skill

**Prerequisites**: L00-L11 (all traffic engineering fundamentals)

**Reflect on Your Skill**: "Your skill is now complete. It should handle: Gateway setup, routing, rate limiting, TLS, autoscaling, LLM traffic. What edge cases need documentation?"

---

## Cognitive Load Analysis

All lessons respect B1 cognitive load limits (7-10 concepts per lesson):

| Lesson | Concepts | Assessment |
|--------|----------|------------|
| L00 | 4 | Within A2 limit (foundational) |
| L01 | 5 | Within A2-B1 limit |
| L02 | 6 | Within B1 limit |
| L03 | 7 | At B1 limit |
| L04 | 6 | Within B1 limit |
| L05 | 7 | At B1 limit |
| L06 | 8 | Within B1 limit |
| L07 | 6 | Within B1 limit |
| L08 | 5 | Within B1 limit |
| L09 | 8 | Within B1 limit |
| L10 | 7 | At B1 limit |
| L11 | 6 | Within B1 limit |
| L12 | Integration | Capstone (no new concepts) |

**Maximum concept introduction**: 8 (L06, L09) - within B1 limit of 10

---

## Intelligence Creation Opportunities

**Lessons that create reusable intelligence for student's skill**:

| Lesson | Pattern Encoded | Skill Component |
|--------|-----------------|-----------------|
| L00 | Initial skill structure | SKILL.md foundation |
| L01 | Service type decision logic | When to use Ingress vs Gateway |
| L02 | Traefik patterns | Simple ingress scenarios |
| L03 | Gateway API templates | GatewayClass, Gateway, HTTPRoute |
| L05 | Routing patterns | Path, header, traffic splitting |
| L06 | Protection patterns | Rate limiting, circuit breaking |
| L07 | TLS patterns | CertManager integration |
| L08 | Deployment patterns | Canary, blue-green, A/B |
| L09 | Scaling patterns | HPA, KEDA, scale-to-zero |
| L10 | Resilience patterns | Retry, timeout, PDB |
| L11 | LLM patterns | Token limiting, provider fallback |
| L12 | Composition pattern | Full production configuration |

---

## Constitution Compliance

- [x] Layer progression: L1 (L00-L02) -> L1-L2 (L03-L06) -> L2 (L07-L09) -> L2-L3 (L10-L11) -> L4 (L12)
- [x] Three Roles in L11: INVISIBLE (no framework labels in student content)
- [x] Teaching modality variation: All 13 lessons use different modalities
- [x] Specification primacy: L03, L12 spec-first before implementation
- [x] Meta-commentary prohibition: Zero "What to notice", "AI as Teacher"
- [x] Minimal content: Only content mapping to objectives
- [x] All concepts <= B1 tier limits (max 8, limit 10)
- [x] Skill-First pattern: L00 creates skill, all lessons include "Reflect on Your Skill"
- [x] Agent Factory alignment: Produces sellable traffic-engineer skill

---

## Success Criteria Mapping (from Spec)

| Success Criteria | Lesson Coverage |
|------------------|-----------------|
| SC-001: Access Task API via Gateway within 15 min | L03-L05 |
| SC-002: Rate limiting rejects requests exceeding threshold | L06 |
| SC-003: Canary deployment with verifiable traffic splitting | L08 |
| SC-004: KEDA autoscaling scales pods on Prometheus metrics | L09 |
| SC-005: Tested traffic-engineer skill | L00, L12 |
| SC-006: Production-ready traffic configuration | L12 |
| SC-007: 100% code examples work on Docker Desktop K8s | All lessons |

---

## Skill Dependency Graph

```
L00 (Create Skill) - no prerequisites
    |
L01 (Ingress Fundamentals) - requires K8s from Ch50
    |
L02 (Traefik) - requires L01
    |
L03 (Gateway API) - requires L02
    |
L04 (Envoy Gateway) - requires L03
    |
L05 (HTTPRoute) - requires L04
    |
L06 (Rate Limiting) - requires L05
    |
L07 (TLS) - requires L06
    |
L08 (Traffic Splitting) - requires L07
    |
L09 (Autoscaling) - requires L08, Prometheus from Ch55
    |
L10 (Resilience) - requires L09
    |
L11 (AI Gateway) - requires L10
    |
L12 (Capstone) - requires L00-L11
```

**Cross-Chapter Dependencies**:
- Ch49: Docker (Task API image)
- Ch50: Kubernetes fundamentals (Pods, Services, Deployments)
- Ch51: Helm charts (installation method)
- Ch52: Kafka/Strimzi (KEDA Kafka scaler example)
- Ch55: Observability (Prometheus metrics for KEDA)

---

## Writing Instructions for Content Implementer

### Lesson Template Structure

Each lesson should follow:
```markdown
---
sidebar_position: [N]
title: "Lesson [N]: [Title]"
description: "[One-line description]"
---

# [Title]

[Compelling opening connecting to reader's goals - why this matters for their Digital FTE]

## Learning Objectives

- [Bloom's verb] [measurable outcome]
...

## Key Concepts

- **[Concept]**: [Brief explanation]
...

## [Main Content Sections]
- Content matching teaching modality from plan
- Hands-on exercises (numbered, testable)
- Code examples (validated, work on Docker Desktop K8s)

## Reflect on Your Skill

[Questions prompting skill improvement based on lesson content]

## Try With AI

[For L2+ only: Action prompts + reflection, NO framework labels]
- Part 1: Initial Request
- Part 2: Critical Evaluation
- Part 3: Constraint Teaching
- Part 4: Refinement
- Part 5: Final Check
```

### Skill-First Enforcement

Every lesson MUST include:
1. **Lesson opening**: Connect to building the student's traffic-engineer skill
2. **"Reflect on Your Skill" section**: How does this lesson improve the skill?
3. **Skill testing**: What can the skill now generate that it couldn't before?

### Forbidden Patterns

- Layer/Stage labels in student content
- "What to notice" meta-commentary
- "AI is teaching you" framework exposition
- "Key Takeaways" final section
- Summary sections
- Kong references (use Envoy Gateway as primary)

### Required Patterns

- Clear learning objectives (Bloom's level)
- Hands-on exercises (testable on Docker Desktop K8s)
- Concept inventory matching plan
- Teaching modality from plan
- "Reflect on Your Skill" section (ALL lessons)
- "Try With AI" only final section (L2+ lessons)
- Code examples with kubectl commands

---

## Implementation Timeline

**Lesson Writing Sequence** (must follow dependencies):

| Lesson | Estimated Hours | Dependencies |
|--------|-----------------|--------------|
| L00 | 2-3 | None |
| L01 | 2-3 | L00 |
| L02 | 2-3 | L01 |
| L03 | 3-4 | L02 |
| L04 | 2-3 | L03 |
| L05 | 3-4 | L04 |
| L06 | 3-4 | L05 |
| L07 | 3-4 | L06 |
| L08 | 2-3 | L07 |
| L09 | 3-4 | L08 |
| L10 | 3-4 | L09 |
| L11 | 4-5 | L10 (Three Roles framework understanding) |
| L12 | 4-5 | L00-L11 (spec-driven approach understanding) |

**Total**: ~38-48 hours of content creation

---

## Plan Status

**READY FOR IMPLEMENTATION**

All 13 lessons designed with:
- Clear pedagogical objectives
- Varied teaching modalities
- Proper Layer progression (L1 -> L2 -> L3 -> L4)
- Constitutional compliance (v7.0.0)
- Hardware tier compatibility (Docker Desktop K8s)
- Success criteria mapping
- Skill-First pattern enforcement
- "Reflect on Your Skill" sections

Content-implementer can begin writing with confidence and clarity.

---

## Appendix: Technology Quick Reference

**Versions** (from spec):
- Gateway API: v1.2+
- Envoy Gateway: v1.6+
- Traefik: v3.x (comparison only)
- KEDA: v2.18+
- CertManager: v1.16+
- Envoy AI Gateway: v0.4+ (conceptual, may be preview)

**Key CRDs**:
- GatewayClass, Gateway, HTTPRoute, GRPCRoute (Gateway API)
- BackendTrafficPolicy, ClientTrafficPolicy, SecurityPolicy (Envoy Gateway)
- ScaledObject (KEDA)
- Certificate, ClusterIssuer (CertManager)

**Expertise Skill Reference**: `.claude/skills/building-with-envoy-gateway/SKILL.md`
- Use for verified patterns and decision logic
- Contains production examples for Task API
