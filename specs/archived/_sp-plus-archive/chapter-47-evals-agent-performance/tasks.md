# Tasks: Chapter 47 - Evals: Measuring Agent Performance

**Generated from**: plan.md
**Created**: 2025-12-30
**Total Tasks**: 24

---

## Task Categories

| Category | Count | Description |
|----------|-------|-------------|
| Setup | 2 | Directory creation, README |
| Lessons | 11 | L00-L10 implementation |
| Validation | 4 | Quality checks |
| Documentation | 2 | Chapter README, sidebar |
| Cleanup | 5 | Issue closure, commit |

---

## Setup Tasks

### TASK-001: Create Chapter Directory Structure
**Priority**: P0 (Blocking)
**Estimated**: 5 min

**Description**: Create the chapter directory and initial structure.

**Acceptance Criteria**:
- [ ] Directory `apps/learn-app/docs/06-AI-Native-Software-Development/47-evals-agent-performance/` exists
- [ ] README.md placeholder created
- [ ] `_category_.json` created with correct position

**Command**:
```bash
mkdir -p apps/learn-app/docs/06-AI-Native-Software-Development/47-evals-agent-performance
```

---

### TASK-002: Create Chapter README
**Priority**: P0 (Blocking)
**Estimated**: 10 min

**Description**: Create chapter README with overview and lesson index.

**Acceptance Criteria**:
- [ ] README.md contains chapter overview
- [ ] Lesson index with all 11 lessons listed
- [ ] Prerequisites section
- [ ] Learning outcomes section

---

## Lesson Implementation Tasks

### TASK-003: Implement L00 - Build Your Evals Skill
**Priority**: P1 (High)
**Estimated**: 45 min
**Layer**: L3 (Skill)

**Description**: First lesson following Skill-First pattern.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
- [ ] Compelling narrative opening (2-3 paragraphs)
- [ ] Clone skills-lab instruction
- [ ] LEARNING-SPEC.md creation guide
- [ ] Skill structure creation steps
- [ ] 3 "Try With AI" prompts with explanations
- [ ] No "Reflect on Your Skill" (this is the skill creation lesson)

**Dependencies**: TASK-001, TASK-002

---

### TASK-004: Implement L01 - Evals Are Exams for Reasoning
**Priority**: P1 (High)
**Estimated**: 40 min
**Layer**: L1 (Manual/Conceptual)

**Description**: Core distinction between TDD and Evals.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] TDD vs Evals comparison table
- [ ] Andrew Ng quote with attribution
- [ ] Calculator vs student analogy
- [ ] Exercise: identify 3 behaviors to improve
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section

**Dependencies**: TASK-003

---

### TASK-005: Implement L02 - The Two Evaluation Axes
**Priority**: P1 (High)
**Estimated**: 40 min
**Layer**: L1 (Manual/Conceptual)

**Description**: Four-quadrant framework for eval classification.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Objective vs Subjective axis explanation
- [ ] Ground Truth axis explanation
- [ ] Four-quadrant table with examples
- [ ] Exercise: classify 5 eval ideas
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section

**Dependencies**: TASK-004

---

### TASK-006: Implement L03 - Designing Eval Datasets
**Priority**: P1 (High)
**Estimated**: 45 min
**Layer**: L2 (Collaboration)

**Description**: Quality over quantity approach to dataset design.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] "10-20, not 1000" emphasis
- [ ] Three categories table (typical, edge, error)
- [ ] Real data emphasis
- [ ] Eval case structure template
- [ ] Exercise: create 20-case dataset
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section

**Dependencies**: TASK-005

---

### TASK-007: Implement L04 - Building Graders with Binary Criteria
**Priority**: P1 (High)
**Estimated**: 50 min
**Layer**: L2 (Collaboration)

**Description**: Binary criteria pattern for reliable grading.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Why 1-5 scales fail explanation
- [ ] Binary criteria pattern with example
- [ ] Code-based grader implementation
- [ ] Rubric conversion exercise
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section

**Dependencies**: TASK-006

---

