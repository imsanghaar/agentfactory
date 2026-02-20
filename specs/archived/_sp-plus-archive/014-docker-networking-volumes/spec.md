# Feature Specification: Docker Chapter 49 Expansion

**Feature Branch**: `014-docker-networking-volumes`
**Created**: 2025-12-23
**Status**: Draft
**Input**: User description: "Chapter 49 Docker Expansion: Add 4 new lessons covering Docker Networking Fundamentals (bridge, port mapping, DNS), Container-to-Container Communication (user networks, service discovery), Volumes & Persistent Data (named volumes, bind mounts, data lifecycle), and Docker Engine Architecture (containerd, runc, OCI)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Docker Networking Fundamentals (Priority: P1)

A learner completing Chapter 49 needs to understand how containers communicate with the outside world and with each other. This foundational networking knowledge is prerequisite for multi-container AI service architectures.

**Why this priority**: Networking is the most critical missing topic—without it, students can't understand how their AI agent receives requests or connects to databases. Direct prerequisite for Compose lesson.

**Independent Test**: Student can explain bridge networks, map container ports to host ports, and understand container DNS resolution without external help.

**Acceptance Scenarios**:

1. **Given** a student who completed Lesson 5 (Multi-Stage Builds), **When** they complete this lesson, **Then** they can run a container with port mapping and access it from their host browser
2. **Given** a container running on the bridge network, **When** student inspects network configuration, **Then** they understand the IP assignment and gateway relationship
3. **Given** two containers on the same bridge network, **When** student attempts communication by container name, **Then** they understand why DNS resolution works (or doesn't) on default vs custom networks

---

### User Story 2 - Container-to-Container Communication (Priority: P2)

A learner building multi-container AI services needs to understand user-defined networks, service discovery patterns, and how containers find each other by name.

**Why this priority**: Builds directly on P1 networking fundamentals. Required before Compose lesson makes sense—students need to understand what Compose automates.

**Independent Test**: Student can create a user-defined network, attach multiple containers, and demonstrate container-to-container communication by name.

**Acceptance Scenarios**:

1. **Given** a student who completed the networking fundamentals lesson, **When** they create a user-defined bridge network, **Then** they can demonstrate DNS-based service discovery between containers
2. **Given** an AI agent container and a Redis container, **When** placed on the same user network, **Then** the agent can connect to Redis using the container name as hostname
3. **Given** containers on different networks, **When** student attempts cross-network communication, **Then** they understand network isolation behavior

---

### User Story 3 - Volumes and Persistent Data (Priority: P3)

A learner deploying AI services needs to understand how to persist data beyond container lifecycle—model files, vector databases, checkpoints, and logs.

**Why this priority**: AI services have unique persistence needs (large model files, embedding databases). This knowledge is critical before Compose (which abstracts volumes) and before Kubernetes (which has its own volume abstraction).

**Independent Test**: Student can create named volumes, bind mount directories, and demonstrate data persistence across container restarts and removals.

**Acceptance Scenarios**:

1. **Given** a container with ephemeral storage, **When** the container is removed and recreated, **Then** student understands data loss behavior
2. **Given** a named volume mounted to a container, **When** the container is removed and a new container mounts the same volume, **Then** data persists
3. **Given** a bind mount from host to container, **When** files are modified on either side, **Then** changes reflect immediately on both sides
4. **Given** an AI service with model files, **When** student designs the volume strategy, **Then** they can articulate why named volumes vs bind mounts for different use cases

---

### User Story 4 - Docker Engine Architecture (Priority: P4)

A learner who will debug production container issues needs to understand the Docker runtime stack—Docker daemon, containerd, runc, and OCI specifications.

**Why this priority**: Lower priority than networking/volumes because it's more conceptual. However, understanding the runtime stack helps debug "container won't start" issues and understand security boundaries.

**Independent Test**: Student can explain the relationship between Docker CLI, dockerd, containerd, and runc, and can identify which component handles which responsibility.

**Acceptance Scenarios**:

1. **Given** a student running Docker commands, **When** they trace the execution path, **Then** they can explain CLI → daemon → containerd → runc flow
2. **Given** a container that fails to start, **When** student investigates, **Then** they know which component's logs to check
3. **Given** OCI specification discussion, **When** student encounters alternative runtimes (gVisor, Kata), **Then** they understand how OCI enables runtime portability

---

### Edge Cases

- What happens when two containers try to map the same host port? (Port conflict error)
- How does networking behave on Docker Desktop vs native Linux? (VM abstraction differences)
- What happens when a volume runs out of space? (Write failures, container health impact)
- How do volumes interact with multi-stage builds? (They don't—volumes are runtime, not build-time)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Lesson 6 (Networking Fundamentals) MUST cover bridge networks, port mapping syntax, and container DNS
- **FR-002**: Lesson 6 MUST include hands-on exercises demonstrating port mapping and network inspection
- **FR-003**: Lesson 7 (Container Communication) MUST cover user-defined networks and service discovery
- **FR-004**: Lesson 7 MUST demonstrate container-to-container communication by name
- **FR-005**: Lesson 8 (Volumes) MUST cover named volumes, bind mounts, and tmpfs
- **FR-006**: Lesson 8 MUST address AI-specific persistence patterns (model files, vector DBs)
- **FR-007**: Lesson 9 (Engine Architecture) MUST explain Docker daemon, containerd, runc, and OCI
- **FR-008**: All 4 lessons MUST follow L1 (Manual Foundation) teaching approach—no AI collaboration yet
- **FR-009**: All lessons MUST include "Try It Yourself" exercises before "Try With AI" sections
- **FR-010**: Lessons MUST shift existing lessons 6-10 to become 10-14, maintaining existing content

### Key Entities

- **Bridge Network**: Default Docker network connecting containers to host
- **User-Defined Network**: Custom network with DNS-based service discovery
- **Named Volume**: Docker-managed persistent storage with lifecycle management
- **Bind Mount**: Host directory mounted directly into container
- **OCI Runtime**: Container runtime specification (runc is reference implementation)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can expose a containerized service on a specific host port and access it externally
- **SC-002**: Students can create a user-defined network and demonstrate container name resolution
- **SC-003**: Students can persist data across container lifecycle using named volumes
- **SC-004**: Students can explain the 4-layer Docker runtime architecture (CLI → daemon → containerd → runc)
- **SC-005**: Chapter structure expands cleanly from 10 to 14 lessons with logical progression intact
- **SC-006**: All new lessons pass constitutional validation (framework invisible, evidence present, proper endings)

## Lesson Structure

### New Lessons (Insert after Lesson 5, before current Lesson 6)

| New Position | Title | Duration | Key Concepts |
|--------------|-------|----------|--------------|
| Lesson 6 | Docker Networking Fundamentals | 30 min | Bridge network, port mapping (-p), container DNS, network drivers |
| Lesson 7 | Container-to-Container Communication | 30 min | User-defined networks, service discovery, network isolation |
| Lesson 8 | Volumes and Persistent Data | 35 min | Named volumes, bind mounts, tmpfs, AI model storage patterns |
| Lesson 9 | Docker Engine Architecture | 25 min | Docker daemon, containerd, runc, OCI specs, runtime stack |

### Shifted Lessons

| Old Position | New Position | Title |
|--------------|--------------|-------|
| Lesson 6 | Lesson 10 | Docker Compose for Development |
| Lesson 7 | Lesson 11 | Security & Best Practices |
| Lesson 8 | Lesson 12 | AI-Assisted Docker with Gordon |
| Lesson 9 | Lesson 13 | Capstone: Production-Ready Agent |
| Lesson 10 | Lesson 14 | Building the Production Dockerfile Skill |

## Prerequisites

- Lessons 1-5 of Chapter 49 (Installation, Fundamentals, Dockerfile, Debugging, Multi-Stage)
- No external prerequisites beyond existing Chapter 49 foundation

## Constitutional Alignment

- **Layer**: All 4 new lessons are L1 (Manual Foundation)
- **Framework Invisibility**: No pedagogical meta-commentary
- **Evidence**: All code examples include expected output
- **Endings**: Each lesson ends with "Try With AI" section only
- **Proficiency**: B1 (7-10 concepts, moderate scaffolding)
