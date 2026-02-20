# Tasks: Chapter 42 - Apps SDK (Building Interactive ChatGPT Apps)

**Source Plan**: specs/048-chapter-42-openai-apps-sdk/plan.md
**Source Spec**: specs/048-chapter-42-openai-apps-sdk/spec.md
**Generated**: 2025-12-28
**Completed**: 2025-12-28
**Total Tasks**: 14

---

## Phase 1: Setup

- [x] T42.DIR Create chapter directory structure at `apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/`

---

## Phase 2: Chapter README

- [x] T42.README Create chapter README.md ✅ (61 lines)
  - **Output Path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/README.md`
  - **SUBAGENT**: content-implementer
    - Write file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Include: chapter overview, learning outcomes, lesson list, prerequisites (Ch33-34, 37-38, 40)
    - Quality reference: `apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/README.md`
  - **Acceptance Criteria**:
    - [ ] YAML frontmatter with sidebar_position: 42
    - [ ] Chapter title and description
    - [ ] "What You'll Learn" section with 5-7 outcomes
    - [ ] Prerequisites section referencing prior chapters
    - [ ] Chapter structure overview

---

## Phase 3: Lesson Implementation

### Lesson 1: Apps SDK Architecture (L1 - Manual Foundation)

- [x] T42.L1 Create lesson 1: Apps SDK Architecture ✅ (372 lines)
  - **Output Path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/01-apps-sdk-architecture.md`
  - **Dependencies**: T42.README
  - **SKILLS**:
    - Invoke: `learning-objectives` (generate B1 measurable outcomes)
  - **SUBAGENT**: content-implementer
    - Write file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/01-sdk-setup-first-agent.md`
    - Expertise source: `.claude/skills/building-chatgpt-apps/SKILL.md`
  - **Key Concepts** (4):
    - Three-layer architecture (ChatGPT UI → Widget iframe → MCP Server)
    - Widget vs standard MCP tool differences
    - Data flow: prompt → model → tool → server → widget → narration
    - Official examples (kitchen_sink) structure
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS)
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter (skills, learning_objectives, cognitive_load: 4 concepts)
    - [ ] Architecture diagram explanation
    - [ ] Comparison table: Apps SDK vs Agents SDK vs standard MCP
    - [ ] Manual diagram drawing exercise (no AI)
    - [ ] Ends with activity section (no summary after)
    - [ ] **No "Try With AI" section** (L1 lesson)

---

### Lesson 2: Your First ChatGPT App (L2 - AI Collaboration)

- [x] T42.L2 Create lesson 2: Your First ChatGPT App ✅ (578 lines)
  - **Output Path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/02-first-chatgpt-app.md`
  - **Dependencies**: T42.L1
  - **SKILLS**:
    - Invoke: `learning-objectives` (B1 measurable outcomes)
    - Invoke: `exercise-designer` (3 exercises)
    - Invoke: `ai-collaborate-teaching` (Three Roles demonstrations)
  - **SUBAGENT**: content-implementer
    - Write file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/02-function-tools-context.md`
    - Expertise source: `.claude/skills/building-chatgpt-apps/SKILL.md`
  - **Key Concepts** (5):
    - Project setup with FastMCP for ChatGPT Apps
    - `text/html+skybridge` MIME type for widget resources
    - Tool definition with `openai/outputTemplate` metadata
    - ngrok tunnel setup for local development
    - ChatGPT Developer Mode registration
  - **Three Roles Required**:
    - AI as Teacher: Widget metadata pattern
    - AI as Student: Simplify React to vanilla HTML
    - AI as Co-Worker: ngrok workflow convergence
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS)
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter (skills, learning_objectives, cognitive_load: 5 concepts)
    - [ ] 3 "Try With AI" prompts with learning explanations
    - [ ] Evidence blocks (Output:) for all code examples
    - [ ] Three Roles demonstrations invisible to reader
    - [ ] Ends with activity section (no summary after)

---

### Lesson 3: Widget Interactivity (L2 - AI Collaboration)

- [x] T42.L3 Create lesson 3: Widget Interactivity ✅ (735 lines)
  - **Output Path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/03-widget-interactivity.md`
  - **Dependencies**: T42.L2
  - **SKILLS**:
    - Invoke: `learning-objectives` (B1 measurable outcomes)
    - Invoke: `exercise-designer` (3 exercises)
    - Invoke: `ai-collaborate-teaching` (Three Roles demonstrations)
  - **SUBAGENT**: content-implementer
    - Write file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Expertise source: `.claude/skills/building-chatgpt-apps/SKILL.md`
  - **Key Concepts** (4):
    - `window.openai` API availability checks (optional chaining)
    - `sendFollowUpMessage` for action buttons
    - `callTool` for tool chaining from widgets
    - `openai/widgetAccessible` metadata for enabling callTool
  - **Three Roles Required**:
    - AI as Teacher: Optional chaining pattern
    - AI as Student: Appropriate method per action type
    - AI as Co-Worker: Missing widgetAccessible debug
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS)
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter (cognitive_load: 4 concepts)
    - [ ] 3 "Try With AI" prompts with learning explanations
    - [ ] Complete window.openai API reference table
    - [ ] Evidence blocks for all code examples
    - [ ] Ends with activity section (no summary after)

