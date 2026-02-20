---
id: "001"
title: "Research-First Chapter 08a Creation (Phase A-B)"
stage: "spec"
date_iso: "2026-02-06"
surface: "agent"
model: "claude-haiku-4-5-20251001"
feature: "chapter-08a-sql-neon"
branch: "main"
user: "AmmarAamir786"
command: "/sp.chapter Chapter 08a: SQL & Neon PostgreSQL with Python"
labels:
  - "chapter-08a"
  - "sqlalchemy"
  - "neon-postgresql"
  - "research-first"
  - "skill-first-pattern"
  - "part-2"
links:
  spec: "specs/chapter-08a-sql-neon/spec.md"
  plan: "specs/chapter-08a-sql-neon/plan.md"
  tasks: "specs/chapter-08a-sql-neon/tasks.md"
  skill: ".claude/skills/building-with-sqlalchemy-orm/SKILL.md"
  adr: null
  ticket: null
  pr: null
files_yaml:
  - ".claude/skills/building-with-sqlalchemy-orm/SKILL.md"
  - ".claude/skills/building-with-sqlalchemy-orm/references/api-patterns.md"
  - ".claude/skills/building-with-sqlalchemy-orm/references/neon-setup.md"
  - ".claude/skills/building-with-sqlalchemy-orm/references/transactions.md"
  - ".claude/skills/building-with-sqlalchemy-orm/references/budget-tracker-complete.py"
  - "specs/chapter-08a-sql-neon/spec.md"
  - "specs/chapter-08a-sql-neon/plan.md"
  - "specs/chapter-08a-sql-neon/tasks.md"
tests_yaml: []
---

# Research-First Chapter 08a Creation (Phase A-B)

## Context

Creating Chapter 08a: "SQL & Neon PostgreSQL with Python" as a new chapter in Part 2 (Agent Workflow Primitives), positioned between Chapter 8 (Computation & Data Extraction) and Chapter 9 (Data Analysis & Financial Modeling).

**User Input**:

- Framework: SQLAlchemy ORM 2.0+ + Neon PostgreSQL serverless
- Running example: Budget Tracker (expense management with categories)
- Proficiency: A1-A2 (beginner students)
- Position: Bridge from CSV files → Databases → Multi-source platforms
- Approach: Skill-first pattern (students own reusable `/database-deployment` skill)

## Execution Summary

### Phase A: Expertise Skill Creation

**Goal**: Build production-grade expertise skill BEFORE writing content (prevents hallucinations)

**Research Method**:

1. WebSearch: SQLAlchemy ORM 2024-2025 tutorials, Neon PostgreSQL serverless, best practices
2. Skill Creator Pro: Generated `building-with-sqlalchemy-orm` skill with:
   - Persona: Python database architect with production experience
   - Core concepts: 5 foundational patterns (Models, Sessions, Relationships, Queries, Neon)
   - Decision logic table: When to use what pattern
   - Complete workflow: 6-step Budget Tracker build
   - MCP integration section
   - Safety guardrails (NEVER/ALWAYS rules)
   - Troubleshooting guide

**Skill Components Created**:

```
.claude/skills/building-with-sqlalchemy-orm/
├── SKILL.md (381 lines - under 500 limit)
├── references/
│   ├── api-patterns.md (Official SQLAlchemy CRUD patterns)
│   ├── neon-setup.md (Serverless PostgreSQL specifics)
│   ├── transactions.md (Session handling, atomicity)
│   └── budget-tracker-complete.py (450+ lines working example)
```

**Quality Assurance**: All patterns verified against official docs, no hallucinations.

---

### Phase B: Specification, Planning, Tasks

#### Step B.1: Specification

**Artifact**: `specs/chapter-08a-sql-neon/spec.md` (420 lines)

**Content**:

- Compelling hook: Why databases matter (CSV limitations)
- 8-lesson structure (L0 skill-first + L1-L7 content)
- Learning outcomes: Bloom's L1-L4, CEFR A1-A2
- Prerequisites: What students know from Ch 3, 7, 8
- Success criteria: 5 measurable outcomes
- Acceptance scenarios: 5 student workflows
- Edge cases: 5 identified with solutions
- Layer progression: L1 (Manual) → L2 (Collaboration) → L3 (Skill) → L4 (Optional)
- Seven Principles mapping
- Expertise skill reference

**Key Design Decisions**:

