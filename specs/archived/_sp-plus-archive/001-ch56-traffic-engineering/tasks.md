# Tasks: Chapter 56 - Traffic Engineering

**Input**: Design documents from `/specs/001-ch56-traffic-engineering/`
**Prerequisites**: spec.md, plan.md
**Branch**: `001-ch56-traffic-engineering`

**Content Type**: Educational Chapter (13 lessons)
**Organization**: Tasks grouped by lesson following plan.md pedagogical arc

## Format: `[ID] [P?] [Lesson] Description`

- **[P]**: Can run in parallel (different lesson files, no dependencies)
- **[Lesson]**: Which lesson this task belongs to (L00, L01, L02...)
- All lesson output paths are absolute

## Path Conventions

**Content Output**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/`
**Expertise Skill**: `.claude/skills/building-with-envoy-gateway/SKILL.md`

---

## Phase 1: Setup (Chapter Infrastructure)

**Purpose**: Create chapter directory structure and verify prerequisites

- [X] T001 Create chapter directory at `apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/`
- [X] T002 Create chapter README.md with overview linking to all 13 lessons
- [X] T003 [P] Verify expertise skill exists at `.claude/skills/building-with-envoy-gateway/SKILL.md`
- [X] T004 [P] Verify Task API deployment manifests exist from Ch50

**Checkpoint**: Directory structure ready, prerequisites verified

---

## Phase 2: Foundational Lessons (L00-L02) - Layer 1 Manual Foundation

**Purpose**: Build vocabulary and skill foundation before AI collaboration

### L00: Build Your Traffic Engineering Skill (Priority: P1)

**Goal**: Students create their `traffic-engineer` skill BEFORE learning content

**Independent Test**: Student can invoke skill to generate valid Gateway + HTTPRoute YAML

- [X] T005 [L00] Lesson 00: Build Your Traffic Engineering Skill
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/00-build-your-traffic-engineering-skill.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Reference: spec.md L00 requirements, plan.md L00 section
    - Quality reference: `apps/learn-app/docs/01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-digital-fte-revolution.md`
  - **SKILLS**:
    - learning-objectives: Generate measurable outcomes for skill creation
    - exercise-designer: Design 3 exercises (clone skills-lab, write LEARNING-SPEC.md, create skill)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **CONTENT**:
    - Teaching modality: Skill-First Discovery
    - Concepts: LEARNING-SPEC.md structure, Context7 docs, skill structure, grounded knowledge
    - Include "Reflect on Your Skill" section
    - Duration: 25 min

### L01: Ingress Fundamentals (Priority: P1)

**Goal**: Build vocabulary for north-south traffic patterns

**Independent Test**: Student can explain why Ingress exists and articulate 3+ limitations

- [X] T006 [L01] Lesson 01: Ingress Fundamentals
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/01-ingress-fundamentals.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Reference: spec.md L01 requirements, plan.md L01 section
  - **SKILLS**:
    - learning-objectives: Bloom's Understand/Analyze for Service types, Ingress limitations
    - exercise-designer: Design 3 Socratic dialogue exercises
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Socratic Dialogue
    - Concepts: North-south traffic, Service types, Ingress resource, annotations, limitations
    - Include "Reflect on Your Skill" section
    - Duration: 30 min

### L02: Traefik Ingress Controller (Priority: P1)

**Goal**: Experience simpler Ingress solution before Gateway API complexity

**Independent Test**: Task API accessible via Traefik, rate limiting functional

- [X] T007 [L02] Lesson 02: Traefik Ingress Controller
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/02-traefik-ingress-controller.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Reference: spec.md L02 requirements, plan.md L02 section
  - **SKILLS**:
    - learning-objectives: Bloom's Apply/Analyze for Helm install, IngressRoute, Middleware
    - exercise-designer: Design 3 hands-on exercises (install, create route, add middleware)
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Hands-On Discovery
    - Concepts: Helm installation, IngressRoute CRD, Middleware, rate limiting, dashboard, comparison
    - Include "Reflect on Your Skill" section
    - Duration: 35 min

**Checkpoint**: Foundation phase complete - students have vocabulary and skill foundation

---

## Phase 3: Gateway API Core Lessons (L03-L06) - Layer 1→2 Transition

**Purpose**: Learn Gateway API standard with emerging AI collaboration

### L03: Gateway API - The New Standard (Priority: P1)

**Goal**: Understand Gateway API as Kubernetes standard replacing Ingress

**Independent Test**: Student explains role separation, has working Gateway routing

- [X] T008 [L03] Lesson 03: Gateway API - The New Standard
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/03-gateway-api-new-standard.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Understand/Apply for GatewayClass, Gateway, HTTPRoute
    - exercise-designer: Design 3 specification-first exercises
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Specification-First
    - Concepts: GatewayClass, Gateway, HTTPRoute, GRPCRoute, ReferenceGrant, role separation, implementations
    - Include "Reflect on Your Skill" section
    - Duration: 40 min

### L04: Envoy Gateway Setup (Priority: P1)

**Goal**: Install and configure Envoy Gateway

**Independent Test**: Envoy Gateway running, GatewayClass available

- [X] T009 [L04] Lesson 04: Envoy Gateway Setup
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/04-envoy-gateway-setup.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Apply for Helm install, architecture verification
    - exercise-designer: Design 3 guided installation exercises
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Guided Installation
    - Concepts: Helm chart, control plane, data plane, xDS protocol, EnvoyProxy CRD, Gateway API CRDs
    - Include "Reflect on Your Skill" section
    - Include "Try With AI" section (L2 starts here)
    - Duration: 35 min

### L05: Traffic Routing with HTTPRoute (Priority: P1)

**Goal**: Master HTTPRoute matching patterns for production routing

**Independent Test**: All routing patterns functional, student can write HTTPRoute from requirements

- [X] T010 [L05] Lesson 05: Traffic Routing with HTTPRoute
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/05-traffic-routing-httproute.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Apply/Analyze for path, header, query, method matching
    - exercise-designer: Design 3 hands-on creation exercises
    - ai-collaborate-teaching: Design Try With AI section for routing generation
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Hands-On Creation
    - Concepts: Path matching types, header matching, query matching, method matching, traffic weights, multiple rules, GRPCRoute
    - Include "Reflect on Your Skill" section
    - Include "Try With AI" section
    - Duration: 40 min

### L06: Rate Limiting & Circuit Breaking (Priority: P2)

**Goal**: Protect services from abuse and cost overruns

**Independent Test**: Rate limiting functional, per-user limits working, circuit breaker configured

- [X] T011 [L06] Lesson 06: Rate Limiting & Circuit Breaking
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/06-rate-limiting-circuit-breaking.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Apply/Analyze/Evaluate for rate limiting patterns
    - exercise-designer: Design 3 error analysis exercises (exceed limit, observe, fix)
    - ai-collaborate-teaching: Design Try With AI section for policy configuration
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Error Analysis
    - Concepts: BackendTrafficPolicy, local vs global rate limiting, descriptors, per-user limits, circuit breaker, health checks, policy merging
    - Include "Reflect on Your Skill" section
    - Include "Try With AI" section
    - Duration: 45 min

**Checkpoint**: Gateway API core complete - students can create and configure Gateway resources

---

## Phase 4: Production Features Lessons (L07-L09) - Layer 2 Collaboration

**Purpose**: TLS, deployment patterns, and autoscaling with AI collaboration

### L07: TLS Termination with CertManager (Priority: P2)

**Goal**: Secure traffic with TLS, automated certificate management

**Independent Test**: HTTPS listener functional, certificate auto-generated

- [X] T012 [L07] Lesson 07: TLS Termination with CertManager
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/07-tls-termination-certmanager.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Apply for CertManager install, ClusterIssuer, TLS config
    - exercise-designer: Design 3 iterative configuration exercises
    - ai-collaborate-teaching: Design Try With AI section for TLS troubleshooting
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Iterative Configuration
    - Concepts: CertManager Helm, ClusterIssuer, Let's Encrypt ACME, Certificate resource, Gateway TLS listener, TLS secrets
    - Include "Reflect on Your Skill" section
    - Include "Try With AI" section
    - Duration: 40 min

### L08: Traffic Splitting Patterns (Priority: P3)

**Goal**: Implement canary, blue-green, and A/B testing patterns

**Independent Test**: Traffic splitting functional, header routing working, rollback demonstrated

- [X] T013 [L08] Lesson 08: Traffic Splitting Patterns
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/08-traffic-splitting-patterns.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Apply/Evaluate for deployment patterns
    - exercise-designer: Design 3 collaborative debugging exercises
    - ai-collaborate-teaching: Design Try With AI section for canary configuration
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Collaborative Debugging
    - Concepts: Canary deployment, traffic weights, header-based routing, blue-green, rollback patterns
    - Include "Reflect on Your Skill" section
    - Include "Try With AI" section
    - Duration: 35 min

### L09: Autoscaling with HPA, VPA & KEDA (Priority: P2)

**Goal**: Intelligent capacity management based on demand

**Independent Test**: HPA scales on CPU, KEDA scales on custom metrics, scale-to-zero observed

- [X] T014 [L09] Lesson 09: Autoscaling with HPA, VPA & KEDA
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/09-autoscaling-hpa-vpa-keda.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Apply/Analyze for HPA, VPA, KEDA patterns
    - exercise-designer: Design 3 hands-on discovery exercises (HPA, KEDA Prometheus, KEDA Kafka)
    - ai-collaborate-teaching: Design Try With AI section for ScaledObject configuration
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Hands-On Discovery
    - Concepts: HPA, metrics-server, VPA, KEDA architecture, ScaledObject, Prometheus scaler, Kafka scaler, scale-to-zero
    - Include "Reflect on Your Skill" section
    - Include "Try With AI" section
    - Duration: 45 min

**Checkpoint**: Production features complete - students can secure and scale their gateway

---

## Phase 5: Intelligence Lessons (L10-L11) - Layer 2→3 Transition

**Purpose**: Pattern recognition and AI-specific traffic management

### L10: Resilience Patterns (Priority: P2)

**Goal**: Production-grade resilience with retries, timeouts, PDB, probes

**Independent Test**: Retries working, PDB protecting, graceful shutdown verified

- [X] T015 [L10] Lesson 10: Resilience Patterns
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/10-resilience-patterns.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Apply/Analyze/Evaluate for resilience patterns
    - exercise-designer: Design 3 pattern recognition exercises
    - ai-collaborate-teaching: Design Try With AI section for resilience configuration
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Pattern Recognition
    - Concepts: Retry policy, backoff, timeout config, PDB, liveness/readiness probes, graceful shutdown, outlier detection
    - Include "Reflect on Your Skill" section
    - Include "Try With AI" section
    - Duration: 40 min

### L11: Envoy AI Gateway for LLM Traffic (Priority: P3)

**Goal**: AI-specific traffic management for cost control and reliability

**Independent Test**: Token limiting configured, provider fallback working, cost implications understood

- [X] T016 [L11] Lesson 11: Envoy AI Gateway for LLM Traffic
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/11-envoy-ai-gateway-llm-traffic.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Apply/Evaluate/Create for LLM traffic patterns
    - exercise-designer: Design 3 AI collaboration exercises (Three Roles INVISIBLE)
    - ai-collaborate-teaching: Design Try With AI with 5-part structure (Initial Request, Critical Evaluation, Constraint Teaching, Refinement, Final Check)
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: AI Collaboration (Three Roles INVISIBLE in student content)
    - Concepts: AI Gateway architecture, token-based rate limiting, token budget, provider fallback, model routing, cost engineering
    - Include "Reflect on Your Skill" section
    - Include "Try With AI" section (5-part structure per plan.md)
    - Duration: 45 min

**Checkpoint**: Intelligence phase complete - students recognize patterns worth encoding

---

## Phase 6: Capstone (L12) - Layer 4 Orchestration

**Purpose**: Spec-driven integration for production Task API traffic management

### L12: Capstone - Production Traffic for Task API (Priority: P1)

**Goal**: Integrate all patterns for production-ready Task API traffic management

**Independent Test**: External access via Gateway works, rate limiting rejects excess, HTTPS functional, KEDA scales under load, student owns tested traffic-engineer skill

- [X] T017 [L12] Lesson 12: Capstone - Production Traffic for Task API
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/56-traffic-engineering/12-capstone-production-traffic-task-api.md`
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - learning-objectives: Bloom's Create/Evaluate for spec-driven integration
    - exercise-designer: Design 5-phase capstone project (Specification, Skill Composition, Implementation, Validation, Skill Finalization)
    - assessment-builder: Design chapter completion assessment
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT**:
    - Teaching modality: Spec-Driven Project
    - Concepts: Specification writing, end-to-end workflow, composition of accumulated intelligence, production validation
    - 5 Phases per plan.md: Specification Writing, Skill Composition, Implementation, Validation, Skill Finalization
    - Include "Reflect on Your Skill" section (final skill submission)
    - Duration: 60 min

