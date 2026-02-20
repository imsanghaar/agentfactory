# Tasks: Chapter 41 - ChatKit Server for Agents

**Input**: Design documents from `/specs/1-ch41-chatkit-server/`
**Prerequisites**: plan.md ✅, spec.md ✅
**Work Type**: Educational Content (8 lessons following 4-Layer Teaching Method)
**Target**: Part 6, Chapter 41 - ChatKit Server for Agents

**Organization**: Tasks are grouped by user story (lesson) to enable independent implementation and validation of each lesson.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different lessons, no dependencies)
- **[Story]**: Which lesson this task creates (US1=L01, US2=L02, etc.)
- **SUBAGENT**: All lesson tasks use content-implementer (direct-write protocol)
- **VALIDATION**: All lesson tasks validated by educational-validator before completion

## Path Conventions

- **Chapter location**: `apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/`
- **Lesson files**: `01-chatkit-architecture.md` through `08-capstone-conversational-agent.md`
- **Quality reference**: `apps/learn-app/docs/01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-the-2025-inflection-point.md`
- **README**: `apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/README.md` (already exists)

---

## Phase 1: Setup & Research (Foundational Prerequisites)

**Purpose**: Gather official documentation and establish quality baselines before content creation

**⚠️ CRITICAL**: Complete before ANY lesson implementation to prevent hallucination (Chapter 2 incident)

- [X] T001 Research ChatKit Python SDK official docs via WebSearch. Verify current 2025 version and gather:
  - ChatKitServer class signature
  - respond() method signature
  - ThreadMetadata, UserMessageItem, RequestContext types
  - stream_agent_response() helper
  - Official examples from https://openai.github.io/chatkit-python/
  - **Doc**: Save findings to `specs/1-ch41-chatkit-server/research-chatkit-sdk.md`
  - ✅ **COMPLETE**: Research documented in research-chatkit-sdk.md

- [X] T002 [P] Research ChatKit.js (React) official docs via WebSearch. Gather:
  - useChatKit hook signature
  - Custom fetch interceptor patterns
  - Script loading patterns for web components
  - Official examples from https://openai.github.io/chatkit-js/
  - **Doc**: Save findings to `specs/1-ch41-chatkit-server/research-chatkit-react.md`
  - ✅ **COMPLETE**: Research documented in research-chatkit-react.md

- [X] T003 [P] Identify quality reference lesson for calibration:
  - Read `apps/learn-app/docs/01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-the-2025-inflection-point.md`
  - Document quality markers: YAML frontmatter completeness, narrative opening depth, "Try With AI" structure, safety notes placement
  - **Doc**: Save calibration notes to `specs/1-ch41-chatkit-server/quality-calibration.md`
  - ✅ **COMPLETE**: Quality calibration documented

- [X] T004 Validate canonical skill format from `.claude/skills/building-chat-interfaces/SKILL.md`:
  - Confirm directory structure (SKILL.md NOT flat file)
  - Confirm YAML frontmatter requirements
  - Confirm required sections (Overview, When to Use, Workflow, References)
  - **Doc**: Note format requirements for L00 lesson reference
  - ✅ **COMPLETE**: Skill format validated and documented in skill-format-validation.md

**Checkpoint**: Research complete, quality baseline established, canonical formats validated

---

## Phase 2: Chapter Structure Validation

**Purpose**: Ensure chapter README and L00 skill lesson meet requirements before generating L01-L08

- [X] T005 Validate existing README.md structure:
  - Verify 8 lessons listed in Chapter Structure section
  - Confirm prerequisites match spec (Chapter 40, Chapters 34-36, Part 5)
  - Validate "Looking Ahead" section connects to Chapters 42-48 and Part 7
  - Update if needed to reflect final plan
  - ✅ **COMPLETE**: README.md validated - all requirements met

- [X] T006 Validate existing L00 lesson (`00-build-your-chatkit-skill.md`):
  - Confirm references canonical skill format from `.claude/skills/building-chat-interfaces/SKILL.md`
  - Verify includes skill creation checklist
  - Validate guides students to official ChatKit docs (no hallucinated patterns)
  - Update if needed based on T001-T004 research
  - ✅ **COMPLETE**: L00 updated with canonical format reference, validation checklist, and verification script usage

