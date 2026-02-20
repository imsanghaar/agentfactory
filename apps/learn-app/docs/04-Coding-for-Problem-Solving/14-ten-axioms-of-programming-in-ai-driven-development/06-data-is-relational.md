---
sidebar_position: 6
title: "Axiom VI: Data is Relational"
description: "Why structured data follows relational patterns, SQL as the universal data language, and how to choose between SQLite and PostgreSQL for agentic development"
keywords: ["SQL", "relational database", "SQLite", "PostgreSQL", "ORM", "SQLModel", "data modeling", "schema", "migrations", "agentic development"]
chapter: 14
lesson: 6
duration_minutes: 22

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding Relational Data Modeling"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain why structured data naturally follows relational patterns and identify entities, attributes, and relationships in a domain"

  - name: "Choosing SQL Databases for Agent Work"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can apply the SQLite vs PostgreSQL decision framework to determine the appropriate database for a given project scope"

  - name: "Writing SQL as Agent-Readable Specifications"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Understand"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can explain why SQL schemas serve as type definitions for data and why AI agents work effectively with SQL as a constrained, declarative language"

learning_objectives:
  - objective: "Explain why SQL has endured for 50+ years and why it remains the default for structured persistent data"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can articulate at least three properties of SQL (declarative, optimized, relational) that make it durable and superior to ad-hoc alternatives for structured data"

  - objective: "Apply the SQLite vs PostgreSQL decision framework to real project scenarios"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Given a project description (single-user CLI tool, multi-user web app, embedded device), student can recommend the correct database with reasoning"

  - objective: "Identify anti-patterns in data persistence and explain their consequences"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student can recognize at least three anti-patterns (JSON-as-database, no migrations, no parameterization) and explain what goes wrong in each case"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (relational model, SQL declarative language, SQLite vs PostgreSQL tradeoffs, ORM layering, migrations, SQL injection) within A2-B1 range (5-7 concepts)"

differentiation:
  extension_for_advanced: "Explore database normalization forms (1NF through 3NF), write a migration script using Alembic, compare query plans between indexed and non-indexed queries"
  remedial_for_struggling: "Focus on the single concrete example: one Task table in SQLite, insert a row, query it back. Understand that SQL is just a language for talking to structured data"
---

# Axiom VI: Data is Relational

Axiom V gave James typed dataclasses for orders, customers, and products — Pyright catching structural errors before runtime. But types describe individual objects. A `CustomerOrder` knows its own shape. It knows nothing about the customer who placed it, the products inside it, or the fifty other orders that customer has made. When the team asked James to build a dashboard showing order history *by customer*, with filters for date range, status, and product category, he hit a wall that types alone could not solve. His data had *relationships*, and nothing in his system understood them.

His data lived in a JSON file: `orders.json`. Each order was a dictionary with a `customer_name` string, a `product_name` string, and a `status` field. To find all orders for "Acme Corp," he loaded the entire file into memory and looped through every record. To find overdue orders across all customers, he looped again. To count how many orders each customer had placed, he looped a third time, building a dictionary by hand. The file was 2,000 records. The dashboard took eleven seconds to load.

Then the product team changed a customer's name from "Acme Corp" to "Acme Corporation." James updated the customer record. He forgot to update the 47 orders that referenced the old name. Now the dashboard showed two customers — "Acme Corp" with 47 historical orders and "Acme Corporation" with zero. The data was inconsistent, and the JSON file had no way to tell him.

"Your data has relationships," Emma told him. "Customers *have* orders. Orders *contain* products. Products *belong to* categories. You are storing relational data in a format that does not understand relationships. That is like writing typed code without a type checker — the structure is there, but nothing enforces it."

She opened a terminal and typed twelve lines of SQL. The same dashboard query that took eleven seconds and forty lines of Python returned in three milliseconds. The customer name lived in one place. The relationships were enforced by the database. The data could not become inconsistent because the system would not allow it.

The difference between JSON-as-database and a relational database is Axiom VI.

## The Problem Without This Axiom

James's `orders.json` was not a beginner's mistake. It was the path every developer follows when data starts simple and grows relational. The trajectory is predictable:

