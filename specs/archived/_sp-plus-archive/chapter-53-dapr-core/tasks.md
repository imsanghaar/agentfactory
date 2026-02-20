# Chapter 53: Dapr Core — Task List

**Generated**: 2025-12-29
**Source Spec**: specs/chapter-53-dapr-core/spec.md
**Source Plan**: specs/chapter-53-dapr-core/plan.md
**Output Directory**: apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/

---

## Phase 1: Setup

- [x] T53.SETUP Create chapter directory structure
- [x] T53.README Update README.md to match spec structure

---

## Phase 2: Lesson Implementation

### L00: Build Your Dapr Skill (Layer 3 - Skill-First)

- [x] T53.L00 Create lesson: Build Your Dapr Skill
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/00-build-your-dapr-skill.md
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/00-build-your-kafka-skill.md
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, exercise-designer
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
    - 3 "Try With AI" prompts with explanations
    - Evidence blocks for all code
    - Duration: 25 minutes
    - No "Reflect on Your Skill" (this IS the skill building lesson)

### L01: The Sidecar Pattern (Layer 1 - Conceptual)

- [x] T53.L01 Create lesson: The Sidecar Pattern
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/01-sidecar-pattern.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/01-eda-foundations.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Architecture diagram (sidecar + app container)
    - Ends with "Reflect on Your Skill" section
    - NO sections after "Try With AI"
    - Duration: 20 minutes

### L02: Building Blocks and Components (Layer 1 - Conceptual)

- [x] T53.L02 Create lesson: Building Blocks and Components
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/02-building-blocks-components.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/02-kafka-architecture.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Building blocks table
    - Component YAML anatomy
    - Ends with "Reflect on Your Skill" section
    - NO sections after "Try With AI"
    - Duration: 20 minutes

### L03: Deploy Dapr + State Management (Layer 2 - Collaboration)

- [x] T53.L03 Create lesson: Deploy Dapr + State Management
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/03-deploy-dapr-state-management.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/03-strimzi-operator-helm.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Evidence blocks for all code (Helm, YAML, Python)
    - Three Roles demonstrations (invisible framework)
    - Simple Todo example (NOT Task API)
    - Async DaprClient patterns
    - Ends with "Reflect on Your Skill" section
    - NO sections after "Try With AI"
    - Duration: 35 minutes

### L04: Service Invocation (Layer 2 - Collaboration)

- [x] T53.L04 Create lesson: Service Invocation
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/04-service-invocation.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/05-producers-schema-registry.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Evidence blocks for all code
    - Three Roles demonstrations (invisible framework)
    - Simple Todo context
    - Async invoke_method patterns
    - Ends with "Reflect on Your Skill" section
    - NO sections after "Try With AI"
    - Duration: 25 minutes

### L05: Pub/Sub Messaging (Layer 2 - Collaboration)

- [x] T53.L05 Create lesson: Pub/Sub Messaging
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/05-pubsub-messaging.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/06-consumer-groups-patterns.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Evidence blocks for all code
    - Three Roles demonstrations (invisible framework)
    - Redis pub/sub component + Kafka swap example
    - dapr-ext-fastapi subscription patterns
    - Connection to Ch52 Kafka knowledge
    - Ends with "Reflect on Your Skill" section
    - NO sections after "Try With AI"
    - Duration: 30 minutes

### L06: Bindings and Triggers (Layer 2 - Collaboration)

- [x] T53.L06 Create lesson: Bindings and Triggers
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/06-bindings-triggers.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/07-exactly-once-transactions.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Evidence blocks for all code
    - Three Roles demonstrations (invisible framework)
    - Cron input binding example
    - HTTP output binding example
    - Bindings vs pub/sub distinction
    - Ends with "Reflect on Your Skill" section
    - NO sections after "Try With AI"
    - Duration: 25 minutes

### L07: Jobs API: Scheduled Tasks (Layer 2 - Collaboration)

