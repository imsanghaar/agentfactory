# Feature Specification: Chapter 52 - Event-Driven Architecture with Kafka

**Feature Branch**: `004-ch52-event-driven-kafka`
**Created**: 2025-12-28
**Status**: Draft
**Proficiency Level**: B1 (Intermediate)

## Overview

This chapter teaches Event-Driven Architecture (EDA) concepts using Apache Kafka as the implementation technology. The primary goal is understanding **why and when** to use events instead of direct API calls, with Kafka as the practical tool to implement these patterns. Students continue building on the Task API from Part 6, now adding event-driven capabilities.

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Docker fundamentals: images, containers, volumes (Chapter 49)
- Kubernetes basics: Pods, Deployments, Services, kubectl (Chapter 50)
- Helm Charts: packaging, values, templates (Chapter 51)
- FastAPI: async endpoints, dependency injection, Pydantic models (Part 6)
- Python async/await patterns
- Task API structure: endpoints, database models, business logic (Part 6)

**What this chapter must explain from scratch**:
- Event-driven architecture concepts (events vs commands)
- Why request-response APIs fail at scale (coupling problems)
- Apache Kafka fundamentals (brokers, topics, partitions, offsets)
- Strimzi operator and Kubernetes CRDs
- Consumer groups and rebalancing
- Delivery semantics (at-least-once, exactly-once)
- Schema evolution with Avro and Schema Registry
- Change Data Capture patterns

## User Scenarios & Testing

### User Story 1 - Understanding EDA Concepts (Priority: P1)

Students learn WHY event-driven architecture matters before touching any tools. They understand coupling problems in request-response systems and when events provide better solutions.

**Why this priority**: Without conceptual foundation, students will use Kafka as "just another message queue" rather than understanding architectural trade-offs.

**Independent Test**: Student can explain to a colleague why their direct API call design would fail at scale and propose an event-driven alternative.

**Acceptance Scenarios**:

1. **Given** a student sees a system where creating an order triggers notifications, audit logs, and inventory updates via direct API calls, **When** they analyze the design, **Then** they identify coupling problems (blocking, cascading failures, tight dependencies)

2. **Given** a student understands events vs commands, **When** they design a system, **Then** they correctly choose events for broadcast scenarios and commands for directed operations

---

### User Story 2 - Deploy and Operate Kafka on Kubernetes (Priority: P1)

Students deploy Kafka on Docker Desktop Kubernetes using Strimzi operator. They manage topics and users via CRDs.

**Why this priority**: No Kafka practice is possible without a running cluster.

**Independent Test**: Student runs `kubectl get kafka` and sees a healthy cluster with topics created via KafkaTopic CRDs.

**Acceptance Scenarios**:

1. **Given** Strimzi operator is installed via Helm, **When** student applies a Kafka CRD with KRaft mode, **Then** a 1-node Kafka cluster starts within 3 minutes

2. **Given** a running Kafka cluster, **When** student applies a KafkaTopic CRD, **Then** Topic Operator creates the topic with specified partitions and replication

---

### User Story 3 - Produce and Consume Events (Priority: P1)

Students write Python producers and consumers using confluent-kafka-python. They understand delivery reports, consumer groups, and offset management.

**Why this priority**: Core Kafka interaction pattern - all other patterns build on this.

**Independent Test**: Student's producer sends events that are received by their consumer, with offsets correctly tracked.

**Acceptance Scenarios**:

1. **Given** a Kafka topic exists, **When** student's producer sends a message with `acks=all`, **Then** delivery callback confirms successful persistence

2. **Given** multiple consumers in the same group, **When** messages arrive on a multi-partition topic, **Then** partitions are distributed across consumers with no message loss

3. **Given** a consumer restarts, **When** it rejoins the group, **Then** it resumes from last committed offset (no reprocessing or gaps)

---

### User Story 4 - Integrate Kafka with FastAPI (Priority: P2)

Students add event publishing to their Task API. When tasks are created/updated/completed, events are emitted to Kafka.

**Why this priority**: Connects Kafka to the running example from Part 6.

**Independent Test**: Creating a task via Task API results in a `task.created` event on Kafka that a separate consumer receives.

**Acceptance Scenarios**:

1. **Given** Task API with Kafka producer integrated, **When** POST /tasks creates a task, **Then** `task.created` event is published asynchronously

2. **Given** a background consumer subscribed to task events, **When** events arrive, **Then** consumer processes them independently of the API

---

### User Story 5 - Schema Evolution with Avro (Priority: P2)

Students design event schemas using Avro and Schema Registry. They evolve schemas while maintaining backward compatibility.

**Why this priority**: Production systems require schema governance to prevent breaking consumers.

**Independent Test**: Student adds a new optional field to schema, old consumers continue working, new consumers see the field.

**Acceptance Scenarios**:

1. **Given** an Avro schema registered in Schema Registry, **When** producer serializes an event, **Then** message contains schema ID (not full schema)

2. **Given** a schema with fields, **When** student adds a new optional field with default, **Then** Schema Registry accepts it as backward-compatible

---

### User Story 6 - Implement Exactly-Once Semantics (Priority: P2)

Students understand delivery guarantees and implement transactions for atomic multi-topic writes.

**Why this priority**: Critical for financial/critical data scenarios.

**Independent Test**: Student's transactional producer writes to two topics atomically - both succeed or both abort.

**Acceptance Scenarios**:

1. **Given** idempotent producer enabled, **When** network causes retry, **Then** broker deduplicates and stores message only once

2. **Given** transaction started, **When** writes to multiple topics succeed, **Then** `commit_transaction()` makes all visible atomically

---

### User Story 7 - Change Data Capture with Debezium (Priority: P3)

