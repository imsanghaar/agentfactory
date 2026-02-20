# Chapter 09: SQL & Neon PostgreSQL with Python — Task Breakdown

**Feature**: chapter-09-sql-neon
**Status**: Ready for Implementation
**Total Tasks**: 12 (8 content lessons + 1 README + 3 validation/assessment)
**Duration**: ~3.5 hours teaching content

---

## Execution Strategy

**Phase Structure**:
1. **Phase 1: Foundation** — Chapter README (provides navigation)
2. **Phase 2: Content Lessons** — L0-L7 (sequential, each lesson blocks next)
3. **Phase 3: Validation & Assessment** — Quality gates + chapter quiz

**Parallelization**: Limited (content is sequential due to pedagogical dependencies). README can be written in parallel with lessons.

**Quality Gate**: All content lessons MUST pass educational-validator + pedagogical-designer before capstone validation.

---

## Phase 1: Foundation

### README & Navigation

- [ ] T09.README Create Chapter README
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/README.md`
  - **Purpose**: Chapter overview, learning outcomes, lesson navigation, Seven Principles applied
  - **Reference**: Match structure of `08-computation-data-extraction/README.md`
  - **SUBAGENT**: content-implementer
    - Output path: (as above)
    - Include chapter structure table (8 lessons, duration, skills)
    - Include "What You'll Build" section (Budget Tracker)
    - Include Seven Principles table
    - Execute autonomously; return confirmation only (~50 lines)
  - **Acceptance Criteria**:
    - ✅ Compelling hook (why databases matter)
    - ✅ Learning outcomes aligned with Bloom's/CEFR (A1-A2)
    - ✅ Lesson table with duration, layer, proficiency
    - ✅ References expertise skill (`.claude/skills/building-with-sqlalchemy-orm/`)
    - ✅ Connection to Chapter 9 explicit

---

## Phase 2: Content Lessons (Sequential)

### L0: Build Your Database Skill

- [ ] T09.L0 Create Lesson 0: Build Your Database Skill
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/00-build-database-skill.md`
  - **Purpose**: Skill-first pattern — students create personal `/database-deployment` skill
  - **Duration**: 20 min (setup phase)
  - **Proficiency**: A1 (foundational)
  - **Layer**: Setup (L0)
  - **Prerequisites**: None (first lesson)
  - **SUBAGENT**: content-implementer
    - Output path: (as above)
    - Skill-First pattern: Fetch docs → Create skill → Test patterns
    - Three "Try With AI" prompts:
      1. "Fetch SQLAlchemy ORM docs from Context7; what are the 3 core concepts?"
      2. "Create a database-deployment skill in `.claude/skills/` with Persona, When to Use, Core Concepts"
      3. "Test your skill: 'Using my database-deployment skill, what's the difference between a model and a migration?'"
    - Include evidence blocks (skill structure, example files)
    - Execute autonomously; return confirmation only
  - **VALIDATION**: educational-validator (reads from disk)
    - Check: Skill-first pattern is clear
    - Check: References official docs (not hallucinated)
    - MUST PASS before proceeding to L1
  - **SKILLS**: learning-objectives, exercise-designer
  - **Acceptance Criteria**:
    - ✅ Full YAML frontmatter
    - ✅ 3 "Try With AI" prompts with explanations
    - ✅ Evidence blocks for skill structure
    - ✅ Student outcome: Created personal skill
    - ✅ Ends with activity (no summary)

---

### L1: From CSV to Databases

