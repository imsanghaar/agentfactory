# Tasks: Chapter 59 - Cost & Disaster Recovery

**Input**: Design documents from `/specs/001-chapter-59-cost-disaster-recovery/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)
**Content Type**: Educational (Book Chapter - 10 Lessons)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Chapter Directory**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/`
- **Quality Reference**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/`
- **Expertise Skill**: `.claude/skills/operational-excellence/SKILL.md`

---

## Phase 1: Setup (Chapter Infrastructure)

**Purpose**: Create chapter directory structure and README

- [ ] T001 Create chapter directory: `apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/`
- [ ] T002 Create README.md with chapter overview, learning objectives, and lesson list
  - Include: Chapter goals, prerequisites (Ch50, Ch51, Ch55, Ch56), proficiency level (B1)
  - Include: Lesson structure table from plan.md
  - Include: Running example (Task API) context

**Checkpoint**: Directory structure ready for lesson implementation

---

## Phase 2: Foundational (SKILL-FIRST Pattern)

**Purpose**: Build operational-excellence skill BEFORE content lessons

**Goal**: US1 - Build Operational Excellence Skill (Priority: P1)

**Independent Test**: Invoke the created skill to generate a VPA manifest for Task API deployment

- [ ] T003 [US1] Lesson 0: Build Your Operational Excellence Skill
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/00-build-your-operational-excellence-skill.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/00-build-your-observability-skill.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, skill-first L00 template
  - **CONTENT REQUIREMENTS**:
    - Layer 3 (Intelligence Design) - Students build skill first
    - Clone fresh skills-lab
    - Write LEARNING-SPEC.md for operational excellence
    - Use `/fetching-library-docs` for VPA, OpenCost, Velero, Chaos Mesh docs
    - Use `/skill-creator` to build skill from documentation
    - Test skill generates valid VPA manifest
    - Test skill generates valid Velero Schedule
    - Include skill components: Persona, Decision Tree, Core Technologies, Safety Guardrails
    - Duration: 15 minutes
    - Maps to evals: SC-001, SC-010

**Checkpoint**: Foundation skill ready - L01-L09 can now reference it for "Reflect on Your Skill" sections

---

## Phase 3: Cost Management Lessons (L01-L04)

**Purpose**: Layer 1 (Manual Foundation) for cost concepts

### Lesson 1: Cloud Cost Fundamentals

**Goal**: US2 - Understand Cloud Costs (Priority: P1)

**Independent Test**: Student can explain cost components of a Kubernetes workload and identify which resources drive costs

- [ ] T004 [US2] Lesson 1: Cloud Cost Fundamentals
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/01-cloud-cost-fundamentals.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/01-three-pillars-of-observability.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer, fact-check-lesson
  - **CONTENT REQUIREMENTS**:
    - Layer 1 (Manual Foundation) - NO AI yet
    - New concepts: Compute costs, Storage costs, Network costs (3 concepts)
    - Explain cost components with Task API examples
    - Cost comparison table: compute vs storage vs network
    - Cost formula: `max(request, usage) x hourly_rate`
    - FinOps introduction: Visibility -> Optimization -> Operation cycle
    - Include "Reflect on Your Skill" section
    - Duration: 20 minutes
    - Maps to evals: SC-002

### Lesson 2: Right-Sizing with VPA

**Goal**: US3 - Right-Size Resources with VPA (Priority: P2)

**Independent Test**: Student can install VPA, apply it to a deployment in "Off" mode, and interpret the recommendations

- [ ] T005 [US3] Lesson 2: Right-Sizing with VPA
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/02-right-sizing-with-vpa.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/01-three-pillars-of-observability.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer, fact-check-lesson
  - **CONTENT REQUIREMENTS**:
    - Layer 1 (Manual Foundation)
    - New concepts: VPA architecture, VPA modes (Off/Initial/Recreate), VPA+HPA coexistence (3 concepts)
    - Install VPA via Helm (from skill's knowledge)
    - VPA CRD walkthrough with Task API target
    - Apply VPA in Off mode, interpret recommendations
    - Calculate potential savings: current vs recommended
    - Safety: Always start with Off mode; VPA+HPA conflict warning
    - Include complete VPA CRD example from expertise skill
    - Include "Reflect on Your Skill" section
    - Duration: 25 minutes
    - Maps to evals: SC-003

### Lesson 3: OpenCost Visibility

**Goal**: US4 - Implement Cost Visibility with OpenCost (Priority: P2)

**Independent Test**: Student can query OpenCost API for cost breakdown by namespace

- [ ] T006 [US4] Lesson 3: OpenCost/Kubecost Visibility
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/03-opencost-visibility.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/01-three-pillars-of-observability.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer, fact-check-lesson
  - **CONTENT REQUIREMENTS**:
    - Layer 1 (Manual Foundation)
    - New concepts: OpenCost architecture, Cost allocation queries (2 concepts)
    - Install OpenCost via Helm with Prometheus connection
    - Query `/allocation` API with `aggregate=namespace`
    - Query with `aggregate=label:team`
    - Idle cost concept: provisioned - allocated
    - Kubecost vs OpenCost comparison
    - Include API query examples from expertise skill
    - Include "Reflect on Your Skill" section
    - Duration: 25 minutes
    - Maps to evals: SC-004

### Lesson 4: FinOps Practices & Budget Alerts

**Goal**: Extended US2/US4 - FinOps maturity and tagging strategy

**Independent Test**: Student can implement cost allocation labels and explain showback vs chargeback progression

- [ ] T007 [US2] Lesson 4: FinOps Practices and Budget Alerts
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/04-finops-practices-budget-alerts.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/01-three-pillars-of-observability.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer, fact-check-lesson
  - **CONTENT REQUIREMENTS**:
    - Layer 1 (Manual Foundation)
    - New concepts: Cost allocation labels, FinOps progression (2 concepts)
    - Required labels: team, app, environment, cost-center
    - Add labels to Task API deployment
    - Query OpenCost with new labels
    - FinOps maturity: showback -> allocation -> chargeback
    - Why showback before chargeback (build trust)
    - Budget alerts concept (conceptual - full implementation Ch55)
    - Include "Reflect on Your Skill" section
    - Duration: 20 minutes
    - Maps to evals: SC-002

**Checkpoint**: Cost management lessons complete (L01-L04). Students understand cost drivers, VPA, OpenCost, and FinOps practices.

---

## Phase 4: Disaster Recovery Lessons (L05-L06)

**Purpose**: Layer 1 -> Layer 2 transition for backup/restore concepts

### Lesson 5: Backup Fundamentals

**Goal**: US5 - Define Backup Strategy (Priority: P1)

**Independent Test**: Student can articulate RTO/RPO requirements and explain how 3-2-1 rule achieves them

- [ ] T008 [US5] Lesson 5: Backup Fundamentals
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/05-backup-fundamentals.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/01-three-pillars-of-observability.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer, fact-check-lesson
  - **CONTENT REQUIREMENTS**:
    - Layer 1 (Manual Foundation)
    - New concepts: RTO, RPO, 3-2-1 backup rule (3 concepts)
    - RTO definition: Maximum acceptable downtime
    - RPO definition: Maximum acceptable data loss
    - Business scenario exercise: Task API requirements
    - 3-2-1 rule: 3 copies, 2 storage types, 1 offsite
    - Backup strategy comparison table (from plan.md)
    - Include "Reflect on Your Skill" section
    - Duration: 20 minutes
    - Maps to evals: SC-005

### Lesson 6: Velero for K8s Backup/Restore

**Goal**: US6 - Implement Velero Backups (Priority: P2)

**Independent Test**: Student can create a Velero Schedule that backs up a namespace daily with 30-day retention

- [ ] T009 [US6] Lesson 6: Velero for K8s Backup/Restore
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/06-velero-backup-restore.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/01-three-pillars-of-observability.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching
  - **CONTENT REQUIREMENTS**:
    - Layer 1 -> Layer 2 (Manual foundation + AI collaboration)
    - New concepts: Velero CRDs, backup hooks, restore procedures (3 concepts)
    - Install Velero via Helm with MinIO for local dev
    - Create BackupStorageLocation
    - Velero CRD walkthrough: Backup vs Schedule
    - TTL for retention (720h = 30 days)
    - **THREE ROLES SECTION** (Layer 2):
      - AI as Teacher: Suggests backup hooks for database consistency
      - AI as Student: Adapts retention based on requirements
      - AI as Co-Worker: Iterates on hook timeout values
    - Include complete Schedule CRD with hooks from expertise skill
    - Include restore procedure examples
    - Include "Reflect on Your Skill" section
    - Duration: 30 minutes
    - Maps to evals: SC-006

**Checkpoint**: Disaster recovery lessons complete (L05-L06). Students understand RTO/RPO, 3-2-1 rule, and can implement Velero backups.

---

## Phase 5: Resilience Lessons (L07-L08)

**Purpose**: Layer 1 -> Layer 2 for chaos engineering and compliance

### Lesson 7: Chaos Engineering Basics

**Goal**: US7 - Validate Resilience with Chaos Mesh (Priority: P2)

**Independent Test**: Student can create a PodChaos experiment and measure recovery time

- [ ] T010 [US7] Lesson 7: Chaos Engineering Basics
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/07-chaos-engineering-basics.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/01-three-pillars-of-observability.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching
  - **CONTENT REQUIREMENTS**:
    - Layer 1 -> Layer 2 (Manual foundation + AI collaboration)
    - New concepts: Chaos principles, PodChaos, Game Day pattern (3 concepts)
    - Install Chaos Mesh via Helm with namespace filtering
    - Annotate staging namespace for chaos experiments
    - PodChaos experiment walkthrough
    - Safety features: namespace filtering, duration limits, selectors
    - **THREE ROLES SECTION** (Layer 2):
      - AI as Teacher: Teaches Game Day structured approach
      - AI as Student: Learns student's specific RTO requirements
      - AI as Co-Worker: Iterates on experiment scope (mode: one vs all)
    - Include complete PodChaos CRD from expertise skill
    - Include Game Day checklist from plan.md
    - Include "Reflect on Your Skill" section
    - Duration: 30 minutes
    - Maps to evals: SC-007

### Lesson 8: Data Sovereignty & Compliance

**Goal**: Extended US8 - Compliance foundation for capstone

**Independent Test**: Student can articulate GDPR implications for multi-region deployments

- [ ] T011 [US8] Lesson 8: Data Sovereignty and Compliance
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/08-data-sovereignty-compliance.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/01-three-pillars-of-observability.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer, fact-check-lesson
  - **CONTENT REQUIREMENTS**:
    - Layer 1 (Manual Foundation - conceptual, no code)
    - New concepts: Data sovereignty, audit trails (2 concepts)
    - Data sovereignty: Legal requirements for data residency
    - GDPR implications: EU data must stay in EU regions
    - Backup location considerations: Where Velero stores backups matters
    - Encryption requirements: At-rest and in-transit
    - Audit trails: K8s audit logs, Velero backup logs
    - NOT in scope: SOC2, ISO27001 certification processes
    - Include "Reflect on Your Skill" section
    - Duration: 20 minutes
    - Maps to evals: SC-008

**Checkpoint**: Resilience lessons complete (L07-L08). Students understand chaos engineering and compliance basics.

---

## Phase 6: Capstone Integration (L09)

**Purpose**: Layer 4 (Spec-Driven Integration) - Full chapter synthesis

**Goal**: US8 - Capstone Integration (Priority: P3)

**Independent Test**: Complete Task API with cost labels visible in OpenCost, Velero backups running, and passing chaos experiment

- [ ] T012 [US8] Lesson 9: Capstone - Resilient, Cost-Aware Task API
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/59-cost-disaster-recovery/09-capstone-resilient-cost-aware-task-api.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/10-capstone-full-observability-stack.md`
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer, assessment-builder, ai-collaborate-teaching
  - **CONTENT REQUIREMENTS**:
    - Layer 4 (Spec-Driven Integration)
    - New concepts: Integration patterns (1 concept - synthesis lesson)
    - **Phase 1: Write Specification** (Spec-First)
      - Task API Operational Excellence Spec
      - Success criteria: cost labels, VPA, Velero, chaos test
    - **Phase 2: Component Composition**
      - Cost allocation labels from L04
      - VPA from L02
      - Velero Schedule from L06
      - PodChaos experiment from L07
    - **Phase 3: AI Orchestration**
      - AI implements spec using operational-excellence skill
      - Student validates against spec requirements
    - **Phase 4: Convergence and Validation**
      - Complete verification checklist from plan.md
      - Measure actual recovery time against 30s RTO
      - Verify cost labels appear in OpenCost
      - Verify backup schedule is running
    - Include complete deployment with labels from plan.md
    - Include capstone artifacts list
    - Include "Reflect on Your Skill" section (skill finalization)
    - Duration: 40 minutes
    - Maps to evals: SC-009, SC-010