| Stage | What Happens | Consequence |
|-------|-------------|-------------|
| Week 1 | JSON file stores 20 records | Fast, simple, readable |
| Month 2 | File grows to 500 records | Queries require loading everything into memory |
| Month 4 | Second entity added (customers separate from orders) | Relationships expressed by duplicating strings |
| Month 6 | Name change breaks data consistency | No constraints, no validation, no way to detect the problem |
| Month 9 | Dashboard needs cross-entity queries | 40 lines of Python to do what SQL does in 3 |
| Month 12 | AI agent asked to query the data | Agent writes custom loops because JSON has no query language |

Without recognizing that structured data is inherently relational, developers fall into three traps. **The JSON Graveyard**: projects accumulate JSON files — `orders.json`, `customers.json`, `products.json` — with no way to express relationships between them. James was building one. **The Flat File Spiral**: as complexity grows, developers invent ad-hoc query languages, build custom indexing, implement their own transaction logic — slowly reinventing a database, badly. **The NoSQL Trap**: developers reach for document stores because the API feels familiar, but when the data *is* relational, fighting its nature creates complexity that a relational database handles natively.

Each path leads to the same destination: a system that cannot answer basic questions about its own data without heroic effort from the developer.

## The Axiom Defined

> **Axiom VI: Structured data follows relational patterns. SQL is the default for persistent structured data. SQLite for single-user, PostgreSQL for multi-user. Use an ORM only when it doesn't obscure the SQL.**

This axiom makes three claims — each of which James learned the hard way:

1. **Structured data is relational by nature.** When you have entities with attributes and connections between them, you have relational data — whether or not you store it relationally. James's JSON file *contained* relational data. It just could not *enforce* the relationships.
2. **SQL is the default choice.** Not the only choice, but the one you should deviate from consciously with good reason.
3. **The ORM serves you, not the reverse.** If your ORM hides the SQL so completely that you cannot reason about what queries execute, it has become an obstacle.

## From Principle to Axiom

In Part 1, Chapter 4, you learned **Principle 5: Persisting State in Files** — the general durability rule that work products must survive beyond a single session. James was already following this principle — his team's markdown knowledge base (Axiom II) and his typed Python modules (Axiom III) all persisted in files.

But Axiom VI refines this principle for a specific category of state: **structured data with relationships**. Not all persistent data belongs in the same format. The distinction matters:

| State Type | Storage | Why |
|-----------|---------|-----|
| Knowledge, documentation, specs | Markdown files | Human-readable, version-controlled, AI-parseable |
| Configuration | YAML/TOML files | Declarative, mergeable, environment-specific |
| Structured entities with relationships | SQL database | Queryable, constrained, normalized, concurrent-safe |
| Binary assets | File system | Git LFS or object storage for large files |

Principle 5 tells you to persist state. Axiom VI tells you HOW to persist structured data: relationally, with SQL, using the right engine for the job.

<details>
<summary>**The Paper That Gave Data a Theory**</summary>

In 1970, an English mathematician named Edgar F. Codd published a paper at IBM's San Jose Research Laboratory: "A Relational Model of Data for Large Shared Data Banks." At the time, databases were navigational — programs traversed pointers from record to record, like walking through a maze. If the structure of the maze changed, every program that navigated it broke. Codd proposed something radical: separate the *logical* structure of data from its *physical* storage. Define data as tables with rows and columns. Express queries as mathematical operations on those tables. Let the database — not the programmer — figure out how to retrieve the data efficiently.

IBM's own database team resisted. They had built IMS, a hierarchical database that powered most of the company's revenue. Codd's relational model threatened that product. IBM delayed implementation for years. But a young programmer named Larry Ellison read Codd's paper, saw its implications, and in 1977 founded a company to build the first commercial relational database. He called it Oracle.

The relational model won because it solved James's exact problem at industrial scale: when data has relationships, a system that *understands* relationships will always outperform one that does not. Codd's tables, foreign keys, and constraints are the reason Emma's twelve-line SQL query returned in three milliseconds what James's forty-line Python loop took eleven seconds to produce. The database optimizer — the component Codd's model made possible — chose the execution path. James did not have to.

More than half a century later, SQL remains the dominant language for structured data. It has survived the rise and fall of object databases (1990s), the XML movement (2000s), the NoSQL revolution (2010s), and the graph database wave (2020s). Each found legitimate niches. None displaced SQL for general-purpose structured data, because Codd's insight addresses a property of data itself: when entities have relationships, a relational system is the natural fit.

</details>

### Why SQL Works

