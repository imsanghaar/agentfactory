# Chapter Specification: Chapter 53 - Dapr Core: Sidecar Building Blocks for AI Microservices

**Feature Branch**: `chapter-53-dapr-core`
**Created**: 2025-12-29
**Status**: Draft
**Part**: 7 (AI Cloud-Native Development)
**Proficiency Level**: B1 (Intermediate)
**Student Skill Name**: `dapr-deployment`

## Overview

**You will build a Dapr skill BEFORE you learn Dapr.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `dapr-deployment` skill using tools from Chapter 5. Then you spend the chapter understanding what you built and making it better. By the end, you don't just "know Dapr"—you OWN a production-ready skill.

**The Core Insight**: Dapr abstracts infrastructure from application code. You've learned Kafka directly in Chapter 52. Now you'll learn to use Dapr's pub/sub, which can talk to Kafka OR Redis OR RabbitMQ—without changing your application code. Same concept, portable implementation.

**Hands-On Approach**: Every building block lesson deploys its component with Helm/kubectl AND writes FastAPI code using async DaprClient. You already know FastAPI async patterns from Part 6—Dapr fits naturally.

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Docker: Container images, multi-stage builds, Dockerfile patterns (Ch49)
- Kubernetes: Pods, Deployments, Services, ConfigMaps, Secrets, namespaces (Ch50)
- Helm: Charts, values, templates, releases, `helm install/upgrade` (Ch51)
- Kafka concepts: Topics, partitions, producers, consumers, event-driven patterns (Ch52)
- **FastAPI: Async endpoints (`async def`), Pydantic models, lifespan events, dependency injection (Part 6)**
- Python: async/await patterns, context managers
- Skills: How to use `/fetching-library-docs` and `/skill-creator` (Ch5)

**What this chapter must explain from scratch**:
- Sidecar pattern and why Dapr uses it
- Building blocks concept (abstraction over infrastructure)
- Components and their configuration (YAML CRDs)
- Service invocation with automatic discovery
- State management without database SDKs
- Pub/Sub without broker-specific code
- Bindings for external system triggers
- Jobs API for scheduled tasks
- Secrets and configuration APIs
- Dapr annotations for Kubernetes deployment

## The Skill-First Arc

```
L00: Build Your Dapr Skill (25 min)
  │   └── Clone skills-lab, fetch docs, create `dapr-deployment` skill
  │
  ├── L01-02: Dapr Foundations
  │   └── Sidecar architecture, building blocks concept
  │
  ├── L03: Setup & First Building Block
  │   └── Helm deployment + Redis component + State Management
  │
  ├── L04-08: Core Building Blocks (each: deploy component + code)
  │   └── Service Invocation, Pub/Sub, Bindings, Jobs, Secrets/Config
  │
  └── L09-10: Production & Capstone
      └── Dapr-enabled Task API, finalize skill
```

## Lesson Breakdown

| # | Lesson | Layer | Duration | Your Skill Improves |
|---|--------|-------|----------|---------------------|
| **0** | **Build Your Dapr Skill** | L3 | 25 min | **Created from official docs** |
| 1 | The Sidecar Pattern | L1 | 20 min | Understand: why sidecars |
| 2 | Building Blocks and Components | L1 | 20 min | Understand: abstraction model |
| 3 | Deploy Dapr + State Management | L2 | 35 min | Add: Helm + state API patterns |
| 4 | Service Invocation | L2 | 25 min | Add: service-to-service calls |
| 5 | Pub/Sub Messaging | L2 | 30 min | Add: pub/sub patterns (connect to Ch52) |
| 6 | Bindings and Triggers | L2 | 25 min | Add: input/output bindings |
| 7 | Jobs API: Scheduled Tasks | L2 | 25 min | Add: job scheduling patterns |
| 8 | Secrets and Configuration | L2 | 25 min | Add: secrets/config APIs |
| 9 | Capstone: Dapr-Enabled Task API | L4 | 40 min | **Production integration** |
| **10** | **Finalize Your Dapr Skill** | L3 | 20 min | **Complete asset** |

**Total**: ~290 minutes (~5 hours)

## Layer Progression