### TASK-008: Implement L05 - LLM-as-Judge Graders
**Priority**: P1 (High)
**Estimated**: 50 min
**Layer**: L2 (Collaboration)

**Description**: Using LLMs as evaluators with limitations.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] LLM-as-judge prompt template
- [ ] Position bias warning
- [ ] LLM grader implementation
- [ ] Exercise: compare to human judgment
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section

**Dependencies**: TASK-007

---

### TASK-009: Implement L06 - Systematic Error Analysis
**Priority**: P1 (High)
**Estimated**: 50 min
**Layer**: L2 (Collaboration)

**Description**: Spreadsheet-based error counting method.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Andrew Ng quote on analysis time
- [ ] Traces and spans explanation
- [ ] Spreadsheet template
- [ ] Prioritization formula (frequency × feasibility)
- [ ] Exercise: create error analysis
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section

**Dependencies**: TASK-008

---

### TASK-010: Implement L07 - Component vs End-to-End Evals
**Priority**: P1 (High)
**Estimated**: 45 min
**Layer**: L2 (Collaboration)

**Description**: Decision framework for eval granularity.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] E2E noise problem explanation
- [ ] Component eval benefits table
- [ ] Decision framework
- [ ] Exercise: implement component eval
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section

**Dependencies**: TASK-009

---

### TASK-011: Implement L08 - Regression Protection
**Priority**: P1 (High)
**Estimated**: 45 min
**Layer**: L2 (Collaboration)

**Description**: Eval-on-every-change workflow.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Before/after comparison pattern
- [ ] Regression detection method
- [ ] Workflow diagram
- [ ] Exercise: implement regression protection
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section

**Dependencies**: TASK-010

---

### TASK-012: Implement L09 - The Complete Quality Loop
**Priority**: P1 (High)
**Estimated**: 50 min
**Layer**: L2 (Collaboration)

**Description**: Build-Evaluate-Analyze-Improve synthesis.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Complete loop visualization
- [ ] Iteration pattern (70% → 85% → 92%)
- [ ] Practical workflow steps
- [ ] Exercise: complete one cycle
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section

**Dependencies**: TASK-011

---

### TASK-013: Implement L10 - Finalize Your Evals Skill
**Priority**: P1 (High)
**Estimated**: 40 min
**Layer**: L3 (Skill)

**Description**: Skill finalization and validation.

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Skill validation checklist
- [ ] Test on non-Task API agent
- [ ] Final documentation template
- [ ] 3 "Try With AI" prompts
- [ ] No "Reflect on Your Skill" (final skill lesson)

**Dependencies**: TASK-012

---

## Validation Tasks

### TASK-014: Run Educational Validator on All Lessons
**Priority**: P1 (High)
**Estimated**: 30 min

**Description**: Validate all lessons against educational standards.

**Acceptance Criteria**:
- [ ] All lessons pass educational-validator
- [ ] Constitution compliance verified
- [ ] YAML frontmatter complete
- [ ] Proficiency levels appropriate (B1-B2)

**Dependencies**: TASK-003 through TASK-013

---

### TASK-015: Run Factual Verifier
**Priority**: P1 (High)
**Estimated**: 30 min

**Description**: Verify all factual claims in lessons.

**Acceptance Criteria**:
- [ ] Andrew Ng quotes verified
- [ ] Methodology claims accurate
- [ ] No hallucinated statistics
- [ ] All sources properly attributed

**Dependencies**: TASK-003 through TASK-013

---

### TASK-016: Run Pedagogical Designer Check
**Priority**: P2 (Medium)
**Estimated**: 20 min

**Description**: Validate learning progression and scaffolding.

**Acceptance Criteria**:
- [ ] Concepts build appropriately
- [ ] Cognitive load managed
- [ ] Prerequisites clear
- [ ] Differentiation provided

**Dependencies**: TASK-003 through TASK-013

---

### TASK-017: Run Validation Auditor
**Priority**: P1 (High)
**Estimated**: 30 min

**Description**: Comprehensive quality assessment.

**Acceptance Criteria**:
- [ ] Technical correctness verified
- [ ] Pedagogical effectiveness confirmed
- [ ] Accessibility checked
- [ ] Final quality gate passed

