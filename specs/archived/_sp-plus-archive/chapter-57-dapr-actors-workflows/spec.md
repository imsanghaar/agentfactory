# Chapter Specification: Chapter 57 - Dapr Actors & Workflows for Stateful Agents

**Part**: 7 (AI Cloud-Native Development)
**Chapter**: 59
**Created**: 2025-12-29
**Status**: Draft (Revised)
**Proficiency Level**: B1 (Intermediate)
**Prerequisites**: Chapter 53 (Dapr Core - Sidecar Building Blocks)

## Chapter Overview

This chapter provides **comprehensive coverage** of Dapr Actors and Workflows for building stateful, long-running AI agent systems. Building on the Dapr Core foundation from Chapter 53, students learn the actor model for encapsulating entity state with turn-based concurrency, and workflow orchestration for durable, fault-tolerant multi-step processes.

**Running Example**: Task API extended with TaskActor (stateful task entities) and TaskProcessingWorkflow (durable task orchestration)

**Student Skill**: `dapr-deployment` (extended from Ch53 with actors & workflows)

**Lesson Count**: 21 lessons (L00-L20) covering actors, workflows, patterns, security, and production deployment

---

## Assumed Knowledge

**What students know BEFORE this chapter** (from Ch53):
- Dapr sidecar architecture and building block concept
- Service invocation with automatic discovery and mTLS
- State management with pluggable stores (Redis)
- Pub/Sub messaging with CloudEvents
- Dapr CLI and local development workflow
- Deploying Dapr on Kubernetes with Helm
- Python SDK: `dapr-client` and `dapr-ext-fastapi`
- Task API implementation with Dapr state and pub/sub

**What this chapter must explain from scratch**:
- The Actor Model (Hewitt, 1973) - conceptual foundation
- Virtual Actors pattern (Microsoft Orleans) - Dapr's implementation
- Turn-based concurrency (single-threaded per actor)
- Actor lifecycle (activation, deactivation, garbage collection)
- Timers vs Reminders (non-persistent vs persistent scheduling)
- Workflow orchestration concepts (durable execution, replay)
- Workflow determinism requirements
- Workflow patterns (chaining, fan-out/fan-in, saga, monitor)
- Python SDK: `dapr-ext-workflow`

---

## Learning Outcomes

By the end of this chapter, students will be able to:

1. **Explain** the Actor Model and when to use actors vs. traditional state management
2. **Implement** Dapr Actors in Python using `dapr-ext-fastapi`
3. **Manage** actor state with persistence and turn-based concurrency
4. **Configure** actor timers and reminders for scheduled work
5. **Design** durable workflows using `dapr-ext-workflow`
6. **Apply** workflow patterns (chaining, fan-out/fan-in, saga, monitor)
7. **Write** deterministic workflow code following Dapr's constraints
8. **Combine** actors and workflows for complex stateful agent systems
9. **Extend** their `dapr-deployment` skill with actors and workflows patterns

---

## User Scenarios & Testing (Learner Journeys)

### Learner Journey 1 - Build Stateful Task Actor (Priority: P1)

A student learning to encapsulate task state in an actor that manages its own lifecycle, handles concurrent updates safely, and schedules deadline reminders.

**Why this priority**: Actors are the foundation for stateful agents. Understanding turn-based concurrency and state encapsulation is essential before workflows.

**Independent Test**: Student can create a TaskActor that persists state, handles method calls, and sets up reminders - all testable locally with `dapr run`.

**Acceptance Scenarios**:

1. **Given** a student with Ch53 Dapr knowledge, **When** they create a TaskActor with `dapr-ext-fastapi`, **Then** they can invoke actor methods via HTTP and see state persisted in Redis.

2. **Given** a TaskActor implementation, **When** student registers a reminder for a deadline, **Then** the reminder fires even after actor deactivation/reactivation.

3. **Given** multiple concurrent requests to the same actor, **When** student observes execution, **Then** they see turn-based (sequential) processing - no race conditions.

