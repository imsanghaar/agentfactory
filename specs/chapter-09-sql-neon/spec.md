---
sidebar_position: 9
title: "Chapter 09: SQL & Neon PostgreSQL with Python"
description: "Build persistent database applications with SQLAlchemy ORM and serverless PostgreSQL, bridging from file processing to multi-table data systems"
feature_name: "chapter-09-sql-neon"
chapter_number: 9
part_number: 2
created_date: 2026-02-06
version: 1.0
status: specification
---

# Chapter 09: SQL & Neon PostgreSQL with Python

## Overview

Your tax preparation script (from Chapter 8) processes one file at a time. What happens when you need to store expense data year-over-year? Track spending patterns? Query by category? Scale to multiple users?

**The problem**: Files are not databases. Each time you run your script, you reload everything from CSV. There's no persistent storage, no relationships between data, no way to ask complex questions efficiently.

**This chapter bridges that gap**: You'll move from "process files" to "manage persistent data systems." You'll learn SQLAlchemy ORM (Python code that talks to databases) and Neon (serverless PostgreSQL that scales automatically). By the end, you'll have a working Budget Tracker application that stores expenses in a real database, tracks them by category, generates monthly reports, and serves as the foundation for the financial analysis workflows in Chapter 9.

**The payoff**: You understand why databases exist, how Python talks to them, and how to build production-ready data layers. You own a reusable `database-skills` skill that you can apply to any domain.

---

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Python fundamentals (Chapter 3): Variables, functions, control flow, error handling
- File processing workflows (Chapter 7): CSV reading, directory navigation, batch operations
- Data extraction with Python (Chapter 8): Building utilities, processing structured data, Bash piping
- Unix philosophy (Chapter 3): Composability, small programs, testing
- General Agents (Chapter 1-3): Prompting, directing AI, understanding AI capabilities

**What this chapter must explain from scratch**:
- Relational databases: Tables, columns, rows, schemas, relationships
- SQL fundamentals: SELECT, INSERT, UPDATE, DELETE (only as conceptual foundation; ORM handles it)
- SQLAlchemy ORM: Maps Python classes to tables, abstracts SQL writing
- Sessions and transactions: Database consistency, atomicity, rollback semantics
- PostgreSQL as a service: Neon's serverless model, auto-scaling, cost implications
- MCP integration for databases: How agents can access database operations

---

## Learning Outcomes

**By the end of this chapter, students will be able to**:

1. **Conceptually**: Explain why databases beat files for persistent data, what ORM means, why Neon's serverless model matters
2. **Apply**: Define data models as Python classes, perform CRUD operations safely, handle transactions
3. **Build**: Create a multi-table application (Budget Tracker) with relationships, queries, and error recovery
4. **Extend**: Connect their database to a Neon account, enable AI agents to query data via MCP

**Bloom's Taxonomy Alignment**:
- L1-L2: Remember/Understand (ORM concepts, why databases matter)
- L3-L5: Apply/Analyze (Define models, implement CRUD, handle transactions)
- L6-L7: Evaluate/Create (Design queries, capstone multi-feature app)

**CEFR Proficiency**: A1-A2 (Beginners, foundational practical skills)

---

## Chapter Structure

| Lesson | Title | Layer | Proficiency | Duration | Key Skills |
|--------|-------|-------|-------------|----------|------------|
| L0 | Build Your Database Skill | Setup | A1 | 20 min | Create personal database skill, fetch docs, test patterns |
| L1 | From CSV to Databases | L1 (Manual) | A1 | 20 min | Recognize database paradigm, compare to files |
| L2 | Models as Code | L1 (Manual) | A1 | 25 min | Define Expense, Category models as Python classes |
| L3 | Creating & Reading Data | L1 (Manual) | A2 | 25 min | First CRUD: insert expenses, query them back |
| L4 | Relationships | L2 (Collaboration) | A2 | 30 min | Connect categories to expenses, multi-table queries, joins |
| L5 | Transactions & Atomicity | L2 (Collaboration) | A2 | 30 min | Understand all-or-nothing, error recovery, rollback |
| L6 | Connecting to Neon | L2 (Collaboration) | A2 | 25 min | Environment setup, serverless specifics, connection pooling |
| L7 | Capstone: Budget Tracker | L3 (Skill) | A2 | 40 min | Multi-table queries, monthly summaries, reporting |