- [ ] T09.L1 Create Lesson 1: From CSV to Databases
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/01-from-csv-to-databases.md`
  - **Purpose**: Motivate databases — why CSV files fail, what databases solve
  - **Duration**: 20 min
  - **Proficiency**: A1
  - **Layer**: L1 (Manual Foundation)
  - **Prerequisites**: L0 (skill created)
  - **SUBAGENT**: content-implementer
    - Output path: (as above)
    - Compare files vs databases (persistence, relationships, querying)
    - Real-world hook: "Tax preparation script from Ch 8 — now we need multi-year data"
    - Three "Try With AI" prompts:
      1. "Why would a CSV fail if you need to track expenses across multiple users and years?"
      2. "What database concept solves the 'relationship' problem (categories linked to expenses)?"
      3. "How would you query 'total spending by category for Jan 2024' in a database vs CSV?"
    - Include evidence blocks (pseudocode comparisons, SQL SELECT example)
    - No actual database setup yet (just conceptual)
    - Execute autonomously; return confirmation only
  - **VALIDATION**: educational-validator
    - Check: Conceptual clarity (no overwhelming implementation details)
    - Check: Motivation is compelling (students understand why they're learning this)
    - MUST PASS before proceeding to L2
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching (setup Three Roles)
  - **Acceptance Criteria**:
    - ✅ Full YAML frontmatter
    - ✅ 3 "Try With AI" prompts
    - ✅ Evidence blocks (CSV vs database comparisons)
    - ✅ No code implementation yet (concept-only)
    - ✅ Ends with activity

---

### L2: Models as Code

- [ ] T09.L2 Create Lesson 2: Models as Code
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/02-models-as-code.md`
  - **Purpose**: Define Expense, Category models as Python classes (SQLAlchemy)
  - **Duration**: 25 min
  - **Proficiency**: A1
  - **Layer**: L1 (Manual Foundation)
  - **Prerequisites**: L1 (understand why databases matter)
  - **Key Concepts**:
    - SQLAlchemy ORM abstraction (classes → tables)
    - Column types (Integer, String, Float, DateTime)
    - Primary keys, constraints
    - Models for Expense, Category, User
  - **SUBAGENT**: content-implementer
    - Output path: (as above)
    - Define first two models (Category, Expense) as Python classes
    - Use examples from `.claude/skills/building-with-sqlalchemy-orm/SKILL.md`
    - Three "Try With AI" prompts:
      1. "I've defined an Expense class with amount (Float). What columns will SQLAlchemy create?"
      2. "How would I add a relationship between Category and Expense (one category has many expenses)?"
      3. "Using my database-deployment skill, what's the difference between a primary key and a foreign key?"
    - Include evidence blocks (full model code, SQLAlchemy syntax)
    - Emphasize: "You write Python classes; SQLAlchemy handles SQL"
    - Execute autonomously; return confirmation only
  - **VALIDATION**: educational-validator
    - Check: Code examples are correct (from expertise skill)
    - Check: Three Roles not explicit yet (this is L1 manual)
    - MUST PASS before proceeding to L3
  - **SKILLS**: learning-objectives, exercise-designer, fact-check-lesson (verify SQLAlchemy syntax)
  - **Acceptance Criteria**:
    - ✅ Full YAML frontmatter
    - ✅ 3 "Try With AI" prompts with explanations
    - ✅ Evidence blocks: Full working model code
    - ✅ Models: Category, Expense (at minimum)
    - ✅ Ends with activity (students define their own model)

---

### L3: Creating & Reading Data (CRUD)

- [ ] T09.L3 Create Lesson 3: Creating & Reading Data
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/03-creating-reading-data.md`
  - **Purpose**: First CRUD — insert expenses, query them back (no filtering yet)
  - **Duration**: 25 min
  - **Proficiency**: A2
  - **Layer**: L1 (Manual Foundation)
  - **Prerequisites**: L2 (models defined)
  - **Key Concepts**:
    - Sessions (database connection management)
    - Create (INSERT): `session.add()`, `session.commit()`
    - Read (SELECT): `session.query()`, `.all()`, `.first()`
    - Basic error handling
  - **SUBAGENT**: content-implementer
    - Output path: (as above)
    - Focus: Budget Tracker — insert 3 sample expenses, query them back
    - Use examples from expertise skill (Session context manager pattern)
    - Three "Try With AI" prompts:
      1. "I created an Expense object. How do I save it to the database?"
      2. "How do I retrieve all expenses from the database?"
      3. "What happens if I forget `session.commit()`? Using my skill, how would I debug this?"
    - Include evidence blocks: Full working script (create + read)
    - Emphasize Session lifecycle
    - Execute autonomously; return confirmation only
  - **VALIDATION**: educational-validator
    - Check: Code runs (students can copy and execute)
    - Check: Session pattern is correct
    - MUST PASS before proceeding to L4
  - **SKILLS**: learning-objectives, exercise-designer, fact-check-lesson
  - **Acceptance Criteria**:
    - ✅ Full YAML frontmatter
    - ✅ 3 "Try With AI" prompts
    - ✅ Evidence blocks: Create + Read working code
    - ✅ Session context manager demonstrated
    - ✅ Ends with activity (students insert their own data)

---

### L4: Relationships

- [ ] T09.L4 Create Lesson 4: Relationships
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/04-relationships.md`
  - **Purpose**: Connect categories to expenses; write join queries
  - **Duration**: 30 min
  - **Proficiency**: A2
  - **Layer**: L2 (AI Collaboration + Three Roles)
  - **Prerequisites**: L3 (basic CRUD works)
  - **Key Concepts**:
    - Foreign keys (category_id in Expense)
    - SQLAlchemy relationships (back_populates)
    - Join queries (expense.category.name)
    - Multi-table queries (all expenses for category)
  - **SUBAGENT**: content-implementer
    - Output path: (as above)
    - Add relationship to models from L2; write join queries
    - Use examples from expertise skill (relationships.md)
    - Three "Try With AI" prompts (Three Roles Framework):
      1. **AI as Teacher**: "I want to get all expenses in the 'Food' category. What's the most efficient way?"
      2. **Student as Teacher**: "I wrote a query but it's returning duplicates. Why? How would I fix it?"
      3. **Convergence**: "Using my database-deployment skill, create a reusable function to get expenses by category"
    - Include evidence blocks: Relationship definition + join query examples
    - Show: `expense.category.name` (ORM convenience)
    - Execute autonomously; return confirmation only
  - **VALIDATION**: educational-validator
    - Check: Three Roles pattern is clear and pedagogically sound
    - Check: Queries are correct (verified against expertise skill)
    - MUST PASS before proceeding to L5
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching (Three Roles mandatory for L2+), fact-check-lesson
  - **Acceptance Criteria**:
    - ✅ Full YAML frontmatter (including Three Roles framework)
    - ✅ 3 "Try With AI" prompts demonstrating Three Roles
    - ✅ Evidence blocks: Relationship + join query code
    - ✅ No summary (ends with activity)