**Checkpoint**: Capstone complete. All 10 success criteria from spec should be achievable.

---

## Phase 7: Validation & Polish

**Purpose**: Run validators, create chapter quiz, finalize documentation

- [ ] T013 [P] Run educational-validator on all 10 lesson files
  - Verify YAML frontmatter completeness (skills, learning_objectives, cognitive_load, differentiation)
  - Verify narrative openings
  - Verify "Try With AI" prompts (3 per lesson)
  - Verify "Reflect on Your Skill" sections (L01-L09)
  - Verify Three Roles demonstrations (L06, L07)

- [ ] T014 [P] Run factual-verifier on all lessons
  - Verify all statistics and dates
  - Verify tool version numbers
  - Verify CNCF project status (OpenCost, Velero, Chaos Mesh)
  - Verify VPA, OpenCost, Velero, Chaos Mesh API patterns

- [ ] T015 [P] Run pedagogical-designer review
  - Verify 4-Layer progression (L3 -> L1 -> L1->L2 -> L4)
  - Verify cognitive load limits (B1: 2-4 concepts per lesson)
  - Verify skill dependencies satisfied by lesson order

- [ ] T016 Create chapter assessment using assessment-architect
  - **SUBAGENT**: assessment-architect
  - Include quiz questions for each success criterion (SC-001 through SC-010)
  - Mix question types: MCQ, scenario-based, code review
  - Target Bloom's levels: Remember, Understand, Apply
  - Output: Chapter quiz or assessment file

