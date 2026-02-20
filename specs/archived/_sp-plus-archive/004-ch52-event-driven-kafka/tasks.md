# Tasks: Chapter 52 - Event-Driven Architecture with Kafka

**Created**: 2025-12-28
**Source Plan**: specs/004-ch52-event-driven-kafka/plan.md
**Chapter Path**: apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/

---

## Task Overview

| ID | Task | Status | Dependencies |
|----|------|--------|--------------|
| T52.README | Update Chapter README | [ ] | None |
| T52.L01 | Lesson 1: From Request-Response to Events | [ ] | None |
| T52.L02 | Lesson 2: Event-Driven Architecture Concepts | [ ] | T52.L01 |
| T52.L03 | Lesson 3: How Kafka Fits - The Mental Model | [ ] | T52.L02 |
| T52.L04 | Lesson 4: Deploying Kafka with Strimzi | [ ] | T52.L03 |
| T52.L05 | Lesson 5: Your First Producer (Python) | [ ] | T52.L04 |
| T52.L06 | Lesson 6: Producer Deep Dive - Reliability | [ ] | T52.L05 |
| T52.L07 | Lesson 7: Your First Consumer (Python) | [ ] | T52.L04 |
| T52.L08 | Lesson 8: Consumer Deep Dive - Groups and Rebalancing | [ ] | T52.L07 |
| T52.L09 | Lesson 9: Async Producers and Consumers in FastAPI | [ ] | T52.L08 |
| T52.L10 | Lesson 10: Message Schemas - Avro and Schema Registry | [ ] | T52.L09 |
| T52.L11 | Lesson 11: Delivery Semantics Deep Dive | [ ] | T52.L08 |
| T52.L12 | Lesson 12: Transactions for Stream Processing | [ ] | T52.L11 |
| T52.L13 | Lesson 13: Reliability Configuration | [ ] | T52.L06 |
| T52.L14 | Lesson 14: Kafka Connect - Building Data Pipelines | [ ] | T52.L04 |
| T52.L15 | Lesson 15: Change Data Capture with Debezium | [ ] | T52.L14 |
| T52.L16 | Lesson 16: Agent Event Patterns | [ ] | T52.L09 |
| T52.L17 | Lesson 17: Saga Pattern for Multi-Step Workflows | [ ] | T52.L16 |
| T52.L18 | Lesson 18: Production Kafka with Strimzi | [ ] | T52.L04 |
| T52.L19 | Lesson 19: Monitoring and Debugging Kafka | [ ] | T52.L08 |
| T52.L20 | Lesson 20: AI-Assisted Kafka Development | [ ] | T52.L19 |
| T52.L21 | Lesson 21: Capstone - Event-Driven Agent Notifications | [ ] | T52.L20 |
| T52.L22 | Lesson 22: Building the Kafka Event Schema Skill | [ ] | T52.L21 |
| T52.VALIDATE | Run all validators | [ ] | All lessons |

---

## Detailed Tasks

### T52.README: Update Chapter README

**Description**: Ensure README matches final lesson structure

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/README.md`

**Acceptance Criteria**:
- [ ] Sidebar position correct (52)
- [ ] All 22 lessons listed with accurate titles
- [ ] Technology choices match spec (Strimzi, KRaft, confluent-kafka-python)
- [ ] Prerequisites updated

---

### T52.L01: Lesson 1 - From Request-Response to Events

**Description**: Create foundational lesson explaining why events beat direct API calls

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/01-from-request-response-to-events.md`

**Layer**: L1 (Manual Foundation)
**Duration**: 40 minutes
**Bloom's Level**: Understand

**Learning Objectives**:
1. Explain why direct API calls between services create tight coupling
2. Identify three types of coupling problems: temporal, availability, behavioral
3. Describe how asynchronous events solve coupling problems

**Acceptance Criteria**:
- [ ] Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
- [ ] Compelling narrative opening with Task API scenario
- [ ] Diagram showing cascading failure in request-response
- [ ] 3 "Try With AI" prompts with "What you're learning" explanations
- [ ] NO sections after "Try With AI"
- [ ] Evidence blocks for conceptual examples

