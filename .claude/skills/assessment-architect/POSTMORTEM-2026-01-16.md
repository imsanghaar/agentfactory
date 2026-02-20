# Assessment-Architect Skill: Critical Quality Issues & Improvement Plan

**Date:** January 16, 2026  
**Chapter:** 5 (Claude Code Features and Workflows)  
**Status:** Quality validation FAILED - identified 7 critical issues

---

## Executive Summary

Generated a 100-question assessment that passed structural validation but **failed conceptual and psychometric validation**. Root cause: subagents did not read reference materials before generation, resulting in placeholder answers and lesson-centric (not concept-centric) questions.

---

## CRITICAL ISSUES IDENTIFIED

### Issue 1: Answer Key Position Bias (SEVERITY: CRITICAL)
**Problem:** 74% of answers are "A", creating statistically impossible distribution
- Precision_Recall: Mixed (acceptable)
- Conceptual_Distinction: **100% A** (Q16-Q35 all A) ❌
- Critical_Evaluation: **95% B** (Q36-Q55) ❌
- Architecture_Analysis: **100% A** (Q56-Q75 all A) ❌
- Decision_Matrix: **100% A** (Q76-Q100 all A) ❌

**Root Cause:** Answer keys are placeholders/templates, not derived from questions  
**Expected Distribution:** ~25 of each (A/B/C/D)  
**Actual Distribution:** A=74, B=23, C=3, D=0

**Impact:** Assessment is unusable - answer key is invalid  
**Fix Required:** Regenerate with validated answer keys grounded in lesson content

---

### Issue 2: Missing Lesson Coverage (SEVERITY: HIGH)
**Problem:** 2 lessons completely excluded from assessment
- Chapter 5 has **17 content lessons**, not 15
- Missing: Lesson 16 (creator-workflow), Lesson 17 (from-skills-to-business)
- Coverage gap: ~12% of chapter content untested

**Actual Lesson Inventory:**
1. origin-story
2. installation-and-authentication
3. free-claude-setup
4. hello-world-basics
5. claude-md-context-files
6. teach-claude-your-way
7. concept-behind-skills
8. agent-skills
9. mcp-integration
10. compiling-mcp-to-skills
11. subagents-and-orchestration
12. settings-hierarchy
13. hooks-and-extensibility
14. plugins-putting-it-all-together
15. ralph-wiggum-loop
16. **creator-workflow** ← MISSING
17. **from-skills-to-business** ← MISSING

**Impact:** Assessment doesn't cover full chapter scope  
**Fix Required:** Include questions testing concepts from all 17 lessons

---

### Issue 3: Lesson Citations vs. Concept Testing (SEVERITY: HIGH)
**Problem:** Questions test "what does Lesson X say" rather than conceptual understanding
**Examples of Current (Poor) Questions:**
- "In the origin story of Claude Code, what key discovery..." (factual recall)
- "According to Lesson 1, what is the OODA Loop..." (lesson trivia)
- "What adoption metric did Claude Code achieve... according to Lesson 1?" (statistic recall)
- "What does CLAUDE.md provide according to Lesson 5?" (definition recall)

**Examples of Desired (Concept-Focused) Questions:**
- "CLAUDE.md and .claude/settings.json both provide configuration. Which statement best captures their architectural difference?"
- "A developer must decide whether to encode team standards in CLAUDE.md (git-checked) or .claude/settings.json (user-local). What is the primary trade-off?"
- "The concept of 'persistent project context' appears in CLAUDE.md. Which other features in Claude Code also address context persistence?"
- "How does the three-level skill loading architecture (metadata→instructions→files) minimize token usage compared to loading all skill content upfront?"

**Impact:** Assessment tests trivia, not mastery  
**Fix Required:** Reframe all questions to test concepts and relationships, not lesson facts

---

### Issue 4: Subagents Didn't Read Reference Files (SEVERITY: CRITICAL)
**Problem:** SKILL.md mandates:
```
SUBAGENT MUST:
  1. Read SKILL.md completely (this file)
  2. Read all 4 reference docs in order (Bloom → Psychometric → Distractor → Rigor)
  3. Read all source lessons from {CHAPTER_PATH}
```

But subagent outputs show **no evidence** of reading references:
- Distractor strategies not evident (should see diverse misconception patterns)
- Psychometric understanding minimal (answer keys are invalid)
- Question grounding shows only lesson names, not conceptual depth