- Budget Tracker as THE running example (coherence across all 8 lessons)
- Neon specifically (free, serverless, teaches scaling)
- SQLAlchemy ORM (teaches "code as interface" Principle 2)
- No database migrations (save for Part 7)
- Three Roles framework in L4-L6 (AI collaboration layers)

#### Step B.2: Clarification

**Process**: Structured ambiguity scan across 9 taxonomy categories

**Coverage Assessment**:

- Functional Scope & Behavior: **Clear**
- User Goals & Success Criteria: **Clear**
- Layer Progression: **Clear**
- Data Model: **Clear**
- Edge Cases: **Clear**
- Constraints: **Clear**
- Terminology: **Clear**
- Non-Functional: **Clear**
- Integration Dependencies: **Clear**

**Result**: No critical ambiguities found. Spec was already comprehensive (informed by Phase A expertise skill).

#### Step B.3: Planning

**Artifact**: `specs/chapter-08a-sql-neon/plan.md` (806 lines)

**Content**:

- Lesson-by-lesson breakdown (8 lessons with layer, duration, objectives)
- Layer progression analysis (L1→L2→L3→L4)
- Cognitive load assessment (A1-A2 validation, ≤6 new concepts per lesson)
- Content dependencies and ordering
- "Try With AI" strategy (3 prompts/lesson × 8 = 24 total)
- Activity/exercise progression (builds toward capstone)
- Assessment points (8 checkpoints, one per lesson)
- Quality reference (matched to Chapter 8)

**Pedagogical Arc**:

- L0: Skill ownership (meta-learning)
- L1: Foundation (why databases, concepts)
- L2: Building (CRUD operations, basic queries)
- L3: Integration (relationships, joins)
- L4: Safety (transactions, atomicity, error handling)
- L5: Deployment (Neon connection, pooling)
- L6: Mastery (capstone multi-table queries, reporting)
- L7: Ownership (students improve their `/database-deployment` skill throughout)

#### Step B.4: Task Generation

**Artifact**: `specs/chapter-08a-sql-neon/tasks.md` (380 lines)

**Task Structure** (12 total):

- **Phase 1**: 1 task (README)
- **Phase 2**: 8 tasks (L0-L7 content lessons, sequential)
- **Phase 3**: 3 tasks (Validation gates + assessment)

**Task Features**:

- Each lesson task includes subagent requirements (content-implementer)
- Each lesson includes validation gate (educational-validator)
- Skills embedded (learning-objectives, exercise-designer, ai-collaborate-teaching for L4-L6)
- Absolute paths specified (no relative paths)
- Clear acceptance criteria per task
- Dependency graph shows sequential execution
- Quality reference lessons provided for each lesson

**Critical Path**: L0 → L7 (sequential, pedagogically ordered)

**Parallelizable After All Content Exists**: README + validators can run in parallel

---

## Deliverables

### Expertise Skill

- **Path**: `.claude/skills/building-with-sqlalchemy-orm/`
- **Files**: SKILL.md + 4 reference documents + complete working example
- **Purpose**: Source of truth for all chapter code examples
- **Status**: ✅ Production-ready, verified against official docs

### Specification

- **Path**: `specs/chapter-08a-sql-neon/spec.md`
- **Lines**: 420
- **Status**: ✅ Complete, no clarifications needed

### Implementation Plan

- **Path**: `specs/chapter-08a-sql-neon/plan.md`
- **Lines**: 806
- **Status**: ✅ Complete, pedagogical arc designed

### Task Breakdown

- **Path**: `specs/chapter-08a-sql-neon/tasks.md`
- **Lines**: 380
- **Tasks**: 12 (1 README + 8 lessons + 3 validation)
- **Status**: ✅ Ready for implementation

---

## Key Decisions & Rationale

| Decision                 | Rationale                                                  | Alternative Considered                                  |
| ------------------------ | ---------------------------------------------------------- | ------------------------------------------------------- |
| **Skill-first approach** | Prevents hallucinations; gives students reusable asset     | Direct content writing (rejected: no quality guarantee) |
| **SQLAlchemy ORM**       | Teaches "code as interface"; less error-prone than raw SQL | Raw SQL (more control but steeper learning curve)       |
| **Neon PostgreSQL**      | Free, zero setup, serverless, teaches modern concepts      | Local PostgreSQL (no cloud concepts), traditional RDS   |
| **Budget Tracker**       | Coherent running example across all 8 lessons              | Multiple examples (harder to follow, less cohesive)     |
| **L0 Skill-First**       | Mandatory first lesson; students own knowledge asset       | Skip (loses ownership model; less transformative)       |
| **Three Roles L4-L6**    | Explicit AI collaboration framework; pedagogically sound   | Direct instruction (misses collaboration layer)         |
| **No migrations**        | Scope for fundamentals; migrations are Part 7 topic        | Include Alembic (adds complexity, not needed for L1-L2) |

