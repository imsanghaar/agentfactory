# Tasks: Chapter 49 - Docker for AI Services

**Input**: Design documents from `/specs/001-docker-chapter/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)
**Tests**: Not applicable (content authoring, not code)
**Organization**: Tasks grouped by lesson to enable independent implementation
**Repository**: `panaversity/ai-native-software-development`

---

## GitHub Issues

| Phase | Issue | Title |
|-------|-------|-------|
| 0 | [#356](https://github.com/panaversity/ai-native-software-development/issues/356) | Study & Context Gathering |
| 1 | [#357](https://github.com/panaversity/ai-native-software-development/issues/357) | Setup - Chapter Infrastructure |
| 2 | [#358](https://github.com/panaversity/ai-native-software-development/issues/358) | Foundational - Shared Assets |
| 3 | [#359](https://github.com/panaversity/ai-native-software-development/issues/359) | Lesson 1 - Docker Installation & Setup |
| 4 | [#360](https://github.com/panaversity/ai-native-software-development/issues/360) | Lesson 2 - Container Fundamentals |
| 5 | [#361](https://github.com/panaversity/ai-native-software-development/issues/361) | Lesson 3 - Writing Your First Dockerfile |
| 6 | [#362](https://github.com/panaversity/ai-native-software-development/issues/362) | Lesson 4 - Container Lifecycle & Debugging |
| 7 | [#363](https://github.com/panaversity/ai-native-software-development/issues/363) | Lesson 5 - Multi-Stage Builds & Optimization |
| 8 | [#364](https://github.com/panaversity/ai-native-software-development/issues/364) | Lesson 6 - Docker Compose for Development |
| 9 | [#365](https://github.com/panaversity/ai-native-software-development/issues/365) | Lesson 7 - Security & Best Practices |
| 10 | [#366](https://github.com/panaversity/ai-native-software-development/issues/366) | Lesson 8 - AI-Assisted Docker with Gordon |
| 11 | [#367](https://github.com/panaversity/ai-native-software-development/issues/367) | Lesson 9 - Capstone: Production-Ready Agent |
| 12 | [#368](https://github.com/panaversity/ai-native-software-development/issues/368) | Lesson 10 - Building the Production Dockerfile Skill |
| 13 | [#369](https://github.com/panaversity/ai-native-software-development/issues/369) | Polish & Cross-Cutting Concerns |

### Closing Issues

When a phase is complete, close the corresponding issue:
```bash
gh issue close <issue-number> --repo panaversity/ai-native-software-development --comment "Phase complete. All tasks done."
```

Or include `Closes #<issue-number>` in your commit message to auto-close on merge.

---

## CRITICAL: Pre-Implementation Study Requirements

**Before writing ANY lesson content, the implementing agent MUST:**

### 1. Study Docker Domain Knowledge (MANDATORY)

**Primary Reference**: `cloud-books/docker_deep_dive.md` (Nigel Poulton, 2024)
- This is the authoritative Docker reference - read relevant chapters before writing each lesson
- Cross-reference with official Docker docs for 2025 updates

**Official Documentation** (fetch as needed):
- Docker Get Started: https://docs.docker.com/get-started/
- Docker Hardened Images: https://www.docker.com/blog/docker-hardened-images/
- Docker Scout: https://docs.docker.com/scout/
- Docker Compose: https://docs.docker.com/compose/

### 2. Study the Reference Format (MANDATORY)

Read and internalize the structure from these reference lessons:

```
apps/learn-app/docs/02-AI-Tool-Landscape/06-gemini-cli-installation-and-basics/03-built-in-tools-deep-dive.md
```