---

### T52.L02: Lesson 2 - Event-Driven Architecture Concepts

**Description**: Teach events vs commands, eventual consistency, and when to use EDA

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/02-event-driven-architecture-concepts.md`

**Layer**: L1 (Manual Foundation)
**Duration**: 45 minutes
**Bloom's Level**: Understand

**Learning Objectives**:
1. Distinguish between events and commands with examples
2. Explain eventual consistency and why it works for most business scenarios
3. Evaluate when to use EDA versus synchronous APIs

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Table comparing events vs commands
- [ ] Bank transfer example for eventual consistency
- [ ] Decision matrix: when EDA fits vs doesn't
- [ ] 3 "Try With AI" prompts

---

### T52.L03: Lesson 3 - How Kafka Fits: The Mental Model

**Description**: Introduce Kafka architecture using visual analogies

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/03-kafka-mental-model.md`

**Layer**: L1 (Manual Foundation)
**Duration**: 45 minutes
**Bloom's Level**: Understand

**Learning Objectives**:
1. Describe Kafka's core components using visual analogies
2. Explain how consumer groups enable parallel processing
3. Trace a message journey from producer to consumer

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Kafka architecture diagram (KRaft mode)
- [ ] Newspaper analogy for topics/partitions
- [ ] 3 "Try With AI" prompts

---

### T52.L04: Lesson 4 - Deploying Kafka with Strimzi

**Description**: First hands-on: deploy Kafka on Docker Desktop K8s with Strimzi

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/04-deploying-kafka-with-strimzi.md`

**Layer**: L1 (Manual - first hands-on)
**Duration**: 50 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Deploy Strimzi operator using Helm
2. Create a Kafka cluster with KafkaNodePool and Kafka CRDs
3. Manage topics with KafkaTopic CRDs

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Complete Helm install commands
- [ ] KafkaNodePool YAML (dual-role for dev)
- [ ] Kafka CRD YAML (KRaft mode)
- [ ] KafkaTopic CRD YAML
- [ ] Verification commands (kubectl)
- [ ] 3 "Try With AI" prompts

---

### T52.L05: Lesson 5 - Your First Producer (Python)

**Description**: Write first Kafka producer with confluent-kafka-python

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/05-your-first-producer.md`

**Layer**: L1 (Manual Foundation)
**Duration**: 45 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Configure a Kafka producer with confluent-kafka-python
2. Send messages with key, value, and delivery callback
3. Verify message delivery

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Install command (uv add confluent-kafka)
- [ ] Complete producer code with delivery callback
- [ ] Explanation of poll() and flush()
- [ ] 3 "Try With AI" prompts

---

### T52.L06: Lesson 6 - Producer Deep Dive: Reliability

**Description**: Configure acks, retries, and idempotent producer

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/06-producer-reliability.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 50 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Configure acks=all for critical data
2. Enable idempotent producer
3. Diagnose delivery failures

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Table: acks=0 vs acks=1 vs acks=all
- [ ] Idempotent producer configuration
- [ ] Error handling patterns
- [ ] AI Three Roles demonstration (invisible framework)
- [ ] 3 "Try With AI" prompts

---

### T52.L07: Lesson 7 - Your First Consumer (Python)

