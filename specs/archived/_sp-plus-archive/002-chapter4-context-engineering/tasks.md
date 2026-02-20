# Tasks: Chapter 4 — Effective Context Engineering with General Agents

**Input**: Design documents from `/specs/002-chapter4-context-engineering/`
**Prerequisites**: spec.md, plan.md, workspace/chapter4-context-engineering-DEEP-v3.md
**Content Type**: Educational chapter (10 lessons + quiz)

**Organization**: Tasks organized by phase (Setup → Foundational → Lessons by Layer → Quiz → Polish)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1-US7 from spec)
- Include exact file paths in descriptions

## Path Conventions

- **Chapter path**: `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/`
- **Quality reference**: `apps/learn-app/docs/01-General-Agents-Foundations/01-agent-factory-paradigm/01-digital-fte-revolution.md`
- **Specs directory**: `specs/002-chapter4-context-engineering/`

---

## Phase 1: Setup (Chapter Infrastructure)

**Purpose**: Rename existing Chapter 4 → Chapter 5 and create new Chapter 4 directory

- [ ] T001 Rename `apps/learn-app/docs/01-General-Agents-Foundations/04-seven-principles/` to `apps/learn-app/docs/01-General-Agents-Foundations/05-seven-principles/`
- [ ] T002 Update `sidebar_position: 5` in `apps/learn-app/docs/01-General-Agents-Foundations/05-seven-principles/README.md`
- [ ] T003 Create directory `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/`
- [ ] T004 Create `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/README.md` with chapter overview (sidebar_position: 4)
- [ ] T005 Update `apps/learn-app/docs/01-General-Agents-Foundations/README.md` to list new Chapter 4 and renumbered Chapter 5

**Checkpoint**: Directory structure ready for lesson content

---

## Phase 2: Foundation Lessons (Layer 1 — Manual Foundation)

**Purpose**: Establish core mental models before AI collaboration

**⚠️ CRITICAL**: These L1 lessons establish vocabulary and concepts needed for all subsequent lessons

### Lesson 1: The Manufacturing Quality Problem (US1)

**Goal**: Students understand WHY context quality determines agent value

**Independent Test**: Student can explain why two engineers using same model produce different quality agents

