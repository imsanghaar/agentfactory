---
sidebar_position: 5
title: "Relationships & Joins"
chapter: 10
lesson: 4
duration_minutes: 30
description: "Define relationships correctly and query linked data without ambiguity"
keywords: ["relationship", "join", "back_populates", "N+1", "SQLAlchemy 2.0"]
skills:
  - name: "Relationship Definition"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can define bidirectional relationships with matching back_populates and appropriate cascade policies"
  - name: "Join Query Construction"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Data Literacy"
    measurable_at_this_level: "Student can write join queries that filter by related table fields using SQLAlchemy 2.0 style"
  - name: "N+1 Detection and Prevention"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can identify N+1 patterns in existing code and apply selectinload to fix them"
learning_objectives:
  - objective: "Define bidirectional relationships with matching back_populates"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student can create linked models where navigation works in both directions"
  - objective: "Write join queries that filter by related table fields"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student can filter expenses by category name using explicit join"
  - objective: "Identify and fix N+1 query anti-patterns"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can spot lazy-loading loops and apply selectinload"
cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (relationship, back_populates, join query, N+1 pattern, selectinload) — cascade and delete-orphan are referenced but treated as advanced extensions"
differentiation:
  extension_for_advanced: "Implement a blog system (Author → Post → Comment) with cascading deletes and benchmark query counts with and without selectinload."
  remedial_for_struggling: "Focus on Section A only (relationships and back_populates). Return to Section B (joins and N+1) after practicing the checkpoint items for Section A."
teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "CRUD and Session Discipline"
  key_points:
    - "back_populates strings must match the attribute name on the other model exactly — a mismatch is a silent bug, not an error"
    - "Cascade policy is a business decision: delete-orphan makes sense for expenses (meaningless without user) but is dangerous for shared entities like categories"
    - "The N+1 problem turns 2 queries into 101 at scale — selectinload fixes it with one line but students must learn to spot the pattern first"
    - "Use relationship attributes for navigation (you have one thing, want its related things) and .join() for filtering across tables"
  misconceptions:
    - "Students think N+1 is a rare edge case — it appears in almost every loop that accesses relationship attributes and only surfaces at scale"
    - "Students assume cascade='all, delete-orphan' is always correct — it depends on whether child rows have meaning without their parent"
    - "Students confuse the relationship declaration with the ForeignKey column — the FK column stores the link, the relationship provides Python navigation"
    - "Students think back_populates errors will raise exceptions — SQLAlchemy often silently accepts mismatches and just behaves unpredictably"
  discussion_prompts:
    - "If you delete a user, should their expenses be deleted too? What about their comments on a shared forum? How do you decide cascade policy?"
    - "Your app works fine with 5 users but crawls with 500 — what is the first thing you check and why?"
    - "When would you use user.expenses vs select(Expense).join(User).where(...)? What makes the decision?"
  teaching_tips:
    - "Split the lesson at the marked break — master Section A before moving to Section B, especially for struggling students"
    - "The N+1 diagram is the centerpiece of Section B — draw the 101-query side vs the 2-query side and let the visual impact land"
    - "Have students count actual queries for 5 users without selectinload, then with — making the optimization measurable builds conviction"
    - "The two-way street analogy for back_populates is effective — draw two roads connecting User and Expense with matching street names"
  assessment_quick_check:
    - "If User.expenses has back_populates='user', what must Expense.user have?"
    - "How many queries does a loop over 100 users accessing user.expenses fire without selectinload?"
    - "Name one relationship where cascade delete-orphan is correct and one where it is dangerous"
---

# Relationships & Joins

:::caution[This lesson introduces several connected concepts. Take your time.]
Relationships, joins, and N+1 patterns are interconnected. This lesson is split into two sections so you can master each piece before combining them.
:::

In Lesson 3, you proved that rows exist by creating and reading them back. Now you will prove that rows *belong together* correctly. A user's expenses should belong to that user, not float around unattached. A category should link to its expenses so you can ask "show me all Food purchases" in a single query.

Here is the trap: your app runs fine with 5 users. Then you get 500 users, and suddenly it is making 501 database calls instead of 2. Nobody changed any code. What happened? That is the N+1 problem, and by the end of this lesson you will know exactly how to spot it and fix it.

:::info[Key Terms for This Lesson]
- **Relationship**: A declared link between two models that lets you navigate from one to the other in Python code — like a contact card that links a person to their company
- **back_populates**: The setting that makes a relationship work in BOTH directions — if User knows about Expenses, Expenses also know about their User
- **Cascade**: Rules that automatically propagate changes — when you delete a User, what happens to their Expenses?
- **N+1 problem**: A hidden performance trap where loading 100 parents triggers 100 separate child queries instead of 1 — your app works fine until it suddenly doesn't
- **selectinload**: SQLAlchemy's fix for N+1 — it prefetches related data in a single efficient query
:::