- [ ] T017 Update README.md with final lesson list and verification status

- [ ] T018 Run canonical-format-checker on skill references
  - Verify CRD examples match official formats
  - Verify skill format follows `.claude/skills/<name>/SKILL.md` pattern

**Checkpoint**: All validators pass. Chapter ready for publication.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup - MUST complete L00 before any other lessons
- **Cost Management (Phase 3)**: Depends on Phase 2 - L01-L04 can be parallelized (different files)
- **Disaster Recovery (Phase 4)**: Depends on Phase 2 - L05-L06 can be parallelized (different files)
- **Resilience (Phase 5)**: Depends on Phase 2 - L07-L08 can be parallelized (different files)
- **Capstone (Phase 6)**: Depends on Phases 3-5 completion (synthesizes all concepts)
- **Validation (Phase 7)**: Depends on all lessons being written

### Lesson Dependencies (within chapter)

- **L00**: No dependencies - MUST complete first (skill-first pattern)
- **L01**: Depends on L00 (skill exists for reflection)
- **L02**: Depends on L01 (cost fundamentals vocabulary)
- **L03**: Depends on L01-L02, Ch55 Prometheus
- **L04**: Depends on L03 (OpenCost installed)
- **L05**: Depends on L00 only (conceptual - no code prereqs)
- **L06**: Depends on L05 (RTO/RPO concepts)
- **L07**: Depends on L05-L06 (backup provides safety net)
- **L08**: Depends on L06 (Velero storage concepts)
- **L09**: Depends on ALL previous lessons (capstone integration)