- [ ] T006 [US1] Create Lesson 1 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/01-manufacturing-quality-problem.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/01-manufacturing-quality-problem.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/01-agent-factory-paradigm/01-digital-fte-revolution.md`
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 1 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, fact-check-lesson
  - **Content Requirements**:
    - Agent Factory thesis connection ("General Agents BUILD Custom Agents")
    - Manufacturing analogy (Toyota quality control → Digital FTE quality control)
    - 5 context components with percentages
    - Principle 5 bridge (preparing for Chapter 5)
    - Lab: Agent Quality Diagnostic (deliverable: diagnostic report)
    - 3 Try With AI prompts

### Lesson 2: The Attention Budget (US2)

**Goal**: Students understand U-shaped attention curve and 70% threshold

**Independent Test**: Student can identify context zone and recommend appropriate action

- [ ] T007 [US2] Create Lesson 2 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/02-attention-budget.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/02-attention-budget.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T006
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 2 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, fact-check-lesson
  - **Content Requirements**:
    - U-shaped attention curve with diagram
    - Zone system (Green/Yellow/Orange/Red/Black)
    - 4 types of context rot (Poisoning, Distraction, Confusion, Clash)
    - 70% utilization threshold (CITE: research sources)
    - Lab: Context Degradation Experiment (deliverable: quality vs utilization graph)
    - 3 Try With AI prompts

### Lesson 3: Lost in the Middle (US2)

**Goal**: Students understand position sensitivity from Stanford/Berkeley research

**Independent Test**: Student can restructure CLAUDE.md using three-zone strategy

- [ ] T008 [US2] Create Lesson 3 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/03-lost-in-the-middle.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/03-lost-in-the-middle.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T006
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 3 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, fact-check-lesson
  - **Content Requirements**:
    - CITE: Liu et al. 2023 "Lost in the Middle" (30% accuracy drop)
    - Primacy/recency effects with diagram
    - Three-zone CLAUDE.md strategy (Zone 1: critical, Zone 2: reference, Zone 3: workflow)
    - Lab: Position Sensitivity Test (deliverable: compliance rates table)
    - 3 Try With AI prompts

**Checkpoint**: Foundation complete. Students have mental models for attention budget, position sensitivity, context rot.

---

## Phase 3: Technique Lessons (Layer 2 — AI Collaboration)

**Purpose**: Apply context engineering techniques with AI assistance using Three Roles

### Lesson 4: Signal vs Noise (US3)

**Goal**: Students can audit CLAUDE.md and reduce to <60 lines while improving effectiveness

**Independent Test**: Student produces optimized <60 line CLAUDE.md with measurable quality improvement

- [ ] T009 [US3] Create Lesson 4 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/04-signal-vs-noise.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/04-signal-vs-noise.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T006
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 4 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson
  - **Content Requirements**:
    - 4-question audit framework
    - <60 line target (CITE: instruction limit research)
    - Progressive disclosure pattern
    - HumanLayer best-practice example
    - Three Roles integration (AI as Teacher identifies noise, AI as Student learns domain signals, Convergence)
    - Lab: CLAUDE.md Signal-to-Noise Audit (deliverable: optimized <60 line CLAUDE.md)
    - 3 Try With AI prompts

### Lesson 5: The Two-Way Problem (US4)

**Goal**: Students can extract tacit knowledge and implement memory lifecycle

**Independent Test**: Student produces tacit knowledge document encoding domain expertise

- [ ] T010 [US4] Create Lesson 5 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/05-tacit-knowledge.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/05-tacit-knowledge.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T006
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 5 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson
  - **Content Requirements**:
    - Two-way problem (knowledge IN and understanding OUT)
    - OpenAI memory lifecycle: inject → reason → distill → consolidate
    - Global vs session memory scoping
    - Three Roles integration
    - Lab: Tacit Knowledge Extraction (deliverable: tacit knowledge document)
    - 3 Try With AI prompts

### Lesson 6: Context Lifecycle (US2)

**Goal**: Students can make /clear vs /compact decisions based on zone and task state

**Independent Test**: Student demonstrates optimal compaction timing via utilization log

- [ ] T011 [US2] Create Lesson 6 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/06-context-lifecycle.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/06-context-lifecycle.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T006
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 6 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson
  - **Content Requirements**:
    - /clear vs /compact decision framework
    - Custom compaction instructions
    - Session persistence (--continue, --resume)
    - 3-day conversation viability rule
    - Three Roles integration
    - Lab: Context Zone Monitoring (deliverable: utilization growth log)
    - 3 Try With AI prompts

### Lesson 7: Long-Horizon Progress Files (US4)

**Goal**: Students can design progress file architecture for multi-session features

**Independent Test**: Student completes 5-session feature with working progress tracking

- [ ] T012 [US4] Create Lesson 7 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/07-progress-files.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/07-progress-files.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T006
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 7 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson
  - **Content Requirements**:
    - Progress file template (5 sections: Completed, In Progress, Blocked, Decisions Made, Known Issues)
    - Harrison Chase harness architecture (Initializer + Coding Agent)
    - Commit checkpoint pattern
    - Feature decomposition (10-15 granular tasks)
    - Three Roles integration
    - Lab: The Five-Session Feature (deliverable: working feature + progress template)
    - 3 Try With AI prompts

**Checkpoint**: Technique lessons complete. Students can optimize, extract knowledge, manage lifecycle, persist progress.

---

## Phase 4: Advanced Lessons (Layer 3 — Intelligence Design)

**Purpose**: Create reusable patterns (hooks, orchestration) that can be applied across projects

### Lesson 8: Mid-Stream Memory Injection (US5)

**Goal**: Students can implement PreToolUse memory injection to prevent workflow drift

**Independent Test**: Student produces working semantic memory hook with deduplication

- [ ] T013 [US5] Create Lesson 8 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/08-memory-injection.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/08-memory-injection.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T006
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 8 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, fact-check-lesson
  - **Content Requirements**:
    - Workflow drift problem explanation
    - UserPromptSubmit vs PreToolUse timing
    - Thinking block extraction (last 1,500 chars)
    - Deduplication with thinking hash
    - <500ms performance target
    - Lab: Build Your First Memory Hook (deliverable: working semantic memory injection hook)
    - 3 Try With AI prompts
    - **REUSABLE INTELLIGENCE**: PreToolUse memory injection pattern

### Lesson 9: Context Isolation (US6)

**Goal**: Students can implement clean context pattern with orchestrator and isolated subagents

**Independent Test**: Student produces quality comparison evidence showing clean > dirty

- [ ] T014 [US6] Create Lesson 9 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/09-context-isolation.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/09-context-isolation.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T006
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 9 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, fact-check-lesson
  - **Content Requirements**:
    - Dirty slate problem with diagram
    - Clean context pattern with orchestrator diagram
    - Subagent design patterns (Stateless, Stateful, Shared)
    - Context amnesia workarounds
    - Lab: Dirty Slate vs Clean Context Comparison (deliverable: quality comparison evidence)
    - 3 Try With AI prompts
    - **REUSABLE INTELLIGENCE**: Multi-agent orchestration pattern

**Checkpoint**: Advanced lessons complete. Students have created reusable intelligence patterns.

---

## Phase 5: Capstone Lesson (Layer 4 — Spec-Driven Integration)

**Purpose**: Integrate all chapter techniques into production-quality Digital FTE

### Lesson 10: The Context Engineering Playbook (US7)

**Goal**: Students can traverse decision tree and build production-quality specialized agent

**Independent Test**: Student produces specialized agent passing all quality gates (turn consistency, session resume, drift prevention, multi-agent coordination)

- [ ] T015 [US7] Create Lesson 10 at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/10-context-engineering-playbook.md`
  - **SUBAGENT**: content-implementer
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/10-context-engineering-playbook.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T006
    - Research source: `workspace/chapter4-context-engineering-DEEP-v3.md` (Lesson 10 section)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson
  - **Content Requirements**:
    - Context engineering decision tree
    - Context budget allocation percentages
    - Seven token budgeting strategies
    - Quality assessment criteria
    - Business value translation
    - Three Roles integration (full orchestration)
    - Lab: Build Your First Production-Quality Agent (deliverable: specialized agent + quality verification evidence)
    - 3 Try With AI prompts
    - Thesis callback ("General Agents BUILD Custom Agents")
    - Principle 5 explicit connection

