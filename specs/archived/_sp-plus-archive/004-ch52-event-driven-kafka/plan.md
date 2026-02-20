# Implementation Plan: Chapter 52 - Event-Driven Architecture with Kafka

**Created**: 2025-12-28
**Source Spec**: specs/004-ch52-event-driven-kafka/spec.md
**Expertise Skill**: .claude/skills/building-with-kafka-strimzi/SKILL.md
**Chapter README**: apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/README.md
**Part**: 7 - AI Cloud Native Development
**Proficiency Level**: B1 (Intermediate) per spec
**Total Lessons**: 22

---

## Pedagogical Arc Overview

| Part | Lessons | Layer | Focus | Cognitive Load |
|------|---------|-------|-------|----------------|
| **A: EDA Foundations** | 1-3 | L1 (Manual) | Concepts, mental models, vocabulary | Light (3-5 concepts/lesson) |
| **B: Kafka Core** | 4-8 | L1->L2 | Hands-on Kafka deployment and clients | Moderate (5-7 concepts/lesson) |
| **C: Production Patterns** | 9-13 | L2 | Advanced patterns with AI collaboration | Moderate-Heavy (6-8 concepts/lesson) |
| **D: Data Pipelines** | 14-15 | L2 | Kafka Connect, Debezium CDC | Moderate (5-6 concepts/lesson) |
| **E: Agent Patterns** | 16-17 | L2 | Event patterns for AI agents | Moderate (5-6 concepts/lesson) |
| **F: Operations** | 18-19 | L2 | Production config, monitoring | Moderate (5-6 concepts/lesson) |
| **G: Integration** | 20-22 | L2/L4/L3 | AI collaboration, capstone, skill creation | Variable |

---

## Part A: EDA Foundations (Lessons 1-3, Layer 1)

### Lesson 1: From Request-Response to Events

**File**: `01-from-request-response-to-events.md`
**Layer**: L1 (Manual Foundation)
**Proficiency**: B1
**Bloom's Level**: Understand
**Duration**: 40 minutes

**Key Concepts from Expertise Skill**:
- Request-response coupling problems
- Synchronous vs asynchronous communication
- Cascading failures in direct API calls
- Temporal coupling and availability coupling
- The need for decoupling

**Learning Objectives**:
1. **Explain** why direct API calls between services create tight coupling (B1, Understand)
2. **Identify** three types of coupling problems in request-response systems: temporal, availability, and behavioral (B1, Understand)
3. **Describe** how asynchronous events solve coupling problems with a real-world example (B1, Understand)