| Property | What It Means | Why It Matters |
|----------|---------------|----------------|
| **Declarative** | You say WHAT you want, not HOW to get it | The database optimizer chooses the execution strategy |
| **Relational** | Data is organized into related tables | Reflects how real-world entities connect |
| **Constrained** | Schema enforces structure, types, and relationships | Invalid data is rejected before it enters the system |
| **Optimized** | Decades of query planner research | Complex queries execute efficiently without manual tuning |
| **Transactional** | ACID guarantees (Atomicity, Consistency, Isolation, Durability) | Data is never left in a half-updated state |
| **Universal** | One language across SQLite, PostgreSQL, MySQL, SQL Server | Skills transfer between databases |

The declarative nature deserves emphasis. This is why Emma's query was so much shorter than James's Python loop. When you write:

```sql
SELECT tasks.title, projects.name
FROM tasks
JOIN projects ON tasks.project_id = projects.id
WHERE tasks.status = 'overdue'
ORDER BY tasks.due_date;
```

You have not specified HOW to find this data. You have not said "scan the tasks array, for each task look up the project, filter by status, then sort." You described the RESULT you want, and the database figures out the fastest path to deliver it. This is the same declarative philosophy behind CSS, HTML, and configuration files — and it is why AI agents work so effectively with SQL.

## Relational Thinking: Entities and Relationships

Emma started James's education by drawing three boxes on a whiteboard — the same three entities that his JSON file had tangled together.

![Entity-Relationship Diagram showing customers, orders, order_items, and products tables with their relationships](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-4/chapter-14/06-entity-relationship-diagram.png)

### 1. Entities (Tables)

An entity is a distinct "thing" in your domain. In James's order system:

- **Customer** — a company or person who places orders
- **Order** — a transaction with a status, date, and total
- **Product** — an item that can be ordered

Each entity becomes a table. Each row is one instance. The key insight: in James's JSON file, these three entities were mashed into a single list of dictionaries. In a relational database, each lives in its own table with its own structure.

### 2. Attributes (Columns)

Each entity has typed properties — and this is where Axiom V meets Axiom VI. The schema *is* a type definition for your data:

```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'shipped', 'delivered')),
    total_amount REAL NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    customer_id INTEGER NOT NULL REFERENCES customers(id)
);
```

Notice the constraints: `NOT NULL` means required, `UNIQUE` prevents duplicates, `CHECK` restricts values to a valid set, `REFERENCES` declares relationships. When Emma showed this to James, he recognized the pattern from Axiom V — these constraints are guardrails, enforced by the database instead of the type checker.

### 3. Relationships (Foreign Keys)

Relationships connect entities — the part James's JSON could not express:

- A Customer **has many** Orders (one-to-many)
- An Order **belongs to** a Customer (many-to-one)
- An Order **contains** Products (many-to-many, via a junction table)

Foreign keys enforce referential integrity: you cannot create an order for a customer that does not exist. This is what prevented James's "Acme Corp" vs "Acme Corporation" disaster — the customer name lives in one row of the `customers` table, and every order references it by `id`, not by duplicated string.

```sql
-- This FAILS if customer_id 999 doesn't exist -- the database protects you
INSERT INTO orders (status, total_amount, customer_id)
VALUES ('pending', 149.99, 999);
-- Error: FOREIGN KEY constraint failed
```

Compare this to JSON, where nothing prevents `"customer_id": 999` even if no such customer exists. The relational database catches the error. The JSON file silently accepts it.

## The SQLite / PostgreSQL Decision

"Which database should I use?" James asked. Emma's answer was a decision framework, not a preference. The axiom specifies two databases — here is when to use each:

| Factor | SQLite | PostgreSQL |
|--------|--------|------------|
| **Writers** | Single process | Many concurrent users |
| **Deployment** | Embedded in your application | Separate server process |
| **Setup** | Zero configuration (just a file) | Requires installation and configuration |
| **Size** | Up to ~1 TB practical | Petabytes with proper architecture |
| **Concurrency** | Single-writer, multiple readers | Full MVCC (Multi-Version Concurrency Control) — concurrent reads and writes without blocking |
| **Use case** | CLI tools, mobile apps, prototypes, embedded | Web apps, APIs, multi-user systems |
| **Backup** | Copy the file | pg_dump or streaming replication |
| **AI agent work** | Local projects, personal tools | Production deployments |

### The Decision Framework

Ask these three questions:

1. **How many processes write to this database simultaneously?**
   - One process: SQLite
   - Multiple processes: PostgreSQL

