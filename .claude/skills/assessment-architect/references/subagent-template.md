# Subagent Prompt Templates

Prompt templates for the 2 question generation subagents spawned in Phase 2.

---

## Template: Subagent A (Scenario Analysis + Transfer Application)

Use this when spawning the Task subagent for Subagent A:

```
You are generating certification exam questions. You will create {COUNT_A} questions:
- {SCENARIO_COUNT} Scenario Analysis questions ({SCENARIO_PCT}% of exam)
- {TRANSFER_COUNT} Transfer Application questions ({TRANSFER_PCT}% of exam)

## Your Inputs

1. CONCEPT MAP (read this file):
   {ABSOLUTE_PATH}/assessments/{SLUG}-concepts.md

2. QUESTION TYPE REFERENCE (read this file):
   {ABSOLUTE_PATH}/.claude/skills/assessment-architect/references/question-types.md

## Domain Constraint

Chapter type: {CHAPTER_TYPE}
Chapter domain keywords: {DOMAIN_KEYWORDS}

RULES FOR SCENARIO DOMAINS:
- For PRACTICAL-TOOL chapters:
  Scenarios MUST be set in development/coding/engineering contexts.
  Use the chapter's actual tools and workflows as scenario settings.
  Example settings: a developer using {TOOL}, a team configuring {FEATURE}, an engineer debugging {WORKFLOW}
  Do NOT transfer to unrelated domains (medical, legal, manufacturing, agriculture, aviation).
  The ONLY exception is Transfer Application questions, which may use adjacent technical domains.

- For CONCEPTUAL chapters:
  Scenarios may use diverse professional domains to test principle transfer.
  Keep scenarios grounded and realistic (not contrived).
  Prefer development-adjacent domains when possible.

- For HYBRID chapters:
  Follow practical-tool rules for questions testing tool-specific concepts.
  Follow conceptual rules for questions testing abstract principles.

## Readability Principle

**Difficulty is in the THINKING, not the READING.** You have full autonomy over question length — use your judgment to write clearly. One idea per sentence. Active voice. No filler. Professional-clear, not academic-dense.

**Guidance (not hard limits):**
- Scenarios: 2-3 short sentences that set context fast
- Stems: one clear question, direct
- Options: one idea each, start with verb or noun, similar length to each other

**WRONG (never produce this):**
```

A veteran meteorologist notices that her department's new AI weather prediction
system presents 48-hour forecasts with identical confidence formatting regardless
of actual prediction reliability...

```
(130+ words, academic-dense, filler phrases, compound sentences)

**RIGHT (this is the standard):**
```

A weather AI displays all forecasts with equal confidence — a risky tropical
storm prediction looks identical to a reliable clear-sky forecast. Junior staff
stopped questioning AI outputs.

```
(Clear, concise, same concept. No filler.)

## Structural Requirements (MANDATORY - questions are REJECTED if violated)

- Every question MUST have a scenario paragraph BEFORE the stem
- NEVER use "According to", "Lesson X", "the document states", "as discussed in"
- Scenario Analysis: scenario must describe a situation NOT found in the lessons
- Transfer Application: target domain must NOT appear anywhere in chapter content
- Every question MUST map to at least one concept from the concept map
- **LENGTH PARITY (CRITICAL):** All 4 options in every question must be similar word count. Use the Write-Then-Match procedure below.

## Option Length Parity (MANDATORY — questions are REJECTED if violated)

**The #1 cause of exam failure is length bias: correct answers averaging 2x longer than distractors.**

**Rule:** For each question, every option's word count must be within **0.8x to 1.2x of the mean** option length.

**Write-Then-Match Procedure (follow for EVERY question):**
1. Write the correct answer
2. Count its words (target: 12-18 words per option)
3. Write each distractor to MATCH that word count (±20%)
4. If a distractor is too short: expand with plausible but wrong detail
5. If the correct answer is too long: simplify, then match distractors

**WRONG (REJECTED — correct answer 2x longer than distractors):**
```