- [x] T53.L07 Create lesson: Jobs API: Scheduled Tasks
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/07-jobs-api.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/08-error-handling-dlq.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Evidence blocks for all code
    - Three Roles demonstrations (invisible framework)
    - Jobs API async patterns
    - Jobs vs Bindings comparison table
    - Ends with "Reflect on Your Skill" section
    - NO sections after "Try With AI"
    - Duration: 25 minutes

### L08: Secrets and Configuration (Layer 2 - Collaboration)

- [x] T53.L08 Create lesson: Secrets and Configuration
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/08-secrets-configuration.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/09-testing-observability.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Evidence blocks for all code
    - Three Roles demonstrations (invisible framework)
    - Kubernetes secrets store component
    - secretKeyRef in component YAML
    - Configuration API mention
    - Ends with "Reflect on Your Skill" section
    - NO sections after "Try With AI"
    - Duration: 25 minutes

### L09: Capstone: Dapr-Enabled Task API (Layer 4 - Integration)

- [x] T53.L09 Create lesson: Capstone: Dapr-Enabled Task API
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/09-capstone-dapr-task-api.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/21-event-driven-notification-service.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Evidence blocks for all code
    - Spec-driven approach (CAPSTONE-SPEC.md)
    - Full Task API with Dapr: state, pubsub, invoke, secrets, jobs
    - Kubernetes deployment with annotations
    - Verification steps (2/2 pod containers)
    - Ends with "Reflect on Your Skill" section
    - NO sections after "Try With AI"
    - Duration: 40 minutes

### L10: Finalize Your Dapr Skill (Layer 3 - Skill Finalization)

- [x] T53.L10 Create lesson: Finalize Your Dapr Skill
  - **SUBAGENT**: content-implementer
    - Output path: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/53-dapr-core/10-finalize-dapr-skill.md
    - Quality reference: /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/52-event-driven-kafka/22-finalize-your-kafka-skill.md
  - **ACCEPTANCE CRITERIA**:
    - Full YAML frontmatter
    - 3 "Try With AI" prompts with explanations
    - Safety guardrails (NEVER/ALWAYS lists)
    - Common errors table
    - Skill validation prompts
    - NO "Reflect on Your Skill" (this IS the skill lesson)
    - NO sections after "Try With AI"
    - Duration: 20 minutes

---

## Phase 3: Validation

- [x] T53.VALIDATE Run all validators
  - **VALIDATORS** (run in parallel):
    - educational-validator (constitutional compliance)
    - factual-verifier (verify all claims)
    - pedagogical-designer (learning progression)
  - **ACCEPTANCE CRITERIA**:
    - All lessons pass educational-validator
    - All factual claims verified
    - Learning progression validated

---

## Phase 4: Commit and PR

- [x] T53.COMMIT Create commit with all chapter content (5972ba87)
- [x] T53.PR Ready for pull request

---

## Summary

| Phase | Tasks | Status |
|-------|-------|--------|
| Setup | 2 | Complete |
| Lessons | 11 (L00-L10) | Complete |
| Validation | 1 | Complete |
| Commit/PR | 2 | Complete |
| **Total** | **16** | **16/16 Complete** |

---

## Implementation Notes

### Parallel Execution
- L00 must complete before L01-L10 (skill context needed)
- L01-L02 can run in parallel (both conceptual)
- L03-L08 should run sequentially (progressive building)
- L09 requires L03-L08 complete (uses all building blocks)
- L10 requires L09 complete (finalizes skill)

### Subagent Configuration
All content-implementer invocations MUST include:
- Absolute output path
- Quality reference lesson path
- Expertise skill reference: .claude/skills/building-with-dapr/SKILL.md
- Autonomous execution directive
- File verification after completion

### Content Quality Requirements
Every lesson MUST have:
1. Full YAML frontmatter with skills, learning_objectives, cognitive_load
2. Compelling narrative opening (2-3 paragraphs before first section)
3. 3 "Try With AI" prompts with "What you're learning:" explanations
4. Evidence blocks for all code examples
5. "Reflect on Your Skill" section (except L00 and L10)
6. NO sections after "Try With AI"
