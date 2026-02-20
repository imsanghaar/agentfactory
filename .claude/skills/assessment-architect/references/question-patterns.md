# Question Patterns

Structural patterns for the 4 question types. Every pattern enforces the scenario-first, concept-grounded approach.

---

## Universal Pattern Structure

ALL questions follow this structure regardless of type:

```
[HEADER]     **Q{N}.** [{TYPE}] [Concept: {concept_name}]
[SCENARIO]   {>20 words} Novel situation providing context
[STEM]       {>15 words} Specific analytical question
[OPTIONS]    A-D, each ≤25 words, similar length
[ANSWER]     Single letter
[REASONING]  Why correct + why each distractor fails
```

---

## Pattern 1: Scenario Analysis (40%)

**Cognitive demand:** Apply a concept to analyze a new situation.

### Template
```
**Q{N}.** [Scenario Analysis] [Concept: {concept}]

{A team/organization/system faces a specific challenge. Include details about
constraints, stakeholders, current state, and desired outcome. The situation
must NOT appear in any lesson - it is novel.}

Given {specific constraint from scenario}, which approach would most
effectively {desired outcome} while {maintaining constraint}?

**A.** {Addresses symptom, not root cause - plausible but shallow}
**B.** {Correct - addresses root cause using the concept}
**C.** {Applies concept to wrong aspect of the scenario}
**D.** {Over-engineers - correct concept but disproportionate to problem}

**Answer:** B
**Reasoning:** B correctly applies {concept} because {explanation}.
A fails because {reason}. C fails because {reason}. D fails because {reason}.
```

### 3 Scenario Analysis Sub-Patterns

**1A: Constraint Satisfaction**
- Scenario presents 2-3 constraints
- Correct answer satisfies all; each distractor violates one
- Tests: Can student identify which approach meets ALL requirements?

**1B: Root Cause Analysis**
- Scenario describes symptoms of a problem
- Correct answer addresses underlying cause
- Tests: Can student distinguish cause from effect?

**1C: Scale/Context Shift**
- Scenario changes scale (small→large) or context (startup→enterprise)
- Correct answer accounts for what changes at new scale
- Tests: Can student reason about how concepts behave at different scales?

---

## Pattern 2: Concept Relationship (25%)

**Cognitive demand:** Understand how concepts interact, enable, or conflict.

### Template
```
**Q{N}.** [Concept Relationship] [Concept: {concept_A}, {concept_B}]

{A situation where two concepts from the chapter interact. Show the
relationship in action through observable effects - don't just state
the concepts exist.}

This situation best demonstrates which relationship between {concept_A}
and {concept_B}?

**A.** {Reverses the direction of the relationship}
**B.** {Correct - accurately describes how A relates to B}
**C.** {Confuses this relationship with a different concept pair}
**D.** {Denies the relationship exists or claims independence}

**Answer:** B
**Reasoning:** The scenario shows {concept_A} {relationship} {concept_B}
because {evidence from scenario}. A reverses this. C confuses with
{other pair}. D incorrectly claims independence.
```

### 3 Concept Relationship Sub-Patterns

**2A: Enabling Relationship**
- Concept A makes Concept B possible or more effective
- Scenario shows what happens when A is present/absent
- Tests: Does student understand the dependency direction?

**2B: Tension/Conflict**
- Concept A and B pull in opposite directions
- Scenario forces a choice between optimizing for A vs B
- Tests: Does student understand the trade-off mechanism?

**2C: Composition/Extension**
- Concept B builds on or extends Concept A
- Scenario shows the layered/composed behavior
- Tests: Does student understand the building-block relationship?

---

## Pattern 3: Transfer Application (20%)

**Cognitive demand:** Apply a principle from the chapter to a completely different domain.

