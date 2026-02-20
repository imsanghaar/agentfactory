# Bias Detection & Prevention Guide

Comprehensive guide to understanding, detecting, and preventing answer option biases in exams.

---

## Overview

**The Problem:** Students can achieve 25-40% accuracy on multiple-choice exams by recognizing patterns rather than understanding content.

**Common Patterns:**

- "The longest answer is usually correct" → Achieves 20-30% accuracy
- "Pick B or C when unsure" → Achieves 25-30% accuracy
- "Most specific option wins" → Achieves 15-25% accuracy

**The Solution:** Three automated checks ensure these strategies fail.

---

## Three Biases We Prevent

### 1. Length Bias

**Pattern:** Students learn "the longest option is usually correct"

**Why it works:** Exam creators often provide detailed, specific correct answers while keeping distractors short. In one real assessment, correct answers averaged 22.7 words while distractors averaged 9.4 words (2.42x ratio). A student who simply picks the longest option gains a significant advantage.

#### Detection

**Primary Method (Per-Question Ratio Check):** For each question, calculate the mean word count of all 4 options. Every option must fall within 0.8x-1.2x of that mean.

**Thresholds:**

- Per-question: Any option outside 0.8x-1.2x = FAIL that question
- Batch-level: >15% of questions with violations = FAIL the exam
- Secondary: Correct answer is longest in >40% of questions = FAIL

**Example (detecting bias with ratio method):**

```markdown
Q1: What change would improve her results?
**A.** Reduce involvement to autocomplete only [6 words]
**B.** Switch to a more capable model [7 words]
**C.** Write detailed specifications for each function and validate the AI's complete output against them [15 words - CORRECT]
**D.** Continue until the AI learns her style [7 words]

Mean word count: (6 + 7 + 15 + 7) / 4 = 8.75
Option C ratio: 15 / 8.75 = 1.71x → FAIL (exceeds 1.2x)
Option A ratio: 6 / 8.75 = 0.69x → FAIL (below 0.8x)

Result: Q1 FAILS length parity check ✗
```

#### Remediation

**Rewrite all options to similar length (not just swap positions):**

```markdown
Q1 FIXED: What change would improve her results?
**A.** Limit the AI to autocomplete mode and manually write the rest of each function [15 words]
**B.** Replace the current model with a higher-tier one that produces cleaner code output [14 words]
**C.** Write detailed specifications first and validate the AI's complete output against them [12 words - CORRECT]
**D.** Continue the current workflow and wait for the AI to adapt to her coding patterns [15 words]

Mean word count: (15 + 14 + 12 + 15) / 4 = 14.0
All ratios: 1.07x, 1.00x, 0.86x, 1.07x → ALL within 0.8-1.2x ✓
```

**Key insight:** Moving the longest option to a different position does NOT fix length bias. It only fixes position bias. To fix length bias, you must rewrite the SHORT options to match the LONG one (or simplify the long one and match all to it).

---

### 2. Position Bias

**Pattern:** Students learn "pick B or C when unsure" (middle options)

**Why it works:** Exam creators often place correct answers toward middle positions (B and C) or avoid edges (A and D).

**Psychology:** Test-takers subconsciously avoid extremes. Creators may unconsciously cluster correct answers.

#### Detection

**Method:** Count how many correct answers are in each position (A/B/C/D).

**Thresholds:**

- Each letter should be 20-30% of total
- Middle (B+C) ≤55%
- Outer (A+D) ≥40%

**Example (detecting bias):**

```
200-question exam analysis:

Distribution Analysis:
  Position A: 30 correct (15%) ✗ Too low (threshold: 20-30%)
  Position B: 60 correct (30%) ✓ Acceptable
  Position C: 60 correct (30%) ✓ Acceptable
  Position D: 50 correct (25%) ✓ Acceptable

Middle (B+C): 120/200 = 60% ✗ TOO HIGH (threshold: ≤55%)
Outer (A+D): 80/200 = 40% ✓ Minimum acceptable

Finding: Position bias detected (60% middle vs 40% outer)
Problem: Students can guess B/C and get 30% accuracy → FAIL ✗
```

#### Remediation

**Automated Sequence Application:** Use pre-made answer sequences from `distribute_answers_v2.py`.

**8 Proven Sequences** (A-H):

- Sequence A: [2,0,3,1,2,0,1,3,2,0,1,3,0,2,1,3,...]
- Sequence B: [1,3,0,2,1,3,0,2,3,1,0,2,3,1,2,0,...]
- (6 more sequences, each guarantees 25% per letter)

**Properties of sequences:**

- Exactly 25% per letter (50 of each for 200 questions)
- No >3 consecutive same letters
- No alternating/cycling patterns
- Proven through quiz-generator use

**Example (after fix):**

