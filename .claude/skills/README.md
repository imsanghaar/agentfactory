# Skill Coordination Guide

## Overview

This guide resolves collisions between related skills and provides clear decision trees for skill selection.

**14 Active Skills** organized by domain with clear triggers and interactions.

---

## CRITICAL COLLISION RESOLUTION

### 1. Content Quality Assessment: TWO TOOLS, DIFFERENT PURPOSES

**Skills**: `chapter-evaluator` + `content-evaluation-framework`

| Aspect | chapter-evaluator | content-evaluation-framework |
|--------|------------------|------------------------------|
| **Purpose** | Diagnose specific problems | Gate decision (pass/fail) |
| **When** | During development (find issues) | Before publication (go/no-go) |
| **Output** | Detailed findings + improvement recommendations | Weighted score (75%+ = pass) |
| **User** | Authors (improving content) | Reviewers (publication gate) |

**CORRECT WORKFLOW**:
```
Author develops lesson
  ↓
Author runs chapter-evaluator → "What's wrong with this?"
  ↓
Author identifies issues + uses remediation skills:
  - Low Clarity? → Use technical-clarity
  - Low Engagement? → Use code-example-generator
  - Low Scaffolding? → Use concept-scaffolding
  ↓
Author revises content
  ↓
Reviewer runs content-evaluation-framework → "Is this 75%+?"
  ↓
PASS → Publish | FAIL → Return to author with chapter-evaluator
```