**Extract and follow**:
- YAML frontmatter structure (learning objectives, CEFR level, cognitive load, Bloom's level)
- Section organization pattern
- "Try With AI" section format (action prompts, NOT meta-commentary)
- Code block formatting conventions
- Exercise structure

### 3. Study the Constitution (MANDATORY)

Read `.specify/memory/constitution.md` (v6.0.1) focusing on:
- Section IIa: 4-Layer Teaching Method
- Section IIa: Three Roles Framework (must be INVISIBLE in student content)
- Section IIa: Meta-Commentary Prohibition (forbidden patterns)
- Section III: 7 Foundational Principles

### 4. Study the Chapter Specification

Read `specs/001-docker-chapter/spec.md` for:
- User Stories and acceptance scenarios
- Functional requirements per lesson
- Success criteria targets
- Technology context (DHI, Scout, Gordon, etc.)

### 5. Study the Chapter Plan

Read `specs/001-docker-chapter/plan.md` for:
- Per-lesson learning objectives
- Concepts inventory per lesson
- Teaching modality per lesson
- Exercise specifications

**Validation**: Before starting Phase 3 (Lesson 1), agent should be able to answer:
- What is the difference between an image and a container? (Docker Deep Dive Ch 6-7)
- What are Docker Hardened Images and why use them? (2025 update)
- What YAML frontmatter fields are required?
- What does a "Try With AI" section look like (correct format)?
- What patterns are FORBIDDEN in student-facing content?
- What teaching modality does each lesson use?

---

## Format: `[ID] [P?] [Lesson] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Lesson]**: Which lesson this task belongs to (L1, L2, L3, etc.)
- Include exact file paths in descriptions

## Path Conventions

- **Lesson files**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/`
- **Assets**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/assets/`
- **Reference format**: `apps/learn-app/docs/02-AI-Tool-Landscape/06-gemini-cli-installation-and-basics/03-built-in-tools-deep-dive.md`
- **Constitution**: `.specify/memory/constitution.md`

---

## Phase 0: Study & Context Gathering (BLOCKING) — [#356](https://github.com/panaversity/ai-native-software-development/issues/356)

**Purpose**: Agent builds mental model of Docker domain AND book conventions before writing content
**Duration**: 3-5 hours
**CRITICAL**: This phase MUST complete before ANY content writing begins
**Close Issue**: `gh issue close 356 --repo panaversity/ai-native-software-development` when complete

### 0a. Domain Knowledge (Docker Expertise)

- [ ] T000a [P] Read Docker Deep Dive book: `cloud-books/docker_deep_dive.md` (Nigel Poulton, 2024) - comprehensive Docker reference
- [ ] T000b [P] Read official Docker documentation: https://docs.docker.com/get-started/ (use WebFetch)
- [ ] T000c [P] Read Docker Hardened Images (DHI) announcement: https://www.docker.com/blog/docker-hardened-images/ (use WebFetch)
- [ ] T000d [P] Read Docker Scout documentation: https://docs.docker.com/scout/ (use WebFetch)
- [ ] T000e Extract key concepts from Docker Deep Dive for each lesson topic
- [ ] T000f Note any differences between book content and 2025 Docker updates (DHI, Scout, Gordon)

### 0b. Book Format & Constitution

- [ ] T000g [P] Read reference lesson format: `apps/learn-app/docs/02-AI-Tool-Landscape/06-gemini-cli-installation-and-basics/03-built-in-tools-deep-dive.md`
- [ ] T000h [P] Read constitution v6.0.1: `.specify/memory/constitution.md` (focus on Section IIa and III)
- [ ] T000i [P] Read chapter specification: `specs/001-docker-chapter/spec.md`
- [ ] T000j [P] Read chapter plan: `specs/001-docker-chapter/plan.md`
- [ ] T000k Extract YAML frontmatter template from reference lesson
- [ ] T000l Extract "Try With AI" section template (correct format, no meta-commentary)
- [ ] T000m List forbidden patterns from constitution (grep validation commands)
- [ ] T000n Confirm understanding: List teaching modality for each of 10 lessons

**Checkpoint**: Agent can explain Docker concepts accurately AND reproduce correct lesson format

**Validation Questions**:
1. What is the difference between an image and a container? (from Docker Deep Dive)
2. What are Docker Hardened Images and why use them? (from DHI docs)
3. What YAML frontmatter fields are required? (from reference lesson)
4. What patterns are FORBIDDEN in student-facing content? (from constitution)

---

## Phase 1: Setup (Chapter Infrastructure) — [#357](https://github.com/panaversity/ai-native-software-development/issues/357)

**Purpose**: Create chapter structure and shared infrastructure
**Close Issue**: `gh issue close 357 --repo panaversity/ai-native-software-development` when complete

- [ ] T001 Create chapter directory at `apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/`
- [ ] T002 [P] Create chapter README.md with 10-lesson overview and learning path
- [ ] T003 [P] Create `assets/` directory for images, diagrams, and code samples
- [ ] T004 [P] Create `_category_.json` for Docusaurus sidebar configuration

**Checkpoint**: Chapter structure ready for lesson content

---

## Phase 2: Foundational (Shared Assets) — [#358](https://github.com/panaversity/ai-native-software-development/issues/358)

**Purpose**: Create shared assets used across multiple lessons
**CRITICAL**: This phase MUST complete before lesson writing begins
**Close Issue**: `gh issue close 358 --repo panaversity/ai-native-software-development` when complete

- [ ] T005 Create sample FastAPI agent code at `assets/sample-agent/` (used in L3-L9)
- [ ] T006 [P] Create architecture diagram showing chapter learning progression at `assets/learning-arc.png`
- [ ] T007 [P] Create Docker concept diagram (images vs containers vs layers) at `assets/docker-concepts.png`
- [ ] T008 [P] Create `assets/dockerfiles/` directory with progressive Dockerfile examples
- [ ] T009 Create `.env.example` file template for environment variable exercises

**Checkpoint**: Shared assets ready - lesson writing can begin

---

## Phase 3: Lesson 1 - Docker Installation & Setup (Priority: P0) — [#359](https://github.com/panaversity/ai-native-software-development/issues/359)

**Goal**: Student installs Docker and verifies working environment
**Duration**: 30-45 minutes writing time (2-3 hours implementation)
**Teaching Modality**: Guided Installation
**Reference**: User Story 0 (Install and Verify Docker Environment)
**Close Issue**: `gh issue close 359 --repo panaversity/ai-native-software-development` when complete

### Implementation for Lesson 1

- [ ] T010 [L1] Create lesson file `01-docker-installation-setup.md` with YAML frontmatter
- [ ] T011 [L1] Write learning objectives (Bloom's: Remember, Understand)
- [ ] T012 [L1] Write "Key Concepts" section (4 concepts: Docker Desktop, Engine, Resources, Hub)
- [ ] T013 [L1] Write platform-specific installation guides (macOS, Windows WSL2, Linux)
- [ ] T014 [L1] Write verification exercises (`docker --version`, `docker run hello-world`)
- [ ] T015 [L1] Write resource configuration section (memory limits, disk settings)
- [ ] T016 [L1] Write Docker Hub authentication section (`docker login`)
- [ ] T017 [L1] Write troubleshooting section for common installation issues
- [ ] T018 [L1] Create installation screenshots at `assets/lesson-01/`

**Checkpoint**: Lesson 1 complete - students can install Docker and verify environment

---

## Phase 4: Lesson 2 - Container Fundamentals (Priority: P1) — [#360](https://github.com/panaversity/ai-native-software-development/issues/360)

**Goal**: Student understands images vs containers and Docker mental model
**Duration**: 45-60 minutes writing time (2-3 hours implementation)
**Teaching Modality**: Hands-On Discovery
**Reference**: User Story 1 (Containerize Existing Agent) - foundational knowledge
**Close Issue**: `gh issue close 360` when complete

### Implementation for Lesson 2

- [ ] T019 [L2] Create lesson file `02-container-fundamentals.md` with YAML frontmatter
- [ ] T020 [L2] Write learning objectives (Bloom's: Understand, Apply)
- [ ] T021 [L2] Write "Key Concepts" section (6 concepts: images, containers, layers, registries, lifecycle, caching)
- [ ] T022 [L2] Write "Why Containers? Why Cloud?" 5-minute intro section
- [ ] T023 [L2] Write hands-on exercise: pull nginx image
- [ ] T024 [L2] Write hands-on exercise: run container with port mapping
- [ ] T025 [L2] Write hands-on exercise: inspect layers with `docker history`
- [ ] T026 [L2] Write hands-on exercise: list, stop, remove containers
- [ ] T027 [L2] Create layer diagram at `assets/lesson-02/layers-diagram.png`

**Checkpoint**: Lesson 2 complete - students understand Docker architecture

---

## Phase 5: Lesson 3 - Writing Your First Dockerfile (Priority: P1) — [#361](https://github.com/panaversity/ai-native-software-development/issues/361)

**Goal**: Student writes and builds first Dockerfile for FastAPI agent
**Duration**: 60 minutes writing time (2-3 hours implementation)
**Teaching Modality**: Hands-On Creation
**Reference**: User Story 1 (Containerize Existing Agent)
**Close Issue**: `gh issue close 361` when complete

### Implementation for Lesson 3

- [ ] T028 [L3] Create lesson file `03-writing-first-dockerfile.md` with YAML frontmatter
- [ ] T029 [L3] Write learning objectives (Bloom's: Apply, Analyze)
- [ ] T030 [L3] Write "Key Concepts" section (7 concepts: Dockerfile structure, FROM, WORKDIR, COPY, RUN, CMD, EXPOSE)
- [ ] T031 [L3] Write base image selection section (introduce DHI `dhi.io/python:3.12`)
- [ ] T032 [L3] Write step-by-step Dockerfile creation walkthrough
- [ ] T033 [L3] Write hands-on exercise: write Dockerfile from scratch
- [ ] T034 [L3] Write hands-on exercise: build image with `docker build`
- [ ] T035 [L3] Write hands-on exercise: run and test API with curl
- [ ] T036 [L3] Create `assets/lesson-03/basic-dockerfile.txt` example
- [ ] T037 [L3] Write assessment criteria (build succeeds, <500MB, API responds)

**Checkpoint**: Lesson 3 complete - students can containerize basic Python app

---

## Phase 6: Lesson 4 - Container Lifecycle & Debugging (Priority: P1) — [#362](https://github.com/panaversity/ai-native-software-development/issues/362)

**Goal**: Student can debug and operate running containers
**Duration**: 45-60 minutes writing time (2-3 hours implementation)
**Teaching Modality**: Error Analysis & Debugging
**Reference**: User Story 1.5 (Debug and Operate Running Containers)
**Close Issue**: `gh issue close 362` when complete

### Implementation for Lesson 4

- [ ] T038 [L4] Create lesson file `04-container-lifecycle-debugging.md` with YAML frontmatter
- [ ] T039 [L4] Write learning objectives (Bloom's: Apply, Analyze)
- [ ] T040 [L4] Write "Key Concepts" section (6 concepts: logs, exec, inspect, env vars, ports, restart policies)
- [ ] T041 [L4] Write hands-on exercise: view container logs (`docker logs`, `-f` flag)
- [ ] T042 [L4] Write hands-on exercise: exec into container (`docker exec -it`)
- [ ] T043 [L4] Write hands-on exercise: inspect container state (`docker inspect`)
- [ ] T044 [L4] Write hands-on exercise: pass environment variables (`--env`, `--env-file`)
- [ ] T045 [L4] Write hands-on exercise: configure port mapping
- [ ] T046 [L4] Write hands-on exercise: test restart policies
- [ ] T047 [L4] Create deliberately broken container example for debugging exercise
- [ ] T048 [L4] Write assessment criteria (identify error from logs, fix with env var)

**Checkpoint**: Lesson 4 complete - students can troubleshoot container issues

---

## Phase 7: Lesson 5 - Multi-Stage Builds & Optimization (Priority: P2) — [#363](https://github.com/panaversity/ai-native-software-development/issues/363)

**Goal**: Student reduces image size by 60%+ through optimization
**Duration**: 60 minutes writing time (2-3 hours implementation)
**Teaching Modality**: Iterative Optimization
**Reference**: User Story 2 (Optimize Image Size and Build Speed)
**Close Issue**: `gh issue close 363` when complete

### Implementation for Lesson 5

- [ ] T049 [L5] Create lesson file `05-multi-stage-builds-optimization.md` with YAML frontmatter
- [ ] T050 [L5] Write learning objectives (Bloom's: Apply, Analyze, Evaluate)
- [ ] T051 [L5] Write "Key Concepts" section (7 concepts: build/runtime stages, caching, UV, .dockerignore, size measurement, context, volume mounts)
- [ ] T052 [L5] Write hands-on exercise: measure original image size
- [ ] T053 [L5] Write multi-stage Dockerfile refactoring walkthrough (builder + runtime)
- [ ] T054 [L5] Write hands-on exercise: create .dockerignore file
- [ ] T055 [L5] Write hands-on exercise: integrate UV package manager
- [ ] T056 [L5] Write hands-on exercise: measure and verify 60%+ reduction
- [ ] T056a [L5] Write hands-on exercise: handle large model files (>1GB) with volume mounts instead of COPY (FR-025)
- [ ] T057 [L5] Create `assets/lesson-05/multi-stage-dockerfile.txt` example
- [ ] T058 [L5] Write Docker Bake mention (advanced topic, link to docs)
- [ ] T059 [L5] Write assessment criteria (<300MB, 60%+ smaller, functionality preserved)

**Checkpoint**: Lesson 5 complete - students produce optimized images

---

## Phase 8: Lesson 6 - Docker Compose for Development (Priority: P2) — [#364](https://github.com/panaversity/ai-native-software-development/issues/364)

**Goal**: Student runs multi-service development environment
**Duration**: 60 minutes writing time (2-3 hours implementation)
**Teaching Modality**: Specification-First
**Reference**: User Story 3 (Multi-Container Local Development)
**Close Issue**: `gh issue close 364` when complete

### Implementation for Lesson 6

- [ ] T060 [L6] Create lesson file `06-docker-compose-development.md` with YAML frontmatter
- [ ] T061 [L6] Write learning objectives (Bloom's: Apply, Analyze)
- [ ] T062 [L6] Write "Key Concepts" section (6 concepts: compose structure, services, ports, health checks, volumes, dependencies)
- [ ] T063 [L6] Write architecture diagram introduction (agent + Postgres + Redis)
- [ ] T064 [L6] Write hands-on exercise: write docker-compose.yml
- [ ] T065 [L6] Write hands-on exercise: define health checks
- [ ] T066 [L6] Write hands-on exercise: configure named volumes
- [ ] T067 [L6] Write hands-on exercise: set up service dependencies
- [ ] T068 [L6] Write hands-on exercise: run with `docker-compose up`
- [ ] T069 [L6] Write hands-on exercise: verify services and networking
- [ ] T070 [L6] Create `assets/lesson-06/docker-compose.yml` example
- [ ] T071 [L6] Write assessment criteria (3 services start, health checks pass, volumes persist)

**Checkpoint**: Lesson 6 complete - students can run complete dev stack

---

## Phase 9: Lesson 7 - Security & Best Practices (Priority: P2) — [#365](https://github.com/panaversity/ai-native-software-development/issues/365)

**Goal**: Student produces hardened images with zero critical CVEs
**Duration**: 60 minutes writing time (2-3 hours implementation)
**Teaching Modality**: Audit & Remediation
**Reference**: User Story 4 (Secure Container with Best Practices)
**Close Issue**: `gh issue close 365` when complete

### Implementation for Lesson 7

- [ ] T072 [L7] Create lesson file `07-security-best-practices.md` with YAML frontmatter
- [ ] T073 [L7] Write learning objectives (Bloom's: Apply, Analyze, Evaluate)
- [ ] T074 [L7] Write "Key Concepts" section (5 concepts: non-root, Scout, DHI, secrets, health checks)
- [ ] T075 [L7] Write hands-on exercise: build deliberately insecure image
- [ ] T076 [L7] Write hands-on exercise: scan with Docker Scout (`docker scout cves`)
- [ ] T077 [L7] Write hands-on exercise: interpret CVE report
- [ ] T078 [L7] Write hands-on exercise: refactor to non-root user (UID 1000)
- [ ] T079 [L7] Write hands-on exercise: switch to DHI base image
- [ ] T080 [L7] Write hands-on exercise: add HEALTHCHECK instruction
- [ ] T081 [L7] Write hands-on exercise: rescan and verify 90%+ CVE reduction
- [ ] T082 [L7] Create `assets/lesson-07/hardened-dockerfile.txt` example
- [ ] T083 [L7] Write assessment criteria (non-root confirmed, 90%+ CVE reduction, health check functional)

**Checkpoint**: Lesson 7 complete - students produce secure images

---

## Phase 10: Lesson 8 - AI-Assisted Docker with Gordon (Priority: P3) — [#366](https://github.com/panaversity/ai-native-software-development/issues/366)

**Goal**: Student demonstrates AI collaboration for Docker workflows
**Duration**: 45-60 minutes writing time (3-4 hours implementation)
**Teaching Modality**: AI Collaboration (Three Roles INVISIBLE)
**Reference**: User Story 5 (AI-Assisted Docker Workflows)
**Close Issue**: `gh issue close 366` when complete

**CRITICAL**: Three Roles framework INVISIBLE. No "AI as Teacher/Student/Co-Worker" labels. Use action prompts and reflection questions only.

### Implementation for Lesson 8

- [ ] T084 [L8] Create lesson file `08-ai-assisted-docker-gordon.md` with YAML frontmatter
- [ ] T085 [L8] Write learning objectives (Bloom's: Apply, Evaluate, Create)
- [ ] T086 [L8] Write "Key Concepts" section (5 concepts: Gordon, prompting, debugging, optimization, iteration)
- [ ] T086a [L8] Write Gordon availability note: "Requires Docker Desktop 4.55+. Fallback: manual Dockerfile writing with optimization principles from L5-L7"
- [ ] T087 [L8] Write Part 1: Initial Request - "Ask Gordon to generate Dockerfile"
- [ ] T088 [L8] Write Part 2: Critical Evaluation - reflection questions (not framework labels)
- [ ] T089 [L8] Write Part 3: Constraint Teaching - "Tell Gordon your CI requires sub-2-min builds"
- [ ] T090 [L8] Write Part 4: Refinement Loop - debugging with Gordon
- [ ] T091 [L8] Write Part 5: Reflection - "What improved through iteration?"
- [ ] T092 [L8] Write "Try With AI" section with action prompts (NO "What to notice" meta-commentary)
- [ ] T093 [L8] Validate lesson for forbidden patterns: grep for "AI as Teacher", "What to notice", framework labels
- [ ] T094 [L8] Write assessment criteria (Gordon-generated Dockerfile works, iteration improves quality)

**Checkpoint**: Lesson 8 complete - students experience AI collaboration (framework invisible)

---

## Phase 11: Lesson 9 - Capstone: Production-Ready Agent (Priority: P3) — [#367](https://github.com/panaversity/ai-native-software-development/issues/367)

**Goal**: Student delivers production-ready containerized agent to registry
**Duration**: 90 minutes writing time (3-4 hours implementation)
**Teaching Modality**: Specification-First Project
**Reference**: User Story 6 (Push Image to Registry)
**Close Issue**: `gh issue close 367` when complete

### Implementation for Lesson 9

- [ ] T095 [L9] Create lesson file `09-capstone-production-ready-agent.md` with YAML frontmatter
- [ ] T096 [L9] Write learning objectives (Bloom's: Create, Evaluate)
- [ ] T097 [L9] Write Phase 1: Specification Writing (20-30 min student time)
- [ ] T098 [L9] Write spec.md template for students (150-200 words, acceptance criteria)
- [ ] T099 [L9] Write Phase 2: Composition & Implementation (40-50 min student time)
- [ ] T100 [L9] Write composition checklist (L3 basics + L5 optimization + L7 security + optional L8 Gordon)
- [ ] T101 [L9] Write Phase 3: Validation & Testing (15-20 min student time)
- [ ] T102 [L9] Write validation checklist (build, size, security scan, functionality, registry push)
- [ ] T103 [L9] Write Phase 4: Reflection (10 min student time)
- [ ] T104 [L9] Write hands-on exercise: tag with semantic version
- [ ] T105 [L9] Write hands-on exercise: push to Docker Hub
- [ ] T106 [L9] Write hands-on exercise: verify portability (pull on different machine)
- [ ] T107 [L9] Write deliverables list (spec.md, Dockerfile, .dockerignore, pushed image, portability verification)
- [ ] T108 [L9] Write assessment criteria (<400MB, zero critical CVEs, functionality verified, portability validated)

**Checkpoint**: Lesson 9 complete - students have production-ready container in registry

---

## Phase 12: Lesson 10 - Building the Production Dockerfile Skill (Priority: P3) — [#368](https://github.com/panaversity/ai-native-software-development/issues/368)

**Goal**: Student creates reusable agent skill for production-ready multi-stage Docker builds
**Duration**: 60-75 minutes writing time (3-4 hours implementation)
**Teaching Modality**: Intelligence Design (Layer 3)
**Layer**: L3 (Transform tacit knowledge into explicit, reusable intelligence)
**Reference**: Constitution Section IIa - Layer 3: Intelligence Design
**Close Issue**: `gh issue close 368` when complete

**CRITICAL**: This lesson demonstrates the paradigm shift from "reusable code" to "reusable intelligence." Students encode their Docker knowledge from L1-L9 into a skill that can be applied across ALL future containerization projects.

### Implementation for Lesson 10

- [ ] T109 [L10] Create lesson file `10-building-production-dockerfile-skill.md` with YAML frontmatter
- [ ] T110 [L10] Write learning objectives (Bloom's: Create, Evaluate, Synthesize)
- [ ] T111 [L10] Write "Key Concepts" section (6 concepts: skills vs subagents, Persona+Questions+Principles pattern, decision points, reusability, skill file structure, skill invocation)
- [ ] T112 [L10] Write introduction: "From Knowledge to Intelligence" - why encode Docker expertise as skill
- [ ] T113 [L10] Write decision framework: When to create skill vs subagent (2-4 decisions → skill, 5+ decisions → subagent)
- [ ] T114 [L10] Write hands-on exercise: Identify 5+ decision points in production Dockerfile creation
- [ ] T115 [L10] Write hands-on exercise: Define skill persona ("Think like a DevOps engineer optimizing for...")
- [ ] T116 [L10] Write hands-on exercise: Write skill questions (analysis questions that force context-specific reasoning)
- [ ] T117 [L10] Write hands-on exercise: Articulate skill principles (DHI preference, non-root default, layer caching, UV, health checks)
- [ ] T118 [L10] Write hands-on exercise: Create skill file structure at `.claude/skills/production-dockerfile/SKILL.md`
- [ ] T119 [L10] Write hands-on exercise: Test skill invocation with sample project
- [ ] T120 [L10] Write hands-on exercise: Iterate on skill based on output quality
- [ ] T121 [L10] Create `assets/lesson-10/production-dockerfile-skill.md` reference implementation
- [ ] T122 [L10] Write "Try With AI" section: Use skill to containerize a NEW project (not the sample agent)
- [ ] T123 [L10] Write reflection: "How does this skill compound your capability across future projects?"
- [ ] T124 [L10] Write assessment criteria (skill produces <400MB images, zero critical CVEs, works on 3+ different project types)

**Skill Structure Template**:
```markdown
.claude/skills/production-dockerfile/
└── SKILL.md
    ---
    name: "production-dockerfile"
    description: "Create production-ready multi-stage Dockerfiles. Use when containerizing Python/FastAPI applications for deployment."
    version: "1.0.0"
    ---

    ## Persona
    Think like a DevOps engineer who prioritizes: security (non-root, minimal CVEs),
    efficiency (small images, fast builds), and maintainability (clear layer structure).

    ## Questions (analyze before generating)
    1. What's the application type? (FastAPI, CLI, worker, etc.)
    2. What dependencies exist? (requirements.txt, pyproject.toml, poetry)
    3. Are there large files (>100MB) that should be volume-mounted?
    4. What's the target environment? (cloud, local dev, CI)
    5. Are there security requirements? (HIPAA, SOC2, etc.)

    ## Principles
    - Base image: DHI (`dhi.io/python:3.12`) unless specific reason for alternative
    - User: Non-root (UID 1000) always
    - Dependencies: UV for speed, copy lock files before code for caching
    - Health: HEALTHCHECK instruction required
    - Size target: <400MB for typical FastAPI apps
```

**Checkpoint**: Lesson 10 complete - students have created reusable Docker skill that compounds across projects

---

## Phase 13: Polish & Cross-Cutting Concerns — [#369](https://github.com/panaversity/ai-native-software-development/issues/369)

**Purpose**: Final validation and chapter-wide improvements
**Close Issue**: `gh issue close 369` when complete

- [ ] T125 [P] Validate all lessons against constitution v6.0.1 (Three Roles invisible, no meta-commentary)
- [ ] T126 [P] Validate YAML frontmatter consistency across all lessons
- [ ] T127 [P] Validate concept counts per lesson (4-7 within B1-B2 limits)
- [ ] T128 [P] Run grep validation: `grep -i "What to notice\|AI.*teach\|AI as" *.md`
- [ ] T129 [P] Validate lesson cross-references and prerequisites
- [ ] T130 [P] Create chapter summary statistics (total concepts, total exercises, total duration)
- [ ] T131 Update chapter README with final 10-lesson list and learning outcomes

**Checkpoint**: Chapter 49 complete and validated

---

## Dependencies & Execution Order

### Phase Dependencies

- **Study (Phase 0)**: No dependencies - START HERE. Agent studies book format before writing.
- **Setup (Phase 1)**: Depends on Phase 0 - creates chapter infrastructure
- **Foundational (Phase 2)**: Depends on Phase 1 - BLOCKS all lesson writing
- **Lessons 1-10 (Phases 3-12)**: All depend on Phase 0 AND Phase 2 completion
  - Lessons can proceed in order (L1 → L2 → L3...) or in parallel by different writers
  - Recommended: Sequential for first-time implementation
- **Polish (Phase 13)**: Depends on all lessons complete

### Lesson Dependencies (Content Progression)

- **Lesson 1**: Foundation (no prerequisites)
- **Lesson 2**: Requires L1 (Docker installed)
- **Lesson 3**: Requires L2 (understands containers)
- **Lesson 4**: Requires L3 (has Dockerfile to debug)
- **Lesson 5**: Requires L4 (can operate containers)
- **Lesson 6**: Requires L5 (optimized single container)
- **Lesson 7**: Requires L6 (multi-service context)
- **Lesson 8**: Requires L7 (security foundation for AI evaluation)
- **Lesson 9**: Requires L1-L8 (integrates all techniques - Layer 4 capstone)
- **Lesson 10**: Requires L1-L9 (encodes accumulated knowledge as skill - Layer 3)

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Phase 2 completes, lessons CAN run in parallel (if multiple writers available)
- All Polish tasks marked [P] can run in parallel

---

## Implementation Strategy

### Single Author Path (Recommended)

1. Complete Phase 0: Study & Context (1-2 hours) **← START HERE**
2. Complete Phase 1: Setup (30 min)
3. Complete Phase 2: Foundational (2 hours)
4. Complete Lessons sequentially L1→L10 (25-35 hours total)
5. Complete Phase 13: Polish (2 hours)

**Total**: ~32-42 hours

### Multi-Author Path

1. **ALL authors**: Complete Phase 0 (Study) independently - each author must understand format
2. Author A: Setup + Foundational
3. Once Foundational complete:
   - Author A: Lessons 1-4
   - Author B: Lessons 5-7
   - Author C: Lessons 8-10
4. All authors: Polish phase

**Total**: ~13-17 hours per author (including study time)

---

## Success Criteria Mapping

| Success Criteria | Lesson | Task(s) |
|-----------------|--------|---------|
| SC-001: 95%+ install Docker in 30 min | L1 | T010-T018 |
| SC-002: 85%+ containerize agent in 90 min | L1-L3 | T010-T037 |
| SC-003: 80%+ debug container in 15 min | L4 | T038-T048 |
| SC-004: 80%+ achieve 60%+ size reduction | L5 | T049-T059 |
| SC-005: 75%+ write Compose first attempt | L6 | T060-T071 |
| SC-006: 90%+ reduce CVEs 90%+ | L7 | T072-T083 |
| SC-007: 70%+ generate Dockerfile via Gordon | L8 | T084-T094 |
| SC-008: 85%+ push and verify portability | L9 | T095-T108 |
| SC-009: Images average <400MB | L5, L9, L10 | T059, T108, T124 |
| SC-010: 90%+ report "just works" | L9 | T106-T108 |
| SC-011: 80%+ create reusable skill | L10 | T109-T124 |

---

## Notes

- [P] tasks = different files, no dependencies
- [Lesson] label maps task to specific lesson for traceability
- Reference format: Gemini CLI chapter `03-built-in-tools-deep-dive.md`
- Verify constitution compliance before marking chapter complete
- Teaching modality variation enforced (10 different modalities across lessons)
- Three Roles framework INVISIBLE in L8 (validate with grep)
- L10 demonstrates Layer 3 (Intelligence Design) - creating reusable skill from accumulated knowledge

---

## Task Status

**Total Tasks**: 147
**Phases**: 14 (including Phase 0: Study)
**Lessons**: 10
**Estimated Implementation Time**: 35-45 hours (single author, including domain study)

### Layer Progression

| Layer | Lessons | Purpose |
|-------|---------|---------|
| L1 (Manual Foundation) | 1-7 | Build mental models, hands-on practice |
| L2 (AI Collaboration) | 8 | Gordon workflows, Three Roles INVISIBLE |
| L4 (Spec-Driven) | 9 | Capstone: specification-first project |
| L3 (Intelligence Design) | 10 | Encode knowledge as reusable skill |

**Note**: L3 (Intelligence Design) comes AFTER L4 (Capstone) because students need the complete end-to-end experience before they can identify patterns worth encoding as reusable intelligence.

✅ **READY FOR IMPLEMENTATION**
