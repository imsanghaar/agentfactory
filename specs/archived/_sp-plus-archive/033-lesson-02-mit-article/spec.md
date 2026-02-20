# Feature Specification: Integrate MIT Technology Review Article into Lesson 02

**Feature Branch**: `033-lesson-02-mit-article`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Improve lesson 02 by integrating MIT Technology Review article on ChatGPT economy impact"

## Success Evals *(defined first per Constitution v6.0.1)*

### Primary Learning Outcomes (Before Specification)

**Eval-1: Job Impact Specificity** (Target: 80%+ students)
Students can identify and explain 3+ specific job categories affected by AI transformation (e.g., writers, designers, financial analysts, blockchain engineers), distinguishing between "80% workforce exposure" and "80% jobs eliminated" when interpreting OpenAI research findings.

**Eval-2: Two Futures Articulation** (Target: 85%+ students)
Students can articulate both economic futures (optimistic upskilling tool vs pessimistic inequality accelerator) with at least one concrete research example per scenario (e.g., MIT productivity study for optimistic, Acemoglu/Johnson historical examples for pessimistic), recognizing that societal choices determine which future emerges.

**Eval-3: Evidence-Based Career Confidence** (Target: 90%+ students)
Students can cite 2+ pieces of empirical evidence from the lesson (MIT Noy/Zhang study showing ChatGPT helped least-skilled workers most, OpenAI research on job exposure patterns) supporting the "expansion not contraction" thesis and apply this evidence to justify their personal learning decisions.

**Eval-4: Turing Trap Recognition** (Target: 75%+ students)
Students can explain Brynjolfsson's "Turing Trap" concept—why building AI that mimics humans leads to replacement rather than augmentation—and identify whether they're positioning themselves as AI's replacement or partner.

**Eval-5: Historical Context Application** (Target: 70%+ students)
Students can reference Acemoglu/Johnson "Power & Progress" framework with at least one historical example (post-WWII shared prosperity vs recent concentrated wealth) showing technology outcomes depend on societal choices, not technological determinism.

**Eval-6: Factual Accuracy & Attribution** (Target: 100%)
All statistical claims (80% workforce, 19% heavily impacted), expert quotes, and study references from MIT TR article verified against original source and properly cited with author (David Rotman), publication, date (March 25, 2023), and URL.

**Eval-7: Complexity Compliance** (Target: 100% of sections)
Enhanced sections maintain A1-A2 proficiency level with 5-7 new concepts per section, clear explanations without jargon, and organic integration into existing lesson structure.

**Eval-8: Reflection Integration** (Target: 3+ new prompts)
"Try With AI" section includes at least 3 new reflection prompts connecting MIT TR insights to student's personal journey, covering job vulnerability assessment, two futures positioning, and evidence-based career confidence.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Understanding Job Transformation Specifics (Priority: P1)

As a student reading Lesson 02, I want to understand **which specific jobs** are affected by AI and **how quickly** this transformation is happening, so I can make informed decisions about my career path and skill development priorities.

**Why this priority**: The current lesson discusses the $3T economy in aggregate but lacks specific job impact data. The MIT TR article provides concrete research (OpenAI study: 80% workforce affected, 19% jobs heavily impacted) that makes the transformation personally relevant.

**Independent Test**: Can be fully tested by reading the enhanced "Job Impact" section and successfully identifying 3-5 specific job categories mentioned, explaining why higher-income jobs are more vulnerable.

**Acceptance Scenarios**:

1. **Given** a student reading the enhanced lesson, **When** they reach the job impact section, **Then** they should encounter specific job categories with OpenAI research citation
2. **Given** a student concerned about job security, **When** they read the comparison to previous automation waves, **Then** they should understand why this wave targets higher-income cognitive work
3. **Given** a student completing the lesson, **When** they reflect on "Try With AI" prompts, **Then** they should articulate which jobs in their field are most/least vulnerable

---

### User Story 2 - Recognizing Two Divergent Economic Futures (Priority: P1)

As a student learning about AI's economic impact, I want to understand that **the outcome isn't predetermined**—there are two possible futures (upskilling tool vs. inequality accelerator)—so I can see my role in shaping which future emerges.

**Why this priority**: The current lesson presents acceleration as inevitable without exploring societal choices. The MIT TR article emphasizes "we need to decide what that looks like" and presents Acemoglu/Johnson's framework.

**Independent Test**: Can be fully tested by presenting a student with a hypothetical AI tool and having them articulate both potential outcomes with specific examples from the lesson.

**Acceptance Scenarios**:

1. **Given** a student reading the "Two Economic Futures" section (new), **When** they encounter the pessimistic vs. optimistic scenarios, **Then** they should see concrete examples
2. **Given** a student who thinks "AI will inevitably take jobs," **When** they read the Acemoglu/Johnson framework, **Then** they should recognize that societal choices determine outcomes
3. **Given** a student completing "Try With AI" exercises, **When** asked to reflect, **Then** they should articulate whether they're positioning as AI's replacement or partner

