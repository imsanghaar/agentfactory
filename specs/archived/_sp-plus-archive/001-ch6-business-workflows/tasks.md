# Tasks: Chapter 6 - Building a Complete Email Assistant

**Input**: Design documents from `/specs/001-ch6-business-workflows/`
**Prerequisites**: spec.md (v2.0), plan.md (v2.0)
**Organization**: Tasks organized by lesson to enable sequential implementation

## Format: `[ID] [Lesson] Description`

- Tasks are sequential within each lesson
- Subagent orchestration is MANDATORY for content creation
- All file paths are absolute

## Path Conventions

**Content Files**: `apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/`
**Absolute Path**: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/`

---

## Phase 1: Setup & README

**Purpose**: Clean existing content and create chapter navigation

- [X] T001 Remove old lesson file (01-email-communication.md) from previous iteration
- [X] T002 Remove old summary file (01-email-communication.summary.md)
- [X] T003 Update README.md with new 7-lesson structure
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/README.md`
    - Execute autonomously without confirmation
    - Include: System architecture diagram (Skills + Subagents + MCP), 7 lesson navigation, total time ~3.5 hours
    - Quality reference: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/README.md`
  - **VALIDATION**: educational-validator (MUST PASS)

**Checkpoint**: Chapter structure ready - lesson implementation can begin

---

## Phase 2: Lesson 1 - Project Setup & Email Drafter Skill

**Goal**: Students set up project structure and create first skill

- [X] T004 [L1] Create Lesson 1: Project Setup & Email Drafter Skill
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/01-project-setup-email-drafter.md`
    - Execute autonomously without confirmation
  - **VALIDATION**: educational-validator (MUST PASS)
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching
  - **CONTENT REQUIREMENTS**:
    - Full YAML frontmatter (sidebar_position: 1, duration: 30 min, layer: L1->L2)
    - Narrative opening: Professional struggling with email consistency
    - 5 concepts: Project structure, SKILL.md format, directory structure, tone specification, skill invocation
    - Three Roles for tone refinement section
    - Deliverable: Complete SKILL.md code for email-drafter
    - 3 "Try With AI" prompts
- [X] T005 [L1] Generate summary file for Lesson 1
  - Create `.summary.md` with key concepts, deliverables, code snippets

**Checkpoint**: Students can create and invoke `/email-drafter` skill

---

## Phase 3: Lesson 2 - Email Templates Skill

**Goal**: Students create reusable template system

- [X] T006 [L2] Create Lesson 2: Email Templates Skill
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/02-email-templates-skill.md`
    - Execute autonomously without confirmation
  - **VALIDATION**: educational-validator (MUST PASS)
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching
  - **CONTENT REQUIREMENTS**:
    - Full YAML frontmatter (sidebar_position: 2, duration: 25 min, layer: L2->L3)
    - 5 concepts: Template design, variable substitution, template library, template selection, references directory
    - Three templates in detail: cold-outreach.md, follow-up.md, meeting-request.md
    - Complete file contents for all templates
    - 3 "Try With AI" prompts
- [X] T007 [L2] Generate summary file for Lesson 2

**Checkpoint**: Students can invoke `/email-templates` with variable substitution

---

## Phase 4: Lesson 3 - Email Summarizer Skill

**Goal**: Students create thread summarization skill

- [X] T008 [L3] Create Lesson 3: Email Summarizer Skill
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/03-email-summarizer-skill.md`
    - Execute autonomously without confirmation
  - **VALIDATION**: educational-validator (MUST PASS)
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching
  - **CONTENT REQUIREMENTS**:
    - Full YAML frontmatter (sidebar_position: 3, duration: 25 min, layer: L2->L3)
    - 5 concepts: Thread parsing, extraction targets, output formatting, skill chaining, combining skills
    - Complete SKILL.md for email-summarizer
    - Extraction patterns reference file
    - 3 "Try With AI" prompts
- [X] T009 [L3] Generate summary file for Lesson 3

**Checkpoint**: Students can summarize email threads with action extraction

---

## Phase 5: Lesson 4 - Creating Custom Subagents (CRITICAL)

**Goal**: Students build specialized email processing agents