---

### L5: Transactions & Atomicity

- [ ] T09.L5 Create Lesson 5: Transactions & Atomicity
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/05-transactions-atomicity.md`
  - **Purpose**: All-or-nothing transactions, error recovery, rollback
  - **Duration**: 30 min
  - **Proficiency**: A2
  - **Layer**: L2 (AI Collaboration + Three Roles)
  - **Prerequisites**: L4 (relationships work)
  - **Key Concepts**:
    - Atomicity (all or nothing)
    - Rollback on error
    - Try/except with session management
    - Context managers ensure cleanup
  - **SUBAGENT**: content-implementer
    - Output path: (as above)
    - Scenario: Transfer $20 from Food to Entertainment (two updates, must both succeed or both fail)
    - Use examples from expertise skill (transactions.md)
    - Three "Try With AI" prompts (Three Roles):
      1. **AI as Teacher**: "Why is this transaction important? What bad thing happens without it?"
      2. **Student as Teacher**: "I wrote a transfer function but one update succeeds and one fails. How do I fix it?"
      3. **Convergence**: "Using my skill, write a transaction pattern I can reuse for any budget transfer"
    - Include evidence blocks: Try/except pattern, rollback demonstration
    - Show: What happens if you don't commit/rollback
    - Execute autonomously; return confirmation only
  - **VALIDATION**: educational-validator
    - Check: Three Roles clear
    - Check: Atomicity concept well-explained
    - Check: Code patterns match expertise skill
    - MUST PASS before proceeding to L6
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching (Three Roles mandatory), fact-check-lesson
  - **Acceptance Criteria**:
    - ✅ Full YAML frontmatter (Three Roles framework)
    - ✅ 3 "Try With AI" prompts (Three Roles)
    - ✅ Evidence blocks: Transaction code + rollback scenario
    - ✅ Real-world example (budget transfer)
    - ✅ Ends with activity

---

### L6: Connecting to Neon

- [ ] T09.L6 Create Lesson 6: Connecting to Neon
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/06-connecting-to-neon.md`
  - **Purpose**: Real Neon account setup, environment variables, connection pooling
  - **Duration**: 25 min
  - **Proficiency**: A2
  - **Layer**: L2 (AI Collaboration + Three Roles)
  - **Prerequisites**: L5 (transactions work locally)
  - **Key Concepts**:
    - Neon project creation (free tier)
    - Connection strings (PostgreSQL URI format)
    - Environment variables (.env file)
    - Connection pooling (`pool_size`, `pool_pre_ping`)
    - SSL/TLS (required by Neon)
  - **SUBAGENT**: content-implementer
    - Output path: (as above)
    - Step-by-step: Create Neon account → Get connection string → Configure .env → Test connection
    - Use examples from expertise skill (neon-setup.md)
    - Three "Try With AI" prompts (Three Roles):
      1. **AI as Teacher**: "I got a connection error. What should I check first?"
      2. **Student as Teacher**: "My .env file works locally but not in production. What's missing?"
      3. **Convergence**: "Using my skill, create a checklist to debug Neon connection issues"
    - Include evidence blocks: Connection code, pooling configuration
    - Security note: Never hardcode credentials
    - Execute autonomously; return confirmation only
  - **VALIDATION**: educational-validator
    - Check: Security practices are clear (environment variables, no credentials in code)
    - Check: Three Roles pattern present
    - Check: Neon specifics correct (pool_pre_ping, sslmode=require)
    - MUST PASS before proceeding to L7
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching (Three Roles mandatory), fact-check-lesson (verify Neon details)
  - **Acceptance Criteria**:
    - ✅ Full YAML frontmatter (Three Roles)
    - ✅ 3 "Try With AI" prompts (Three Roles)
    - ✅ Evidence blocks: Connection setup code, .env example
    - ✅ Security note: No credentials in examples
    - ✅ Troubleshooting section included
    - ✅ Ends with activity (students connect to real Neon)

