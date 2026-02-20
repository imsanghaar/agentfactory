# Feature Specification: Chapter 56 - Traffic Engineering

**Feature Branch**: `001-ch56-traffic-engineering`
**Created**: 2025-12-30
**Status**: Draft
**Input**: Chapter 56: Traffic Engineering - Gateway API, Envoy & Autoscaling for Part 7 AI Cloud Native Development

---

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Docker containerization and multi-stage builds (Ch49)
- Kubernetes fundamentals: Pods, Deployments, Services, Namespaces (Ch50)
- Helm charts for package management (Ch51)
- Event-driven architecture with Kafka/Strimzi (Ch52)
- Dapr sidecar patterns for service invocation (Ch53)
- GitOps with Argo CD for declarative deployments (Ch54)
- Observability with Prometheus, Grafana, OpenTelemetry (Ch55)
- Running example: Task API deployed on Docker Desktop Kubernetes

**What this chapter must explain from scratch**:
- Why Ingress API is being replaced (limitations, annotation chaos)
- Gateway API as the new Kubernetes standard (GatewayClass, Gateway, HTTPRoute)
- Envoy Gateway architecture (control plane + data plane)
- BackendTrafficPolicy, ClientTrafficPolicy, SecurityPolicy CRDs
- KEDA event-driven autoscaling beyond HPA
- Envoy AI Gateway for LLM traffic management (unique to this book)

---

## Chapter Overview

**Proficiency Level**: B1 (Intermediate)
**Part**: 7 - AI Cloud Native Development (Tier 2: Enterprise)
**Chapter Number**: 56
**Total Duration**: ~8 hours (13 lessons)
**Running Example**: Task API with production traffic management

**Chapter Narrative**: Your Task API is deployed on Kubernetes with observability. But external users can't reach it, and there's no protection against traffic spikes or cost overruns. This chapter adds the "front door" - routing external traffic to your services, protecting them with rate limiting and circuit breakers, securing connections with TLS, and scaling intelligently based on actual demand.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Build Traffic Engineering Skill (Priority: P1)

Students build their own `traffic-engineer` skill before learning the content, establishing ownership of the learning outcome as a Digital FTE asset.

**Why this priority**: Skill-First pattern - students own a sellable skill, not just knowledge. This skill is tested and improved throughout the chapter.

**Independent Test**: Student can invoke their skill to generate valid Gateway + HTTPRoute YAML that passes kubectl validation.

**Acceptance Scenarios**:

1. **Given** a fresh clone of skills-lab, **When** student writes LEARNING-SPEC.md and fetches Envoy Gateway docs via Context7, **Then** they have a grounded foundation for skill creation
2. **Given** official documentation, **When** student uses /skill-creator to build traffic-engineer skill, **Then** skill generates syntactically valid Kubernetes Gateway API resources
3. **Given** a completed skill, **When** student applies generated resources to Docker Desktop K8s, **Then** resources are accepted without errors

---

### User Story 2 - Expose Services via Gateway API (Priority: P1)

Students route external traffic to their Task API using Gateway API instead of legacy Ingress, learning the new Kubernetes standard.

**Why this priority**: Core functionality - without external access, no other traffic engineering matters.

**Independent Test**: Student can access Task API endpoints from their browser or curl via the Gateway.

**Acceptance Scenarios**:

1. **Given** Task API deployed on K8s, **When** student creates GatewayClass + Gateway + HTTPRoute, **Then** external requests reach Task API
2. **Given** multiple path prefixes (/api/v1, /health), **When** student configures HTTPRoute matching rules, **Then** requests route to correct endpoints
3. **Given** a working HTTPRoute, **When** student modifies traffic weights, **Then** requests split between backends as configured

---

### User Story 3 - Protect Services with Rate Limiting (Priority: P2)

Students protect their Task API from abuse and cost overruns using BackendTrafficPolicy rate limiting.

**Why this priority**: Production requirement - unprotected APIs get abused, costs explode.

**Independent Test**: Student can trigger rate limiting by exceeding configured thresholds and observe 429 responses.

**Acceptance Scenarios**:

1. **Given** an HTTPRoute with BackendTrafficPolicy, **When** requests exceed 100/minute threshold, **Then** additional requests receive 429 Too Many Requests
2. **Given** per-user rate limits via x-user-id header, **When** different users make requests, **Then** each user has independent rate limit quota
3. **Given** rate limit configuration, **When** student monitors Envoy metrics, **Then** rate limit decisions are observable

---

### User Story 4 - Secure with TLS (Priority: P2)

Students terminate TLS at the gateway using CertManager for automated certificate management.

**Why this priority**: Security requirement - production traffic must be encrypted.

**Independent Test**: Student can access Task API via HTTPS with valid certificate (even self-signed for local development).

**Acceptance Scenarios**:

1. **Given** CertManager installed, **When** student creates Certificate resource, **Then** TLS secret is generated automatically
2. **Given** Gateway with TLS listener, **When** client connects via HTTPS, **Then** connection is encrypted
3. **Given** staging issuer, **When** student tests certificate workflow, **Then** no rate limiting from Let's Encrypt production