---

### Lesson 4: Response Payload Design (L2 - AI Collaboration)

- [x] T42.L4 Create lesson 4: Response Payload Design ✅ (709 lines)
  - **Output Path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/04-response-payload-design.md`
  - **Dependencies**: T42.L3
  - **SKILLS**:
    - Invoke: `learning-objectives` (B1 measurable outcomes)
    - Invoke: `exercise-designer` (3 exercises)
    - Invoke: `ai-collaborate-teaching` (Three Roles demonstrations)
  - **SUBAGENT**: content-implementer
    - Write file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Expertise source: `.claude/skills/building-chatgpt-apps/SKILL.md`
  - **Key Concepts** (3):
    - `structuredContent` - concise JSON for model narration
    - `_meta` - large/sensitive data hidden from model
    - `content` - optional markdown/text for model
  - **Three Roles Required**:
    - AI as Teacher: Payload separation principle
    - AI as Student: Balance summary vs details
    - AI as Co-Worker: Data flow tracing
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS)
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter (cognitive_load: 3 concepts)
    - [ ] 3 "Try With AI" prompts with learning explanations
    - [ ] Response payload structure diagram
    - [ ] Visibility comparison table
    - [ ] Ends with activity section (no summary after)

---

### Lesson 5: State and Display Modes (L2 - AI Collaboration)

- [x] T42.L5 Create lesson 5: State and Display Modes ✅ (935 lines)
  - **Output Path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/05-state-display-modes.md`
  - **Dependencies**: T42.L4
  - **SKILLS**:
    - Invoke: `learning-objectives` (B1 measurable outcomes)
    - Invoke: `exercise-designer` (3 exercises)
    - Invoke: `ai-collaborate-teaching` (Three Roles demonstrations)
  - **SUBAGENT**: content-implementer
    - Write file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Expertise source: `.claude/skills/building-chatgpt-apps/SKILL.md`
  - **Key Concepts** (5):
    - `widgetState` - reading persisted UI state
    - `setWidgetState` - synchronous state persistence
    - React hooks: `useWidgetState`, `useOpenAiGlobal` (optional advanced)
    - Display modes: inline, pip, fullscreen
    - `requestDisplayMode` API
  - **Three Roles Required**:
    - AI as Teacher: State persistence lifecycle
    - AI as Student: Vanilla JS primary, React optional
    - AI as Co-Worker: Platform coercion behavior
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS)
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter (cognitive_load: 5 concepts)
    - [ ] 3 "Try With AI" prompts with learning explanations
    - [ ] State management patterns (vanilla JS)
    - [ ] React hooks reference as sidebar
    - [ ] Ends with activity section (no summary after)

---

### Lesson 6: Building TaskManager Widget (L3 - Pattern Application)