**Total Duration**: ~215 minutes (~3.5 hours) over 8 lessons

---

## Layer Progression

This chapter follows the Four-Layer Teaching Method:

**L1: Manual Foundation** (L1-L3)
- Students write raw SQLAlchemy code
- Manual transaction handling with try/except
- Foundation: "This is how databases work"

**L2: AI-as-Collaborator** (L4-L6)
- AI suggests query patterns
- Students refine and validate
- Focus: "How do I build this efficiently?"

**L3: Skill Building** (L7 Capstone)
- Students create `/database-deployment` skill
- Leverage that skill to build complex queries
- Outcome: "I own reusable database knowledge"

**L4: Orchestration** (Optional, bridges to Ch 9)
- If time: Connect Budget Tracker to Chapter 9's financial modeling
- Agents query historical data to generate forecasts

---

## Student Outcomes

### By Chapter End, Students Will Have

**1. A Working Budget Tracker Application**
```
- Multi-table structure (users, categories, expenses)
- Full CRUD operations (create expense, list by category, update, delete)
- Complex queries (monthly summaries, category spending, trends)
- Error handling (orphaned records, invalid categories)
- Ready to connect to Neon and share with friends
```

**2. A Personal Database Skill**
- Created in L0, improved throughout the chapter
- References official SQLAlchemy + Neon docs
- Ready for reuse in other projects (portfolio piece)
- Demonstrates "skill-first learning" (you own the knowledge)

**3. Foundation for Chapter 9**
- Database queries retrieve historical spending data
- Financial models in Ch 9 will use this as data source
- Connection is explicit: "Ch 8a built persistence, Ch 9 builds analysis"

---

## Seven Principles Applied

| Principle | How It Appears | Where |
|-----------|---|---|
| **P1: Bash is the Key** | Connection strings, environment variables via shell | L6 (Neon setup) |
| **P2: Code as Universal Interface** | Python classes map to database tables; ORM is "code interface" | L2-L3 (Models as Code) |
| **P3: Verification as Core Step** | Test queries with known data; verify atomicity with rollback | L5 (Transactions) |
| **P4: Small, Reversible Decomposition** | Each lesson: single model → single CRUD op → single feature | Throughout |
| **P5: Persisting State in Files** | Database persistence replaces file-based state | L1 (CSV to Tables) |
| **P6: Constraints and Safety** | Transactions ensure consistency; foreign keys prevent orphans | L5-L6 |
| **P7: Observability** | Query logging, transaction debugging, connection pool monitoring | L6 (Neon debugging) |

---

## Expertise Skill Reference

**This chapter leverages**: `.claude/skills/building-with-sqlalchemy-orm/SKILL.md`

The skill includes:
- API patterns (from official SQLAlchemy 2.0+ docs)
- Neon-specific setup (connection strings, SSL, pooling)
- Transaction patterns (context managers, savepoints, rollback)
- Complete Budget Tracker example (tested, runnable code)

**Why the skill exists**: Ensures all examples are accurate, no hallucinated APIs, no deprecated patterns. Students copy patterns directly from the skill.

---

## Prerequisites

**Technical Setup**:
- Python 3.9+ (students have this from Ch 3)
- Neon free account (takes 2 minutes to create, no credit card needed)
- SQLAlchemy + psycopg2 (installed with: `pip install sqlalchemy psycopg2-binary` or `uv add sqlalchemy psycopg2-binary`)

**Conceptual Foundation**:
- Understands CSV files (Ch 8)
- Comfortable with Python functions and error handling (Ch 3)
- Familiar with environment variables (Ch 6 or earlier)
- Know what "persistent data" means (no re-reading files each time)

---

## Assumptions

1. **Students use Neon** (not local PostgreSQL)
   - *Rationale*: Neon is free, requires zero setup, auto-scales, teaches serverless concepts
   - *Fallback*: Lessons work with any PostgreSQL; just change connection string

2. **SQLAlchemy ORM (not raw SQL)**
   - *Rationale*: ORM teaches "code as interface" (Principle 2); students stay in Python; less error-prone
   - *Fallback*: Skill includes both raw SQL patterns (references/api-patterns.md) for advanced students

