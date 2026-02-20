---
sidebar_position: 11
title: "Chapter 10: Structured Data & Persistent Storage Quiz"
proficiency_level: A2
layer: 2
estimated_time: "30 mins"
chapter_type: Technical
running_example_id: structured-data-persistent-storage-quiz-v3
---

# Chapter 10: Structured Data & Persistent Storage Quiz

Twenty-two questions. No tricks. If you've done the work in this chapter, you'll know these answers. If some questions stump you, that's not failure -- it's feedback. Check the source reference, revisit that lesson, and come back.

Scoring guidance:

- `20-22`: strong operational readiness for chapter scope
- `16-19`: good foundation, revisit weak outcome areas
- `<=15`: repeat core exercises before moving forward

Best practice: answer once without notes, then review misses and retake after targeted repair.

## What This Quiz Measures

- modeling and constraints
- CRUD and session safety
- relationship and query reasoning
- transaction integrity
- Neon operations and security
- Chapter 8 -> 9 -> 10 tool escalation judgment

## Question-to-Outcome Map

Outcome IDs:

- `O1` Modeling and constraints
- `O2` CRUD and session correctness
- `O3` Relationships and query reasoning
- `O4` Transaction safety
- `O5` Neon operations and security
- `O6` Tool choice and verification judgment

| Question | Primary outcome |
| -------- | --------------- |
| Q1       | O6              |
| Q2       | O6              |
| Q3       | O6              |
| Q4       | O6              |
| Q5       | O1              |
| Q6       | O2              |
| Q7       | O2              |
| Q8       | O3              |
| Q9       | O3              |
| Q10      | O4              |
| Q11      | O4              |
| Q12      | O5              |
| Q13      | O5              |
| Q14      | O6              |
| Q15      | O6              |
| Q16      | O6              |
| Q17      | O1              |
| Q18      | O3              |
| Q19      | O4              |
| Q20      | O5              |
| Q21      | O6              |
| Q22      | O6              |