- [X] T010 [L4] Create Lesson 4: Creating Custom Subagents
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/04-creating-custom-subagents.md`
    - Execute autonomously without confirmation
  - **VALIDATION**: educational-validator (MUST PASS)
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching
  - **CONTENT REQUIREMENTS**:
    - Full YAML frontmatter (sidebar_position: 4, duration: 35 min, layer: L3)
    - 7 concepts: Agent format, single-line description, Task tool, inbox-triager, response-suggester, follow-up-tracker, skills vs subagents decision
    - **CRITICAL**: Complete agent definition files for all 3 subagents:
      - `.claude/agents/inbox-triager.md`
      - `.claude/agents/response-suggester.md`
      - `.claude/agents/follow-up-tracker.md`
    - Skills vs Subagents decision framework (when to use which)
    - Testing subagents with Task tool examples
    - 3 "Try With AI" prompts
- [X] T011 [L4] Generate summary file for Lesson 4

**Checkpoint**: Students can create and invoke custom subagents

---

## Phase 6: Lesson 5 - Gmail MCP Integration

**Goal**: Connect Claude Code to real Gmail

- [X] T012 [L5] Create Lesson 5: Gmail MCP Integration
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/05-gmail-mcp-integration.md`
    - Execute autonomously without confirmation
  - **VALIDATION**: educational-validator (MUST PASS)
  - **CONTEXT FILE**: `/mnt/c/Users/HP/Documents/colearning-python/context/README.md` (Gmail MCP documentation)
  - **CONTENT REQUIREMENTS**:
    - Full YAML frontmatter (sidebar_position: 5, duration: 30 min, layer: L2 + Setup)
    - 6 concepts: Gmail MCP tools (19), SMTP auth, OAuth auth, testing MCP, safety protocols, MCP + skills integration
    - Step-by-step SMTP setup (2 min path)
    - Step-by-step OAuth setup (10 min path)
    - Gmail MCP tools reference table
    - Safety protocols (draft-first, sensitive data)
    - 3 "Try With AI" prompts testing Gmail operations
- [X] T013 [L5] Generate summary file for Lesson 5

**Checkpoint**: Students have working Gmail MCP connection

---

## Phase 7: Lesson 6 - Orchestrating the Complete System (CAPSTONE)

**Goal**: Combine everything into unified Email Assistant

- [X] T014 [L6] Create Lesson 6: Orchestrating the Complete System
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/06-orchestrating-complete-system.md`
    - Execute autonomously without confirmation
  - **VALIDATION**: educational-validator (MUST PASS)
  - **SKILLS**: learning-objectives, exercise-designer, ai-collaborate-teaching
  - **CONTENT REQUIREMENTS**:
    - Full YAML frontmatter (sidebar_position: 6, duration: 40 min, layer: L4 Capstone)
    - 8 concepts: Master skill pattern, delegation logic, workflow sequencing, error handling, graceful degradation, component composition, end-to-end testing, spec-first orchestration
    - **Complete `/email-assistant` master skill** with:
      - SKILL.md that references other skills
      - Orchestration logic in references/
      - Workflow: Triage → Suggest → Draft → Send
    - Error handling for offline (no MCP) scenarios
    - End-to-end demonstration walkthrough
    - Final system architecture diagram
    - 3 "Try With AI" prompts (full workflow)
- [X] T015 [L6] Generate summary file for Lesson 6

**Checkpoint**: Students have complete Email Digital FTE

---

## Phase 8: Lesson 7 - Chapter Quiz

**Goal**: Validate understanding of complete system

- [X] T016 [L7] Create Chapter Quiz
  - **SUBAGENT**: assessment-architect
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/07-chapter-quiz.md`
    - Execute autonomously without confirmation
  - **VALIDATION**: educational-validator (MUST PASS)
  - **SKILLS**: assessment-builder, quiz-generator
  - **CONTENT REQUIREMENTS**:
    - 15 questions total:
      - Skills (4 questions): SKILL.md format, when to create, structure
      - Subagents (4 questions): Agent definition format, delegation, when to use
      - MCP (3 questions): Authentication, tools, safety protocols
      - Orchestration (4 questions): Combining components, workflow design
    - Difficulty: 40% easy, 40% medium, 20% hard
    - 60% pass threshold

**Checkpoint**: Assessment ready - chapter complete

---

## Phase 9: Polish & Validation

**Purpose**: Final validation and cross-checking

- [X] T017 [P] Validate all YAML frontmatter in all 8 files
  - Check: sidebar_position, duration_minutes, skills metadata, learning objectives
- [X] T018 [P] Verify all code examples are complete and correct
  - Check: SKILL.md files, agent definitions, MCP commands