**Checkpoint**: Foundation validated - lesson implementation can now begin in parallel

---

## Phase 3: User Story 1 - L01 ChatKit Architecture (Priority: P1) 🎯 Foundation

**Goal**: Build vocabulary and mental models for ChatKit architecture without code implementation (Layer 1 - Manual)

**Independent Test**: Student can explain ChatKitServer.respond() vs FastAPI route handler differences and diagram ThreadItem lifecycle (maps to SC-001 success criteria)

### Implementation for US1 (Lesson 1)

- [X] T007 [US1] Create Lesson 1: ChatKit Architecture Foundations
  - ✅ **COMPLETE**: 430 lines, Layer 1 foundation, 7 concepts, B1 proficiency validated
  - **SUBAGENT**: content-implementer
    - **Execute autonomously without confirmation**
    - **Output path**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/01-chatkit-architecture.md`
    - **Writes file directly** (returns confirmation only, NOT full content ~50 lines max)
    - **Quality reference**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-the-2025-inflection-point.md`
    - **Requirements**:
      - Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation per spec FR-006)
      - Narrative opening (2-3 paragraphs, real-world scenario)
      - Layer 1 (Manual): NO AI collaboration, NO code examples yet
      - Architecture diagrams (FastAPI stateless vs ChatKitServer stateful)
      - ThreadItem lifecycle visualization
      - RequestContext multi-tenant isolation diagram
      - Build vocabulary: Thread, ThreadItem, RequestContext, respond(), streaming vs request/response
      - Max 7 concepts (validated in plan: within B1 limit)
      - NO "Try With AI" section (Layer 1 restriction)
      - Safety note embedded: "Multi-user authentication prevents thread access violations"
      - Agent Factory connection: "ChatKitServer = infrastructure for sellable chat agents"
    - **Research source**: Use `specs/1-ch41-chatkit-server/research-chatkit-sdk.md` for accurate terminology
  - **SKILLS**:
    - Invoke `learning-objectives` for measurable outcomes (LO-001 through LO-003 from plan)
    - Invoke `skills-proficiency-mapper` to validate B1 proficiency alignment
  - **VALIDATION**: educational-validator reads file from disk
    - MUST PASS constitution compliance (no meta-commentary, correct layer)
    - MUST PASS fact-checking (no hallucinated architecture claims)
    - MUST PASS proficiency alignment (B1 tier, 7 concepts ≤ 10 limit)
  - **QUALITY GATE**: Invoke `content-evaluation-framework` before marking complete

**Checkpoint**: L01 (Layer 1 Foundation) complete and validated - students have vocabulary for L02-L08 implementation

---

## Phase 4: User Story 2 - L02 Connecting First Agent (Priority: P1)

**Goal**: Wire existing OpenAI agent into ChatKit with streaming responses (Layer 2 - AI Collaboration)

**Independent Test**: Student creates minimal ChatKitServer responding to user messages via agent (maps to SC-002: <30 min implementation)

### Implementation for US2 (Lesson 2)

