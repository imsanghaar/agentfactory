# Tasks: Linux Mastery for Digital FTEs

**Input**: Design documents from `/specs/001-linux-mastery/`
**Prerequisites**: plan.md, spec.md
**Chapter Type**: Educational Content (Technical/Code-Focused)

**Tests**: No automated tests - assessments are hands-on exercises and chapter quiz

**Organization**: Tasks are grouped by lesson to enable systematic chapter creation with proper skill invocations and validation gates.

## Format: `[ID] [P?] [Lesson] Description`

- **[P]**: Can run in parallel (different lessons, no dependencies)
- **[Lesson]**: Which lesson this task belongs to (L01, L02, L03, etc.)
- All lesson tasks use content-implementer subagent with educational-validator gate
- Skills invoked: learning-objectives, exercise-designer, ai-collaborate-teaching (L2+)

## Content Task Template (All Lesson Tasks)

Each lesson task follows this pattern:

```markdown
- [ ] T0XX [P] [L0Z] Lesson Z: [Title]
  - **Skill: learning-objectives**: Generate measurable outcomes (Bloom's, CEFR, assessment)
  - **Skill: exercise-designer**: Create 3 deliberate practice exercises
  - **Skill: ai-collaborate-teaching**: Design Three Roles sections (if L2+)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/[part]/[chapter]/[lesson].md
    - Execute autonomously without confirmation
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-version-control/01-your-first-git-repository.md
    - Returns confirmation only (~50 lines), NOT full content
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring (6 categories)
```

---

## Phase 1: Chapter Setup

**Purpose**: Initialize chapter directory and README

- [x] T001 Create chapter directory structure at `apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/`
- [x] T002 Create chapter README.md with title, description, principles, lessons table, and connection to Digital FTE vision
- [x] T003 Set chapter metadata: sidebar_position=10, title="Chapter 10: Linux Mastery for Digital FTEs"

**Checkpoint**: Chapter directory ready for lesson creation ✅

---

## Phase 2: Foundation Lessons (Layer 1: Manual Foundation)

**Purpose**: Build CLI mindset and environment setup WITHOUT AI assistance

### Lesson 1: The CLI Architect Mindset

- [x] T004 [P] [L01] Lesson 1: The CLI Architect Mindset
  - **Skill: learning-objectives**: Generate 5 measurable outcomes for CLI mindset (Understand, B1)
  - **Skill: exercise-designer**: Create 3 practice exercises (filesystem navigation, path understanding, CLI vs GUI analysis)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/01-cli-architect-mindset.md
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-version-control/01-your-first-git-repository.md
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring

### Lesson 2: Modern Terminal Environment

- [x] T005 [P] [L02] Lesson 2: Modern Terminal Environment
  - **Skill: learning-objectives**: Generate 5 measurable outcomes for environment setup (Apply, B1)
  - **Skill: exercise-designer**: Create 3 hands-on exercises (package installation, zoxide setup, fzf integration)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/02-modern-terminal-environment.md
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-version-control/02-viewing-changes-safe-undo.md
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring

**Checkpoint**: Foundation complete - students ready for AI collaboration (Layer 2)

---

## Phase 3: Core Agent Operations (Layer 2: AI Collaboration)

**Purpose**: Hands-on practice with tmux, scripting, and security using AI Three Roles

### Lesson 3: Persistent Sessions with tmux

- [x] T006 [P] [L03] Lesson 3: Persistent Sessions with tmux
  - **Skill: learning-objectives**: Generate 4 measurable outcomes for tmux (Apply, B1)
  - **Skill: exercise-designer**: Create 3 practice exercises (session creation, pane splitting, persistence testing)
  - **Skill: ai-collaborate-teaching**: Design Three Roles sections (AI suggests layouts, student teaches SSH constraints, co-worker iteration)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/03-persistent-sessions-tmux.md
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-version-control/03-testing-ai-safely-with-branches.md
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring

### Lesson 4: Bash Scripting for Agent Automation

- [x] T007 [P] [L04] Lesson 4: Bash Scripting for Agent Automation
  - **Skill: learning-objectives**: Generate 5 measurable outcomes for bash scripting (Apply, B1)
  - **Skill: exercise-designer**: Create 3 practice exercises (shebang/permissions, variables/interpolation, error handling)
  - **Skill: ai-collaborate-teaching**: Design Three Roles sections (AI teaches error handling, student teaches deployment constraints, co-worker script refinement)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/04-bash-scripting-agent-automation.md
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-version-control/06-reusable-git-patterns.md
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring

### Lesson 5: Security Hardening & Least Privilege