**Evidence:** 
- Answer key bias (indicates template generation)
- Heavy lesson citations (indicates surface-level content reading)
- No trade-off analysis in questions (indicates didn't read psychometric standards)

**Impact:** Quality validation gates failed  
**Fix Required:** Make reference reading MANDATORY and VERIFIABLE by subagents

---

### Issue 5: No User Input Upfront (SEVERITY: MEDIUM)
**Problem:** Assessment parameters (title, question count, difficulty, time limit) hardcoded, not negotiated with user

**Current:** Automatically generate 100 questions, 150 min, T2 Intermediate  
**Desired:** Ask user first:
- Question count (50/75/100/custom)
- Assessment title
- Difficulty tier (T1/T2/mixed)
- Time limit preference

**Impact:** Inflexible workflow, can't adapt to user needs  
**Fix Required:** Add user input phase before subagent spawning

---

### Issue 6: Internal Planning Headers in Output (SEVERITY: MEDIUM)
**Problem:** Final quiz shows internal planning structure
```
# Questions 1-15: Precision_Recall
# Questions 16-35: Conceptual_Distinction
...
```

Users don't need to know these are internal type categories.

**Current:** Users see planning artifact  
**Desired:** Final output shows only question headers, question content, answer key

**Impact:** Unprofessional output, confuses users about question types  
**Fix Required:** Remove internal headers from final DOCX output

---

### Issue 7: No Validation Between Phases (SEVERITY: MEDIUM)
**Problem:** Phase 5 validation only checks file existence/size, not content quality

**Current:** 
- ✓ Validates file exists
- ✓ Validates file size >5KB
- ✓ Validates question count
- ❌ Does NOT validate answer key sanity
- ❌ Does NOT validate answer position distribution
- ❌ Does NOT sample-check answers match questions

**Desired:** Add content quality gates:
- Answer position distribution within 15-35 per choice
- Sample 10 random answers, verify they match question content
- Flag any section with >70% same answer

**Impact:** Invalid assessments pass validation  
**Fix Required:** Add psychometric validation gates to Phase 5

---

## ROOT CAUSE ANALYSIS

**Why did assessment generation fail?**

1. **Subagents treated instructions as suggestions**: SKILL.md says "MUST read reference files" but subagents appear to have skipped them
2. **No verification of prerequisite reading**: No check that subagents actually read context before generating
3. **Template-based generation**: Subagents appear to have used question templates with placeholder answers
4. **Scope definition incomplete**: Chapter inventory not fully audited before phase 1
5. **Validation gates insufficient**: Phase 5 only checked structure, not content quality
6. **No feedback loop**: Generated assessment accepted despite obvious answer key bias

---

## IMPROVEMENT ROADMAP

### Phase A: Governance & Verification
- [ ] Add mandatory "context reading checkpoint" in Phase 4
- [ ] Require subagents to summarize key concepts from EACH reference file
- [ ] Create verification prompt: "List 3 distractor strategies used in your questions"
- [ ] Create verification prompt: "Explain the DIF/DIS targets for T2 Intermediate"

### Phase B: User Interaction
- [ ] Add AskUserQuestion before Phase 1 for:
  - Quiz title/description
  - Question count (50/75/100/custom)
  - Difficulty tier
  - Time limit
  - Target audience
- [ ] Display captured parameters to user for confirmation
- [ ] Adapt distribution strategy to user question count

### Phase C: Content Quality
- [ ] Audit full lesson inventory in Phase 1 (verify all 17 lessons discovered)
- [ ] Change question focus: CONCEPTS > Lesson facts
  - Reframe prompts to ask about relationships, trade-offs, patterns
  - Reduce explicit lesson citations
  - Increase scenario-based and comparative questions
- [ ] Create concept map showing which lessons address each concept
- [ ] Distribute questions across ALL lessons (not just first 15)

### Phase D: Enhanced Validation (Phase 5)
- [ ] Add answer key psychometric checks:
  - Position distribution (expect 20-30 per choice for 100Q)
  - Flag sections with >70% same answer as FAIL
  - Sample-verify 10 random Q-A pairs match content
- [ ] Add content quality checks:
  - Grep for excessive lesson citations
  - Flag questions that read like lesson trivia
  - Check for diversity in question stems (avoid repetition)
- [ ] Add coverage verification:
  - Verify questions exist for each lesson
  - Flag lessons with <2 questions

### Phase E: Output Quality
- [ ] Remove internal type headers from final output (Precision_Recall, etc.)
- [ ] Display only: Question #, Question stem, A/B/C/D, Answer key
- [ ] Add metadata section (not visible to test-taker):
  - Cognitive level distribution
  - Lesson coverage map
  - Psychometric metrics

### Phase F: Iterative Improvement
- [ ] Create "Regenerate" option if Phase 5 validation fails
- [ ] Allow user to re-run specific sections (e.g., "regenerate Q16-Q35")
- [ ] Create feedback loop for answer key review before finalizing

---

## SUCCESS CRITERIA FOR NEXT ITERATION

- [ ] Answer key distribution: All 4 choices within 20-30 occurrences
- [ ] Lesson coverage: All 17 lessons referenced in at least 2-3 questions
- [ ] Concept focus: <20% of questions cite lesson names explicitly
- [ ] Question diversity: Stems don't repeat patterns (not all "According to Lesson X...")
- [ ] Subagent compliance: Subagents provide summary of reference materials read
- [ ] Validation gates: Phase 5 rejects assessment if position bias >60%
- [ ] User input: Quiz parameters captured and confirmed before generation
- [ ] Output quality: Final DOCX contains no internal planning headers

---

## IMPLEMENTATION PRIORITY

**HIGH (Must fix before next session):**
1. Answer key validation in Phase 5
2. Subagent prerequisite reading verification
3. Lesson inventory audit (all 17 lessons)
4. Concept-focused question reframing
5. User input phase addition

**MEDIUM (Should fix):**
6. Remove internal headers from output
7. Coverage verification in Phase 5
8. Question diversity analysis

**LOW (Nice to have):**
9. Regenerate capability
10. Feedback loop for answer key review

---

## LESSON LEARNED: "Parallelization Requires Visible Coordination"

The original principle was "Parallelization requires coordination. Coordination requires explicit protocols."

We had **explicit protocols** in SKILL.md, but **no verification** that protocols were followed. Five parallel subagents all failed to:
1. Read mandatory reference files
2. Generate valid answer keys
3. Cover missing lessons

**New principle:** "Parallelization requires verifiable coordination with visibility gates."

Next iteration must include:
- Verification checkpoints (subagent summaries of what they read)
- Content quality gates that reject invalid output
- Coverage audits that catch missing lessons
- User feedback loops that surface issues before DOCX delivery

---