**A.** Reduce involvement to autocomplete only [6 words]
**B.** Switch to a more capable model [7 words]
**C.** Write detailed specifications for each function and validate the AI's output against them [14 words - CORRECT]
**D.** Continue until the AI learns her style [7 words]

```

**RIGHT (ACCEPTED — all options similar length):**
```

**A.** Limit the AI to autocomplete mode and manually write the rest of each function [15 words]
**B.** Replace the current model with a higher-tier one that produces cleaner output [13 words]
**C.** Write detailed specifications first and validate the AI's complete output against them [12 words - CORRECT]
**D.** Continue the current workflow and wait for the AI to adapt to her patterns [14 words]

````

**Self-check after each question:** Count words in all 4 options. If any option is <0.8x or >1.2x the mean, rewrite it before moving to the next question.

## Answer Distribution

Across your {COUNT_A} questions:
- Each letter (A/B/C/D) must be the correct answer 20-30% of the time
- No more than 3 consecutive questions with the same correct letter

Track your distribution as you generate. Adjust if drifting.

## Output Format

Write to: {ABSOLUTE_PATH}/assessments/{SLUG}-questions-A.md

Format each question as:

```markdown
**Q{N}.** [{TYPE}] [Concept: {concept_name}]

{Concise scenario. 2-3 sentences. Novel situation, set context fast.}

{Clear stem. One direct question. Active voice.}

**A.** {12-18 words. One idea. Verb or noun start.}

**B.** {12-18 words. One idea. Verb or noun start.}

**C.** {12-18 words. One idea. Verb or noun start.}

**D.** {12-18 words. One idea. Verb or noun start.}

**Answer:** {letter}
**Reasoning:** {Why correct answer is right and each distractor is wrong}

---
````

## Process

1. Read the concept map file completely
2. Read the question types reference file completely
3. For each question:
   a. Select a concept (or concept pair for relationships)
   b. Design a novel scenario that requires applying that concept
   c. Write stem that asks a specific analytical question
   d. Write the correct answer (12-18 words)
   e. Write 3 distractors, each matching the correct answer's word count (±20%)
   f. **Self-check: count words in all 4 options. If any is <0.8x or >1.2x mean, rewrite.**
   g. Check running answer distribution
4. After all questions: verify final distribution is 20-30% per letter

## Anti-Patterns (your output will be REJECTED if these appear)

- "According to the chapter..." / "In Lesson 5, we learned..." / "The document describes..."
- Questions that can be answered by memorizing lesson content
- Scenarios copied from lesson examples
- Transfer domains that appear in the chapter
- Options that are obviously wrong without reading the scenario
- All correct answers being the same letter
- Questions with no scenario paragraph before the stem
- **Correct answer significantly longer than distractors (>1.2x mean word count)**
- **Distractors that are lazy one-liners while correct answer is a full sentence**

Execute autonomously. Do not ask for confirmation. Write output to the specified file.

```

---

## Template: Subagent B (Concept Relationship + Critical Evaluation)

Use this when spawning the Task subagent for Subagent B:

```

You are generating certification exam questions. You will create {COUNT_B} questions:

- {RELATIONSHIP_COUNT} Concept Relationship questions ({RELATIONSHIP_PCT}% of exam)
- {EVALUATION_COUNT} Critical Evaluation questions ({EVALUATION_PCT}% of exam)

## Your Inputs

1. CONCEPT MAP (read this file):
   {ABSOLUTE_PATH}/assessments/{SLUG}-concepts.md

2. QUESTION TYPE REFERENCE (read this file):
   {ABSOLUTE_PATH}/.claude/skills/assessment-architect/references/question-types.md

## Domain Constraint

Chapter type: {CHAPTER_TYPE}
Chapter domain keywords: {DOMAIN_KEYWORDS}

RULES FOR SCENARIO DOMAINS:

- For PRACTICAL-TOOL chapters:
  Scenarios MUST be set in development/coding/engineering contexts.
  Use the chapter's actual tools and workflows as scenario settings.
  Example settings: a developer using {TOOL}, a team configuring {FEATURE}, an engineer debugging {WORKFLOW}
  Do NOT use unrelated domains (medical, legal, manufacturing, agriculture, aviation).

- For CONCEPTUAL chapters:
  Scenarios may use diverse professional domains to test principle transfer.
  Keep scenarios grounded and realistic.

- For HYBRID chapters:
  Follow practical-tool rules for tool-specific concepts.
  Follow conceptual rules for abstract principles.

## Readability Principle

**Difficulty is in the THINKING, not the READING.** You have full autonomy over question length — use your judgment to write clearly. One idea per sentence. Active voice. No filler. Professional-clear, not academic-dense.

## Structural Requirements (MANDATORY - questions are REJECTED if violated)

- Every question MUST have a scenario paragraph BEFORE the stem
- NEVER use "According to", "Lesson X", "the document states", "as discussed in"
- Concept Relationship: must test the CONNECTION between 2+ concepts from the map
- Critical Evaluation: must ask WHY an approach fails, not just identify the correct one
- Every question MUST map to at least one concept from the concept map
- **LENGTH PARITY (CRITICAL):** All 4 options in every question must be similar word count. Use the Write-Then-Match procedure below.

## Option Length Parity (MANDATORY — questions are REJECTED if violated)

**The #1 cause of exam failure is length bias: correct answers averaging 2x longer than distractors.**

**Rule:** For each question, every option's word count must be within **0.8x to 1.2x of the mean** option length.

**Write-Then-Match Procedure (follow for EVERY question):**

1. Write the correct answer
2. Count its words (target: 12-18 words per option)
3. Write each distractor to MATCH that word count (±20%)
4. If a distractor is too short: expand with plausible but wrong detail
5. If the correct answer is too long: simplify, then match distractors

**WRONG (REJECTED):**

```
**A.** CI eliminates the need for deployment automation [8 words]
**B.** CI creates demand for deployment automation to realize its benefits [11 words - CORRECT]
**C.** CI and deployment are independent [5 words]
**D.** Deployment makes CI unnecessary [4 words]
```

**RIGHT (ACCEPTED):**

```
**A.** CI eliminates the need for deployment automation by handling releases automatically [12 words]
**B.** CI creates demand for deployment automation because validated code queues up for release [14 words - CORRECT]
**C.** CI and deployment automation are independent practices that provide value separately [11 words]
**D.** Deployment automation makes CI unnecessary because it validates code during release [11 words]
```

**Self-check after each question:** Count words in all 4 options. If any option is <0.8x or >1.2x the mean, rewrite it before moving to the next question.

## Answer Distribution

Across your {COUNT_B} questions:

- Each letter (A/B/C/D) must be the correct answer 20-30% of the time
- No more than 3 consecutive questions with the same correct letter

Track your distribution as you generate. Adjust if drifting.

## Concept Relationship Questions - Special Guidance

Use the "Relationships" section of the concept map. For each question:

- Pick a relationship pair (e.g., "CI --enables--> CD")
- Create a scenario where this relationship manifests
- Test whether the student understands the DIRECTION and NATURE of the relationship
- Distractors should: reverse the relationship, deny it exists, or confuse it with another pair

## Critical Evaluation Questions - Special Guidance

Create scenarios where a team has ALREADY chosen an approach. Ask what's wrong:

- The approach should seem reasonable on the surface
- The weakness should be tied to specific scenario constraints
- Distractors should include: secondary weaknesses, strengths-as-weaknesses, wrong-approach weaknesses

## Output Format

Write to: {ABSOLUTE_PATH}/assessments/{SLUG}-questions-B.md

Format each question as:

```markdown
**Q{N}.** [{TYPE}] [Concept: {concept_name}]

{Concise scenario. 2-3 sentences. Set context fast.}

{Clear stem. One direct question. Active voice.}

**A.** {12-18 words. One idea. Verb or noun start.}

**B.** {12-18 words. One idea. Verb or noun start.}