**Description**: Write first Kafka consumer with poll loop

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/07-your-first-consumer.md`

**Layer**: L1->L2 (Transition)
**Duration**: 45 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Implement a consumer poll loop with error handling
2. Configure auto.offset.reset
3. Choose between auto-commit and manual commit

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Complete consumer code with poll loop
- [ ] Error handling for partition EOF
- [ ] Auto-commit vs manual commit comparison
- [ ] 3 "Try With AI" prompts

---

### T52.L08: Lesson 8 - Consumer Deep Dive: Groups and Rebalancing

**Description**: Understand consumer groups, rebalancing, and lag

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/08-consumer-groups-rebalancing.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 50 minutes
**Bloom's Level**: Analyze

**Learning Objectives**:
1. Explain partition distribution and rebalancing triggers
2. Implement rebalance callbacks
3. Diagnose consumer lag

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Rebalance callback code (on_assign, on_revoke)
- [ ] Consumer lag explanation
- [ ] Static membership mention
- [ ] 3 "Try With AI" prompts

---

### T52.L09: Lesson 9 - Async Producers and Consumers in FastAPI

**Description**: Integrate Kafka with FastAPI using lifespan events

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/09-async-fastapi-integration.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 50 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Integrate producer with FastAPI lifespan
2. Publish events from endpoints
3. Run background consumer thread

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] FastAPI lifespan context manager
- [ ] Producer integration with endpoints
- [ ] Background consumer thread pattern
- [ ] Connection to Task API
- [ ] 3 "Try With AI" prompts

---

### T52.L10: Lesson 10 - Message Schemas: Avro and Schema Registry

**Description**: Design event schemas with Avro and Schema Registry

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/10-avro-schema-registry.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 55 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Design an Avro schema for task events
2. Integrate Schema Registry with producer/consumer
3. Evolve schemas safely

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Avro schema example for TaskCreated
- [ ] AvroSerializer/AvroDeserializer code
- [ ] Schema evolution example
- [ ] 3 "Try With AI" prompts

---

### T52.L11: Lesson 11 - Delivery Semantics Deep Dive

**Description**: Compare delivery guarantees and implementation requirements

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/11-delivery-semantics.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 45 minutes
**Bloom's Level**: Analyze

**Learning Objectives**:
1. Compare at-most-once, at-least-once, exactly-once
2. Implement at-least-once pattern
3. Evaluate when exactly-once is necessary

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Comparison table of delivery semantics
- [ ] Decision matrix for choosing semantic
- [ ] Idempotent consumer alternative
- [ ] 3 "Try With AI" prompts

---

### T52.L12: Lesson 12 - Transactions for Stream Processing

**Description**: Implement transactional producers for atomic multi-topic writes

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/12-transactions-stream-processing.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 50 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Implement a transactional producer
2. Configure consumers with read_committed
3. Explain zombie fencing

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Transactional producer code
- [ ] Transaction lifecycle (begin/commit/abort)
- [ ] read_committed consumer config
- [ ] 3 "Try With AI" prompts

---

### T52.L13: Lesson 13 - Reliability Configuration

**Description**: Configure replication factor, min.insync.replicas, and ISR

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/13-reliability-configuration.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 45 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Configure replication factor and min.insync.replicas
2. Explain ISR mechanics
3. Diagnose NOT_ENOUGH_REPLICAS errors

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] RF/min.isr formula explanation
- [ ] Dev vs prod settings comparison
- [ ] Strimzi configuration examples
- [ ] 3 "Try With AI" prompts

---

### T52.L14: Lesson 14 - Kafka Connect: Building Data Pipelines

**Description**: Deploy Kafka Connect for standardized data integration

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/14-kafka-connect-pipelines.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 50 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Deploy Kafka Connect with Strimzi
2. Configure a source connector
3. Decide when to use Connect vs custom client

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] KafkaConnect CRD example
- [ ] Source connector configuration
- [ ] Decision matrix: Connect vs client
- [ ] 3 "Try With AI" prompts

---

### T52.L15: Lesson 15 - Change Data Capture with Debezium

**Description**: Capture database changes as events using Debezium and outbox pattern

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/15-debezium-cdc.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 55 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Explain CDC advantages over polling
2. Deploy Debezium PostgreSQL connector
3. Implement the outbox pattern

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Debezium connector configuration
- [ ] Outbox table schema
- [ ] WAL reading explanation
- [ ] 3 "Try With AI" prompts

---

### T52.L16: Lesson 16 - Agent Event Patterns

**Description**: Design event schemas for Task API with metadata and fanout

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/16-agent-event-patterns.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 50 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Design event schemas with correlation/causation IDs
2. Implement notification fanout
3. Build immutable audit log

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Event naming conventions (domain.action)
- [ ] Event schema with metadata
- [ ] Fanout pattern example
- [ ] Audit log consumer
- [ ] 3 "Try With AI" prompts

---

### T52.L17: Lesson 17 - Saga Pattern for Multi-Step Workflows

**Description**: Implement sagas for coordinating multi-service workflows

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/17-saga-pattern.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 55 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Explain saga pattern and when it applies
2. Implement choreography-based saga
3. Design compensation events

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Choreography vs orchestration comparison
- [ ] Saga state machine
- [ ] Compensation event examples
- [ ] 3 "Try With AI" prompts

---

### T52.L18: Lesson 18 - Production Kafka with Strimzi

**Description**: Configure multi-broker Kafka for production reliability

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/18-production-kafka-strimzi.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 50 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Configure multi-node Kafka cluster
2. Set resource limits and persistent storage
3. Manage users and ACLs with KafkaUser CRDs

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Production KafkaNodePool (separate roles)
- [ ] PVC configuration
- [ ] KafkaUser with ACLs
- [ ] 3 "Try With AI" prompts

---

### T52.L19: Lesson 19 - Monitoring and Debugging Kafka

**Description**: Monitor consumer lag and diagnose common issues

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/19-monitoring-debugging.md`