---

### Learner Journey 2 - Orchestrate Task Processing Workflow (Priority: P1)

A student learning to orchestrate multi-step task processing using durable workflows that survive failures and restarts.

**Why this priority**: Workflows are essential for long-running agent processes (approval flows, multi-step AI pipelines). Equal priority with actors as they serve different but complementary use cases.

**Independent Test**: Student can create a TaskProcessingWorkflow that chains activities, handles failures with retries, and can be queried for status.

**Acceptance Scenarios**:

1. **Given** a student understanding workflow concepts, **When** they implement a chained workflow with validation → assignment → completion activities, **Then** workflow executes in order and persists progress.

2. **Given** a running workflow, **When** an activity fails mid-execution, **Then** workflow automatically retries and resumes from the last checkpoint (not from scratch).

3. **Given** a workflow waiting for external input, **When** student raises an event via CLI or API, **Then** workflow receives the event and continues execution.

---

### Learner Journey 3 - Apply Advanced Workflow Patterns (Priority: P2)

A student learning to implement production workflow patterns like fan-out/fan-in for parallel processing and saga for compensation.

**Why this priority**: Production agent systems require parallel task processing and rollback capabilities. Important but builds on P1 foundations.

**Independent Test**: Student can implement a fan-out workflow that processes multiple items in parallel and aggregates results.

**Acceptance Scenarios**:

1. **Given** a list of tasks to process, **When** student implements fan-out/fan-in pattern, **Then** all tasks execute in parallel and results are aggregated.

2. **Given** a multi-step workflow with compensatable actions, **When** a later step fails, **Then** compensation activities execute in reverse order (saga pattern).

---

### Learner Journey 4 - Extend Dapr Deployment Skill (Priority: P2)

A student extending their `dapr-deployment` skill (from Ch53) with actor and workflow patterns.

**Why this priority**: Skill-First pattern - the chapter's meta-learning outcome. Students build a reusable asset.

**Independent Test**: Student's extended skill can generate TaskActor and TaskProcessingWorkflow implementations correctly.

**Acceptance Scenarios**:

1. **Given** a student's `dapr-deployment` skill from Ch53, **When** they complete L00 extending it with actor/workflow docs, **Then** the skill knows actor registration and workflow runtime patterns.

2. **Given** lessons L01-L08 completed, **When** student uses their skill to generate actor code, **Then** output includes correct decorator syntax, state manager usage, and reminder registration.

---

### Edge Cases

- What happens when an actor is invoked during garbage collection?
  - Dapr reactivates it automatically (virtual actor pattern)
- How does workflow handle non-deterministic code (e.g., `datetime.now()`)?
  - Workflow fails on replay; must use `ctx.current_utc_datetime`
- What happens when reminder fires but actor service is down?
  - Reminder is retried (up to 3 times with backoff) then stored in Scheduler
- How does workflow survive complete cluster restart?
  - State persisted in actor backend; workflow resumes from last checkpoint

---

## Requirements

### Functional Requirements (Lesson Coverage)

**L00 - Extend Your Dapr Skill**:
- **FR-001**: Students MUST extend existing `dapr-deployment` skill with actor and workflow patterns
- **FR-002**: Students MUST fetch `dapr-ext-workflow` documentation using `/fetching-library-docs`
- **FR-003**: Skill MUST include actor interface patterns and workflow runtime setup

**L01 - The Actor Model**:
- **FR-004**: Chapter MUST explain Actor Model (Hewitt, 1973) conceptually before implementation
- **FR-005**: Chapter MUST distinguish Virtual Actors (Dapr/Orleans) from traditional actors (Akka)
- **FR-006**: Chapter MUST explain turn-based concurrency with relatable analogies
- **FR-007**: Chapter MUST cover actor lifecycle: activation, deactivation, garbage collection