- [x] T008 [P] [L05] Lesson 5: Security Hardening & Least Privilege
  - **Skill: learning-objectives**: Generate 5 measurable outcomes for security (Apply, B2)
  - **Skill: exercise-designer**: Create 3 practice exercises (user creation, permission management, SSH key setup)
  - **Skill: ai-collaborate-teaching**: Design Three Roles sections (AI teaches least privilege, student teaches compliance, co-worker permissions iteration)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/05-security-hardening-least-privilege.md
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/06-AI-Cloud-Native-Development/58-production-security/01-production-security-overview.md (if exists)
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring

**Checkpoint**: Core operations complete - students can manage agents securely

---

## Phase 4: Process Control & Troubleshooting (Layer 2→3)

**Purpose**: Production operations and debugging skills with intelligence creation

### Lesson 6: Process Control with systemd

- [x] T009 [P] [L06] Lesson 6: Process Control with systemd
  - **Skill: learning-objectives**: Generate 4 measurable outcomes for systemd (Apply, B2)
  - **Skill: exercise-designer**: Create 3 practice exercises (service file creation, restart testing, boot verification)
  - **Skill: ai-collaborate-teaching**: Design Three Roles sections (AI teaches restart policies, student teaches dependencies, co-worker service refinement)
  - **INTELLIGENCE CREATION**: Document deployment-automation skill (systemd template, deployment checklist)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/06-process-control-systemd.md
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/06-AI-Cloud-Native-Development/50-kubernetes-for-ai-services/01-kubernetes-fundamentals.md (if exists)
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring

### Lesson 7: Debugging & Troubleshooting

- [x] T010 [P] [L07] Lesson 7: Debugging & Troubleshooting
  - **Skill: learning-objectives**: Generate 5 measurable outcomes for debugging (Analyze, B2)
  - **Skill: exercise-designer**: Create 3 diagnostic exercises (log analysis, network debugging, process troubleshooting)
  - **Skill: ai-collaborate-teaching**: Design Three Roles sections (AI teaches diagnostic methodology, student describes failure symptoms, co-worker systematic diagnosis)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/07-debugging-troubleshooting.md
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/06-AI-Cloud-Native-Development/55-observability-cost-engineering/01-observability-overview.md (if exists)
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring

**Checkpoint**: Process control complete - students can deploy and debug agents

---

## Phase 5: Mastery & Capstone (Layer 3→4)

**Purpose**: Create reusable intelligence and deploy production Digital FTE

### Lesson 8: Advanced Workflow Integration

- [x] T011 [P] [L08] Lesson 8: Advanced Workflow Integration
  - **Skill: learning-objectives**: Generate 4 measurable outcomes for workflow synthesis (Evaluate, B2-C1)
  - **Skill: exercise-designer**: Create 3 integration exercises (pattern evaluation, skill testing, scenario application)
  - **INTELLIGENCE CREATION**: Create linux-agent-ops skill (Persona + Questions + Principles pattern)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/08-advanced-workflow-integration.md
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/05-Building-Custom-Agents/46-tdd-for-agents/01-tdd-agentic-foundation.md (if exists)
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring

### Lesson 9: Capstone - Production Digital FTE Deployment

- [x] T012 [P] [L09] Lesson 9: Capstone - Production Digital FTE Deployment
  - **Skill: learning-objectives**: Generate 5 measurable outcomes for capstone (Create, C1)
  - **Skill: exercise-designer**: Create 3 deployment exercises (spec writing, AI orchestration, validation)
  - **CAPSTONE**: Specification-first methodology (spec BEFORE implementation)
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/09-capstone-production-deployment.md
    - Reference lesson: /mnt/g/voice_learning/book_project/apps/learn-app/docs/07-Turing-LLMOps-Proprietary-Intelligence/72-capstone-end-to-end-llmops/01-capstone-overview.md (if exists)
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)
  - **Skill: content-evaluation-framework**: Quality rubric scoring

**Checkpoint**: Capstone complete - Digital FTE deployed

---

## Phase 6: Chapter Assessment

**Purpose**: Validate student learning with comprehensive quiz

- [x] T013 Create Chapter Quiz with assessment-architect skill
  - **Skill: assessment-architect**: Generate 50-question interactive quiz covering all 6 topics
  - Mix of multiple-choice, scenario-based, and practical exercises
  - Target: 85%+ completion rate, 80%+ average score (SC-010)
  - Output: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/10-chapter-quiz.md
  - **SUBAGENT**: content-implementer
    - Output path: /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/10-chapter-quiz.md
    - Execute autonomously without confirmation
    - Returns confirmation only
  - **VALIDATION**: educational-validator (MUST PASS before marking complete)

