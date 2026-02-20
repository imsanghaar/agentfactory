# Chapter Specification: Chapter 47 - Evals: Measuring Agent Performance

**Part**: 6 (AI Native Software Development)
**Chapter**: 47
**Created**: 2025-12-30
**Status**: Draft
**Proficiency Level**: B1-B2 (Intermediate to Upper Intermediate)
**Prerequisites**: Chapter 34-36 (SDK chapters), Chapter 46 (TDD for Agents)

## Chapter Overview

This chapter teaches the **thinking and methodology** behind agent evaluations (evals)—the systematic approach to measuring AI agent reasoning quality. Unlike TDD (Chapter 46) which tests code correctness with deterministic PASS/FAIL outcomes, evals measure probabilistic reasoning quality with scores.

**Core Thesis** (Andrew Ng): *"One of the biggest predictors for whether someone is able to build agentic workflows really well is whether or not they're able to drive a really disciplined evaluation process."*

**Running Example**: Task API agent (from Ch40) evaluated for routing decisions, tool selection, and output quality

**Student Skill**: `agent-evals` (built in L00, extended throughout chapter)

**Lesson Count**: 11 lessons (L00-L10) covering eval concepts, graders, error analysis, and production workflows

**Key Distinction**:
| Aspect | TDD (Ch46) | Evals (Ch47) |
|--------|-----------|--------------|
| Tests | Does function return correct output? | Did agent make the right decision? |
| Outcome | PASS or FAIL (deterministic) | Scores (probabilistic) |
| Example | "Does get_weather() return valid JSON?" | "Did agent correctly interpret user intent?" |
| Analogy | Testing if calculator works | Testing if student knows WHEN to use multiplication |

---

## Assumed Knowledge

**What students know BEFORE this chapter** (from Prerequisites):
- SDK usage: OpenAI Agents SDK, Google ADK, Claude Agent SDK (Ch34-36)
- Agent architecture: tools, system prompts, routing, handoffs
- TDD concepts: tests, assertions, pytest, mocking (Ch46)
- Running example: Task API agent with create/update/query capabilities
- Basic Python testing patterns

**What this chapter must explain from scratch**:
- Evals as "exams for agent reasoning" (not code tests)
- The two evaluation axes: Objective/Subjective × Ground Truth availability
- Graders: automated quality checks with binary criteria (not 1-5 scales)
- Error analysis: systematic counting of failure patterns
- Component-level vs End-to-end evaluations
- LLM-as-judge pattern and its limitations (position bias)
- Regression protection: running evals on every change
- The Build-Evaluate-Analyze-Improve loop

---

## Learning Outcomes

By the end of this chapter, students will be able to:

1. **Distinguish** evals from traditional tests (TDD) based on determinism and outcome types
2. **Design** evaluation datasets with typical, edge, and error cases (10-20 quality cases)
3. **Create** graders using binary criteria (not 1-5 scales) for reliable assessment
4. **Implement** LLM-as-judge graders with proper prompt structure
5. **Perform** systematic error analysis using spreadsheets to count failure patterns
6. **Decide** when to use end-to-end vs component-level evaluations
7. **Build** regression protection by running evals on every agent change
8. **Apply** the Build-Evaluate-Analyze-Improve loop to improve agent quality
9. **Extend** their `agent-evals` skill with patterns from each lesson

---

## User Scenarios & Testing (Learner Journeys)

### Learner Journey 1 - Build First Eval Dataset (Priority: P1)

A student learning to create their first evaluation dataset for the Task API agent, understanding what makes a good eval case.

**Why this priority**: Dataset design is foundational. Without good test cases, all other eval work is meaningless.

**Independent Test**: Student can create a 20-case eval dataset covering typical, edge, and error scenarios for Task API agent.

**Acceptance Scenarios**:

1. **Given** a student with SDK knowledge, **When** they examine Task API agent outputs manually, **Then** they can identify 3-5 behaviors that need improvement.

2. **Given** identified improvement areas, **When** student creates eval cases, **Then** each case has clear input, expected behavior, and rationale for inclusion.