### Template
```
**Q{N}.** [Transfer Application] [Concept: {concept}]

{A situation in [NOVEL DOMAIN - not in chapter] that shares structural
similarity with the concept. Describe the domain-specific problem without
using chapter terminology.}

Applying the principle of {concept} to this {domain} context, which
approach would most effectively address {domain-specific goal}?

**A.** {Surface-level analogy - matches vocabulary but not structure}
**B.** {Correct structural transfer - applies the underlying principle}
**C.** {Applies a different chapter concept incorrectly}
**D.** {Domain-specific solution that ignores the transferable principle}

**Answer:** B
**Reasoning:** The structural principle of {concept} is {abstract form}.
In {domain}, this manifests as {B's approach}. A matches surface features
only. C applies {wrong concept}. D solves without leveraging the principle.
```

### Key Rules for Transfer

1. **Domain validation:** grep chapter content for the transfer domain. Must return 0 matches.
2. **Structural, not surface:** The correct answer transfers the STRUCTURE, not the vocabulary.
3. **Domain authenticity:** The scenario should feel natural in the target domain, not forced.
4. **Principle extraction:** The concept map's "Transfer domains" field suggests valid targets.

### Transfer Domain Categories

| Domain Category | Example Domains | Works For |
|----------------|-----------------|-----------|
| Healthcare | Hospital scheduling, patient data, triage | Event systems, data flow, prioritization |
| Urban Planning | Traffic, zoning, public transit | Architecture, scaling, constraint satisfaction |
| Agriculture | Crop rotation, irrigation, harvest timing | Lifecycle management, optimization, scheduling |
| Education | Curriculum design, assessment, class grouping | Modularity, progression, feedback loops |
| Manufacturing | Assembly lines, quality control, inventory | Pipeline patterns, validation, throughput |
| Sports | Team strategy, training, game analysis | Coordination, optimization, decision-making |

---

## Pattern 4: Critical Evaluation (15%)

**Cognitive demand:** Identify WHY a chosen approach fails in a specific context.

### Template
```
**Q{N}.** [Critical Evaluation] [Concept: {concept}]

{A team/organization has chosen [specific approach] for [specific goal].
The approach seems reasonable on the surface. Include details that reveal
a subtle mismatch between the approach and the context's requirements.}

What is the PRIMARY weakness of this approach given the specific
constraints described in the scenario?

**A.** {Real weakness but SECONDARY - not the main issue here}
**B.** {Correct PRIMARY weakness - tied to scenario-specific constraints}
**C.** {Actually a STRENGTH misframed as a weakness}
**D.** {Weakness of a DIFFERENT approach, not the one described}

**Answer:** B
**Reasoning:** The primary weakness is {B} because the scenario specifies
{constraint} which directly conflicts with {approach's property}. A is
real but secondary. C is actually beneficial. D describes {other approach}'s
weakness.
```

### 3 Critical Evaluation Sub-Patterns

**4A: Constraint Mismatch**
- Approach is valid in general but fails given scenario's specific constraint
- Tests: Can student identify when a generally-good approach is wrong?

**4B: Scale Failure**
- Approach works at current scale but breaks at scenario's described scale
- Tests: Can student reason about scaling limitations?

**4C: Hidden Assumption**
- Approach works IF an unstated assumption holds, but scenario violates it
- Tests: Can student identify implicit assumptions in solutions?

---

## Distractor Quality Checklist

For ALL patterns, verify each distractor:

- [ ] Is wrong for a specific, identifiable reason
- [ ] Would be chosen by a student with a specific misconception
- [ ] Is similar length to the correct answer (within 5 words)
- [ ] Is grammatically consistent with the stem
- [ ] Is related to the topic (not absurd)
- [ ] Cannot be eliminated without understanding the scenario

---

## Anti-Patterns (Questions to NEVER Generate)

```
WRONG: "What is the definition of [concept]?"
       → Tests recall, not understanding

WRONG: "According to Lesson 5, which of the following..."
       → Cites source, tests memorization

WRONG: "Which of the following is true about [concept]?"
       → No scenario, no analytical demand

WRONG: "[Concept] was introduced in [year]. What is its primary purpose?"
       → Tests fact + definition, not application

WRONG: "List three benefits of [concept]."
       → Even as MCQ, tests recall not analysis
```
