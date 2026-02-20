---
sidebar_position: 3
title: "Models as Code"
chapter: 10
lesson: 2
duration_minutes: 25
description: "Define SQLAlchemy models as executable schema contracts"
keywords: ["SQLAlchemy", "ORM", "models", "ForeignKey", "Numeric"]
skills:
  - name: "Schema Design"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can define SQLAlchemy models with correct types, constraints, and foreign keys"
  - name: "Type Safety for Financial Data"
    proficiency_level: "A1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Data Literacy"
    measurable_at_this_level: "Student can explain why Numeric is required for money and why Float introduces errors"
learning_objectives:
  - objective: "Create a complete SQLAlchemy model file with correct types and constraints"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student runs models.py and creates tables without errors"
  - objective: "Explain why Numeric(10,2) is used instead of Float for financial values"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Student can demonstrate the float precision problem and explain the fix"
cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (nullable constraint, Numeric vs Float, ForeignKey, declarative model) within A2 limit"
differentiation:
  extension_for_advanced: "Design a project management schema (User -> Project -> Task -> TimeEntry) with appropriate types, then compare with a classmate's design choices."
  remedial_for_struggling: "Focus on just the User model first. Add one constraint at a time (nullable, unique) and test each. Only add Category and Expense after User works."
teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "From Scripts to Databases"
  key_points:
    - "Float vs Numeric is the single most common money bug — 0.1 + 0.2 != 0.3 in floating point, and it compounds at scale"
    - "A model file is an executable contract, not documentation — the database enforces it on every insert and update"
    - "nullable=False is the bouncer at the door; app-level validation is a polite sign — students must understand which to trust"
    - "Foreign keys store IDs not names — if Alice changes her email, you update one row instead of 500 expense rows"
  misconceptions:
    - "Students think rounding floats solves the money problem — it shifts responsibility to the developer for every calculation, which is error-prone"
    - "Students confuse the model file with documentation — it is runnable code that creates real database constraints"
    - "Students want to store user names directly in expense rows instead of using foreign key references — leads to update anomalies"
    - "Students assume nullable=True is a safe default — it allows empty required fields that cause downstream query bugs"
  discussion_prompts:
    - "If 0.1 + 0.2 produces 0.30000000000000004, what happens when you sum a million transactions? At what scale does this matter?"
    - "Why does the Expense model reference users.id instead of storing Alice's name directly? What breaks when Alice changes her email?"
    - "When would you choose nullable=True intentionally? Can you think of a field where 'no value' is meaningful, not just lazy?"
  teaching_tips:
    - "Start with the live Python shell demo: type 0.1 + 0.2 and watch students react — this makes the Float problem visceral"
    - "The ER diagram is whiteboard-worthy — draw it and have students identify which lines are foreign keys and why"
    - "Walk through the type selection guide as a decision tree, not a reference table — ask students to classify fields from their own domains"
    - "The manual validation drill (step 3: insert duplicate email) is critical — students must see the database reject bad data"
  assessment_quick_check:
    - "What type should you use for a monetary amount column and why?"
    - "Explain what nullable=False does that app-level validation cannot guarantee"
    - "Why does the Expense table store user_id instead of the user's name?"
---

# Models as Code

In Lesson 1, you proved that data survives a process restart. Now you need to answer a harder question: what shape should that data take, and who enforces the rules?

Quick test: open a Python shell and type `0.1 + 0.2`. Did you get `0.3`? You did not. You got `0.30000000000000004`. Welcome to floating-point arithmetic -- and the reason your money column needs `Numeric`, not `Float`.

That tiny rounding error does not sound like much until you process a million transactions. At one hundred-thousandth of a cent per transaction, you are off by ten dollars. At a billion transactions, you are off by ten thousand. Banks do not tolerate "close enough," and neither should your budget tracker.

:::info[Key Terms for This Lesson]
- **Nullable**: Whether a field can be left empty -- `nullable=False` means "this field is REQUIRED, period"
- **Constraint**: A rule the database enforces automatically -- like a bouncer that rejects bad data before it gets in
- **Numeric(10, 2)**: A decimal type that stores up to 10 digits with exactly 2 decimal places -- precise enough for dollars and cents without floating-point surprises
:::

## The Float Problem (And Its Fix)

You might be thinking: "Can't I just round the floats?" You can. But rounding is YOUR responsibility. Every calculation, every sum, every comparison -- you have to remember to round. Miss one spot and your totals drift. With `Numeric(10, 2)`, the database handles precision for you. Every value stored, every calculation performed, exact to two decimal places. No discipline required.

Here is the difference in practice:

```python
# Float: your problem
a = 0.1 + 0.2
print(a)           # 0.30000000000000004
print(a == 0.3)    # False (!)

# Numeric(10, 2): database's problem
# Stored as exact decimal: 0.30
# Comparisons work: 0.30 == 0.30 → True
```

**Output:**
```
0.30000000000000004
False
```

Float for money is how you lose $0.00000000004 on every transaction. Doesn't sound like much until you process a million of them.

## The Schema Contract

A model file is not documentation. It is a contract your database enforces on every insert, every update, every foreign key reference. If the data violates the contract, it gets rejected -- no exceptions, no "I forgot to validate in the app layer."

Here is what our budget tracker needs:

