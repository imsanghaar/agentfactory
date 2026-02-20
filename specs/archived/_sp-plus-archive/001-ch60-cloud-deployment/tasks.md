# Tasks: Chapter 60 - Real Cloud Deployment

**Input**: Design documents from `/specs/001-ch60-cloud-deployment/`
**Prerequisites**: plan.md (required), spec.md (required)
**Branch**: `001-ch60-cloud-deployment`

**Content Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/`

**Organization**: Tasks organized by User Story (from spec.md) mapped to lessons (from plan.md)

---

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1-US6)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Chapter Infrastructure)

**Purpose**: Create chapter directory and foundational files

- [ ] T001 Create chapter directory at `apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/`
- [ ] T002 [P] Create `_category_.json` with chapter metadata (label: "60. Real Cloud Deployment", position: 60)
- [ ] T003 [P] Create chapter README.md with overview linking to L00-L10

**Checkpoint**: Chapter structure ready for lesson implementation

---

## Phase 2: User Story 1 - Build Cloud Deployment Skill (Priority: P1)

**Goal**: Student creates `multi-cloud-deployer` skill using Skill-First Learning Pattern

**Independent Test**: Student runs Claude Code, creates skill, and can generate deployment plans

**Lessons**: L00

### Implementation

- [ ] T004 [US1] **Lesson L00: Build Your Cloud Deployment Skill**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/00-build-your-cloud-deployment-skill.md`
  - **SUBAGENT**: content-implementer
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Include YAML frontmatter with sidebar_position: 0, chapter: 60, lesson: 0
    - Teaching stage: L3 (Intelligence Design - Skill-First)
    - Duration: 15 minutes
  - **SKILLS**: learning-objectives (measurable outcomes for skill creation)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS)
  - **QUALITY REFERENCE**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/50-kubernetes-for-ai-services/00-build-your-kubernetes-skill.md`
  - **CONTENT REQUIREMENTS**:
    - Clone skills-lab instructions
    - Use `/fetching-library-docs` for DigitalOcean and Hetzner docs
    - Use `/skill-creator` to build multi-cloud-deployer skill
    - Verify skill at `.claude/skills/multi-cloud-deployer/`
    - Maps to eval: SC-007

**Checkpoint**: L00 complete - Skill-First pattern established

---

## Phase 3: User Story 2 - Deploy to Managed Kubernetes (DOKS) (Priority: P1)

**Goal**: Student deploys Task API to DigitalOcean DOKS with full production stack

**Independent Test**: Student accesses https://tasks.yourdomain.com/health successfully

**Lessons**: L01, L02, L03, L04, L05, L06

### Implementation

- [ ] T005 [US2] **Lesson L01: Beyond Docker Desktop**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/01-beyond-docker-desktop.md`
  - **SUBAGENT**: content-implementer
    - Writes file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Teaching stage: L1 (Manual Foundation)
    - Duration: 25 minutes
    - 5 concepts: Docker Desktop limits, managed K8s benefits, self-managed K8s, cost triangle, provider selection
  - **SKILLS**: learning-objectives
  - **VALIDATION**: educational-validator (MUST PASS)
  - **QUALITY REFERENCE**: Match Ch50 L01 quality
  - **CONTENT REQUIREMENTS**:
    - Cost comparison table from expertise skill (Dec 2025 pricing)
    - Managed vs self-managed decision matrix
    - "Reflect on Your Skill" section at end
    - Maps to evals: SC-004, SC-007

