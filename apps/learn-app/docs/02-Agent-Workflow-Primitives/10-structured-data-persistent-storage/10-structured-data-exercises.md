---
title: "Structured Data Practice Exercises"
practice_exercise: ch10-structured-data
sidebar_position: 10
chapter: 10
lesson: 9
duration_minutes: 120
skills:
  - name: "Model-Build-Debug Discipline"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can build and debug relational apps under realistic constraints"
  - name: "Operational Verification"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Quality Assurance"
    measurable_at_this_level: "Student can prove correctness with evidence instead of assumptions"
learning_objectives:
  - objective: "Build and debug relational apps independently under time constraints"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student completes Core exercises with evidence artifacts"
  - objective: "Produce evidence-based proof of correctness"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student submits EVIDENCE.md with pass/fail results for each exercise"
cognitive_load:
  new_concepts: 0
  assessment: "No new concepts — exercises apply and integrate previously learned material"
differentiation:
  extension_for_advanced: "Complete all Challenge track exercises. Design a new Challenge D exercise and share with classmates."
  remedial_for_struggling: "Complete Core 1 and Core 2 only. Focus on producing clear evidence artifacts rather than rushing through all four exercises."
teaching_guide:
  lesson_type: "hands-on"
  session_group: 3
  session_title: "Cloud Deployment and Verification"
  key_points:
    - "The mantra is 'claim nothing, prove everything' — evidence artifacts (DECISIONS.md, EVIDENCE.md) replace verbal claims"
    - "Core exercises map 1:1 to chapter lessons: model integrity (L3), CRUD reliability (L4), relationship debug (L5), transaction+Neon (L6+L7)"
    - "Getting stuck for 10+ minutes is the signal to move on and return later — later exercises often illuminate earlier blockers"
    - "Incomplete evidence for a finished exercise teaches nothing; complete evidence for half the exercises teaches the discipline that matters"
  misconceptions:
    - "Students think exercises are optional review — they are where muscle memory forms, which is different from understanding concepts"
    - "Students rush through all exercises with minimal evidence rather than producing thorough evidence for fewer exercises"
    - "Students think 'it runs without errors' is sufficient evidence — quality gates require failure-path proof and explicit artifacts"
  discussion_prompts:
    - "Which of the four Core exercises felt hardest? What does that tell you about which chapter concept needs another pass?"
    - "Could someone who was not in the room verify your work from EVIDENCE.md alone? What would they need that is missing?"
  teaching_tips:
    - "Set a visible timer for each exercise — timeboxing prevents students from spending 90 minutes on Core 1 and rushing the rest"
    - "Have students swap EVIDENCE.md files and review each other's proof — peer review builds the 'would another engineer accept this?' instinct"
    - "Core 3 (relationship debug) is the hardest for most students — consider pairing struggling students for this exercise"
    - "The self-assessment scoring (0-2 per criterion) is a powerful self-reflection tool — have students score honestly and identify their weakest area"
  assessment_quick_check:
    - "What three artifacts must every exercise submission include?"
    - "What does the quality gate in Core 1 reject and why?"
    - "What is the difference between completing all exercises poorly and completing two exercises with thorough evidence?"
---

# Structured Data Practice Exercises

In the capstone you built a complete budget tracker with models, CRUD, transactions, and a Neon connection. Now you put those skills under pressure, independently and with a timer running.

Getting stuck is not failure. Quitting is. These exercises are **meant** to be challenging. If everything felt easy, you would not be learning anything new. The moments where you stare at an error message and think "I have no idea what went wrong" are the moments where real understanding forms.

If you are stuck for more than 10 minutes on one part, move on and come back. Sometimes the later exercises give you a new perspective on the earlier ones.

You might be thinking: "I don't know where to start." That is fine. The hints are there. Use them.

One rule above all others:

- **Claim nothing. Prove everything.**

## How to Use

1. Read the exercise brief.
2. Implement or debug.
3. Collect evidence artifacts.
4. Write a short postmortem.

## Evidence Format (Use Across All Exercises)

For each exercise, submit:

- `DECISIONS.md`: what you changed and why
- `EVIDENCE.md`: commands run, outputs, and pass/fail summary
- one explicit "known risk" note after completion

This keeps your practice aligned with capstone release discipline.

Timebox suggestion:

- Core 1: 25 minutes
- Core 2: 30 minutes
- Core 3: 30 minutes
- Core 4: 35 minutes

If you run out of time, finish evidence for completed work instead of starting a new unfinished exercise. Incomplete evidence for a finished exercise teaches you nothing. Complete evidence for half the exercises teaches you the discipline that matters in production.

## Core Track (Mandatory)

