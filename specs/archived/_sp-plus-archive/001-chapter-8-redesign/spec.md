# Feature Specification: Chapter 8 Redesign - Git & GitHub for AI-Driven Development (CoLearning Format)

**Feature Branch**: `08-redesign`
**Created**: 2025-11-05
**Status**: Draft
**Input**: User description: "create specs for chapter 8 using above pedagogical pattern"

## Overview

Redesign Chapter 8 (Git & GitHub for AI-Driven Development) using the **conversational CoLearning pedagogical pattern** where learners interact with AI agents to understand Git concepts through actual dialogue. This approach:

1. **Models real AI collaboration workflows** - Shows how learners would actually use AI tools
2. **Teaches validation thinking** - Demonstrates evals-first, specification-first patterns
3. **Reduces intimidation** - Git becomes a conversation, not a command to memorize
4. **Integrates AIDD principles** - Commits as validation evidence, branches as specifications

**Key Innovation**: Instead of "here's a command," learners see: "You ask → Agent executes → You learn the pattern → You understand WHY"

**Target Audience**: Beginners with no Git experience (Part 2, CEFR A1-A2)
**Estimated Duration**: 3-4 hours
**Reading Level**: Grade 7 baseline

---

## User Scenarios & Testing

### User Story 1 - Learning Git Through AI Conversation (Priority: P1)

A complete beginner wants to learn Git but finds traditional tutorials intimidating. They want to learn by asking an AI agent to help them create checkpoints, make commits, and understand what's happening through natural dialogue.

**Why this priority**: This is the foundational learning pattern for the entire chapter. If learners can't grasp Git through conversation, they won't complete any other scenarios.

**Independent Test**: Learner can complete a full Git workflow (create repo → make commits → create branch → merge) by conversing with AI agent, understanding each step.

**Acceptance Scenarios**:

1. **Given** a beginner with no Git knowledge, **When** they ask agent "Show me my current directory path" and "Create a git repository here", **Then** they see the agent execute commands, explain outputs, and understand that Git is now tracking their project
2. **Given** learner has uncommitted changes, **When** they ask "Save my work with a commit", **Then** agent guides them through staging and committing while explaining what each step does
3. **Given** learner asks "What's the pattern for starting new features?", **When** agent explains the three-step pattern (checkout main → pull → create branch), **Then** learner can articulate the pattern in their own words

---

### User Story 2 - Creating Validation-Driven Commits (AIDD Core) (Priority: P1)

A learner using Claude Code to generate authentication code wants to commit it properly with validation evidence, not just "Add auth." They want to document that the AI-generated code actually works.

**Why this priority**: This is the core AIDD pattern - commits document validation, not just code changes. This shifts learners from "save code" to "save evidence."

**Independent Test**: Learner can create a commit message that documents: (1) what AI generated, (2) validation evidence (tests, manual checks), (3) success criteria met.

**Acceptance Scenarios**:

1. **Given** Claude Code generated authentication code, **When** learner asks agent "How should I commit AI-generated code?", **Then** agent teaches the validation commit pattern: `[AI] Tool - Feature\n\nEvals:\n- ✅ Success criteria\n\nTests: X/Y passing`
2. **Given** learner tested code and all tests pass, **When** they create commit with validation evidence, **Then** future reviewers can see exactly what was validated
3. **Given** learner reviews commit history, **When** they see validation commits, **Then** they understand which features work and what was tested

---

### User Story 3 - Specification-Driven Branching (AIDD Pattern) (Priority: P2)

A learner wants to implement a payment feature using AIDD. They want to create a specification first, then use Git branches to track progress against that spec.

**Why this priority**: Bridges Git mechanics to specification-first development. Teaches that branches represent specifications, not just isolated work.

**Independent Test**: Learner can create a spec file in a feature branch, commit it, then implement against it with validation commits.

**Acceptance Scenarios**:

1. **Given** learner needs to build payment processing, **When** they ask agent "How should I organize this with Git using AIDD?", **Then** agent guides: spec first, then branch named after spec
2. **Given** spec is committed in feature branch, **When** learner asks AI to implement it, **Then** implementation commits reference spec and include validation against spec criteria
3. **Given** feature is complete, **When** learner creates PR, **Then** PR description shows: Specification → Implementation → Validation evidence

---

### User Story 4 - Checkpoints Before AI Sessions (Safety Pattern) (Priority: P2)

A learner wants Claude Code to refactor their code but fears it might break something. They want to create a safe checkpoint they can return to if AI changes don't work.

**Why this priority**: Essential safety pattern for AI-driven development. Without this, learners won't trust AI tools with significant changes.