- [ ] T006 [US2] **Lesson L02: DigitalOcean Account & doctl Setup**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/02-digitalocean-account-setup.md`
  - **SUBAGENT**: content-implementer
    - Teaching stage: L1 (Manual Foundation)
    - Duration: 20 minutes
    - 4 concepts: account creation, API token, doctl CLI, authentication
  - **SKILLS**: learning-objectives
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT REQUIREMENTS**:
    - Account creation with $200 free credit mention
    - `doctl auth init` with expected output blocks
    - `doctl account get` verification
    - "Reflect on Your Skill" section
    - Maps to evals: SC-001, SC-007

- [ ] T007 [US2] **Lesson L03: Provisioning DOKS Cluster**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/03-provisioning-doks-cluster.md`
  - **SUBAGENT**: content-implementer
    - Teaching stage: L1 (Manual Foundation)
    - Duration: 30 minutes
    - 6 concepts: cluster create, node size, node count, region, version, kubeconfig
  - **SKILLS**: learning-objectives
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT REQUIREMENTS**:
    - Full `doctl kubernetes cluster create` command with all options
    - Expected output block (SC-008 compliance)
    - `doctl kubernetes cluster kubeconfig save`
    - `kubectl get nodes` verification
    - "Reflect on Your Skill" section
    - Maps to evals: SC-001, SC-003, SC-007

- [ ] T008 [US2] **Lesson L04: Cloud Load Balancer & DNS**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/04-cloud-load-balancer-dns.md`
  - **SUBAGENT**: content-implementer
    - Teaching stage: L1 (Manual Foundation)
    - Duration: 25 minutes
    - 5 concepts: LoadBalancer behavior, external IP, LB cost, DNS A-record, DNS TTL
  - **SKILLS**: learning-objectives
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT REQUIREMENTS**:
    - LoadBalancer vs NodePort comparison
    - `kubectl get svc -w` to watch EXTERNAL-IP
    - DNS configuration (or nip.io/sslip.io for testing)
    - Cost awareness ($12/mo per LB)
    - "Reflect on Your Skill" section
    - Maps to evals: SC-003, SC-006

- [ ] T009 [US2] **Lesson L05: Deploying Task API to DOKS**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/05-deploying-task-api-to-doks.md`
  - **SUBAGENT**: content-implementer
    - Teaching stage: L2 (AI Collaboration)
    - Duration: 35 minutes
    - 6 concepts: deployment sequence, Dapr init, Traefik, cert-manager, Helm values, verification
  - **SKILLS**: learning-objectives, ai-collaborate-teaching (Three Roles invisible)
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT REQUIREMENTS**:
    - Three Roles demonstrated INVISIBLY (no meta-commentary)
    - Complete "Try With AI" section (5 parts)
    - Full deployment script from expertise skill
    - `curl https://tasks.yourdomain.com/health` verification
    - "Reflect on Your Skill" section
    - Maps to evals: SC-002, SC-003, SC-008

- [ ] T010 [US2] **Lesson L06: Production Secrets & Configuration**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/06-production-secrets-configuration.md`
  - **SUBAGENT**: content-implementer
    - Teaching stage: L2 (AI Collaboration)
    - Duration: 25 minutes
    - 5 concepts: K8s Secrets, ConfigMaps, image pull secrets, rotation, config hierarchy
  - **SKILLS**: learning-objectives, ai-collaborate-teaching
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT REQUIREMENTS**:
    - Three Roles demonstrated invisibly
    - GHCR image pull secret creation
    - Secret mounting verification
    - "Reflect on Your Skill" section
    - Maps to evals: SC-002, SC-008

**Checkpoint**: US2 complete - DOKS deployment path fully documented

---

## Phase 4: User Story 3 - Budget Cloud Lab (Hetzner + K3s) (Priority: P2)

**Goal**: Student sets up persistent ~$5/month Kubernetes lab

**Independent Test**: kubectl get nodes works against Hetzner cluster

**Lessons**: L07

### Implementation

- [ ] T011 [US3] **Lesson L07: Personal Cloud Lab - Hetzner + K3s**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/07-personal-cloud-lab-hetzner.md`
  - **SUBAGENT**: content-implementer
    - Teaching stage: L1 (Manual Foundation)
    - Duration: 30 minutes
    - 6 concepts: Hetzner account, API token, hetzner-k3s CLI, K3s, cluster.yaml, CCM
  - **SKILLS**: learning-objectives
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT REQUIREMENTS**:
    - hetzner-k3s installation
    - cluster.yaml configuration from expertise skill
    - `hetzner-k3s create --config cluster.yaml` with expected output (SC-008)
    - `kubectl get nodes` verification
    - Comparison with DOKS (same Helm commands work)
    - "Reflect on Your Skill" section
    - Maps to evals: SC-005, SC-006, SC-007

