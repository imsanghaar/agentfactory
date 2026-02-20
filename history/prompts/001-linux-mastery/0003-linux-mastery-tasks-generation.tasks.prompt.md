---
id: "0003"
title: "linux-mastery-tasks-generation"
stage: "tasks"
date: "2026-02-08T01:05:00Z"
surface: "cli"
model: "claude-opus-4-6"
feature: "001-linux-mastery"
branch: "001-linux-mastery"
user: "unknown"
command: "/sp.tasks"
labels: ["chapter", "linux", "educational-content", "task-generation"]
links:
  spec: "../../specs/001-linux-mastery/spec.md"
  plan: "../../specs/001-linux-mastery/plan.md"
  tasks: "../../specs/001-linux-mastery/tasks.md"
  ticket: ""
  adr: ""
  pr: ""
files:
  - path: "specs/001-linux-mastery/tasks.md"
    status: "created"
  - path: "specs/001-linux-mastery/plan.md"
    status: "referenced"
  - path: "specs/001-linux-mastery/spec.md"
    status: "referenced"
tests: []

## Prompt

/sp.tasks

User requested generation of complete task breakdown for Linux Mastery chapter following the specification and plan created in previous sessions.

## Response snapshot

Generated comprehensive tasks.md with 19 tasks organized in 7 phases covering chapter setup, 9 lessons, assessment, and polish.

**Task Organization**:

**Phase 1: Chapter Setup** (3 tasks)
- T001-T003: Directory creation, README, metadata setup

**Phase 2: Foundation Lessons** (2 lessons - Layer 1)
- T004: Lesson 1 - CLI Architect Mindset (learning-objectives, exercise-designer, content-implementer, educational-validator, content-evaluation-framework)
- T005: Lesson 2 - Modern Terminal Environment (same skill pipeline)

**Phase 3: Core Agent Operations** (3 lessons - Layer 2 AI Collaboration)
- T006: Lesson 3 - tmux sessions (+ ai-collaborate-teaching skill)
- T007: Lesson 4 - Bash scripting (+ ai-collaborate-teaching skill)
- T008: Lesson 5 - Security hardening (+ ai-collaborate-teaching skill)

**Phase 4: Process Control & Troubleshooting** (2 lessons - Layer 2→3)
- T009: Lesson 6 - systemd (+ intelligence creation: deployment-automation skill)
- T010: Lesson 7 - Debugging (+ ai-collaborate-teaching skill)

**Phase 5: Mastery & Capstone** (2 lessons - Layer 3→4)
- T011: Lesson 8 - Advanced Integration (creates linux-agent-ops skill)
- T012: Lesson 9 - Capstone (specification-first Digital FTE deployment)

**Phase 6: Chapter Assessment** (1 task)
- T013: Chapter Quiz with assessment-architect skill (50 questions, 85%+ completion target)

**Phase 7: Polish** (6 tasks)
- T014: Summary files (summary-generator skill)
- T015: Fact-checking (fact-check-lesson skill)
- T016: Technical clarity (technical-clarity skill)
- T017: Update chapter-index.md
- T018: Final validation (educational-validator)
- T019: Missing summaries

**Content Task Template Applied**:

Each lesson task includes:
1. **Skill: learning-objectives** - Generate measurable outcomes (Bloom's, CEFR, assessment)
2. **Skill: exercise-designer** - Create 3 deliberate practice exercises
3. **Skill: ai-collaborate-teaching** - Design Three Roles sections (Layer 2+ only)
4. **SUBAGENT: content-implementer** - Write lesson to absolute path, return confirmation only (~50 lines)
5. **VALIDATION: educational-validator** - Read from disk, MUST PASS before complete
6. **Skill: content-evaluation-framework** - 6-category quality rubric scoring

**Key Features**:

- Total 19 tasks across 7 phases
- All lessons follow content work template with skill invocations
- Direct-write protocol: content-implementer returns confirmation only, NOT full content
- Quality gates: educational-validator MUST PASS before marking lesson complete
- Parallel execution: L01-L02 parallel; L03-L05 parallel after foundation; L06-L07 parallel after core
- Safety requirements: All dangerous operations include explicit warnings
- Progressive complexity: B1 → B2 → C1 across lessons (Layer 1→4)
- Three Roles explicitly included in all Layer 2 lessons (L03-L07)

**Dependencies Documented**:

- Foundation (L01-L02) → Core Operations (L03-L05) → Process Control (L06-L07) → Mastery (L08-L09)
- Sequential or parallel strategies provided
- Quality gates enforced at each lesson

## Outcome

- ✅ Impact: Complete task breakdown created with 19 tasks organized for systematic chapter creation
- 🧪 Tests: No automated tests (educational content uses hands-on exercises and chapter quiz)
- 📁 Files: specs/001-linux-mastery/tasks.md (created), plan.md and spec.md (referenced)
- 🔁 Next prompts: Content implementation phase - invoke content-implementer subagent for each lesson following task template
- 🧠 Reflection: Task generation successfully applied content work template with mandatory skill invocations (learning-objectives, exercise-designer, ai-collaborate-teaching) and subagent orchestration (content-implementer with direct-write protocol). Direct-write protocol prevents context bloat by having subagent return confirmation only (~50 lines) instead of full lesson content (800+ lines). Quality gates ensure each lesson passes educational-validator before marking complete.

## Evaluation notes (flywheel)

- Failure modes observed: None - task generation completed successfully on first attempt
- Graders run and results (PASS/FAIL):
  - Content task template validation: PASS (all lessons include skill invocations and subagent orchestration)
  - Direct-write protocol validation: PASS (content-implementer returns confirmation only, not full content)
  - Quality gate validation: PASS (educational-validator required before marking complete)
  - Dependency validation: PASS (Layer 1→2→3→4 progression enforced)
  - Three Roles validation: PASS (ai-collaborate-teaching skill included in all Layer 2 lessons)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Consider creating skill invocation automation script to streamline the repeated skill calls (learning-objectives + exercise-designer + ai-collaborate-teaching + content-evaluation-framework) across all lessons