2. **Does this need to run as a network service?**
   - No (CLI tool, desktop app, local agent): SQLite
   - Yes (web API, shared service): PostgreSQL

3. **Is this a prototype or production?**
   - Prototype: SQLite (migrate to PostgreSQL later if needed)
   - Production multi-user: PostgreSQL from the start

### SQLite in Practice

SQLite is not a toy database. It is the most widely deployed database engine in the world — present in every smartphone, every web browser, and most operating systems. For James's order dashboard — a single-user internal tool — it was exactly the right choice. No server to maintain, no connection strings to manage, no Docker containers. Just a file:

```python static
import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# The schema Emma wrote — James's orders.json replaced in 12 lines
cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL DEFAULT 'pending',
    total_amount REAL NOT NULL,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
)""")

# Insert with parameterized queries (SAFE — see anti-patterns below)
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)",
               ("Acme Corporation", "orders@acme.com"))
customer_id = cursor.lastrowid

cursor.execute("INSERT INTO orders (status, total_amount, customer_id) VALUES (?, ?, ?)",
               ("shipped", 149.99, customer_id))
conn.commit()

# The dashboard query — 3 milliseconds instead of 11 seconds
cursor.execute("""
    SELECT customers.name, COUNT(orders.id), SUM(orders.total_amount)
    FROM customers
    JOIN orders ON orders.customer_id = customers.id
    GROUP BY customers.id
    ORDER BY SUM(orders.total_amount) DESC
""")

for name, count, total in cursor.fetchall():
    print(f"{name}: {count} orders, ${total:.2f} total")

conn.close()
```

This replaced James's entire forty-line Python loop. The database is a single file (`orders.db`) that you can copy, back up, or inspect with any SQLite tool. When the team later moved the dashboard to a multi-user web app, the SQL transferred directly to PostgreSQL — same queries, different connection string. This is the universality of SQL: learn it once, apply it everywhere.

## SQL and AI: Why Agents Love Relational Data

This is where Axiom VI connects to everything this book teaches — and where the lesson becomes urgent rather than merely architectural. When James asked an AI agent to "show me all overdue orders for Acme Corp" against his JSON file, the agent generated this:

```python static
import json
from datetime import datetime, timedelta

with open("orders.json") as f:
    data = json.load(f)

cutoff = datetime.now() - timedelta(days=30)
results = []
for order in data["orders"]:
    # Hope that "customer" is spelled consistently
    if "Acme" in order.get("customer_name", ""):
        if order.get("status") == "pending":
            created = datetime.fromisoformat(order["created_at"])
            if created < cutoff:
                results.append(order)
```

The code works — until someone stores the customer name as `"customer"` instead of `"customer_name"`, or formats dates differently, or nests orders inside customer objects. The AI had no schema to consult, so it guessed at field names, assumed a flat structure, and produced brittle string matching. Every assumption is a silent failure waiting to happen.

When he asked the same question against his SQL schema, the agent generated:

```sql
SELECT orders.id, orders.total_amount, orders.created_at
FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE customers.name = 'Acme Corporation'
AND orders.status = 'pending'
AND orders.created_at < datetime('now', '-30 days');
```

The difference is structural. **SQL has a constrained vocabulary** — approximately 30 keywords that matter. Compare this to Python's thousands of library functions. Fewer choices mean fewer hallucination opportunities. **SQL is declarative** — it describes WHAT you want, not HOW to get it. Natural language intent maps almost word-for-word to SQL. **The schema is the specification** — when you give an AI agent your `CREATE TABLE` statements, it knows exactly what data exists, what types each column holds, and how tables relate. The schema is to data what type annotations are to code — a machine-readable contract.

### SQL is Verifiable

Unlike generated Python, SQL queries can be verified mechanically before touching real data:

1. **Syntax check**: Does the query parse?
2. **Schema check**: Do the referenced tables and columns exist?
3. **Type check**: Are comparisons between compatible types?
4. **Result check**: Does `EXPLAIN` show a reasonable query plan?

This makes SQL ideal for AI-generated code. James could verify every AI-generated query against the schema without running it against production data — the same principle as Pyright catching type errors before runtime.

**Practical tip**: Keep a `schema.sql` file in your project's `docs/` directory — the same knowledge base from Axiom II. When an AI agent needs to work with your data, it reads one file and has the complete map: every table, every column, every relationship, every constraint. Emma called it "the system prompt for your database." James added his on the same day and never removed it — every AI prompt that touched the order system started with `@docs/schema.sql`.