- [X] T008 [P] [US2] Create Lesson 2: Connecting Your First Agent to ChatKit
  - ✅ **COMPLETE**: 473 lines, Layer 2 collaboration, 3 "Try With AI" prompts, code with Output sections
  - **SUBAGENT**: content-implementer
    - **Execute autonomously without confirmation**
    - **Output path**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/02-connecting-first-agent.md`
    - **Writes file directly** (returns confirmation only)
    - **Quality reference**: Same as T007
    - **Requirements**:
      - Full YAML frontmatter (per FR-006)
      - Narrative opening connecting to L01 architecture understanding
      - Layer 2 (Collaboration): Include Three Roles demonstrations (hidden from students per FR-010)
      - Code examples: ChatKitServer class inheritance, respond() implementation, stream_agent_response() helper
      - Running example: TaskManager conversational agent (Part 6 consistency)
      - Integrate existing OpenAI agent from Chapter 34
      - 3 "Try With AI" prompts with "What you're learning" explanations (per FR-007)
      - Safety note: "Test with OpenAI API key from environment variables, never hardcode"
      - Agent Factory connection: "Connect existing agents to conversational products"
      - Max 8 concepts (B1 limit validated in plan)
    - **Research source**: Use `specs/1-ch41-chatkit-server/research-chatkit-sdk.md` for code syntax
  - **SKILLS**:
    - Invoke `learning-objectives` (LO from plan)
    - Invoke `exercise-designer` (3 exercises: connection, basic response, error handling)
    - Invoke `ai-collaborate-teaching` (design Three Roles sections for Layer 2)
  - **VALIDATION**: educational-validator (constitution + fact-check + code syntax against ChatKit SDK)
  - **QUALITY GATE**: `content-evaluation-framework`

**Checkpoint**: L02 complete - students have working ChatKit integration

---

## Phase 5: User Story 3 - L03 Streaming Implementation (Priority: P2)

**Goal**: Implement token-by-token streaming with progress indicators and interruption handling (Layer 2 - Collaboration)

**Independent Test**: Student implements streaming with <100ms latency per token (maps to SC-003)

### Implementation for US3 (Lesson 3)

- [X] T009 [P] [US3] Create Lesson 3: Streaming Response Patterns
  - ✅ **COMPLETE**: 526 lines, AsyncIterator patterns, 15+ code examples with Output sections
  - **SUBAGENT**: content-implementer
    - **Execute autonomously without confirmation**
    - **Output path**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/03-streaming-implementation.md`
    - **Writes file directly** (returns confirmation only)
    - **Quality reference**: Same as T007
    - **Requirements**:
      - Full YAML frontmatter
      - Layer 2 (Collaboration) with Three Roles
      - Code: stream_agent_response() detailed usage, ProgressUpdateEvent for long operations, interruption handling
      - Performance validation: measure token latency
      - 3 "Try With AI" prompts focusing on streaming optimization
      - Safety note: "Buffer limits prevent memory exhaustion on long responses"
      - Agent Factory connection: "Professional streaming UX = customer-facing agent quality"
      - Max 8 concepts (B1)
    - **Research source**: `specs/1-ch41-chatkit-server/research-chatkit-sdk.md`
  - **SKILLS**: `learning-objectives`, `exercise-designer` (3 exercises on streaming patterns)
  - **VALIDATION**: educational-validator + fact-check streaming latency claims
  - **QUALITY GATE**: `content-evaluation-framework`

**Checkpoint**: L03 complete - students implement professional streaming UX

---

## Phase 6: User Story 4 - L04 Conversation Management (Priority: P2) + Skill Creation

**Goal**: Persist history, include in prompts, handle context window limits (Layer 2→3: Skill creation opportunity)

**Independent Test**: Agent references previous messages in responses (maps to SC-004)

### Implementation for US4 (Lesson 4)