- [x] T42.L6 Create lesson 6: Building TaskManager Widget ✅ (1090 lines)
  - **Output Path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/06-taskmanager-widget.md`
  - **Dependencies**: T42.L5
  - **SKILLS**:
    - Invoke: `learning-objectives` (B1 measurable outcomes)
    - Invoke: `exercise-designer` (guided pattern application)
  - **SUBAGENT**: content-implementer
    - Write file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Expertise source: `.claude/skills/building-chatgpt-apps/SKILL.md`
  - **Patterns Applied**:
    - Three-layer architecture (Lesson 1)
    - FastMCP server with widget resources (Lesson 2)
    - Interactive buttons (Lesson 3)
    - structuredContent vs _meta (Lesson 4)
    - State persistence (Lesson 5)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS)
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] TaskManager specification (spec-driven approach)
    - [ ] MCP server with 4 tools: list_tasks, add_task, complete_task, delete_task
    - [ ] Task list widget with interactive buttons
    - [ ] State persistence for task selections
    - [ ] Ends with activity section (no summary after)

---

### Lesson 7: TaskManager Capstone (L4 - Spec-Driven Integration)

- [x] T42.L7 Create lesson 7: TaskManager Capstone ✅ (940 lines)
  - **Output Path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/07-taskmanager-capstone.md`
  - **Dependencies**: T42.L6
  - **SKILLS**:
    - Invoke: `learning-objectives` (B1 measurable outcomes)
  - **SUBAGENT**: content-implementer
    - Write file directly (returns confirmation only)
    - Execute autonomously without confirmation
    - Expertise source: `.claude/skills/building-chatgpt-apps/SKILL.md`
  - **Capstone Deliverables**:
    - Complete implementation review
    - Debug and fix common issues
    - Deployment considerations
    - Future extensions (categories, due dates, OAuth)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS)
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] Complete code walkthrough
    - [ ] Troubleshooting section (from skill)
    - [ ] Extension exercise (add categories)
    - [ ] Independent challenge (add due dates)
    - [ ] Ends with activity section (no summary after)

---

## Phase 4: Assessment

- [x] T42.QUIZ Create chapter quiz ✅ (589 lines, 50 questions)
  - **Output Path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/06-AI-Native-Software-Development/42-openai-apps-sdk/quiz.md`
  - **Dependencies**: T42.L7
  - **SKILLS**:
    - Invoke: `assessment-builder` (50 questions, Bloom's alignment)
    - Invoke: `quiz-generator` (Quiz component with randomized batching)
  - **SUBAGENT**: content-implementer
    - Write file directly (returns confirmation only)
    - Execute autonomously without confirmation
  - **Quiz Coverage**:
    - Architecture concepts (10 questions)
    - Widget development (15 questions)
    - window.openai API (10 questions)
    - Response payloads (5 questions)
    - State and display modes (5 questions)
    - Integration patterns (5 questions)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS)
  - **Acceptance Criteria**:
    - [ ] 50 questions total
    - [ ] Uses Quiz component with randomized batching
    - [ ] Coverage across all 7 lessons
    - [ ] Immediate feedback on each question
    - [ ] 80% pass threshold documented

---

## Phase 5: Validation

- [x] T42.VALIDATE Run all validators on chapter content ✅ (PASS)
  - **Dependencies**: T42.QUIZ (all content complete)
  - **VALIDATORS** (run in parallel):
    - `educational-validator` - per lesson (8x parallel)
    - `validation-auditor` - chapter-wide quality assessment
    - `factual-verifier` - verify all technical claims
    - `pedagogical-designer` - validate L1→L2→L3→L4 progression
  - **Gate Criteria**:
    - All 8 lessons pass educational-validator
    - validation-auditor score ≥ 80%
    - Zero unverified factual claims
    - Pedagogical progression validated
  - **On Failure**: Fix issues and re-run failed validators

---

## Dependency Graph

```
T42.DIR
    |
    v
T42.README
    |
    v
T42.L1 (Architecture)
    |
    v
T42.L2 (First App)
    |
    v
T42.L3 (Interactivity)
    |
    v
T42.L4 (Payloads)
    |
    v
T42.L5 (State/Display)
    |
    v
T42.L6 (TaskManager Build)
    |
    v
T42.L7 (Capstone)
    |
    v
T42.QUIZ
    |
    v
T42.VALIDATE
```

---

## Parallel Execution Opportunities

- [ ] T42.L1 through T42.L7 can be validated in parallel AFTER all are written
- [ ] T42.VALIDATE runs 4 validators in parallel

---

## Summary

| Phase | Tasks | Description |
|-------|-------|-------------|
| Setup | 1 | Create directory structure |
| README | 1 | Chapter introduction |
| Lessons | 7 | L1 + 4×L2 + L3 + L4 progression |
| Assessment | 1 | 50-question quiz |
| Validation | 1 | Run all validators |
| **Total** | **11** | Plus 3 dependent tasks |

---

## Implementation Strategy

1. **MVP Scope**: T42.DIR → T42.README → T42.L1 → T42.L2 (First working lesson)
2. **Incremental**: Each lesson independently testable
3. **Quality Gates**: Validation after each lesson before marking complete
4. **Expertise Source**: All lessons reference `.claude/skills/building-chatgpt-apps/SKILL.md`