| Layer | Lessons | Focus |
|-------|---------|-------|
| **L1: Manual/Conceptual** | 1-2 | Sidecar pattern, building blocks mental model |
| **L2: AI Collaboration** | 3-8 | Deploy Dapr + each building block with AI assistance |
| **L3: Skill Building** | 0, 10 | Create and finalize `dapr-deployment` skill |
| **L4: Spec-Driven** | 9 | Capstone: Dapr-enable the Task API from Part 6 |

## Detailed Lesson Specifications

### L00: Build Your Dapr Skill (25 min) - Layer 3

**Objective**: Create a `dapr-deployment` skill BEFORE learning Dapr concepts.

**Content**:
1. Clone the skills-lab repository
2. Write LEARNING-SPEC.md for Dapr learning goals
3. Use `/fetching-library-docs dapr` to get official documentation
4. Use `/skill-creator` to build `dapr-deployment` skill
5. Test the skill on a simple prompt

**Ends with**: Skill created at `.claude/skills/dapr-deployment/SKILL.md`

---

### L01: The Sidecar Pattern (20 min) - Layer 1

**Objective**: Understand why Dapr uses the sidecar architecture.

**Content**:
- What is a sidecar? (Ambassador pattern in Kubernetes)
- Why separate infrastructure from application code
- Dapr sidecar injection via annotations
- HTTP API on localhost:3500, gRPC on localhost:50001
- Container vs process mode (self-hosted vs Kubernetes)
- The 2/2 Ready pattern in pod status

**Vocabulary**: sidecar, daprd, sidecar-injector, app-id, app-port

**Reflect on Skill**: Does your skill explain sidecar architecture?

---

### L02: Building Blocks and Components (20 min) - Layer 1

**Objective**: Understand Dapr's abstraction model.

**Content**:
- Building blocks = APIs (state, pubsub, invoke, secrets, bindings, jobs, config)
- Components = implementations (Redis, Kafka, Kubernetes secrets)
- How swapping components changes infrastructure without code changes
- Component YAML structure (apiVersion, kind, metadata, spec)
- Scoping components to specific apps

**Vocabulary**: building block, component, pluggable, component spec, scopes

**Reflect on Skill**: Does your skill distinguish building blocks from components?

---

### L03: Deploy Dapr + State Management (35 min) - Layer 2

**Objective**: Deploy Dapr control plane AND use state management in one hands-on lesson.

**Part A: Deploy Dapr with Helm** (15 min)
- Dapr control plane components (operator, sidecar-injector, sentry, placement, scheduler)
- Installing Dapr with Helm: `helm upgrade --install dapr dapr/dapr`
- Verifying installation: `kubectl get pods -n dapr-system`
- Deploy Redis for state store: `helm install redis bitnami/redis`
- Apply state store component YAML

**Part B: State Management with Async DaprClient** (20 min)
- State API endpoints: GET/POST `/v1.0/state/{store}`
- Key-value operations: save, get, delete, bulk
- ETag for optimistic concurrency
- **Async Python SDK pattern**:
  ```python
  from dapr.clients import DaprClient

  async with DaprClient() as client:
      await client.save_state(store_name='statestore', key='task-1', value='...')
      state = await client.get_state(store_name='statestore', key='task-1')
  ```
- FastAPI integration with lifespan

**Try With AI**:
```
Deploy Dapr 1.14 on my Docker Desktop Kubernetes cluster.
Then create a FastAPI endpoint that saves a task to Dapr state store using async DaprClient.
```

**Reflect on Skill**: Does your skill include Helm deployment AND state patterns?

---

### L04: Service Invocation (25 min) - Layer 2

**Objective**: Call services via Dapr with automatic discovery and mTLS.

**Hands-On Setup**: Deploy a second service (notification-service) with Dapr annotations.

**Content**:
- Service invocation API: `/v1.0/invoke/{app-id}/method/{method}`
- Automatic service discovery via app-id annotation
- mTLS between sidecars (Sentry service)
- **Async Python SDK**:
  ```python
  async with DaprClient() as client:
      response = await client.invoke_method(
          app_id='notification-service',
          method_name='notify',
          http_verb='POST',
          data='{"message": "Task created"}'
      )
  ```
- HTTP header proxying: `dapr-app-id` header alternative
- Retries and timeouts configuration

**Try With AI**:
```
My task-api needs to call notification-service when a task is created.
Deploy both services with Dapr and show me async service invocation.
```

