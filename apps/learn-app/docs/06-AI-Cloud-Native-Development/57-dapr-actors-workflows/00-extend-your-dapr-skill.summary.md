### Core Concept
Extend your existing `dapr-deployment` skill to cover actors and workflows by grounding new patterns in official documentation before coding—so the skill can generate stateful actors and durable orchestrations accurately.

### Key Mental Models
- **Skill-first research**: Specify goals, fetch docs, then encode patterns to avoid hallucinated code.
- **Actors vs workflows**: Actors model stateful entities with identity and turn-based concurrency; workflows orchestrate long-running, multi-step processes with durability.
- **Determinism boundary**: Keep deterministic logic in workflows and push non-deterministic work to activities.

### Critical Patterns
- Write a LEARNING-SPEC outlining actor interfaces/implementations, reminders/timers, registration, and invocation via `ActorProxy`.
- Capture workflow patterns: `@workflow` functions yielding `call_activity`, retry policies, runtime registration, and client operations.
- Use `/fetching-library-docs` to pull authoritative SDK details before updating the skill.
- Validate the skill with targeted prompts (actor generation, workflow orchestration, decision guidance).

### Common Mistakes
- Extending skills from memory instead of official docs, leading to wrong imports or signatures.
- Mixing non-deterministic operations inside workflows rather than activities.
- Lacking clear success criteria, so the skill can’t be validated.

### Connections
- **Builds on**: Chapter 53 Dapr building blocks skill.
- **Leads to**: Actor and workflow implementation lessons across Chapter 57.
