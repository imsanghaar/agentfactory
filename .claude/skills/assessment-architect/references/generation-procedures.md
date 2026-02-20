# Generation Procedures: Concept-First Workflow

Step-by-step procedures for the 4-phase assessment generation workflow.

---

## Phase 1: Concept Extraction Procedure

**Executor:** The forked skill agent (not a subagent)

### Step 1.1: Discover and Read Lessons

```
1. PATH confirmed from Input Parsing (SKILL.md)
2. List all lessons:
   ls {PATH}/*.md | grep -v README | grep -v summary | grep -v quiz
3. Count: wc -l
4. Read ALL lessons (not a sample)
```

### Step 1.2: Extract Concepts

For each lesson, identify:

- Named concepts (ideas, patterns, principles worth testing)
- Skip facts (dates, version numbers, statistics, definitions)

**Decision criteria:** "Could I write a scenario-based question about this?"

- YES → It's a concept (extract it)
- NO → It's a fact (skip it)

See `references/concept-extraction-guide.md` for detailed extraction rules.

### Step 1.3: Map Relationships

After extracting all concepts:

1. For each pair of concepts, ask: "Does A affect B?"
2. If yes, classify: enables / conflicts-with / extends / requires / alternative-to
3. Record with direction: `A --enables--> B`

### Step 1.4: Identify Trade-offs

Scan for patterns:

- "X vs Y" comparisons in lessons
- "advantage/disadvantage" discussions
- "when to use" decision points

### Step 1.5: Generate Transfer Domains

For each concept:

1. Identify the STRUCTURAL principle (strip domain-specific details)
2. Brainstorm 2-3 domains where this structure applies
3. Verify domain NOT in chapter: `grep -ri "{domain}" {PATH}/`
4. If grep returns matches: discard that domain, try another

### Step 1.6: Write Concept Map

Output to `assessments/{SLUG}-concepts.md` following the format in `concept-extraction-guide.md`.

### Step 1.7: Calculate Question Count

```
concept_count = number of concepts extracted
base = ceil(concept_count * 0.8)
tier_multiplier = {T1: 0.7, T2: 1.0, T3: 1.3}[user_tier]
raw = base * tier_multiplier
result = clamp(round_to_nearest_5(raw), min=30, max=150)
```

Report to user:

```
Concept extraction complete:
- Concepts: {N}
- Relationships: {N}
- Trade-offs: {N}
- Recommended questions: {result} (Tier {tier})
- Override? (enter number 30-150, or press enter for {result})
```

---

## Phase 2: Subagent Spawning Procedure

**Executor:** The forked skill agent (spawns 2 Task subagents)

### Step 2.1: Calculate Counts

```
TOTAL = confirmed question count (from Phase 1)

Subagent A:
  SCENARIO_COUNT = round(TOTAL * 0.40)
  TRANSFER_COUNT = round(TOTAL * 0.20)
  COUNT_A = SCENARIO_COUNT + TRANSFER_COUNT

Subagent B:
  RELATIONSHIP_COUNT = round(TOTAL * 0.25)
  EVALUATION_COUNT = TOTAL - COUNT_A - RELATIONSHIP_COUNT  # remainder
  COUNT_B = RELATIONSHIP_COUNT + EVALUATION_COUNT

Verify: COUNT_A + COUNT_B == TOTAL
```

### Step 2.2: Prepare Variables

```
ABSOLUTE_PATH = working directory (pwd)
SLUG = chapter/part slug (from Phase 0)
```

### Step 2.3: Spawn Subagents (Parallel)

Use `references/subagent-template.md` templates. Spawn both using the Task tool simultaneously.

Key points:

- Each subagent receives ONLY the concept map + question-types.md
- Each writes to its own output file
- Both execute autonomously (no confirmation prompts)

### Step 2.4: Verify Outputs

After both subagents complete:

```
ls -la assessments/{SLUG}-questions-A.md  # Subagent A output
ls -la assessments/{SLUG}-questions-B.md  # Subagent B output

# Verify non-empty
wc -l assessments/{SLUG}-questions-A.md   # Should be substantial
wc -l assessments/{SLUG}-questions-B.md   # Should be substantial
```

---

## Phase 3: Validation Procedure

**Executor:** The forked skill agent (not a subagent)

### Step 3.1: Anti-Memorization Scan

```bash
# Check for recall patterns
grep -inE "(According to|Lesson [0-9]|the document states|as discussed in|as described in|the chapter explains|we learned that)" assessments/{SLUG}-questions-*.md
```

If matches found: record question numbers and patterns.

### Step 3.2: Structural Scan

For each question in both files:

1. Verify scenario paragraph exists (text before the "?" stem)
2. Verify stem exists (sentence ending in "?")
3. Verify 4 options (A-D) are present
4. Verify concept tag maps to concept map

### Step 3.3: Concept Mapping Verification

```
FOR each question:
  concept_tag = extract from [Concept: {name}] header
  IF concept_tag not in concept_map_concepts:
    FAIL "Q{N}: references concept '{name}' not in map"
```