### Parallel Opportunities

```bash
# After L00 completes, these can run in parallel:
T004 (L01), T005 (L02)  # Different files, cost focus
T008 (L05)              # Different file, backup focus (conceptual)

# After L01-L02 complete:
T006 (L03), T007 (L04)  # Different files, OpenCost + FinOps

# After L05-L06 complete:
T010 (L07), T011 (L08)  # Different files, chaos + compliance

# Validation phase - all parallel:
T013, T014, T015, T016, T017, T018  # Different validators, independent
```

---

## Implementation Strategy

### MVP First (L00 + L01 + L09)

1. Complete Phase 1: Setup
2. Complete Phase 2: L00 (Skill-first - CRITICAL)
3. Implement L01 (Cloud Cost Fundamentals)
4. Implement L09 (Capstone - skeleton)
5. **VALIDATE**: Test skill creation and cost concepts
6. Iterate based on feedback

### Incremental Delivery

1. Setup + L00 -> Skill foundation ready
2. L01-L04 -> Cost management complete -> Test independently
3. L05-L06 -> Disaster recovery complete -> Test independently
4. L07-L08 -> Resilience complete -> Test independently
5. L09 -> Capstone integrates all -> Full chapter test
6. Phase 7 -> Validation -> Publication ready

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + L00 together
2. Once L00 is done:
   - Developer A: L01, L02
   - Developer B: L05, L06
   - Developer C: L07, L08
3. L03, L04 after L01-L02 complete
4. L09 after all lessons complete
5. Validation in parallel

---

## Summary

| Phase | Task Count | User Stories | Parallel Opportunities |
|-------|------------|--------------|------------------------|
| Setup | 2 | - | Yes (T001, T002) |
| Foundational | 1 | US1 | No (blocking) |
| Cost Management | 4 | US2, US3, US4 | Yes (T004, T005) then (T006, T007) |
| Disaster Recovery | 2 | US5, US6 | Yes (T008, T009) |
| Resilience | 2 | US7, US8 | Yes (T010, T011) |
| Capstone | 1 | US8 | No (synthesis) |
| Validation | 6 | - | Yes (all parallel) |

**Total Tasks**: 18
**Total Lessons**: 10 (L00-L09)
**Estimated Implementation**: Sequential - all lessons, Parallel - grouped by phase