**Reflect on Skill**: Add service invocation patterns to your skill.

---

### L05: Pub/Sub Messaging (30 min) - Layer 2

**Objective**: Publish and subscribe to events using Dapr pub/sub.

**Hands-On Setup**: Apply Redis pub/sub component YAML (or swap to Kafka from Ch52!).

**Content**:
- Pub/Sub API: `/v1.0/publish/{pubsub}/{topic}`
- CloudEvents format (automatic wrapping)
- Declarative subscriptions (Subscription CRD)
- Programmatic subscriptions (dapr-ext-fastapi)
- **Async Python SDK**:
  ```python
  async with DaprClient() as client:
      await client.publish_event(
          pubsub_name='pubsub',
          topic_name='task-events',
          data='{"event_type": "task.created", ...}',
          data_content_type='application/json'
      )
  ```
- FastAPI extension: `@dapr_app.subscribe(pubsub='pubsub', topic='task-events')`
- **Connection to Ch52**: Same concepts, different broker—swap Redis for Kafka with one YAML change

**Try With AI**:
```
Add pub/sub to my Task API: publish task.created events using async DaprClient
and create a subscription handler using dapr-ext-fastapi.
```

**Reflect on Skill**: Add pub/sub patterns to your skill.

---

### L06: Bindings and Triggers (25 min) - Layer 2

**Objective**: Connect to external systems with input/output bindings.

**Hands-On Setup**: Apply cron binding component + HTTP output binding.

**Content**:
- Input bindings: trigger your app from external events (cron, webhooks, queues)
- Output bindings: invoke external systems (HTTP, email, storage)
- Binding component configuration with `direction` metadata
- **Async Python SDK**:
  ```python
  async with DaprClient() as client:
      await client.invoke_binding(
          binding_name='http-binding',
          operation='post',
          data='{"webhook": "triggered"}'
      )
  ```
- FastAPI endpoint for input binding: `/cron-trigger`
- Difference from pub/sub: bindings are for external systems, pub/sub is for internal messaging

**Try With AI**:
```
Create a cron binding that triggers a cleanup endpoint every 5 minutes.
Then create an HTTP output binding to call an external webhook.
Show async DaprClient usage.
```

**Reflect on Skill**: Add binding patterns to your skill.

---

### L07: Jobs API: Scheduled Tasks (25 min) - Layer 2

**Objective**: Schedule future jobs using Dapr's Jobs API.

**Content**:
- Jobs API vs Bindings: Jobs are for scheduling future work, bindings are for external triggers
- Scheduler control plane service (already deployed with Dapr)
- Creating jobs: one-time or recurring
- Jobs stored in embedded Etcd
- **Async Python SDK**:
  ```python
  async with DaprClient() as client:
      # Schedule a job for future execution
      await client.schedule_job(
          name='daily-cleanup',
          schedule='@daily',  # or cron expression
          data={'action': 'cleanup-old-tasks'}
      )
  ```
- Job handler endpoint in FastAPI
- At-least-once execution guarantee

**Try With AI**:
```
Schedule a job that runs daily at midnight to archive completed tasks.
Use the Dapr Jobs API with async DaprClient and create a FastAPI handler.
```

**Reflect on Skill**: Add job scheduling patterns to your skill.

---

### L08: Secrets and Configuration (25 min) - Layer 2

**Objective**: Access secrets and configuration through Dapr APIs.

**Hands-On Setup**: Create Kubernetes secret + apply secrets component YAML.

**Content**:
- Secrets API: `/v1.0/secrets/{store}/{key}`
- Kubernetes secrets store component (built-in, no extra install)
- **Async Python SDK**:
  ```python
  async with DaprClient() as client:
      secret = await client.get_secret(
          store_name='kubernetes-secrets',
          key='api-credentials'
      )
      api_key = secret.secret.get('api-key')
  ```
- Configuration API: `/v1.0/configuration/{store}`
- Configuration subscriptions for dynamic updates
- Referencing secrets in component YAML (secretKeyRef)

**Try With AI**:
```
Configure my Task API to get the database password from Kubernetes secrets
via Dapr using async DaprClient. Also show how to reference secrets in component YAML.
```