---

## Quality Validation

**Specification Quality**:

- ✅ No [NEEDS CLARIFICATION] markers
- ✅ Assumptions documented and reasonable
- ✅ Learning outcomes measurable
- ✅ Success criteria testable
- ✅ Edge cases identified
- ✅ Seven Principles mapped

**Planning Quality**:

- ✅ Layer progression validated (L1→L4)
- ✅ Cognitive load assessed (A1-A2 appropriate)
- ✅ Pedagogical arc coherent
- ✅ Content dependencies clear
- ✅ Assessment points distributed

**Task Quality**:

- ✅ Each task is autonomous (can be assigned independently)
- ✅ Acceptance criteria are measurable
- ✅ Subagent requirements embedded
- ✅ Quality gates specified
- ✅ Dependency graph prevents invalid orderings

---

## Risk Assessment

| Risk                           | Probability | Impact | Mitigation                                     |
| ------------------------------ | ----------- | ------ | ---------------------------------------------- |
| **Hallucinated APIs**          | Low         | High   | Expertise skill verified against official docs |
| **Pedagogical overload**       | Low         | Medium | Cognitive load assessment per lesson           |
| **Budget Tracker incoherence** | Very Low    | Medium | Single running example throughout              |
| **Neon setup issues**          | Low         | Low    | Troubleshooting section, debugging checklist   |
| **Three Roles confusion**      | Low         | Medium | Explicit framework in L4-L6, clear prompts     |

---

## Next Steps

**Phase B.5-B.11**: Implementation & Validation

1. Invoke content-implementer subagent for each lesson (L0-L7)
2. Run educational-validator after each lesson (BLOCKING gate)
3. Create README (T08a.README)
4. Run all validators in parallel (educational, factual, pedagogical)
5. Create chapter quiz (T08a.ASSESSMENT)
6. Merge to main branch

**Timeline**: Implementation ready to begin; no blocking dependencies.

---

## Lessons Learned

1. **Skill-first prevents hallucinations**: Having expertise skill as source of truth ensures accuracy
2. **Comprehensive spec avoids rework**: Clear spec → clear plan → clear tasks (minimal rewrites)
3. **Pedagogy-first design**: Layer progression, cognitive load, Three Roles shape better content than generic instruction
4. **Budget Tracker coherence**: Single running example creates stronger learning trajectory than scattered examples

---

## Files Modified/Created

**Skill Files**:

- `.claude/skills/building-with-sqlalchemy-orm/SKILL.md`
- `.claude/skills/building-with-sqlalchemy-orm/references/api-patterns.md`
- `.claude/skills/building-with-sqlalchemy-orm/references/neon-setup.md`
- `.claude/skills/building-with-sqlalchemy-orm/references/transactions.md`
- `.claude/skills/building-with-sqlalchemy-orm/references/budget-tracker-complete.py`

**Specification Files**:

- `specs/chapter-08a-sql-neon/spec.md`
- `specs/chapter-08a-sql-neon/plan.md`
- `specs/chapter-08a-sql-neon/tasks.md`

**Documentation**:

- `history/prompts/chapter-08a-sql-neon/001-research-first-chapter-creation.spec.prompt.md` (this file)

---

## Metrics

| Metric                  | Value                                            |
| ----------------------- | ------------------------------------------------ |
| **Skill creation time** | 1 research phase + 5 reference documents         |
| **Spec completeness**   | 420 lines, 0 clarifications needed               |
| **Plan detail**         | 806 lines, 8 lessons, layer progression defined  |
| **Task granularity**    | 12 tasks, each <2 hours estimated effort         |
| **Code examples**       | 450+ line working Budget Tracker                 |
| **Quality gates**       | 3 validators (educational, factual, pedagogical) |
| **Total artifacts**     | 1,606 lines across spec + plan + tasks           |

---

**Status**: ✅ Research-first chapter creation complete. Ready for implementation.

**Phase**: Specification (B.1-B.4 complete; B.5+ pending)

**Created**: 2026-02-06

**Contributor**: Claude Haiku 4.5 (Agent)
