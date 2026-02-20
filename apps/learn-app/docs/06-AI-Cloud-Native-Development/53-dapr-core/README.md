---
sidebar_position: 53
title: "Chapter 53: Dapr Core - Sidecar Building Blocks"
description: "Simplify distributed AI agent systems with Dapr's portable building blocks for state, pub/sub, service invocation, and more"
keywords:
  [
    dapr,
    sidecar,
    building blocks,
    kubernetes,
    microservices,
    state management,
    pubsub,
    service invocation,
  ]
---

# Chapter 53: Dapr Core - Sidecar Building Blocks

Dapr abstracts infrastructure behind portable HTTP/gRPC APIs. You build the `dapr-deployment` skill, deploy Dapr to Kubernetes, and refactor the Part 6 Task API to use Dapr building blocks instead of direct clients.

---

## Goals

- Understand the Dapr sidecar architecture and components
- Deploy Dapr to Kubernetes via Helm
- Use Dapr building blocks: state, pub/sub, service invocation, bindings, jobs, secrets, config
- Swap infrastructure backends by updating component YAML instead of code
- Capture the patterns in a reusable Dapr skill

---

## Lesson Progression

| Lesson  | Focus                                                                   |
| ------- | ----------------------------------------------------------------------- |
| L00     | Build Your Dapr Skill (skill-first)                                     |
| L01-L02 | Sidecar pattern, building blocks, components                            |
| L03-L08 | Deploy Dapr; state, invocation, pub/sub, bindings, jobs, secrets/config |
| L09     | Capstone: Dapr-enabled Task API                                         |
| L10     | Finalize the Dapr skill                                                 |

Each lesson ends with a reflection to test, find gaps, and improve the skill.

---

## Outcome & Method

You finish with the Task API running through Dapr (state, pub/sub, invocation, bindings, jobs, secrets) plus a Dapr deployment skill. The chapter uses the 4-Layer approach: concepts → collaboration on components → spec-driven capstone → skill finalization.

---

## Prerequisites

- Chapter 3 skills tooling
- Chapters 49-51 (Docker, Kubernetes, Helm)
- Chapter 52 (Kafka mental model for pub/sub abstraction)
- Part 6 Task API (async FastAPI)

## Technology Stack

- **Dapr**: 1.14+ (latest stable)
- **Python SDK**: `dapr-client`, `dapr-ext-fastapi`
- **State Store**: Redis (simple, familiar pattern)
- **Pub/Sub**: Redis (simpler than Kafka for learning Dapr)
- **Platform**: Docker Desktop Kubernetes
- **Helm**: For Dapr control plane deployment

## Looking Ahead

This chapter covers Dapr's **core building blocks**. Chapter 59 adds **stateful patterns**:

- **Dapr Actors** for agent state management
- **Dapr Workflows** for long-running orchestration
- **Virtual actors pattern** for distributed agent systems

## Skill-First Learning

This chapter follows the **Skill-First Learning Pattern**:

1. **L00**: Build your `dapr-deployment` skill FIRST using official docs
2. **L01-L08**: Learn each building block while improving your skill
3. **L09**: Apply everything in a real capstone project
4. **L10**: Finalize your skill as a sellable Digital FTE component

Every lesson (L01-L09) ends with a "Reflect on Your Skill" section where you update your skill based on what you learned.
