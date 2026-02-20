---
sidebar_position: 6
title: "Transactions & Atomicity"
chapter: 10
lesson: 5
duration_minutes: 30
description: "Protect multi-step writes with commit/rollback boundaries"
keywords: ["transaction", "atomicity", "rollback", "commit", "SQLAlchemy"]
skills:
  - name: "Transaction Design"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can implement single-session multi-step writes with try/except/rollback"
  - name: "Atomicity Reasoning"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can identify which operations require atomic boundaries and explain the failure mode without them"
learning_objectives:
  - objective: "Implement atomic multi-step writes with rollback on failure"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student runs a forced failure and proves zero partial rows remain"
  - objective: "Distinguish schema validity from transaction correctness"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can explain how data can be schema-valid but business-invalid without transactions"
cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (atomicity, transaction boundary, invariant checking) within A2-B1 range"
differentiation:
  extension_for_advanced: "Implement a multi-step e-commerce checkout (reserve inventory + charge card + create order) with rollback. What happens if the charge succeeds but order creation fails?"
  remedial_for_struggling: "Focus on the bank transfer analogy first. Then implement the single transfer_budget function. The invariant checking is important but can wait until the basic pattern clicks."
teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "CRUD and Session Discipline"
  key_points:
    - "Atomicity means all-or-nothing — a failed transfer must leave zero rows, not one debit without a credit"
    - "The multi-session anti-pattern (splitting debit and credit across sessions) causes irreversible partial state that no rollback can fix"
    - "Invariant checks (sum of transfer entries = 0) catch bugs that return-message checking misses entirely"
    - "Transactions protect write mechanics (all-or-nothing); input validation protects write meaning (is this sensible) — you need both"
  misconceptions:
    - "Students think single inserts need explicit transaction wrappers — SQLAlchemy sessions already handle single-operation atomicity"
    - "Students trust return messages over database state — a function can return success:false while still leaving partial rows"
    - "Students believe catching the exception is enough — without explicit rollback, the session enters a dirty state that corrupts later queries"
    - "Students split related writes across sessions thinking each session handles its own rollback — but Session A's commit is permanent and Session B cannot undo it"
  discussion_prompts:
    - "If the debit commits in Session A and the credit fails in Session B, where did the money go? How would you detect this in production?"
    - "Name three operations in your domain that require atomic boundaries and three that do not — what is the distinguishing pattern?"
  teaching_tips:
    - "Start with the bank transfer scenario — every student understands that $100 disappearing is unacceptable, making atomicity feel urgent"
    - "The transaction states diagram is whiteboard-worthy — draw BEGIN branching to either COMMIT or ROLLBACK with the transfer example"
    - "Run the failure drill live: insert valid transfer, query count (+2), insert invalid transfer, query count (+0) — the numbers tell the story"
    - "Emphasize the debug posture: always trust the database over return values — have students practice querying after both success and failure"
  assessment_quick_check:
    - "What happens if you split a debit and credit across two separate sessions and the second session fails?"
    - "Write the one-session transaction template from memory: try/add_all/commit/except/rollback"
    - "How do you prove rollback worked — by checking the return message or by querying the database?"
---

# Transactions & Atomicity

In Lesson 4, you defined relationships between models and queried linked data with joins. Now you face a different problem: what happens when a write operation involves *multiple* steps, and one of them fails halfway through?

Imagine you are transferring $100 from your Food budget to Entertainment. The debit goes through — your Food balance drops by $100. Then the credit fails. Crash. Network error. Doesn't matter why. Your $100 just vanished into thin air. Not in Food. Not in Entertainment. Gone.

You might be thinking: "That can't really happen, right?" It absolutely can. And it does. Every production system that handles money or inventory has battle scars from exactly this scenario. The fix is not hope or retry logic. The fix is a *transaction* — a boundary that guarantees either both writes happen, or neither does.

:::info[Key Terms for This Lesson]
- **Transaction**: A group of database operations that must ALL succeed or ALL fail — there's no middle ground
- **Atomicity**: The "all-or-nothing" property — like a light switch, it's either on or off, never halfway
- **Invariant**: A truth that must always hold — "debits and credits in a transfer always net to zero" is an invariant. If it ever breaks, something went wrong.
:::

