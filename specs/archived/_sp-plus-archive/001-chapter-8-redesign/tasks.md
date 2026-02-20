# Tasks: Chapter 8 Redesign - Git & GitHub for AI-Driven Development (CoLearning Format)

**Input**: Design documents from `/specs/001-chapter-8-redesign/`
**Prerequisites**: plan.md (5 lessons), spec.md (6 user stories, 26 functional requirements)

**Tests**: Not applicable - educational content, not software implementation

**Organization**: Tasks are grouped by lesson (which map to user stories) to enable independent content creation and review.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can be written in parallel (different lessons, no dependencies)
- **[Lesson]**: Which lesson this task creates (e.g., L1, L2, L3, L4, L5)
- Include exact file paths in descriptions

## Path Conventions

**Chapter Location**: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/`

**Files to Create/Update**:
- `README.md` — Chapter overview, learning objectives, prerequisites
- `01-why-git-matters.md` — Lesson 1
- `02-git-essentials.md` — Lesson 2
- `03-safe-experimentation.md` — Lesson 3
- `04-pull-requests-collaboration.md` — Lesson 4
- `05-natural-language-git.md` — Lesson 5

---

## Phase 1: Setup (Chapter Foundation)

**Purpose**: Initialize chapter structure and establish pedagogical framework

- [ ] T001 Update chapter README with conversational CoLearning format overview in `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/README.md`
- [ ] T002 Document 5-lesson architecture with CEFR proficiency levels in README
- [ ] T003 Add AIDD integration overview (validation commits, spec branches, checkpoints) to README
- [ ] T004 Create chapter-level "Try With AI" policy note: Use ChatGPT (pre-tool) or AI CLI (post-tool) in final section of each lesson

---

## Phase 2: Foundational (Pedagogical Templates)

**Purpose**: Create reusable conversational examples and establish pattern library

**⚠️ CRITICAL**: These templates MUST be complete before lesson content creation

- [ ] T005 Create conversational template: "You: → Agent: → Tool Output: → Agent: → What you learned:" pattern with 3 concrete examples in specs/001-chapter-8-redesign/conversational-examples.md
- [ ] T006 Document validation commit template: `[AI] Tool - Feature\n\nEvals:\n- ✅ criteria\n\nTests: X/Y` with progressive levels (1: AI tag, 2: +tests, 3: +manual validation)
- [ ] T007 Create checkpoint pattern template showing 3 contexts: (1) basic commit, (2) before branching, (3) before AI session
- [ ] T008 Document "Your Turn: Practice" format with 5 example prompts that are copy-paste ready

**Checkpoint**: Template library complete - lesson content creation can now begin in parallel

---

## Phase 3: Lesson 1 - Why Git Matters (US1: Learning Git Through Conversation) 🎯 MVP Foundation

**Goal**: Establish motivation and conceptual foundation without intimidating commands

**Maps to User Story 1 (P1)**: Learning Git through AI conversation
**Independent Test**: Learner can articulate 3+ reasons why Git matters for AI development (safety, collaboration, auditability)

**CEFR Level**: A1 Understand
**Cognitive Load**: 3 concepts (safety net, checkpoints, collaboration)
**Duration**: 30 minutes

### Content Creation for Lesson 1

- [ ] T009 [P] [L1] Write opening hook: "What if Claude Code broke your project? With Git, you're 30 seconds from recovery" in `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/01-why-git-matters.md`
- [ ] T010 [P] [L1] Create "The Three Problems Git Solves" section with AI-specific contexts (safety for AI experiments, collaboration on AI code, auditing AI changes)
- [ ] T011 [P] [L1] Write 4-5 concrete scenarios with conversational format:
  - Solo developer: AI refactoring with rollback safety
  - Team code review: Catching AI bug before production
  - Debugging: Finding when/where AI introduced bug
  - Accidental secret: Understanding Git history permanence
- [ ] T012 [L1] Create "Analogies That Make Git Click" section: video game save points, film production takes, sports checkpoint analysis, insurance for code
- [ ] T013 [L1] Write reflection prompts (no hands-on practice yet): "Think of a time you worked on code with others—what went wrong?" and "What would concern you about AI-generated payment code?"
- [ ] T014 [L1] Add "Try With AI" section: Prompt learners to ask ChatGPT "Explain Git's role in AI-driven development as if I've never coded before"

**Checkpoint**: Lesson 1 complete - learners understand WHY before learning HOW

---

## Phase 4: Lesson 2 - Git Essentials (US1: Conversation + US2: Validation Commits) 🎯 Core Skills

**Goal**: Teach fundamental Git workflow through conversational examples + introduce validation commit pattern

**Maps to User Stories**:
- US1 (P1): Learning through conversation (acceptance scenario 1-2)
- US2 (P1): Validation-driven commits (all scenarios)

**Independent Test**: Learner can create repository, make validation commit with AI attribution and test evidence, view history

**CEFR Level**: A1 Apply
**Cognitive Load**: 4 concepts (repository, staging, commit, validation format)
**Duration**: 90 minutes (45 content + 45 practice)

### Content Creation for Lesson 2

- [ ] T015 [P] [L2] Write installation section with conversational format: "You: I need to install Git" → "Agent: Let me help you install Git for [OS]" → Tool Output → Agent explains in `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/02-git-essentials.md`
- [ ] T016 [P] [L2] Create platform-specific installation conversations (3 separate: Windows/Mac/Linux) showing full "You → Agent → Output → Agent → Learned" pattern
- [ ] T017 [P] [L2] Write configuration conversation: "You: How do I set my name?" → Agent guides `git config --global user.name` with explanation of why identity matters
- [ ] T018 [L2] Create "The Core Workflow" conversation showing complete cycle: status → add → commit → log with AIDD validation format introduced
- [ ] T019 [L2] Write 3 conversational examples demonstrating validation commit pattern:
  - Example 1: Basic commit with [AI] tag only (Level 1)
  - Example 2: Commit with [AI] tag + tests passing (Level 2)
  - Example 3: Full validation commit with tests + manual checks (Level 3)
- [ ] T020 [L2] Create "Understanding Git Output" conversation: Agent explains `git status` colors/sections, what "staged" means, how to read `git log`
- [ ] T021 [L2] Write "Your Turn: Practice" section with 5 copy-paste ready prompts:
  - "Install Git and show me the version"
  - "Configure my Git identity with name [X] and email [Y]"
  - "Create a new repository in this directory"
  - "Stage my changes and create a commit"
  - "Show me my commit history"
- [ ] T022 [L2] Add troubleshooting conversation: "You: Git installation failed" → Agent diagnoses common issues per platform
- [ ] T023 [L2] Create "Try With AI" section: "Ask your AI agent: 'Create a validation commit for code Claude just generated with test evidence'"

**Checkpoint**: Lesson 2 complete - learners can use basic Git workflow with AIDD validation pattern

---

## Phase 5: Lesson 3 - Safe Experimentation (US3: Spec Branching + US4: Checkpoints) 🎯 Safety Patterns

**Goal**: Teach branching for safe AI experimentation + checkpoint pattern before AI sessions

**Maps to User Stories**:
- US3 (P2): Specification-driven branching (all scenarios)
- US4 (P2): Checkpoints before AI sessions (all scenarios)

**Independent Test**: Learner creates spec file in feature branch, commits checkpoint before AI session, tests changes, then merges or rolls back

**CEFR Level**: A2 Apply
**Cognitive Load**: 4 concepts (branches, checkpoints, merge, rollback)
**Duration**: 90 minutes (40 content + 50 practice)

### Content Creation for Lesson 3

- [ ] T024 [P] [L3] Write "The Checkpoint Pattern" conversation: "You: Before letting Claude refactor my auth.py, how do I protect my work?" → Agent guides checkpoint creation + noting hash in `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/03-safe-experimentation.md`
- [ ] T025 [P] [L3] Create "Specification-Driven Branching" conversation showing AIDD workflow:
  - Create spec file: payment-spec.md
  - Commit spec as first commit in feature branch
  - Implement with validation commits referencing spec
  - Show how commits validate against spec criteria
- [ ] T026 [P] [L3] Write "Branch-Based Experimentation" conversations (3 examples):
  - "You: Create a safe space to test Claude's database refactoring" → Agent creates feature branch
  - "You: How do I switch back to my safe main branch?" → Agent explains checkout
  - "You: The AI changes work! How do I keep them?" → Agent guides merge
- [ ] T027 [L3] Create "Undoing Changes (The Safety Net)" conversation showing progressive options:
  - Soft reset (keep changes, undo commit)
  - Hard reset (discard everything - show warning!)
  - Revert (safe alternative creating new commit)
- [ ] T028 [L3] Write merge conversation with conflict resolution: "You: Git says CONFLICT in auth.py. What do I do?" → Agent explains markers, guides resolution, shows asking AI for help
- [ ] T029 [L3] Create rollback scenario: "You: Claude's refactoring broke my tests. How do I go back?" → Agent guides `git reset --hard [checkpoint-hash]`
- [ ] T030 [L3] Write "Your Turn: Practice" with 6 prompts:
  - "Create a checkpoint commit before AI makes changes"
  - "Create a feature branch called feature/user-authentication"
  - "Switch between my feature branch and main"
  - "Merge my feature branch into main"
  - "Show me how to rollback one commit"
  - "Create and resolve a simple merge conflict"
- [ ] T031 [L3] Add "Try With AI" section: "Ask your agent: 'Guide me through creating a spec-driven branch for a payment feature, with checkpoint before implementation'"

**Checkpoint**: Lesson 3 complete - learners can safely experiment with AI using branches and checkpoints

---

## Phase 6: Lesson 4 - Pull Requests & Collaboration (US5: PR as Spec Review) 🎯 Team Workflows

**Goal**: Teach GitHub PR workflow with spec fulfillment evidence

**Maps to User Story 5 (P3)**: Pull requests as spec reviews (all scenarios)

**Independent Test**: Learner creates PR with description showing: spec reference → implementation summary → validation evidence → spec fulfillment checklist

**CEFR Level**: A2 Apply
**Cognitive Load**: 3 concepts (remote, push/pull, pull requests)
**Duration**: 75 minutes (35 content + 40 practice)

### Content Creation for Lesson 4

- [ ] T032 [P] [L4] Write "Understanding Pull Requests" conversation: "You: What's a pull request and why do teams use them?" → Agent explains code review, discussion, auditing in `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/04-pull-requests-collaboration.md`
- [ ] T033 [P] [L4] Create "Creating Your First PR" conversation with AIDD template:
  - Push branch: "You: How do I share my feature branch?" → Agent guides `git push -u origin feature-name`
  - Open PR on GitHub web interface (walkthrough with descriptions)
  - PR description template showing: Spec → Implementation → Validation → Fulfillment checklist
- [ ] T034 [P] [L4] Write "Code Review Conversation" showing what reviewers check in AI code:
  - Security concerns (no hardcoded secrets)
  - Logic correctness (edge cases handled)
  - Test coverage (validation evidence present)
  - Spec alignment (requirements met)
- [ ] T035 [L4] Create "Iteration and Feedback" conversation: "You: Reviewer said my auth needs rate limiting. How do I update the PR?" → Agent guides: make changes → commit → push (PR auto-updates)
- [ ] T036 [L4] Write "Merging on GitHub" conversation showing merge strategies: merge commit (default), squash (clean history), rebase (linear)
- [ ] T037 [L4] Create "Handling PR Conflicts" conversation: "You: GitHub says my PR has conflicts. What now?" → Agent guides: pull main → resolve locally → push
- [ ] T038 [L4] Write "Your Turn: Practice" with 7 prompts:
  - "Create a repository on GitHub"
  - "Push my local branch to GitHub"
  - "Create a pull request via GitHub web interface"
  - "Add a comment to my own PR (simulate review)"
  - "Make additional commits to address feedback"
  - "Merge my PR on GitHub"
  - "Pull the merged changes back to my local main"
- [ ] T039 [L4] Add "Try With AI" section: "Ask your agent: 'Help me create a PR description that shows spec fulfillment for the auth feature I just completed'"

**Checkpoint**: Lesson 4 complete - learners can collaborate using GitHub PRs with spec review practices

---

## Phase 7: Lesson 5 - Natural Language Git (US6: Troubleshooting + All Prior) 🎯 Convenience Layer

**Goal**: Show how to use AI agents for Git operations via natural language while maintaining understanding

**Maps to User Story 6 (P3)**: Troubleshooting through conversation (all scenarios)
**Also synthesizes**: All prior user stories (US1-US5) by showing natural language alternatives

**Independent Test**: Learner can translate 10+ Git commands to natural language prompts, use AI to troubleshoot errors, explain when to use prompts vs. direct commands

**CEFR Level**: A2 Apply
**Cognitive Load**: 2 concepts (natural language translation, when to use AI help)
**Duration**: 45 minutes (15 concept + 30 practice)

### Content Creation for Lesson 5

- [ ] T040 [P] [L5] Write "Why Natural Language Prompts?" mindset conversation: "You: Git commands feel overwhelming. Can AI help?" → Agent explains: prompts reduce memorization BUT still understand concepts in `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/05-natural-language-git.md`
- [ ] T041 [P] [L5] Create "Command-to-Prompt Translation" table with 10+ examples:
  - `git status` → "What changes are in my working directory?"
  - `git checkout -b feature-auth` → "Create a new branch called feature-auth and switch to it"
  - `git commit` → "Stage all changes and create validation commit with AI attribution"
  - (Include 7+ more covering all core patterns from Lessons 2-4)
- [ ] T042 [P] [L5] Write "Complex Workflow Prompts" conversations showing multi-step scenarios:
  - "Create checkpoint → let Claude refactor → review → decide to merge or rollback"
  - "Create spec-driven branch → implement → validate → create PR with spec fulfillment"
  - "Setup .gitignore for Python project → commit → push to GitHub"
- [ ] T043 [L5] Create "Troubleshooting Prompts" conversation library:
  - "You: Git gave error 'CONFLICT in auth.py'" → "Agent: Let me explain conflict markers and guide resolution"
  - "You: Push rejected - remote has changes" → "Agent: You need to pull first. Here's how to merge..."
  - "You: I committed something I shouldn't have" → "Agent: Let's undo that commit safely"
- [ ] T044 [L5] Write "Best Practices for AI CLI Conversations" section:
  - Be specific: "Create branch for user authentication" not just "create branch"
  - Ask for explanations: "Do that AND explain each command"
  - Request safety checks: "Show me what will be committed first"
  - Use for learning: "Explain the checkpoint pattern in your own words"
- [ ] T045 [L5] Create comparison: When to use natural language (complex workflows, overwhelmed, learning) vs. direct commands (frequent operations, building muscle memory)
- [ ] T046 [L5] Write "Your Turn: Practice" with 6 prompts testing all prior lessons:
  - "Ask AI to explain checkpoint pattern in simple terms"
  - "Use natural language to create spec-driven branch"
  - "Request AI help to create validation commit for recent changes"
  - "Ask AI to show commit history in readable format"
  - "Get AI help understanding a merge conflict"
  - "Request AI guide for complex workflow: checkpoint → branch → implement → PR"
- [ ] T047 [L5] Add "Try With AI" section: "Ask your agent: 'I'm stuck with a Git error [paste error]. Explain what it means and help me fix it without losing my work'"

**Checkpoint**: Lesson 5 complete - learners can use AI as Git convenience layer while maintaining conceptual understanding

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final integration, validation, and consistency checks

- [ ] T048 Review all 5 lessons for conversational format consistency (every concept has "You → Agent → Output → Agent → Learned" pattern with 3+ repetitions)
- [ ] T049 Validate CEFR proficiency alignment across lessons: A1 (L1-L2) → A2 (L3-L5) progression maintains coherence
- [ ] T050 [P] Verify cognitive load limits: L1=3, L2=4, L3=4, L4=3, L5=2 concepts (all within A1 max 5, A2 max 7)
- [ ] T051 [P] Validate pattern recognition: "Checkpoint pattern" shown in 3 contexts (L2: basic, L3: branching, L5: natural language) with explicit call-outs
- [ ] T052 Cross-check all AIDD integration points:
  - Validation commit format appears in L2, L3, L4 examples
  - Specification-driven branching demonstrated in L3, L4
  - Checkpoint before AI shown in L2, L3, L5
  - PR as spec review in L4
- [ ] T053 [P] Verify all "Your Turn: Practice" sections have 3-5 copy-paste ready prompts
- [ ] T054 [P] Check all "Try With AI" sections follow policy: ChatGPT web (pre-tool) or AI CLI (post-tool chapters)
- [ ] T055 Validate reading level: Grade 7 baseline, technical terms defined on first use, no gatekeeping language ("obviously", "simply", "just")
- [ ] T056 Test cross-platform compatibility: All Git commands mentioned work on Windows/Mac/Linux (add platform notes where different)
- [ ] T057 [P] Verify GitHub workflows use free-tier features only
- [ ] T058 Update chapter README with completion summary: 5 lessons, 13 skills mapped, AIDD integration complete, ~4.5 hours total duration
- [ ] T059 Create end-of-chapter comprehensive project:
  - Title: "Build Your First AI-Assisted Feature with Git"
  - Requirements: Create repo → spec file → checkpoint → branch → implement with validation commits → PR with spec fulfillment → merge
  - Acceptance: All 6 user stories demonstrated in single project
- [ ] T060 [P] Add chapter-level resources:
  - Quick Reference Card: 10 core Git patterns
  - AIDD Cheat Sheet: Validation commit template, checkpoint pattern, spec-driven workflow
  - Troubleshooting Guide: 10 common errors with conversational solutions

---

## Dependencies & Execution Strategy

### Lesson Dependencies

```
Foundational Templates (T005-T008) — MUST complete first
    ↓