### Step 3.4: Transfer Domain Verification

```
FOR each [Transfer Application] question:
  Extract domain from scenario context
  grep -ri "{domain}" {CHAPTER_PATH}/*.md
  IF matches found:
    FAIL "Q{N}: transfer domain '{domain}' appears in chapter"
```

### Step 3.5: Length Parity Check (CRITICAL)

```
FOR each question in both files:
  option_words = [wordcount(A), wordcount(B), wordcount(C), wordcount(D)]
  mean_length = mean(option_words)

  FOR each option:
    ratio = option_words[i] / mean_length
    IF ratio < 0.8 OR ratio > 1.2:
      FAIL "Q{N}: Option {letter} is {ratio:.2f}x mean ({option_words[i]} words vs {mean_length:.1f} mean)"

# Batch-level threshold
violation_count = count of questions with any length violation
IF violation_count / total > 0.15:
  FAIL "Length parity failed: {violation_count}/{total} questions have options outside 0.8x-1.2x range"
```

If violations found, remediate per `references/validation-rules.md` before proceeding.

### Step 3.6: Answer Distribution Analysis

```
# Count answers
answers_A = grep -c "Answer.*A" assessments/{SLUG}-questions-*.md
answers_B = grep -c "Answer.*B" assessments/{SLUG}-questions-*.md
answers_C = grep -c "Answer.*C" assessments/{SLUG}-questions-*.md
answers_D = grep -c "Answer.*D" assessments/{SLUG}-questions-*.md

# Check 20-30% each
total = answers_A + answers_B + answers_C + answers_D
FOR each letter:
  pct = count / total * 100
  IF pct < 20 or pct > 30: FAIL
```

### Step 3.7: Type Distribution Check

```
scenario_count = grep -c "Scenario Analysis" assessments/{SLUG}-questions-*.md
relationship_count = grep -c "Concept Relationship" assessments/{SLUG}-questions-*.md
transfer_count = grep -c "Transfer Application" assessments/{SLUG}-questions-*.md
evaluation_count = grep -c "Critical Evaluation" assessments/{SLUG}-questions-*.md

# Each should be within 15% of target
```

### Step 3.8: Produce Validation Report

See `references/validation-rules.md` for report format.

---

## Phase 4: Assembly Procedure

**Executor:** The forked skill agent (not a subagent)

### Step 4.1: Load and Merge Questions

```
1. Read assessments/{SLUG}-questions-A.md
2. Read assessments/{SLUG}-questions-B.md
3. Parse into individual question objects
4. Interleave (alternate A/B, don't group by type)
5. Renumber Q1 through Q{TOTAL}
```

### Step 4.2: Build Exam Markdown

Following the format specified in SKILL.md Phase 4 Step 2:

- Header with metadata (count, time, passing score)
- Questions section (numbered, with scenarios)
- Answer key table
- Educator metadata section

### Step 4.3: Strip Internal Tags

Remove from final output:

```
- [Scenario Analysis] tags
- [Concept Relationship] tags
- [Transfer Application] tags
- [Critical Evaluation] tags
- [Concept: {name}] tags
- **Reasoning:** sections (keep in separate educator key)
```

The student-facing exam contains ONLY: question numbers, scenarios, stems, and A/B/C/D options.
The answer key contains: question number, correct letter, type (for educator reference).

### Step 4.4: Write Final Markdown

```
Write to: assessments/{SLUG}-exam.md
```

### Step 4.5: Convert to DOCX

```bash
pandoc assessments/{SLUG}-exam.md -o assessments/{SLUG}-Assessment-Final.docx --from=markdown --to=docx
```

### Step 4.6: Post-Conversion Verification

```bash
ls -la assessments/{SLUG}-Assessment-Final.docx
# Verify exists and size > 10KB
```

### Step 4.7: Report Completion

```
Phase 4 Complete:
  - DOCX: assessments/{SLUG}-Assessment-Final.docx
  - Size: {N}KB
  - Questions: {TOTAL}
  - Concept coverage: {X}/{Y} ({Z}%)
  - Answer distribution: A={N} B={N} C={N} D={N}
  - Ready for distribution
```

---

## Error Recovery

### If Subagent Fails to Write Output

```
IF file not found after subagent completion:
  1. Report which subagent failed
  2. Re-spawn ONLY that subagent
  3. Maximum 2 retries
  4. If still failing: report to user
```

### If Validation Finds >20% Failures

```
IF failed_questions / total > 0.20:
  1. Identify which subagent produced most failures
  2. Re-spawn that subagent with failure report as additional context
  3. Re-validate
  4. Maximum 2 regeneration cycles
```

### If Distribution Is Off

```
IF answer distribution outside 20-30%:
  1. Identify over/under-represented letters
  2. Find questions where correct answer can be swapped without changing question quality
  3. Swap answer positions (move correct answer to under-represented letter)
  4. Re-verify distribution
```