**Independent Test**: Learner creates checkpoint commit, lets AI make changes, validates, and either keeps changes or rolls back.

**Acceptance Scenarios**:

1. **Given** learner has working code, **When** they ask "Create a safe checkpoint before AI refactoring", **Then** agent guides: commit current state, note commit hash, verify rollback path
2. **Given** AI refactored code, **When** tests fail, **Then** learner can roll back to checkpoint: `git reset --hard <hash>`
3. **Given** AI changes work, **When** learner commits with validation, **Then** checkpoint commit remains in history as reference point

---

### User Story 5 - Pull Requests as Spec Reviews (Collaboration) (Priority: P3)

A learner completed a feature and wants to create a PR that shows specification fulfillment, not just code changes. They want teammates to review against requirements.

**Why this priority**: Professional workflow pattern. Important for teams but not essential for solo learners initially.

**Independent Test**: Learner creates PR with description showing: spec → implementation → validation → spec fulfillment checklist.

**Acceptance Scenarios**:

1. **Given** feature branch complete with validation commits, **When** learner asks "How do I create a PR showing spec fulfillment?", **Then** agent generates PR template with spec reference, implementation summary, validation evidence
2. **Given** reviewer sees PR, **When** they read description, **Then** they can verify each spec requirement was met without digging through commits
3. **Given** reviewer requests changes, **When** learner updates and pushes, **Then** PR automatically updates and shows iterative validation

---

### User Story 6 - Troubleshooting Through Conversation (Error Handling) (Priority: P3)

A learner encounters merge conflicts or Git errors. Instead of getting stuck, they want to ask AI agent "What does this error mean?" and get guided resolution.

**Why this priority**: Reduces Git fear and dropout. Ensures learners don't abandon Git when errors occur.

**Independent Test**: Learner can paste Git error to agent, understand the cause, and execute resolution steps with guidance.

**Acceptance Scenarios**:

1. **Given** learner sees "CONFLICT (content): Merge conflict in auth.py", **When** they ask agent "What is this and how do I fix it?", **Then** agent explains conflict markers, shows conflicted section, guides resolution
2. **Given** learner gets "rejected push" error, **When** they share error with agent, **Then** agent diagnoses (remote has changes) and guides: pull → merge/rebase → push
3. **Given** learner asks "How do I undo my last commit?", **When** agent explains --soft vs --hard vs --mixed, **Then** learner chooses appropriate option and understands implications

---

### Edge Cases

- **What happens when learner asks agent to commit but has no changes staged?** Agent detects with `git status`, explains staging area, guides `git add` before commit
- **What if learner accidentally commits secrets (API keys in .env)?** Agent checks for common secret patterns before commit, warns, guides `.gitignore` creation
- **How does agent handle when learner wants to merge but has uncommitted changes?** Agent detects dirty working directory, explains commit or stash options
- **What if learner creates branch with poor naming (e.g., "test" or "fix")?** Agent suggests specification-based naming: `feature/spec-description`
- **What happens when learner's commit message is vague ("update code")?** Agent prompts for validation evidence: "What did you change? Did you test it? What works now?"
- **How does system handle when learner tries destructive operations (--hard reset, force push)?** Agent asks confirmation: "This deletes changes permanently. Do you have a backup? Are you sure?"

---

## Requirements

### Functional Requirements - Chapter Structure

- **FR-001**: Chapter MUST use conversational CoLearning format for ALL sections: "You: [request]" → "Agent: [action/explanation]" → "Tool Output: [result]" → "Agent: [interpretation]"
- **FR-002**: Each new Git concept MUST follow learning pattern: User asks WHAT → Agent shows HOW (command/syntax) → "What you learned:" reflection
- **FR-003**: Chapter MUST include "Your Turn: Practice" sections after each major concept with 3-5 prompts learners can try
- **FR-004**: All Git operations MUST be demonstrated through AI agent conversation, not as standalone commands
- **FR-005**: Chapter MUST integrate AIDD principles: validation commits, specification branches, evals-first thinking

### Functional Requirements - Git Concepts (Conversational Format)

- **FR-006**: Chapter MUST teach repository initialization through conversation: "You: Create a git repository" → "Agent: Tool → Shell $ git init"
- **FR-007**: Chapter MUST teach validation commit pattern: AI-generated code + tests passing + manual validation = complete commit message
- **FR-008**: Chapter MUST teach specification-driven branching: spec file created first, branch named after spec, commits validate against spec
- **FR-009**: Chapter MUST teach checkpoint pattern: commit before AI session, note hash, validate after, rollback if needed
- **FR-010**: Chapter MUST teach pull requests as spec reviews: PR description shows spec → implementation → validation proof
- **FR-011**: Chapter MUST demonstrate merge conflict resolution through guided agent conversation, not abstract examples
- **FR-012**: Chapter MUST teach `.gitignore` creation through conversation when learner asks to commit project files