---

## Section A: Relationships and back_populates

### Why Relationships Break Silently

If relationships are missing or misconfigured, your app will often still run. The danger is quiet corruption:

- Totals tied to the wrong user
- Categories resolved inconsistently
- Delete behavior that surprises production systems

This is where many "it worked in test" systems fail after launch. Wrong relationships produce believable analytics that are still wrong.

### Defining Bidirectional Relationships

The goal is simple: define the link once, navigate it from either side. When you have a `User` and want their expenses, you write `user.expenses`. When you have an `Expense` and want its owner, you write `expense.user`. The `back_populates` parameter connects these two directions.

Here are the models that make this work:

```python
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, create_engine, select
from sqlalchemy.orm import Session, declarative_base, relationship, selectinload

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    expenses = relationship("Expense", back_populates="category")


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)

    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    alice = User(email="alice@example.com")
    food = Category(name="Food")
    session.add_all([alice, food])
    session.flush()

    expense = Expense(user_id=alice.id, category_id=food.id, description="Lunch", amount=12.50)
    session.add(expense)
    session.commit()

    # Navigate from user to expenses
    print(f"Alice's expenses: {len(alice.expenses)}")
    # Navigate from expense to user
    print(f"Expense owner: {alice.expenses[0].user.email}")
```

**Output:**
```
Alice's expenses: 1
Expense owner: alice@example.com
```

Notice the symmetry. On the `User` side, `expenses = relationship("Expense", back_populates="user")` declares "I have many expenses." On the `Expense` side, `user = relationship("User", back_populates="expenses")` declares "I belong to one user." The string you pass to `back_populates` must match the attribute name on the other model exactly. If `User.expenses` says `back_populates="user"`, then `Expense.user` must say `back_populates="expenses"`. A mismatch here is a silent bug — SQLAlchemy may not raise an error, but navigation will behave unpredictably.

The `cascade="all, delete-orphan"` on `User.expenses` means: if you delete a User, automatically delete their Expenses too. This makes sense for expenses (an expense without a user is meaningless), but would be dangerous for categories (deleting a category should not wipe out every expense ever tagged with it). Cascade policy is a business decision, not a technical default.

<details>
<summary>If you're stuck on back_populates</summary>

Think of it like a two-way street sign. `User.expenses` is the road from User to Expense. `Expense.user` is the road back. `back_populates` tells SQLAlchemy these two roads connect the same relationship. Without it, SQLAlchemy treats them as two separate, unrelated relationships — changes on one side would not reflect on the other within the same session.

</details>

### When to Use Relationships vs Joins

You now have two ways to access related data. Here is when to use each:

| Need | Recommended pattern |
|---|---|
| You already loaded one `User` and need that user's expenses | `user.expenses` (relationship attribute) |
| You need all expenses where `Category.name == "Food"` | `select(Expense).join(Category).where(...)` (explicit join) |
| You need a report grouped by category | Grouped select with explicit joins and aggregates |

The rule: use relationship attributes for object navigation (you have one thing, you want its related things). Use `.join()` when filtering or aggregating across tables.

```python
with Session(engine) as session:
    # Join query: filter expenses by category name
    food_expenses = session.execute(
        select(Expense).join(Category).where(Category.name == "Food")
    ).scalars().all()

    print(f"Food expenses: {len(food_expenses)}")
```

**Output:**
```
Food expenses: 1
```

---

:::tip[Pause and Reflect]
If relationships and back_populates make sense, continue to Section B. If not, re-read Section A and try defining a relationship between two models of your own choosing before moving on.
:::

---

## Section B: Joins, N+1, and selectinload

### The N+1 Problem

You might be thinking: "Why can't I just loop through each user and access their expenses?" You can. And it will work. Until it won't.

Every developer discovers N+1 the hard way — usually at 2am when the staging server is crawling. Here is what happens:

```
N+1 Problem (100 users):

Without selectinload:          With selectinload:
┌─────────────────┐           ┌─────────────────┐
│ SELECT * FROM   │           │ SELECT * FROM   │
│ users           │ 1 query   │ users           │ 1 query
└────────┬────────┘           └────────┬────────┘
         │                             │
    ┌────┴────┐                   ┌────┴────┐
    │ For each│                   │ SELECT * │
    │ user... │                   │ FROM     │
    └────┬────┘                   │ expenses │
         │                        │ WHERE    │
  ┌──────┼──────┐                 │ user_id  │ 1 query
  │      │      │                 │ IN (...)│
  v      v      v                 └─────────┘
query  query  query
  1      2    ...100              Total: 2 queries
                                  vs 101 queries!
Total: 101 queries
```

When you access `user.expenses` inside a loop, SQLAlchemy fires a separate query for each user. With 5 users that is 6 queries — barely noticeable. With 500 users that is 501 queries, and your response time goes from milliseconds to seconds.