**L02 - Hello Actors - Your First Actor**:
- **FR-008**: Students MUST create actor interface with ABC and `@abstractmethod`
- **FR-009**: Students MUST implement actor class extending `Actor`
- **FR-010**: Students MUST register actors with FastAPI using `DaprActor`
- **FR-011**: Students MUST invoke actor methods via HTTP API

**L03 - Chat Actor - Stateful Conversations**:
- **FR-012**: Students MUST build ChatActor that maintains conversation history
- **FR-013**: Students MUST integrate actor with Dapr pub/sub for message-driven input
- **FR-014**: Chapter MUST demonstrate actor receiving messages and updating state

**L04 - Actor State Management**:
- **FR-015**: Students MUST use `_state_manager` for persistent actor state
- **FR-016**: Students MUST implement `_on_activate` and `_on_deactivate` lifecycle hooks
- **FR-017**: Chapter MUST explain turn-based concurrency guarantees for state safety
- **FR-018**: Chapter MUST show state persisting across actor deactivation/reactivation

**L05 - Timers and Reminders**:
- **FR-019**: Students MUST implement timers for lightweight, non-persistent scheduling
- **FR-020**: Students MUST implement reminders for persistent scheduling that survives restarts
- **FR-021**: Chapter MUST contrast timers vs reminders with clear decision criteria table
- **FR-022**: Students MUST handle timer/reminder callbacks in actor methods

**L06 - Actor Communication Patterns**:
- **FR-023**: Students MUST implement actor-to-actor communication via ActorProxy
- **FR-024**: Chapter MUST explain coordination patterns (parent-child, peer-to-peer)
- **FR-025**: Students MUST implement a task delegation scenario between actors

**L07 - Event-Driven Actors**:
- **FR-026**: Students MUST integrate actors with Dapr pub/sub topics
- **FR-027**: Students MUST use Dapr bindings with actors for external system integration
- **FR-028**: Chapter MUST demonstrate actors responding to external events

**L08 - Actors Observability**:
- **FR-029**: Students MUST configure tracing for actor method calls (Zipkin/Jaeger)
- **FR-030**: Students MUST view actor metrics (activation count, method duration)
- **FR-031**: Chapter MUST cover debugging strategies for actor systems

**L09 - Dapr Workflows Overview**:
- **FR-032**: Chapter MUST explain workflow concepts (durable execution, event sourcing, replay)
- **FR-033**: Students MUST understand workflow determinism requirements
- **FR-034**: Chapter MUST explain when to use workflows vs actors vs plain state
- **FR-035**: Chapter MUST cover workflow engine architecture (actor backend)

**L10 - Workflow Architecture**:
- **FR-036**: Chapter MUST explain internal workflow engine mechanics
- **FR-037**: Chapter MUST explain replay-based execution model
- **FR-038**: Chapter MUST cover state persistence and checkpointing
- **FR-039**: Students MUST understand why workflow code must be deterministic

**L11 - Authoring Workflows**:
- **FR-040**: Students MUST implement workflow function with `dapr-ext-workflow`
- **FR-041**: Students MUST implement activities as units of work
- **FR-042**: Students MUST set up WorkflowRuntime and DaprWorkflowClient
- **FR-043**: Students MUST pass data between activities and handle return values

**L12 - Managing Workflows**:
- **FR-044**: Students MUST start workflows via API and CLI
- **FR-045**: Students MUST query workflow status and history
- **FR-046**: Students MUST raise external events to workflows (`wait_for_external_event`)
- **FR-047**: Students MUST terminate and purge workflow instances

**L13 - Workflow Patterns - Chaining & Fan-Out**:
- **FR-048**: Students MUST implement task chaining pattern
- **FR-049**: Students MUST implement fan-out/fan-in pattern with `when_all`
- **FR-050**: Chapter MUST show parallel task processing with result aggregation

**L14 - Workflow Patterns - Saga & Monitor**:
- **FR-051**: Students MUST implement saga pattern with compensation activities
- **FR-052**: Students MUST implement monitor pattern with `continue_as_new`
- **FR-053**: Chapter MUST cover human interaction pattern (approval workflows)

