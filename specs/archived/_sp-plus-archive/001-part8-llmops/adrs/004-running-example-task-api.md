# ADR-004: Task API as Running Example for Part 8

**Status**: Accepted
**Date**: 2026-01-01
**Decision Makers**: Course architects

## Context

The book uses a **unified running example** across parts for continuity:

| Part | Example | Application |
|------|---------|-------------|
| Part 5 | `Task` class (OOP) | Python fundamentals |
| Part 6 Ch40 | Task API (FastAPI + SQLModel) | Agent backends |
| Part 7 Ch49 | Containerized Task API | Docker deployment |
| Part 7 Ch50 | Task API on Kubernetes | K8s orchestration |

Part 8 needs a domain for fine-tuning examples. Options considered:
1. Generic "chatbot" (overused, not distinctive)
2. New domain (breaks continuity)
3. Task API domain (extends existing example)

## Decision

**Use Task API domain as the running example for Part 8 fine-tuning.**

### What This Means

Students will fine-tune models to be "Task Management Experts":
- Understand task prioritization
- Generate task descriptions
- Parse natural language into task structures
- Suggest task organization strategies

### Implementation Across Chapters

| Chapter | Application |
|---------|-------------|
| **Ch 63** | Generate synthetic Task management Q&A dataset |
| **Ch 64** | Fine-tune on Task domain instructions |
| **Ch 65** | Create "TaskBot" persona (professional productivity assistant) |
| **Ch 66** | Train JSON tool-calling for Task API endpoints |
| **Ch 68** | Align for safe task suggestions (no harmful recommendations) |
| **Ch 71** | Deploy as Task API agent backend |
| **Ch 72** | Capstone: Full TaskBot Digital FTE |

### Example Dataset Entries

```json
{"instruction": "Create a task for reviewing the quarterly report", "output": "Title: Review Q4 Report\nPriority: High\nDue: End of week\nDescription: Analyze revenue trends, compare to projections, prepare executive summary."}

{"instruction": "I need to remember to call mom on Sunday", "output": "Title: Call Mom\nPriority: Medium\nDue: Sunday\nDescription: Weekly check-in call with mom."}

{"instruction": "What tasks should I prioritize this week?", "output": "Based on your task list, I recommend prioritizing: 1) High-priority deadline tasks, 2) Dependencies blocking other work, 3) Quick wins under 30 minutes."}
```

## Consequences

### Positive

- Seamless continuity from Parts 6-7
- Students already understand the domain
- Practical: Task management is relatable, not toy example
- Agent integration clear: TaskBot + Task API = complete system

### Negative

- Task domain may feel limiting for some students
- Some students may want more exciting domain (medical, legal, finance)
- Task management fine-tuning is simpler than domain-specific expertise

### Mitigations

- Capstone allows students to apply patterns to their own domain
- Lessons teach transferable patterns, not Task-specific tricks
- "Try With AI" sections encourage domain experimentation

## References

- Part 6 Ch40: Task API implementation
- Part 7 Ch49-51: Task API containerization and deployment
- CLAUDE.md: "Use `task-api` consistently (NOT `ai-agent`)"