## How Transactions Work

A transaction wraps multiple database operations into a single unit of work. The database keeps all changes in a temporary state until you explicitly say "commit" (make permanent) or "rollback" (discard everything). If anything goes wrong before the commit, every change since the transaction began is undone automatically.

```
Transaction States:

  ┌─────────┐     ops succeed     ┌──────────┐
  │  BEGIN   │───────────────────►│  COMMIT   │
  │          │                    │ (durable) │
  └────┬─────┘                    └──────────┘
       │
       │ any op fails
       │
       ▼
  ┌──────────┐
  │ ROLLBACK │
  │ (undo    │
  │  ALL ops)│
  └──────────┘

  Example: Budget Transfer
  ┌─────────────────────────────────────┐
  │ BEGIN                               │
  │   1. Debit $100 from Food     ✓    │
  │   2. Credit $100 to Fun      ✗    │
  │                                     │
  │ → ROLLBACK: Debit is also undone   │
  │ → Result: $0 changed (correct!)    │
  └─────────────────────────────────────┘
```

That last line is the key insight. After a rollback, your data looks exactly as it did before the transfer attempt. No phantom debits. No missing money. The database pretends the whole thing never happened.

(Partial writes: because nothing says "professional software" like $100 disappearing from both accounts.)

## The Transfer Function

Here is an atomic budget transfer using SQLAlchemy. Everything happens inside one session, wrapped in try/except/rollback. If the credit fails, the debit is rolled back. If the debit fails, nothing was written yet. Either way, your data stays consistent.

```python
from datetime import date
from decimal import Decimal

from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String, create_engine, select
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, nullable=False, default=date.today)


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)


def transfer_budget(user_id: int, from_category_id: int, to_category_id: int, amount: Decimal):
    with Session(engine) as session:
        try:
            from_cat = session.execute(
                select(Category).where(Category.id == from_category_id)
            ).scalars().first()
            to_cat = session.execute(
                select(Category).where(Category.id == to_category_id)
            ).scalars().first()

            if not from_cat or not to_cat:
                raise ValueError("Category not found")

            debit = Expense(
                user_id=user_id,
                category_id=from_category_id,
                description=f"Transfer to {to_cat.name}",
                amount=-amount,
            )
            credit = Expense(
                user_id=user_id,
                category_id=to_category_id,
                description=f"Transfer from {from_cat.name}",
                amount=amount,
            )

            session.add_all([debit, credit])
            session.commit()
            return {"success": True}
        except Exception as exc:
            session.rollback()
            return {"success": False, "error": str(exc)}
```

**Output (successful transfer):**
```
>>> transfer_budget(user_id=1, from_category_id=1, to_category_id=2, amount=Decimal("100.00"))
{"success": True}
```

**Output (invalid category):**
```
>>> transfer_budget(user_id=1, from_category_id=1, to_category_id=999, amount=Decimal("100.00"))
{"success": False, "error": "Category not found"}
```

Notice the pattern: one session, one try block, one commit at the end, one rollback in the except. This is the core transaction template you will use for every multi-step write in this course.

## The Failure Drill

Reading about atomicity is not the same as proving it works. Run this drill to see rollback in action:

1. Run transfer with valid categories — expect two new rows
2. Run transfer with an invalid destination category — expect zero new rows
3. Query the expense count before and after each run
4. Confirm the invariant: successful transfers change count by exactly 2, failed transfers change count by exactly 0

This invariant check is stronger than checking return messages alone. A function can return `{"success": False}` while still leaving partial rows behind if the rollback was missing. The only proof is querying the database directly.

:::tip[Pause and Reflect]
Think about the transfer function you just saw. What would happen if step 1 (debit) committed in one session and step 2 (credit) ran in a different session? What if the second session crashed? Where did the money go?
:::

## The Multi-Session Anti-Pattern

The most dangerous mistake is splitting related operations across separate sessions. Here is what that looks like:

**Bad pattern:**
- Session A writes the debit and commits
- Session B writes the credit and fails