**Checkpoint**: Capstone complete - students have production-ready traffic configuration and finalized skill

---

## Phase 7: Validation & Polish

**Purpose**: Chapter-wide validation and cross-cutting improvements

- [X] T018 Run educational-validator on all 13 lessons
  - Check: Layer labels not in student content
  - Check: No meta-commentary ("What to notice", "AI as Teacher")
  - Check: All lessons have "Reflect on Your Skill" section
  - Check: L04+ have "Try With AI" section
  - Check: Cognitive load within B1 limits

- [X] T019 Run factual-verifier on technical claims
  - Verify: Technology versions (Gateway API v1.2+, Envoy Gateway v1.6+, KEDA v2.18+)
  - Verify: Helm commands work on Docker Desktop K8s
  - Verify: CRD examples are syntactically valid

- [X] T020 [P] Update chapter README.md with final lesson links and descriptions

- [X] T021 [P] Create chapter _category_.json for Docusaurus sidebar
  ```json
  {
    "label": "Traffic Engineering",
    "position": 56,
    "link": {
      "type": "generated-index"
    }
  }
  ```

- [X] T022 Run content-evaluation-framework on all lessons (validated via educational-validator)
  - Technical Accuracy: 30%
  - Pedagogical Effectiveness: 25%
  - Writing Quality: 20%
  - Structure & Organization: 15%
  - AI-First Teaching: 10%
  - Constitution Compliance: Pass/Fail

