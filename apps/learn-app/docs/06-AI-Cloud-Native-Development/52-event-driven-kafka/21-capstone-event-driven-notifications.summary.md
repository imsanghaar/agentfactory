### Core Concept
Build a complete event-driven notification system using spec-driven development: write specification first with clear intent, constraints, and success criteria, then implement by composing patterns from previous lessons.

### Key Mental Models
- **Spec-driven development**: Specification defines what "done" looks like before writing code - enables focused implementation and clear validation
- **Compose, don't recreate**: Capstone applies patterns from lessons 5-20 (producers, consumers, schemas, reliability) rather than learning new concepts
- **Success criteria as checkboxes**: Each criterion is verifiable ("event includes event_id, event_type, occurred_at") not vague ("system works well")
- **Three-phase approach**: Phase 1 (Specification) -> Phase 2 (Implementation) -> Phase 3 (Validation against spec)

### Critical Patterns
- Specification structure: Intent (business value), Constraints (technical/operational bounds), Success Criteria (verifiable), Non-Goals (scope boundaries), Architecture (component diagram)
- Event schema with factory methods: `TaskEvent.task_created()`, `TaskEvent.task_completed()` for type-safe event creation
- Publisher with lifespan management: Initialize in FastAPI lifespan, flush on shutdown
- Notification service: Separate consumer group, filters by event_type, manual commit after processing
- Audit service: Separate consumer group, logs ALL events, deduplicates by event_id, append-only storage

### AI Collaboration Keys
- Use AI to add Schema Registry integration with Avro after JSON implementation works
- Ask AI to implement dead letter queue pattern for handling processing failures
- Leverage AI to review and improve specification for edge cases, monitoring requirements, and automated testing

### Common Mistakes
- Starting implementation without written specification, leading to scope creep and unclear completion criteria
- Not validating each success criterion with actual evidence (curl commands, log output, file contents)
- Forgetting to commit consumer offsets, causing duplicate processing on service restart

### Connections
- **Builds on**: All lessons 1-20 (producers, consumers, schemas, reliability, patterns)
- **Leads to**: Chapter 53 (Dapr) - abstracting pub/sub behind portable APIs using concepts learned here