**L15 - Combining Actors with Workflows**:
- **FR-054**: Chapter MUST provide decision framework: when to use actors vs workflows
- **FR-055**: Students MUST implement hybrid pattern: workflow orchestrating actors
- **FR-056**: Chapter MUST cover actors as workflow activity backing

**L16 - Multi-App Workflows**:
- **FR-057**: Students MUST implement cross-app activity calls with `app_id` parameter
- **FR-058**: Students MUST implement cross-app child workflow calls
- **FR-059**: Chapter MUST explain multi-app workflow restrictions (same namespace, same state store)
- **FR-060**: Chapter MUST cover error handling for unavailable target apps

**L17 - Namespaced Actors**:
- **FR-061**: Students MUST configure actors for multi-tenant deployment
- **FR-062**: Students MUST configure separate state stores per namespace (Redis DB example)
- **FR-063**: Chapter MUST explain Placement service behavior with namespaces
- **FR-064**: Chapter MUST cover namespace isolation guarantees

**L18 - Actor Security Essentials**:
- **FR-065**: Students MUST configure actor state encryption at rest
- **FR-066**: Students MUST enable mTLS for actor communication
- **FR-067**: Students MUST implement audit logging for actor method calls
- **FR-068**: Chapter MUST cover threat model for actor systems

**L19 - Capstone: Stateful Task Agent**:
- **FR-069**: Students MUST build TaskActor with state, reminders, and status management
- **FR-070**: Students MUST build TaskProcessingWorkflow orchestrating task lifecycle
- **FR-071**: Capstone MUST demonstrate actors and workflows working together
- **FR-072**: Capstone MUST run on Docker Desktop Kubernetes

**L20 - Finalize Your Dapr Skill**:
- **FR-073**: Students MUST validate their skill generates correct actor code
- **FR-074**: Students MUST validate their skill generates correct workflow code
- **FR-075**: Students MUST document their skill improvements from the chapter

### Key Entities

- **TaskActor**: Virtual actor representing a single task with state (title, status, assignee, deadlines), methods (get_task, update_status, assign), and reminders (deadline_reminder)
- **TaskProcessingWorkflow**: Durable workflow orchestrating task lifecycle (validate → assign → await_completion → notify)
- **Activity**: Unit of work in workflow (validate_task, assign_task, send_notification, etc.)
- **WorkflowRuntime**: Runtime that registers and executes workflows
- **DaprWorkflowClient**: Client for starting, querying, and managing workflow instances

---

## Lesson Structure

### Part A: Dapr Actors (L00-L08)

| Lesson | Title | Layer | Duration | Focus | Source |
|--------|-------|-------|----------|-------|--------|
| L00 | Extend Your Dapr Skill | L3 | 25 min | Skill-First: extend skill with actor/workflow docs | Skill-First |
| L01 | The Actor Model | L1 | 25 min | Conceptual foundation: Hewitt 1973, virtual actors | 01_hello_actors |
| L02 | Hello Actors - Your First Actor | L2 | 30 min | Create, deploy, invoke basic actor | 01_hello_actors |
| L03 | Chat Actor - Stateful Conversations | L2 | 35 min | Build agent with state, integrate pub/sub | 02_chat_actor |
| L04 | Actor State Management | L2 | 30 min | StateManager, lifecycle hooks, persistence | 02_chat_actor |
| L05 | Timers and Reminders | L2 | 30 min | Scheduling: non-persistent vs persistent | 04_advanced_actor_config |
| L06 | Actor Communication Patterns | L2 | 30 min | Actor-to-actor calls, coordination | 03_actors_communication |
| L07 | Event-Driven Actors | L2 | 35 min | Pub/sub integration, bindings | 06_event_driven_actors |
| L08 | Actors Observability | L2 | 25 min | Tracing, metrics, debugging | 05_actors_observability |