Complete all four exercises below.

> **Glossary for Core Track**
>
> | Term                 | Meaning                                                                                                    |
> | -------------------- | ---------------------------------------------------------------------------------------------------------- |
> | **Model integrity**  | Your SQLAlchemy models enforce correct data through types, constraints, and foreign keys, not through hope |
> | **CRUD**             | Create, Read, Update, Delete: the four basic operations every database application needs                   |
> | **Rollback proof**   | Evidence that a failed operation left zero partial writes in the database                                  |
> | **Session boundary** | The explicit `with Session(engine) as session:` block where all database mutations happen                  |
> | **N+1 query**        | A performance bug where your code runs one query per row instead of one query for all rows                 |

<ExerciseCard id="C1" title="Model Integrity Build" />

### Core 1 - Model Integrity Build

**Goal:** Build `User`, `Category`, `Expense`-style models for a new domain.

Pick a domain you find interesting: a recipe tracker, a reading list, a workout log, a pet adoption registry. The specific domain does not matter. What matters is that you define real relationships between real entities with real constraints.

Deliverables:

- model file with constraints + foreign keys
- `MODEL-VERIFICATION.md` with 3 query checks

Minimum evidence:

- schema output
- one invalid insert failure proof
- one explanation of why chosen types prevent ambiguity

Quality gate:

- reject any solution that stores money in float
- reject any solution that represents relationships only through free-text identifiers

<details>
<summary>Hint: Where to start</summary>

Start by listing the entities in your chosen domain. What are the "things"? What connects them? For a recipe tracker, the things might be `Recipe`, `Ingredient`, and `RecipeIngredient` (the join table). Once you have the entities on paper, turn them into SQLAlchemy models the same way you did in Lesson 3. Constraints and foreign keys come from asking: "What should the database refuse to store?"

</details>

<ExerciseCard id="C2" title="CRUD Reliability Build" />

### Core 2 - CRUD Reliability Build

**Goal:** Implement create/read/update/delete with session + rollback discipline.

This is the exercise where muscle memory forms. You have seen CRUD in the lessons. Now build it from scratch for your own domain, without copying and pasting. When the rollback test passes, you will feel it click.

Deliverables:

- CRUD module
- `CRUD-EVIDENCE.md` with before/after snapshots

Minimum evidence:

- one successful write
- one failed write with rollback proof
- one query proving no accidental duplicate rows

Quality gate:

- reject any solution that catches exceptions without rollback
- reject any solution that mutates state outside explicit session boundaries

<details>
<summary>Hint: Where to start</summary>

Copy the CRUD pattern from Lesson 4 and adapt it. Do not write from scratch. Adapting a working pattern to your domain is faster and teaches you to recognize which parts are universal (session management, commit/rollback) and which parts are domain-specific (the fields you create and query). Change the model names and fields, then run it.

</details>

<ExerciseCard id="C3" title="Relationship Query Debug" />

### Core 3 - Relationship Query Debug

**Goal:** Fix a broken relationship setup and return correct joined results.

This exercise is different from the others. You are not building from scratch. You are handed broken code and your job is to find what is wrong, fix it, and prove the fix works. Debugging relationship definitions is one of the most common real-world SQLAlchemy tasks.

Deliverables:

- corrected relationship definitions
- `RELATIONSHIP-TRACE.md`

Minimum evidence:

- bidirectional navigation works
- one `join()` query returns expected rows
- one N+1 risk identified and corrected

Quality gate:

- reject solutions with mismatched `back_populates`
- reject solutions that only test one relationship direction

<details>
<summary>Hint: Where to start</summary>

The bug is in the relationship definitions. Check `back_populates` first. The most common mistake is that `back_populates` on one side points to a name that does not exist on the other side, or the names are swapped. Print both sides of the relationship (parent.children and child.parent) to confirm navigation works in both directions before moving to join queries.

</details>

<ExerciseCard id="C4" title="Transaction + Neon Ops Drill" />

### Core 4 - Transaction + Neon Ops Drill

**Goal:** Prove atomic multi-step writes and cloud connection reliability.

This is the closest exercise to production work. You are combining local transaction safety with a real cloud database connection. When your forced-failure test leaves zero partial writes AND your Neon health check passes, you have completed the full Chapter 10 skill chain.

Deliverables:

- `transfer_*` transaction function
- Neon connection config + health check script
- `OPS-EVIDENCE.md`

Minimum evidence:

- forced failure leaves zero partial writes
- Neon `SELECT 1` passes
- pool settings documented and justified

Quality gate:

- reject releases without rollback drill output
- reject configs that hardcode credentials