---

### L7: Capstone — Budget Tracker

- [ ] T09.L7 Create Lesson 7: Capstone — Budget Tracker
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/07-capstone-budget-tracker.md`
  - **Purpose**: Multi-table queries, monthly summaries, reporting — full Budget Tracker app
  - **Duration**: 40 min
  - **Proficiency**: A2
  - **Layer**: L3 (Skill Building)
  - **Prerequisites**: L6 (connected to Neon)
  - **Key Concepts**:
    - Aggregation queries (SUM, COUNT, GROUP BY)
    - Complex joins (User → Category → Expense)
    - Monthly summaries (date filtering, grouping)
    - Reporting output (formatted display)
    - Full CRUD on multi-table schema
  - **SUBAGENT**: content-implementer
    - Output path: (as above)
    - Full Budget Tracker: 3 models (User, Category, Expense), 5+ complex queries
    - Use complete example from expertise skill (budget-tracker-complete.py)
    - Three "Try With AI" prompts (emphasis on skill improvement):
      1. "I want to show total spending by category for this month. How do I write that query?"
      2. "My monthly summary is slow. Using my database-deployment skill, how would I optimize it?"
      3. "Show me the complete Budget Tracker code that I can run end-to-end"
    - Include evidence blocks: All models + all queries + complete script
    - Emphasis: "You now own a database-deployment skill you can apply anywhere"
    - Execute autonomously; return confirmation only
  - **VALIDATION**: educational-validator
    - Check: Code is production-ready (safe queries, proper error handling)
    - Check: Skill-building emphasis is clear (students improve their skill throughout)
    - Check: All patterns from Ch 8a appear (models, CRUD, relationships, transactions, Neon)
    - MUST PASS before final validation phase
  - **SKILLS**: learning-objectives, exercise-designer, fact-check-lesson, summary-generator (capstone context)
  - **Acceptance Criteria**:
    - ✅ Full YAML frontmatter
    - ✅ 3 "Try With AI" prompts
    - ✅ Evidence blocks: Complete working script (all models + queries)
    - ✅ Real-world use case (monthly budgets, category breakdown, trends)
    - ✅ Production-safe code (transactions, error handling)
    - ✅ Skill-building emphasis (students improve their `/database-deployment` skill)
    - ✅ Connection to Ch 9 explicit ("Next: Use this data for financial analysis")
    - ✅ Ends with activity

---

## Phase 3: Validation & Assessment

### Content Validation

- [ ] T09.VALIDATE-EDUCATIONAL Run educational-validator on all lessons
  - **Purpose**: Gate all 8 lessons through pedagogical quality validator
  - **Scope**: L0-L7 (8 lessons)
  - **Success Criteria**:
    - ✅ All 8 lessons PASS educational-validator
    - ✅ No lingering [TODO] placeholders
    - ✅ All "Try With AI" prompts have explanations
    - ✅ All code blocks have evidence (Output: sections)
    - ✅ Three Roles framework present in L4-L6
    - ✅ YAML frontmatter complete in all lessons
    - ✅ No lesson exceeds 40 minutes
  - **SUBAGENT**: educational-validator (parallel on 8 lessons)
    - Invoke once for each lesson; capture pass/fail + feedback
    - Files must exist on disk (written by content-implementer)
    - BLOCKING: All must pass before proceeding

---

- [ ] T09.VALIDATE-FACTUAL Run fact-check-lesson on all content
  - **Purpose**: Verify all facts, dates, version numbers, Neon details
  - **Scope**: L0-L7
  - **Success Criteria**:
    - ✅ No hallucinated SQLAlchemy APIs
    - ✅ Neon connection details are current (2026 documentation)
    - ✅ Python version assumptions correct (3.9+)
    - ✅ All PostgreSQL concepts are accurate
    - ✅ Zero unverified claims
  - **SUBAGENT**: fact-check-lesson
    - Verify against expertise skill references + official docs
    - BLOCKING: All claims must be verified

---

- [ ] T09.VALIDATE-PEDAGOGICAL Run pedagogical-designer on chapter flow
  - **Purpose**: Validate layer progression (L1→L2→L3→L4), cognitive load, prerequisite chain
  - **Scope**: Entire chapter (L0-L7) as a system
  - **Success Criteria**:
    - ✅ Layer progression honored (L1 is pure manual foundation)
    - ✅ Cognitive load appropriate per lesson (≤6 new concepts for A1-A2)
    - ✅ Prerequisites are correct (L2 depends on L1, etc.)
    - ✅ Skill-first pattern is clear (L0 → improved through L7)
    - ✅ Three Roles present in L2+ (collaboration layers)
    - ✅ Connection to Chapter 9 is explicit
  - **SUBAGENT**: pedagogical-designer
    - Reviews chapter README + all 8 lessons
    - BLOCKING: Progression must be valid

---

### Chapter Assessment

- [ ] T09.ASSESSMENT Create Chapter 09 Quiz
  - **Purpose**: 50-question interactive assessment (Bloom's L1-L4: Remember through Analyze)
  - **Path**: `/home/apoc/Downloads/work/panaversity/agentfactory/apps/learn-app/docs/02-Applied-General-Agent-Workflows/09-structured-data-persistent-storage/08-chapter-quiz.md`
  - **Coverage**:
    - L1-L2: Conceptual (why databases, ORM basics) — 15 questions
    - L3-L4: Applied (CRUD, queries, relationships) — 20 questions
    - L5-L6: Safety (transactions, Neon) — 10 questions
    - L7: Synthesis (capstone scenarios) — 5 questions
  - **SUBAGENT**: assessment-architect
    - Use concept-first approach: Extract key concepts from spec/lessons, generate questions around them
    - Randomized batching (display 15-20 per page)
    - Use Quiz component (if available in platform)
    - Execute autonomously
  - **Success Criteria**:
    - ✅ 50 questions total
    - ✅ Mix of question types (multiple choice, short answer)
    - ✅ Coverage of all 8 lessons
    - ✅ Measures Bloom's L1-L4 (Remember through Analyze)
    - ✅ Randomized order (prevent memorization)

---

## Task Dependencies Map

```
T09.README (independent)
    ↓