<Quiz
title="Chapter 10: Structured Data & Persistent Storage Assessment (v3)"
questionsPerBatch={5}
questions={[
{
question: "Which sequence best matches Part 2's escalation story?",
options: [
"Bash -> Python -> SQL -> selective hybrid",
"SQL -> Python -> Bash -> selective hybrid",
"Python -> Bash -> SQL -> selective hybrid",
"Hybrid from the start of every project"
],
correctOption: 0,
explanation: "Part 2 follows a constraint-driven escalation: Bash for file movement and orchestration (Chapter 8), Python for deterministic computation (Chapter 9), SQL for persistence and relational integrity (Chapter 10), and hybrid verification only when output risk justifies the overhead. Each tool enters when the previous one hits a boundary, not before.",
source: "Chapter README"
},
{
question: "Why does Chapter 9-style looping become risky at Chapter 10 scale?",
options: [
"Neon rejects loop-generated inserts from Python scripts",
"Python cannot handle dates or time zones reliably",
"Each new question adds another custom logic path and maintenance risk",
"Loops are disallowed by SQLAlchemy in production contexts"
],
correctOption: 2,
explanation: "Every new business question -- monthly breakdown, per-user rollup, category comparison -- requires another hand-written loop with its own edge cases and bugs. The bug surface grows linearly with query count. A database handles new questions with new queries, not new code paths.",
source: "Lesson 0"
},
{
question: "Braintrust/Vercel tested SQL vs Bash for structured data queries. What was the key finding?",
options: [
"Bash was faster but significantly less accurate overall",
"SQL achieved 100% accuracy at lower cost; Bash achieved 52.7% accuracy at higher cost",
"Both tools performed equally well on structured queries",
"Bash was more accurate for small structured datasets"
],
correctOption: 1,
explanation: "SQL: 100% accuracy, $0.51, 45 seconds. Bash: 52.7% accuracy, $3.34, 401 seconds. The right tool for structured data is not just faster -- it is correct. This is the empirical basis for Chapter 10's escalation from scripts to SQL.",
source: "Chapter README / Lesson 0"
},
{
question: "Based on the Braintrust/Vercel research, when is Bash-based data processing the WRONG choice?",
options: [
"For orchestrating multi-step shell pipeline workflows",
"For one-time text transformations on flat files",
"For file discovery and movement tasks across directories",
"For structured data querying requiring accuracy and consistency"
],
correctOption: 3,
explanation: "Bash excels at file operations and orchestration -- that is Chapter 8 territory. For structured data queries requiring accuracy, SQL is the right escalation. The Braintrust benchmark showed Bash achieving only 52.7% accuracy on structured queries, making it unreliable for any scenario where correctness matters.",
source: "Chapter README / Lesson 0"
},
{
question: "Safest money type for Expense.amount is:",
options: [
"Float with rounding applied after operations",
"String parsed to decimal at query time",
"Numeric(10, 2) for exact decimal semantics",
"Boolean flag paired with integer cents field"
],
correctOption: 2,
explanation: "Financial values need exact decimal semantics. Float stores 0.1 + 0.2 as 0.30000000000000004 -- acceptable for physics simulations, unacceptable for money. Numeric(10, 2) guarantees exact cents, which is why every payment system, bank ledger, and accounting tool uses fixed-point decimals instead of floating point.",
source: "Lesson 2"
},
{
question: "If you call session.add(row) without commit, what should you expect?",
options: [
"Row usually does not persist after session closes",
"SQLAlchemy auto-commits all sessions by default behavior",
"Neon commits staged rows when the session object closes",
"Row always persists because add triggers immediate write"
],
correctOption: 0,
explanation: "session.add() stages a change in memory but does not write it to the database. Without an explicit session.commit(), the row is lost when the session closes. This is intentional: it lets you stage multiple changes and commit them as one atomic unit, or roll them all back if something goes wrong.",
source: "Lesson 3"
},
{
question: "After a failed commit, why call rollback before reusing session logic?",
options: [
"It improves query performance for subsequent operations",
"It rotates database credentials to fresh auth tokens",
"It creates indexes needed for the next transaction",
"It resets failed transaction state so the session is usable again"
],
correctOption: 3,
explanation: "A failed commit leaves the session in a broken transaction state. Any subsequent operations on that session will also fail until you call rollback() to clear the failed state. Think of it like resetting a jammed printer -- you have to clear the error before you can print again.",
source: "Lesson 3/5"
},
{
question: "Best approach when filtering Expense rows by Category.name is:",
options: [
"Filter in Python after loading all rows into memory",
"Use select(Expense).join(Category).where(...) at the database layer",
"Export data to CSV then grep for matching rows",
"Run the same unfiltered query twice and compare results"
],
correctOption: 1,
explanation: "Filtering at the database layer with an explicit join is both faster and more correct. Loading all rows into Python and filtering wastes memory and network bandwidth. More importantly, the database can use indexes to find matching rows in milliseconds, while Python-side filtering requires scanning every row sequentially.",
source: "Lesson 4"
},
{
question: "What is the most common N+1 anti-pattern signal?",
options: [
"Looping parent objects and lazy-loading children repeatedly",
"Using selectinload to eagerly fetch related child records",
"Running a single grouped query with aggregate functions applied",
"Using one join query that fetches parents and children together"
],
correctOption: 0,
explanation: "The N+1 problem fires when your code loads N parent objects and then executes a separate query for each parent's children -- turning 1 query into N+1 queries. With 100 users, that is 101 database round-trips instead of 1. The fix is eager loading (selectinload or joinedload) which fetches everything in one or two queries.",
source: "Lesson 4"
},
{
question: "A transfer creates debit and credit rows. Required property:",
options: [
"Auto-increment for sequential row identification",
"Read replica for distributing query load evenly",
"Materialized view for precomputed balance lookups",
"Atomicity ensuring both rows commit or neither does"
],
correctOption: 3,
explanation: "Both rows must commit together or not at all. If the debit commits but the credit fails, money vanishes from the system. Atomicity guarantees all-or-nothing: either the complete transfer persists, or nothing does. This is not a nice-to-have -- it is what separates a reliable ledger from a data-corruption time bomb.",
source: "Lesson 5"
},
{
question: "Which implementation is safest for multi-step writes?",
options: [
"Separate sessions per step with independent commit calls",
"Single session with try/except + commit/rollback for atomicity",
"Commit after every line to guarantee immediate persistence",
"No exception handling so errors surface as stack traces"
],
correctOption: 1,
explanation: "One logical operation needs one atomic boundary. A single session wrapping all steps in try/except means either everything commits on success or everything rolls back on failure. Separate sessions per step create partial-write risk: step 1 commits, step 2 fails, and you are left with half a transfer.",
source: "Lesson 5"
},
{
question: "Correct credential handling for Neon is:",
options: [
"Hardcode DATABASE_URL directly in the application source code",
"Commit credentials to git and plan to rotate them later",
"Store DATABASE_URL in .env and ignore .env in git",
"Put credentials in README for easy team access and reference"
],
correctOption: 2,
explanation: "Environment-based secret handling is baseline security discipline. Your DATABASE_URL contains your host, username, and password. Committing it to git means anyone who clones the repo has full database access. Store it in .env, add .env to .gitignore, and load it with python-dotenv or os.environ at runtime.",
source: "Lesson 6"
},
{
question: "pool_pre_ping=True primarily helps with:",
options: [
"Stale pooled connections that silently died between requests",
"SQL injection prevention through input parameter sanitization",
"Schema migrations across different database version upgrades",
"Foreign key creation and constraint validation during setup"
],
correctOption: 0,
explanation: "Serverless databases like Neon can close idle connections without warning. Without pre-ping, your next query hits a dead connection and fails. pool_pre_ping=True sends a lightweight check ('SELECT 1') before each connection is used, detecting dead connections and replacing them transparently. Small cost, large reliability gain.",
source: "Lesson 6"
},
{
question: "Which statement about hybrid verification is correct?",
options: [
"Run the same SQL query twice to confirm consistent results",
"Replace SQL with Bash for independent cross-tool verification",
"Always use hybrid verification for every single database query",
"Use SQL primary plus an independent path when stakes justify overhead"
],
correctOption: 3,
explanation: "Hybrid verification means computing the same answer through two independent code paths and comparing results. It is not free -- it doubles compute cost and adds code complexity. You apply it selectively: financial reports that drive business decisions justify the overhead. A quick count of rows in a dev database does not.",
source: "Lesson 7"
},
{
question: "Which check is NOT independent?",
options: [
"SQL total vs raw ledger recompute from source data",
"SQL query rerun with same predicates and identical logic",
"SQL vs separately parsed CSV using different code path",
"SQL vs independent audit export computed from raw records"
],
correctOption: 1,
explanation: "Running the same query again with the same predicates is not independent verification -- it uses the same logic path. If there is a bug in your WHERE clause, running it twice just confirms the same wrong answer twice. True independence requires a different code path: recomputing from raw data, parsing source files separately, or using an independent audit export.",
source: "Lesson 7"
},
{
question: "For hybrid parity, which condition is mandatory?",
options: [
"Both paths must apply equivalent scope (user_id, time window, category)",
"Both paths must use the same programming language throughout",
"Both paths must use SQL as the underlying query engine",
"Both paths must run in one function within a single module"
],
correctOption: 0,
explanation: "If your SQL path filters by user_id=5 and date range January-March, but your independent path calculates across all users and all months, the numbers will never match. Scope mismatch is the most common cause of false hybrid failures. Both paths must answer the same question over the same data slice.",
source: "Lesson 7"
},
{
question: "Most robust modeling move for user-category expenses is:",
options: [
"Store user name directly on each expense record row",
"Keep all data in one text field with delimiters applied",
"Infer relationships later from pattern matching on names",
"Use FK user_id and FK category_id constraints for integrity"
],
correctOption: 3,
explanation: "Foreign keys make impossible states impossible. With FK constraints, you cannot create an expense for a user who does not exist or a category that was deleted. Storing names directly creates orphaned data when names change, duplicated data across rows, and no way for the database to enforce referential integrity.",
source: "Lesson 2/4"
},
{
question: "If report totals look suspicious, safest first step is:",
options: [
"Drop constraints to see if totals change after removal",
"Increase pool_size to handle more concurrent query connections",
"Inspect query predicates and generated SQL/log path for errors",
"Ship if trend looks normal compared to the previous period"
],
correctOption: 2,
explanation: "Before changing anything structural, verify what the system actually executed. Print the generated SQL. Check the WHERE clause parameters. Confirm the date range and filters match your intent. Most 'wrong totals' are caused by incorrect predicates, not database bugs. Dropping constraints or increasing pool size addresses problems that are almost certainly not the cause.",
source: "Lesson 4/8"
},
{
question: "You can demo a happy path, but rollback was never tested. Release decision?",
options: [
"Block release until forced-failure rollback test passes successfully",
"Release now since the happy path demo looked successful",
"Release if code is clean and passes static analysis checks",
"Release only if reads work correctly under normal conditions"
],
correctOption: 0,
explanation: "A happy-path demo proves the system works when nothing goes wrong. Production systems encounter failures: network drops, constraint violations, timeout errors. Without a forced-failure rollback test, you have no evidence that your system recovers gracefully. 'It works when everything is fine' is not a release-readiness claim.",
source: "Lesson 5/8"
},
{
question: "Error: remaining connection slots are reserved. Best immediate action?",
options: [
"Increase pool size to allow more simultaneous database connections",
"Disable SSL to reduce connection overhead and free up slots",
"Rewrite models to use fewer database connections per operation",
"Reduce pool footprint and audit session leaks for unclosed connections"
],
correctOption: 3,
explanation: "This error means you have exhausted available database connections. The instinct to increase pool_size usually makes it worse -- you are already at the limit. Instead, audit for session leaks: sessions opened but never closed, connections held during long computations, or missing 'with Session()' context managers that guarantee cleanup.",
source: "Lesson 6"
},
{
question: "A report mismatch exceeds tolerance and cause is unknown. Best policy?",
options: [
"Publish with warning noting the discrepancy for downstream review",
"Ignore if prior month matched and the trend appears stable",
"Block release and investigate before publish to find root cause",
"Average SQL and raw values to split the difference between them"
],
correctOption: 2,
explanation: "An unexplained mismatch in a high-stakes report is a release blocker, full stop. Averaging the two values hides the error. Publishing with a warning pushes investigation downstream to someone less equipped to diagnose it. The prior month matching is irrelevant -- this month's data has a problem you do not understand yet.",
source: "Lesson 7/8"
},
{
question: "Which statement best reflects Chapter 10 mastery?",
options: [
"Memorize ORM syntax for every SQLAlchemy method call",
"Apply reusable design and verification decisions under failure risk",
"Only build budget trackers using the exact chapter examples",
"Avoid debugging by writing more code to cover edge cases"
],
correctOption: 1,
explanation: "Chapter 10 mastery is not about SQLAlchemy syntax -- syntax is searchable. The durable outcome is engineering judgment: knowing when to escalate tools, how to model data relationally, why transactions matter for correctness, and what evidence constitutes release readiness. These decisions transfer to any database, any ORM, any project.",
source: "Capstone"
}
]}
/>

## After You Finish

Missed a few? Good -- that means you know exactly what to revisit. Check the outcome IDs below to pinpoint which lesson to review.

- **O1 misses** (modeling and constraints): revisit Lessons 2 and 4.
- **O2 misses** (CRUD and session correctness): revisit Lessons 3 and 5.
- **O3 misses** (relationships and query reasoning): revisit Lesson 4.
- **O4 misses** (transaction safety): revisit Lesson 5.
- **O5 misses** (Neon operations and security): revisit Lesson 6.
- **O6 misses** (tool choice and verification): revisit Lesson 0, Lesson 7, and capstone policy sections.