### Part B: Dapr Workflows (L09-L14)

| Lesson | Title | Layer | Duration | Focus | Source |
|--------|-------|-------|----------|-------|--------|
| L09 | Dapr Workflows Overview | L1 | 25 min | Durable execution, event sourcing, determinism | 01_hello_workflow |
| L10 | Workflow Architecture | L1 | 25 min | Engine internals, actor backend, replay | 02_architecture_theory |
| L11 | Authoring Workflows | L2 | 35 min | Workflow functions, activities, data passing | 03_author_workflows |
| L12 | Managing Workflows | L2 | 30 min | Start, query, events, terminate, purge via API/CLI | 04_manage_workflows |
| L13 | Workflow Patterns - Chaining & Fan-Out | L2 | 35 min | Task chaining, parallel execution with when_all | 05_patterns |
| L14 | Workflow Patterns - Saga & Monitor | L2 | 35 min | Compensation, long-running polling | 05_patterns |

### Part C: Advanced Production Patterns (L15-L18)

| Lesson | Title | Layer | Duration | Focus | Source |
|--------|-------|-------|----------|-------|--------|
| L15 | Combining Actors with Workflows | L2 | 30 min | When to use each, hybrid patterns | Integration |
| L16 | Multi-App Workflows | L2 | 30 min | Cross-app activities, child workflows | workflow-multi-app.md |
| L17 | Namespaced Actors | L2 | 25 min | Multi-tenancy, namespace isolation | namespaced-actors.md |
| L18 | Actor Security Essentials | L2 | 30 min | State encryption, mTLS, audit logging | 08_actor_security |

### Part D: Capstone & Skill (L19-L20)

| Lesson | Title | Layer | Duration | Focus | Source |
|--------|-------|-------|----------|-------|--------|
| L19 | Capstone: Stateful Task Agent | L4 | 45 min | TaskActor + TaskProcessingWorkflow | 06_ai_pizza_shop |
| L20 | Finalize Your Dapr Skill | L3 | 20 min | Skill validation and documentation | Skill-First |

**Total**: 21 lessons, ~11 hours

**Layer Key**:
- L1 (Manual): Conceptual understanding before implementation
- L2 (Collaboration): AI-assisted implementation
- L3 (Skill): Building/extending the student's skill
- L4 (Spec-Driven): Capstone with full orchestration

**Scope Notes**:
- Actor Partitioning (howto-actors-partitioning.md) → **DEPRECATED** in Dapr 1.15+, uses Scheduler by default
- DACA Actor Runtime specifics (07_daca_actor_runtime) → DACA-specific patterns, optional extension
- Protobuf Serialization → Advanced optimization, out of scope
- **NOW INCLUDED**: Multi-App Workflows, Namespaced Actors, Actor Security (comprehensive as final Dapr chapter)

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can explain the actor model and its benefits in under 2 minutes (L01 assessment)
- **SC-002**: Students can implement a working ChatActor with state persistence (L03-L04)
- **SC-003**: Students can implement timers AND reminders with correct use case selection (L05)
- **SC-004**: Students can trace actor method calls via Zipkin/Jaeger (L08)
- **SC-005**: Students can explain workflow determinism rules and identify violations (L10)
- **SC-006**: Students can implement a workflow with 3+ chained activities that survives restart (L11)
- **SC-007**: Students can implement fan-out/fan-in pattern processing 5+ items in parallel (L13)
- **SC-008**: Students can implement saga pattern with compensation (L14)
- **SC-009**: Students can decide when to use actors vs workflows for a given scenario (L15)
- **SC-010**: Students can implement cross-app workflow with activities on different services (L16)
- **SC-011**: Students can configure multi-tenant actors with namespace isolation (L17)
- **SC-012**: Students can secure actors with state encryption and mTLS (L18)
- **SC-013**: Capstone integrates actors and workflows on Docker Desktop Kubernetes (L19)
- **SC-014**: Students' extended `dapr-deployment` skill generates valid actor/workflow code (L20)