<details>
<summary>Hint: Where to start</summary>

Start with the `SELECT 1` health check. If that works, everything else is CRUD + rollback on top of a connection you already trust. Write the health check script first, confirm it connects to Neon, then build the transfer function locally with SQLite, then switch to the Neon connection string. Small steps, each verified before the next.

</details>

## Challenge Track (Optional)

These exercises go beyond the chapter baseline. They simulate real production scenarios where the answer is not obvious and the stakes are higher.

Choose one or more.

> **Glossary for Challenge Track**
>
> | Term                         | Meaning                                                                                   |
> | ---------------------------- | ----------------------------------------------------------------------------------------- |
> | **Verification gate**        | A check that must pass before code ships: if the numbers disagree, the release is blocked |
> | **CSV migration**            | Moving data from flat CSV files into a normalized relational schema without losing rows   |
> | **Incident recovery**        | Diagnosing a broken production state, fixing it safely, and proving nothing else broke    |
> | **Row-count reconciliation** | Confirming that every row in the source data appears in the destination after migration   |
> | **Regression proof**         | Evidence that your fix did not break something that was previously working                |

<ExerciseCard id="A" title="High-Stakes Verification Gate" />

### Challenge A - High-Stakes Verification Gate

Build SQL summary + independent raw-ledger verification.

Evidence:

- `mismatch-policy-result.json`
- clear release block decision when mismatch exceeds tolerance
- mismatch triage notes

Use this challenge if your target role includes finance, compliance, or audit-sensitive workflows.

<ExerciseCard id="B" title="Legacy CSV Migration" />

### Challenge B - Legacy CSV Migration

Normalize a messy multi-file dataset into relational schema.

Evidence:

- row-count reconciliation
- key-field parity checks
- explicit list of non-lossy transformations

<ExerciseCard id="C" title="Recovery Under Incident" />

### Challenge C - Recovery Under Incident

Given a broken budget app state, prioritize fixes and recover safely.

Evidence:

- prioritized fix log
- regression proof after recovery
- short incident postmortem with prevention actions

Use this challenge if your target role includes operations ownership or on-call responsibilities.

## Outcome Mapping

| Outcome                  | Core track coverage | Challenge extension |
| ------------------------ | ------------------- | ------------------- |
| Model correctness        | Core 1              | Challenge B         |
| Safe CRUD                | Core 2              | Challenge C         |
| Relationship correctness | Core 3              | Challenge B         |
| Transaction safety       | Core 4              | Challenge C         |
| Neon reliability         | Core 4              | Challenge C         |
| Hybrid judgment          | Core 4              | Challenge A         |

If you complete all Core exercises with clear evidence, you meet Chapter 10 baseline mastery. Challenge track pushes you toward production-level judgment.

## Suggested Scoring for Self-Assessment

Use a 0-2 scale for each criterion per exercise:

- `Model correctness`
- `Write safety`
- `Query correctness`
- `Failure-path evidence`
- `Operational clarity`

Interpretation:

- `8-10`: ready for capstone-level work
- `6-7`: repeat one core exercise with stricter evidence
- `<6`: revisit lesson material before continuing

A score below 6 is not a verdict on you. It means the material needs another pass. Go back to the lesson that covers your weakest criterion, re-read the key section, then try the exercise again with that specific gap in mind.

## Try With AI

**Setup:** Open Claude Code, Cursor, or Windsurf in a project directory with your exercise files.

**Prompt 1: Evidence Review**

```
Here is my EVIDENCE.md for the CRUD exercise:

[paste your EVIDENCE.md]

Review this evidence file. For each claim I make:
1. Is the evidence sufficient to prove the claim?
2. What additional evidence would make the proof stronger?
3. Are there any claims I made without supporting output?

Be strict. In production, reviewers will be stricter than you.
```

**What you're learning:** You are building the skill of self-auditing. Production teams reject pull requests with claims like "this works" and no proof. By having AI critique your evidence, you learn what "sufficient proof" actually looks like, and you carry that standard into every future exercise.

**Prompt 2: Failure Scenario Generation**

```
I built a CRUD module for [your domain] with these models:

[paste your model definitions]

Generate 5 failure scenarios I should test:
- 2 involving constraint violations
- 2 involving transaction rollback
- 1 involving a relationship navigation bug

For each scenario, tell me what to try AND what the correct
behavior should be. I want to test these myself, not have
you fix them.
```

**What you're learning:** You are practicing defensive thinking. Production bugs do not come from the happy path. They come from the cases you did not consider. By asking AI to generate failure scenarios, you learn to think about what could go wrong before it goes wrong, which is the core skill behind "claim nothing, prove everything."
