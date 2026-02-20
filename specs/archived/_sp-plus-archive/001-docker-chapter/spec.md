# Feature Specification: Chapter 49 - Docker for AI Services

**Feature Branch**: `001-docker-chapter`
**Created**: 2025-12-22
**Updated**: 2025-12-22 (Revised to 9-lesson structure based on learning sciences feedback)
**Status**: Draft
**Input**: Design Docker Chapter. This is first chapter of Part 7 (AI Cloud Native Development).

---

## Pedagogical Decision: No Separate Cloud Introduction Chapter

**Question**: Should there be an introductory chapter before Docker to explain cloud and containers?

**Decision**: **No**. Start directly with Docker (Chapter 49).

**Reasoning (Learning Sciences)**:

1. **Concrete-first principle**: Students have a working FastAPI agent from Part 6. Containerizing it is concrete, immediately applicable, and solves a real problem ("works on my machine" → "works everywhere").

2. **Learning psychology**: Abstract cloud concepts (regions, availability zones, IaaS/PaaS/SaaS taxonomy) are meaningless without concrete context. Students can't reason about "cloud portability" until they've experienced the pain of "this doesn't run on my teammate's machine."

3. **Motivation alignment**: Students coming from Part 6 have the question "How do I deploy my agent?" Docker answers this directly. A cloud theory chapter would delay value delivery without improving comprehension.

4. **Progressive disclosure**: Students learn cloud concepts **in context** through the chapter progression:
   - Chapter 49 (Docker): Portability, reproducibility, infrastructure-as-code
   - Chapter 50 (Kubernetes): Orchestration, scaling, self-healing
   - Chapter 59 (Infrastructure-as-Code): Terraform, provisioning, multi-cloud patterns

**Implementation**: Chapter 49 Lesson 2 (Container Fundamentals) includes a 5-minute "Why Containers? Why Cloud?" section that introduces cloud concepts in the context of Docker's value proposition, not as abstract theory.

---

## Revised Lesson Structure (10 Lessons)

**Rationale for Revision**: Original 8-lesson structure had a cognitive gap between "Writing Your First Dockerfile" and "Multi-Stage Builds." Students need to:
1. Install and verify Docker before learning concepts
2. Understand and operate containers before optimizing them
3. Debug containers before applying advanced patterns
4. **NEW**: Encode accumulated knowledge as reusable intelligence (Layer 3)

**Learning Progression Logic**:
```
Install → Understand → Create → Operate → Optimize → Compose → Secure → AI-Assist → Capstone → Skill
   1          2           3         4          5          6         7          8          9        10
```

| # | Lesson Title | What Students Do | Why This Order | Layer |
|---|--------------|------------------|----------------|-------|
| 1 | Docker Installation & Setup | Install Docker Desktop, verify with `docker --version`, run `hello-world`, configure resources | Can't learn Docker without Docker installed | L1 |
| 2 | Container Fundamentals | Pull images, run containers, explore layers, inspect filesystems, understand images vs containers | Mental model before writing | L1 |
| 3 | Writing Your First Dockerfile | Write simple Dockerfile for FastAPI hello-world, build, run, verify API responds | First hands-on creation | L1 |
| 4 | Container Lifecycle & Debugging | `docker logs`, `docker exec`, `docker ps`, environment variables, port mapping, restart policies | Learn to operate before optimizing | L1 |
| 5 | Multi-Stage Builds & Optimization | Refactor to multi-stage, layer caching, size reduction, UV for fast installs, volume mounts for large files | Now optimization makes sense | L1 |
| 6 | Docker Compose for Development | Multi-service setup (agent + Postgres + Redis), networking, volumes, health checks | Local dev environment | L1 |
| 7 | Security & Best Practices | Non-root user, DHI base images, Docker Scout scanning, secrets handling | Production readiness | L1→L2 |
| 8 | AI-Assisted Docker with Gordon | Generate Dockerfiles, debug errors, optimize via natural language (requires Docker Desktop 4.55+) | AI collaboration (Three Roles INVISIBLE) | L2 |
| 9 | Capstone: Production-Ready Agent | Full containerization of Part 6 agent, push to registry, verify portability | Integration & validation | L4 |
| 10 | Building the Production Dockerfile Skill | Create reusable skill encoding Docker expertise using Persona+Questions+Principles pattern | From knowledge to intelligence | L3 |

**Why L3 (Skill) comes after L4 (Capstone)**: Students need complete end-to-end experience before they can identify patterns worth encoding as reusable intelligence. The capstone validates their knowledge; the skill crystallizes it for future reuse.

---

## User Scenarios & Testing

### User Story 0 - Install and Verify Docker Environment (Priority: P0)

Riley is starting Chapter 49 with no Docker experience. They need to install Docker Desktop, verify it's running correctly, and understand the basic Docker environment before learning container concepts. They've never used containers before and need guided setup.

**Why this priority**: Foundation for everything. Without a working Docker installation, no other lessons are possible. This is the "hello world" moment.

**Independent Test**: Student installs Docker Desktop, runs `docker --version`, executes `docker run hello-world`, and sees the welcome message confirming Docker works.

**Acceptance Scenarios**:

1. **Given** a fresh machine (Mac, Windows, or Linux), **When** student follows installation guide for their OS, **Then** Docker Desktop installs without errors and starts successfully.

2. **Given** Docker Desktop is running, **When** student runs `docker --version` in terminal, **Then** version 24.0+ (or Engine v29+) is displayed.