**Checkpoint**: All validation complete, chapter ready for review

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational Lessons (Phase 2)**: Depends on Setup - BLOCKS subsequent phases
- **Gateway API Core (Phase 3)**: Depends on Phase 2 completion
- **Production Features (Phase 4)**: Depends on L06 completion
- **Intelligence Lessons (Phase 5)**: Depends on L09 completion
- **Capstone (Phase 6)**: Depends on L00-L11 completion
- **Validation (Phase 7)**: Depends on all lessons complete

### Lesson Dependencies (Sequential within phases)

**Phase 2**: L00 → L01 → L02 (sequential, manual foundation)
**Phase 3**: L03 → L04 → L05 → L06 (sequential, Gateway API learning curve)
**Phase 4**: L07, L08, L09 can run in parallel after L06
**Phase 5**: L10 → L11 (L11 depends on L10 resilience context)
**Phase 6**: L12 requires all L00-L11 complete

### Parallel Opportunities

**Within Phase 4 (after L06 complete)**:
```
Task: "L07 TLS Termination with CertManager" [P]
Task: "L08 Traffic Splitting Patterns" [P]
Task: "L09 Autoscaling with HPA, VPA & KEDA" [P]
```

**Within Phase 7 (after all lessons)**:
```
Task: "T019 Run factual-verifier" [P]
Task: "T020 Update README" [P]
Task: "T021 Create _category_.json" [P]
```