---

### User Story 5 - Scale Based on Demand (Priority: P2)

Students configure autoscaling using HPA, VPA, and KEDA for intelligent capacity management.

**Why this priority**: Cost efficiency - scale up for demand, scale down (to zero) when idle.

**Independent Test**: Student can observe pod scaling in response to load (Prometheus metrics or Kafka lag).

**Acceptance Scenarios**:

1. **Given** HPA targeting 70% CPU, **When** load increases, **Then** pods scale up within configured limits
2. **Given** KEDA ScaledObject with Prometheus scaler, **When** request rate exceeds threshold, **Then** pods scale based on custom metrics
3. **Given** KEDA with Kafka scaler, **When** consumer lag grows, **Then** worker pods scale to process backlog
4. **Given** idle workload, **When** no requests for cooldown period, **Then** pods scale to zero (KEDA)

---

### User Story 6 - Deploy Canary Releases (Priority: P3)

Students implement canary and blue-green deployment patterns using HTTPRoute traffic splitting.

**Why this priority**: Advanced deployment strategy - reduces risk of releasing new versions.

**Independent Test**: Student can route 10% of traffic to canary version and verify both versions receive requests.

**Acceptance Scenarios**:

1. **Given** stable v1 and canary v2 deployments, **When** student configures 90/10 traffic weights, **Then** approximately 10% of requests go to v2
2. **Given** header-based routing, **When** x-version: v2 header is sent, **Then** request always routes to v2
3. **Given** failed canary, **When** student updates HTTPRoute to weight 0 for v2, **Then** all traffic returns to v1 immediately

---

### User Story 7 - Manage LLM Traffic Costs (Priority: P3)

Students apply Envoy AI Gateway patterns for token-based rate limiting and provider fallback.

**Why this priority**: AI-specific - unique value for AI agent developers, not covered by traditional gateway content.

**Independent Test**: Student can explain why token-based limits differ from request-based limits and configure provider fallback.

**Acceptance Scenarios**:

1. **Given** LLM endpoint behind AI Gateway, **When** token budget is exhausted, **Then** requests are rejected with budget exceeded error
2. **Given** multiple LLM providers configured, **When** primary provider rate limits, **Then** traffic fails over to secondary provider
3. **Given** model-specific routing, **When** request specifies gpt-4 model, **Then** routing follows configured priority chain

---

### Edge Cases

