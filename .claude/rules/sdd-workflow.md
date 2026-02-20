# Spec-Driven Development Workflow

**The Four-Phase SDD Workflow** — front-load thinking so implementation becomes execution.

## Phase 1: Research (Parallel Subagents)

**Deliverable**: Written research summaries in `specs/<feature>/research/`

```
Spawn parallel subagents to investigate:
- Reference implementations
- Existing codebase patterns
- Best practices for this domain
```

## Phase 2: Specification (Written Artifact)

**Deliverable**: `specs/<feature>/spec.md`

Contains:

- What you're building and why
- Patterns discovered in research
- How this fits existing architecture
- Implementation approach with phases
- Explicit constraints (what NOT to build)
- Measurable success criteria

**Why written matters**: The spec becomes your **source of truth** that survives session restarts.

## Phase 3: Refinement (Interview)

**Deliverable**: Updated spec with ambiguities resolved

Use AskUserQuestion to surface design decisions:

- "Should we migrate existing data or start fresh?"
- "The research found two patterns. Which matches your constraints?"

## Phase 4: Implementation (Task Delegation)

**Deliverable**: Working code committed in atomic chunks

```
Implement @specs/<feature>/spec.md
Use the task tool and each task should only be done by a subagent
so that context is clear. After each task do a commit before you continue.
You are the main agent and your subagents are your devs.
```

---

## Artifact Structure (specs/<feature>/)

**All SDD artifacts live together per feature:**

```
specs/<feature>/
├── spec.md        # Specification (source of truth)
├── plan.md        # Implementation plan (from Plan Mode)
├── tasks.md       # Task breakdown
├── progress.md    # Session progress tracking
├── research/      # Research findings from Phase 1
│   ├── codebase-analysis.md
│   └── best-practices.md
├── notes/         # Subagent observations and decisions
│   └── <date>-<topic>.md
└── adrs/          # Architecture Decision Records
    └── 001-why-fastapi.md
```

**Key principle**: One folder = one feature = all context. Nothing scattered elsewhere.

## Progress Tracking (progress.md)

```markdown
# Feature: <feature-name>

## Current Phase

[Research | Specification | Refinement | Implementation]

## Session Log

| Date       | Phase          | Work Done          | Next Steps |
| ---------- | -------------- | ------------------ | ---------- |
| 2026-02-04 | Implementation | Tasks 1-5 complete | Tasks 6-8  |

## Blocked Items

- [Item]: [Reason] → [Who can unblock]

## Task Status

- [x] Task 1: Schema definition
- [x] Task 2: API endpoints
- [ ] Task 3: Tests
```

## When to Create specs/<feature>/

- Any work spanning multiple sessions
- Features with 5+ implementation items
- Content chapters (lessons as tasks)
- Anything needing rollback boundaries

---

## SpecKit Commands (Active)

| Command             | Purpose                              | When to Use            |
| ------------------- | ------------------------------------ | ---------------------- |
| `/sp.specify`       | Create/update feature specifications | Starting new features  |
| `/sp.git.commit_pr` | Autonomous git workflows             | Committing and PRs     |
| `/sp.phr`           | Record prompt history                | After significant work |
| `/sp.constitution`  | Update constitution                  | Governance changes     |
| `/sp.chapter`       | Research-first chapter creation      | New technical chapters |

### Deprecated (Use Native Features)

| Deprecated          | Replacement                                         |
| ------------------- | --------------------------------------------------- |
| `/sp.plan`          | Use native Plan Mode (EnterPlanMode tool)           |
| `/sp.tasks`         | Use native Tasks (TaskCreate, TaskList, TaskUpdate) |
| `/sp.implement`     | Use Ch5 L7 pattern with subagents                   |
| `/sp.analyze`       | Use Grep/Glob directly                              |
| `/sp.taskstoissues` | Only if GitHub integration needed                   |

**Why deprecated**: These duplicate native Claude Code capabilities. Use native features for better integration.
