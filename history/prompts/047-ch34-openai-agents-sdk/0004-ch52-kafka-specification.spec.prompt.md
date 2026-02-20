---
id: "0004"
title: ch52-kafka-specification
stage: spec
date: 2025-12-28
surface: claude-code
model: opus-4
feature: 004-ch52-event-driven-kafka
branch: main
user: mjs
command: /sp.specify
labels: [chapter, kafka, event-driven, part7]
links:
  spec: specs/004-ch52-event-driven-kafka/spec.md
  ticket:
  adr:
  pr:
files:
  - specs/004-ch52-event-driven-kafka/spec.md
  - specs/004-ch52-event-driven-kafka/checklists/requirements.md
tests:

---

## Prompt

Create specification for Chapter 52: Event-Driven Architecture with Kafka. Context includes 22-lesson structure from existing README, Strimzi operator for Kubernetes, KRaft mode (no ZooKeeper), confluent-kafka-python, Task API running example from Part 6, B1 proficiency level.

## Response snapshot

Created comprehensive specification with:
- 8 user stories covering EDA concepts, Kafka deployment, producer/consumer patterns, FastAPI integration, schema evolution, exactly-once semantics, CDC, and capstone
- 12 functional requirements covering lesson count, technology choices, layer progression
- 8 success criteria measuring student outcomes
- Assumed knowledge and prerequisites documented
- Edge cases identified for production scenarios

## Outcome

- ✅ Impact: Specification provides clear requirements for 22-lesson Kafka chapter
- 🧪 Tests: N/A (spec phase)
- 📁 Files: spec.md, checklists/requirements.md
- 🔁 Next prompts: /sp.plan for implementation planning
- 🧠 Reflection: Used existing README structure as foundation, added testable acceptance scenarios

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All checklist items PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