Lesson 1 (T009-T014) — Can start immediately after templates
    ↓ (establishes motivation)
Parallel Track 1          Parallel Track 2          Parallel Track 3
Lesson 2 (T015-T023)     [Can run in parallel]     [Can run in parallel]
    ↓                         ↓                         ↓
Lesson 3 (T024-T031)     Lesson 4 (T032-T039)     Lesson 5 (T040-T047)
    ↓                         ↓                         ↓
          Polish & Integration (T048-T060) — All lessons complete
```

**Parallel Opportunities**:
- After Lesson 1: Lessons 2, 4, and 5 content can be written simultaneously (different lessons, different files)
- Lesson 3 depends on Lesson 2 (builds on validation commit pattern)
- Polish tasks (T050-T060) can run in parallel once all lessons exist

### Story-to-Lesson Mapping

| User Story | Priority | Lesson(s) | Independent Test |
|------------|----------|-----------|------------------|
| **US1: Learning Through Conversation** | P1 | L1 (motivation), L2 (workflow) | Complete full Git workflow conversationally |
| **US2: Validation Commits** | P1 | L2 (introduction), L3-L4 (reinforcement) | Create validation commit with AI attribution + tests |
| **US3: Specification Branching** | P2 | L3 (spec-driven workflow) | Create spec file → branch → implement with validation |
| **US4: Checkpoint Pattern** | P2 | L2 (basic), L3 (before AI), L5 (natural language) | Create checkpoint → AI changes → validate → keep or rollback |
| **US5: PR as Spec Review** | P3 | L4 (complete workflow) | Create PR with spec fulfillment evidence |
| **US6: Troubleshooting** | P3 | L5 (error conversations) | Paste Git error → AI explains → guided resolution |

### Implementation Strategy

**MVP Scope** (Minimum Viable Chapter):
- Phase 1-2: Setup & Templates (T001-T008)
- Phase 3: Lesson 1 (T009-T014) — Motivation
- Phase 4: Lesson 2 (T015-T023) — Core workflow with AIDD validation

**This MVP delivers**:
- Conversational learning format established
- Core Git workflow taught (status, add, commit, log)
- AIDD validation pattern introduced
- Learners can make their first validation commit

**Incremental Additions**:
- **Iteration 2**: Add Lesson 3 (branching & checkpoints for safe AI experimentation)
- **Iteration 3**: Add Lesson 4 (GitHub PRs for team collaboration)
- **Iteration 4**: Add Lesson 5 (natural language convenience layer)
- **Final Polish**: Complete Phase 8 (consistency, resources, end-of-chapter project)

---

## Task Summary

**Total Tasks**: 60 tasks across 8 phases

**Task Distribution by Phase**:
- Phase 1 (Setup): 4 tasks
- Phase 2 (Foundation): 4 tasks (BLOCKING)
- Phase 3 (Lesson 1): 6 tasks
- Phase 4 (Lesson 2): 9 tasks
- Phase 5 (Lesson 3): 8 tasks
- Phase 6 (Lesson 4): 8 tasks
- Phase 7 (Lesson 5): 8 tasks
- Phase 8 (Polish): 13 tasks

**Parallel Opportunities**: 28 tasks marked [P] can run concurrently (47% of total)

**Critical Path**: Setup (4) → Foundation (4) → Lesson 1 (6) → Lesson 2 (9) → Lesson 3 (8) → Polish (13) = 44 sequential tasks

**Independent Tests per Story**:
- US1: Complete Git workflow conversationally ✓
- US2: Create validation commit with AI attribution ✓
- US3: Spec-driven branch with implementation ✓
- US4: Checkpoint → AI → validate → keep/rollback ✓
- US5: PR with spec fulfillment evidence ✓
- US6: Error troubleshooting with AI guidance ✓

**Estimated Effort** (for lesson-writer agent):
- Template creation: 2-3 hours
- Lesson 1: 4-5 hours (conceptual, requires strong narrative)
- Lesson 2: 6-8 hours (longest, includes installation + validation pattern)
- Lesson 3: 6-7 hours (branching complexity + AIDD workflows)
- Lesson 4: 5-6 hours (GitHub UI walkthrough + PR templates)
- Lesson 5: 4-5 hours (translations + troubleshooting scenarios)
- Polish: 4-5 hours (cross-cutting validation)
- **Total**: 31-41 hours for complete chapter implementation

---

## Success Criteria Validation

All 8 success criteria from spec mapped to tasks:

| SC | Requirement | Tasks | Validation Method |
|----|-------------|-------|-------------------|
| **SC-001** | Create repo in 5 min | T015-T023 (L2) | Exercise with timer |
| **SC-002** | Safe checkpoint + rollback | T024-T031 (L3) | Checkpoint → break → rollback exercise |
| **SC-003** | Branch workflow without loss | T024-T031 (L3) | Create → edit → merge exercise |
| **SC-004** | PR workflow | T032-T039 (L4) | Full GitHub PR exercise |
| **SC-005** | Translate 10+ commands | T040-T047 (L5) | Translation table + practice |
| **SC-006** | Understand when to commit | T015-T023 (L2), T045 (L5) | Reflection prompts |
| **SC-007** | End-of-chapter project | T059 (Polish) | Comprehensive project combining all skills |
| **SC-008** | 5 common scenarios | T032-T039 (L4), T040-T047 (L5) | Scenario-based exercises |

---

## Lesson Author Policy Notes

**Critical Requirements**:

1. **Conversational Format**: Every concept MUST use the 5-component pattern:
   - "You:" (learner request in natural language)
   - "Agent:" (AI explanation + commands if applicable)
   - "Tool Output:" (actual terminal output or conceptual explanation)
   - "Agent:" (clarification of what happened and why)
   - "What you learned:" (single-sentence reflection)
   - **Minimum**: 3 complete conversational exchanges per lesson

2. **"Try With AI" Section**: Each lesson MUST end with this single final section (NOT "Key Takeaways" or "What's Next"):
   - **Before Part 2 tool chapters**: Direct learners to ChatGPT web interface
   - **After Chapters 5-7**: Instruct to use preferred AI companion (Gemini CLI, Claude CLI)
   - **Provide**: Both CLI command examples AND web interface alternatives where applicable

3. **AIDD Integration**: All code/commit examples MUST demonstrate:
   - Validation commit format: `[AI] Tool - Feature\n\nEvals:\n- ✅ criteria\n\nTests: X/Y`
   - Checkpoint pattern before AI sessions (shown 3x minimum across chapter)
   - Specification-driven branching (spec file first commit)
   - PR descriptions showing spec fulfillment

4. **Cognitive Load**: Respect CEFR limits:
   - A1 lessons (L1-L2): Max 5 new concepts per lesson
   - A2 lessons (L3-L5): Max 7 new concepts per lesson
   - Pattern recognition: Show same pattern 3x in different contexts with explicit call-outs

5. **Accessibility**:
   - Grade 7 reading level baseline
   - Define technical terms on first use
   - No gatekeeping language ("obviously", "simply", "just")
   - Platform-specific notes for Windows/Mac/Linux where commands differ

6. **Skills Proficiency**: Each lesson has documented CEFR level and measurable indicators (see plan.md lines 622-726)
