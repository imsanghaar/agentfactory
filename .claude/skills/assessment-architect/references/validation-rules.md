# Validation Rules

Structural checks applied in Phase 3. Questions that FAIL are rejected and regenerated.

---

## Anti-Memorization Checks (FAIL = reject question)

These are grep-based structural checks. No judgment needed - if the pattern matches, the question fails.

```
FAIL if question contains "According to"           (case-insensitive)
FAIL if question contains "Lesson [0-9]"           (references specific lesson)
FAIL if question contains "lesson [0-9]"           (lowercase variant)
FAIL if question contains "the document states"    (source-citing pattern)
FAIL if question contains "as discussed in"        (reference pattern)
FAIL if question contains "as described in"        (reference pattern)
FAIL if question contains "the chapter explains"   (source-citing pattern)
FAIL if question contains "we learned that"        (recall pattern)
```

**Implementation:**

```bash
# Run against question files
grep -inE "(According to|Lesson [0-9]|the document states|as discussed in|as described in|the chapter explains|we learned that)" assessments/{SLUG}-questions-*.md
# If output is non-empty: FAIL - list matching lines
```

---

## Structural Checks (FAIL = reject question)

### Scenario Presence

```
FOR each question:
  scenario = text between question header and stem (first "?" sentence)
  IF scenario is empty or missing: FAIL "Q{N}: no scenario paragraph before stem"
```

### Concept Mapping

```
FOR each question:
  concept_tag = extract [Concept: {name}] from question header
  IF concept_tag not in concept_map: FAIL "Q{N}: concept '{name}' not in concept map"
```

### Transfer Domain Novelty (Transfer Application questions only)

```
FOR each Transfer Application question:
  domain = extract domain from scenario
  IF grep -i "{domain}" {chapter_lessons}: FAIL "Q{N}: transfer domain '{domain}' found in chapter content"
```

---

## Distribution Checks (FAIL = reject batch, redistribute)

### Answer Key Distribution

```
total = count of all questions
count_A = questions with answer A
count_B = questions with answer B
count_C = questions with answer C
count_D = questions with answer D

FOR each letter:
  percentage = count_{letter} / total * 100
  IF percentage < 20: FAIL "Answer {letter} underrepresented ({percentage}%)"
  IF percentage > 30: FAIL "Answer {letter} overrepresented ({percentage}%)"
```

### Consecutive Answer Check

```
answers = ordered list of correct answers
FOR i in range(len(answers) - 3):
  IF answers[i] == answers[i+1] == answers[i+2] == answers[i+3]:
    FAIL "4+ consecutive '{answers[i]}' answers starting at Q{i+1}"
```

### Length Parity Check (Per-Question Ratio — CRITICAL)

```
FOR each question:
  option_words = [wordcount(A), wordcount(B), wordcount(C), wordcount(D)]
  mean_length = mean(option_words)

  FOR each option:
    ratio = option_words[i] / mean_length
    IF ratio < 0.8 OR ratio > 1.2:
      FAIL "Q{N}: Option {letter} is {ratio:.2f}x mean ({option_words[i]} words vs {mean_length:.1f} mean)"
      store as length_violation

# Batch-level threshold
violation_count = count of questions with any length violation
IF violation_count / total > 0.15: FAIL "Length parity failed: {violation_count}/{total} questions have options outside 0.8x-1.2x range"

# Legacy rank check (secondary)
count_longest = count where correct answer has highest word count
IF count_longest / total > 0.40: FAIL "Correct answer is longest option {count_longest}/{total} times"
```

**Remediation for length violations:**

```
FOR each question with length violation:
  IF shortest option < 0.8x mean:
    EXPAND the short option with plausible wrong detail to reach 0.8x-1.2x range
  IF longest option > 1.2x mean:
    SIMPLIFY the long option without changing its correctness/incorrectness

  After adjustment: re-verify all 4 options are within 0.8x-1.2x of NEW mean
```

### Position Bias Check (Middle vs Outer)