---

## Parallel Example: Phase 4 Lessons

```bash
# After L06 completes, launch L07, L08, L09 in parallel:
Task: content-implementer for L07 TLS Termination
Task: content-implementer for L08 Traffic Splitting
Task: content-implementer for L09 Autoscaling
```

---

## Implementation Strategy

### MVP First (Lessons 00-06 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational Lessons L00-L02 (T005-T007)
3. Complete Phase 3: Gateway API Core L03-L06 (T008-T011)
4. **STOP and VALIDATE**: Test lessons work, code examples execute
5. Students can complete Gateway API fundamentals

### Full Chapter Delivery

1. Setup + Foundational + Gateway API Core → Core complete
2. Add Production Features L07-L09 → Students can secure and scale
3. Add Intelligence L10-L11 → Students recognize patterns
4. Add Capstone L12 → Students integrate all patterns
5. Validation Phase → Chapter ready for review

### Skill-First Validation

After each phase:
1. Verify student's traffic-engineer skill improves
2. Test skill generates valid YAML for concepts learned
3. "Reflect on Your Skill" sections match lesson content

---

## Summary

**Total Tasks**: 22
**Lesson Tasks**: 13 (T005-T017)
**Setup Tasks**: 4 (T001-T004)
**Validation Tasks**: 5 (T018-T022)

**Task Count per User Story/Priority**:
- P1 (US1, US2): L00, L01, L02, L03, L04, L05, L12 = 7 lessons
- P2 (US3, US4, US5): L06, L07, L09, L10 = 4 lessons
- P3 (US6, US7): L08, L11 = 2 lessons

**Estimated Implementation Time**: 38-48 hours (from plan.md)

**MVP Scope**: Phase 1-3 (Setup + Foundational + Gateway API Core) = Tasks T001-T011