---

### User Story 3 - Evidence-Based Optimism for Career Entry (Priority: P2)

As a beginner considering whether to enter software development, I want to see **concrete evidence** that AI creates opportunity rather than just displacing workers, so I can commit to learning with confidence.

**Why this priority**: Many beginners experience anxiety about "learning to code when AI can code." The MIT TR article provides empirical evidence showing expansion, not contraction.

**Independent Test**: Can be fully tested by asking a student to cite **three pieces of evidence** from the lesson supporting the "expansion, not displacement" thesis.

**Acceptance Scenarios**:

1. **Given** a student reading the enhanced "Acceleration Paradox" section, **When** they encounter the MIT productivity study, **Then** they should understand the experimental design and key findings
2. **Given** a skeptical student who asks "But won't experienced developers lose jobs?", **When** they review the evidence section, **Then** they should cite specific research findings
3. **Given** a student completing the lesson, **When** they answer "Try With AI" reflection prompts, **Then** they should articulate why evidence supports their learning journey

---

### User Story 4 - Understanding Policy and Societal Context (Priority: P3)

As a student learning about AI's economic transformation, I want to understand the **policy debates and societal choices** being discussed by economists, so I recognize this is a civic and political issue.

**Why this priority**: This elevates the lesson from "how to position yourself" to "how society should respond." This is P3 because it's enrichment rather than core learning objective.

**Independent Test**: Can be fully tested by having a student summarize 2-3 policy proposals mentioned in the lesson and explain the rationale for each.

**Acceptance Scenarios**:

1. **Given** a student reading the "What This Means For You" section (enhanced), **When** they encounter policy discussion, **Then** they should understand proposals like public-funded AI research
2. **Given** a student discussing AI with non-technical friends, **When** asked "Should government regulate AI?", **Then** they should reference specific concerns
3. **Given** a student reflecting on the conclusion, **When** they consider their role, **Then** they should recognize both individual skill choices AND collective policy choices matter

---

### Edge Cases

- **What happens when** a student encounters conflicting information about AI's job impact from other sources?
  - Lesson should equip them to distinguish between "80% of jobs have SOME exposure" vs. "80% of jobs will be eliminated"

- **How does the lesson handle** students at different career stages?
  - Content remains accessible to A1-A2 proficiency while providing depth for advanced readers

- **What if** a student reads this in 2027-2028 and predictions haven't materialized?
  - Frame predictions as "expert forecasts at time of writing (2023)" with caveats

- **How does content avoid** dated references while preserving insights?
  - Integrate insights into existing structure rather than adding time-stamped sections

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Lesson MUST integrate specific job impact data from OpenAI research (80% workforce exposure, 19% heavily impacted jobs, specific categories: writers, designers, financial analysts, blockchain engineers)

- **FR-002**: Lesson MUST add new section "Two Economic Futures" presenting both pessimistic and optimistic scenarios with concrete examples from MIT TR article

- **FR-003**: Lesson MUST incorporate MIT productivity study (Noy/Zhang) findings showing ChatGPT helped least-skilled workers most

- **FR-004**: Lesson MUST include Brynjolfsson's "Turing Trap" concept explaining why human-mimicking AI leads to replacement rather than augmentation

- **FR-005**: Lesson MUST integrate Acemoglu/Johnson "Power & Progress" framework showing historical examples (post-WWII shared prosperity vs. recent concentrated wealth)

- **FR-006**: Lesson MUST properly cite MIT Technology Review article throughout with author (David Rotman), publication (MIT Technology Review), date (March 25, 2023), and URL

- **FR-007**: Lesson MUST update "Try With AI" section to include reflection prompts about two futures, personal positioning relative to AI, and evidence-based career confidence

- **FR-008**: Lesson summary MUST be updated to reflect new content additions: job specifics, two futures framework, MIT study evidence, Acemoglu/Johnson perspectives

- **FR-009**: New content MUST maintain A1-A2 proficiency level (5-7 concepts per section, clear explanations, minimal jargon) per constitutional complexity requirements

- **FR-010**: Lesson MUST preserve existing structure and flow, integrating new content organically rather than appending disconnected sections

- **FR-011**: All factual claims from MIT TR article MUST be verified against original source (article text retrieved via browser automation) before integration

- **FR-012**: Lesson MUST include at least one visual aid (diagram, chart, or infographic) illustrating two economic futures or job impact distribution

### Key Entities

- **Lesson Content**: Main educational markdown file containing narrative, examples, expert insights, diagrams, and learning exercises
  - Current state: Comprehensive lesson on $3T developer economy, acceleration paradox, historical precedent
  - Target state: Enhanced with MIT TR article insights on job specifics, two futures, evidence-based optimism, policy context

