# Chapter 14: Ten Axioms of Agentic Development - Specification

## Overview

Chapter 14 bridges Parts 1-3 (experiential learning with General Agents) and Parts 4-6 (technical implementation). It formalizes the **Ten Axioms** — the developer-specific methodology that governs how to write software in the AI era.

**Position**: First chapter in Part 4 (Coding for Problem Solving)
**Nature**: Conceptual/Methodology (NOT a framework/SDK chapter — no L00 skill-first pattern)
**Proficiency**: A2-B1 (readers have completed Parts 1-3, now ready for technical depth)

## Relationship to Seven Principles (Chapter 4)

| Seven Principles (Ch 4) | Ten Axioms (Ch 14)              |
| ----------------------- | ------------------------------- |
| Mindset for ALL users   | Methodology for DEVELOPERS      |
| "How to think"          | "How to build"                  |
| General (any AI tool)   | Specific (software engineering) |
| Experiential/intuitive  | Formal/prescriptive             |

The axioms are the **technical instantiation** of the principles. Each axiom connects back to one or more principles but adds implementation specificity.

## The Ten Axioms

| #    | Axiom                              | Principle Connection  | Core Teaching                                                                |
| ---- | ---------------------------------- | --------------------- | ---------------------------------------------------------------------------- |
| I    | Shell as Orchestrator              | P1: Bash is the Key   | Shell coordinates all tools; complexity stays in programs                    |
| II   | Knowledge is Markdown              | P5: Persisting State  | All specs, docs, decisions live in markdown — the universal knowledge format |
| III  | Programs Over Scripts              | P2: Code as Interface | Production work requires structured programs with types, tests, CI           |
| IV   | Composition Over Monoliths         | P4: Decomposition     | Build from composable units, not monolithic blocks                           |
| V    | Types Are Guardrails               | P6: Constraints       | Type systems prevent errors at compile time, not runtime                     |
| VI   | Data is Relational                 | P5: Persisting State  | SQL as default for structured data; relational thinking                      |
| VII  | Tests Are the Specification        | P3: Verification      | TDG: tests define correctness, AI generates implementations                  |
| VIII | Version Control is Memory          | P5: Persisting State  | Git as persistent memory layer for all work                                  |
| IX   | Verification is a Pipeline         | P3: Verification      | CI/CD automates and enforces verification continuously                       |
| X    | Observability Extends Verification | P7: Observability     | Runtime monitoring extends pre-deployment testing                            |

## Lesson Structure (All 10 Lessons)

Each lesson follows this consistent structure:

1. **Opening Hook** (2-3 paragraphs): Real-world scenario showing the axiom's importance
2. **The Problem Without This Axiom**: What goes wrong when you violate it
3. **The Axiom Defined**: Formal statement and explanation
4. **Connection to Principles**: How it extends the Seven Principles
5. **Practical Application**: Concrete patterns and examples with code
6. **Anti-Patterns**: Common violations and their consequences
7. **Try With AI** (3 prompts): Hands-on exploration of the axiom

## Prerequisites

- Part 1: General Agents Foundations (Chapters 1-4)
- Part 2: Agent Workflow Primitives (Chapters 5-10)
- Part 3: Applied Domain Workflows (Chapters 11-13)

## Layer Progression

- Lessons 01-04: **L1 (Manual)** — Introduce axioms conceptually, students understand before applying
- Lessons 05-07: **L2 (Collaboration)** — Students explore axioms with AI assistance
- Lessons 08-10: **L2→L3** — Students see how axioms compose into systems; pipeline/observability lessons bridge to practical skill-building

## Quality Requirements

- Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
- 3 "Try With AI" prompts per lesson with "What you're learning" explanations
- Code examples with evidence blocks (Python, bash, YAML as appropriate)
- Tables comparing approaches (with/without axiom)
- Connection to student's existing knowledge from Parts 1-3
- No fluff — pragmatic, industrial tone per manifesto

## Assessment

Chapter quiz (lesson 11) covering all 10 axioms with scenario-based questions testing application, not just recall.

## Output Path

```
apps/learn-app/docs/04-Coding-for-Problem-Solving/14-ten-axioms-of-agentic-development/
├── 01-shell-as-orchestrator.md
├── 02-knowledge-is-markdown.md
├── 03-programs-over-scripts.md
├── 04-composition-over-monoliths.md
├── 05-types-are-guardrails.md
├── 06-data-is-relational.md
├── 07-tests-are-the-specification.md
├── 08-version-control-is-memory.md
├── 09-verification-is-a-pipeline.md
├── 10-observability-extends-verification.md
├── 11_chapter_14_quiz.md
└── README.md
```