**Layer**: L2 (AI Collaboration)
**Duration**: 50 minutes
**Bloom's Level**: Analyze

**Learning Objectives**:
1. Monitor consumer lag
2. Diagnose under-replicated partitions
3. Use Kafka CLI tools

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Consumer lag monitoring commands
- [ ] Key metrics table
- [ ] Common errors and fixes table
- [ ] 3 "Try With AI" prompts

---

### T52.L20: Lesson 20 - AI-Assisted Kafka Development

**Description**: Deep AI collaboration for Kafka development

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/20-ai-assisted-kafka-development.md`

**Layer**: L2 (AI Collaboration - Deep)
**Duration**: 45 minutes
**Bloom's Level**: Apply

**Learning Objectives**:
1. Apply AI Three Roles to Kafka debugging
2. Generate Avro schemas with AI
3. Optimize configuration with AI

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Three Roles examples (Teacher/Student/Co-Worker)
- [ ] Practical exercises with AI
- [ ] Reflection section
- [ ] 3 "Try With AI" prompts

---

### T52.L21: Lesson 21 - Capstone: Event-Driven Agent Notifications

**Description**: Spec-driven capstone integrating all chapter concepts

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/21-capstone-event-driven-notifications.md`

**Layer**: L4 (Spec-Driven Capstone)
**Duration**: 90 minutes
**Bloom's Level**: Create

**Learning Objectives**:
1. Write a specification for event-driven notifications
2. Implement by composing skills from previous lessons
3. Validate against specification

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Phase 1: Specification writing (25 min)
- [ ] Phase 2: Skill composition (45 min)
- [ ] Phase 3: Validation (20 min)
- [ ] End-to-end test scenarios
- [ ] 3 "Try With AI" prompts

---

### T52.L22: Lesson 22 - Building the Kafka Event Schema Skill

**Description**: Create reusable skill for event schema design

**Output Path**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/22-kafka-event-schema-skill.md`

**Layer**: L3 (Intelligence Design)
**Duration**: 60 minutes
**Bloom's Level**: Create

**Learning Objectives**:
1. Extract reusable patterns into skill specification
2. Design skill with persona, questions, and principles
3. Test skill on novel domain

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Skill structure explanation
- [ ] Event schema patterns extracted
- [ ] Skill YAML example
- [ ] Testing on e-commerce domain
- [ ] 3 "Try With AI" prompts

---

### T52.VALIDATE: Run All Validators

**Description**: Execute validators before commit

**Acceptance Criteria**:
- [ ] educational-validator passes for all 22 lessons
- [ ] validation-auditor score >= 80%
- [ ] factual-verifier confirms all claims
- [ ] pedagogical-designer validates progression

---

## Implementation Notes

**Quality Reference**: Match structure and quality of:
`apps/learn-app/docs/01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-digital-fte-revolution.md`

**Expertise Source**: Use patterns from:
`.claude/skills/building-with-kafka-strimzi/SKILL.md`

**Framework Invisibility**: AI Three Roles must be demonstrated through content, never mentioned explicitly (no "AI as Teacher" headings).