- [X] T010 [P] [US4] Create Lesson 4: Conversation History Management
  - ✅ **COMPLETE**: 621 lines, Layer 3 with conversation-history skill creation, canonical format validated
  - **SUBAGENT**: content-implementer
    - **Execute autonomously without confirmation**
    - **Output path**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/04-conversation-management.md`
    - **Writes file directly** (returns confirmation only)
    - **Quality reference**: Same as T007
    - **Requirements**:
      - Full YAML frontmatter
      - Layer 2→3: Introduce skill creation for conversation-history patterns
      - Code: thread.metadata storage, history inclusion in prompts, context window management (truncation strategies)
      - **Skill creation section**: Guide students to create `conversation-history` skill (Layer 3 Intelligence)
      - Reference canonical skill format from T004 validation
      - 3 "Try With AI" prompts including skill refinement
      - Safety note: "Context window limits require truncation; maintain conversation coherence"
      - Agent Factory connection: "Agents with memory = higher-value services"
      - Max 9 concepts (B1 upper limit)
    - **Research source**: `specs/1-ch41-chatkit-server/research-chatkit-sdk.md`
  - **SKILLS**: `learning-objectives`, `exercise-designer`, `creating-skills` (guide skill creation)
  - **VALIDATION**: educational-validator + canonical format compliance check
  - **QUALITY GATE**: `content-evaluation-framework`

**Checkpoint**: L04 complete - students manage conversation memory + create reusable skill

---

## Phase 7: User Story 5 - L05 Session Lifecycle (Priority: P3) + Skill Creation

**Goal**: Create, resume, timeout, cleanup sessions (Layer 2→3: Skill creation)

**Independent Test**: Sessions resume correctly after 24-hour gaps (maps to SC-005)

### Implementation for US5 (Lesson 5)

- [X] T011 [P] [US5] Create Lesson 5: Session Lifecycle Management
  - ✅ **COMPLETE**: 829 lines, Layer 3 with session-lifecycle skill creation
  - **SUBAGENT**: content-implementer
    - **Execute autonomously without confirmation**
    - **Output path**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/05-session-lifecycle.md`
    - **Writes file directly** (returns confirmation only)
    - **Quality reference**: Same as T007
    - **Requirements**:
      - Full YAML frontmatter
      - Layer 2→3: Skill creation for session-lifecycle patterns
      - Code: session creation, resume with session_id, timeout handling, cleanup strategies
      - **Skill creation section**: `session-lifecycle` skill
      - 3 "Try With AI" prompts on session edge cases
      - Safety note: "Session cleanup prevents resource leaks; implement timeout policies"
      - Agent Factory connection: "Multi-user sessions = scalable Digital FTE deployment"
      - Max 8 concepts (B1)
    - **Research source**: `specs/1-ch41-chatkit-server/research-chatkit-sdk.md`
  - **SKILLS**: `learning-objectives`, `exercise-designer`, `creating-skills`
  - **VALIDATION**: educational-validator
  - **QUALITY GATE**: `content-evaluation-framework`

**Checkpoint**: L05 complete - students manage session lifecycle + create session-lifecycle skill

---

## Phase 8: User Story 6 - L06 Authentication & Security (Priority: P2) + Skill Creation

**Goal**: Multi-tenant user isolation via RequestContext (Layer 2→3: Skill creation)

**Independent Test**: Users cannot access each other's threads (maps to SC-006)

### Implementation for US6 (Lesson 6)

- [X] T012 [P] [US6] Create Lesson 6: Authentication and Security Patterns
  - ✅ **COMPLETE**: 827 lines, Layer 3 with chatkit-auth-security skill creation, JWT/JWKS patterns
  - **SUBAGENT**: content-implementer
    - **Execute autonomously without confirmation**
    - **Output path**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/06-authentication-security.md`
    - **Writes file directly** (returns confirmation only)
    - **Quality reference**: Same as T007
    - **Requirements**:
      - Full YAML frontmatter
      - Layer 2→3: Skill creation for chatkit-auth-security patterns
      - Code: RequestContext user_id isolation, JWT validation, authentication middleware patterns
      - Security testing: demonstrate isolation prevents cross-user access
      - **Skill creation section**: `chatkit-auth-security` skill
      - 3 "Try With AI" prompts on security patterns
      - Safety note: "RequestContext must validate on EVERY request; trust nothing from client"
      - Agent Factory connection: "Secure multi-tenant agents = enterprise-ready products"
      - Max 9 concepts (B1)
    - **Research source**: `specs/1-ch41-chatkit-server/research-chatkit-sdk.md`
  - **SKILLS**: `learning-objectives`, `exercise-designer`, `creating-skills`
  - **VALIDATION**: educational-validator + security pattern validation
  - **QUALITY GATE**: `content-evaluation-framework`

**Checkpoint**: L06 complete - students secure ChatKit with proper isolation + create auth skill

---

## Phase 9: User Story 7 - L07 React UI Integration (Priority: P3)

**Goal**: Connect ChatKit React components with custom auth (Layer 2 - Final Application)

**Independent Test**: React UI connects to backend with auth in <20 min (maps to SC-007)

### Implementation for US7 (Lesson 7)

- [X] T013 [P] [US7] Create Lesson 7: React UI Integration with ChatKit
  - ✅ **COMPLETE**: 636 lines, useChatKit patterns, custom fetch interceptors, Next.js integration
  - **SUBAGENT**: content-implementer
    - **Execute autonomously without confirmation**
    - **Output path**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/07-react-ui-integration.md`
    - **Writes file directly** (returns confirmation only)
    - **Quality reference**: Same as T007
    - **Requirements**:
      - Full YAML frontmatter
      - Layer 2 (Collaboration - final application layer)
      - Code: useChatKit hook, custom fetch interceptor for auth, page context injection, script loading detection
      - Running example: TaskManager chat widget
      - 3 "Try With AI" prompts on frontend integration
      - Safety note: "Never expose API keys in browser; use server-side proxy patterns"
      - Agent Factory connection: "Complete user-facing Digital FTE product"
      - Max 10 concepts (B1 upper limit for final technical lesson)
    - **Research source**: `specs/1-ch41-chatkit-server/research-chatkit-react.md`
  - **SKILLS**: `learning-objectives`, `exercise-designer` (frontend exercises), `frontend-design` (quality UI guidance)
  - **VALIDATION**: educational-validator + React code syntax validation
  - **QUALITY GATE**: `content-evaluation-framework`