**Content Outline**:
- Opening scenario: Task API calling notifications, audit, and reminders synchronously
- Diagram: What happens when notification service is slow
- Three coupling problems: temporal (both must be up), availability (failures cascade), behavioral (caller knows callee's interface)
- The solution preview: events as facts, consumers read independently
- "Try With AI" prompts (3)

**Dependencies**: None (chapter opener)

---

### Lesson 2: Event-Driven Architecture Concepts

**File**: `02-event-driven-architecture-concepts.md`
**Layer**: L1 (Manual Foundation)
**Proficiency**: B1
**Bloom's Level**: Understand
**Duration**: 45 minutes

**Key Concepts from Expertise Skill**:
- Events vs Commands distinction
- Eventual consistency
- Event sourcing (conceptual intro)
- CQRS overview (conceptual intro)
- When EDA fits vs when it does not

**Learning Objectives**:
1. **Distinguish** between events (immutable facts about the past) and commands (requests to perform actions) with examples (B1, Understand)
2. **Explain** eventual consistency and why it is acceptable for most business scenarios (B1, Understand)
3. **Evaluate** when to use EDA versus synchronous APIs based on use case characteristics (B1, Analyze)

**Content Outline**:
- Events: "TaskCreated" - something happened (immutable)
- Commands: "CreateTask" - request to do something (can fail)
- Table: Event vs Command naming, semantics, handling
- Eventual consistency: The bank transfer example
- When EDA fits: high fanout, audit trails, decoupling needed
- When EDA does NOT fit: simple CRUD, low latency required, strong consistency mandatory
- "Try With AI" prompts (3)

**Dependencies**: Lesson 1

---

### Lesson 3: How Kafka Fits - The Mental Model

**File**: `03-kafka-mental-model.md`
**Layer**: L1 (Manual Foundation)
**Proficiency**: B1
**Bloom's Level**: Understand
**Duration**: 45 minutes

**Key Concepts from Expertise Skill**:
- Topics as named streams
- Partitions for parallelism
- Offsets for position tracking
- Producers and consumers
- Consumer groups
- Brokers (KRaft mode)

**Learning Objectives**:
1. **Describe** Kafka's core components (topics, partitions, offsets, brokers) using visual analogies (B1, Understand)
2. **Explain** how consumer groups enable parallel processing without message loss (B1, Understand)
3. **Trace** the journey of a message from producer through topic to consumer, identifying each component (B1, Apply)

**Content Outline**:
- Analogy: Topics as newspaper sections, partitions as delivery routes
- Visual: Kafka architecture diagram (KRaft mode - no ZooKeeper)
- Topics: Named streams of events
- Partitions: Parallelism units, ordering guarantees within partition
- Offsets: "Where was I?" bookmark for consumers
- Consumer groups: Load distribution without coordination
- Brokers: The newspaper printing presses
- "Try With AI" prompts (3)

**Dependencies**: Lessons 1-2

---

## Part B: Kafka Core (Lessons 4-8, L1 to L2)

### Lesson 4: Deploying Kafka with Strimzi

**File**: `04-deploying-kafka-with-strimzi.md`
**Layer**: L1 (Manual - first hands-on)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 50 minutes

**Key Concepts from Expertise Skill**:
- Strimzi operator (CNCF project)
- Helm installation of Strimzi
- Kafka CRD with KRaft mode
- KafkaNodePool for combined controller/broker
- KafkaTopic CRD
- Entity Operator (Topic + User operators)

**Learning Objectives**:
1. **Deploy** Strimzi operator on Docker Desktop Kubernetes using Helm (B1, Apply)
2. **Create** a Kafka cluster using KafkaNodePool and Kafka CRDs in KRaft mode (B1, Apply)
3. **Manage** Kafka topics declaratively using KafkaTopic custom resources (B1, Apply)

**Content Outline**:
- Prerequisites check: Docker Desktop K8s, kubectl, Helm
- Step 1: Add Strimzi Helm repo, install operator
- Step 2: Verify operator pods running
- Step 3: Apply KafkaNodePool (dual-role: controller + broker)
- Step 4: Apply Kafka CRD (KRaft mode, no ZooKeeper)
- Step 5: Wait for cluster ready, verify with kubectl
- Step 6: Create KafkaTopic via CRD
- Explanation: How Topic Operator works
- "Try With AI" prompts (3)

**Dependencies**: Lessons 1-3, Chapters 49-51 (Docker, K8s, Helm)

---

### Lesson 5: Your First Producer (Python)

**File**: `05-your-first-producer.md`
**Layer**: L1 (Manual Foundation)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 45 minutes

**Key Concepts from Expertise Skill**:
- confluent-kafka-python library
- Producer configuration basics
- produce() method
- Delivery reports (callbacks)
- poll() and flush()

**Learning Objectives**:
1. **Configure** a Kafka producer with confluent-kafka-python including bootstrap servers and client ID (B1, Apply)
2. **Send** messages to a topic using produce() with key, value, and delivery callback (B1, Apply)
3. **Verify** message delivery using delivery reports and console inspection (B1, Apply)

**Content Outline**:
- Install confluent-kafka-python (uv add confluent-kafka)
- Basic producer setup: bootstrap.servers, client.id
- The produce() call: topic, key, value
- Why keys matter: partition assignment
- Delivery callback: success vs failure handling
- poll(0) for callback processing
- flush() before shutdown
- Hands-on: Send 10 messages to task-created topic
- Verify: Use Kafka CLI to consume and see messages
- "Try With AI" prompts (3)

**Dependencies**: Lesson 4 (running Kafka cluster)

---

### Lesson 6: Producer Deep Dive - Reliability

**File**: `06-producer-reliability.md`
**Layer**: L2 (AI Collaboration begins)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 50 minutes

**Key Concepts from Expertise Skill**:
- acks settings (0, 1, all)
- Retries and delivery.timeout.ms
- Idempotent producer (enable.idempotence)
- max.in.flight.requests.per.connection
- When to use which acks level

**Learning Objectives**:
1. **Configure** acks=all for critical data and explain trade-offs vs acks=1 (B1, Apply)
2. **Enable** idempotent producer to prevent duplicates during retries (B1, Apply)
3. **Diagnose** delivery failures using delivery callback error handling patterns (B1, Analyze)

**Content Outline**:
- acks=0: Fire and forget (fast, lossy)
- acks=1: Leader acknowledgment (balanced)
- acks=all: All ISR acknowledgment (safe, slower)
- Decision table: Use case -> acks setting
- Retries: What happens on network failure?
- Idempotent producer: Broker deduplication
- AI Collaboration: Three Roles demonstration
  - AI as Teacher: Suggests optimal retry configuration
  - AI as Student: Adapts to production requirements
  - AI as Co-Worker: Iterates on error handling strategy
- "Try With AI" prompts (3)

**Dependencies**: Lesson 5

---

### Lesson 7: Your First Consumer (Python)

**File**: `07-your-first-consumer.md`
**Layer**: L1->L2 (Transition)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 45 minutes

**Key Concepts from Expertise Skill**:
- Consumer configuration
- group.id and consumer groups
- subscribe() vs assign()
- poll() loop pattern
- auto.offset.reset (earliest, latest)
- enable.auto.commit (true/false)
- Manual commit with commit()

**Learning Objectives**:
1. **Implement** a consumer poll loop with proper error handling for partition EOF (B1, Apply)
2. **Configure** auto.offset.reset to control behavior for new consumer groups (B1, Apply)
3. **Choose** between auto-commit and manual commit based on processing guarantees needed (B1, Analyze)

**Content Outline**:
- Consumer setup: group.id, auto.offset.reset
- subscribe() to topics
- The poll loop: poll(timeout), check for None, check for errors
- Processing messages: decode, business logic
- Auto-commit: Simple but risky (what if crash after poll, before process?)
- Manual commit: Control when offsets are stored
- At-least-once pattern: Process, then commit
- "Try With AI" prompts (3)

**Dependencies**: Lessons 4-6

---

### Lesson 8: Consumer Deep Dive - Groups and Rebalancing

**File**: `08-consumer-groups-rebalancing.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Analyze
**Duration**: 50 minutes

**Key Concepts from Expertise Skill**:
- Consumer group mechanics
- Partition assignment strategies
- Rebalance triggers (member join/leave)
- on_assign and on_revoke callbacks
- Static membership (group.instance.id)
- Consumer lag concept

**Learning Objectives**:
1. **Explain** how Kafka distributes partitions across consumers in a group and what triggers rebalancing (B1, Understand)
2. **Implement** rebalance callbacks to commit offsets before partition revocation (B1, Apply)
3. **Diagnose** consumer lag as an indicator of consumer performance issues (B1, Analyze)

**Content Outline**:
- Consumer groups: Why multiple consumers share work
- Partition assignment: Cooperative vs eager
- Rebalancing: When it happens, what it means
- Problem: Message processed, rebalance, no commit -> duplicate
- Solution: on_revoke callback with synchronous commit
- Static membership: Reduce unnecessary rebalances
- Consumer lag: Difference between latest offset and consumer position
- AI Collaboration: Debug rebalancing issues with AI
- "Try With AI" prompts (3)

**Dependencies**: Lesson 7

---

## Part C: Production Patterns (Lessons 9-13, Layer L2)

### Lesson 9: Async Producers and Consumers in FastAPI

**File**: `09-async-fastapi-integration.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 50 minutes

**Key Concepts from Expertise Skill**:
- FastAPI lifespan events
- Producer integration with FastAPI
- Background consumer thread
- Async patterns for Kafka (not truly async, but non-blocking)
- Thread safety considerations

**Learning Objectives**:
1. **Integrate** Kafka producer with FastAPI using lifespan events for proper startup/shutdown (B1, Apply)
2. **Publish** events from FastAPI endpoints asynchronously without blocking request handling (B1, Apply)
3. **Run** a background consumer thread alongside FastAPI for event processing (B1, Apply)

**Content Outline**:
- FastAPI lifespan: Initialize producer on startup, flush on shutdown
- Producing from endpoints: produce() + poll(0) pattern
- Why not await? confluent-kafka is not async, but non-blocking
- Background consumer: Threading for consuming in parallel
- Connecting to Task API: Add event publishing to create_task endpoint
- AI Collaboration: Design async patterns with AI assistance
- "Try With AI" prompts (3)

**Dependencies**: Lessons 5-8, Part 6 Task API

---

### Lesson 10: Message Schemas - Avro and Schema Registry

**File**: `10-avro-schema-registry.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 55 minutes

**Key Concepts from Expertise Skill**:
- Why schemas matter (contract between producers and consumers)
- Avro schema format
- Schema Registry deployment
- AvroSerializer and AvroDeserializer
- Schema evolution compatibility types (backward, forward, full)

**Learning Objectives**:
1. **Design** an Avro schema for task events with required and optional fields (B1, Apply)
2. **Integrate** Schema Registry with producer/consumer for automatic schema validation (B1, Apply)
3. **Evolve** schemas safely using backward-compatible changes (adding optional fields with defaults) (B1, Apply)

**Content Outline**:
- Problem: JSON schema drift, no contract enforcement
- Solution: Avro + Schema Registry
- Avro schema syntax: records, fields, types, defaults
- Schema Registry: Stores and versions schemas
- Producer with AvroSerializer: Schema ID in message header
- Consumer with AvroDeserializer: Automatic deserialization
- Schema evolution: Adding fields safely
- AI Collaboration: Generate Avro schemas from Python classes
- "Try With AI" prompts (3)

**Dependencies**: Lesson 9

---

### Lesson 11: Delivery Semantics Deep Dive

**File**: `11-delivery-semantics.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Analyze
**Duration**: 45 minutes

**Key Concepts from Expertise Skill**:
- At-most-once delivery
- At-least-once delivery
- Exactly-once delivery
- Idempotent producer limitations
- Trade-offs: latency, throughput, complexity

**Learning Objectives**:
1. **Compare** at-most-once, at-least-once, and exactly-once semantics with implementation requirements (B1, Analyze)
2. **Implement** at-least-once pattern for typical event processing (B1, Apply)
3. **Evaluate** when exactly-once is necessary vs when at-least-once with idempotent consumers suffices (B1, Evaluate)

**Content Outline**:
- At-most-once: Fast, can lose data (acks=0, commit before process)
- At-least-once: Safe, may duplicate (acks=all, process then commit)
- Exactly-once: Complex, expensive (transactions + read_committed)
- Decision matrix: Use case -> delivery semantic
- Idempotent consumers: Alternative to exactly-once
- AI Collaboration: Analyze existing system and recommend semantic
- "Try With AI" prompts (3)

**Dependencies**: Lessons 6-8

---

### Lesson 12: Transactions for Stream Processing

**File**: `12-transactions-stream-processing.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 50 minutes

**Key Concepts from Expertise Skill**:
- Transactional producer
- transactional.id configuration
- init_transactions(), begin_transaction(), commit_transaction(), abort_transaction()
- Zombie fencing
- isolation.level=read_committed

**Learning Objectives**:
1. **Implement** a transactional producer that writes to multiple topics atomically (B1, Apply)
2. **Configure** consumers with isolation.level=read_committed to see only committed messages (B1, Apply)
3. **Explain** how zombie fencing prevents duplicate processing from crashed transactional producers (B1, Understand)

**Content Outline**:
- Use case: Consume from input, process, produce to output + audit
- Problem: Crash after output produce, before commit -> duplicate on restart
- Solution: Transactions make consume-process-produce atomic
- transactional.id: Unique identifier for transactional producer
- init_transactions(): One-time setup
- begin/commit/abort: Transaction lifecycle
- Zombie fencing: Old producer with same transactional.id is fenced
- Consumer side: read_committed isolation
- AI Collaboration: Design transactional workflow with AI
- "Try With AI" prompts (3)

**Dependencies**: Lessons 6, 11

---

### Lesson 13: Reliability Configuration

**File**: `13-reliability-configuration.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 45 minutes

**Key Concepts from Expertise Skill**:
- Replication factor
- min.insync.replicas
- In-Sync Replicas (ISR)
- unclean.leader.election.enable
- Broker configuration for durability

**Learning Objectives**:
1. **Configure** replication factor and min.insync.replicas for durability guarantees (B1, Apply)
2. **Explain** how ISR works and what happens when brokers fall out of sync (B1, Understand)
3. **Diagnose** NOT_ENOUGH_REPLICAS errors and determine appropriate remediation (B1, Analyze)

**Content Outline**:
- Replication factor: How many copies of each partition
- ISR: Replicas that are caught up with leader
- min.insync.replicas: Minimum ISR for acks=all to succeed
- Formula: RF=3, min.isr=2 -> can lose 1 broker
- unclean.leader.election: Allow out-of-sync replica to become leader?
- Dev vs Prod settings: RF=1 (dev) vs RF=3 (prod)
- Strimzi configuration for these settings
- AI Collaboration: Analyze cluster config for reliability gaps
- "Try With AI" prompts (3)

**Dependencies**: Lessons 4, 6

---

## Part D: Data Pipelines (Lessons 14-15, Layer L2)

### Lesson 14: Kafka Connect - Building Data Pipelines

**File**: `14-kafka-connect-pipelines.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 50 minutes

**Key Concepts from Expertise Skill**:
- Kafka Connect architecture
- Source connectors vs Sink connectors
- Connect REST API
- KafkaConnect CRD with Strimzi
- When to use Connect vs custom client

**Learning Objectives**:
1. **Deploy** Kafka Connect using Strimzi KafkaConnect CRD (B1, Apply)
2. **Configure** a source connector to pull data into Kafka (B1, Apply)
3. **Decide** when Kafka Connect is appropriate vs writing a custom producer/consumer (B1, Evaluate)

**Content Outline**:
- What is Kafka Connect? Standardized data integration
- Source connectors: External system -> Kafka (e.g., file, database)
- Sink connectors: Kafka -> External system (e.g., Elasticsearch, S3)
- Strimzi KafkaConnect CRD: Deploy Connect workers
- Connector configuration: JSON REST API
- Example: File source connector
- Decision matrix: Connect vs custom client
- AI Collaboration: Design data pipeline architecture with AI
- "Try With AI" prompts (3)

**Dependencies**: Lesson 4

---

### Lesson 15: Change Data Capture with Debezium

**File**: `15-debezium-cdc.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 55 minutes

**Key Concepts from Expertise Skill**:
- Change Data Capture (CDC) concept
- Debezium PostgreSQL connector
- Database transaction log reading
- Outbox pattern for transactional atomicity
- Event schema from table structure

**Learning Objectives**:
1. **Explain** CDC advantages over polling for capturing database changes (B1, Understand)
2. **Deploy** Debezium PostgreSQL connector to capture table changes as Kafka events (B1, Apply)
3. **Implement** the outbox pattern to ensure database writes and event publishing are atomic (B1, Apply)

**Content Outline**:
- Problem: App writes to DB, then produces to Kafka - what if crash between?
- CDC: Read database transaction log, never miss a change
- Debezium: Best-in-class CDC for Kafka
- PostgreSQL WAL: How Debezium reads changes
- Outbox pattern: Write event to outbox table in same transaction as domain write
- Debezium reads outbox, produces to Kafka, deletes from outbox
- Strimzi KafkaConnector CRD for Debezium
- AI Collaboration: Design CDC pipeline with AI
- "Try With AI" prompts (3)

**Dependencies**: Lessons 4, 14, Part 6 Task API with database

---

## Part E: Agent Communication Patterns (Lessons 16-17, Layer L2)

### Lesson 16: Agent Event Patterns

**File**: `16-agent-event-patterns.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 50 minutes

**Key Concepts from Expertise Skill**:
- Task lifecycle events (task.created, task.updated, task.completed)
- Event naming conventions (domain.action)
- Notification fanout pattern
- Immutable audit log
- Correlation IDs and causation IDs

**Learning Objectives**:
1. **Design** event schemas for Task API lifecycle events with proper metadata (correlation_id, causation_id) (B1, Apply)
2. **Implement** notification fanout where multiple services consume the same event independently (B1, Apply)
3. **Build** an immutable audit log consumer that records all events for compliance (B1, Apply)

**Content Outline**:
- Event naming: domain.action (task.created, task.completed)
- Event schema: event_id, event_type, occurred_at, data, metadata
- Metadata: correlation_id (request trace), causation_id (what caused this event)
- Notification fanout: Email service, Slack service, mobile push - all consume task.completed
- Audit log: Append-only consumer, never deletes, compliance requirement
- Topic design: task-events (single) vs task-created, task-completed (per event)
- AI Collaboration: Design event schema with AI
- "Try With AI" prompts (3)

**Dependencies**: Lessons 7-9, Part 6 Task API

---

### Lesson 17: Saga Pattern for Multi-Step Workflows

**File**: `17-saga-pattern.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 55 minutes

**Key Concepts from Expertise Skill**:
- Saga pattern concept
- Choreography vs orchestration sagas
- Compensation events (undo actions)
- Implementing saga with Kafka events
- Saga state tracking

**Learning Objectives**:
1. **Explain** the saga pattern and when it applies to multi-service workflows (B1, Understand)
2. **Implement** a choreography-based saga using Kafka events between services (B1, Apply)
3. **Design** compensation events that undo partial work when a saga step fails (B1, Apply)

**Content Outline**:
- Scenario: Create task -> assign user -> notify -> schedule reminder
- Problem: What if notification fails after assignment?
- Saga pattern: Sequence of local transactions with compensations
- Choreography: Each service listens and acts, no central coordinator
- Orchestration: Central saga coordinator tells services what to do
- Compensation events: task.assignment.reversed, user.notification.cancelled
- Saga state machine: Track which steps completed
- AI Collaboration: Design saga compensation logic with AI
- "Try With AI" prompts (3)

**Dependencies**: Lesson 16

---

## Part F: Deployment and Operations (Lessons 18-19, Layer L2)

### Lesson 18: Production Kafka with Strimzi

**File**: `18-production-kafka-strimzi.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 50 minutes

**Key Concepts from Expertise Skill**:
- Multi-broker Kafka CRD configuration
- Resource limits and requests
- Persistent storage with PVCs
- TLS encryption (overview)
- Entity Operator for topic/user management

**Learning Objectives**:
1. **Configure** a multi-node Kafka cluster for production reliability (B1, Apply)
2. **Set** appropriate resource limits and persistent storage for Kafka brokers (B1, Apply)
3. **Manage** Kafka users and ACLs using KafkaUser CRDs (B1, Apply)

**Content Outline**:
- Dev vs Prod: Single node -> multi-node
- KafkaNodePool: Separate controller and broker roles (production)
- Persistent storage: PVC configuration
- Resource limits: CPU, memory sizing
- TLS: Listener configuration for encryption
- KafkaUser CRD: SCRAM-SHA-512 authentication
- ACLs: Topic-level permissions
- AI Collaboration: Review production config with AI
- "Try With AI" prompts (3)

**Dependencies**: Lesson 4

---

### Lesson 19: Monitoring and Debugging Kafka

**File**: `19-monitoring-debugging.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Bloom's Level**: Analyze
**Duration**: 50 minutes

**Key Concepts from Expertise Skill**:
- Consumer lag monitoring
- Under-replicated partitions
- Key broker metrics (request latency, disk usage)
- Kafka CLI tools for debugging
- Common error messages and fixes

**Learning Objectives**:
1. **Monitor** consumer lag to identify slow consumers before they cause data loss (B1, Apply)
2. **Diagnose** under-replicated partitions and determine root cause (B1, Analyze)
3. **Use** Kafka CLI tools to inspect topics, consumer groups, and offsets (B1, Apply)

**Content Outline**:
- Consumer lag: What it means, why it matters
- Monitoring consumer lag: kafka-consumer-groups.sh --describe
- Alert thresholds: When lag is a problem
- Under-replicated partitions: Broker down or slow
- Key metrics: request latency, disk usage, ISR shrink rate
- Kafka CLI toolkit: kafka-topics.sh, kafka-console-consumer.sh
- Common errors table from expertise skill
- AI Collaboration: Debug consumer lag with AI assistance
- "Try With AI" prompts (3)

**Dependencies**: Lessons 7-8, 13

---

## Part G: AI Collaboration and Capstone (Lessons 20-22)

### Lesson 20: AI-Assisted Kafka Development

**File**: `20-ai-assisted-kafka-development.md`
**Layer**: L2 (AI Collaboration - Deep)
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 45 minutes

**Key Concepts from Expertise Skill**:
- Using AI to debug Kafka issues
- AI-generated Avro schemas
- Configuration optimization with AI
- AI Three Roles for Kafka development

**Learning Objectives**:
1. **Apply** AI Three Roles (Teacher/Student/Co-Worker) to solve Kafka debugging challenges (B1, Apply)
2. **Generate** Avro schemas from domain requirements using AI collaboration (B1, Apply)
3. **Optimize** Kafka producer/consumer configuration with AI-assisted analysis (B1, Apply)

**Content Outline**:
- AI as Teacher: Learn optimal configuration patterns
- AI as Student: Refine AI suggestions for your production context
- AI as Co-Worker: Iterate on event schema design
- Practical exercise: Debug consumer lag scenario with AI
- Practical exercise: Generate Avro schema for new event type
- Practical exercise: Optimize producer throughput config
- Reflection: What did AI teach you? What did you teach AI?
- "Try With AI" prompts (3)

**Dependencies**: All previous lessons

---

### Lesson 21: Capstone - Event-Driven Agent Notifications

**File**: `21-capstone-event-driven-notifications.md`
**Layer**: L4 (Spec-Driven Capstone)
**Proficiency**: B1
**Bloom's Level**: Create
**Duration**: 90 minutes

**Key Concepts from Expertise Skill**:
- Full event-driven architecture implementation
- Task API event integration
- Notification service consumer
- Audit log consumer
- Schema Registry integration
- End-to-end testing

**Learning Objectives**:
1. **Write** a specification for event-driven notifications that includes intent, constraints, and success criteria (B1, Create)
2. **Implement** the specification by composing skills from previous lessons (producers, consumers, schemas) (B1, Create)
3. **Validate** the implementation against the specification with end-to-end tests (B1, Evaluate)

**Content Outline**:
- Phase 1: Write Specification (25 min)
  - Intent: Add event-driven notifications to Task API
  - Constraints: Use Avro schemas, at-least-once delivery, audit trail
  - Success criteria: Events published on task creation, notification service receives, audit logged
- Phase 2: Compose Skills (45 min)
  - Skill 1: Producer integration from Lesson 9
  - Skill 2: Schema design from Lesson 10
  - Skill 3: Consumer implementation from Lesson 16
  - AI orchestrates implementation from spec
- Phase 3: Validate (20 min)
  - Test: Create task, verify event published
  - Test: Verify notification consumer receives
  - Test: Verify audit log entry created
- "Try With AI" prompts (3)

**Dependencies**: All previous lessons

---

### Lesson 22: Building the Kafka Event Schema Skill

**File**: `22-kafka-event-schema-skill.md`
**Layer**: L3 (Intelligence Design - Skill Creation)
**Proficiency**: B1
**Bloom's Level**: Create
**Duration**: 60 minutes

**Key Concepts from Expertise Skill**:
- Reusable skill design
- Persona + Questions + Principles pattern
- Event schema design patterns
- Topic naming conventions
- Schema evolution strategies

**Learning Objectives**:
1. **Extract** reusable event schema design patterns from chapter learnings into a skill specification (B1, Create)
2. **Design** a skill with clear persona, triggering questions, and decision principles (B1, Create)
3. **Test** the skill on a novel domain (non-Task API) to verify reusability (B1, Evaluate)

**Content Outline**:
- What is a skill? Reusable intelligence for future projects
- Skill structure: Persona, When to Use, Principles, Decision Logic
- Extracting patterns from Chapter 52:
  - Event naming: domain.action
  - Schema fields: event_id, event_type, occurred_at, data, metadata
  - Evolution strategy: backward compatible only
  - Topic design: single vs per-event-type
- Writing the skill YAML frontmatter
- Testing on new domain: e-commerce order events
- Integrating skill into Claude Code
- "Try With AI" prompts (3)

**Dependencies**: All previous lessons, especially Lessons 10, 16

---

## Summary Tables

### Lessons by Layer

| Layer | Lessons | Count |
|-------|---------|-------|
| L1 (Manual) | 1, 2, 3, 4, 5 | 5 |
| L1->L2 (Transition) | 7 | 1 |
| L2 (AI Collaboration) | 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 | 14 |
| L3 (Intelligence Design) | 22 | 1 |
| L4 (Spec-Driven Capstone) | 21 | 1 |

### Lessons by Bloom's Level

| Bloom's Level | Lessons | Count |
|---------------|---------|-------|
| Understand | 1, 2, 3 | 3 |
| Apply | 4, 5, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20 | 15 |
| Analyze | 8, 11 | 2 |
| Evaluate | (integrated into Apply lessons) | - |
| Create | 21, 22 | 2 |

### Proficiency Levels

All lessons at **B1 (Intermediate)** per spec. This is appropriate for Part 7 (Cloud Native) where students have completed Parts 1-6 fundamentals.

### Duration Summary

| Part | Lessons | Total Minutes |
|------|---------|---------------|
| A: Foundations | 1-3 | 130 |
| B: Kafka Core | 4-8 | 240 |
| C: Production | 9-13 | 245 |
| D: Pipelines | 14-15 | 105 |
| E: Agent Patterns | 16-17 | 105 |
| F: Operations | 18-19 | 100 |
| G: Capstone | 20-22 | 195 |
| **Total** | 22 | **1120 min (~19 hours)** |

---

## Dependency Graph

```
Lesson 1
    └── Lesson 2
        └── Lesson 3
            └── Lesson 4 (+ Ch 49-51)
                ├── Lesson 5
                │   └── Lesson 6
                │       └── Lesson 11
                │           └── Lesson 12
                │       └── Lesson 13
                ├── Lesson 7
                │   └── Lesson 8
                │       └── Lesson 19
                └── Lesson 14
                    └── Lesson 15 (+ Part 6 DB)

Lessons 5-8 + Part 6 Task API
    └── Lesson 9
        └── Lesson 10
            └── Lesson 22

Lessons 7-9 + Part 6
    └── Lesson 16
        └── Lesson 17

Lesson 4
    └── Lesson 18

All Lessons
    └── Lesson 20
        └── Lesson 21
            └── Lesson 22
```

---

## Implementation Checklist

For each lesson, implementer must:

- [ ] Include full YAML frontmatter (sidebar_position, title, description, keywords, skills, learning_objectives, cognitive_load, differentiation)
- [ ] Write compelling narrative opening (2-3 paragraphs before first section)
- [ ] Include key concepts from expertise skill
- [ ] Create 3 "Try With AI" prompts with learning explanations
- [ ] Add code examples with type hints (confluent-kafka patterns)
- [ ] Include comparison tables where appropriate
- [ ] Link to Task API from Part 6 where relevant
- [ ] Verify all Strimzi/Kafka commands work on Docker Desktop K8s
- [ ] Test code examples before inclusion