Here is the anti-pattern in code:

```python
# N+1 ANTI-PATTERN — do not use in production
users = session.execute(select(User)).scalars().all()
for u in users:
    for e in u.expenses:   # Each iteration triggers a new SELECT
        ...
```

**Output (what the database sees):**
```
SELECT * FROM users                           -- 1 query
SELECT * FROM expenses WHERE user_id = 1      -- query 2
SELECT * FROM expenses WHERE user_id = 2      -- query 3
...
SELECT * FROM expenses WHERE user_id = 100    -- query 101
```

### The Fix: selectinload

The fix is one line. Tell SQLAlchemy to prefetch the related data in a single batch query:

```python
# FIXED — selectinload prefetches all expenses in one query
users = session.execute(
    select(User).options(selectinload(User.expenses))
).scalars().all()

for u in users:
    for e in u.expenses:   # No extra queries — data already loaded
        ...
```

**Output (what the database sees):**
```
SELECT * FROM users                                          -- 1 query
SELECT * FROM expenses WHERE user_id IN (1, 2, 3, ... 100)  -- 1 query
-- Total: 2 queries regardless of user count
```

The performance signal to monitor: if response time rises with user count more than linearly, inspect for hidden N+1 paths first. Optimize query shape before adding infrastructure.

### Practical Review Question

If a teammate adds a report loop that touches `user.expenses` for each user, ask:

1. What query count does this produce at 10, 100, and 1,000 users?
2. Can we prefetch or aggregate in one query shape?

That question alone catches many early performance regressions.

---

## Common Failures and Safety Reminders

**Cascade safety reminder:**

- `delete-orphan` can be correct for child rows that have no meaning without their parent (expenses without a user)
- It can be dangerous for shared entities or audit records (categories shared by many expenses)
- Always test delete behavior on non-production data before rollout

**Relationship test plan** — treat this as a contract test suite for relationship correctness:

1. Create one user and two categories
2. Create expenses linked to both categories
3. Query via `user.expenses` and verify count
4. Query via `join(Category)` and verify filtered set
5. Remove one expense from the relationship collection and verify expected cascade behavior

### Alternative Domains

These same patterns apply everywhere:

- **Blog system**: Author → Post → Comment. An author has many posts, each post has many comments. Deleting an author cascades to their posts and comments.
- **E-commerce**: Customer → Order → LineItem → Product. An order has many line items, but deleting an order should not delete the products (shared entities).

The relationship and cascade decisions are always business decisions first, technical decisions second.

**What breaks next?** Once linked reads are correct, write safety becomes the next boundary. Multi-step operations need atomic transactions — that is Lesson 5.

## Try With AI

**Setup:** Open Claude or ChatGPT with your budget tracker models from this chapter.

### Prompt 1: Relationship Contract Review

```text
Here are my SQLAlchemy models:

[paste your User, Category, and Expense models]

Review them and verify:
1) back_populates matches both sides exactly
2) FK columns match referenced PK types
3) cascade policy is explicit and justified for each relationship

Return corrected code if any mismatch exists.
```

**What you're learning:** You are practicing the skill of using AI as a code reviewer for structural correctness. Relationship mismatches are hard to spot by eye because SQLAlchemy often does not raise errors — it just behaves wrong. AI excels at this kind of pattern-matching verification.

### Prompt 2: N+1 Detection

```text
Here is a reporting function that loads users and prints their expenses:

[paste a loop that accesses user.expenses without selectinload]

1. Identify the N+1 problem in this code
2. Show the fixed version using selectinload
3. Explain how many queries the original fires for 100 users vs the fix
```

**What you're learning:** You are building the instinct to recognize N+1 patterns before they reach production. The AI can explain the query count math, but the real skill is learning to see the pattern yourself — a loop that accesses a relationship attribute is always suspicious.

### Prompt 3: Design Relationships for Your Domain

```text
I'm building a [describe your project — e.g., recipe manager, task tracker, inventory system].

Help me define SQLAlchemy relationships between these entities:
[list your entities]

For each relationship:
- Should it be one-to-many or many-to-many?
- What cascade policy makes business sense?
- Which side gets back_populates?

Show me the complete model code.
```

**What you're learning:** You are moving from following examples to making relationship design decisions for your own domain. The AI helps you think through cascade policies and cardinality, but the business logic — what should happen when a parent is deleted — is your decision to make.

## Checkpoint

- [ ] I can define bidirectional relationships with matching `back_populates`.
- [ ] I know when to use `.join()` vs relationship attribute access.
- [ ] I can explain `cascade="all, delete-orphan"` impact before using it.
- [ ] I can identify and fix one N+1 pattern.
- [ ] I can validate relationship queries with expected sample rows.
