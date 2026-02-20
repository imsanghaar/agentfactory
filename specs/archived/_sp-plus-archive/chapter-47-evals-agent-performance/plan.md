# Implementation Plan: Chapter 47 - Evals: Measuring Agent Performance

**Based on**: spec.md and clarifications.md
**Created**: 2025-12-30
**Target**: 11 lessons (L00-L10)

---

## Implementation Strategy

### Approach
This is a **conceptual chapter** teaching evaluation THINKING, not specific tooling. The implementation focuses on:
1. Clear analogies and frameworks (exams for reasoning, four quadrants)
2. Practical exercises with Task API agent running example
3. Skill-First pattern with `agent-evals` skill development
4. Framework-agnostic patterns that apply to any SDK

### Quality Reference
All lessons will follow the format of `01-the-2025-inflection-point.md`:
- Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
- Compelling narrative opening (2-3 paragraphs before first section)
- Tables for comparisons
- 3 "Try With AI" prompts with "What you're learning" explanations
- Safety notes where appropriate

---

## Lesson Implementation Order

### Phase 1: Foundational Concepts (L00-L03)

#### L00: Build Your Evals Skill
**Priority**: FIRST (Skill-First pattern)
**Duration**: 25 min
**Layer**: L3 (Skill)

**Content Outline**:
1. Opening: Why evals require systematic thinking (not guessing)
2. Clone skills-lab fresh
3. Write LEARNING-SPEC.md for eval methodology
4. Fetch eval documentation patterns
5. Create initial `agent-evals` skill structure
6. Verify skill works with basic eval generation

**Key Deliverables**:
- Student creates `agent-evals` skill directory
- Skill includes Andrew Ng methodology reference
- Skill can generate basic eval case structure

**Dependencies**: None (first lesson)

---

#### L01: Evals Are Exams for Reasoning
**Priority**: HIGH (foundational concept)
**Duration**: 20 min
**Layer**: L1 (Manual/Conceptual)

**Content Outline**:
1. Opening: The difference between testing code and testing reasoning
2. TDD vs Evals comparison table
3. Andrew Ng quote: disciplined evaluation process
4. The calculator vs student analogy
5. Identifying behaviors to improve in Task API agent
6. Reflect on Your Skill

**Key Deliverables**:
- Student understands TDD ≠ Evals distinction
- Student can identify 3 behaviors to improve in any agent
- Comparison table: TDD vs Evals

**Dependencies**: L00 completed

---

#### L02: The Two Evaluation Axes
**Priority**: HIGH (framework for classification)
**Duration**: 20 min
**Layer**: L1 (Manual/Conceptual)

**Content Outline**:
1. Opening: Not all evals are the same
2. Axis 1: Objective (code-checkable) vs Subjective (LLM-judged)
3. Axis 2: Per-example ground truth vs No ground truth
4. Four-quadrant diagram with examples
5. Exercise: Classify 5 Task API eval ideas
6. Reflect on Your Skill

**Key Deliverables**:
- Four-quadrant framework internalized
- Student can classify any eval into quadrant
- Skill updated with classification patterns

**Dependencies**: L01 completed

---

#### L03: Designing Eval Datasets
**Priority**: HIGH (practical foundation)
**Duration**: 25 min
**Layer**: L2 (Collaboration)

**Content Outline**:
1. Opening: Quality over quantity (10-20, not 1000)
2. Three categories: typical, edge, error cases
3. Using REAL data from production/user queries
4. Eval case structure: input, expected, rationale
5. Exercise: Create 20-case dataset for Task API agent
6. Reflect on Your Skill

**Key Deliverables**:
- Student creates 20-case eval dataset
- Dataset includes all three categories
- Skill updated with dataset design patterns

**Dependencies**: L02 completed

---

### Phase 2: Building Graders (L04-L05)

#### L04: Building Graders with Binary Criteria
**Priority**: HIGH (key methodology insight)
**Duration**: 30 min
**Layer**: L2 (Collaboration)

**Content Outline**:
1. Opening: Why LLMs can't do 1-5 scales reliably
2. The binary criteria pattern: 5 yes/no → 0-5 score
3. Converting subjective rubrics to binary criteria
4. Implementing code-based graders for objective criteria
5. Exercise: Create grader for Task API output structure
6. Reflect on Your Skill

**Key Deliverables**:
- Student converts 1-5 rubric to binary criteria
- Student implements code-based grader
- Skill updated with grader templates

**Dependencies**: L03 completed

---

#### L05: LLM-as-Judge Graders
**Priority**: MEDIUM (builds on L04)
**Duration**: 30 min
**Layer**: L2 (Collaboration)

**Content Outline**:
1. Opening: When code can't judge quality
2. LLM-as-judge prompt structure
3. Position bias warning (avoid pairwise comparisons)
4. Implementing LLM grader with binary criteria
5. Exercise: Compare LLM grader to human judgment
6. Reflect on Your Skill

**Key Deliverables**:
- Student implements LLM-as-judge grader
- Student understands position bias limitation
- Skill updated with LLM grader templates

**Dependencies**: L04 completed

---

### Phase 3: Analysis & Improvement (L06-L09)