```
count_middle = count_B + count_C
count_outer = count_A + count_D

IF count_middle / total > 0.55: FAIL "Middle positions (B+C) overrepresented ({count_middle}/{total})"
IF count_outer / total < 0.40: FAIL "Outer positions (A+D) underrepresented ({count_outer}/{total})"
```

### Specificity Bias Check (see bias-detection-guide.md for full algorithm)

```
FOR each question:
  correct_specificity = score(correct_option)  # word count + examples + qualifiers + technical density
  distractor_avg = mean(score(A), score(B), score(C), score(D)) - score(correct)

  IF correct_specificity > distractor_avg * 1.30:
    WARN "Q{N}: Correct option significantly more specific than distractors"
    FLAG for manual review

# Batch-level threshold
IF warned_count / total > 0.20: FAIL "Specificity bias detected in {warned_count}/{total} questions"
```

---

## Type Distribution Check

```
expected_scenario = total * 0.40
expected_relationship = total * 0.25
expected_transfer = total * 0.20
expected_evaluation = total * 0.15

FOR each type:
  actual = count of questions with [TYPE] tag matching
  IF actual < expected * 0.85: FAIL "{type} underrepresented ({actual} vs {expected})"
  IF actual > expected * 1.15: FAIL "{type} overrepresented ({actual} vs {expected})"
```

---

## Concept Coverage Check (WARNING, not FAIL)

```
concepts_in_map = list of all concepts from concept map
concepts_tested = unique concepts referenced in questions

coverage = len(concepts_tested) / len(concepts_in_map) * 100
uncovered = concepts_in_map - concepts_tested

REPORT: "{coverage}% concept coverage ({len(concepts_tested)}/{len(concepts_in_map)})"
IF uncovered: WARN "Untested concepts: {list uncovered}"
```

---

## Validation Report Format

After running all checks, produce:

```markdown
## Validation Report

### Anti-Memorization: {PASS/FAIL}

- Recall patterns found: {N} questions
- Failed questions: {list Q numbers and matched patterns}

### Structure: {PASS/FAIL}

- Missing scenario: {N} questions
- Missing concept mapping: {N} questions
- Transfer domain in chapter: {N} questions

### Bias Detection: {PASS/FAIL/WARN}

- Length parity: {PASS/FAIL} ({N}/{total} questions outside 0.8x-1.2x ratio)
  - Mean correct-to-distractor ratio: {X.Xx} (target: 0.8-1.2x)
  - Worst violations: Q{N} ({ratio}x), Q{N} ({ratio}x)
- Position bias: {PASS/FAIL} (A={N}% B={N}% C={N}% D={N}%, middle={N}%)
- Specificity bias: {PASS/WARN} ({N} questions flagged for review)

### Distribution: {PASS/FAIL}

- Answer distribution: A={N}({%}) B={N}({%}) C={N}({%}) D={N}({%})
- Consecutive violations: {N}

### Type Distribution: {PASS/FAIL}

- Scenario Analysis: {actual} (expected {expected})
- Concept Relationship: {actual} (expected {expected})
- Transfer Application: {actual} (expected {expected})
- Critical Evaluation: {actual} (expected {expected})

### Concept Coverage: {X}% ({tested}/{total})

- Uncovered: {list}

### Overall: {PASS / FAIL - N issues}
```

---

## Remediation Procedure

If validation fails:

1. **Identify which subagent produced failures**
   - Check file: `questions-A.md` failures → re-spawn Subagent A
   - Check file: `questions-B.md` failures → re-spawn Subagent B

2. **Report to user:**

   ```
   Validation failed: {N} questions rejected
   - Anti-memorization: {N} (Subagent {A/B})
   - Structural: {N} (Subagent {A/B})
   - Distribution: {fix by redistributing, no regeneration needed}
   ```

3. **Regenerate only the failing subagent** with additional instruction:

   ```
   IMPORTANT: Your previous output had {N} questions rejected for:
   {list specific failures}

   Ensure NONE of these patterns appear in your output.
   ```

4. **Re-validate** after regeneration. Maximum 2 regeneration attempts.
   If still failing after 2 attempts: report to user with specific failures for manual review.
