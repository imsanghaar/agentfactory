---
id: "0177"
title: "Chapter 44: Relational Databases for Agents with SQLModel"
stage: general
date: 2025-12-30
surface: cli
model: claude-opus-4-5
feature: chapter-44-relational-databases-sqlmodel
branch: 001-ch60-cloud-deployment
user: mjs
command: /sp.chapter
labels: [chapter-creation, skill-first, sqlmodel, async, postgresql]
links:
  spec: specs/chapter-44-relational-databases-sqlmodel/spec.md
  ticket: none
  adr: none
  pr: pending
files:
  - .claude/skills/building-with-sqlmodel-async/SKILL.md
  - .claude/skills/building-with-sqlmodel-async/references/async-patterns.md
  - .claude/skills/building-with-sqlmodel-async/references/relationships.md
  - .claude/skills/building-with-sqlmodel-async/references/migrations.md
  - .claude/skills/building-with-sqlmodel-async/scripts/verify.py
  - specs/chapter-44-relational-databases-sqlmodel/spec.md
  - specs/chapter-44-relational-databases-sqlmodel/clarifications.md
  - specs/chapter-44-relational-databases-sqlmodel/plan.md
  - specs/chapter-44-relational-databases-sqlmodel/tasks.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/README.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/00-build-your-database-skill.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/01-why-agents-need-structured-data.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/02-sqlmodel-async-engine-setup.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/03-designing-agent-data-models.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/04-async-session-management.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/05-crud-operations-pattern.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/06-relationships-and-eager-loading.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/07-transactions-and-error-handling.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/08-migrations-with-alembic.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/09-capstone-complete-database-layer.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/10-chapter-quiz.md
tests:
  - verify.py: PASS (skill validation)
  - L02 validator: 87.5% PASS
  - L06 validator: 73.25% CONDITIONAL (skill-first pattern conflict)
---

## Prompt

User invoked `/sp.chapter` for Chapter 44: Relational Databases for Agents with SQLModel.

Key requirements:
- Part 6: AI Native Software Development
- B1 intermediate level
- Skill-first pattern with student skill `relational-db-agent`
- Technology: SQLModel async, PostgreSQL, asyncpg, Alembic
- 10 lessons (L00-L09) + quiz
- Autonomous execution through all phases

## Response snapshot

### Phase A: Expertise Skill Creation
Created `building-with-sqlmodel-async` skill with comprehensive async patterns:
- AsyncSession from sqlmodel.ext.asyncio.session
- create_async_engine with pool_pre_ping=True
- JSONB column configuration
- Self-referential relationship patterns
- selectinload() for N+1 prevention
- result.unique().all() pattern
- Transaction rollback patterns
- Alembic async migration setup

### Phase B: Chapter Content Creation
1. Created specification with 10-lesson structure
2. Created implementation plan with skill-first approach
3. Generated all 12 content files (README, L00-L09, Quiz)
4. Ran validators - L02 PASS (87.5%), L06 conditional pass

Key patterns taught:
- L00: Build relational-db-agent skill
- L01: Relational vs vector databases
- L02: Async engine with pool configuration
- L03: SQLModel with JSONB, constraints
- L04: AsyncSession lifecycle
- L05: Async CRUD operations
- L06: Relationships and eager loading
- L07: Transactions and error handling
- L08: Alembic async migrations
- L09: Capstone - complete database layer

## Outcome

- ✅ Impact: Complete chapter created with expertise skill + 12 lesson files
- 🧪 Tests: Skill verified, lessons validated (L02: 87.5%, L06: 73.25%)
- 📁 Files: 21 files created across skill, specs, and content directories
- 🔁 Next prompts: Commit and PR creation
- 🧠 Reflection: Skill-first pattern places "Reflect on Your Skill" after "Try With AI" which conflicts with constitution principle 7. This is intentional for practical chapters but flagged by validator.

## Evaluation notes (flywheel)

- Failure modes observed: Context7 library lookup failed for SQLModel (used WebSearch fallback)
- Graders run and results (PASS/FAIL): L02 PASS (87.5%), L06 CONDITIONAL (73.25%)
- Prompt variant (if applicable): skill-first-chapter-pattern
- Next experiment: Consider restructuring "Reflect on Your Skill" to appear as subsection within "Try With AI" to satisfy both skill-first pattern and constitution compliance