Result: irreversible partial state. The debit is permanent because Session A already committed. Session B's rollback only undoes Session B's work — it cannot reach back into Session A and undo the debit. Your $100 is gone.

(This is why related database writes should *never* live in separate sessions. If they must succeed together, they must live in the same transaction. Period.)

Another frequent mistake is catching an exception and returning without calling rollback. That leaves the failed transaction state unresolved and causes downstream confusion — later queries in the same session may behave unpredictably because the session is in a "dirty" state.

## Input Validation: Necessary but Not Sufficient

Transactions prevent partial writes. They do not correct bad business inputs. You still need validation rules:

- Validate that the amount is positive
- Validate that source and target categories are different
- Validate ownership scope if categories are user-specific

Think of it this way: transactions protect the *mechanics* of your write (all-or-nothing). Input validation protects the *meaning* of your write (is this a sensible operation?). You need both.

## Invariants: The Test That Catches Everything

An invariant is a truth about your data that must always hold. For budget transfers, the core invariants are:

- Transfer ledger entries for a completed move always net to zero
- Category totals before and after a transfer preserve the global sum
- Failed transfers produce no new rows

Writing these invariants into tests gives you faster confidence than manual spot checking. When a test asserts "the sum of all amounts for this transfer is zero," it catches bugs that return-message checks miss entirely.

When in doubt, choose stronger safety:

- Explicit rollback in every except block
- Explicit invariant assertions in every test
- Explicit post-failure query checks that verify actual database state

## Debug Posture for Transaction Bugs

When something goes wrong with a transaction, follow this discipline:

- Distrust return messages without database verification
- Inspect persisted rows directly after both success and failure paths
- Treat any partial side effect as a severity-one defect

If your function returns `{"success": False}` but the database has one new row instead of zero, you have a transaction bug. The return message lied. The database told the truth. Always trust the database over application-level return values.

**What breaks next?** Write safety can still fail in production if cloud connection handling is weak. Deployment reliability is next.

## Try With AI

**Setup:** Open Claude or ChatGPT with your budget tracker models from this chapter.

### Prompt 1: Atomicity Classifier

```text
For each scenario, classify "needs atomic transaction" vs "does not need atomic transaction":
- single insert (one new expense)
- transfer between two categories (debit + credit)
- monthly summary read (SELECT with GROUP BY)
- merge category migration (move all expenses from category A to B, then delete A)
Explain the failure mode if atomicity is missing for each one that needs it.
```

**What you're learning:** Not every database operation needs a transaction boundary. Single reads and single writes are already atomic by default. The skill is recognizing *which* operations involve multiple steps where partial completion would corrupt your data. This classification instinct prevents both under-protection (missing transactions where needed) and over-protection (wrapping single inserts in unnecessary transaction ceremony).

### Prompt 2: Rollback Proof Drill

```text
Write a transaction function that intentionally fails after the first insert.
Then show the post-failure query proving zero rows were committed.
Use SQLAlchemy 2.0 style and explicit rollback.
```

**What you're learning:** Proving rollback works requires more than reading the return value. You need to query the database after the failure and verify the row count is unchanged. This drill builds the habit of verifying database state directly — a practice that catches transaction bugs that return-message checking misses.

### Prompt 3: Apply to Your Domain

```text
Think of a multi-step operation in a project you're building. Maybe it's: creating a user account + sending a welcome email + logging the event. Or: transferring inventory between warehouses. Break it into steps and ask: "If step 2 fails, what happens to step 1?" Design the transaction boundary.
```

**What you're learning:** Transaction design isn't just for banks. Any operation where partial completion would corrupt your data needs an atomic boundary. Recognizing these moments — and wrapping them in try/except/rollback — is a skill that separates reliable systems from fragile ones.

## Checkpoint

- [ ] I can explain atomicity as all-or-nothing business truth.
- [ ] I can implement one-session multi-step writes with rollback.
- [ ] I can prove rollback with a deliberate failure drill.
- [ ] I can identify multi-session anti-patterns in write workflows.
- [ ] I can distinguish schema validity from transaction correctness.