**Reflect on Skill**: Add secrets/config patterns to your skill.

---

### L09: Capstone: Dapr-Enabled Task API (40 min) - Layer 4

**Objective**: Refactor the Task API from Part 6 to use Dapr building blocks.

**Content**:
- Spec-driven approach: write specification first
- Replace direct Redis with Dapr state management
- Add Dapr pub/sub for task events (task.created, task.completed)
- Use Dapr service invocation for notification service
- Use Dapr secrets for API keys
- Use Dapr jobs for scheduled cleanup
- Deploy with Dapr annotations on Kubernetes:
  ```yaml
  annotations:
    dapr.io/enabled: "true"
    dapr.io/app-id: "task-api"
    dapr.io/app-port: "8000"
  ```
- Test the complete flow: create task → event published → notification sent

**Deliverable**: Working Task API using Dapr for ALL infrastructure abstraction.

---

### L10: Finalize Your Dapr Skill (20 min) - Layer 3

**Objective**: Complete and test your `dapr-deployment` skill.

**Content**:
- Review all "Reflect on Skill" additions from L01-09
- Test skill against multiple prompts:
  - "Deploy Dapr on Kubernetes"
  - "Add state management to my FastAPI app"
  - "Set up pub/sub with Dapr"
  - "Schedule a recurring job"
- Add safety guardrails and common errors
- Document references section
- Validate skill triggers correctly

**Ends with**: Production-ready `dapr-deployment` skill in your skills library.

## User Scenarios & Testing

### User Story 1 - Learn Skill-First (Priority: P1)

Student creates a `dapr-deployment` skill before learning Dapr concepts, then improves it throughout the chapter.

**Why this priority**: Core pedagogical approach—students learn by building and refining their own asset.

**Independent Test**: Student can generate Dapr deployment YAML using only their skill.

**Acceptance Scenarios**:
1. **Given** student in skills-lab, **When** they run `/fetching-library-docs dapr` and `/skill-creator`, **Then** `.claude/skills/dapr-deployment/SKILL.md` exists
2. **Given** skill exists, **When** prompted "Deploy Dapr on Kubernetes", **Then** skill provides correct Helm commands

---

### User Story 2 - Understand Sidecar Architecture (Priority: P1)

Student understands why Dapr uses sidecars and can explain the benefits.

**Why this priority**: Foundational mental model required for all subsequent lessons.

**Independent Test**: Student can draw/describe the sidecar pattern.

**Acceptance Scenarios**:
1. **Given** L01 complete, **When** asked "Why sidecars?", **Then** student explains separation of concerns and portability
2. **Given** L01 complete, **When** shown Dapr annotations, **Then** student can explain what each annotation does

---

### User Story 3 - Deploy Dapr and Use Building Blocks (Priority: P1)

Student can deploy Dapr AND use each building block with async DaprClient.

**Why this priority**: Hands-on skills are prerequisite for capstone.

**Independent Test**: `kubectl get pods -n dapr-system` shows all components Running AND student can write async FastAPI code using DaprClient.

**Acceptance Scenarios**:
1. **Given** Docker Desktop K8s running, **When** student runs Helm install, **Then** dapr-operator, sidecar-injector, sentry, placement, scheduler pods are Running
2. **Given** Dapr installed, **When** student writes async state management code, **Then** data persists in Redis
3. **Given** pub/sub configured, **When** student publishes event with async client, **Then** subscriber receives CloudEvent

---

### User Story 4 - Use Jobs API for Scheduling (Priority: P2)

Student can schedule future jobs using Dapr Jobs API.

**Why this priority**: Important for agent automation tasks.

**Independent Test**: Student can schedule a job and see it execute.

**Acceptance Scenarios**:
1. **Given** Dapr running, **When** student schedules a job, **Then** job appears in scheduler
2. **Given** job scheduled, **When** due time arrives, **Then** FastAPI handler receives job trigger

---

### User Story 5 - Complete Capstone (Priority: P2)

Student refactors Part 6 Task API to use Dapr for all infrastructure.

**Why this priority**: Integration capstone demonstrates real-world application.

**Independent Test**: Task API works with Dapr, no direct Redis/Kafka clients.