3. **Given** Docker is installed, **When** student runs `docker run hello-world`, **Then** Docker pulls the image and displays "Hello from Docker!" message.

4. **Given** limited system resources, **When** student configures Docker Desktop memory to 4GB, **Then** settings persist and Docker restarts with new limits.

---

### User Story 1 - Containerize Existing Agent for Deployment (Priority: P1)

Alex has built a working FastAPI agent during Part 6 that runs perfectly on their laptop (Python 3.12, M1 Mac). They want to deploy it to a cloud server (Linux x86_64, different Python version) but hit dependency conflicts, path issues, and "it works on my machine" syndrome. They need to package the agent as a portable container that runs identically everywhere.

**Why this priority**: Core value proposition of Docker. This is the fundamental problem Chapter 49 solves. Without mastering this, subsequent cloud-native chapters (Kubernetes, CI/CD) are impossible.

**Independent Test**: Student can write a Dockerfile that builds successfully, runs the containerized agent locally with `docker run`, and verifies API endpoints respond correctly. The container must work on a different machine/OS without modification.

**Acceptance Scenarios**:

1. **Given** a FastAPI agent with dependencies listed in `pyproject.toml`, **When** student writes a Dockerfile and runs `docker build`, **Then** build succeeds without errors and produces an image under 500MB.

2. **Given** a built container image, **When** student runs `docker run -p 8000:8000 agent-image`, **Then** the agent starts successfully and responds to `curl http://localhost:8000/health` with HTTP 200.

3. **Given** the container runs on student's machine (e.g., Mac M1), **When** a teammate pulls the image and runs it on a different OS (e.g., Linux x86_64), **Then** the agent behaves identically without dependency or path issues.

4. **Given** the agent depends on environment variables (API keys, database URLs), **When** student runs `docker run --env-file .env agent-image`, **Then** the agent reads configuration correctly without hardcoded secrets.

---

### User Story 1.5 - Debug and Operate Running Containers (Priority: P1)

Jordan has a running container but something is wrong—the API returns 500 errors. They need to inspect logs, execute commands inside the container, check environment variables, and understand container state to diagnose the issue.

**Why this priority**: Debugging is essential before optimization. Students who can't troubleshoot containers will be blocked at every subsequent step. This bridges "it runs" to "I understand why it runs."

**Independent Test**: Student can view container logs, exec into a running container, inspect environment variables, and identify why their container is failing.

**Acceptance Scenarios**:

1. **Given** a running container with errors, **When** student runs `docker logs <container>`, **Then** error messages are visible and help identify the issue.

2. **Given** a running container, **When** student runs `docker exec -it <container> /bin/sh`, **Then** they get a shell inside the container and can inspect the filesystem.

3. **Given** a container started with `--env API_KEY=test`, **When** student runs `docker exec <container> env`, **Then** they see `API_KEY=test` in the output.

4. **Given** a container that keeps restarting, **When** student runs `docker ps -a` and `docker inspect <container>`, **Then** they can see exit codes and restart history to diagnose the issue.

---

### User Story 2 - Optimize Image Size and Build Speed (Priority: P2)

Sam's initial Dockerfile works but produces a 2GB image that takes 10 minutes to build and 5 minutes to pull from a registry. They need to apply multi-stage builds, layer caching, and dependency optimization to reduce image size to <300MB and build time to <2 minutes.

**Why this priority**: Production viability. Large images waste bandwidth (slow deployments), storage (costly), and developer time (slow iteration). This is the difference between "it works" and "it ships to production."

**Independent Test**: Student refactors their Dockerfile using multi-stage builds and layer caching strategies. They measure before/after image size (`docker images`) and build time (`time docker build`). Success = image size reduced by 60%+ and build time reduced by 50%+.

**Acceptance Scenarios**:

1. **Given** a naive Dockerfile with all build tools in the final image, **When** student applies multi-stage builds (build stage + runtime stage), **Then** final image size is <40% of original size.

2. **Given** a Dockerfile that reinstalls dependencies on every code change, **When** student reorders COPY commands to leverage layer caching (dependencies before code), **Then** rebuilds after code changes complete in <30 seconds (vs 5+ minutes).

3. **Given** a Dockerfile using `python:3.12` base image (1GB), **When** student switches to Docker Hardened Image `dhi.io/python:3.12` or slim variant, **Then** base layer size is <200MB.

4. **Given** a Python project with 50+ dependencies, **When** student uses `uv` for faster installs in Dockerfile, **Then** dependency installation time is <50% of `pip install`.

---

### User Story 3 - Multi-Container Local Development (Priority: P2)

Taylor's agent needs PostgreSQL (database), Redis (caching), and a vector database (Qdrant) running locally for development. Starting these manually with `brew install postgres && redis-server` is fragile and inconsistent across teammates. They need Docker Compose to define and run all services together with one command.

**Why this priority**: Development environment consistency. This is the bridge between "single container" (P1-P2) and "production orchestration" (Kubernetes in Chapter 50). Docker Compose is essential for local multi-service testing.

**Independent Test**: Student writes `docker-compose.yml` defining 4 services (agent, Postgres, Redis, Qdrant), runs `docker-compose up`, and verifies all services start and connect correctly. Stopping with `docker-compose down` cleans up all containers.

**Acceptance Scenarios**:

1. **Given** a `docker-compose.yml` with services defined, **When** student runs `docker-compose up`, **Then** all 4 services (agent, Postgres, Redis, Qdrant) start successfully and logs show "ready" messages from each.