## ORMs: When to Use, When to Avoid

James noticed that his Python code and his SQL schema were expressing the same structure in two languages — his `CustomerOrder` dataclass mirrored his `orders` table. An ORM (Object-Relational Mapper) bridges that gap, letting you define the structure once. In Python, SQLModel (built on SQLAlchemy) is the recommended choice for agentic development because it unifies Pydantic validation with SQLAlchemy's database layer:

```python static
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional
from datetime import datetime

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    email: str

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: str = Field(default="pending")
    total_amount: float
    customer_id: int = Field(foreign_key="customer.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Create database and tables
engine = create_engine("sqlite:///orders.db")
SQLModel.metadata.create_all(engine)

# Use the ORM — James recognized his dataclasses, now backed by a database
with Session(engine) as session:
    customer = Customer(name="Acme Corporation", email="orders@acme.com")
    session.add(customer)
    session.commit()
    session.refresh(customer)

    order = Order(status="shipped", total_amount=149.99, customer_id=customer.id)
    session.add(order)
    session.commit()

    # Query — still readable, maps directly to SQL concepts
    statement = select(Order).where(Order.status != "delivered")
    for order in session.exec(statement):
        print(f"[{order.status}] ${order.total_amount:.2f}")
```

James noticed something: the SQLModel classes looked almost identical to his Axiom V dataclasses. That was the point. The ORM unified his type definitions with his database schema — one structure serving both purposes.

### The ORM Rule

The axiom says: **"Use an ORM only when it doesn't obscure the SQL."**

This means:

| Use the ORM When | Avoid the ORM When |
|-------------------|---------------------|
| CRUD operations (Create, Read, Update, Delete) | Complex analytical queries with multiple JOINs |
| Type safety matters (Python type hints on models) | Performance-critical paths where you need query plan control |
| Schema definition (models as documentation) | You cannot explain what SQL the ORM generates |
| Migrations (Alembic integrates with SQLAlchemy) | The ORM syntax is more complex than raw SQL |

The test is simple: **Can you explain the SQL that your ORM code generates?** If yes, the ORM is adding value. If no, write the SQL directly. A useful heuristic: if you spend more than two minutes reading ORM documentation to express a `JOIN` or `GROUP BY`, the ORM has become the obstacle. Write the SQL.

There is an agentic angle here too. AI agents are significantly better at generating raw SQL than complex ORM-specific syntax. SQL is a constrained, universal language with decades of training data. ORM DSLs — like SQLAlchemy's legacy `session.query(Order).filter(Order.status == 'pending').join(Customer)` — are framework-specific dialects that AI is more likely to hallucinate. When you need AI to write a query, raw SQL is the more agent-native language.

Emma showed James the dividing line with two examples from his own codebase:

```python static
# Good: ORM for simple CRUD — the SQL is obvious
order = session.get(Order, order_id)
order.status = "delivered"
session.commit()

# Better as raw SQL: James's dashboard query (complex aggregation)
cursor.execute("""
    SELECT customers.name, COUNT(orders.id) AS total,
           SUM(orders.total_amount) AS revenue
    FROM customers
    JOIN orders ON orders.customer_id = customers.id
    GROUP BY customers.id ORDER BY revenue DESC
""")
```

## Migrations: Schema Evolution Over Time

Three months after migrating to SQL, James needed to add a `priority` column to the orders table. He could not just edit the `CREATE TABLE` statement — the database already existed with real data. Emma showed him **migrations**: versioned scripts that transform your schema from one state to the next — like version control for your database structure.

Without migrations, schema changes are manual commands run against production databases with no record, no rollback, and no reproducibility. With migrations, every schema change is:

- **Versioned**: Each migration has a sequence number
- **Reversible**: Each migration defines both "upgrade" and "downgrade"
- **Reproducible**: Run all migrations to recreate the database from scratch
- **Auditable**: Git tracks who changed the schema and when

In the Python ecosystem, **Alembic** (built on SQLAlchemy) handles migrations:

```python static
# alembic/versions/001_add_priority_to_tasks.py
"""Add priority column to tasks table"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('tasks', sa.Column('priority', sa.Integer(), nullable=True))
    op.create_index('ix_tasks_priority', 'tasks', ['priority'])

def downgrade():
    op.drop_index('ix_tasks_priority', 'tasks')
    op.drop_column('tasks', 'priority')
```

