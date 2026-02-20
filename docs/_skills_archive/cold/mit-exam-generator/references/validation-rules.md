# Validation Rules

Quality criteria that MUST pass before delivering an exam.

---

## Pre-Delivery Validation Pipeline

Run ALL checks. Fix failures before delivery.

```
VALIDATE
├── Structure Checks
│   ├── Question count matches target
│   ├── All questions have 4 options (A-D)
│   ├── Sequential numbering (no gaps)
│   └── Proper markdown formatting
│
├── Answer Distribution Checks
│   ├── Each letter 20-30% of total
│   ├── No >3 consecutive same letter
│   └── Random distribution (no patterns)
│
├── Content Coverage Checks
│   ├── All source sections represented
│   ├── Question type distribution met
│   └── Bloom level distribution met
│
├── Quality Checks
│   ├── No ambiguous wording
│   ├── No multiple correct answers
│   ├── Distractors are plausible
│   └── No direct quotes in explanations
│
└── Source Integrity Checks
    ├── Every question has section reference
    ├── All facts verifiable in source
    └── No external knowledge required
```

---

## Structure Validation

### Question Count

| Content Density | Target Questions |
|-----------------|------------------|
| Rich (100+ concepts) | 200 |
| Moderate (50-99) | 100 |
| Light (25-49) | 50 |
| Sparse (<25) | max(25, concepts) |

**Rule:** Actual count must be within 5% of target.

### Format Requirements

- [ ] Each question starts with `**Q[N].**`
- [ ] Exactly 4 options: A), B), C), D)
- [ ] One blank line between questions
- [ ] Answer key table complete
- [ ] Explanation section complete

---

## Answer Distribution Validation

### Letter Balance

```
For N total questions:
  Expected per letter = N / 4
  Acceptable range = Expected ± 10%

Example (200 questions):
  Expected: 50 per letter
  Acceptable: 45-55 per letter
```

**Failure:** Redistribute answers if any letter outside range.

### Sequence Check

```
Maximum consecutive same-letter answers: 3

FAIL: A, A, A, A (4 consecutive)
PASS: A, A, A, B (3 consecutive, then break)
```

**Failure:** Swap answers to break sequences.

### Pattern Detection

Check for predictable patterns:
- No alternating (A,B,A,B,A,B)
- No cycling (A,B,C,D,A,B,C,D)
- No clustering by section

---

## Content Coverage Validation

### Question Type Distribution

| Type | Target % | Acceptable Range |
|------|----------|------------------|
| Precision Recall | 10% | 8-12% |
| Conceptual Distinction | 15% | 13-17% |
| Decision Matrix | 12.5% | 10-15% |
| Architecture Analysis | 12.5% | 10-15% |
| Economic/Quantitative | 10% | 8-12% |
| Specification Design | 10% | 8-12% |
| Critical Evaluation | 12.5% | 10-15% |
| Strategic Synthesis | 10% | 8-12% |
| Research Extension | 7.5% | 5-10% |

### Bloom Level Distribution

| Level | Target % | Acceptable Range |
|-------|----------|------------------|
| Remember/Understand | 25% | 20-30% |
| Apply | 20% | 15-25% |
| Analyze | 25% | 20-30% |
| Evaluate | 18% | 13-23% |
| Create/Synthesize | 12% | 8-16% |

### Source Section Coverage

```
For each section in source:
  minimum_questions = ceil(section_weight * total_questions * 0.5)

IF any section has < minimum_questions:
  FAIL - Generate more questions for that section
```

---

## Quality Validation

### Ambiguity Check

Questions MUST NOT contain:
- "could be" / "might be" (unless intentional)
- Double negatives
- "always" / "never" (unless factually absolute)
- Undefined pronouns ("it", "this" without clear referent)

### Single Correct Answer

For each question verify:
- Exactly ONE option is fully correct
- Other options have identifiable flaw
- No "equally correct" options

### Distractor Plausibility

Distractors must be:
- Related to the topic
- Grammatically consistent with stem
- Similar length to correct answer
- Not obviously wrong

**Red Flags:**
- One option much longer than others
- Joke or absurd options
- "All of the above" / "None of the above"

### No Direct Quotes

Explanations must use:
- Paraphrasing
- Section references ("As discussed in [Section Name]...")
- Concept references

**NOT:** "The document states '...' therefore..."

---

## Source Integrity Validation

### Section Reference Required

Every question MUST have:
```
Section: [Exact heading from source]
```

### Fact Verification

All numerical values, definitions, and claims must be:
- Directly from source, OR
- Logically derivable from source

**NOT:** External knowledge, assumptions, or generalizations

### Self-Contained

The exam must be answerable using ONLY the source material.
No questions requiring:
- External references
- Prior domain knowledge
- Information from other sources

---

## Validation Report Format

Generate after all checks:

```markdown
## Validation Report

### Summary
- Total Questions: [N]
- Target: [M]
- Status: [PASS/FAIL]

### Structure
- [ ] Question count: [N]/[M] ([PASS/FAIL])
- [ ] Format compliance: [PASS/FAIL]
- [ ] Sequential numbering: [PASS/FAIL]

### Answer Distribution
- A: [N] ([%]) [PASS/FAIL]
- B: [N] ([%]) [PASS/FAIL]
- C: [N] ([%]) [PASS/FAIL]
- D: [N] ([%]) [PASS/FAIL]
- Max consecutive: [N] [PASS/FAIL]

### Content Coverage
- Question types: [All within range / X types out of range]
- Bloom levels: [All within range / X levels out of range]
- Section coverage: [All sections covered / X sections under-represented]

### Quality
- Ambiguity issues: [N]
- Multiple correct: [N]
- Weak distractors: [N]
- Quote violations: [N]

### Source Integrity
- Missing references: [N]
- Unverifiable facts: [N]

### Overall: [PASS / FAIL - X issues to fix]
```

---

## Failure Remediation

| Failure Type | Remediation |
|--------------|-------------|
| Answer imbalance | Swap correct answers to balance |
| Consecutive sequence | Reorder questions or swap answers |
| Missing question type | Generate additional questions of that type |
| Missing Bloom level | Adjust existing or add questions |
| Weak distractors | Rewrite with stronger alternatives |
| Quote in explanation | Paraphrase and add section reference |
| Missing section ref | Add appropriate reference |

**Process:** Fix all failures, then re-run validation until PASS.
