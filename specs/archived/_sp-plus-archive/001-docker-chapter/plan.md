# Chapter 49 Implementation Plan: Docker for AI Services

**Source Spec**: `specs/001-docker-chapter/spec.md`
**Planning Date**: 2025-12-22
**Constitution**: v6.0.1 (Reasoning-Activated, Meta-Commentary Prohibited)
**Status**: Ready for Implementation

---

## Summary

This plan structures a 9-lesson chapter teaching Docker fundamentals for AI service deployment. The chapter progresses from installation through production-ready containerization, incorporating Layer 1 (manual foundation), Layer 2 (AI collaboration), and Layer 4 (spec-driven capstone). All lessons respect B1-B2 cognitive load limits and use varied teaching modalities to maintain engagement.

---

## Chapter Identity & Context

**Part**: 7 (AI Cloud Native Development) — First Chapter
**Target Audience**: B1-B2 tier (students with working FastAPI agents from Part 6)
**Prerequisites**: Completed Parts 1-6, basic CLI familiarity
**Proficiency Tier**: B1-B2 (Intermediate to Advanced)
**Hardware Tier**: Tier 1 compatible (8GB RAM, no GPU)
**Duration**: ~450-510 minutes (7.5-8.5 hours total)

---

## Pedagogical Architecture

### Learning Arc (9 Lessons)

| # | Lesson | Layer | Duration | Concepts | Purpose |
|---|--------|-------|----------|----------|---------|
| 1 | Docker Installation & Setup | L1 | 30-45 min | 4 | **Foundation** - Verify working Docker |
| 2 | Container Fundamentals | L1 | 45-60 min | 6 | **Foundation** - Mental model |
| 3 | Writing Your First Dockerfile | L1 | 60 min | 7 | **Application** - Manual creation |
| 4 | Container Lifecycle & Debugging | L1 | 45-60 min | 6 | **Application** - Operations |
| 5 | Multi-Stage Builds & Optimization | L1→L2 | 60 min | 6 | **Application** - Optimization |
| 6 | Docker Compose for Development | L1 | 60 min | 6 | **Integration** - Multi-service |
| 7 | Security & Best Practices | L1→L2 | 60 min | 5 | **Integration** - Hardening |
| 8 | AI-Assisted Docker with Gordon | L2 | 45-60 min | 5 | **Validation** - AI collaboration |
| 9 | Capstone: Production-Ready Agent | L4 | 90 min | Integration | **Mastery** - End-to-end |

### Teaching Modality Variation

Each lesson uses a different primary teaching modality to maintain engagement and prevent convergence:

1. Guided Installation (step-by-step walkthroughs)
2. Hands-On Discovery (pull → run → inspect)
3. Hands-On Creation (write → build → test)
4. Error Analysis (break → debug → fix)
5. Iterative Optimization (measure → refactor → validate)
6. Specification-First (spec → architecture → build)
7. Audit & Remediation (scan → identify → fix)
8. AI Collaboration (prompt → evaluate → iterate)
9. Capstone Project (spec → compose → validate)

---

## Detailed Lesson Plans

### Lesson 1: Docker Installation & Setup