```
Applying Sequence A: [2,0,3,1,2,0,1,3,2,0,1,3,...]

Q1-Q50 distributed to positions: C,A,D,B,C,A,B,D,C,A,B,D,...
Q51-Q100 distributed to positions: A,D,B,C,A,D,C,B,A,D,C,B,...
Q101-Q150 distributed to positions: C,B,D,A,C,B,D,A,C,B,D,A,...
Q151-Q200 distributed to positions: B,A,C,D,B,A,C,D,B,A,C,D,...

Result after redistribution:
  Position A: 50/200 = 25% ✓
  Position B: 50/200 = 25% ✓
  Position C: 50/200 = 25% ✓
  Position D: 50/200 = 25% ✓

Middle: 100/200 = 50% ✓ (under 55% threshold)
Outer: 100/200 = 50% ✓ (over 40% threshold)

Guessing B/C now yields 25% accuracy (random chance) → PASS ✓
```

---

### 3. Specificity Bias

**Pattern:** Students learn "the most detailed/specific option is usually correct"

**Why it works:** Correct answers often include examples, qualifications, and details while distractors are vague.

**Psychology:** Detailed options sound more authoritative and confident.

#### Detection

**Method:** Calculate specificity score (0-100) for each option, compare correct vs average distractor.

**Scoring factors:**

1. **Word count** (0-20 pts): Longer usually = more specific
2. **Examples** (0-30 pts): "e.g.", "such as", "for instance" (10 pts each)
3. **Qualifiers** (0-20 pts): "typically", "usually", "often" (5 pts each)
4. **Technical density** (0-30 pts): Percentage of capitalized terms

**Specificity Formula:**

```python
score = (word_count × 0.5) + (example_count × 10) + (qualifier_count × 5) + (technical_density × 30)
# Capped at 100
```

**Example (detecting bias):**

```markdown
Q: What best describes the role of the API gateway?

**A.** It's important.
Specificity: (2 words × 0.5) + 0 + 0 + 0 = 1/100

**B.** Manages incoming requests and routes them to appropriate backend services.
Specificity: (9 words × 0.5) + 0 + 0 + (technical words) = 15/100

**C.** Acts as a centralized entry point that handles cross-cutting concerns
such as authentication, rate limiting, logging, and request transformation,
ensuring consistent policies across all microservices.
Specificity: (35 words × 0.5) + (1 example: "such as") + (4 qualifiers implied) = 57/100
[CORRECT]

**D.** It helps with stuff.
Specificity: (4 words × 0.5) + 0 + 0 + 0 = 2/100

Analysis:
Correct score: 57/100
Distractor average: (1 + 15 + 2) / 3 = 6/100
Gap: (57 - 6) / 6 = 850% ✗ MASSIVE BIAS

Finding: Correct answer 8.5x more specific than average distractor
Problem: Students can pick the longest, most detailed option and get high accuracy
Severity: CRITICAL (>50% questions show this pattern) → FAIL ✗
```

#### Remediation

**Manual Review Required:** Semantic meaning is critical; automated changes risk breaking correctness.

**Option 1: Enhance Distractors**

```markdown
Before (weak distractors):
**C.** Acts as a centralized entry point that handles cross-cutting concerns
such as authentication, rate limiting, logging, and request transformation,
ensuring consistent policies across all microservices. [CORRECT - very specific]

**A.** It's important. [Too vague]

After (enhanced):
**C.** Acts as a centralized entry point that handles cross-cutting concerns
such as authentication, rate limiting, and request transformation. [CORRECT - still specific]

**A.** Manages incoming requests and routes them to services based on a static routing table.
[Same specificity level, but incorrect]
```

**Option 2: Simplify Correct Answer**

```markdown
Before:
**C.** Acts as a centralized entry point that handles cross-cutting concerns
such as authentication, rate limiting, logging, and request transformation,
ensuring consistent policies across all microservices. [CORRECT]

After:
**C.** Centralizes handling of cross-cutting concerns like authentication and rate limiting. [CORRECT]
```

**Option 3: Regenerate Question**

```markdown
Before (problem: correct is too specific):
Q: What role does the API gateway play?
**C.** [Very specific, detailed answer] - CORRECT

After (solution: all options equally specific):
Q: Select the PRIMARY role of the API gateway:
**A.** Centralized request validation with policy enforcement [Specific but incorrect]
**B.** Centralized request routing with cross-cutting concerns handling [Specific and CORRECT]
**C.** Decentralized service discovery with client-side routing [Specific but incorrect]
**D.** Load balancing with direct client-to-service connections [Specific but incorrect]

Now all options are equally specific, so guess-by-detail doesn't work.
```

---

## Running Bias Detection

### From Command Line

