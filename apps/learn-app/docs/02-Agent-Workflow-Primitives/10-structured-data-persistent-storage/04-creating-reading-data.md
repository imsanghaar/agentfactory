---
sidebar_position: 4
title: "Creating & Reading Data"
chapter: 10
lesson: 3
duration_minutes: 25
description: "Implement reliable CREATE and READ patterns with SQLAlchemy sessions"
keywords: ["SQLAlchemy", "Session", "CRUD", "select", "rollback"]
skills:
  - name: "CRUD Operations"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can create rows, read them back in new sessions, and handle write failures with rollback"
  - name: "Session Lifecycle Management"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can explain the session lifecycle: open, add, flush, commit/rollback, close"
learning_objectives:
  - objective: "Insert a row and read it back in a separate session"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student inserts an expense and confirms it exists via a new session query"
  - objective: "Handle write failures with explicit rollback"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student demonstrates try/except/rollback pattern with invalid FK insert"
cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (session lifecycle, commit vs flush, rollback on failure, select query patterns) within A2 limit"
differentiation:
  extension_for_advanced: "Implement a full CRUD module with update and delete operations. Add a function that demonstrates the difference between .flush() and .commit() with concurrent sessions."
  remedial_for_struggling: "Focus on the happy path first: insert one row, read it back. Only after that works, try the failure case. The rollback pattern is important but secondary to basic CRUD."
teaching_guide:
  lesson_type: "hands-on"
  session_group: 2
  session_title: "CRUD and Session Discipline"
  key_points:
    - "The session lifecycle (open, add, flush, commit/rollback) is the mental model that prevents most CRUD bugs"
    - "flush() assigns IDs without committing — needed when creating parent rows before inserting children that reference them"
    - "Rollback is not error recovery — it is the expected path for failed writes and must be practiced, not just understood"
    - "Reading back in a new session is the only reliable proof that data was committed, not just cached in memory"
  misconceptions:
    - "Students assume session.add() saves data — it only stages the object in memory; commit() is required for durability"
    - "Students think commit failure is rare — duplicate emails, invalid FKs, and constraint violations happen routinely in production"
    - "Students confuse .first() with .all() thinking they are interchangeable — .first() silently hides multiple matches"
    - "Students skip the SQLite PRAGMA foreign_keys=ON and wonder why invalid FK inserts succeed locally"
  discussion_prompts:
    - "Why is practicing the failure path (rollback after bad FK) just as important as the happy path? In production, which happens more often?"
    - "What is the difference between flush and commit? When would you need flush without immediately committing?"
  teaching_tips:
    - "Walk through the session lifecycle diagram step by step — have students identify which stage their code is at before running it"
    - "The shopping cart analogy for sessions is powerful: add() = put items in cart, flush() = preview total, commit() = place order, rollback() = empty cart"
    - "Have students deliberately skip session.commit() and observe that read-back returns nothing — this makes the commit requirement visceral"
    - "The PRAGMA foreign_keys=ON listener is easy to overlook — demo what happens without it by inserting a bad FK that silently succeeds"
  assessment_quick_check:
    - "What happens to your data if you call session.add() but never call session.commit()?"
    - "Write the try/except/rollback pattern from memory for a write that might fail"
    - "When should you use .first() vs .all() and what bug can .first() hide?"
---

# Creating & Reading Data

In the previous lesson, you defined your models as Python classes. Tables exist, columns have types, constraints are in place. But a schema without data is like a filing cabinet with labeled drawers and nothing inside. Now you'll put data in and get it back out -- reliably.

You might be thinking: "Why can't I just `session.add()` and move on?" Because adding without committing is like writing a check without signing it -- the bank won't process it. And if something goes wrong mid-write, you need a way to tear up that check cleanly. That's what this lesson is about: the session lifecycle that makes database writes trustworthy.

:::info[Key Terms for This Lesson]
- **CRUD**: Create, Read, Update, Delete -- the four basic operations every database application needs
- **Session**: A workspace for database operations -- think of it as a shopping cart where you add items before checking out (committing)
- **Commit vs Flush**: `flush()` sends your changes to the database temporarily (like previewing your cart). `commit()` makes them permanent (like clicking "Place Order"). If anything fails, `rollback()` empties the cart.
- **Rollback**: Undo all uncommitted changes in the current session -- your safety net when writes go wrong
:::

## The Session Lifecycle

Before you write a single row, understand the machine you're working with. A session moves through a predictable sequence, and knowing where you are in that sequence prevents most beginner CRUD bugs.