**DO NOT**:
- Use chapter-evaluator as final gate (it's diagnostic, not pass/fail)
- Use content-evaluation-framework during development (doesn't identify what's wrong)
- Ask "which one?" — use BOTH in sequence

---

### 2. Teaching AI Collaboration: DESIGN FIRST, THEN CODE

**Skills**: `ai-collaborate-teaching` + `code-example-generator`

| Aspect | ai-collaborate-teaching | code-example-generator |
|--------|------------------------|------------------------|
| **Purpose** | Design lesson balance | Generate specific examples |
| **Scope** | Whole lesson structure | Individual code examples |
| **Question** | "How should this lesson mix foundation/AI/verification?" | "What code example demonstrates this concept?" |
| **Output** | 40/40/20 balance plan | Runnable code with validation |

**CORRECT WORKFLOW**:
```
Lesson concept defined
  ↓
Use ai-collaborate-teaching → "Design the lesson balance"
  ↓
Lesson should be 40% foundation + 40% AI + 20% verification
  ↓
For EACH section needing code:
  Use code-example-generator → Generate specific examples
  (Examples must follow Spec→Prompt→Code→Validation)
  ↓
Assemble lesson with code examples fitting the 40/40/20 structure
```

**DO NOT**:
- Skip ai-collaborate-teaching and jump to code examples (no balance)
- Use code-example-generator randomly (examples must fit lesson design)

---

### 3. Learning Design: OBJECTIVES → SCAFFOLDING → CLARITY

**Skills**: `learning-objectives` + `concept-scaffolding` + `technical-clarity`

| Skill | Question | Output | When |
|-------|----------|--------|------|
| learning-objectives | "What will students DO?" | SMART outcomes + Bloom's levels + assessments | PLAN (first) |
| concept-scaffolding | "How will students LEARN it?" | 3-7 step progression + cognitive load limits | DESIGN (second) |
| technical-clarity | "Is this clear to read?" | Prose refinement + jargon checks | POLISH (third) |

**CORRECT WORKFLOW**:
```
Step 1: Define learning objectives
  → What outcomes? (Bloom's Create level)
  → What proficiency? (CEFR B1)
  → How to assess? (Concrete evals)
  → Output: learning_objectives.md

Step 2: Design progression to reach objectives
  → How many steps? (3-7)
  → Concepts per step? (B1 = 3-5)
  → Validation checkpoints?
  → Output: scaffolding_plan.md

Step 3: Write lesson content following scaffolding
  → Use code-example-generator for worked examples
  → Use ai-collaborate-teaching for 40/40/20 balance
  → Output: lesson.md (draft)

Step 4: Polish clarity
  → Run technical-clarity skill
  → Fix: gatekeeping language, jargon, accessibility
  → Output: lesson.md (final)

Step 5: Verify against outcomes
  → Use chapter-evaluator
  → All objectives measurable? Learning outcomes clear?
  → Output: evaluation report
```

**DO NOT**:
- Write lesson first, define objectives after (backwards)
- Skip scaffolding design (jump straight to writing)
- Polish prose before content is solid (wrong priority)

---

## SKILL SELECTION MATRIX

### By Task: "I need to..."

#### ✏️ PLAN & DESIGN

**"Define what students will learn"**
→ Use `learning-objectives`

**"Design the progression to teach a concept"**
→ Use `concept-scaffolding`

**"Balance a lesson between foundation/AI/verification"**
→ Use `ai-collaborate-teaching`

#### 🛠️ IMPLEMENT & CREATE

**"Generate a working code example"**
→ Use `code-example-generator`

**"Generate a full PhD-level exam from notes"**
→ Use `mit-exam-generator`

**"Generate a lesson summary for quick review"**
→ Use `summary-generator`

**"Create a production skill from scratch"**
→ Use `skill-creator-pro`

**"Create platform skills/agents/specs correctly"**
→ Use `canonical-format-checker`

#### 🔍 REVIEW & EVALUATE

**"Diagnose problems in a chapter (detailed analysis)"**
→ Use `chapter-evaluator`

**"Gate a chapter for publication (yes/no)"**
→ Use `content-evaluation-framework`

**"Check technical prose for accessibility"**
→ Use `technical-clarity`

**"Validate a skill meets production standards"**
→ Use `skill-validator`

#### 🔧 FIX & IMPROVE

**"Fix Gate 4 failures (word count/continuity)"**
→ Use `content-refiner`

**"Map skill proficiency to CEFR levels"**
→ Use `skills-proficiency-mapper`

---

## DOMAIN ORGANIZATION

### 1. PEDAGOGICAL DESIGN (Objectives + Progression)

**Core**: `learning-objectives` → `concept-scaffolding`
- **learning-objectives**: WHAT will students achieve
- **concept-scaffolding**: HOW they'll learn it
- **Support**: `technical-clarity` (polish), `ai-collaborate-teaching` (balance)

### 2. CONTENT CREATION (Write + Generate)

**Core**: `code-example-generator` + `ai-collaborate-teaching`
- **code-example-generator**: Create specific examples
- **ai-collaborate-teaching**: Design lesson structure
- **Support**: `mit-exam-generator` (assessments), `summary-generator` (review)

### 3. QUALITY GATES (Diagnose + Gate + Validate)

**Diagnostic**: `chapter-evaluator` (find issues)
**Gate**: `content-evaluation-framework` (publish decision)
**Support**: `technical-clarity` (fix prose), `content-refiner` (fix structure)

### 4. PLATFORM STANDARDS (Skills + Specs + Patterns)

**Creation**: `skill-creator-pro`
**Validation**: `skill-validator`, `canonical-format-checker`
**Support**: `skills-proficiency-mapper`

---

## COMMON WORKFLOWS

### Workflow 1: Create a New Lesson

```
1. Define objectives → learning-objectives
2. Design progression → concept-scaffolding
3. Generate examples → code-example-generator
4. Design lesson balance → ai-collaborate-teaching
5. Write content following scaffolding
6. Polish prose → technical-clarity
7. Diagnose problems → chapter-evaluator
8. Fix issues using remediation skills
9. Gate for publication → content-evaluation-framework
10. PUBLISH
```

**Time**: ~8-12 hours (depends on complexity)

---

### Workflow 2: Review Existing Chapter

```
1. Run chapter-evaluator → Get detailed analysis
2. For each low-scoring dimension:
   - Low Clarity? → Fix with technical-clarity
   - Low Engagement? → Use code-example-generator for better examples
   - Low Scaffolding? → Redesign with concept-scaffolding
   - Low Objectives? → Clarify with learning-objectives
3. Re-run chapter-evaluator
4. Submit to content-evaluation-framework
5. If PASS → Publish | If FAIL → Repeat steps 2-3
```

**Time**: ~4-6 hours (revision depends on issues found)

---

### Workflow 3: Create a Production Skill

```
1. Determine skill type (Builder/Guide/Automation/Analyzer/Validator)
2. Run skill-creator-pro → Get domain expertise + structure
3. Implement skill + bundled resources
4. Run skill-validator → Check quality (9-category scoring)
5. Fix any failures identified
6. Re-validate
7. Deploy to production
```

**Time**: ~6-10 hours (depends on domain complexity)

---

### Workflow 4: Fix Gate 4 Failure

```
1. Understand what Gate 4 failure means (word count? continuity? both?)
2. Run content-refiner → Diagnose + fix in phases
3. Phase 1: Fix continuity (if needed)
4. Phase 2: Fix word count (layer-aware)
5. Phase 3: Validate (run checks)
6. Re-submit to Gate 4
7. If still failing → Understand why and address root cause
```

**Time**: ~1-2 hours

---

## NO-COLLISION SKILLS

These skills have clear, non-overlapping purposes:

- **summary-generator**: Extract key concepts from lessons (unique)
- **mit-exam-generator**: Generate rigorous exams (specialized, no overlap)
- **skill-creator-pro**: Create production skills (unique domain)
- **skill-validator**: Validate skills (complements skill-creator-pro)
- **canonical-format-checker**: Prevent format drift (specialized niche)
- **skills-proficiency-mapper**: Map proficiency levels (unique function)

---

## QUICK DECISION TREE

```
User asks: "Help me with [task]"

Is it about lesson content?
  ├─ YES
  │   ├─ Define learning outcomes? → learning-objectives
  │   ├─ Design progression? → concept-scaffolding
  │   ├─ Generate code example? → code-example-generator
  │   ├─ Balance lesson structure? → ai-collaborate-teaching
  │   ├─ Fix prose clarity? → technical-clarity
  │   ├─ Diagnose problems? → chapter-evaluator
  │   ├─ Gate for publication? → content-evaluation-framework
  │   ├─ Fix Gate 4 failure? → content-refiner
  │   └─ Create lesson summary? → summary-generator
  │
  └─ NO, it's about something else
    ├─ Exams/assessments? → mit-exam-generator
    ├─ Creating a skill? → skill-creator-pro
    ├─ Validating a skill? → skill-validator
    ├─ Teaching platform patterns? → canonical-format-checker
    ├─ Mapping skill proficiency? → skills-proficiency-mapper
    ├─ Teaching AI collaboration patterns? → ai-collaborate-teaching
    └─ Teaching foundational concepts in general? → concept-scaffolding
```

---

## VERSION NOTES

- **Report Date**: January 16, 2026
- **Skills Evaluated**: 14 (removed: creating-skills, operational-excellence)
- **Critical Fixes Applied**:
  1. ✅ content-refiner: Added failure diagnosis logic + phase-based approach
  2. ✅ chapter-evaluator: Added weighting + publication gate decision logic
  3. ✅ concept-scaffolding: Added YAML frontmatter + comparison to learning-objectives
- **Collision Resolutions**: 3 major (addressed above)
- **Status**: **PRODUCTION-READY** (all skills vetted)

---

## FEEDBACK & UPDATES

If skills change or new collisions emerge:
1. Update the relevant workflow section above
2. Update the decision tree
3. Test the workflow with a real task
4. Document the change in VERSION NOTES

**Last Updated**: January 16, 2026