3. **Given** an eval dataset, **When** student runs agent against it, **Then** they can calculate a baseline pass rate (e.g., 70%).

---

### Learner Journey 2 - Create Binary-Criteria Graders (Priority: P1)

A student learning to build graders that use binary yes/no criteria instead of unreliable 1-5 scales.

**Why this priority**: Graders define "good" automatically. The binary criteria pattern is the key insight from Andrew Ng's methodology.

**Independent Test**: Student can create a grader with 5 binary criteria that produces consistent scores.

**Acceptance Scenarios**:

1. **Given** understanding of why 1-5 scales are unreliable, **When** student converts a subjective quality rubric to binary criteria, **Then** grader produces repeatable scores.

2. **Given** a binary grader, **When** student runs it on 10 agent outputs, **Then** scores are consistent (no variance) on identical inputs.

3. **Given** Task API agent output, **When** student applies their grader, **Then** they get a 0-5 score based on criteria met.

---

### Learner Journey 3 - Perform Systematic Error Analysis (Priority: P1)

A student learning to systematically count errors by component rather than going by "gut feel."

**Why this priority**: Error analysis determines WHERE to focus improvement efforts. This is Andrew Ng's key insight about less experienced teams under-investing in analysis.

**Independent Test**: Student can create an error analysis spreadsheet that shows which component causes most failures.

**Acceptance Scenarios**:

1. **Given** 20 failed eval cases, **When** student analyzes traces, **Then** they can categorize each failure by component (routing, tool selection, output format, etc.).

2. **Given** categorized errors, **When** student counts patterns, **Then** they can identify the component with highest error percentage (e.g., "45% of errors from routing").

3. **Given** error analysis results, **When** student prioritizes fixes, **Then** they focus on high-frequency × feasibility-to-fix components.

---

### Learner Journey 4 - Build Regression Protection (Priority: P2)

A student learning to run evals on every agent change to catch regressions.

**Why this priority**: Without regression protection, improvements in one area can break other areas. This is the eval-driven development loop.

**Independent Test**: Student can run eval suite before and after a change and compare results.

**Acceptance Scenarios**:

1. **Given** baseline eval results (70%), **When** student makes a change to improve routing, **Then** they can re-run evals and compare (e.g., 85%).

2. **Given** an improvement that breaks something else, **When** student compares before/after, **Then** they detect the regression before shipping.

3. **Given** consistent improvement pattern, **When** student iterates (70% → 85% → 92%), **Then** they have confidence to deploy.

---

### Learner Journey 5 - Build Agent-Evals Skill (Priority: P2)

A student building their `agent-evals` skill through the chapter.

**Why this priority**: Skill-First pattern - the chapter's meta-learning outcome. Students build a reusable asset.

**Independent Test**: Student's skill can help them design evals, create graders, and analyze errors for ANY agent (not just Task API).

**Acceptance Scenarios**:

1. **Given** a student completing L00, **When** they create initial `agent-evals` skill, **Then** skill includes eval design patterns and grader templates.

2. **Given** lessons L01-L09 completed, **When** student tests their skill on a new agent, **Then** skill helps them create appropriate evals.

3. **Given** L10 completed, **When** student finalizes skill, **Then** it's production-ready with error analysis and regression patterns.

---

### Edge Cases

- What happens when LLM-as-judge disagrees with human judgment?
  - This indicates the grader rubric needs refinement; add more specific criteria
- How do you handle non-deterministic agent outputs?
  - Run multiple times (3-5) and look for patterns; accept variability in scores
- What if all evals pass but users still complain?
  - Eval dataset doesn't cover real usage; add cases from production failures
- How many eval cases are "enough"?
  - Start with 10-20; grow when evals fail to capture your judgment about quality

---

## Requirements

### Functional Requirements (Lesson Coverage)

**L00 - Build Your Evals Skill**:
- **FR-001**: Students MUST create `agent-evals` skill following Skill-First pattern
- **FR-002**: Students MUST fetch evaluation methodology docs using `/fetching-library-docs`
- **FR-003**: Skill MUST include eval design patterns and grader templates
- **FR-004**: Students MUST clone skills-lab fresh (no state assumptions)