**Acceptance Scenarios**:
1. **Given** Task API with Dapr annotations, **When** deployed, **Then** pod has 2/2 containers (app + sidecar)
2. **Given** Task API running, **When** task created, **Then** state saved via Dapr AND event published via Dapr

---

### Edge Cases

- What happens when Dapr sidecar is not ready? (startup probe, readiness check)
- How to handle component not found errors?
- What if two apps use same app-id?
- How to debug failed service invocation?
- What happens when scheduled job fails?

## Requirements

### Functional Requirements

- **FR-001**: Chapter MUST start with L00 "Build Your Dapr Skill" lesson
- **FR-002**: Every lesson L01-L09 MUST end with "Reflect on Your Skill" section
- **FR-003**: All code examples MUST use async DaprClient (`async with DaprClient()`)
- **FR-004**: All code examples MUST use FastAPI async patterns
- **FR-005**: Helm deployment MUST use Dapr 1.14+
- **FR-006**: State store component MUST use Redis (familiar from caching patterns)
- **FR-007**: Pub/Sub component MUST use Redis (simpler than Kafka for initial learning)
- **FR-008**: Each building block lesson (L03-L08) MUST include hands-on component deployment
- **FR-009**: Capstone (L09) MUST refactor Task API from Part 6
- **FR-010**: All Kubernetes examples MUST target Docker Desktop Kubernetes
- **FR-011**: Chapter MUST include Jobs API lesson (L07)
- **FR-012**: Chapter MUST NOT cover Actors or Workflows (deferred to Ch59)
- **FR-013**: Each lesson MUST have 3 "Try With AI" prompts with learning explanations

### Key Entities

- **Dapr Component**: Custom resource defining infrastructure connection (type, version, metadata)
- **Dapr Subscription**: Custom resource defining topic subscription routing
- **App-id**: Unique identifier for service discovery and state scoping
- **Building Block**: Category of Dapr API (state, pubsub, invoke, secrets, bindings, jobs, config)
- **Job**: Scheduled future work managed by Scheduler service

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can deploy Dapr on Kubernetes in under 10 minutes
- **SC-002**: Students can write async FastAPI apps using 6+ Dapr building blocks
- **SC-003**: Students complete capstone with Task API using Dapr for state, pubsub, invoke, secrets, and jobs
- **SC-004**: Students own a tested `dapr-deployment` skill in their skills library
- **SC-005**: 90% of code examples compile and run without modification
- **SC-006**: Students can swap Redis for another backend by changing only component YAML

## Technology Choices

| Component | Choice | Rationale |
|-----------|--------|-----------|
| **Dapr Version** | 1.14+ | Latest stable, includes Jobs API |
| **Python SDK** | dapr-client (async), dapr-ext-fastapi | Official SDKs, async support |
| **State Store** | Redis | Simple, familiar from caching |
| **Pub/Sub** | Redis | Simpler than Kafka for initial learning |
| **Secrets** | Kubernetes secrets | Built-in, no extra setup |
| **Platform** | Docker Desktop Kubernetes | Consistent with Ch49-51 |

## What's NOT Covered

This chapter focuses on **core building blocks**, not advanced patterns:

- **Dapr Actors** — stateful virtual actors (Chapter 59)
- **Dapr Workflows** — long-running orchestration (Chapter 59)
- **Production security** — mTLS deep dive, API tokens (covered at overview level)
- **Multi-cluster** — cross-cluster service invocation
- **Dapr Agents** — Python framework for LLM agents (potential future chapter)

## Prerequisites

- **Chapter 49**: Docker fundamentals
- **Chapter 50**: Kubernetes basics (Pods, Deployments, Services, Secrets)
- **Chapter 51**: Helm Charts
- **Chapter 52**: Kafka concepts (understand what Dapr abstracts)
- **Part 6**: Your FastAPI agent service (Task API) with async patterns

## Looking Ahead

This chapter covers Dapr's stateless building blocks. Chapter 59 adds **stateful patterns**—Actors for agent state and Workflows for long-running orchestration. The foundation you build here (sidecar architecture, components, APIs) applies directly to those advanced patterns.

## Expertise Skill Reference

Use `.claude/skills/building-with-dapr/SKILL.md` for accurate API patterns, component configurations, and Python SDK examples when implementing lessons.

## Quality Reference

Match structure and quality of Chapter 52 at:
`apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/`