- What happens when CertManager fails to issue certificate? (Gateway serves without TLS, logs warning)
- How does system handle circuit breaker open state? (Returns 503 immediately, doesn't attempt backend)
- What happens when KEDA scaler connection fails? (Falls back to configured replica count)
- How does rate limiting behave during Redis unavailability? (Local rate limiting continues, global limits may exceed)

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Chapter MUST follow Skill-First pattern with L00 creating student's traffic-engineer skill
- **FR-002**: Each lesson MUST end with "Reflect on Your Skill" section testing and improving the student skill
- **FR-003**: Chapter MUST cover Gateway API as the Kubernetes standard replacing Ingress
- **FR-004**: Chapter MUST include Envoy Gateway installation and configuration via Helm
- **FR-005**: Chapter MUST teach HTTPRoute matching (path, header, query param, method)
- **FR-006**: Chapter MUST cover BackendTrafficPolicy for rate limiting and circuit breaking
- **FR-007**: Chapter MUST include TLS termination with CertManager integration
- **FR-008**: Chapter MUST teach traffic splitting for canary and blue-green deployments
- **FR-009**: Chapter MUST cover HPA, VPA, and KEDA autoscaling patterns
- **FR-010**: Chapter MUST include resilience patterns (retries, timeouts, PDB, probes)
- **FR-011**: Chapter MUST cover Envoy AI Gateway for LLM-specific traffic management
- **FR-012**: Capstone MUST integrate all patterns for production Task API traffic management
- **FR-013**: All code examples MUST work on Docker Desktop Kubernetes
- **FR-014**: Chapter MUST reference expertise skill at .claude/skills/building-with-envoy-gateway/

### Lesson Structure Requirements

| Lesson | Title | Duration | Layer | Key Concepts |
|--------|-------|----------|-------|--------------|
| L00 | Build Your Traffic Engineering Skill | 25 min | L1 | Skill-First, Context7, skill-creator |
| L01 | Ingress Fundamentals | 30 min | L1 | North-south traffic, Service types, Ingress limitations |
| L02 | Traefik Ingress Controller | 35 min | L1 | Helm install, IngressRoute, Middleware |
| L03 | Gateway API - The New Standard | 40 min | L1→L2 | GatewayClass, Gateway, HTTPRoute, Role separation |
| L04 | Envoy Gateway Setup | 35 min | L2 | Helm install, Architecture, xDS protocol |
| L05 | Traffic Routing with HTTPRoute | 40 min | L2 | Path/header/query matching, Traffic weights, GRPCRoute |
| L06 | Rate Limiting & Circuit Breaking | 45 min | L2 | BackendTrafficPolicy, Local vs Global, Policy merging |
| L07 | TLS Termination with CertManager | 40 min | L2 | ClusterIssuer, Let's Encrypt, mTLS |
| L08 | Traffic Splitting Patterns | 35 min | L2 | Canary, Blue-green, A/B testing, Rollback |
| L09 | Autoscaling with HPA, VPA & KEDA | 45 min | L2 | Metrics-server, ScaledObject, Scalers |
| L10 | Resilience Patterns | 40 min | L2→L3 | Retry, Timeout, PDB, Probes, Graceful shutdown |
| L11 | Envoy AI Gateway for LLM Traffic | 45 min | L3 | Token limits, Provider fallback, Cost control |
| L12 | Capstone - Production Traffic for Task API | 60 min | L4 | Full integration, Skill finalization |

### Key Entities

- **GatewayClass**: Cluster-scoped template defining gateway implementation (like StorageClass for networking)
- **Gateway**: Namespace-scoped traffic entry point with listeners (ports, protocols, hostnames)
- **HTTPRoute**: L7 routing rules with path/header/query matching and backend references
- **BackendTrafficPolicy**: Envoy Gateway CRD for rate limiting, retries, circuit breaker, load balancing
- **ClientTrafficPolicy**: Envoy Gateway CRD for TLS, timeouts, keepalive, connection limits
- **SecurityPolicy**: Envoy Gateway CRD for JWT, OIDC, CORS, IP allowlist (referenced, not implemented)
- **ScaledObject**: KEDA CRD for event-driven autoscaling with multiple trigger types
- **Certificate**: CertManager CRD for automated TLS certificate lifecycle

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can expose Task API via Gateway API and access it from browser/curl within 15 minutes of lesson completion
- **SC-002**: Students can configure rate limiting that demonstrably rejects requests exceeding threshold
- **SC-003**: Students can implement canary deployment with verifiable traffic splitting (observing both versions receive requests)
- **SC-004**: Students can configure KEDA autoscaling that scales pods in response to custom Prometheus metrics
- **SC-005**: Students own a tested traffic-engineer skill that generates valid Gateway + HTTPRoute + BackendTrafficPolicy resources
- **SC-006**: Capstone produces production-ready traffic configuration for Task API with TLS, rate limiting, and autoscaling
- **SC-007**: 100% of code examples execute successfully on Docker Desktop Kubernetes without cloud provider dependencies

### Learning Progression Validation

- L00-L02 establishes vocabulary: students can explain Gateway vs Ingress distinction
- L03-L06 builds core competency: students can create and debug Gateway API resources
- L07-L09 adds production concerns: students can secure and scale their gateway
- L10-L11 advances to intelligence: students recognize patterns and apply AI-specific solutions
- L12 demonstrates mastery: students orchestrate all components for production deployment

---

## Assumptions

- Docker Desktop Kubernetes is enabled and functional on student machine
- Helm 3.x is installed and configured
- kubectl is configured to communicate with Docker Desktop cluster
- Students have completed Ch49-55 prerequisites
- Task API from Ch40 is available for deployment
- Internet access available for Helm chart downloads and Let's Encrypt (staging)
- Students understand basic Kubernetes concepts (Pods, Services, Deployments, Namespaces)

---

## Scope Boundaries

### In Scope
- Gateway API v1.0+ with Envoy Gateway implementation
- Traefik as simpler alternative (comparison, not deep dive)
- Rate limiting, circuit breaking, retries, timeouts
- TLS termination with CertManager
- HPA, VPA, and KEDA autoscaling
- Canary and blue-green deployment patterns
- Envoy AI Gateway concepts for LLM traffic
- Docker Desktop Kubernetes as target platform

### Out of Scope
- Full authentication implementation (reference auth chapters)
- Service mesh (Istio/Linkerd) - separate topic
- Kong Gateway (Envoy is the focus)
- AWS/GCP-specific load balancers (portable K8s focus)
- Production cloud deployment (covered in later chapters)
- gRPC deep dive (GRPCRoute mentioned, not primary focus)

---

## Dependencies

- **Ch49**: Docker containerization (Task API image)
- **Ch50**: Kubernetes fundamentals (Pods, Services, Deployments)
- **Ch51**: Helm charts (installation method for all components)
- **Ch52**: Kafka/Strimzi (KEDA Kafka scaler example)
- **Ch55**: Observability (Prometheus metrics for KEDA, Grafana dashboards)
- **Expertise Skill**: .claude/skills/building-with-envoy-gateway/SKILL.md

---

## Technology Versions

| Technology | Version | Notes |
|------------|---------|-------|
| Gateway API | v1.2+ | Kubernetes standard |
| Envoy Gateway | v1.6+ | CNCF implementation |
| Traefik | v3.x | Gateway API support |
| KEDA | v2.18+ | Event-driven autoscaling |
| CertManager | v1.16+ | TLS automation |
| Envoy AI Gateway | v0.4+ | LLM traffic management |
| Docker Desktop K8s | Latest | Development platform |
