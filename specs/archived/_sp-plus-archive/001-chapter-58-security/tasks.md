# Tasks: Chapter 58 - Production Security & Compliance

**Input**: Design documents from `/specs/001-chapter-58-security/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)
**Expertise Skill**: `.claude/skills/building-with-cloud-security/SKILL.md`
**Content Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/`
**GitHub Issues**: #563-#582 (panaversity/agentfactory)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1-US10)
- All lesson tasks use `content-implementer` subagent with `educational-validator`

## User Story to Lesson Mapping

| User Story | Priority | Lesson | Title |
|------------|----------|--------|-------|
| US1 | P1 | L00 | Build Your Cloud Security Skill |
| US2 | P1 | L01 | Cloud Native Security Model (4C's) |
| US3 | P1 | L02 | RBAC Deep Dive |
| US4 | P1 | L03 | NetworkPolicies |
| US5 | P2 | L05 | Pod Security Standards |
| US6 | P2 | L04 | Secrets Management |
| US7 | P2 | L06 | Image Scanning & Supply Chain |
| US8 | P2 | L07 | Dapr Security |
| US9 | P3 | L08 | Compliance Fundamentals |
| US10 | P1 | L09 | Capstone - Secure Task API |

---

## Phase 1: Setup (Chapter Structure)

**Purpose**: Create chapter directory and README

- [x] T58.R [P] Create chapter directory and README ([#563](https://github.com/panaversity/agentfactory/issues/563))
  - **Output path**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/README.md`
  - **Content**: Chapter overview matching Ch49/Ch50 structure
  - **Include**: Learning outcomes, lesson list, prerequisites, running example (Task API)
  - **Reference**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-containerization/README.md`

**Checkpoint**: Chapter directory exists with README overview

---

## Phase 2: P1 User Stories (Core Security Foundation)

**Purpose**: Complete all P1 priority lessons - the foundational security knowledge

### T58.L00 [US1] Build Your Cloud Security Skill (15 min) - Layer 3

**Goal**: Students create working `cloud-security` skill grounded in official docs
**Independent Test**: Skill exists in `.claude/skills/` and generates RBAC/NetworkPolicy/PSS configs

- [x] T58.L00 [US1] Create lesson: Build Your Cloud Security Skill ([#564](https://github.com/panaversity/agentfactory/issues/564))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/00-build-your-cloud-security-skill.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/06-AI-Native-Software-Development/40-agent-native-fastapi/00-build-your-fastapi-agent-api-skill.md`
  - **SKILLS**:
    - `learning-objectives` (generate measurable outcomes for skill creation)
    - `exercise-designer` (skill testing exercises)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - Clone skills-lab fresh
    - Write LEARNING-SPEC.md
    - Use `/fetching-library-docs kubernetes security`
    - Use `/skill-creator` to build skill
    - 2 "Try With AI" prompts
  - **Acceptance**: SC-001 - Skill creation in under 15 min

---

### T58.L01 [US2] Cloud Native Security Model (25 min) - Layer 1

**Goal**: Students understand 4C model and classify security controls by layer
**Independent Test**: Student explains why Code-level security alone cannot compensate for Cluster vulnerabilities

- [x] T58.L01 [US2] Create lesson: Cloud Native Security Model ([#565](https://github.com/panaversity/agentfactory/issues/565))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/01-cloud-native-security-model.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-digital-fte-revolution.md`
  - **SKILLS**:
    - `learning-objectives` (4C model understanding, control classification)
    - `exercise-designer` (classify 10 controls exercise)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - 4C concentric circles diagram
    - Task API examples at each layer
    - Key principle: outer layers must be secure
    - Interactive exercise: Classify 10 controls
    - "Reflect on Your Skill" section
  - **Acceptance**: SC-002 - Classify 5+ controls by layer with 90% accuracy

---

### T58.L02 [US3] RBAC Deep Dive (30 min) - Layer 1

**Goal**: Implement RBAC for Task API with least privilege principle
**Independent Test**: Task API runs with dedicated ServiceAccount, ConfigMap read only

- [x] T58.L02 [US3] Create lesson: RBAC Deep Dive ([#566](https://github.com/panaversity/agentfactory/issues/566))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/02-rbac-deep-dive.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/07-AI-Cloud-Native-Development/50-kubernetes-fundamentals/03-pods-and-containers.md`
  - **SKILLS**:
    - `learning-objectives` (RBAC implementation, least privilege)
    - `exercise-designer` (RBAC testing exercises with kubectl auth can-i)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - ServiceAccount creation with `automountServiceAccountToken: false`
    - Minimal Role (ConfigMap read only)
    - RoleBinding
    - Testing with `kubectl auth can-i`
    - RBAC decision matrix from expertise skill
    - "Reflect on Your Skill" section
  - **Acceptance**: SC-003 - Dedicated ServiceAccount with minimal permissions

---

### T58.L03 [US4] NetworkPolicies (30 min) - Layer 1

**Goal**: Implement default-deny NetworkPolicies with explicit allows
**Independent Test**: Unauthorized traffic blocked, verifiable with test pod

- [x] T58.L03 [US4] Create lesson: NetworkPolicies ([#567](https://github.com/panaversity/agentfactory/issues/567))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/03-network-policies.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/07-AI-Cloud-Native-Development/50-kubernetes-fundamentals/06-namespaces.md`
  - **SKILLS**:
    - `learning-objectives` (NetworkPolicy implementation, default deny)
    - `exercise-designer` (traffic verification exercises)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - Calico CNI installation on Docker Desktop
    - Default deny (ALWAYS FIRST)
    - DNS allow rule (CRITICAL edge case)
    - Allow ingress from Envoy Gateway
    - Verification with test pod
    - Edge case: What happens without DNS allow?
    - "Reflect on Your Skill" section
  - **Acceptance**: SC-004 - Unauthorized traffic blocked

**Checkpoint**: Core cluster security complete (RBAC + NetworkPolicy)

---

## Phase 3: P2 User Stories (Container & Runtime Security)

**Purpose**: Complete P2 priority lessons - container hardening and runtime controls

### T58.L04 [US6] Secrets Management (25 min) - Layer 1

**Goal**: Create and consume K8s Secrets securely via volume mounts
**Independent Test**: Task API credentials stored as Secret, consumed via volume mount

- [x] T58.L04 [US6] Create lesson: Secrets Management ([#568](https://github.com/panaversity/agentfactory/issues/568))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/04-secrets-management.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/07-AI-Cloud-Native-Development/50-kubernetes-fundamentals/07-configmaps-and-secrets.md`
  - **SKILLS**:
    - `learning-objectives` (secrets creation, consumption patterns)
    - `exercise-designer` (secrets mounting exercises)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - K8s Secret creation
    - Volume mount consumption (NOT env vars)
    - Why volume mount over environment variables table
    - Secrets hierarchy diagram (K8s → Sealed → ESO)
    - ESO overview (show, don't require)
    - "Reflect on Your Skill" section
  - **Acceptance**: Secrets via volume mount pattern

---

### T58.L05 [US5] Pod Security Standards (25 min) - Layer 1

**Goal**: Apply PSS labels and write compliant pod specs for Restricted profile
**Independent Test**: Task API passes PSS restricted validation

- [x] T58.L05 [US5] Create lesson: Pod Security Standards ([#569](https://github.com/panaversity/agentfactory/issues/569))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/05-pod-security-standards.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/07-AI-Cloud-Native-Development/50-kubernetes-fundamentals/08-deployments.md`
  - **SKILLS**:
    - `learning-objectives` (PSS levels, namespace labels, compliant specs)
    - `exercise-designer` (PSS compliance exercises)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - PSS levels table (Privileged, Baseline, Restricted)
    - Namespace labeling commands
    - PSS-compliant pod spec with securityContext
    - Common violations and fixes table
    - Verification: test privileged pod rejection
    - "Reflect on Your Skill" section
  - **Acceptance**: SC-005 - Task API passes PSS restricted

---

### T58.L06 [US7] Image Scanning & Supply Chain (25 min) - Layer 1

**Goal**: Scan images with Trivy, fail CI/CD on HIGH+ vulnerabilities
**Independent Test**: Task API image has no CRITICAL vulnerabilities

- [x] T58.L06 [US7] Create lesson: Image Scanning & Supply Chain ([#570](https://github.com/panaversity/agentfactory/issues/570))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/06-image-scanning-supply-chain.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-containerization/07-security-best-practices.md`
  - **SKILLS**:
    - `learning-objectives` (Trivy scanning, severity levels, CI/CD integration)
    - `exercise-designer` (image scanning workflow exercises)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - Trivy installation (brew/curl)
    - Scan commands with severity levels
    - Severity levels action table
    - CI/CD integration (GitHub Actions example)
    - SBOM generation
    - Cosign overview (show, don't require)
    - Image digest pinning
    - "Reflect on Your Skill" section
  - **Acceptance**: SC-006 - No CRITICAL vulnerabilities

---

### T58.L07 [US8] Dapr Security (25 min) - Layer 2 (AI Collaboration)

**Goal**: Configure Dapr mTLS, API tokens, and component scopes using Three Roles
**Independent Test**: Only Task API can access its designated state store

- [x] T58.L07 [US8] Create lesson: Dapr Security ([#571](https://github.com/panaversity/agentfactory/issues/571))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/07-dapr-security.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-fundamentals/05-service-invocation.md`
  - **SKILLS**:
    - `learning-objectives` (mTLS verification, component scopes)
    - `exercise-designer` (Dapr security configuration exercises)
    - `ai-collaborate-teaching` (THREE ROLES REQUIRED for Layer 2)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - **THREE ROLES DEMONSTRATIONS** (REQUIRED):
      - AI as Teacher: mTLS verification commands (new knowledge)
      - AI as Student: Dev vs prod requirements (student corrects)
      - AI as Co-Worker: Component scopes iteration (convergence)
    - mTLS status verification commands
    - Component scopes YAML
    - API token authentication (optional)
    - Verification: scope enforcement test
    - "Reflect on Your Skill" section
  - **Acceptance**: Component scopes isolate Task API resources

**Checkpoint**: Container and runtime security complete

---

## Phase 4: P3 User Stories + Capstone (Governance & Integration)

**Purpose**: Complete compliance awareness and capstone integration

### T58.L08 [US9] Compliance Fundamentals (20 min) - Layer 1

**Goal**: Identify K8s controls that support SOC2/HIPAA requirements
**Independent Test**: Student lists 3 K8s controls for SOC2 access control

- [x] T58.L08 [US9] Create lesson: Compliance Fundamentals ([#578](https://github.com/panaversity/agentfactory/issues/578))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/08-compliance-fundamentals.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability/03-metrics-collection.md`
  - **SKILLS**:
    - `learning-objectives` (compliance mapping, evidence collection)
    - `exercise-designer` (compliance control identification exercises)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - Important disclaimer: awareness, not certification
    - SOC2 relevant K8s controls table
    - HIPAA relevant K8s controls table
    - Audit policy example
    - Evidence collection checklist
    - Three controls for SOC2 access control (eval answer)
    - "Reflect on Your Skill" section
  - **Acceptance**: SC-008 - Articulate 3 K8s controls for SOC2

---

### T58.L09 [US10] Capstone - Secure Task API (40 min) - Layer 4

**Goal**: Apply ALL security patterns, complete 10-point audit checklist
**Independent Test**: Task API passes all 10 security checklist items

- [x] T58.L09 [US10] Create lesson: Capstone - Secure Task API ([#579](https://github.com/panaversity/agentfactory/issues/579))
  - **SUBAGENT**: `content-implementer`
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/09-capstone-secure-task-api.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/07-AI-Cloud-Native-Development/50-kubernetes-fundamentals/10-capstone-project.md`
  - **SKILLS**:
    - `learning-objectives` (spec-driven integration, security audit)
    - `exercise-designer` (penetration test scenarios)
    - `assessment-builder` (10-point security checklist as summative assessment)
  - **VALIDATION**: `educational-validator` reads file from disk (MUST PASS before marking complete)
  - **Key content from plan**:
    - Security specification (FIRST - spec-driven pattern)
    - Compose all security components (L01-L08)
    - **10-point security audit checklist** with kubectl commands
    - Penetration test scenarios (3 scenarios)
    - Security posture documentation template
  - **Acceptance**: SC-007 - Complete 10-point audit with all items passing

**Checkpoint**: All lessons complete, capstone integrates all patterns

---

## Phase 5: Validation & Assets

**Purpose**: Create supporting assets and validate all content

- [x] T58.C Create 10-point security checklist asset ([#580](https://github.com/panaversity/agentfactory/issues/580))
  - **Output path**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/assets/security-checklist.md`
  - **Content**: Standalone 10-point checklist from L09 plan
  - **Format**: Markdown table with Check, Command, Expected columns
  - **Use case**: Students can copy/reference for their own projects

- [x] T58.V Validate all lessons with educational-validator ([#581](https://github.com/panaversity/agentfactory/issues/581))
  - **Scope**: All 10 lessons (L00-L09) + README
  - **Validation**: Run `educational-validator` on each file
  - **Criteria**:
    - Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
    - Compelling narrative opening (2-3 paragraphs)
    - "Try With AI" sections with 3+ prompts (except L07 which uses Three Roles)
    - "Reflect on Your Skill" section in L01-L08
    - Layer progression validated
    - Constitution compliance
  - **Action**: Fix any issues before marking complete

- [x] T58.A Run assessment-architect for chapter quiz ([#582](https://github.com/panaversity/agentfactory/issues/582))
  - **SKILLS**: `assessment-architect`
  - **Scope**: Design end-of-chapter assessment
  - **Bloom's levels**: Apply/Analyze (B1 proficiency)
  - **Coverage**: All 8 success criteria (SC-001 through SC-008)
  - **Output**: Assessment design document or quiz questions

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup)
    └── T58.R README
         │
         ▼
Phase 2 (P1 User Stories) - Execute in order
    ├── T58.L00 [US1] → Creates skill foundation
    ├── T58.L01 [US2] → 4C mental model (needs L00 for reflection)
    ├── T58.L02 [US3] → RBAC (needs L01 context)
    └── T58.L03 [US4] → NetworkPolicy (needs L01 context)
         │
         ▼
Phase 3 (P2 User Stories) - Can parallelize after Phase 2
    ├── T58.L04 [US6] → Secrets (needs L02 RBAC context)
    ├── T58.L05 [US5] → PSS (needs L02, L04 context)
    ├── T58.L06 [US7] → Image Scanning (needs L05 container context)
    └── T58.L07 [US8] → Dapr Security (needs L02-L06 foundation)
         │
         ▼
Phase 4 (P3 + Capstone)
    ├── T58.L08 [US9] → Compliance (needs L02-L07 for mapping)
    └── T58.L09 [US10] → Capstone (needs ALL previous)
         │
         ▼
Phase 5 (Validation)
    ├── T58.C → Security checklist asset
    ├── T58.V → Validate all lessons
    └── T58.A → Chapter assessment
```

### Internal Lesson Dependencies

| Lesson | Depends On | Reason |
|--------|------------|--------|
| L00 | None | Starting point |
| L01 | L00 | Skill reflection needs skill |
| L02 | L01 | RBAC is cluster layer from 4C |
| L03 | L01 | NetworkPolicy is cluster layer from 4C |
| L04 | L02 | RBAC protects secrets |
| L05 | L02, L04 | ServiceAccount and Secrets context |
| L06 | L05 | Container layer context |
| L07 | L02-L06 | All cluster security foundation |
| L08 | L02-L07 | All controls for compliance mapping |
| L09 | ALL | Capstone integrates everything |

### Parallel Opportunities

Within each phase, tasks marked [P] can run in parallel. After Phase 2 completion:

```bash
# Phase 3 can be parallelized:
T58.L04, T58.L05, T58.L06, T58.L07 can start together (different files)

# Phase 5 validation can be parallelized:
T58.C, T58.A can run in parallel after T58.V completes
```

---

## Implementation Strategy

### MVP First (P1 Stories Only)

1. Complete Phase 1: Setup (README)
2. Complete Phase 2: P1 Stories (L00, L01, L02, L03)
3. **STOP and VALIDATE**: Core security foundation complete
4. Students can secure Task API with RBAC + NetworkPolicy

### Full Chapter Delivery

1. Complete Phases 1-2 → Core security
2. Complete Phase 3 → Container and runtime security
3. Complete Phase 4 → Compliance + Capstone
4. Complete Phase 5 → Validation + Assets
5. Run `educational-validator` on all content

### Estimated Total Duration

| Phase | Tasks | Est. Duration |
|-------|-------|---------------|
| Phase 1 | 1 task | 30 min |
| Phase 2 | 4 lessons | 3-4 hours |
| Phase 3 | 4 lessons | 3-4 hours |
| Phase 4 | 2 lessons | 2-3 hours |
| Phase 5 | 3 tasks | 1-2 hours |
| **Total** | **14 tasks** | **10-14 hours** |

---

## Success Criteria Mapping

| Success Criterion | Task | Lesson |
|-------------------|------|--------|
| SC-001 | T58.L00 | Skill creation in 15 min |
| SC-002 | T58.L01 | Classify 5+ controls by layer |
| SC-003 | T58.L02 | Dedicated ServiceAccount |
| SC-004 | T58.L03 | Unauthorized traffic blocked |
| SC-005 | T58.L05 | PSS restricted compliance |
| SC-006 | T58.L06 | No CRITICAL vulnerabilities |
| SC-007 | T58.L09 | 10-point audit checklist |
| SC-008 | T58.L08 | 3 K8s controls for SOC2 |

---

## Notes

- All lessons use `content-implementer` subagent with direct file writes
- All lessons require `educational-validator` before marking complete
- L07 uses `ai-collaborate-teaching` skill for Three Roles (Layer 2)
- L09 uses `assessment-builder` for 10-point checklist design
- Expertise skill `.claude/skills/building-with-cloud-security/SKILL.md` provides accurate patterns
- Quality reference lessons provided for each task
- Absolute paths used for all output files