- **Lesson Summary**: Companion markdown file distilling core concepts, mental models, patterns, and common mistakes
  - Current state: 23-line summary covering value vs. salary, expansion paradox, acceleration pattern
  - Target state: Updated to reflect new mental models (two futures, Turing Trap, Power & Progress framework)

- **MIT TR Article**: Source material providing authoritative research, expert quotes, and economic analysis
  - Author: David Rotman (Editor at Large, MIT Technology Review)
  - Key sources cited within: OpenAI researchers, MIT economists, Stanford/Cambridge researchers
  - Publication date: March 25, 2023

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can identify at least 3 specific job categories mentioned as vulnerable to AI transformation and explain why higher-income cognitive work is affected

- **SC-002**: Students can articulate both economic futures (optimistic upskilling vs. pessimistic inequality) with at least one concrete example from research for each scenario

- **SC-003**: Students can cite at least two pieces of empirical evidence from the lesson supporting AI expansion rather than contraction thesis

- **SC-004**: Lesson achieves 90%+ factual accuracy as validated by checking all MIT TR article claims against original source text

- **SC-005**: Enhanced lesson maintains A1-A2 proficiency level per constitutional requirements: average section contains 5-7 new concepts with clear explanations

- **SC-006**: MIT Technology Review article is properly attributed throughout lesson with complete citation (author, publication, date, URL)

- **SC-007**: Updated lesson summary accurately reflects enhanced content, adding mental models for "Two Economic Futures" and "Turing Trap" concepts

- **SC-008**: "Try With AI" section includes at least 3 new reflection prompts connecting article insights to student's personal learning journey

- **SC-009**: Lesson content flows logically with new material integrated organically into existing structure, not appended as disconnected sections

- **SC-010**: At least one visual aid effectively illustrates key concept from MIT TR article

## Assumptions

- New content will be woven into existing sections rather than added as standalone "MIT TR Article Insights" section
- Full academic citation (author, publication, date, URL) on first mention, shorter citations subsequently
- New content will maintain A1-A2 proficiency level even when discussing complex economic concepts
- One new diagram will be created showing "Two Economic Futures" branching paths
- Summary will add 3-5 new lines covering Two Futures framework, Turing Trap warning, and MIT study evidence
- Browser-automated article retrieval (completed in Phase 0) provides sufficient content for fact-checking

## Non-Goals

- **Not adding**: Comprehensive economic theory lessons—this remains a practical software development book
- **Not creating**: Separate lesson on policy and regulation—policy discussion serves as context
- **Not including**: Detailed analysis of every expert mentioned in MIT TR article
- **Not updating**: Other lessons in Chapter 1 to align with MIT TR insights—scope limited to Lesson 02
- **Not adding**: Interactive exercises beyond enhanced "Try With AI" prompts
- **Not changing**: Fundamental lesson structure or learning objectives—enhancement adds depth, not new direction

## Dependencies & Prerequisites

### Required Before Implementation

- ✅ **Article content verification**: Complete browser-automated retrieval of MIT TR article text (COMPLETED in Phase 0)
- **Constitutional review**: Confirm enhancement aligns with Principle 3 (Factual Accuracy), Principle 2 (Progressive Complexity A1-A2), Principle 7 (Minimal Content)

### Optional Enhancements (Post-MVP)

- **Visual design consistency**: New diagram for "Two Economic Futures" should match existing lesson diagram style
- **Cross-lesson citation**: If future lessons reference "two economic futures" framework, this lesson becomes canonical source

## Success Metrics

### Quantitative Metrics

- **Fact-check pass rate**: 100% of MIT TR article claims verified against original source before publication
- **Citation completeness**: 100% of article-sourced claims include proper attribution
- **Complexity compliance**: 100% of enhanced sections maintain 5-7 concepts per section (A1-A2 limit)
- **Summary accuracy**: Updated summary includes 3+ new mental models with 0 omissions

### Qualitative Metrics

- **Narrative cohesion**: Enhanced lesson reads as unified narrative, not patchwork of disconnected insights
- **Pedagogical effectiveness**: New content serves learning objectives without introducing confusion
- **Student agency**: Lesson successfully reframes transformation from "inevitable disruption" to "outcome depends on choices"

### Validation Checkpoints

1. **Post-integration fact-check**: Compare every statistical claim, expert quote, and study reference against browser-retrieved MIT TR article text
2. **Constitutional compliance review**: Educational-validator checks Principle 2 (complexity), Principle 3 (accuracy), Principle 7 (minimal content)
3. **Narrative flow testing**: Read enhanced lesson end-to-end to ensure organic integration without abrupt transitions
4. **Summary alignment check**: Verify updated summary accurately represents enhanced content

---

**Ready for**: Planning phase (`/sp.plan`) once specification approved by user and validated by spec-architect subagent.