```
Entity-Relationship Diagram:

┌──────────────┐         ┌──────────────┐
│    User      │         │   Category   │
├──────────────┤         ├──────────────┤
│ id (PK)      │         │ id (PK)      │
│ email (UQ)   │         │ name (UQ)    │
│ name         │         │ color        │
│ created_at   │         └──────┬───────┘
└──────┬───────┘                │
       │                        │
       │ 1:many                 │ 1:many
       │                        │
       ▼                        ▼
┌──────────────────────────────────┐
│           Expense                │
├──────────────────────────────────┤
│ id (PK)                          │
│ user_id (FK → users.id)         │
│ category_id (FK → categories.id)│
│ description                      │
│ amount: Numeric(10,2)           │
│ date                             │
│ created_at                       │
└──────────────────────────────────┘

PK = Primary Key, FK = Foreign Key, UQ = Unique
```

Three entities. Two foreign keys. One money column that uses exact decimals. This is the shape of every expense that enters your system.

:::tip[Pause and Reflect]
Look at the Expense model. Why does it reference `users.id` and `categories.id` instead of storing the user's name and category name directly? What would go wrong if Alice changed her email and you had her name stored in 500 expense rows?
:::

## The Model File

Here is the complete, runnable model file. Every line is a decision about what your database will and will not accept.

```python
from datetime import date, datetime, timezone

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    color = Column(String(7), default="#FF6B6B", nullable=False)


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, default=date.today, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)


if __name__ == "__main__":
    engine = create_engine("sqlite:///budget_tracker.db")
    Base.metadata.create_all(engine)
    print("Schema created")
```

**Output:**
```
Schema created
```

Every `nullable=False` is a decision: this field is required. Period. You could enforce that in application code instead, but application code has bugs, gets bypassed, and changes over time. A database constraint is permanent. (Think of it this way: `nullable=False` is the bouncer at the door. App-level validation is a polite sign that says "please don't enter without a ticket." Which one do you trust more?)

## Type Selection Guide

Choosing the right type is not about what Python supports. It is about what the data means to the business.

| Business meaning | Recommended SQLAlchemy type | Why |
|---|---|---|
| Monetary value | `Numeric(10, 2)` | Exact decimal behavior |
| Optional free-form note | `String(...)` or `Text` | Human-readable variable content |
| Status flag | `Boolean` | Explicit two-state logic |
| User-facing code | `String(..., unique=True)` | Stable lookup and duplicate prevention |
| Event time | `DateTime` (UTC default) | Ordering and incident traceability |

The pattern is consistent: pick the type that makes invalid data impossible, not the type that is easiest to type.

## Same Patterns, Different Domains

These model patterns are not specific to budget tracking. The same decisions appear everywhere:

**Project management** (User, Project, Task, TimeEntry):
- `hours` uses `Numeric(6, 2)` -- not Float -- because billable hours need exact decimals
- `task.project_id` is a ForeignKey -- you cannot log time against a project that does not exist
- `email` is `unique=True, nullable=False` -- no duplicate accounts, no anonymous users

**E-commerce** (Customer, Order, Product):
- `price` uses `Numeric(10, 2)` -- same money rule
- `order.customer_id` is a ForeignKey -- orphan orders break every report
- `sku` is `String(50), unique=True` -- duplicate SKUs cause warehouse chaos

The entities change. The type decisions stay the same. Money is always `Numeric`. References are always foreign keys. Required fields are always `nullable=False`.

## Schema Contract Checklist

Before you move on, verify your model file against this checklist:

- every foreign key points to a real primary key
- every required business field uses `nullable=False`
- every row that must be unique has a uniqueness constraint
- financial fields avoid float semantics
- timestamp defaults are explicit and timezone-aware

## Manual Validation Drill

Run these steps to prove your schema works as promised:

1. Run `python models.py` to create the schema
2. Inspect tables in SQLite shell or DB browser
3. Try inserting two users with the same email -- confirm the database rejects the second
4. Try inserting an expense with a missing `category_id` -- confirm it fails
5. Confirm error messages match your expectations

This drill trains you to trust constraints that are proven, not assumed. If a constraint does not reject bad data when you test it, it is not a constraint -- it is a suggestion.

**What breaks next?** With schema in place, write paths become the main risk. Lesson 3 tackles session discipline: how to create and read data without leaving the database in a half-written state.

## Try With AI

### Prompt 1: Model Review

```text
Review this SQLAlchemy model file for beginner-breaking mistakes:
- missing imports
- wrong money type
- weak nullability constraints
- missing foreign keys
Return fixes with explanations.
```

**What you're learning:** Code review is a skill that transfers to every project. By asking AI to review your model file, you learn to spot the same mistakes yourself -- missing constraints, wrong types, broken references. The AI catches what you miss today so you catch it yourself tomorrow.

### Prompt 2: Requirement to Model

```text
Convert this requirement into a runnable SQLAlchemy model file:
users, projects, and time_entries.
Use exact decimal for billable hours, enforce foreign keys, and include created_at timestamps.
```

**What you're learning:** Translating business requirements into typed models is the core skill of schema design. The gap between "we need to track time" and a correct model file is where most bugs hide. Practicing this translation builds the muscle memory to get it right on the first try.

### Prompt 3: Apply to Your Domain

```text
Think of a real project you want to build. What are the 2-3 main "things" (entities) it tracks? For each entity, list the fields you'd need and whether each should be required (nullable=False) or optional. Which fields handle money? Which need to be unique? Turn your answers into SQLAlchemy model classes.
```

**What you're learning:** Model design is the foundation of every database application. The skill of translating business requirements into typed, constrained models transfers to any domain -- from healthcare records to inventory systems to social networks.

### Safety Note

Never run model files that drop or recreate tables against a production database. The `create_all` call in this lesson is safe for new databases, but on an existing database with real data, it can silently skip schema changes or, worse, destroy data if combined with `drop_all`. Always use migration tools (like Alembic) for production schema changes.