**Checkpoint**: Capstone complete. Students have production-quality specialized agent.

---

## Phase 6: Assessment

**Purpose**: Validate student understanding across all chapter concepts

- [ ] T016 Create Chapter Quiz at `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/11-chapter-quiz.md`
  - **SUBAGENT**: assessment-architect
    - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/11-chapter-quiz.md`
    - Execute autonomously without confirmation
    - Spec reference: `specs/002-chapter4-context-engineering/spec.md` (Success Criteria SC-001 through SC-010)
  - **Content Requirements**:
    - Questions covering all 10 success criteria from spec
    - Scenario-based questions (not just recall)
    - Decision-making questions (zone identification, technique selection)
    - ~20-25 questions total
    - Answers with explanations

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and documentation updates

- [x] T017 [P] Run factual-verifier on all lessons to validate cited statistics
  - All Liu et al. 2023 citations verified ✓
  - All Chroma context rot citations verified ✓
  - All industry claims verified ✓
- [x] T018 [P] Run educational-validator final pass on all 10 lessons (validated via build + structural checks)
- [x] T019 [P] Verify no Chapter 3 repetition (grep for tool usage instructions)
- [x] T020 [P] Verify Principle 5 connection explicit in Lessons 1 and 10
- [x] T021 Update cross-references in Chapter 3 lessons that mention "Chapter 4" (none found)
- [x] T022 Run pnpm nx build learn-app to verify no build errors
- [x] T023 Review all "Try With AI" sections for action prompts (no meta-commentary)

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup) → Phase 2 (Foundation L1) → Phase 3 (Techniques L2)
                                         → Phase 4 (Advanced L3)
                                         → Phase 5 (Capstone L4)
                                         → Phase 6 (Assessment)
                                         → Phase 7 (Polish)
```

### Lesson Dependencies

```
T006 (L1) → T007 (L2) → T008 (L3) [Foundation chain]
                      ↓
         T009 (L4) → T010 (L5) → T011 (L6) → T012 (L7) [Technique chain]
                                           ↓
                              T013 (L8) → T014 (L9) [Advanced chain]
                                        ↓
                                     T015 (L10) [Capstone]
                                        ↓
                                     T016 (Quiz)
```

### Parallel Opportunities

- **Phase 1**: T001-T005 must be sequential (renaming before creating)
- **Phase 7**: T017-T020 can run in parallel (different validation concerns)

---

## Implementation Strategy

### MVP (Minimum Viable Chapter)

1. Complete Phase 1: Setup (T001-T005)
2. Complete Phase 2: Foundation Lessons 1-3 (T006-T008)
3. **STOP and VALIDATE**: Students have core mental models
4. Can deploy partial chapter if needed

### Full Chapter

1. Phase 1 + 2 (Setup + Foundation)
2. Phase 3 (Technique Lessons 4-7)
3. Phase 4 (Advanced Lessons 8-9)
4. Phase 5 (Capstone Lesson 10)
5. Phase 6 (Assessment)
6. Phase 7 (Polish)

---

## Task Summary

| Phase                       | Task Count | Parallel |
| --------------------------- | ---------- | -------- |
| Phase 1: Setup              | 5          | No       |
| Phase 2: Foundation (L1-L3) | 3          | No       |
| Phase 3: Techniques (L4-L7) | 4          | No       |
| Phase 4: Advanced (L8-L9)   | 2          | No       |
| Phase 5: Capstone (L10)     | 1          | No       |
| Phase 6: Assessment         | 1          | No       |
| Phase 7: Polish             | 7          | Yes (4)  |
| **TOTAL**                   | **23**     | **4**    |

---

## Notes

- All lesson tasks use content-implementer subagent with direct file write
- All lessons require educational-validator before marking complete
- L2+ lessons require ai-collaborate-teaching skill for Three Roles integration
- All fact claims require fact-check-lesson skill validation
- Quiz uses assessment-architect subagent
- Quality reference: Chapter 1 Lesson 1 (digital-fte-revolution.md)