### Quality Gates

- All code examples work on Docker Desktop Kubernetes with Dapr 1.14+
- Each lesson ends with "Reflect on Your Skill" section (except L00, L19, L20)
- Python SDK versions: `dapr-ext-fastapi` for actors, `dapr-ext-workflow` for workflows
- State store: Redis (same as Ch53 for consistency)
- Total chapter duration: ~11 hours (comprehensive coverage as final Dapr chapter)

---

## Technology Stack

| Component | Technology | Version | Notes |
|-----------|------------|---------|-------|
| Runtime | Dapr | 1.14+ | Same as Ch53 |
| Actor SDK | dapr-ext-fastapi | Latest | Actor registration with FastAPI |
| Workflow SDK | dapr-ext-workflow | Latest | Workflow runtime and client |
| State Store | Redis | Any | Actor and workflow state |
| Platform | Docker Desktop Kubernetes | Latest | Consistent with Part 7 |
| Python | Python | 3.11+ | For type hints and modern syntax |

---

## Dependencies

### Chapter Dependencies
- **Ch53 (Dapr Core)**: Students must complete Ch53 first - provides Dapr fundamentals, state management, pub/sub, and the initial `dapr-deployment` skill

### Skill Dependencies
- Students have `dapr-deployment` skill from Ch53 that will be extended in L00

### Technical Dependencies
- Dapr installed on Docker Desktop Kubernetes (from Ch53)
- Redis deployed for state storage (from Ch53)
- Python 3.11+ with `dapr-client`, `dapr-ext-fastapi`, `dapr-ext-workflow`

---

## Available Reference Materials

| Resource | Path | Purpose |
|----------|------|---------|
| Dapr Docs 1.16 | `dapr-docs-1.16/` | Official documentation |
| Personal Work - Actors | `07_daca_agent_native_dev/05_agent_actors/` | Example implementations |
| Personal Work - Workflows | `07_daca_agent_native_dev/06_dapr_workflows/` | Example implementations |
| Skill Reference - Actors | `.claude/skills/building-with-dapr/references/actors.md` | Actor patterns |
| Skill Reference - Workflows | `.claude/skills/building-with-dapr/references/workflows.md` | Workflow patterns |

---

## Assumptions

1. **Dapr Environment Ready**: Students have completed Ch53 and have Dapr running on Docker Desktop Kubernetes
2. **Redis Available**: Redis is deployed and configured as state store (from Ch53)
3. **Python Proficiency**: Students can write Python with async/await patterns (B1 level)
4. **Docker/K8s Basics**: Students understand container deployment (from Ch49-51)
5. **Skill-First Pattern Familiarity**: Students understand the Skill-First approach from earlier Part 7 chapters

---

## Scope Boundaries

### In Scope
- Actor model concepts and Dapr Virtual Actors
- Actor implementation with Python SDK (`dapr-ext-fastapi`)
- Actor state management, timers, and reminders
- Actor communication patterns and event-driven actors
- Actor observability (tracing, metrics)
- **Namespaced actors for multi-tenancy** (production pattern)
- **Actor security: state encryption, mTLS, audit logging** (production essential)
- Workflow concepts and determinism rules
- Workflow implementation with Python SDK (`dapr-ext-workflow`)
- Workflow patterns: chaining, fan-out/fan-in, saga, monitor
- Workflow management (start, query, events, terminate, purge)
- **Multi-app workflows: cross-service activities and child workflows** (distributed pattern)
- Extending `dapr-deployment` skill with actors and workflows

### Out of Scope
- Actor partitioning for legacy reminders (**DEPRECATED** - Dapr 1.15+ uses Scheduler)
- Custom workflow backends (using default actor backend)
- Dapr Core building blocks review (covered in Ch53)
- Multi-language actor/workflow implementations (Python only)
- DACA-specific actor runtime patterns (optional advanced extension)