This migration adds a `priority` column and an index. If something goes wrong, `downgrade()` reverses it cleanly. The migration file lives in version control alongside your code — schema and application evolve together.

## Anti-Patterns

You have seen the JSON graveyard. Every team has one. It is the project folder with `data.json`, `users.json`, `config.json`, and `backup_data_old_FINAL_v2.json` — the one where every new feature means another JSON file, every query means another Python loop, every relationship means another duplicated string.

It is the system where a developer once changed a customer name and broke six months of reports because the name was copied into 2,000 order records instead of referenced by ID. It is the project where the AI agent was asked to "find all orders from last quarter" and generated forty lines of `json.load()`, nested loops, and datetime parsing — code that a single SQL query would replace.

The JSON graveyard was not built by bad developers. It was built by developers who started with twenty records and did not recognize the moment when their data became relational.

| Anti-Pattern | What Goes Wrong | The Fix |
|-------------|-----------------|---------|
| **JSON files as database** | No queries, no relations, no constraints, loads everything into memory | Use SQLite — same simplicity, relational power |
| **NoSQL as default** | Fighting relational data with document model, denormalization headaches | Start relational. Move to NoSQL only for genuinely non-relational data (logs, events, documents) |
| **Raw string SQL** | SQL injection vulnerabilities, crashes on special characters | Always use parameterized queries (`?` placeholders) |
| **No migrations** | Manual schema changes, inconsistent environments, no rollback | Use Alembic or equivalent migration tool |
| **Ignoring indexes** | Queries slow to a crawl as data grows (full table scans) | Index columns used in WHERE, JOIN, and ORDER BY |
| **Over-normalization** | Dozens of tables for simple domains, JOIN-heavy queries for basic reads | Normalize to 3NF, denormalize consciously with measured justification |

## The String Concatenation Trap

James wrote his first search feature using f-strings — `f"SELECT * FROM orders WHERE customer_id = {user_input}"`. Emma stopped him before the code left his machine. "Type this into the search box," she said, and dictated: `'; DROP TABLE orders; --`

James stared at the resulting SQL: `SELECT * FROM orders WHERE customer_id = ''; DROP TABLE orders; --'`. His entire orders table would have been deleted by a user typing thirteen characters into a search box.

"This is SQL injection," Emma told him. "The OWASP Top 10 has listed it as a critical risk for over two decades, and it is still one of the most common vulnerabilities in production software. The rule is absolute: never interpolate user-provided values into SQL strings. Always use parameterized queries."

```python static
# DANGEROUS — SQL injection vulnerability
cursor.execute(f"SELECT * FROM orders WHERE customer_id = '{user_input}'")

# SAFE — parameterized query (the database treats user_input as DATA, never as SQL)
cursor.execute("SELECT * FROM orders WHERE customer_id = ?", (user_input,))
```

Parameterized queries are not optional. They are a non-negotiable safety requirement. This applies to AI-generated code as well — when asking an AI to generate database queries, include in your prompt: "All queries must use parameterized statements. No string interpolation for user input." James added this line to every AI prompt that touched the database.

---

## Try With AI

Use these prompts to build practical understanding of relational data modeling and SQL for agent development.

### Prompt 1: Schema Design (Relational Thinking)

```
I'm building an order management system with these requirements:
- Customers place orders
- Orders contain multiple products (many-to-many via order_items)
- Products have a name, price, and category
- Orders have a status (pending/shipped/delivered), total amount, and creation date
- Each order belongs to exactly one customer

Design the SQLite schema for me. For each table, explain:
1. Why each column exists
2. What constraints protect data integrity (NOT NULL, UNIQUE, CHECK, REFERENCES)
3. How foreign keys express relationships

Then show me 3 queries that demonstrate relational power:
- All pending orders for a specific customer with product details
- Revenue by product category for the last 30 days
- Customers who have never placed an order

Use CREATE TABLE statements with full constraints.
```

**What you're learning**: Relational thinking — how to decompose a domain into entities, identify relationships, and express constraints that prevent invalid data. The many-to-many relationship (orders-to-products) requires a junction table (`order_items`), which is a fundamental pattern you will use repeatedly. You are developing the eye for spotting when data needs to be a table versus a column — the same judgment James lacked when he put customer names inside order records.

### Prompt 2: JSON-to-SQL Migration (Recognizing the Problem)