2. **Given** the agent service depends on Postgres, **When** Docker Compose starts services, **Then** agent waits for Postgres to be ready (using `depends_on` with healthcheck) before starting.

3. **Given** services need persistent data (Postgres database), **When** student runs `docker-compose down && docker-compose up`, **Then** data persists across container restarts (using named volumes).

4. **Given** multiple teammates run the same `docker-compose.yml`, **When** each runs `docker-compose up`, **Then** all experience identical service behavior regardless of host OS or installed software.

---

### User Story 4 - Secure Container with Best Practices (Priority: P2)

Casey's Dockerfile runs the agent as root user, includes development tools in production image, and has 47 critical CVEs flagged by their security scanner. They need to apply security best practices: non-root user, minimal base image (distroless or Alpine), vulnerability scanning with Docker Scout, and secret management.

**Why this priority**: Security is non-negotiable for production deployment. Root containers violate least-privilege principle. Vulnerable dependencies expose attack surface. This story bridges "it works" to "it's production-ready."

**Independent Test**: Student refactors Dockerfile to run as non-root user, uses hardened base image (`dhi.io/python:3.12`), scans with `docker scout cves <image>`, and verifies zero critical/high vulnerabilities. Secret handling uses environment variables, not hardcoded values.

**Acceptance Scenarios**:

1. **Given** a Dockerfile running as root, **When** student adds `USER nonroot` instruction, **Then** container runs with UID 1000 (verified with `docker exec <container> whoami`).

2. **Given** a base image with vulnerabilities, **When** student switches to Docker Hardened Image (`dhi.io/python:3.12`), **Then** `docker scout cves` shows 90%+ reduction in CVEs compared to `python:3.12`.

3. **Given** secrets needed at runtime (API keys), **When** student uses `docker run --env API_KEY=secret`, **Then** secrets are not hardcoded in Dockerfile or committed to version control.

4. **Given** a production-bound image, **When** student runs `docker scout quickview <image>`, **Then** report shows zero critical vulnerabilities and confirms SLSA Level 3 provenance (for DHI images).

---

### User Story 5 - AI-Assisted Docker Workflows with Gordon (Priority: P3)