**Learning Objectives** (Bloom's: Remember, Understand):
- Install Docker Desktop on operating system
- Verify installation with CLI commands
- Configure resource limits
- Authenticate to Docker Hub

**Concepts** (4 total):
1. Docker Desktop architecture
2. Docker Engine and containerd
3. Resource configuration
4. Docker Hub authentication

**Teaching Modality**: Guided Installation
- Platform-specific walkthroughs (macOS, Windows WSL2, Linux)
- Verification checkpoints
- Troubleshooting common issues

**Hands-On Exercises**:
1. Install Docker Desktop for OS
2. Run `docker --version` and verify version 24.0+
3. Execute `docker run hello-world`
4. Configure Docker Desktop memory to 4GB
5. Authenticate to Docker Hub

**Assessment**: Container works, version confirmed, Docker Hub authenticated

**Prerequisites**: None (foundational)

**Outputs**: Working Docker Desktop, verified CLI access

---

### Lesson 2: Container Fundamentals

**Learning Objectives** (Bloom's: Understand, Apply):
- Explain relationship between images and containers
- Understand Docker layers and caching
- Pull and run publicly available images
- Inspect container state
- Clean up containers and images

**Concepts** (6 total):
1. Docker images (immutable snapshots)
2. Containers (running instances)
3. Layers (filesystem diffs)
4. Registries (Docker Hub)
5. Container lifecycle
6. Layer caching mechanics

**Teaching Modality**: Hands-On Discovery
- Pull nginx image
- Run container and explore with `docker ps`
- Inspect layers with `docker history`
- Clean up containers

**Hands-On Exercises**:
1. Pull image: `docker pull nginx:latest`
2. Run container: `docker run -d -p 8080:80 nginx:latest`
3. List containers: `docker ps`
4. Inspect layers: `docker history nginx:latest`
5. Stop and remove: `docker stop`, `docker rm`

**Assessment**: Student explains images vs containers, navigates Docker output correctly

**Prerequisites**: Lesson 1

**Outputs**: Mental model of Docker architecture, CLI proficiency

---

### Lesson 3: Writing Your First Dockerfile

**Learning Objectives** (Bloom's: Apply, Analyze):
- Write Dockerfile from scratch
- Select appropriate base image (DHI)
- Use core instructions (FROM, WORKDIR, COPY, RUN, CMD, EXPOSE)
- Build and test image
- Verify API functionality

**Concepts** (7 total):
1. Dockerfile structure
2. FROM instruction (base image)
3. WORKDIR instruction
4. COPY vs ADD
5. RUN instruction (layers)
6. CMD vs ENTRYPOINT
7. EXPOSE instruction

**Teaching Modality**: Hands-On Creation
- Provide FastAPI sample app
- Write Dockerfile line-by-line
- Key decision: Use DHI (`dhi.io/python:3.12`)
- Build, run, test with curl

**Hands-On Exercises**:
1. Write Dockerfile for FastAPI app
2. Build: `docker build -t my-agent:1.0 .`
3. Run: `docker run -p 8000:8000 my-agent:1.0`
4. Test API: `curl http://localhost:8000/health`
5. Verify HTTP 200 response

**Assessment**: Build succeeds, image <500MB, API responds correctly

**Prerequisites**: Lessons 1-2

**Outputs**: Working Dockerfile, built image, verified API functionality

---

### Lesson 4: Container Lifecycle & Debugging

**Learning Objectives** (Bloom's: Apply, Analyze):
- View container logs for diagnosis
- Execute commands inside containers
- Inspect container state
- Pass environment variables
- Configure port mapping
- Use restart policies

**Concepts** (6 total):
1. Container logs (`docker logs`, `-f` flag)
2. Interactive debugging (`docker exec -it /bin/sh`)
3. Container inspection (`docker inspect`)
4. Environment variables
5. Port mapping syntax
6. Restart policies

**Teaching Modality**: Error Analysis & Debugging
- Start with deliberately broken container
- Diagnose using logs and exec
- Identify root cause
- Fix by adjusting configuration

**Hands-On Exercises**:
1. Run container that fails (missing env var)
2. View logs: `docker logs <container>`
3. Exec into container: `docker exec -it <container> /bin/sh`
4. Inspect environment: `env | grep API`
5. Run with env var: `--env API_KEY=test-key`
6. Test restart policy

**Assessment**: Student identifies error from logs, fixes with env var, validates restart behavior

**Prerequisites**: Lesson 3

**Outputs**: Debugging proficiency, understanding of environment and lifecycle management

---

### Lesson 5: Multi-Stage Builds & Optimization

**Learning Objectives** (Bloom's: Apply, Analyze, Evaluate):
- Refactor Dockerfile to multi-stage structure
- Implement layer caching optimization
- Use UV package manager
- Create .dockerignore
- Measure and validate size reduction

**Concepts** (6 total):
1. Build stage vs runtime stage
2. Layer caching strategy (order matters)
3. UV package manager integration
4. .dockerignore patterns
5. Image size measurement
6. Build context optimization

**Teaching Modality**: Iterative Optimization
- Measure original size
- Refactor to multi-stage
- Apply caching optimization
- Use UV for faster installs
- Measure 60%+ reduction

**Hands-On Exercises**:
1. Measure original image size
2. Create multi-stage Dockerfile (builder + runtime)
3. Create .dockerignore file
4. Build and measure: `docker images`
5. Verify 60%+ size reduction
6. Test functionality

**Assessment**: Image <300MB, 60%+ smaller than original, functionality preserved

**Prerequisites**: Lessons 1-4

**Outputs**: Multi-stage Dockerfile, optimized image, measurement data

---

### Lesson 6: Docker Compose for Development

**Learning Objectives** (Bloom's: Apply, Analyze):
- Define multi-service architecture
- Configure networking
- Implement health checks
- Use named volumes
- Manage dependencies
- Run complete stack with one command

**Concepts** (6 total):
1. docker-compose.yml structure
2. Service definition
3. Port mapping in Compose
4. Health checks
5. Named volumes
6. Service dependencies

**Teaching Modality**: Specification-First
- Show architecture diagram
- Provide high-level spec
- Students write docker-compose.yml
- Run all services together

**Hands-On Exercises**:
1. Write docker-compose.yml (agent + Postgres + Redis)
2. Define health checks
3. Configure named volumes
4. Set up service dependencies
5. Run: `docker-compose up`
6. Verify all services healthy
7. Stop: `docker-compose down`

**Assessment**: All 3 services start, health checks pass, networking works, volumes persist

**Prerequisites**: Lessons 1-5

**Outputs**: Working docker-compose.yml, local multi-service environment

---

### Lesson 7: Security & Best Practices

**Learning Objectives** (Bloom's: Apply, Analyze, Evaluate):
- Configure non-root user execution
- Scan with Docker Scout
- Compare standard vs hardened images
- Implement secret handling
- Configure health checks

**Concepts** (5 total):
1. Non-root user (UID 1000)
2. Docker Scout CVE scanning
3. Docker Hardened Images (DHI)
4. Secret management
5. Health checks (HEALTHCHECK instruction)

**Teaching Modality**: Audit & Remediation
- Start with insecure Dockerfile
- Scan with Scout (see CVE report)
- Switch to non-root + DHI
- Rescan and verify improvement

**Hands-On Exercises**:
1. Build initial image (deliberately insecure)
2. Scan: `docker scout cves <image>`
3. Review CVE report
4. Refactor: non-root user, DHI base, health checks
5. Rebuild and rescan
6. Verify 90%+ CVE reduction
7. Verify non-root: `docker run <image> whoami`

**Assessment**: Non-root confirmed (UID 1000), CVEs reduced 90%+, health check functional

**Prerequisites**: Lessons 1-6

**Outputs**: Hardened Dockerfile, security scan report, reduced vulnerability count

---

### Lesson 8: AI-Assisted Docker with Gordon

**Learning Objectives** (Bloom's: Apply, Evaluate, Create):
- Use Gordon to generate Dockerfiles
- Debug build errors with AI
- Optimize image size through conversation
- Evaluate and refine solutions
- Understand AI collaboration in infrastructure

**Concepts** (5 total):
1. Gordon capabilities
2. Natural language prompting
3. Error debugging with AI
4. Optimization suggestions
5. Iterative refinement

**Teaching Modality**: AI Collaboration (Three Roles INVISIBLE)

**CRITICAL IMPLEMENTATION NOTE**:
This lesson demonstrates bidirectional learning through Gordon interaction. The Three Roles framework (AI as Teacher/Student/Co-Worker) is INTERNAL to your planning—it must be INVISIBLE in student-facing content.

**Teaching Approach**:
- Active prompts: "Ask Gordon...", "Tell Gordon..."
- Reflection questions: "What improved?", "What did you discover?"
- Experience bidirectional learning WITHOUT framework labels

**Hands-On Exercises**:

**Part 1: Initial Request**
- Ask Gordon: "Create Dockerfile for FastAPI with Python 3.12, UV, health checks..."
- Review output
- Reflection: What optimizations didn't you know about?

**Part 2: Critical Evaluation**
- Evaluate: Does this match my requirements?
- What assumptions did Gordon make?
- What's unnecessary?

**Part 3: Constraint Teaching**
- Tell Gordon: "We need sub-2-minute builds for CI"
- Gordon adapts Dockerfile
- Observe: How did Gordon respond to YOUR constraint?

**Part 4: Refinement Loop**
- Show Gordon a build error
- Gordon debugs and provides fix
- Apply fix, test
- Iterate if needed

**Part 5: Reflection**
- Compare final to initial version
- What improved through iteration?
- What did collaboration achieve?

**Assessment**: Gordon-generated Dockerfile works, iteration improves quality, student evaluates suggestions

**Prerequisites**: Lessons 1-7 (deep Docker understanding needed to evaluate AI suggestions)

**Outputs**: Gordon-refined Dockerfile, experience with AI collaboration

---

### Lesson 9: Capstone - Production-Ready Agent

**Learning Objectives** (Bloom's: Create, Evaluate):
- Write specification for containerization
- Compose all Lessons 1-8 techniques
- Build production-grade container
- Push to registry
- Validate portability
- Evaluate spec↔code alignment

**Concepts** (Integration across 8 lessons):
- Specification-driven approach
- End-to-end workflow
- Composition of techniques
- Production validation

**Teaching Modality**: Specification-First Project
- Write spec BEFORE implementation
- Compose techniques from Lessons 1-8
- Build, validate, push

**Project Structure**:

**Phase 1: Specification Writing** (20-30 min)
- Write spec.md answering:
  - What are we containerizing?
  - What's success?
  - What constraints?
  - What components compose this?

**Phase 2: Composition & Implementation** (40-50 min)
- Build Dockerfile incorporating:
  - Lesson 3 basics
  - Lesson 5 optimization
  - Lesson 7 security
  - Lesson 8 refinement (optional: use Gordon)

**Phase 3: Validation & Testing** (15-20 min)
1. Build success: `docker build -t agent:1.0 .`
2. Size validation: `docker images | grep agent` (<400MB)
3. Security scan: `docker scout cves agent:1.0` (zero critical)
4. Functionality: `docker run ... && curl /health` (HTTP 200)
5. Registry push: `docker push <username>/agent:1.0`
6. Portability: Pull and run on different machine

**Phase 4: Reflection** (10 min)
- How did specification guide implementation?
- Which Lessons 1-8 techniques did you use?
- How does this enable deployment?

**Hands-On Deliverables**:
1. spec.md (150-200 words, clear acceptance criteria)
2. Dockerfile (optimized, non-root, health checks)
3. .dockerignore
4. Docker image pushed to registry
5. Portability verification (screenshot of pull/run on different environment)

**Assessment**: <400MB image, zero critical CVEs, functionality verified, portability validated, spec quality

**Prerequisites**: Lessons 1-8 (all Docker fundamentals)

**Outputs**: Production-ready container image, published to registry, validated portability

---

## Cognitive Load Analysis

All lessons respect B1-B2 cognitive load limits (5-10 concepts per lesson):

- Lessons 1-2: 4-6 concepts (A2 foundation level)
- Lessons 3-7: 5-7 concepts (B1 application/integration)
- Lessons 8-9: 5+ concepts (B1-B2 validation/mastery)

**All concepts justified by spec and verified against Docker 2025 documentation.**

---

## Constitution Compliance

- [x] Layer progression: L1 (1-7) → L2 (8) → L4 (9)
- [x] Three Roles in Lesson 8: INVISIBLE (no framework labels)
- [x] Teaching modality variation: No two lessons identical
- [x] Specification primacy: Lesson 9 spec-first before code
- [x] Meta-commentary prohibition: Zero "What to notice", "AI as Teacher"
- [x] Minimal content: Only content mapping to objectives
- [x] All concepts ≤ CEFR tier limits

---

## Success Criteria (from Spec)

- [x] SC-001: 95%+ install Docker within 30 min — Lesson 1
- [x] SC-002: 85%+ containerize agent within 90 min — Lessons 1-3
- [x] SC-003: 80%+ debug container within 15 min — Lesson 4
- [x] SC-004: 80%+ achieve 60%+ size reduction — Lesson 5
- [x] SC-005: 75%+ write Compose first attempt — Lesson 6
- [x] SC-006: 90%+ reduce CVEs 90%+ — Lesson 7
- [x] SC-007: 70%+ generate Dockerfile via Gordon — Lesson 8
- [x] SC-008: 85%+ push and verify portability — Lesson 9
- [x] SC-009: Images average <400MB — Lessons 5, 9
- [x] SC-010: 90%+ report "just works" — Lesson 9

---

## Writing Instructions for Content Implementer

### Lesson Template Structure

Each lesson should follow:
```
# Lesson [X]: [Title]

## Learning Objectives
- [Bloom's verb] [measurable outcome]
...

## Key Concepts
- [Concept]: [Brief explanation]
...

## [Main Content Sections]
- **Introduction**: Why this matters
- **Content**: Teaching content (match modality)
- **Hands-On Exercises**: Numbered, testable tasks
- **Assessment**: Validation criteria

## Try With AI
[For L2+ only: Action prompts + reflection, NO framework labels]
```

### Forbidden Patterns
- ❌ Layer/Stage labels in student content
- ❌ "What to notice" meta-commentary
- ❌ "AI is teaching you" framework exposition
- ❌ "Key Takeaways" final section
- ❌ Summary sections

### Required Patterns
- ✅ Clear learning objectives (Bloom's level)
- ✅ Hands-on exercises (testable)
- ✅ Concept inventory matching plan
- ✅ Teaching modality from plan
- ✅ "Try With AI" only final section (L2+ lessons)

---

## Implementation Timeline

**Lesson Writing Sequence** (must follow dependencies):
1. Lesson 1 (2-3 hours)
2. Lesson 2 (2-3 hours)
3. Lesson 3 (2-3 hours)
4. Lesson 4 (2-3 hours)
5. Lesson 5 (2-3 hours)
6. Lesson 6 (2-3 hours)
7. Lesson 7 (2-3 hours)
8. Lesson 8 (3-4 hours — requires Three Roles framework understanding)
9. Lesson 9 (3-4 hours — requires spec-driven approach understanding)

**Total**: ~22-30 hours of content creation

---

## Plan Status

✅ **READY FOR IMPLEMENTATION**

All 9 lessons designed with:
- Clear pedagogical objectives
- Varied teaching modalities
- Proper Layer progression
- Constitutional compliance
- Hardware tier compatibility
- Success criteria mapping

Content-implementer can begin writing with confidence and clarity.