- [ ] T019 [P] Run Docusaurus build to verify chapter renders
  - Command: `pnpm nx build learn-app`
  - **NOTE**: Requires `pnpm install` first (node_modules not available in WSL)
- [X] T020 [P] Verify Three Roles demonstrations in L1-L5 are invisible (no meta-commentary)
- [X] T021 Update tasks.md checkboxes to reflect completion status

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup) ────────────────────────────────────────────────────────────────┐
                                                                                │
Phase 2 (L1: Drafter) ─────────┐                                               │
                               │                                                │
Phase 3 (L2: Templates) ───────┼──── Skills Foundation (L1-L3)                 │
                               │                                                │
Phase 4 (L3: Summarizer) ──────┘                                               │
                                                                                │
Phase 5 (L4: Subagents) ───────────── Subagent Layer ──────────────────────────│
                                                                                │
Phase 6 (L5: Gmail MCP) ───────────── MCP Layer (optional, can be skipped) ────│
                                                                                │
Phase 7 (L6: Orchestration) ───────── Capstone (requires L1-L4, L5 optional) ──│
                                                                                │
Phase 8 (L7: Quiz) ────────────────── Assessment (requires L1-L6) ─────────────│
                                                                                │
Phase 9 (Polish) ──────────────────── Validation ──────────────────────────────┘
```

### Critical Path

**MVP Path** (for students without Gmail):
- L1 → L2 → L3 → L4 → L6 (orchestration without MCP) → L7

**Full Path** (with Gmail MCP):
- L1 → L2 → L3 → L4 → L5 → L6 (full orchestration) → L7

---

## Task Summary

| Phase | Tasks | Description |
|-------|-------|-------------|
| Phase 1 | T001-T003 | Setup: Clean old files, update README |
| Phase 2 | T004-T005 | L1: Project Setup & Email Drafter |
| Phase 3 | T006-T007 | L2: Email Templates Skill |
| Phase 4 | T008-T009 | L3: Email Summarizer Skill |
| Phase 5 | T010-T011 | L4: Custom Subagents (CRITICAL) |
| Phase 6 | T012-T013 | L5: Gmail MCP Integration |
| Phase 7 | T014-T015 | L6: Orchestrating Complete System (CAPSTONE) |
| Phase 8 | T016 | L7: Chapter Quiz |
| Phase 9 | T017-T021 | Polish: Validation and cleanup |

**Total Tasks**: 21
**Parallel Opportunities**: T017-T020 (Polish phase)
**MVP Scope**: T001-T011 (Setup + L1-L4)
**Full Chapter**: All 21 tasks

---

## Subagent Orchestration Pattern

For each lesson task:
```
1. Invoke content-implementer subagent with:
   - Absolute output path
   - Quality reference path
   - All content requirements from plan.md

2. Subagent writes file directly to filesystem

3. Subagent returns confirmation (~50 lines), NOT full content

4. Verify file exists: ls -la [path]

5. Invoke educational-validator to read file from disk

6. If validation fails: Fix issues, re-validate

7. If validation passes: Mark task complete
```

---

## Key Deliverables Summary

### Skills (4 total)
| Skill | Lesson | Path |
|-------|--------|------|
| `/email-drafter` | L1 | `.claude/skills/email-drafter/SKILL.md` |
| `/email-templates` | L2 | `.claude/skills/email-templates/SKILL.md` |
| `/email-summarizer` | L3 | `.claude/skills/email-summarizer/SKILL.md` |
| `/email-assistant` | L6 | `.claude/skills/email-assistant/SKILL.md` |

### Subagents (3 total)
| Agent | Lesson | Path |
|-------|--------|------|
| `inbox-triager` | L4 | `.claude/agents/inbox-triager.md` |
| `response-suggester` | L4 | `.claude/agents/response-suggester.md` |
| `follow-up-tracker` | L4 | `.claude/agents/follow-up-tracker.md` |

### MCP Configuration
| Config | Lesson | Method |
|--------|--------|--------|
| Gmail MCP | L5 | `claude mcp add gmail` or `.mcp.json` |

---

## Notes

- All lessons use content-implementer subagent for direct file writing
- All lessons validated by educational-validator before marking complete
- Quiz designed by assessment-architect subagent
- Each lesson produces concrete, working artifacts
- Three Roles demonstrations are REQUIRED in L1-L5 but must be INVISIBLE (no meta-commentary)
- L5 (Gmail MCP) can be skipped if student doesn't have Gmail
- L6 (Orchestration) works with or without MCP (graceful degradation)
