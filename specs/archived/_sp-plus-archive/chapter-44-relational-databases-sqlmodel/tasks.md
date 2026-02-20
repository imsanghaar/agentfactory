# Tasks: Chapter 44 - Relational Databases for Agents with SQLModel

## Task Overview

| Task ID | Description | Output Path | Dependencies |
|---------|-------------|-------------|--------------|
| T44.README | Create chapter README | `.../44-relational-databases-sqlmodel/README.md` | None |
| T44.L00 | Create L00: Build Your Database Skill | `.../44-relational-databases-sqlmodel/00-build-your-database-skill.md` | T44.README |
| T44.L01 | Create L01: Why Agents Need Structured Data | `.../44-relational-databases-sqlmodel/01-why-agents-need-structured-data.md` | T44.L00 |
| T44.L02 | Create L02: SQLModel + Async Engine Setup | `.../44-relational-databases-sqlmodel/02-sqlmodel-async-engine-setup.md` | T44.L01 |
| T44.L03 | Create L03: Designing Agent Data Models | `.../44-relational-databases-sqlmodel/03-designing-agent-data-models.md` | T44.L02 |
| T44.L04 | Create L04: Async Session Management | `.../44-relational-databases-sqlmodel/04-async-session-management.md` | T44.L02 |
| T44.L05 | Create L05: CRUD Operations Pattern | `.../44-relational-databases-sqlmodel/05-crud-operations-pattern.md` | T44.L03, T44.L04 |
| T44.L06 | Create L06: Relationships and Eager Loading | `.../44-relational-databases-sqlmodel/06-relationships-and-eager-loading.md` | T44.L05 |
| T44.L07 | Create L07: Transactions and Error Handling | `.../44-relational-databases-sqlmodel/07-transactions-and-error-handling.md` | T44.L05 |
| T44.L08 | Create L08: Migrations with Alembic | `.../44-relational-databases-sqlmodel/08-migrations-with-alembic.md` | T44.L03 |
| T44.L09 | Create L09: Capstone | `.../44-relational-databases-sqlmodel/09-capstone-complete-database-layer.md` | All L00-L08 |
| T44.QUIZ | Create chapter quiz | `.../44-relational-databases-sqlmodel/10-chapter-quiz.md` | All lessons |
| T44.VALIDATE | Run all validators | N/A | All content |

---

## Detailed Tasks