3. **No database migrations** (no Alembic)
   - *Rationale*: Chapter 8a teaches fundamentals; migrations are Production Topic for Part 7
   - *Scope*: `Base.metadata.create_all(engine)` is sufficient for learning

4. **Budget Tracker is THE running example** (not multiple examples)
   - *Rationale*: Coherence. Every lesson builds toward same goal. Easier to follow.
   - *Continuity*: Chapter 9 will use Budget Tracker data for financial modeling

5. **Three "Try With AI" prompts per lesson** (consistent with Part 2 pedagogy)
   - *Rationale*: Matches Chapter 8 quality; builds AI collaboration skills
   - *Variation*: L0 (skill-building) may focus on fetching docs + testing; L7 (capstone) may use AI to refine queries

---

## Success Criteria

1. **Students can define a data model**
   - Write Python classes that map to database tables ✅
   - Include relationships (foreign keys) ✅
   - Predict what tables/columns will be created ✅

2. **Students can perform safe CRUD**
   - Create records without SQL injection risk ✅
   - Query filtered data (WHERE clauses) ✅
   - Update and delete with proper error handling ✅
   - Use transactions to guarantee atomicity ✅

3. **Students connect to Neon successfully**
   - Create free Neon account ✅
   - Get connection string ✅
   - Configure environment variables ✅
   - Verify connection with a test query ✅

4. **Students build and deploy Budget Tracker**
   - Define User, Category, Expense models ✅
   - Implement all CRUD operations ✅
   - Write complex queries (joins, aggregations, grouping) ✅
   - Handle transactions for multi-step operations ✅

5. **Students own a reusable database skill**
   - Created in L0, improved throughout chapter ✅
   - References official docs (not hallucinated) ✅
   - Tested on real patterns ✅
   - Portfolio-ready (can show to employers/collaborators) ✅

---

## Acceptance Scenarios

### Scenario 1: Student Creates First Model
```
GIVEN: Student finishes L2
WHEN: They define Expense class with amount, description, date
THEN: They can predict that SQLAlchemy will create an `expenses` table
  AND: Table has columns for amount (float), description (string), date (datetime)
  AND: Primary key (id) is auto-generated
```

### Scenario 2: Student Inserts and Queries Data
```
GIVEN: Student finishes L3
WHEN: They create 5 expenses via Python
THEN: They can query all expenses back
  AND: filter by amount > 50
  AND: order by date descending
  AND: get correct results (no SQL written by hand)
```

### Scenario 3: Student Handles a Transaction
```
GIVEN: Student finishes L5
WHEN: They transfer $20 from Food budget to Entertainment
THEN: Both debit and credit succeed together
  OR: Both roll back (if error in second operation)
  AND: No partial state (either both happen or neither)
```

### Scenario 4: Student Connects to Neon
```
GIVEN: Student finishes L6
WHEN: They paste their Neon connection string into .env
THEN: Budget Tracker successfully creates tables in Neon
  AND: They can insert/query data from Python
  AND: Data persists even after closing and re-opening the app
```

### Scenario 5: Student Completes Capstone
```
GIVEN: Student finishes L7
WHEN: They run the Budget Tracker capstone
THEN: They can:
  - Add expenses via function call
  - View monthly spending summary
  - See breakdown by category
  - Export data (or print formatted report)
  AND: All operations use transactions safely
```

---

## Edge Cases & Error Handling

1. **Orphaned Records**: User deletes category while expenses exist
   - *Solution*: Teach foreign key constraints and CASCADE delete
   - *Chapter Coverage*: L4 (Relationships)

2. **Concurrent Updates**: Two processes modify same expense simultaneously
   - *Solution*: Transaction isolation, optimistic locking pattern
   - *Chapter Coverage*: L5 (Transactions) - mention but don't implement

3. **Invalid Connection String**: Wrong Neon credentials
   - *Solution*: Clear error message, debugging checklist in L6
   - *Chapter Coverage*: L6 (Troubleshooting section)

4. **Connection Pool Exhaustion**: Too many open connections
   - *Solution*: Configure `pool_size`, `pool_pre_ping` in L6
   - *Chapter Coverage*: L6 (Connection Pooling)