#### L06: Systematic Error Analysis
**Priority**: HIGH (key methodology insight)
**Duration**: 30 min
**Layer**: L2 (Collaboration)

**Content Outline**:
1. Opening: Andrew Ng quote on analysis time
2. Traces (full output) and spans (single step)
3. Spreadsheet-based error counting method
4. Prioritization: frequency × feasibility
5. Exercise: Create error analysis for Task API failures
6. Reflect on Your Skill

**Key Deliverables**:
- Student creates error analysis spreadsheet
- Student identifies highest-error component
- Skill updated with error analysis patterns

**Dependencies**: L05 completed

---

#### L07: Component vs End-to-End Evals
**Priority**: MEDIUM (decision framework)
**Duration**: 25 min
**Layer**: L2 (Collaboration)

**Content Outline**:
1. Opening: Why E2E evals are noisy
2. Benefits of component evals: signal, speed, isolation
3. Decision framework: when to use each
4. Exercise: Create component-level eval for Task API routing
5. Compare results with E2E eval
6. Reflect on Your Skill

**Key Deliverables**:
- Student implements component-level eval
- Student understands signal vs noise tradeoff
- Skill updated with decision framework

**Dependencies**: L06 completed

---

#### L08: Regression Protection
**Priority**: MEDIUM (operational workflow)
**Duration**: 25 min
**Layer**: L2 (Collaboration)

**Content Outline**:
1. Opening: Improvements that break other things
2. Eval-on-every-change workflow
3. Before/after comparison pattern
4. Detecting regressions via score comparison
5. Exercise: Implement regression protection
6. Reflect on Your Skill

**Key Deliverables**:
- Student implements regression protection workflow
- Student can detect regression via comparison
- Skill updated with regression patterns

**Dependencies**: L07 completed

---

#### L09: The Complete Quality Loop
**Priority**: HIGH (synthesis)
**Duration**: 30 min
**Layer**: L2 (Collaboration)

**Content Outline**:
1. Opening: Build-Evaluate-Analyze-Improve loop
2. The iteration pattern: 70% → 85% → 92%
3. Practical workflow visualization
4. Exercise: Complete one full improvement cycle
5. Document improvement journey
6. Reflect on Your Skill

**Key Deliverables**:
- Student completes full improvement cycle
- Student documents progress (baseline → improved)
- Skill updated with complete loop pattern

**Dependencies**: L08 completed

---

### Phase 4: Skill Finalization (L10)

#### L10: Finalize Your Evals Skill
**Priority**: HIGH (skill completion)
**Duration**: 20 min
**Layer**: L3 (Skill)

**Content Outline**:
1. Opening: From learning to asset
2. Validate skill helps with eval design
3. Validate skill helps with grader creation
4. Validate skill helps with error analysis
5. Test on a DIFFERENT agent (not Task API)
6. Final skill documentation

**Key Deliverables**:
- Student's skill works on non-Task API agent
- Skill is production-ready
- Student has sellable asset

**Dependencies**: L00-L09 completed

---

## Implementation Notes

### Common Elements Across All Lessons

1. **YAML Frontmatter**: Full structure with skills, learning_objectives, cognitive_load, differentiation
2. **Narrative Opening**: 2-3 paragraphs connecting to real-world relevance
3. **Tables**: Use for comparisons (TDD vs Evals, Component vs E2E)
4. **Try With AI**: 3 prompts per lesson with "What you're learning" explanations
5. **Reflect on Your Skill**: 3-5 sentences at lesson end (except L00, L10)

### Running Example: Task API Agent

All exercises use the Task API agent with these eval scenarios:
- **Routing**: create vs update vs query intent classification
- **Tool Selection**: correct tool calls for given intent
- **Output Format**: proper JSON structure in responses
- **Error Handling**: graceful handling of invalid inputs

### Framework-Agnostic Code

All code examples use generic Python patterns:
```python
# Generic pattern - works with any SDK
def evaluate_agent(agent, eval_case):
    """Run agent and evaluate response."""
    response = agent.run(eval_case["input"])
    score = grader(response, eval_case["expected"])
    return {"case": eval_case["name"], "score": score}
```

### Quality Validation

Before marking lessons complete:
1. Run educational-validator on each lesson
2. Verify factual claims with WebSearch
3. Check YAML frontmatter completeness
4. Verify 3 "Try With AI" prompts exist
5. Verify "Reflect on Your Skill" section exists

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Lessons too abstract | Include concrete Task API examples in every lesson |
| SDK-specific code creep | Use generic function signatures, add "works with any SDK" notes |
| Missing skill reflection | Template checklist before finalizing each lesson |
| Inconsistent quality | Compare each lesson to quality reference before completion |

---

## Estimated Timeline

| Phase | Lessons | Estimated Duration |
|-------|---------|-------------------|
| Phase 1 | L00-L03 | ~2 hours |
| Phase 2 | L04-L05 | ~1.5 hours |
| Phase 3 | L06-L09 | ~2 hours |
| Phase 4 | L10 | ~30 min |
| Validation | All | ~1 hour |
| **Total** | 11 lessons | ~7 hours |