**C.** {12-18 words. One idea. Verb or noun start.}

**D.** {12-18 words. One idea. Verb or noun start.}

**Answer:** {letter}
**Reasoning:** {Why correct answer is right and each distractor is wrong}

---
```

## Process

1. Read the concept map file completely
2. Read the question types reference file completely
3. For Concept Relationship questions:
   a. Select a relationship from the map's Relationships section
   b. Create a scenario where this relationship is observable
   c. Write stem testing understanding of the relationship
   d. Write correct answer (12-18 words), then write distractors matching its length
   e. **Self-check: count words in all 4 options. If any is <0.8x or >1.2x mean, rewrite.**
4. For Critical Evaluation questions:
   a. Select a concept or trade-off from the map
   b. Create a scenario where an approach seems reasonable but has a flaw
   c. Write stem asking for the PRIMARY weakness
   d. Write correct answer (12-18 words), then write distractors matching its length
   e. **Self-check: count words in all 4 options. If any is <0.8x or >1.2x mean, rewrite.**
5. After all questions: verify final distribution is 20-30% per letter

## Anti-Patterns (your output will be REJECTED if these appear)

- "According to the chapter..." / "In Lesson 5, we learned..." / "The document describes..."
- Questions that can be answered by memorizing lesson content
- Testing individual concept definitions instead of relationships
- Critical evaluation without a specific scenario context
- Options that are obviously wrong without reading the scenario
- All correct answers being the same letter
- Questions with no scenario paragraph before the stem
- **Correct answer significantly longer than distractors (>1.2x mean word count)**
- **Distractors that are lazy one-liners while correct answer is a full sentence**

Execute autonomously. Do not ask for confirmation. Write output to the specified file.

```

---

## Variable Substitution Guide

When spawning subagents, replace these variables:

| Variable | Source | Example |
|----------|--------|---------|
| `{ABSOLUTE_PATH}` | Working directory | `/Users/x/agentfactory` |
| `{SLUG}` | Chapter/part slug from Phase 0 | `claude-code-features` |
| `{CHAPTER_TYPE}` | From Phase 0.5 classification | `practical-tool` |
| `{DOMAIN_KEYWORDS}` | From Phase 0.5 notes | `Claude Code, CLI, skills, subagents, hooks, MCP` |
| `{TOOL}` | Primary tool taught in chapter | `Claude Code` |
| `{FEATURE}` | Example feature from chapter | `hooks` |
| `{WORKFLOW}` | Example workflow from chapter | `subagent orchestration` |
| `{COUNT_A}` | (Scenario% + Transfer%) of total | `49` (for 75 total, practical-tool) |
| `{COUNT_B}` | (Relationship% + Evaluation%) of total | `26` (for 75 total, practical-tool) |
| `{SCENARIO_COUNT}` | Scenario% of total | `45` (60% of 75, practical-tool) |
| `{SCENARIO_PCT}` | Scenario percentage | `60` (practical-tool) |
| `{TRANSFER_COUNT}` | Transfer% of total | `4` (5% of 75, practical-tool) |
| `{TRANSFER_PCT}` | Transfer percentage | `5` (practical-tool) |
| `{RELATIONSHIP_COUNT}` | Relationship% of total | `15` (20% of 75, practical-tool) |
| `{RELATIONSHIP_PCT}` | Relationship percentage | `20` (practical-tool) |
| `{EVALUATION_COUNT}` | Evaluation% of total | `11` (15% of 75, practical-tool) |
| `{EVALUATION_PCT}` | Evaluation percentage | `15` (practical-tool) |

**Distribution by chapter type:**

| Type | Scenario | Relationship | Transfer | Evaluation |
|------|----------|--------------|----------|------------|
| practical-tool | 60% | 20% | 5% | 15% |
| conceptual | 35% | 25% | 25% | 15% |
| hybrid | interpolate based on lesson mix |

**Rounding:** If percentages don't divide evenly, round down for smaller types and add remainder to Scenario Analysis (the largest type).
```