**L01 - Evals Are Exams for Reasoning**:
- **FR-005**: Chapter MUST establish core distinction: TDD tests CODE, Evals test REASONING
- **FR-006**: Chapter MUST use Andrew Ng's "exams for agents" framing
- **FR-007**: Chapter MUST explain probabilistic outcomes vs deterministic PASS/FAIL
- **FR-008**: Students MUST identify 3 behaviors to improve in Task API agent by manual inspection

**L02 - The Two Evaluation Axes**:
- **FR-009**: Chapter MUST explain Objective (code-checkable) vs Subjective (LLM-judged) evals
- **FR-010**: Chapter MUST explain Per-example ground truth vs No ground truth evals
- **FR-011**: Chapter MUST provide the four-quadrant framework with examples
- **FR-012**: Students MUST classify 5 potential Task API evals into the four quadrants

**L03 - Designing Eval Datasets**:
- **FR-013**: Chapter MUST emphasize quality over quantity (10-20 cases, not 1000)
- **FR-014**: Chapter MUST explain three categories: typical, edge, error cases
- **FR-015**: Chapter MUST emphasize using REAL data from production/user queries
- **FR-016**: Students MUST create 20-case eval dataset for Task API agent

**L04 - Building Graders with Binary Criteria**:
- **FR-017**: Chapter MUST explain why 1-5 scales are poorly calibrated
- **FR-018**: Chapter MUST teach binary criteria pattern (5 yes/no → 0-5 score)
- **FR-019**: Students MUST convert a subjective rubric to binary criteria
- **FR-020**: Students MUST implement code-based grader for objective criteria

**L05 - LLM-as-Judge Graders**:
- **FR-021**: Chapter MUST teach LLM-as-judge prompt structure
- **FR-022**: Chapter MUST warn about position bias in pairwise comparisons
- **FR-023**: Students MUST implement LLM grader for subjective criteria
- **FR-024**: Students MUST compare LLM grader to human judgment on 10 cases

**L06 - Systematic Error Analysis**:
- **FR-025**: Chapter MUST quote Andrew Ng: "Less experienced teams under-invest in analysis"
- **FR-026**: Chapter MUST teach spreadsheet-based error counting
- **FR-027**: Chapter MUST explain traces (full output) and spans (single step)
- **FR-028**: Students MUST create error analysis spreadsheet for Task API failures
- **FR-029**: Students MUST identify highest-error component and prioritize fix

**L07 - Component vs End-to-End Evals**:
- **FR-030**: Chapter MUST explain when to use each type
- **FR-031**: Chapter MUST explain benefits of component evals: clearer signal, faster, less noise
- **FR-032**: Students MUST create component-level eval for Task API routing
- **FR-033**: Students MUST compare component vs E2E eval results

**L08 - Regression Protection**:
- **FR-034**: Chapter MUST teach eval-on-every-change workflow
- **FR-035**: Chapter MUST show before/after comparison pattern
- **FR-036**: Students MUST implement regression protection for Task API agent
- **FR-037**: Students MUST demonstrate detecting a regression via eval comparison

**L09 - The Complete Quality Loop**:
- **FR-038**: Chapter MUST teach Build-Evaluate-Analyze-Improve loop
- **FR-039**: Chapter MUST show iteration pattern (70% → 85% → 92%)
- **FR-040**: Students MUST complete one full improvement cycle
- **FR-041**: Students MUST document their improvement journey

**L10 - Finalize Your Evals Skill**:
- **FR-042**: Students MUST validate their skill helps with eval design
- **FR-043**: Students MUST validate their skill helps with grader creation
- **FR-044**: Students MUST validate their skill helps with error analysis
- **FR-045**: Students MUST test skill on a DIFFERENT agent (not Task API)

### Key Entities