```
I have this JSON file that stores my project data:

{
  "tasks": [
    {"id": 1, "title": "Design API", "project": "Backend", "assignee": "Alice", "status": "done"},
    {"id": 2, "title": "Write tests", "project": "Backend", "assignee": "Bob", "status": "pending"},
    {"id": 3, "title": "Deploy", "project": "Backend", "assignee": "Alice", "status": "pending"},
    {"id": 4, "title": "UI mockup", "project": "Frontend", "assignee": "Carol", "status": "in_progress"}
  ]
}

Show me:
1. Three questions I CANNOT efficiently answer with this JSON structure
2. The normalized SQL schema that fixes these problems
3. The migration script (Python + sqlite3) that reads the JSON and populates the database
4. The SQL queries that answer those three questions easily

Explain what I gain by moving to SQL and what (if anything) I lose.
```

**What you're learning**: The concrete costs of non-relational storage and the practical process of migrating to SQL. You are also learning to recognize when your data has outgrown its format — a judgment you will apply repeatedly as projects evolve.

### Prompt 3: Schema for Your Domain

```
I work in [describe your domain: e-commerce, healthcare, education, logistics, etc.].

Help me apply relational thinking to my specific context:

1. What are the 3-5 core entities in my domain?
   (In e-commerce: customers, orders, products. In education: students, courses, assignments.)

2. What relationships connect them?
   (One-to-many? Many-to-many? Which need junction tables?)

3. Design a SQLite schema with full constraints (NOT NULL, REFERENCES, CHECK).

4. Write 3 natural language questions a non-technical person might ask about this data,
   then translate each to SQL.

5. Now give me the same data as a JSON structure. Compare:
   - How confident are you generating correct queries against the schema vs the JSON?
   - What errors could happen with JSON that the schema prevents?
   - Which format would you prefer as an AI agent, and why?

Use [my specific technology stack or project type] for the examples.
```

**What you're learning**: How to translate Axiom VI into your own domain. Every field has entities, relationships, and constraints — learning to recognize yours is what transforms the abstract principle into practical architecture. The schema-vs-JSON comparison gives you the direct experience of what James discovered: schemas are specifications that AI agents can reason about, while JSON is unstructured data that AI must guess about.

---

## Key Takeaways

James's `orders.json` — 2,000 records, eleven-second queries, inconsistent customer names — taught him what Edgar Codd formalized in 1970: when data has relationships, a system that understands relationships will always outperform one that does not. Emma's twelve lines of SQL replaced forty lines of Python loops, enforced referential integrity, and gave AI agents a constrained, declarative language to query against.

- **Structured data is relational by nature.** When entities have connections — customers have orders, orders contain products — you have relational data whether or not you store it relationally. JSON files store relational data without understanding it. SQL databases enforce the relationships.
- **SQL is the default for persistent structured data.** Codd's relational model has survived every challenger for more than half a century because it addresses a property of data itself. SQLite for single-user tools and prototypes, PostgreSQL for multi-user production systems. The SQL you write transfers between both.
- **Schemas are type definitions for data.** Just as Axiom V's type annotations give AI a specification for code, SQL schemas give AI a specification for data. Constraints, foreign keys, and CHECK clauses tell the AI exactly what exists, what is valid, and how entities relate — without any additional documentation.
- **The ORM serves you, not the reverse.** If you cannot explain the SQL your ORM generates, write the SQL directly. Use ORMs for CRUD operations and schema management. Use raw SQL for complex queries where you need to see and control the execution plan.
- **Parameterized queries are non-negotiable.** The String Concatenation Trap is not theoretical — thirteen characters in a search box can delete an entire table. Always use parameter placeholders. Always instruct AI agents to do the same.

## Looking Ahead

Your shell orchestrates programs. Your knowledge lives in markdown. Your programs have types and tests. Your systems are composed from focused units. Your types catch structural errors. Your data lives in relational tables with enforced constraints. But how do you know that all of these pieces actually work together? How do you verify that the composed function returns the right result, that the type-checked code handles edge cases, that the SQL query produces correct output — and keeps producing it as the system evolves?

James had types, composition, and relational data. He still shipped a bug that no type checker or database constraint could catch: a function that returned the wrong *value* with the right *type*. In Axiom VII, you will discover that tests are not afterthoughts — they are the specification that defines what "correct" means, and the only layer that catches logical errors before they reach users.