**Dependencies**: TASK-014, TASK-015, TASK-016

---

## Documentation Tasks

### TASK-018: Update Chapter Index
**Priority**: P2 (Medium)
**Estimated**: 10 min

**Description**: Update specs/book/chapter-index.md with implementation status.

**Acceptance Criteria**:
- [ ] Chapter 47 marked as Implemented
- [ ] Lesson count accurate
- [ ] Student skill listed

**Dependencies**: TASK-017

---

### TASK-019: Create _category_.json
**Priority**: P2 (Medium)
**Estimated**: 5 min

**Description**: Create Docusaurus category configuration.

**Acceptance Criteria**:
- [ ] Correct position (47)
- [ ] Proper label
- [ ] Collapsible set appropriately

**Dependencies**: TASK-001

---

## Cleanup Tasks

### TASK-020: Create GitHub Issues for Each Lesson
**Priority**: P2 (Medium)
**Estimated**: 15 min

**Description**: Create tracking issues for lesson implementation.

**Acceptance Criteria**:
- [ ] 11 issues created (one per lesson)
- [ ] Labels applied
- [ ] Linked to milestone if exists

**Dependencies**: TASK-002

---

### TASK-021: Close Lesson Issues as Completed
**Priority**: P2 (Medium)
**Estimated**: 10 min

**Description**: Close issues as lessons are completed.

**Acceptance Criteria**:
- [ ] All 11 lesson issues closed
- [ ] Completion notes added

**Dependencies**: TASK-017

---

### TASK-022: Git Add and Status Check
**Priority**: P1 (High)
**Estimated**: 5 min

**Description**: Stage all new files and verify.

**Acceptance Criteria**:
- [ ] All lesson files staged
- [ ] README staged
- [ ] _category_.json staged
- [ ] No unintended files

**Dependencies**: TASK-017

---

### TASK-023: Create Commit
**Priority**: P1 (High)
**Estimated**: 5 min

**Description**: Create commit with proper message.

**Acceptance Criteria**:
- [ ] Commit message follows format
- [ ] All files included
- [ ] No secrets committed

**Dependencies**: TASK-022

---

### TASK-024: Create Pull Request (Optional)
**Priority**: P3 (Low)
**Estimated**: 10 min

**Description**: Create PR if on feature branch.

**Acceptance Criteria**:
- [ ] PR created with summary
- [ ] Test plan included
- [ ] Reviewers assigned if applicable

**Dependencies**: TASK-023

---

## Task Execution Order

```
Phase 1: Setup
  TASK-001 → TASK-002 → TASK-019 → TASK-020

Phase 2: Lessons (Sequential due to dependencies)
  TASK-003 → TASK-004 → TASK-005 → TASK-006
  → TASK-007 → TASK-008 → TASK-009 → TASK-010
  → TASK-011 → TASK-012 → TASK-013

Phase 3: Validation (Parallel where possible)
  [TASK-014, TASK-015, TASK-016] → TASK-017

Phase 4: Cleanup
  TASK-018 → TASK-021 → TASK-022 → TASK-023 → TASK-024
```

---

## Progress Tracking

| Task | Status | Completed |
|------|--------|-----------|
| TASK-001 | Pending | |
| TASK-002 | Pending | |
| TASK-003 | Pending | |
| TASK-004 | Pending | |
| TASK-005 | Pending | |
| TASK-006 | Pending | |
| TASK-007 | Pending | |
| TASK-008 | Pending | |
| TASK-009 | Pending | |
| TASK-010 | Pending | |
| TASK-011 | Pending | |
| TASK-012 | Pending | |
| TASK-013 | Pending | |
| TASK-014 | Pending | |
| TASK-015 | Pending | |
| TASK-016 | Pending | |
| TASK-017 | Pending | |
| TASK-018 | Pending | |
| TASK-019 | Pending | |
| TASK-020 | Pending | |
| TASK-021 | Pending | |
| TASK-022 | Pending | |
| TASK-023 | Pending | |
| TASK-024 | Pending | |