**Checkpoint**: L07 complete - students build full-stack conversational interface

---

## Phase 10: User Story 8 - L08 Capstone Spec-Driven Agent (Priority: P1) 🎯 Synthesis

**Goal**: Layer 4 synthesis - write spec FIRST, then orchestrate AI to implement complete Digital FTE

**Independent Test**: 90% complete capstone with passing acceptance tests (maps to SC-008)

### Implementation for US8 (Lesson 8)

- [X] T014 [US8] Create Lesson 8: Capstone - Spec-Driven Conversational Agent
  - ✅ **COMPLETE**: 765 lines, Layer 4 spec-driven synthesis, complete TaskManager integration, 3 skills composed
  - **SUBAGENT**: content-implementer
    - **Execute autonomously without confirmation**
    - **Output path**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/08-capstone-conversational-agent.md`
    - **Writes file directly** (returns confirmation only)
    - **Quality reference**: Same as T007
    - **Requirements**:
      - Full YAML frontmatter
      - **Layer 4 (Spec-Driven)**: Students write specification FIRST before implementation
      - Specification template: intent, constraints, success criteria, acceptance tests
      - Skill composition: Use conversation-history (L04), session-lifecycle (L05), chatkit-auth-security (L06) skills together
      - AI orchestration: Students direct AI to implement from their spec
      - Deployment guidance: Local → production readiness checklist
      - Capstone assessment criteria tied to spec quality and acceptance test passage
      - 3 "Try With AI" prompts for specification refinement and implementation orchestration
      - Safety note: "Production ChatKit requires TLS, rate limiting, monitoring - covered in Part 7"
      - Agent Factory connection: "Sellable conversational agent Digital FTE - complete product"
      - Max 10 concepts (acceptable for capstone synthesis)
    - **Research source**: Both research docs + .specify/templates/spec-template.md for spec structure
  - **SKILLS**: `learning-objectives`, `ai-collaborate-teaching` (Layer 4 orchestration patterns), `assessment-architect` (capstone evaluation)
  - **VALIDATION**: educational-validator + spec-driven methodology compliance
  - **QUALITY GATE**: `content-evaluation-framework`

**Checkpoint**: L08 complete - students produce sellable Digital FTE via spec-driven development

---

## Phase 11: Assessment & Polish (Final Quality Gates)

**Purpose**: Complete chapter with assessment and final validation

- [ ] T015 [P] Create chapter quiz using assessment-architect skill:
  - 50 questions covering all 8 lessons
  - Balanced distribution across Bloom's taxonomy (per spec FR-013)
  - Maps to learning objectives from each lesson
  - **Output path**: `/mnt/d/hammad/TutorsGPT/agentfactory/apps/learn-app/docs/06-AI-Native-Software-Development/41-chatkit-server/09-chapter-quiz.md`
  - **SKILLS**: `assessment-builder` (question generation), `quiz-generator` (MCQ formatting)
  - **VALIDATION**: Answer distribution check (avoid pattern bias)

- [ ] T016 Validate README.md completeness:
  - All 8 lessons listed with correct titles
  - Prerequisites accurate
  - "What You'll Learn" matches lesson coverage
  - "Looking Ahead" connects to next chapters

- [ ] T017 Run chapter-level validators in parallel:
  - **Skill**: `canonical-format-checker` - Verify skill formats in L04, L05, L06 match canonical sources
  - **Skill**: `content-evaluation-framework` - Chapter-level quality assessment
  - **Subagent**: `validation-auditor` - Comprehensive chapter review
  - **Subagent**: `factual-verifier` - Verify all statistics, dates, SDK versions against official sources

- [ ] T018 Create chapter completion checklist:
  - All 21 functional requirements (FR-001 through FR-021) validated
  - All 14 success criteria (SC-001 through SC-014) measurable
  - Constitution v7.0.0 compliance confirmed
  - Agent Factory alignment explicit in all lessons
  - **Output**: `specs/1-ch41-chatkit-server/completion-checklist.md`

**Checkpoint**: Chapter 41 complete, validated, and ready for publication

---

## Dependencies & Execution Strategy

### Critical Path (Must Complete Sequentially)

```
Phase 1 (Research) → Phase 2 (Validation) → Phases 3-10 (Lessons - can parallelize) → Phase 11 (Assessment)
```

### Parallel Execution Opportunities

**After Phase 2 complete**, these can run in parallel:

```
T007 (L01) ║
T008 (L02) ║  All lessons independent
T009 (L03) ║  (different files, no cross-dependencies)
T010 (L04) ║
T011 (L05) ║
T012 (L06) ║
T013 (L07) ║
T014 (L08) ║
```

**Phase 11 tasks** can run in parallel after all lessons complete:
- T015 (Quiz generation)
- T016 (README validation)
- T017 (Validators - parallel)

### MVP Scope Recommendation

**Minimum Viable Chapter** (for early review):
- Phase 1: Research ✅ (required)
- Phase 2: Validation ✅ (required)
- Phase 3: L01 Foundation ✅ (required - builds vocabulary)
- Phase 4: L02 First Agent ✅ (required - proves concept)
- Phase 10: L08 Capstone ✅ (required - demonstrates synthesis)
- Phase 11: Assessment ✅ (required - measures outcomes)

**Incremental Delivery** (recommended for iterative review):
1. MVP (L01, L02, L08) - ~2 days
2. Add L03, L04 (streaming + memory) - +1 day
3. Add L05, L06 (sessions + security) - +1 day
4. Add L07 (React UI) - +0.5 day
5. Polish & Assessment - +0.5 day
**Total**: ~5 days for complete chapter with parallel execution

---

## Task Summary

**Total Tasks**: 18
- Phase 1 (Setup): 4 tasks
- Phase 2 (Validation): 2 tasks
- Phases 3-10 (Lessons): 8 tasks (one per lesson)
- Phase 11 (Assessment): 4 tasks

**Parallel Opportunities**: 11 tasks can run in parallel (after prerequisites)
**Estimated Effort**: 5-7 days with parallel subagent execution

**Work Type**: Educational Content (Chapter with 8 lessons)
**Quality Gates**: Every lesson passes educational-validator + content-evaluation-framework
**Success Criteria**: All 14 success criteria from spec (SC-001 through SC-014) validated

---

## Format Validation ✅

All tasks follow checklist format:
- ✅ Checkbox present (`- [ ]`)
- ✅ Task ID sequential (T001-T018)
- ✅ [P] markers for parallelizable tasks
- ✅ [Story] labels for lesson tasks (US1-US8)
- ✅ Absolute file paths specified
- ✅ SUBAGENT blocks for content creation
- ✅ VALIDATION blocks for quality gates
- ✅ SKILLS blocks for mandatory skill invocations

**Ready for `/sp.implement` phase** ✅