Morgan is new to Docker and finds Dockerfile syntax confusing (COPY vs ADD, CMD vs ENTRYPOINT). They want to use Gordon (Docker's AI assistant) to generate Dockerfiles, debug build errors, and optimize configurations through natural language prompts instead of memorizing syntax.

**Why this priority**: Aligns with book's AI-native philosophy (Layer 2: AI Collaboration). Gordon lowers the learning curve and accelerates common tasks. This demonstrates AI-assisted infrastructure workflows.

**Independent Test**: Student uses Gordon to generate a Dockerfile from a prompt ("Create Dockerfile for FastAPI app with Python 3.12 and UV"), debugs a build error by pasting error message to Gordon, and optimizes an existing Dockerfile by asking "How can I reduce image size?"

**Acceptance Scenarios**:

1. **Given** a FastAPI project without a Dockerfile, **When** student prompts Gordon "Create Dockerfile for FastAPI with UV, Python 3.12, and health checks", **Then** Gordon generates a working multi-stage Dockerfile that builds successfully.

2. **Given** a Dockerfile build error (`ERROR: failed to solve: process "/bin/sh -c uv install" did not complete`), **When** student pastes error to Gordon with context, **Then** Gordon identifies the issue (missing UV installation) and provides corrected Dockerfile.

3. **Given** an existing Dockerfile with 800MB image, **When** student asks Gordon "How can I reduce this image size?", **Then** Gordon suggests multi-stage builds, Alpine base, and layer reordering with explanations.

4. **Given** student wants to understand Dockerfile best practices, **When** student asks Gordon "What's wrong with this Dockerfile?" and pastes naive version, **Then** Gordon critiques security issues (root user), inefficiencies (cache busting), and suggests improvements.

---

### User Story 6 - Push Image to Registry for Team/CI Use (Priority: P3)

Riley has a working container image locally but needs to share it with teammates and deploy it to staging via CI/CD. They need to push the image to Docker Hub (or GitHub Container Registry) with proper tagging (semantic versioning, latest tag) and pull it from another machine.

**Why this priority**: Enables team collaboration and CI/CD pipelines. This is the final step before Kubernetes deployment (Chapter 50). Registries are essential infrastructure for production workflows.

**Independent Test**: Student tags their image with version (`myagent:1.0.0`) and `latest`, pushes to Docker Hub with `docker push`, and verifies a teammate (or CI job) can pull and run the image with `docker pull` and `docker run`.

**Acceptance Scenarios**:

1. **Given** a locally built image, **When** student tags it with `docker tag myagent:local username/myagent:1.0.0`, **Then** both tags reference the same image ID (verified with `docker images`).

2. **Given** a tagged image and Docker Hub credentials, **When** student runs `docker push username/myagent:1.0.0`, **Then** push succeeds and image appears in Docker Hub repository.

3. **Given** an image pushed to registry, **When** a teammate on a different machine runs `docker pull username/myagent:1.0.0 && docker run username/myagent:1.0.0`, **Then** container runs identically to local version.

4. **Given** a CI pipeline (GitHub Actions), **When** pipeline builds image and pushes with tag `username/myagent:sha-abc123`, **Then** subsequent deployment stage pulls and deploys the exact image built in CI.

---

### User Story 7 - Create Reusable Docker Skill (Priority: P3)

Riley has completed the Docker chapter and realizes they'll containerize many more projects in the future. Rather than relying on memory each time, they want to encode their Docker expertise as a reusable skill that can be invoked by AI agents. The skill should apply all best practices learned (DHI, non-root, multi-stage, UV, health checks) consistently across different project types.

**Why this priority**: This is the paradigm shift from "reusable code" to "reusable intelligence." Students learn that in the agentic era, skills compound capability across ALL future projects, not just Docker projects. This is Layer 3 (Intelligence Design) of the 4-Layer Teaching Method.

**Independent Test**: Student creates a skill file at `.claude/skills/production-dockerfile/SKILL.md` using Persona+Questions+Principles pattern, invokes it on a NEW project (not the sample agent), and verifies the generated Dockerfile meets all quality criteria (<400MB, zero critical CVEs, non-root, health check).

**Acceptance Scenarios**:

1. **Given** completion of Lessons 1-9, **When** student identifies 5+ decision points in production Dockerfile creation, **Then** they can articulate why each decision matters and when alternatives apply.

2. **Given** the Persona+Questions+Principles pattern, **When** student writes a skill file with appropriate persona ("Think like a DevOps engineer..."), analysis questions, and principles, **Then** the skill activates reasoning mode in AI (not prediction mode).

3. **Given** a completed skill file, **When** student invokes the skill on a Python CLI project (different from FastAPI sample), **Then** the generated Dockerfile follows all encoded principles (DHI, non-root, UV, HEALTHCHECK).

4. **Given** a skill-generated Dockerfile, **When** student builds and scans the image, **Then** image is <400MB with zero critical CVEs, validating skill effectiveness.

---

### Edge Cases

- **Large model files (5GB+)**: What happens when Dockerfile copies a 5GB model file? (Build context size limits, .dockerignore usage, volume mounts for models)

- **Platform mismatch (M1 Mac → x86_64 server)**: What happens when image built on M1 Mac (`arm64`) is deployed to x86_64 server? (Multi-platform builds with `docker buildx`, platform-specific base images)

- **Dependency conflicts (Python version mismatch)**: What happens when project requires Python 3.12 but base image uses 3.11? (Explicit base image version pinning, virtual environment isolation)

- **Network isolation (agent can't reach internet during build)**: What happens when `RUN pip install` fails due to firewall blocking PyPI? (Offline builds, package mirrors, vendored dependencies)

- **Permission errors (non-root user can't write to /app)**: What happens when non-root user tries to write logs to `/app/logs`? (Correct directory permissions with `RUN chown`, volume mounts)

- **Ephemeral container filesystem (data loss on restart)**: What happens when agent writes state to container filesystem and container restarts? (Volumes for persistence, stateless design patterns)

- **Build cache invalidation (rebuilds everything on minor change)**: What happens when Dockerfile COPY order causes cache invalidation on every code change? (Layer ordering optimization, .dockerignore patterns)

- **Container won't start (silent exit)**: What happens when container exits immediately with no logs? (Missing CMD, incorrect entrypoint, segfault - use `docker logs` and `docker inspect`)

---

## Requirements

### Functional Requirements

#### Installation and Setup (Lesson 1)

- **FR-001**: Student MUST be able to install Docker Desktop on their operating system (macOS, Windows with WSL2, or Linux) following platform-specific instructions.

- **FR-002**: Student MUST be able to verify Docker installation by running `docker --version` and confirming version 24.0+ or Engine v29+.

- **FR-003**: Student MUST be able to run `docker run hello-world` and see the confirmation message that Docker is working correctly.

- **FR-004**: Student MUST be able to configure Docker Desktop resource limits (memory, CPU, disk) appropriate for their machine.

- **FR-005**: Student MUST be able to authenticate to Docker Hub with `docker login` using their Docker ID.

#### Container Fundamentals (Lesson 2)

- **FR-006**: Student MUST be able to pull images from Docker Hub using `docker pull <image>:<tag>` and verify with `docker images`.

- **FR-007**: Student MUST be able to run a container from an image with `docker run` and understand the relationship between images and containers.

- **FR-008**: Student MUST be able to explain the concept of layers and how Docker caches them for efficiency.

- **FR-009**: Student MUST be able to list running containers with `docker ps` and all containers with `docker ps -a`.

- **FR-010**: Student MUST be able to stop and remove containers with `docker stop` and `docker rm`.

#### Dockerfile Creation and Build (Lesson 3)

- **FR-011**: Student MUST be able to write a Dockerfile that uses Docker Hardened Images (`dhi.io/python:3.12`) as base image and successfully builds a FastAPI agent container.

- **FR-012**: Student MUST be able to use core Dockerfile instructions: FROM, WORKDIR, COPY, RUN, CMD, and EXPOSE.

- **FR-013**: Student MUST be able to build Docker image with `docker build -t <name>:<tag> .` and verify successful build with `docker images`.

- **FR-014**: Student MUST be able to run containerized agent with `docker run -p 8000:8000 <image>` and verify API responds to requests.

#### Container Lifecycle & Debugging (Lesson 4)

- **FR-015**: Student MUST be able to view container logs with `docker logs <container>` and stream live logs with `docker logs -f <container>`.

- **FR-016**: Student MUST be able to execute commands inside running container with `docker exec -it <container> /bin/sh` for debugging.

- **FR-017**: Student MUST be able to inspect container details with `docker inspect <container>` to see configuration, network, and state.

- **FR-018**: Student MUST be able to pass environment variables to containers with `--env` and `--env-file` flags.

- **FR-019**: Student MUST be able to configure port mapping with `-p host:container` syntax and understand networking basics.

- **FR-020**: Student MUST be able to use restart policies (`--restart=unless-stopped`) for container resilience.

#### Multi-Stage Builds & Optimization (Lesson 5)

- **FR-021**: Student MUST be able to implement multi-stage Dockerfile with separate build stage (contains build tools, UV, compilation) and runtime stage (minimal runtime dependencies only).

- **FR-022**: Student MUST be able to use layer caching optimization by ordering Dockerfile instructions from least-frequently-changed (dependencies) to most-frequently-changed (application code).

- **FR-023**: Student MUST be able to install Python dependencies using UV package manager in Dockerfile for faster builds compared to pip.

- **FR-024**: Student MUST be able to create `.dockerignore` file to exclude unnecessary files (`.git`, `__pycache__`, `*.pyc`, `.env`) from build context.

- **FR-025**: Student MUST be able to handle large AI model files (>1GB) using volume mounts or external storage rather than copying into image layers.

#### Docker Compose for Development (Lesson 6)

- **FR-026**: Student MUST be able to write `docker-compose.yml` defining multiple services (agent, Postgres, Redis) with correct service dependencies and networking.

- **FR-027**: Student MUST be able to configure service health checks in Docker Compose to ensure dependent services wait for readiness before starting.

- **FR-028**: Student MUST be able to use named volumes in Docker Compose for persistent data storage (Postgres data directory).

- **FR-029**: Student MUST be able to start all services with `docker-compose up`, stop with `docker-compose down`, and verify logs with `docker-compose logs`.

- **FR-030**: Student MUST be able to configure inter-service networking so containers can communicate via service names (e.g., `postgres:5432`).

#### Security and Best Practices (Lesson 7)

- **FR-031**: Student MUST be able to configure Dockerfile to run application as non-root user (UID 1000) with `USER` instruction.

- **FR-032**: Student MUST be able to scan container image for vulnerabilities using `docker scout cves <image>` and interpret CVE report (critical/high/medium severity).

- **FR-033**: Student MUST be able to compare vulnerability counts between standard base images (`python:3.12`) and Docker Hardened Images (`dhi.io/python:3.12`) to verify 90%+ reduction.

- **FR-034**: Student MUST be able to configure secrets using environment variables passed at runtime (`--env` or `--env-file`) rather than hardcoding in Dockerfile.

- **FR-035**: Student MUST be able to configure health checks in Dockerfile using `HEALTHCHECK` instruction that validates API endpoint availability.

#### AI-Assisted Workflows (Lesson 8)

- **FR-036**: Student MUST be able to use Gordon (Docker AI assistant) to generate Dockerfile from natural language description of application requirements.

- **FR-037**: Student MUST be able to use Gordon to debug Dockerfile build errors by pasting error messages and receiving corrected Dockerfile.

- **FR-038**: Student MUST be able to use Gordon to optimize existing Dockerfile for size/performance and receive actionable recommendations.

#### Registry Operations (Lesson 9)

- **FR-039**: Student MUST be able to tag Docker image with semantic version (`myagent:1.0.0`) and `latest` tag using `docker tag`.

- **FR-040**: Student MUST be able to push image to Docker Hub (or GitHub Container Registry) with `docker push <username>/<repo>:<tag>`.

- **FR-041**: Student MUST be able to pull image from registry on different machine with `docker pull` and verify image SHA matches original.

- **FR-042**: Student MUST be able to verify container portability by running same image on different OS/architecture.

#### Intelligence Design (Lesson 10)

- **FR-043**: Student MUST be able to identify 5+ decision points in production Dockerfile creation (base image selection, package manager choice, user permissions, layer ordering, health check strategy).

- **FR-044**: Student MUST be able to create a skill file using the Persona+Questions+Principles pattern at `.claude/skills/production-dockerfile/SKILL.md`.

- **FR-045**: Student MUST be able to define a skill persona that activates reasoning mode ("Think like a DevOps engineer who prioritizes...").

- **FR-046**: Student MUST be able to write analysis questions that force context-specific reasoning (not generic "make it secure" but "what security requirements apply to THIS deployment context?").

- **FR-047**: Student MUST be able to articulate skill principles that encode Docker best practices learned in L1-L9 (DHI default, non-root mandatory, UV for dependencies, HEALTHCHECK required).

- **FR-048**: Student MUST be able to test skill invocation on a different project type (CLI app, worker, etc.) and verify output meets quality criteria.

- **FR-049**: Student MUST be able to iterate on skill based on output quality and refine questions/principles to improve results.

---

### Key Entities

- **Container Image**: Immutable filesystem snapshot containing application code, dependencies, and runtime. Built from Dockerfile. Stored in registry. Instantiated as containers.

- **Container**: Running instance of an image. Isolated process with own filesystem, network namespace, and resource limits. Ephemeral (data lost on stop unless volumes used).

- **Dockerfile**: Text file defining image build steps. Instructions executed sequentially (FROM, RUN, COPY, CMD, etc.). Each instruction creates a layer.

- **Layer**: Filesystem diff created by each Dockerfile instruction. Cached for reuse. Immutable after creation. Layers shared across images.

- **Docker Compose Configuration**: YAML file defining multi-service application. Specifies services, networks, volumes, dependencies, health checks.

- **Registry**: Storage and distribution system for Docker images. Examples: Docker Hub, GitHub Container Registry, Google Artifact Registry.

- **Volume**: Persistent data storage mechanism. Survives container restarts. Mounted into container filesystem at runtime.

- **Build Context**: Directory containing Dockerfile and files referenced by COPY/ADD. Sent to Docker daemon during build. Filtered by `.dockerignore`.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: 95%+ students can install Docker and run `hello-world` container within 30 minutes of starting Lesson 1.

- **SC-002**: 85%+ students can containerize their Part 6 FastAPI agent and successfully run it locally with correct API responses within 90 minutes of completing Lesson 3.

- **SC-003**: 80%+ students can debug a failing container using `docker logs` and `docker exec` to identify the root cause within 15 minutes.

- **SC-004**: 80%+ students can reduce initial Dockerfile image size by 60%+ through multi-stage builds and optimized base images within one iteration.

- **SC-005**: 75%+ students can write Docker Compose configuration that starts 3+ services (agent, database, cache) with correct networking and health checks on first attempt.

- **SC-006**: 90%+ students can scan their container image with Docker Scout and identify/remediate critical vulnerabilities by switching to Docker Hardened Images.

- **SC-007**: 70%+ students can use Gordon to generate a working Dockerfile from natural language prompt without manual Dockerfile writing.

- **SC-008**: 85%+ students can push their container image to a registry and successfully pull/run it on a different machine (verifying portability).

- **SC-009**: Container images produced by students average <400MB final size (measured across 50+ student submissions).

- **SC-010**: 90%+ students report that containerized agent "just works" on teammates' machines without dependency/environment issues (survey measure).

- **SC-011**: 80%+ students successfully create a reusable Docker skill file that produces <400MB images with zero critical CVEs when invoked on a different project type.

---

## Technology Context (2025 Updates)

### Docker Hardened Images (DHI) - December 2025

**Integration**: Use as recommended base images throughout chapter.

- **Registry**: `dhi.io` (not Docker Hub)
- **Example**: `dhi.io/python:3.12`, `dhi.io/python:3.12-slim`, `dhi.io/python:3.12-distroless`
- **Benefits**: Up to 95% fewer CVEs, 95% smaller images, non-root by default, SLSA Level 3 provenance
- **Variants**: Slim (minimal), Distroless (no shell/package manager), FIPS/STIG (enterprise compliance)
- **License**: Apache 2.0 (free for all use)

**Teaching Approach**: Lesson 3 (Writing First Dockerfile) introduces DHI as default choice. Lesson 7 (Security) demonstrates CVE reduction by comparing `python:3.12` vs `dhi.io/python:3.12`.

---

### Docker Scout - Real-Time Vulnerability Scanning

**Integration**: Security validation tool for Lesson 7.

- **Continuous CVE ingestion**: Not batch updates, real-time vulnerability detection
- **EPSS scoring**: Exploit Prediction Scoring System (prioritize high-EPSS CVEs)
- **Remediation guidance**: Suggests base image upgrades to fix vulnerabilities
- **Command**: `docker scout cves <image>`, `docker scout quickview <image>`

**Teaching Approach**: Lesson 7 hands-on exercise: Scan student's image, interpret report, switch to DHI base, rescan to verify reduction.

---

### Docker Bake - Declarative Build Orchestration

**Integration**: Mentioned in Lesson 5 (Multi-Stage Builds) as advanced topic.

- **GA**: February 2025
- **Config**: `docker-bake.hcl` (HCL or JSON format)
- **Features**: Parallel builds, matrix builds (multiple platforms/tags), dependency graphs
- **Command**: `docker buildx bake`

**Teaching Approach**: Brief mention in Lesson 5 ("For complex builds with multiple variants, Docker Bake automates orchestration"). Link to official docs for advanced students. Not core curriculum (Docker Compose covers multi-container, Bake is niche).

---

### Docker Engine v29 - November 2025

**Integration**: Background context, not explicit teaching.

- **containerd image store**: Default (replaces legacy graph driver)
- **API v1.44**: Minimum required (Docker v25+ client)
- **cgroup v2**: Recommended (cgroup v1 deprecated, removed 2029)
- **nftables**: Opt-in support

**Teaching Approach**: Prerequisites note in Lesson 1: "Install Docker Desktop 4.55+ or Docker Engine v29+". No deep dive into engine internals. Focus on user-facing commands.

---

### Gordon - Docker AI Assistant

**Integration**: Core feature for Lesson 8 (AI-Assisted Docker).

- **Capabilities**: Dockerfile generation, build error debugging, optimization suggestions, best practice advice
- **Access**: Docker Desktop (built-in), Docker CLI (with extension)
- **Patterns**: Natural language → Dockerfile, Error message → Fix, Audit → Recommendations

**Teaching Approach**: Lesson 8 demonstrates Three Roles framework (INVISIBLE to students):
- **AI as Teacher**: Gordon suggests multi-stage builds student didn't know about
- **AI as Student**: Student corrects Gordon's generic Dockerfile with project-specific constraints
- **AI as Co-Worker**: Iterative refinement toward optimized Dockerfile

---

## Non-Goals (What This Chapter Does NOT Teach)

### Kubernetes Orchestration
**Rationale**: Covered in Chapter 50. Docker chapter focuses on single-host container operations. Kubernetes adds orchestration, scaling, and cluster management—too much complexity for containerization fundamentals.

### CI/CD Pipeline Integration
**Rationale**: Covered in Chapter 55 (CI/CD & GitOps). This chapter teaches manual `docker build` and `docker push`. Automated builds via GitHub Actions or GitLab CI are separate concern.

### Production Monitoring and Logging
**Rationale**: Covered in Chapter 56 (Observability). This chapter shows `docker logs` for local debugging. Centralized logging (ELK, Loki), metrics (Prometheus), and tracing (Jaeger) are production ops topics.

### Multi-Architecture Builds (ARM64 + x86_64)
**Rationale**: Mentioned briefly in edge cases (M1 Mac → x86 server) with `docker buildx build --platform` command. Full cross-compilation workflows are advanced and not required for initial containerization.

### Docker Swarm or Alternative Orchestrators
**Rationale**: Docker Swarm is deprecated in favor of Kubernetes. Alternative orchestrators (Nomad, ECS) are out of scope. Chapter 50 standardizes on Kubernetes.

### Advanced Networking (Overlay Networks, Service Mesh)
**Rationale**: Chapter teaches default bridge networking and Docker Compose networks. Overlay networks (multi-host) and service mesh (Istio) are Kubernetes topics (Chapters 52, 59).

### Docker Security Deep Dive (AppArmor, Seccomp, SELinux)
**Rationale**: Chapter covers essential security (non-root user, DHI base images, secrets). Advanced Linux security modules (AppArmor profiles, Seccomp filters) are production hardening topics beyond beginner scope.

### GPU Support for AI Workloads
**Rationale**: Chapter focuses on CPU-based FastAPI agents. GPU passthrough (`docker run --gpus all`) for ML training/inference is covered in Part 8 (LLMOps).

### Dockerfile Linting and Static Analysis (Hadolint)
**Rationale**: Mentioned briefly as optional best practice. Full linter integration (CI checks, policy enforcement) is CI/CD topic (Chapter 55).

### Docker BuildKit Internals
**Rationale**: Students use BuildKit (default in v23+) without knowing internals. Deep dive into BuildKit architecture (LLB, cache backends) is unnecessary for containerization competence.

---

## Constraints

### Chapter Scope Boundaries

- **9 lessons**: Install → Fundamentals → Create → Operate → Optimize → Compose → Secure → AI-Assist → Capstone structure.
- **45-60 minutes per lesson**: Cognitive load appropriate for B1-B2 tier (5-7 concepts per lesson).
- **Prerequisites enforced**: Students MUST have completed Part 6 (working FastAPI agent). Validate in Lesson 1 setup check.

### Technical Constraints

- **Docker version**: Require Docker Desktop 4.55+ or Docker Engine v29+ (supports containerd image store, DHI, Scout).
- **Base images**: Prioritize Docker Hardened Images (`dhi.io/python:3.12`) over standard Docker Hub images.
- **Platform support**: Examples test on Linux (x86_64), macOS (M1/M2 arm64), Windows WSL2. Multi-platform builds using `docker buildx`.
- **Registry**: Default to Docker Hub (free tier sufficient). GitHub Container Registry as alternative (better CI/CD integration).

### Security Requirements

- **Non-root default**: All Dockerfiles MUST include `USER` instruction (UID 1000 or `nonroot`).
- **No hardcoded secrets**: API keys, database passwords MUST use `--env-file` or Kubernetes secrets (Chapter 50), never `ENV` in Dockerfile.
- **Vulnerability scanning**: All student images MUST pass `docker scout cves` with zero critical vulnerabilities before capstone completion.

### Educational Constraints

- **No assumed Docker knowledge**: Lesson 1 starts from installation. Lesson 2 explains "What is a container?" Foundation for students who have never used Docker.
- **Progressive complexity**: L1 (Manual foundation - write Dockerfile by hand) → L2 (AI collaboration - use Gordon) → L4 (Capstone - integrate all patterns).
- **Operate before optimize**: Students MUST demonstrate debugging skills (Lesson 4) before learning optimization (Lesson 5).
- **AI-native alignment**: Lesson 8 demonstrates AI-assisted workflows (Gordon). Earlier lessons teach manual skills to build evaluation capability.

---

## Dependencies and Assumptions

### Prerequisites (from Part 6)

- Working FastAPI agent service (OpenAI Agents SDK or equivalent)
- Python project with `pyproject.toml` or `requirements.txt`
- Basic command-line familiarity (`cd`, `ls`, environment variables)

### Software Requirements

- Docker Desktop 4.55+ (includes Docker Engine v29, Compose v2, Scout, Gordon)
- OR Docker Engine v29+ with separate Compose and Scout installations
- Git (for .dockerignore and repository context)
- Text editor or IDE (for Dockerfile editing)

### Assumptions

- **Network access**: Students can pull images from `dhi.io` and Docker Hub. Offline/airgapped environments are out of scope.
- **Hardware**: 8GB+ RAM (Docker Desktop requirement), 20GB+ disk space (for images and build cache).
- **Operating system**: Linux (native), macOS (Docker Desktop), Windows (WSL2 + Docker Desktop). Windows native containers (Windows Server) out of scope.
- **Cloud account (optional)**: Docker Hub account (free tier) for registry push. GitHub account for GitHub Container Registry alternative.

### Integration Points with Later Chapters

- **Chapter 50 (Kubernetes)**: Consumes container images produced in Chapter 49. Dockerfile health checks map to Kubernetes readiness/liveness probes.
- **Chapter 55 (CI/CD)**: Automates `docker build` and `docker push` from Chapter 49 manual workflows.
- **Chapter 56 (Observability)**: Extends `docker logs` with centralized logging (Loki), structured logging (JSON logs).
- **Chapter 59 (Infrastructure-as-Code)**: Terraform provisions container registries and build infrastructure introduced in Chapter 49.

---

## Open Questions / Needs Clarification

*No critical clarifications needed.* Specification is complete based on:
- Revised 9-lesson structure addressing learning sciences feedback
- Part 7 prerequisites (Part 6 FastAPI agents)
- 2025 Docker ecosystem updates (DHI, Scout, Bake, Engine v29)
- Constitution pedagogical frameworks (L1→L2→L4, B1-B2 tier, 5-7 concepts/lesson)
- Reference format from Gemini CLI chapter (03-built-in-tools-deep-dive.md)

**Key revision**: Added Lesson 1 (Installation) and Lesson 4 (Container Lifecycle & Debugging) to address cognitive gap between "write Dockerfile" and "optimize Dockerfile." Students must operate before they optimize.

---

## Appendix: Lesson-Level Breakdown (Revised 9 Lessons)

### Lesson 1: Docker Installation & Setup
**Layer**: L1 (Manual Foundation)
**Duration**: 30-45 minutes
**Concepts**: Docker Desktop installation, verification, resource configuration, Docker Hub authentication
**Hands-On**: Install Docker Desktop, run `docker --version`, run `docker run hello-world`, configure memory limits
**Outcome**: Student has working Docker environment ready for learning
**CEFR**: A2 | **Bloom's**: Remember, Understand

### Lesson 2: Container Fundamentals
**Layer**: L1 (Manual Foundation)
**Duration**: 45-60 minutes
**Concepts**: Images vs containers, layers, registries, pulling images, running containers, container lifecycle
**Hands-On**: Pull `nginx` image, run container, explore with `docker ps`, stop/remove containers, inspect layers
**Outcome**: Student understands Docker mental model and can explain images vs containers
**CEFR**: A2 | **Bloom's**: Understand, Apply

### Lesson 3: Writing Your First Dockerfile
**Layer**: L1 (Manual Foundation)
**Duration**: 60 minutes
**Concepts**: FROM, WORKDIR, COPY, RUN, CMD, EXPOSE, base image selection (DHI)
**Hands-On**: Write Dockerfile for simple FastAPI "hello world", build with `docker build`, run with `docker run`, test API
**Outcome**: Student can containerize basic Python app from scratch
**CEFR**: A2-B1 | **Bloom's**: Apply, Analyze

### Lesson 4: Container Lifecycle & Debugging
**Layer**: L1 (Manual Foundation)
**Duration**: 45-60 minutes
**Concepts**: Container states, logs, exec, inspect, environment variables, port mapping, restart policies
**Hands-On**: Debug a failing container using logs/exec, pass env vars, configure ports, test restart behavior
**Outcome**: Student can troubleshoot container issues and understand container operations
**CEFR**: B1 | **Bloom's**: Apply, Analyze

### Lesson 5: Multi-Stage Builds & Optimization
**Layer**: L1→L2 (Manual then AI-assisted optimization)
**Duration**: 60 minutes
**Concepts**: Build stage vs runtime stage, layer caching, .dockerignore, UV package manager, size optimization
**Hands-On**: Refactor Lesson 3 Dockerfile to multi-stage, measure size reduction, optimize cache usage
**Outcome**: Student produces images <40% size of naive Dockerfile
**CEFR**: B1 | **Bloom's**: Apply, Analyze, Evaluate

### Lesson 6: Docker Compose for Development
**Layer**: L1 (Manual Foundation)
**Duration**: 60 minutes
**Concepts**: Multi-service definition, networking, volumes, health checks, dependencies, service discovery
**Hands-On**: Write `docker-compose.yml` for agent + Postgres + Redis, test with `docker-compose up`, verify connectivity
**Outcome**: Student can run complete development stack with one command
**CEFR**: B1 | **Bloom's**: Apply, Analyze

### Lesson 7: Security & Best Practices
**Layer**: L1→L2 (Manual security + AI-assisted scanning)
**Duration**: 60 minutes
**Concepts**: Non-root user, DHI benefits, vulnerability scanning (Scout), secret handling, SLSA provenance
**Hands-On**: Refactor Dockerfile to non-root, scan with Scout, switch to DHI, rescan to verify CVE reduction
**Outcome**: Student produces images with zero critical CVEs
**CEFR**: B1-B2 | **Bloom's**: Apply, Analyze, Evaluate

### Lesson 8: AI-Assisted Docker with Gordon
**Layer**: L2 (AI Collaboration - Three Roles)
**Duration**: 45-60 minutes
**Concepts**: Natural language Dockerfile generation, error debugging, optimization prompts, AI collaboration patterns
**Hands-On**: Use Gordon to generate Dockerfile, debug build error, optimize image size via conversation
**Outcome**: Student demonstrates AI-assisted infrastructure workflows
**CEFR**: B1-B2 | **Bloom's**: Apply, Evaluate, Create

### Lesson 9: Capstone - Production-Ready Agent
**Layer**: L4 (Spec-Driven Integration)
**Duration**: 90 minutes
**Concepts**: End-to-end containerization, registry push, portability validation, production checklist
**Hands-On**: Package Part 6 agent with all optimizations, push to Docker Hub, pull and run on different machine, verify portability
**Outcome**: Production-ready container image (<400MB, zero critical CVEs, portable across environments)
**CEFR**: B2 | **Bloom's**: Create, Evaluate

---

**Specification Status**: ✅ **READY FOR PLANNING**

All mandatory sections complete. Success criteria measurable. 2025 technology updates integrated. Pedagogical layers defined. 9-lesson structure addresses learning sciences feedback (operate before optimize). No critical clarifications needed.