```
Session Lifecycle:

  open          add/modify       flush          commit
   |               |               |              |
   v               v               v              v
+------+    +-----------+    +----------+    +----------+
| New  |--->|  Pending   |--->| Flushed  |--->| Committed|
|Session|    |  Changes   |    | (in DB   |    | (durable)|
+------+    +-----------+    | but not  |    +----------+
                              | permanent)|
                              +-----+----+
                                    | error?
                                    v
                              +----------+
                              | Rollback |
                              | (undo    |
                              |  all)    |
                              +----------+
```

Here's what each stage means in plain language:

1. **Open**: You create a session. Nothing has happened yet.
2. **Pending**: You call `session.add()`. The object is tracked in memory, but the database hasn't seen it.
3. **Flushed**: You call `session.flush()`. SQLAlchemy sends the SQL to the database and the database assigns IDs -- but this is a preview, not a commitment. If the session ends without a commit, the changes vanish.
4. **Committed**: You call `session.commit()`. The transaction finalizes. The data is durable -- it survives restarts, crashes, power outages.
5. **Rollback**: Something went wrong. You call `session.rollback()`, and every pending or flushed change in that session is undone. Clean slate.

Why does flush exist separately from commit? Because sometimes you need the database to assign an ID (like an auto-incrementing primary key) before you can create related rows -- but you don't want to commit until everything succeeds. That's exactly what happens in the code below.

## The Happy Path: Insert and Read Back

Here's the pattern you'll use hundreds of times. Create some rows, commit them, then prove they exist by reading them in a fresh session.

```python
from datetime import date
from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String, create_engine, event, select
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, nullable=False, default=date.today)


engine = create_engine("sqlite:///:memory:")


@event.listens_for(engine, "connect")
def _enable_sqlite_fk(dbapi_connection, _connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Base.metadata.create_all(engine)

with Session(engine) as session:
    user = User(email="alice@example.com", name="Alice")
    food = Category(name="Food")
    session.add_all([user, food])
    session.flush()

    session.add(
        Expense(
            user_id=user.id,
            category_id=food.id,
            description="Groceries",
            amount=52.50,
            date=date(2024, 1, 15),
        )
    )
    session.commit()

with Session(engine) as session:
    rows = session.execute(select(Expense).where(Expense.amount >= 50)).scalars().all()
    print([(r.description, str(r.amount)) for r in rows])
```

**Output:**

```text
[('Groceries', '52.50')]
```

Walk through the key moments:

- `session.add_all([user, food])` stages both objects. Nothing hits the database yet.
- `session.flush()` sends the INSERT statements to the database. Now `user.id` and `food.id` have real values (the database assigned them). But the transaction is still open -- this is the "preview your cart" step.
- `session.add(Expense(...))` uses those freshly assigned IDs. Without the flush, `user.id` would still be `None`.
- `session.commit()` finalizes everything. Now the data is permanent.
- The second `with Session(...)` block opens an entirely new session. If the data shows up here, it's genuinely committed -- not just cached in memory.

The `.scalars()` call deserves a quick explanation: when you run `session.execute(select(Expense))`, SQLAlchemy returns rows wrapped in a result object. The `.scalars()` call unwraps them -- think of it as opening the envelope to get the letter inside. Without it, you'd get `Row` objects instead of `Expense` objects.

(A note about that `PRAGMA foreign_keys=ON` listener: SQLite disables foreign key enforcement by default. The listener turns it on for every connection so your local development catches the same FK violations that PostgreSQL would catch in production. Without it, you could insert an expense pointing to a nonexistent user and SQLite would happily accept it -- a nasty surprise when you deploy.)

## Read-Path Verification Checklist

Don't trust that your writes worked just because no error appeared. Trust the read:

1. Write one known row with deterministic values
2. Read that row in a new session
3. Assert expected field values, not only row count
4. Run one failing FK insert and verify the rollback path
5. Repeat the read to prove the failed write left no residue

This simple loop prevents most beginner CRUD illusions -- the cases where you think data was saved but it was only in memory, or where a failed write silently corrupted your session state.

## The Failure Path: Rollback in Action

You might be thinking: "When would commit actually fail?" More often than you'd hope -- duplicate emails, invalid foreign keys, network hiccups. The question isn't IF it fails, it's WHEN.

Here's what a controlled failure looks like:

```python
with Session(engine) as session:
    try:
        bad_row = Expense(
            user_id=9999,  # invalid
            category_id=1,
            description="Invalid FK demo",
            amount=10.00,
        )
        session.add(bad_row)
        session.commit()
    except Exception as exc:
        session.rollback()
        print(type(exc).__name__)
```