T09.L0 (Build Skill)
    ↓
T09.L1 (CSV → Databases)
    ↓
T09.L2 (Models as Code)
    ↓
T09.L3 (CRUD)
    ↓
T09.L4 (Relationships)
    ↓
T09.L5 (Transactions)
    ↓
T09.L6 (Neon)
    ↓
T09.L7 (Capstone)
    ↓
T09.VALIDATE-EDUCATIONAL (all 8 lessons must exist)
T09.VALIDATE-FACTUAL (all 8 lessons must exist)
T09.VALIDATE-PEDAGOGICAL (all 8 lessons + README must exist)
    ↓
T09.ASSESSMENT (quiz, after validation passes)
```

**Critical Path**: L0 → L7 (sequential, cannot be parallelized due to pedagogical dependencies)

**Parallelizable**:
- README can be written in parallel with any lesson
- After all lessons exist: VALIDATE-EDUCATIONAL, VALIDATE-FACTUAL, VALIDATE-PEDAGOGICAL can run in parallel

---

## Task Execution Order

**Recommended Sequence**:
1. Start T09.README (independent)
2. Execute L0-L7 sequentially (each blocks next due to pedagogical progression)
3. Once all lessons written: Run validators in parallel
4. Once validators pass: Create assessment (T09.ASSESSMENT)
5. Completion: All 12 tasks done, chapter ready for publication

---

## Completion Criteria

✅ **All Tasks Complete** when:
- All 8 content lessons exist on disk
- README complete
- All educational-validator checks PASS
- All fact-check-lesson checks PASS
- All pedagogical-designer checks PASS
- Quiz created with 50 questions
- Zero [TODO] placeholders remaining
- Chapter is cohesive (L0-L7 form complete arc)
- Students can complete capstone and own reusable skill

---

## Notes for Implementation

**Expertise Skill Integration**:
- `.claude/skills/building-with-sqlalchemy-orm/SKILL.md` is the source of truth
- All code examples come from this skill (no hallucinations)
- Students should reference this skill throughout

**Three Roles Framework** (L2+):
- L1 (L0-L3): Manual foundation (student is primary actor)
- L2 (L4-L6): AI assists (Three Roles: AI as Teacher, Student as Teacher, Convergence)
- L3 (L7): Skill building (student owns the knowledge)

**Quality Assurance**:
- Each lesson MUST pass educational-validator before next lesson starts
- No lesson should take >40 min (cognitive load constraint)
- All code MUST run (students can copy-paste from evidence blocks)