Students capture database changes as events using the outbox pattern with Debezium.

**Why this priority**: Advanced pattern for ensuring transactional integrity between DB and events.

**Independent Test**: Database INSERT triggers event on Kafka topic within seconds.

**Acceptance Scenarios**:

1. **Given** Debezium connector configured for PostgreSQL, **When** row is inserted in outbox table, **Then** event appears on Kafka topic

---

### User Story 8 - Build Capstone: Event-Driven Notifications (Priority: P3)

Students complete a spec-driven capstone adding event-driven notifications to Task API.

**Why this priority**: Integration of all concepts in a realistic scenario.

**Independent Test**: Task API publishes events, notification service consumes them, audit log is maintained.

**Acceptance Scenarios**:

1. **Given** complete event-driven architecture, **When** task is created, **Then** notification service receives event AND audit log records it

---

### Edge Cases

- What happens when Kafka broker is temporarily unavailable? (Producer buffering, retry behavior)
- How does consumer handle poison messages that cause processing exceptions?
- What happens during consumer group rebalancing while processing a message?
- How to handle Schema Registry unavailability?
- What if transaction coordinator fails mid-transaction?

## Requirements

### Functional Requirements

- **FR-001**: Chapter MUST contain 22 lessons organized in 7 parts (A through G)
- **FR-002**: Lessons 1-3 MUST teach EDA concepts without requiring Kafka installation
- **FR-003**: Lesson 4 MUST use Strimzi operator (Helm install) for Kafka deployment on Kubernetes
- **FR-004**: Chapter MUST use KRaft mode (no ZooKeeper) - Kafka 3.8+ / 4.0
- **FR-005**: All code examples MUST use confluent-kafka-python library
- **FR-006**: Chapter MUST continue Task API running example from Part 6
- **FR-007**: Lesson 21 (Capstone) MUST be spec-driven following L4 pattern
- **FR-008**: Lesson 22 MUST produce a reusable skill following L3 pattern
- **FR-009**: Each lesson MUST include 3 "Try With AI" prompts with explanations
- **FR-010**: Schema examples MUST use Avro with Confluent Schema Registry
- **FR-011**: CDC lesson MUST cover Debezium with outbox pattern
- **FR-012**: Production lessons MUST cover consumer lag monitoring and debugging

### Chapter Structure Requirements

| Part | Lessons | Layer | Focus |
|------|---------|-------|-------|
| A: EDA Foundations | 1-3 | L1 (Manual) | Concepts, mental models, vocabulary |
| B: Kafka Core | 4-8 | L1→L2 | Hands-on Kafka with AI assistance |
| C: Production Patterns | 9-13 | L2 | Advanced patterns, AI collaboration |
| D: Data Pipelines | 14-15 | L2 | Kafka Connect, Debezium CDC |
| E: Agent Patterns | 16-17 | L2 | Event patterns for AI agents |
| F: Operations | 18-19 | L2 | Production config, monitoring |
| G: Capstone | 20-22 | L2/L4/L3 | AI collab, capstone, skill creation |

### Technology Stack

- **Platform**: Docker Desktop Kubernetes
- **Kafka Operator**: Strimzi (CNCF incubating project)
- **Kafka Version**: 3.8+ with KRaft mode
- **Python Client**: confluent-kafka-python
- **Schemas**: Avro + Confluent Schema Registry
- **CDC**: Debezium PostgreSQL connector
- **Running Example**: Task API from Part 6

### Key Entities

- **Event**: Immutable record of something that happened (id, type, timestamp, data, metadata)
- **Topic**: Named stream of events, partitioned for scalability
- **Consumer Group**: Set of consumers sharing partition assignments
- **Schema**: Avro definition of event structure, versioned in registry
- **Saga**: Multi-step workflow coordinated via events

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students deploy Kafka on Kubernetes in under 10 minutes following lesson instructions
- **SC-002**: Students can explain the difference between events and commands with real examples
- **SC-003**: Students correctly implement at-least-once delivery pattern for critical events
- **SC-004**: Students' event schemas pass backward compatibility check in Schema Registry
- **SC-005**: Students' Task API publishes events that are independently consumed by notification service
- **SC-006**: Students complete capstone spec and implementation within 2 hours
- **SC-007**: 80% of students can debug consumer lag issues using lesson-provided techniques
- **SC-008**: Students create a reusable Kafka Event Schema skill they can apply to future projects

### Learning Progression Validation

- L1-L3 build vocabulary (events, topics, partitions, consumer groups) needed for L21 capstone spec
- L4-L8 provide hands-on foundation before advanced patterns in L9-L17
- L20 (AI collaboration) comes after students have manual proficiency
- L21 (capstone) integrates all concepts in spec-driven format
- L22 (skill creation) extracts reusable patterns for future chapters

## Assumptions

1. Students have completed Chapters 49-51 and have Docker Desktop Kubernetes running
2. Students have the Task API from Part 6 available to extend
3. Docker Desktop Kubernetes has sufficient resources (4GB+ RAM allocated)
4. Students have basic command-line proficiency (kubectl, helm)
5. Schema Registry will be deployed as part of Strimzi ecosystem or separately via Helm

## Dependencies

- Chapter 49: Docker fundamentals
- Chapter 50: Kubernetes fundamentals
- Chapter 51: Helm Charts
- Part 6: Task API implementation
- Expertise skill: `.claude/skills/building-with-kafka-strimzi/SKILL.md`

## Out of Scope

- Multi-datacenter replication (MirrorMaker 2)
- Deep security configuration (SASL, SSL, ACLs beyond basics)
- Kafka Streams framework
- ZooKeeper (deprecated in Kafka 4.0)
- Cloud-managed Kafka services (Confluent Cloud, Amazon MSK)