**Output:**

```text
IntegrityError
```

The database rejects the row because `user_id=9999` doesn't exist in the `users` table (that's your foreign key constraint doing its job). The `session.rollback()` call undoes everything in this session's transaction, leaving the database exactly as it was before.

Running one controlled failure now saves hours of confusing downstream debugging later. `session.add()` without `commit` is the database equivalent of "I'll save my file later." We all know how that story ends.

Use this pattern whenever a write might fail:

```python
try:
    session.add(expense)
    session.commit()
except Exception:
    session.rollback()
    raise
```

**Output:**

(Re-raises the original exception after rolling back cleanly.)

Also avoid reusing failed session state after exception paths. Rollback first, then continue or open a new session.

:::tip[Pause and Reflect]
You've seen both a successful insert and a failed one. Why is the failure case just as important to practice? In production, which scenario do you think happens more often -- and what happens if you don't handle it?
:::

## Query Patterns for Reading

Once data is committed, you need flexible ways to get it back. Here are the patterns you'll reach for most often:

```python
# one row or None
one = session.execute(select(Category).where(Category.name == "Food")).scalars().first()

# many rows
many = session.execute(select(Category)).scalars().all()

# range query
march_rows = session.execute(
    select(Expense).where(Expense.date >= date(2024, 3, 1), Expense.date < date(2024, 4, 1))
).scalars().all()
```

**Output:**

```text
# one: <Category name='Food'> (or None if not found)
# many: [<Category name='Food'>]
# march_rows: [] (no March expenses in our data)
```

Use `.first()` when you expect zero or one result. Use `.all()` when you expect a list. If you use `.first()` on a query that could match many rows, you'll silently get just the first one -- which might hide bugs where your filter isn't specific enough.

Think of it this way: imagine building a user registration system. When checking if an email already exists, `.first()` is exactly right -- you only need to know if at least one match exists. But when listing all users in an admin panel, `.all()` is what you want. Picking the wrong one doesn't crash your program; it just gives you misleading results, which is worse.

Or consider a project tracker where tasks get created, assigned, completed, and archived. Every one of those operations is a CRUD operation with this same session pattern: open, add or query, commit or rollback, close.

## Debugging Patterns

When things don't work as expected, check these in order:

- **If reads are empty**, verify commit happened. A missing `session.commit()` means your data exists only in the session's memory.
- **If FK errors don't appear locally**, verify the SQLite FK pragma is enabled. Without `PRAGMA foreign_keys=ON`, SQLite silently accepts invalid foreign keys.
- **If one query "sometimes" works**, check whether `.first()` is hiding multiple matches that should have been constrained by a unique index.

Good beginner habit: print small deterministic result sets while learning. Switch to assertions once behavior is stable. This keeps debugging concrete and avoids "it looked right" mistakes.

## Micro-Check Before Moving On

Before you continue to the next lesson, verify these three things:

- Can you insert one valid row and read it back in a new session?
- Can you trigger one invalid row (bad FK) and handle it with rollback?
- Can you explain why both outcomes are useful to practice?

**What breaks next?** Single-table CRUD is stable now. The next risk is cross-table truth: relationships and query shape.

## Try With AI

### Prompt 1: CRUD Sanity Check

```text
Given this SQLAlchemy CRUD code, find correctness risks:
- missing commit
- missing rollback
- FK misuse
- wrong assumptions about .first() vs .all()
Provide corrected code.
```

**What you're learning:** You're developing an eye for the subtle bugs that slip past "it runs without errors." AI is good at spotting patterns like missing rollbacks or commit-before-flush issues -- this is AI as code reviewer, catching what human eyes skip during the "it works on my machine" phase.

### Prompt 2: Add a Safe Read Pattern

```text
Add a function list_expenses_over(amount) that returns
[(description, amount)] using SQLAlchemy 2.0 select() style.
Include one test query example and expected output.
```

**What you're learning:** Writing query functions that return clean data structures (not raw SQLAlchemy objects) is how production code stays testable. You're practicing the pattern of wrapping database access in functions with predictable inputs and outputs.

### Prompt 3: Apply to Your Domain

```text
Pick a project you're building. Write the CRUD operations for your main entity:
1. A create function that inserts one row with validation
2. A read function that queries by one filter condition
3. A failure case that tests what happens with invalid data
Show the expected output for each operation.
```

**What you're learning:** CRUD is the bread and butter of every database app. The session, add, commit/rollback pattern you're learning here is the same pattern used in production systems serving millions of users. Master it once, use it everywhere.
