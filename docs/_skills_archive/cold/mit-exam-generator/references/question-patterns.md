# Question Type Patterns

Templates and examples for each question type.

---

## 1. Precision Recall (10%)

**Purpose:** Test exact knowledge of facts, numbers, definitions.

**Pattern:**
```
According to [source], [specific measurable claim]?
A) [Wrong value - close but incorrect]
B) [Wrong value - common misconception]
C) [Correct value from source]
D) [Wrong value - plausible alternative]
```

**Example:**
```
Q: According to the document, a Digital FTE operates how many hours weekly?
A) 120 hours
B) 148 hours
C) 168 hours
D) 200 hours

Correct: C (168 = 24 x 7, explicitly stated)
```

**Distractor Strategy:** Use values that are:
- Mathematically close (120, 148)
- Represent common assumptions (200 = "always working")
- Could be confused with related metrics

---

## 2. Conceptual Distinction (15%)

**Purpose:** Test understanding of differences between related concepts.

**Pattern:**
```
Which BEST differentiates [Concept A] from [Concept B]?
A) [Surface-level difference - incomplete]
B) [Correct fundamental distinction]
C) [Related but not distinguishing]
D) [Common misconception about difference]
```

**Example:**
```
Q: Which BEST differentiates synchronous from asynchronous communication?
A) Speed of message delivery
B) Whether sender blocks waiting for response
C) Network protocol used
D) Message format requirements

Correct: B (blocking behavior is the fundamental distinction)
```

**Distractor Strategy:**
- Option that's true but not THE key distinction
- Technical detail that's incidental
- Common but incorrect belief

---

## 3. Decision Matrix (12.5%)

**Purpose:** Test multi-criteria decision-making ability.

**Pattern:**
```
Given constraints [X, Y, Z], which approach is MOST appropriate?
A) [Fails on constraint X]
B) [Fails on constraint Y]
C) [Satisfies all constraints]
D) [Fails on constraint Z]
```

**Example:**
```
Q: A team needs a solution that is: low-cost, fast to implement, and
   requires no infrastructure changes. Which approach fits?
A) Custom-built microservice (fails: slow to implement)
B) Enterprise platform license (fails: high cost)
C) Managed SaaS integration (satisfies all)
D) On-premise installation (fails: infrastructure changes)

Correct: C
```

---

## 4. Architecture Analysis (12.5%)

**Purpose:** Test understanding of system structure and data flow.

**Pattern:**
```
In [system/architecture], what is the role of [component]?
A) [Role of different component]
B) [Correct role]
C) [Partial/incomplete role]
D) [Plausible but incorrect role]
```

**Example:**
```
Q: In event-driven architecture, what is the primary role of the message broker?
A) Process and transform events
B) Decouple producers from consumers
C) Store events permanently
D) Validate event schemas

Correct: B (decoupling is primary; others may be secondary features)
```

---

## 5. Economic/Quantitative (10%)

**Purpose:** Test ability to perform calculations and comparisons.

**Pattern:**
```
Given [values from source], calculate [metric].
A) [Common calculation error]
B) [Correct calculation]
C) [Wrong formula applied]
D) [Off-by-one or unit error]
```

**Example:**
```
Q: Human FTE costs $6,000/month, Digital FTE costs $1,500/month.
   What is the annual savings per replacement?
A) $18,000 (monthly difference only)
B) $54,000 (correct: $4,500 x 12)
C) $36,000 (wrong multiplier)
D) $72,000 (doubled incorrectly)

Correct: B
```

**Calculation Types:**
- ROI / cost-benefit
- Break-even analysis
- Efficiency ratios
- Comparative metrics

---

## 6. Specification Design (10%)

**Purpose:** Test ability to apply frameworks and methodologies.

**Pattern:**
```
When applying [framework/methodology] to [scenario], what should be [specified element]?
A) [Violates framework principle]
B) [Correct application]
C) [Over-engineers the solution]
D) [Under-specifies requirements]
```

---

## 7. Critical Evaluation (12.5%)

**Purpose:** Test judgment and trade-off analysis.

**Pattern:**
```
What is the PRIMARY limitation/risk/trade-off of [approach]?
A) [Minor concern, not primary]
B) [Correct primary limitation]
C) [Benefit misframed as limitation]
D) [Limitation of different approach]
```

**Example:**
```
Q: What is the PRIMARY trade-off of eventual consistency?
A) Higher infrastructure costs
B) Temporary data inconsistency across nodes
C) Slower write performance
D) Complex deployment requirements

Correct: B (this is THE defining trade-off)
```

---

## 8. Strategic Synthesis (10%)

**Purpose:** Test integration of multiple concepts.

**Pattern:**
```
To achieve [goal] while maintaining [constraint], which combination of [elements] is optimal?
A) [Incomplete combination]
B) [Conflicting elements]
C) [Correct synergistic combination]
D) [Overkill/unnecessary elements]
```

---

## 9. Research Extension (7.5%)

**Purpose:** Test extrapolation to novel scenarios.

**Pattern:**
```
If [established principle from source] were applied to [novel scenario], what outcome would be expected?
A) [Misapplication of principle]
B) [Correct extrapolation]
C) [Ignores key constraint]
D) [Over-generalizes principle]
```

---

## Distractor Quality Guidelines

Good distractors are:
- **Plausible** (70-90% correct, fail on critical detail)
- **Non-obvious** (require understanding to eliminate)
- **Distinct** (each wrong for different reason)
- **Educational** (reveal common misconceptions)

Avoid:
- Absurd options
- "Trick" wording
- Ambiguous language
- Multiple correct answers
