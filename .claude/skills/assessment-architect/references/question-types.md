# Question Types: Scenario-Based Assessment Framework

4 question types. ALL require a concise scenario before the stem.

**Difficulty is in the THINKING, not the READING.**

---

## Readability Principle (applies to ALL types)

Write questions that are clear, concise, and professional. The challenge should come from applying concepts to novel situations — not from parsing dense prose.

**Good writing:**

- Scenarios: 2-3 short sentences. Set context fast. No backstory.
- Stems: One clear question. Active voice. Direct.
- Options: One idea each. Start with verb or noun. Similar length to each other.
- No filler, no redundant qualifiers, no compound-complex sentences.

Use your judgment. The examples below show the standard.

---

## 1. Scenario Analysis (40% of exam)

**Bloom Level:** Apply / Analyze
**Purpose:** Apply concepts to novel situations not in the lessons.

**Structure:**

```
SCENARIO (concise, 2-3 sentences):
A situation involving [concept]. Specific but brief.

STEM (one clear question):
What approach addresses [the problem in the scenario]?

OPTIONS (concise, one idea each):
**A.** [Wrong concept applied — plausible but mismatched]
**B.** [Correct application]
**C.** [Partially correct — misses a key constraint]
**D.** [Common misconception]
```

**Example:**

```
A weather AI displays all forecasts identically — a risky tropical storm
prediction looks the same as a reliable clear-sky forecast. Staff stopped
questioning AI outputs.

How should the team handle AI outputs that show no uncertainty signal?

**A.** Trust outputs that match historical weather patterns
**B.** Verify all forecasts independently before publishing
**C.** Add disclaimers noting AI may contain errors
**D.** Use a different model trained on more weather data
```

Total: ~70 words. Clear. Tests confidence-trap concept.

**Distractor Design:**

- A: Uses unreliable heuristic (pattern matching ≠ verification)
- C: Passive legal protection, doesn't change behavior
- D: Misidentifies the problem as model quality

---

## 2. Concept Relationship (25% of exam)

**Bloom Level:** Analyze / Evaluate
**Purpose:** Test HOW concepts connect, enable, or conflict.

**Structure:**

```
SCENARIO (concise, 2-3 sentences):
A situation where two concepts interact in tension or synergy.

STEM (one clear question):
What relationship between [A] and [B] does this demonstrate?

OPTIONS (concise, one idea each):
**A.** [Reverses the dependency direction]
**B.** [Correct relationship with proper causality]
**C.** [Denies any relationship exists]
**D.** [Confuses with a different concept pair]
```

**Example:**

```
A team adopted CI but kept manual deploys. Code quality improved,
but release frequency dropped as validated code queued up faster
than ops could deploy it.

What relationship between CI and deployment automation does this show?

**A.** CI eliminates the need for deployment automation
**B.** CI creates demand for deployment automation to realize its benefits
**C.** CI and deployment are independent practices without interaction
**D.** Deployment automation makes CI unnecessary
```

Total: ~80 words. Tests the "creates-demand-for" relationship.

**Distractor Design:**

- A: Reverses dependency
- C: Denies relationship
- D: Reverses which practice is foundational

---

## 3. Transfer Application (20% of exam)

**Bloom Level:** Apply / Create
**Purpose:** Apply a chapter principle to a domain NOT in the chapter.

**Key Constraint:** The transfer domain must NOT appear in chapter content. Verify: `grep -ri "{domain}" {PATH}/` returns 0.

**Structure:**

```
SCENARIO (concise, 2-3 sentences):
A situation in [domain NOT in chapter] with structural similarity
to a chapter principle.

STEM (one clear question):
Applying [principle], which approach addresses [the problem]?

OPTIONS (concise, one idea each):
**A.** [Surface-level fix that misses the structural principle]
**B.** [Correct structural transfer]
**C.** [Different principle applied incorrectly]
**D.** [Domain-specific solution ignoring transferable insight]
```

**Example (chapter teaches event-driven architecture):**

```
A city's emergency dispatch polls each unit for availability before
assigning incidents. During multi-incident events, polling creates
dangerous delays.

Applying the publish-subscribe pattern, which redesign reduces delays?

**A.** Faster polling that checks all units simultaneously
**B.** Units broadcast availability changes to a central hub in real-time
**C.** Assign more dispatchers to parallelize manual polling
**D.** Predict availability from historical shift patterns
```

Total: ~70 words. Domain (emergency services) not in chapter.

**Distractor Design:**

- A: Optimizes old pattern instead of replacing it
- C: Throws resources at the symptom
- D: Different paradigm (prediction ≠ event-driven)

---

## 4. Critical Evaluation (15% of exam)

**Bloom Level:** Evaluate
**Purpose:** Identify WHY an approach fails in context.

**Key Constraint:** The failure must be non-obvious. The approach should seem reasonable on surface.

**Structure:**

```
SCENARIO (concise, 2-3 sentences):
A team chose [approach] for [situation]. Seems reasonable initially.

STEM (one clear question):
What is the PRIMARY weakness of this approach here?

OPTIONS (concise, one idea each):
**A.** [Secondary weakness, not primary in this context]
**B.** [Correct primary weakness tied to scenario specifics]
**C.** [A strength misframed as weakness]
**D.** [Weakness of a different approach entirely]
```

**Example:**

```
A fintech uses eventual consistency for account balances across three
regions. The system handles deposits and withdrawals. Regulators require
real-time overdraft prevention.

What is the PRIMARY weakness of eventual consistency here?

**A.** Read operations will be slower due to node synchronization
**B.** Overdraft prevention requires strong consistency, which eventual can't provide
**C.** Eventual consistency can't work across geographic regions
**D.** The system needs more storage for cross-region data replication
```

Total: ~80 words. Tests WHY eventual consistency specifically fails for this constraint.

**Distractor Design:**

- A: Describes a problem EC doesn't have (fast reads)
- C: Misunderstands CAP theorem (EC is designed for partitions)
- D: Generic distributed concern, not specific to consistency model

---

## Universal Rules

1. **Clarity:** Write concisely. Difficulty is in thinking, not reading. Use your judgment on length.
2. **Scenario required:** Every question must have a scenario paragraph before the stem.
3. **Distribution:** Each letter correct 20-30% across the full exam.
4. **No memorization:** Never "According to...", "Lesson X", "the document states..."
5. **Concept grounding:** Every question maps to at least one concept from the concept map.
6. **Distractor quality:** Each wrong answer is wrong for a specific, identifiable reason.
7. **Length parity (CRITICAL):** All 4 options must be within 0.8x-1.2x of their mean word count. Target 12-18 words per option. Write the correct answer first, then match distractors to its length. NEVER write a 15-word correct answer with 5-word distractors.
8. **No giveaways:** If a student can identify the correct answer by its length alone, the question is invalid.