### Functional Requirements - AIDD Integration

- **FR-013**: Every commit example MUST include validation evidence section: "Evals:\n- ✅ Success criterion\n\nTests: X/Y passing"
- **FR-014**: Chapter MUST show branch naming convention: `feature/[spec-id]-description` or `feature/[feature-name]`
- **FR-015**: Chapter MUST demonstrate how to document AI contributions: `[AI] <Tool-Name> - <Feature>` prefix in commits
- **FR-016**: Chapter MUST show how to review AI-generated code before committing: run tests, manual validation, security check
- **FR-017**: Chapter MUST teach learners to ask "Does this meet the specification?" before committing

### Functional Requirements - Cognitive Load (Part 2 Beginners)

- **FR-018**: Chapter MUST introduce maximum 8-10 core Git patterns, not 20+ commands (A1-A2 cognitive load limit)
- **FR-019**: Each lesson section MUST introduce maximum 5 new concepts (cognitive load threshold for beginners)
- **FR-020**: Chapter MUST use "Your agent chooses..." framing when multiple equivalent commands exist (don't overwhelm with options)
- **FR-021**: Chapter MUST include "What you learned:" reflections after each conversation to reinforce pattern recognition
- **FR-022**: Chapter MUST provide ready-to-use prompts learners can copy-paste: "Try asking your agent: 'Show me my commit history'"

### Functional Requirements - Platform Integration

- **FR-023**: Conversational examples MUST work with Claude Code, Gemini CLI, and generic AI agents (not tool-specific)
- **FR-024**: Chapter MUST reference Chapters 5-7 (Claude Code, Gemini CLI, Bash) to show integrated workflow
- **FR-025**: Chapter MUST forward-bridge to Part 3 (Prompt Engineering): "You'll learn advanced prompting in Chapter 10"
- **FR-026**: All Git commands in agent responses MUST work on Windows, Mac, and Linux

### Key Entities

- **Git Repository**: Version-controlled project directory
  - Attributes: working directory, staging area, commit history, branches, remotes
  - Representation in conversation: "Agent: Tool → Shell $ git init" creates repository

- **Validation Commit**: Commit with evidence that code works
  - Attributes: AI attribution, success criteria checked, tests passed, manual validation performed
  - Format: `[AI] Tool - Feature\n\nEvals:\n- ✅ criteria\n\nTests: X/Y passing`

- **Specification Branch**: Feature branch named after specification
  - Attributes: spec file (first commit), implementation commits (with validation), PR (spec review)
  - Naming: `feature/[spec-name]` or `feature/[spec-id]-description`

- **Checkpoint Commit**: Safe state before AI modifications
  - Attributes: commit message indicating "Checkpoint before...", hash noted for rollback
  - Purpose: Safety net for AI-assisted refactoring or generation

- **Conversational Exchange**: Learning unit in CoLearning format
  - Attributes: User request → Agent action → Tool output → Agent explanation → Learner reflection
  - Purpose: Models real AI collaboration, teaches pattern recognition

---

## Success Criteria

### Measurable Outcomes - Learning

- **SC-001**: 90%+ of learners complete first Git repository creation through AI conversation within 5 minutes
- **SC-002**: Learners can create validation commit (AI attribution + test evidence) without template after 3 guided examples
- **SC-003**: 85%+ of learners can articulate "checkpoint before AI session" pattern in their own words after Chapter 8
- **SC-004**: Learners successfully create specification-driven branch (spec first, then implementation) in end-of-chapter project
- **SC-005**: 80%+ of learners can troubleshoot common Git errors by asking AI agent conversationally
- **SC-006**: Learners demonstrate understanding of "validation-driven commits" by checking tests before committing in exercises

### Measurable Outcomes - AIDD Adoption

- **SC-007**: Commit messages in learner exercises include validation evidence (tests + manual checks) 75%+ of the time
- **SC-008**: Learners create checkpoint commits before AI sessions in 90%+ of guided exercises
- **SC-009**: End-of-chapter PR includes: spec reference, validation evidence, spec fulfillment checklist (100% of submitted projects)
- **SC-010**: Learners can explain "specification-first branching" pattern to a peer (assessed via self-reflection)

### Measurable Outcomes - Engagement

- **SC-011**: Chapter completion rate matches or exceeds Chapter 7 (Bash) completion rate (target: 85%+)
- **SC-012**: Learner feedback indicates Git is "less intimidating" than traditional tutorials (qualitative survey)
- **SC-013**: Learners attempt "Your Turn: Practice" exercises at 70%+ rate (tracked if analytics available)
- **SC-014**: Zero dropout due to "Git is too hard" in conversational format (qualitative feedback)

---

## Scope

### In Scope - Conversational Learning Format

- CoLearning dialogue format for all concepts: "You: [ask]" → "Agent: [guide]" → "What you learned:"
- Pattern-based learning: Show command 3x in conversations → Learner recognizes pattern → Internalize, don't memorize
- "Your Turn: Practice" sections with copy-paste prompts
- "What you learned:" reflections after each conversation
- Error troubleshooting through conversational guidance

### In Scope - Git Concepts (Simplified for Part 2)

- Repository creation and status checking (conversational)
- Validation commits with AI attribution and test evidence
- Checkpoint commits before AI sessions
- Specification-driven branches (spec file first)
- Merge workflow (with conflict resolution through conversation)
- Pull requests as spec reviews
- `.gitignore` for AI projects (when learner tries to commit secrets)

### In Scope - AIDD Integration

- Evals-first thinking: "What should work?" before "Did AI generate it?"
- Specification commits (first commit in feature branch)
- Validation commit format: `[AI] Tool - Feature\n\nEvals:\n- ✅\n\nTests: X/Y`
- Checkpoint pattern: commit → note hash → AI session → validate → keep or rollback
- Branch naming: `feature/spec-name`
- PR as spec review: description shows spec fulfillment

### Out of Scope

- Advanced Git commands (rebase, cherry-pick, bisect, reflog) - too complex for A1-A2
- Git internals or data structures (blobs, trees, refs) - not needed for usage
- GitHub Actions, CI/CD, or automation - covered in later parts
- Team workflow policies, branching strategies (GitFlow) - too advanced
- Git performance optimization or large repository management
- Alternative version control systems (Mercurial, SVN)
- Git GUIs or visual tools - focus on CLI for AI tool consistency

### Assumptions

1. Learners completed Chapters 5-7 (Claude Code, Gemini CLI, Bash) and understand terminal basics
2. Learners have Claude Code or Gemini CLI installed and authenticated
3. Learners have or will create free GitHub account (all features work on free tier)
4. Learners have internet access for GitHub operations
5. Learners are comfortable asking questions conversationally (not intimidated by AI)
6. Learners have at least one small project directory to practice Git (from previous chapters)

### Dependencies

- **Prerequisite Chapters**: 5 (Claude Code), 6 (Gemini CLI), 7 (Bash Essentials)
- **External Tools**: Git CLI, GitHub account, AI CLI tool (Claude Code or Gemini CLI)
- **Platform Requirements**: Windows 10+, macOS 10.15+, or modern Linux
- **Network Access**: Required for GitHub push/pull operations

### Constraints

- **Time Constraint**: 3-4 hours completion time (same as current Chapter 8)
- **Complexity Constraint**: Maximum 8-10 core patterns, 5 new concepts per section (A1-A2 cognitive load)
- **Format Constraint**: ALL content must use conversational CoLearning format (no command lists without dialogue)
- **Tool Constraint**: Examples must work with Claude Code and Gemini CLI
- **Platform Constraint**: All commands must work cross-platform (Windows/Mac/Linux)
- **Reading Level**: Grade 7 baseline, no unexplained jargon

---

## Non-Goals

- Teaching Git as a standalone tool (it's taught through AI agent conversations)
- Covering every Git command or flag (focus on 8-10 patterns learners will actually use)
- Replacing traditional Git tutorials (this is AIDD-focused Git learning)
- Teaching professional Git workflows beyond basic AIDD patterns
- Deep technical understanding of Git internals
- Preparing learners for Git certification exams
- Teaching Git history or version control theory

---

## Risks and Mitigations

### Risk 1: Learners rely too much on AI without understanding Git concepts (HIGH IMPACT)

**Impact**: Learners can execute Git operations conversationally but can't explain what's happening or troubleshoot independently.

**Mitigation**:
- Include "What you learned:" reflections after every conversation showing the pattern
- Require learners to articulate patterns in self-assessments: "The checkpoint pattern is: ___"
- Design exercises where learners explain concepts to peers or in writing
- Show same pattern 3 times in different contexts so learners recognize it
- Include quiz questions testing conceptual understanding, not command memorization

### Risk 2: Conversational format makes content too long/verbose (MEDIUM IMPACT)

**Impact**: Chapter becomes 2x longer than current version, overwhelming learners with reading.

**Mitigation**:
- Keep conversations concise: 3-5 exchanges per concept maximum
- Use "Tool Output:" format to show results inline without lengthy explanations
- Remove redundant explanations (show pattern once, reference it later: "Remember the checkpoint pattern?")
- Balance conversation with traditional prose for overviews and summaries
- Target same 3-4 hour completion time as current chapter

### Risk 3: Examples don't work across different AI agents (MEDIUM IMPACT)

**Impact**: Learner uses AI tool that responds differently than examples, causing confusion.

**Mitigation**:
- Use generic "Agent:" label, not "Claude Code:" or "Gemini CLI:" (works for any agent)
- Test examples with Claude Code, Gemini CLI, and ChatGPT to ensure portability
- Teach prompts that work universally: "Show me...", "Create...", "What does this mean?"
- Include troubleshooting: "If your agent responds differently, ask: 'Explain this command'"
- Focus on learner prompts (which are tool-agnostic), not exact agent responses

### Risk 4: Learners skip "Your Turn: Practice" exercises (MEDIUM IMPACT)

**Impact**: Passive reading without hands-on practice, poor retention.

**Mitigation**:
- Make practice prompts extremely easy to try (copy-paste ready)
- Include immediate feedback mechanism: "After trying, check: Did your agent..."
- Embed practice exercises inline after concepts, not at end of chapter (when motivation wanes)
- Tie end-of-chapter project to practice exercises: "You'll need the checkpoint pattern from Practice #2"
- Use engaging scenarios: "Try this with your actual project from Chapter 5"

### Risk 5: Validation commit format feels bureaucratic to beginners (LOW-MEDIUM IMPACT)

**Impact**: Learners see validation evidence as unnecessary overhead, revert to "Add feature" messages.

**Mitigation**:
- Show realistic scenario where validation commit saved the day (debugging, code review)
- Start with minimal validation format, expand gradually: Level 1 (AI tag) → Level 2 (+ tests) → Level 3 (+ manual checks)
- Demonstrate value: "Your teammate can see tests passed without asking" or "Future you knows what works"
- Make template available: Learners fill in blanks rather than writing from scratch
- Praise good validation commits in examples: "This is an excellent commit message because..."

---

## Validation Criteria

### Content Validation

- [ ] All sections use conversational CoLearning format consistently
- [ ] Each new concept includes: Conversation → "What you learned:" → "Your Turn: Practice"
- [ ] Git operations demonstrated through agent dialogue, not standalone commands
- [ ] AIDD patterns (validation commits, spec branches, checkpoints) integrated throughout
- [ ] Examples tested with Claude Code and Gemini CLI (ensure portability)
- [ ] Cognitive load limits enforced: max 8-10 patterns, max 5 concepts per section
- [ ] All commands work cross-platform (Windows/Mac/Linux)

### Pedagogical Validation

- [ ] Chapter follows graduated complexity guidelines (Part 2 = A1-A2 tier)
- [ ] Content meets Grade 7 reading level baseline
- [ ] No gatekeeping language ("obviously", "simply", "just type")
- [ ] Pattern recognition reinforced: same pattern shown 3x in different contexts
- [ ] Reflections prompt learners to articulate understanding in their own words
- [ ] Error scenarios include conversational troubleshooting (not just "here's the fix")
- [ ] Exercises are immediately actionable (copy-paste prompts provided)

### AIDD Alignment Validation

- [ ] All commit examples include validation evidence (tests, manual checks, security)
- [ ] Specification-first workflow demonstrated: spec commit → implementation → validation
- [ ] Evals-first thinking modeled: "What should work?" before committing
- [ ] AI collaboration shown as iterative: checkpoint → generate → validate → commit or rollback
- [ ] PR examples show spec fulfillment, not just code changes
- [ ] Chapter bridges to Part 5 (Spec-Driven Development) concepts

### Engagement Validation

- [ ] Conversational format feels natural, not forced or artificial
- [ ] Examples use realistic scenarios from AI-driven development
- [ ] Learner reflection prompts are thought-provoking, not busywork
- [ ] "Your Turn: Practice" exercises are genuinely useful, not just checkbox activities
- [ ] Content reduces Git intimidation (language, analogies, reassurance)
- [ ] Chapter ending motivates continuation: "You're now ready to..."

---

## Open Questions / Clarifications Needed

[NONE - Spec is complete based on clear user input and reference examples provided]