- **Eval Case**: Input + expected behavior + rationale for inclusion
- **Eval Dataset**: Collection of 10-20 high-quality cases (typical + edge + error)
- **Grader**: Automated quality check that turns assessment into measurable scores
- **Binary Criteria**: Yes/no checklist items that sum to a reliable score
- **LLM-as-Judge**: Using an LLM to evaluate another LLM's output
- **Error Analysis**: Systematic counting of failure patterns by component
- **Trace**: All intermediate outputs from agent run
- **Span**: Output of a single step in agent execution
- **Regression**: Previously passing behavior that breaks after a change

---

## Lesson Structure

### Part A: Foundations (L00-L03)

| Lesson | Title | Layer | Duration | Focus | Source |
|--------|-------|-------|----------|-------|--------|
| L00 | Build Your Evals Skill | L3 | 25 min | Skill-First: create skill with eval patterns | Skill-First |
| L01 | Evals Are Exams for Reasoning | L1 | 20 min | Core distinction: TDD vs Evals | Andrew Ng |
| L02 | The Two Evaluation Axes | L1 | 20 min | Objective/Subjective × Ground Truth | Andrew Ng |
| L03 | Designing Eval Datasets | L2 | 25 min | Quality over quantity, 3 categories, real data | Andrew Ng |

### Part B: Building Graders (L04-L05)

| Lesson | Title | Layer | Duration | Focus | Source |
|--------|-------|-------|----------|-------|--------|
| L04 | Building Graders with Binary Criteria | L2 | 30 min | Binary yes/no pattern, code graders | Andrew Ng |
| L05 | LLM-as-Judge Graders | L2 | 30 min | LLM evaluation prompts, position bias | Andrew Ng |

### Part C: Analysis & Improvement (L06-L09)

| Lesson | Title | Layer | Duration | Focus | Source |
|--------|-------|-------|----------|-------|--------|
| L06 | Systematic Error Analysis | L2 | 30 min | Spreadsheet counting, traces, prioritization | Andrew Ng |
| L07 | Component vs End-to-End Evals | L2 | 25 min | When to use each, signal vs noise | Andrew Ng |
| L08 | Regression Protection | L2 | 25 min | Eval-on-every-change, before/after comparison | Andrew Ng |
| L09 | The Complete Quality Loop | L2 | 30 min | Build-Evaluate-Analyze-Improve iteration | Andrew Ng |

### Part D: Skill Finalization (L10)

| Lesson | Title | Layer | Duration | Focus | Source |
|--------|-------|-------|----------|-------|--------|
| L10 | Finalize Your Evals Skill | L3 | 20 min | Skill validation, test on different agent | Skill-First |

**Total**: 11 lessons, ~4.5 hours

**Layer Key**:
- L1 (Manual): Conceptual understanding before implementation
- L2 (Collaboration): AI-assisted implementation
- L3 (Skill): Building/extending the student's skill
- L4 (Spec-Driven): Capstone with full orchestration (not used in this conceptual chapter)

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can explain TDD vs Evals distinction in under 2 minutes (L01 assessment)
- **SC-002**: Students can classify any eval into the four-quadrant framework (L02)
- **SC-003**: Students can create a 20-case eval dataset with proper categorization (L03)
- **SC-004**: Students can convert a 1-5 rubric to binary criteria (L04)
- **SC-005**: Students can implement LLM-as-judge grader that matches human judgment 80%+ (L05)
- **SC-006**: Students can create error analysis spreadsheet showing component error percentages (L06)
- **SC-007**: Students can explain when to use component vs E2E evals (L07)
- **SC-008**: Students can detect a regression using before/after eval comparison (L08)
- **SC-009**: Students can complete one full improvement cycle with documented progress (L09)
- **SC-010**: Students' `agent-evals` skill works on a non-Task API agent (L10)

### Quality Gates

- All examples use Task API agent as running example (consistency with Ch40, Ch46)
- Framework-agnostic: concepts apply to any SDK (OpenAI, Claude, Google ADK)
- Each lesson ends with "Reflect on Your Skill" section (except L00, L10)
- Primary source: Andrew Ng's Agentic AI Course methodology
- No specific eval framework dependency (teach the thinking, not the tooling)

---

## Technology Stack