```bash
# Check for biases (report only)
python scripts/bias_detector.py exam-file.md

# Auto-fix remediable biases
python scripts/bias_detector.py exam-file.md --fix-auto

# Full validation pipeline
python scripts/validate_exam.py exam-file.md --fix-auto --verbose

# Export results as JSON
python scripts/validate_exam.py exam-file.md --json
```

### Output Format

```
============================================================
BIAS DETECTION REPORT
============================================================

✓ LENGTH: NONE
   0.0% affected
   • No significant length bias detected

✓ POSITION: PASS (FIXED: Applied sequence C)
   Distribution: A:24%, B:26%, C:25%, D:25%
   • ✓ Remediation applied

⚠ SPECIFICITY: WARNING
   4.0% affected (8 questions)
   • Affected questions: [15, 23, 47, 89, 112, 145, 167, 193]
   • Manual review recommended (enhance distractors)

============================================================
OVERALL: PASS with warnings
============================================================
```

---

## Thresholds & Tuning

All thresholds are configurable in `scripts/config.py`:

```python
BIAS_THRESHOLDS = {
    'length_parity': {
        'ratio_min': 0.80,     # Each option must be ≥0.8x of mean
        'ratio_max': 1.20,     # Each option must be ≤1.2x of mean
        'batch_fail': 0.15,    # >15% of questions with violations = FAIL
    },
    'length_rank': {           # Legacy rank-based check (secondary)
        'high': 0.40,          # 40%+ correct is longest = FAIL
    },
    'position': {
        'middle_max': 0.55,    # B+C ≤55%
        'outer_min': 0.40,     # A+D ≥40%
        'letter_min': 0.20,    # Each letter ≥20%
        'letter_max': 0.30     # Each letter ≤30%
    },
    'specificity': {
        'score_gap': 0.30,             # 30% more specific
        'question_pct_high': 0.50,     # >50% = high
        'question_pct_medium': 0.35,   # 35-50% = medium
        'question_pct_low': 0.20       # 20-35% = low
    }
}
```

### Adjusting Thresholds

**Stricter (harder to pass):**

```python
'length': {'high': 0.55}  # Flag if 55%+ same rank (vs 60%)
'position': {'middle_max': 0.50}  # Middle ≤50% (vs 55%)
```

**Lenient (easier to pass):**

```python
'length': {'high': 0.65}  # Flag only if 65%+ same rank
'position': {'middle_max': 0.60}  # Middle ≤60%
```

---

## FAQ

### Q: Why these specific thresholds?

**Length Bias (60%):**

- Random chance per position = 25%
- 60% means only 35% more than random
- Allows for natural variation while catching real bias

**Position Bias (25% per letter):**

- 25% = perfect balance
- ±5% tolerance = 20-30%
- Middle ≤55% prevents "B/C strategy"

**Specificity Bias (30% gap):**

- 30% = clearly more specific (not marginal)
- Catches obvious bias while avoiding false positives

### Q: What if I disagree with auto-fixes?

**You can:**

1. Disable auto-fix: Use `--report-only` flag
2. Manually review changes before accepting
3. Adjust thresholds in `config.py` for your needs
4. Create custom sequences instead of pre-made

### Q: How much does bias detection slow down generation?

**Typical overhead:**

- 200-question exam: <5 seconds
- 100-question exam: <2 seconds
- Detection runs after generation (independent)

### Q: Can biases return after auto-fix?

**No.** Pre-made sequences guarantee the math:

- If sequence places A in position 0, B in position 1, ...
- Then distributing answers per sequence guarantees exact distribution

### Q: What if my domain naturally needs longer correct answers?

**Three options:**

1. **Accept the bias:** If domain requires it, document explicitly
2. **Standardize length:** Use templates that enforce ±2 word range
3. **Change question format:** Use matching/ordering instead of MCQ

### Q: How do I validate the validation?

Test on known-good exams:

```bash
# Run on your best existing exams
python scripts/bias_detector.py my_good_exam.md

# Should show low/no bias
# If it fails, review the detected issues
# Adjust thresholds if legitimate
```

---

## Performance Benchmarks

Tested on various exam sizes:

| Questions | Length Detection | Position Detection | Specificity Detection | Total |
| --------- | ---------------- | ------------------ | --------------------- | ----- |
| 50        | 0.8s             | 0.3s               | 4.2s                  | 5.3s  |
| 100       | 1.5s             | 0.6s               | 8.1s                  | 10.2s |
| 200       | 3.2s             | 1.2s               | 16.8s                 | 21.2s |
| 500       | 8.0s             | 3.0s               | 42.0s                 | 53.0s |

**Target:** Complete validation <30 seconds for 200 questions ✓

---

## References

- Configuration: `scripts/config.py`
- Bias Detection: `scripts/bias_detector.py`
- Validation Orchestration: `scripts/validate_exam.py`
- Validation Rules: `references/validation-rules.md`