**Checkpoint**: Chapter complete - ready for publication

---

## Phase 7: Polish & Cross-Cutting

**Purpose**: Final improvements and validation

- [x] T014 [P] Create lesson summary files using summary-generator skill
  - Generate .summary.md for each lesson (L01-L09)
  - Extract key concepts, mental models, patterns, common mistakes
- [x] T015 Run fact-check-lesson skill on all lessons
  - Verify all technical claims (commands, options, file paths)
  - Ensure no hallucinated facts
- [x] T016 Run technical-clarity skill on all lessons
  - Validate accessibility and jargon density
  - Ensure content passes "Grandma Test"
- [x] T017 Update chapter-index.md with Chapter 10 entry
  - Add chapter number, title, part location
- [x] T018 Final validation: Run educational-validator on entire chapter
  - All lessons must pass 6-gate review process
- [x] T019 Create summary files for any missing lessons using summary-generator skill

---

## Dependencies & Execution Order

### Phase Dependencies

- **Chapter Setup (Phase 1)**: No dependencies - can start immediately
- **Foundation Lessons (Phase 2)**: No dependencies - can start after Chapter Setup
- **Core Operations (Phase 3)**: Depends on Foundation Lessons (Layer 1 → Layer 2 progression)
- **Process Control (Phase 4)**: Depends on Core Operations (conceptual dependencies)
- **Mastery & Capstone (Phase 5)**: Depends on all previous lessons (accumulated intelligence)
- **Chapter Assessment (Phase 6)**: Depends on all lessons complete
- **Polish (Phase 7)**: Depends on all content complete

### Lesson Dependencies

- **Lesson 1 (L01)**: No dependencies - starts chapter
- **Lesson 2 (L02)**: No dependencies - parallel with L01
- **Lessons 3-5 (L03-L05)**: Depend on L01-L02 (require Layer 1 foundation)
- **Lessons 6-7 (L06-L07)**: Depend on L03-L05 (build on core operations)
- **Lesson 8 (L08)**: Depends on L01-L07 (synthesizes all patterns)
- **Lesson 9 (L09)**: Depends on L01-L08 (capstone integration)

### Parallel Opportunities

**After Chapter Setup**:
- L01 and L02 can run in parallel
- After L01-L02: L03, L04, L05 can run in parallel
- After L03-L05: L06 and L07 can run in parallel
- After L06-L07: L08 (requires all previous)
- After L08: L09 (capstone)

**Example**: Launch L03, L04, L05 together after foundation complete

```bash
# Three lesson tasks running in parallel:
Task T006: Lesson 3 (tmux)
Task T007: Lesson 4 (bash scripting)
Task T008: Lesson 5 (security)
```

---

## Implementation Strategy

### Sequential Lesson Creation

1. Complete Phase 1: Chapter Setup
2. Complete Phase 2: Foundation Lessons (L01, L02)
3. Complete Phase 3: Core Operations (L03, L04, L05)
4. Complete Phase 4: Process Control (L06, L07)
5. Complete Phase 5: Mastery (L08, L09)
6. Complete Phase 6: Assessment (Quiz)
7. Complete Phase 7: Polish

### Parallel Lesson Creation (Recommended)

With multiple content-implementer instances:

1. Team completes Chapter Setup together
2. Create L01 and L02 in parallel
3. After L01-L02 validated, create L03-L05 in parallel
4. After L03-L05 validated, create L06-L07 in parallel
5. Create L08 (synthesis requires all patterns)
6. Create L09 (capstone)
7. Complete Quiz and Polish phases

### Quality Gates

Each lesson MUST pass:

1. **Skill Invocations**: learning-objectives, exercise-designer, ai-collaborate-teaching (L2+)
2. **Subagent Creation**: content-implementer with reference lesson
3. **Validation Gate**: educational-validator (6-gate review)
4. **Quality Scoring**: content-evaluation-framework (6-category rubric)

**No lesson proceeds to下一个 without passing validation**

---

## Notes

- [P] tasks = different lessons (after foundation), can run in parallel
- [L0Z] label maps task to specific lesson for traceability
- Each lesson uses content-implementer subagent (returns confirmation only, NOT full content)
- educational-validator gate MUST PASS before marking lesson complete
- Safety warnings required for all dangerous operations (sudo, rm -rf, chmod 777, kill -9, SSH)
- All examples must use realistic agent deployment scenarios
- Progressive complexity: B1 → B2 → C1 across lessons

---

**Document Version**: 1.0.0
**Last Updated**: 2026-02-08
**Total Tasks**: 19
**Estimated Implementation Time**: 15-20 hours