**Checkpoint**: US3 complete - Budget alternative path documented

---

## Phase 5: User Story 4 - Multi-Cloud Portability (Priority: P2)

**Goal**: Student understands kubectl/Helm/Dapr are universal across providers

**Independent Test**: Student explains provision → connect → deploy pattern

**Lessons**: L09

### Implementation

- [ ] T012 [US4] **Lesson L09: Same Patterns, Different Clouds**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/09-same-patterns-different-clouds.md`
  - **SUBAGENT**: content-implementer
    - Teaching stage: L2 (AI Collaboration)
    - Duration: 20 minutes
    - 4 concepts: universal commands, provision-connect-deploy, quick-starts, portability
  - **SKILLS**: learning-objectives, ai-collaborate-teaching
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT REQUIREMENTS**:
    - Multi-cloud comparison table (DOKS vs AKS vs GKE vs EKS vs Civo)
    - "90% identical" insight reinforced
    - Quick-start provisioning commands for each provider
    - "Reflect on Your Skill" section
    - Maps to evals: SC-004, SC-007

**Checkpoint**: US4 complete - Multi-cloud portability insight delivered

---

## Phase 6: User Story 5 - Production Checklist (Priority: P2)

**Goal**: Student validates deployment against production criteria

**Independent Test**: Student completes 10-item checklist with all passes

**Lessons**: L08

### Implementation

- [ ] T013 [US5] **Lesson L08: Production Checklist & Verification**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/08-production-checklist-verification.md`
  - **SUBAGENT**: content-implementer
    - Teaching stage: L2 (AI Collaboration)
    - Duration: 25 minutes
    - 6 concepts: health check, resource audit, monitoring, replicas, network policy, checklist pattern
  - **SKILLS**: learning-objectives, ai-collaborate-teaching
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT REQUIREMENTS**:
    - 10-item production readiness checklist table
    - kubectl commands for each verification
    - Expected output for passing checks
    - Three Roles invisible
    - "Reflect on Your Skill" section
    - Maps to evals: SC-002, SC-003, SC-008

**Checkpoint**: US5 complete - Production validation documented

---

## Phase 7: User Story 6 - Cost Management & Teardown (Priority: P3)

**Goal**: Student understands costs and can tear down clusters

**Independent Test**: Student deletes all resources and verifies $0 ongoing cost

**Lessons**: Integrated into L08, L10

### Implementation

(Cost management integrated into L08 production checklist - item 10)
(Teardown integrated into L10 capstone)

**Checkpoint**: US6 complete - Cost discipline embedded throughout

---

## Phase 8: Capstone (All User Stories Combined)

**Goal**: End-to-end spec-driven production deployment

**Independent Test**: Working HTTPS endpoint, skill generates commands for 3+ providers

**Lessons**: L10

### Implementation