| Component | Technology | Version | Notes |
|-----------|------------|---------|-------|
| Running Example | Task API agent | From Ch40 | Consistent with Part 6 |
| Language | Python | 3.11+ | For type hints and modern syntax |
| Testing | pytest | Any | For code-based graders |
| LLM | Any SDK | Any | Framework-agnostic examples |
| Spreadsheet | Any | Any | For error analysis (can be CSV/Excel/Sheets) |

---

## Dependencies

### Chapter Dependencies
- **Ch34-36 (SDK chapters)**: Students must know how agents work
- **Ch40 (FastAPI for Agents)**: Provides Task API running example
- **Ch46 (TDD for Agents)**: Students must understand TDD to appreciate Evals distinction

### Skill Dependencies
- Students have Python testing knowledge from Ch46
- Students have agent development skills from Ch34-36

### Technical Dependencies
- Python 3.11+ with pytest
- Access to any LLM API (for LLM-as-judge examples)
- Spreadsheet software (for error analysis)

---

## Available Reference Materials

| Resource | Path | Purpose |
|----------|------|---------|
| Agent Evals Skill | `.claude/skills/agent-evals/SKILL.md` | Expertise skill with methodology |
| Andrew Ng Methodology | `.claude/skills/agent-evals/references/andrew-ng-methodology.md` | Source material |
| Evaluation Skill | `.claude/skills/evaluation/SKILL.md` | Context engineering evaluation (different focus) |
| Quality Reference | `01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-the-2025-inflection-point.md` | Lesson format reference |

---

## Assumptions

1. **TDD Understanding**: Students have completed Ch46 and understand test-driven development
2. **SDK Proficiency**: Students can build agents with at least one SDK (Ch34-36)
3. **Python Proficiency**: Students can write Python with pytest patterns (B1 level)
4. **Task API Familiarity**: Students know the running example from Ch40
5. **Skill-First Familiarity**: Students understand the Skill-First pattern from Part 6 chapters

---

## Scope Boundaries

### In Scope
- Eval concepts: exams for reasoning, probabilistic outcomes
- Two evaluation axes: Objective/Subjective × Ground Truth
- Eval dataset design: typical, edge, error cases
- Graders: binary criteria pattern, code-based and LLM-based
- LLM-as-judge: prompt structure, position bias warning
- Error analysis: spreadsheet counting, trace/span analysis
- Component vs End-to-end evaluation tradeoffs
- Regression protection workflow
- Build-Evaluate-Analyze-Improve loop
- Building `agent-evals` skill

### Out of Scope
- Specific eval frameworks (e.g., Evalica, Promptfoo, Braintrust)
- Continuous monitoring dashboards (operations focus)
- A/B testing for agent variants (experimentation focus)
- Cost/latency optimization (covered elsewhere)
- Multi-agent evaluation coordination
- Eval infrastructure at scale (enterprise focus)

---

## Anti-Patterns to Address

| Anti-Pattern | Why It's Bad | What to Teach |
|-------------|--------------|---------------|
| Waiting for perfect evals | Delays useful feedback | Start with 10 quick cases |
| 1000+ test cases first | Quantity without quality | 20 thoughtful cases |
| 1-5 scale ratings | LLMs poorly calibrated | Binary criteria summed |
| Ignoring traces | Miss root cause | Read intermediate outputs |
| End-to-end only | Too noisy for debugging | Add component-level evals |
| Synthetic test data | Misses real-world messiness | Use actual user queries |
| Going by gut | May work on wrong component | Count errors systematically |
| Skipping regression tests | Breaks working features | Run evals on every change |

---

## Framework-Agnostic Application

These concepts apply to ANY agent framework:

| Framework | Trace Access | Grader Integration | Dataset Storage |
|-----------|-------------|-------------------|-----------------|
| OpenAI Agents SDK | Built-in tracing | Custom graders | JSON/CSV files |
| Claude Agent SDK | Hooks for tracing | Custom graders | JSON/CSV files |
| Google ADK | Evaluation module | Built-in graders | Vertex AI datasets |
| LangChain | LangSmith traces | LangSmith evals | LangSmith datasets |
| Custom | Logging middleware | Custom graders | Any storage |

The thinking is portable. The skill is permanent.