5. **Data Type Mismatch**: Trying to insert string into amount (float) column
   - *Solution*: SQLAlchemy validation, type hints in models
   - *Chapter Coverage*: L2-L3 (Model definition, CRUD)

---

## Connection to Chapter 9

**Chapter 9 (Data Analysis & Financial Modeling)** will:
- Query Budget Tracker data for historical analysis
- Build financial forecasts based on spending patterns
- Generate investment recommendations
- Explicit bridge: "In Ch 8a you built the database; in Ch 9 you analyze it"

**Skill Continuity**: The `database-skills` skill from Ch 8a becomes a foundation for the `financial-analysis-skills` skill in Ch 9.

---

## Constraints

**In Scope**:
- SQLAlchemy ORM fundamentals (models, sessions, relationships, transactions)
- CRUD operations (all four, all safe)
- Querying (filtering, ordering, joining, aggregating)
- PostgreSQL + Neon setup
- Connection pooling basics
- Error handling and transactions
- Budget Tracker capstone

**Out of Scope**:
- Database migrations (Alembic) → Part 7
- Complex optimization (indexes, query plans) → Part 7
- Raw SQL writing → Not needed; ORM covers 99% of cases
- NoSQL databases → Explicit focus on relational (PostgreSQL)
- Distributed transactions → Out of scope for A1-A2

---

## Quality References

**Structure Match**: Chapter 8 (6 lessons + capstone)
**Prose Style**: Chapter 7 (compelling narrative, real-world hook)
**Lesson Duration**: 15-40 minutes each (matches Part 2 pedagogy)
**Code Quality**: All examples from `.claude/skills/building-with-sqlalchemy-orm/SKILL.md` (verified, tested)

---

## Differentiation

**For Advanced Students**:
- Explore connection pooling optimization (L6)
- Implement custom query builder patterns (L7)
- Add connection to AI agents via MCP (optional extension)
- Migrate Budget Tracker to read replicas (optional)

**For Struggling Students**:
- Start with single-table Expense model (skip relationships initially)
- Use provided CRUD functions as templates (in L3)
- Focus on one query pattern at a time (don't combine filtering + ordering + grouping in L4)
- Checkpoint: "Does `CREATE` and `READ` work? Yes? Continue. No? Debug here."

---

## Student Skill Outcome

By chapter end, students will have created (and iteratively improved) a `/database-deployment` skill with:

```
.claude/skills/database-deployment/
├── SKILL.md (their own understanding, not copy-paste)
│   ├── Persona: "I'm a Python developer building data-persistent apps"
│   ├── When to use: "When I need to store data long-term"
│   ├── Core Concepts: Models, Sessions, Relationships
│   ├── Decision Logic: When to normalize, when to denormalize
│   └── Workflow: Define model → Connect → CRUD → Query → Test
├── references/
│   ├── model-patterns.md (what I learned)
│   ├── transaction-safety.md (what I learned)
│   └── neon-setup.md (what I learned)
└── examples/
    └── budget-tracker.py (my working capstone)
```

This skill is:
- **Yours**: You created it, you own it
- **Reusable**: Apply it to any database project
- **Portfolio-Ready**: Show it to employers as evidence of learning
- **Living**: Update it as you learn more about databases

---

## Next Steps (Post-Chapter)

1. **Chapter 9**: Use Budget Tracker data for financial analysis
2. **Optional Mini-Chapter**: Add web API (Flask/FastAPI) to Budget Tracker
3. **Part 5+**: Use database skills in larger agent projects
4. **Certification**: Create a small portfolio project using your `database-deployment` skill

---

## Blockers & Dependencies

- ✅ Expertise skill exists: `.claude/skills/building-with-sqlalchemy-orm/SKILL.md`
- ✅ Chapter 8 completed (students know data processing)
- ⏳ Neon account (students create during L6)
- ⏳ IDE/terminal access (same as all chapters)

---

## Revision History

- **v1.0** (2026-02-06): Initial specification from Phase A expertise skill research
  - 8 lessons (L0 skill-first + L1-L7 content)
  - Budget Tracker as running example
  - Neon PostgreSQL + SQLAlchemy ORM
  - Ready for `/sp.clarify`