### T44.README: Chapter README

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/README.md`

**Acceptance Criteria**:
- [ ] Chapter title and overview
- [ ] Learning outcomes (7 items)
- [ ] Lesson listing with durations
- [ ] Prerequisites noted
- [ ] Technology stack summary

---

### T44.L00: Build Your Database Skill

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/00-build-your-database-skill.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
- [ ] Narrative opening connecting to skill-first philosophy
- [ ] Step-by-step: Clone skills-lab, write LEARNING-SPEC, fetch docs, create skill
- [ ] 3 "Try With AI" prompts with "What you're learning" explanations
- [ ] "Reflect on Your Skill" section at end
- [ ] Evidence blocks for code examples
- [ ] NO sections after "Try With AI"

---

### T44.L01: Why Agents Need Structured Data

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/01-why-agents-need-structured-data.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Compelling narrative: Agent loses work on restart
- [ ] Comparison: Vector DB vs Relational DB use cases
- [ ] ACID properties explained simply
- [ ] Why async matters for agents
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] NO sections after "Try With AI"

---

### T44.L02: SQLModel + Async Engine Setup

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/02-sqlmodel-async-engine-setup.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Installation commands with evidence
- [ ] `create_async_engine` with all pooling params explained
- [ ] URL conversion pattern (postgresql:// → postgresql+asyncpg://)
- [ ] SQLite async for testing
- [ ] Table creation pattern
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] NO sections after "Try With AI"

---

### T44.L03: Designing Agent Data Models

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/03-designing-agent-data-models.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] `table=True` explained
- [ ] Field types and constraints
- [ ] JSONB column pattern for lists
- [ ] Primary keys and indexes
- [ ] Timestamps pattern
- [ ] Complete Task model example
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] NO sections after "Try With AI"

---

### T44.L04: Async Session Management

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/04-async-session-management.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] AsyncSession import from correct module
- [ ] `get_session()` dependency pattern
- [ ] Session lifecycle explained
- [ ] MissingGreenlet error prevention
- [ ] `expire_on_commit=False` pattern
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] NO sections after "Try With AI"

---

### T44.L05: CRUD Operations Pattern

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/05-crud-operations-pattern.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Create: add → flush → commit → refresh
- [ ] Read: get() and exec(select())
- [ ] Update: modify + commit + refresh
- [ ] Delete: delete + commit
- [ ] All operations with await
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] NO sections after "Try With AI"

---

### T44.L06: Relationships and Eager Loading

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/06-relationships-and-eager-loading.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] One-to-many relationship pattern
- [ ] Many-to-one with multiple FKs (sa_relationship_kwargs)
- [ ] Self-referential relationship (parent/subtasks)
- [ ] N+1 problem demonstration
- [ ] selectinload() solution
- [ ] `result.unique().all()` requirement
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] NO sections after "Try With AI"

---

### T44.L07: Transactions and Error Handling

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/07-transactions-and-error-handling.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] flush() vs commit() distinction
- [ ] Multi-operation transaction pattern
- [ ] Rollback on error
- [ ] `async with session.begin()` pattern
- [ ] IntegrityError handling
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] NO sections after "Try With AI"

---

### T44.L08: Migrations with Alembic

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/08-migrations-with-alembic.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] `alembic init -t async alembic` command
- [ ] env.py configuration for async
- [ ] Model import requirement explained
- [ ] Autogenerate migration
- [ ] Upgrade/downgrade commands
- [ ] Data migration example
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] NO sections after "Try With AI"

---

### T44.L09: Capstone - Complete Database Layer

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/09-capstone-complete-database-layer.md`

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Project setup instructions
- [ ] database.py creation task
- [ ] All models with relationships
- [ ] CRUD service layer task
- [ ] Transaction handling task
- [ ] Alembic setup task
- [ ] Reference to TaskFlow API implementation
- [ ] 3 "Try With AI" prompts (for orchestration)
- [ ] "Reflect on Your Skill" final assessment
- [ ] NO sections after "Try With AI"

---

### T44.QUIZ: Chapter Quiz

**Output**: `apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/10-chapter-quiz.md`

**Acceptance Criteria**:
- [ ] 15 questions covering all lessons
- [ ] Mix of question types (MCQ, code completion, debugging)
- [ ] Questions at Bloom's Remember, Understand, Apply levels
- [ ] Answer key with explanations
- [ ] YAML frontmatter

---

### T44.VALIDATE: Run All Validators

**Acceptance Criteria**:
- [ ] educational-validator passes for each lesson
- [ ] validation-auditor ≥80% weighted score
- [ ] factual-verifier: all claims verified
- [ ] pedagogical-designer: layer progression validated

---

## Progress Tracking

| Task | Status | Issue # | Notes |
|------|--------|---------|-------|
| T44.README | [ ] Pending | | |
| T44.L00 | [ ] Pending | | |
| T44.L01 | [ ] Pending | | |
| T44.L02 | [ ] Pending | | |
| T44.L03 | [ ] Pending | | |
| T44.L04 | [ ] Pending | | |
| T44.L05 | [ ] Pending | | |
| T44.L06 | [ ] Pending | | |
| T44.L07 | [ ] Pending | | |
| T44.L08 | [ ] Pending | | |
| T44.L09 | [ ] Pending | | |
| T44.QUIZ | [ ] Pending | | |
| T44.VALIDATE | [ ] Pending | | |