- [ ] T014 [US1-6] **Lesson L10: Capstone - Full Production Deployment**
  - **OUTPUT PATH**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag-factory/apps/learn-app/docs/07-AI-Cloud-Native-Development/60-real-cloud-deployment/10-capstone-full-production.md`
  - **SUBAGENT**: content-implementer
    - Teaching stage: L4 (Spec-Driven Integration)
    - Duration: 45 minutes
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, assessment-builder
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTENT REQUIREMENTS**:
    - Deployment specification template (spec FIRST)
    - Three deployment path choices (DOKS, Hetzner, AKS)
    - Component composition (skills from L00-L09)
    - Convergence loop (iterate with AI)
    - Teardown commands with cost verification (SC-006)
    - Final skill evaluation rubric
    - "Reflect on Your Skill" section (skill finalization)
    - Maps to ALL evals: SC-001 through SC-008

**Checkpoint**: Capstone complete - Digital FTE component produced

---

## Phase 9: Polish & Cross-Cutting Validation

**Purpose**: Final validation and quality assurance

- [ ] T015 [P] Run educational-validator on ALL lessons (L00-L10)
- [ ] T016 [P] Run factual-verifier on cloud pricing and CLI commands
- [ ] T017 [P] Verify all "Reflect on Your Skill" sections present
- [ ] T018 [P] Verify all expected output blocks present (SC-008)
- [ ] T019 [P] Verify Three Roles invisible (grep for forbidden patterns)
- [ ] T020 [P] Verify no meta-commentary ("What to notice", "AI as Teacher")
- [ ] T021 Update chapter README.md with final lesson list
- [ ] T022 Run content-evaluation-framework on chapter

**Checkpoint**: Chapter validated and ready for publication

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup
    ↓
Phase 2: US1 (L00 - Skill-First) ← MUST be first lesson
    ↓
Phase 3: US2 (L01-L06 - DOKS path) ← Primary production path
    ↓ (parallel possible)
Phase 4: US3 (L07 - Hetzner path)
Phase 5: US4 (L09 - Multi-cloud)
Phase 6: US5 (L08 - Production checklist)
    ↓
Phase 8: Capstone (L10) ← Requires L00-L09 complete
    ↓
Phase 9: Polish
```

### Lesson Order (Must Follow)

1. L00 (Skill-First - MUST be first)
2. L01-L04 (DOKS foundation)
3. L05-L06 (DOKS deployment)
4. L07 (Hetzner alternative)
5. L08 (Production checklist)
6. L09 (Multi-cloud)
7. L10 (Capstone - MUST be last)

### Parallel Opportunities

- T002, T003 can run in parallel (Setup)
- T015-T020 can run in parallel (Validation)
- L05 and L06 could be parallelized (different AI collaboration focus)

---

## Task Summary

| Phase | Tasks | Lessons | User Story |
|-------|-------|---------|------------|
| Setup | T001-T003 | - | - |
| US1 | T004 | L00 | P1 |
| US2 | T005-T010 | L01-L06 | P1 |
| US3 | T011 | L07 | P2 |
| US4 | T012 | L09 | P2 |
| US5 | T013 | L08 | P2 |
| US6 | (integrated) | - | P3 |
| Capstone | T014 | L10 | ALL |
| Polish | T015-T022 | - | - |

**Total Tasks**: 22
**Total Lessons**: 11 (L00-L10)
**Estimated Implementation Time**: 5-6 hours

---

## Implementation Strategy

### MVP First (Skill-First + DOKS Path)

1. Complete Phase 1: Setup
2. Complete Phase 2: US1 (L00 - Build Skill)
3. Complete Phase 3: US2 (L01-L06 - DOKS deployment)
4. **STOP and VALIDATE**: Test DOKS deployment end-to-end
5. Students can deploy to production at this point

### Full Chapter

1. MVP + Phase 4 (Hetzner) + Phase 5-6 (Multi-cloud, Checklist)
2. Phase 8: Capstone
3. Phase 9: Polish

---

## Notes

- All lessons MUST end with "Reflect on Your Skill" section (FR-002)
- All code examples MUST include expected output blocks (SC-008)
- L2 lessons MUST apply Three Roles INVISIBLY (no meta-commentary)
- Expertise skill reference: `.claude/skills/building-with-multi-cloud/SKILL.md`
- Quality reference: Ch50 Kubernetes lessons
- Student skill: `.claude/skills/multi-cloud-deployer/`
