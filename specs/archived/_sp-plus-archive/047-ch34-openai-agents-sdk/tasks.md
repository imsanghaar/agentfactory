# Tasks: Chapter 34 - OpenAI Agents SDK (Production Mastery)

**Input**: Design documents from `/specs/047-ch34-openai-agents-sdk/`
**Prerequisites**: spec.md, plan.md
**Constitution**: v7.0.0 (Agent Factory Paradigm)
**Generated**: 2025-12-29

## Format: `[ID] [P?] [Lesson] Description`

- **[P]**: Can run in parallel (independent lessons)
- **[Lesson]**: Which lesson/phase this task belongs to (L00-L10, QUIZ)
- Absolute file paths required for all output

## Output Paths

```
apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/
├── 00-build-your-openai-agents-skill.md    # L00 - Skill Building
├── 01-sdk-setup-first-agent.md              # L01
├── 02-function-tools-context-objects.md     # L02
├── 03-agents-as-tools-orchestration.md      # L03
├── 04-handoffs-message-filtering.md         # L04
├── 05-guardrails-agent-validation.md        # L05
├── 06-sessions-conversation-memory.md       # L06
├── 07-tracing-hooks-observability.md        # L07
├── 08-mcp-integration.md                    # L08
├── 09-rag-filesearchtool.md                 # L09
├── 10-capstone-customer-support.md          # L10
└── 11-chapter-quiz.md                       # Quiz
```

---

## Phase 1: Setup & Skill Building (L00)

**Purpose**: Build OpenAI Agents SDK skill via Skill-First pattern before lesson implementation

**Goal**: Create `openai-agents` skill grounded in official documentation

- [x] T001 [L00] Clone skills-lab fresh for Chapter 34 work
  ```bash
  cd /mnt/c/Users/HP/Documents/colearning-python
  ```

- [x] T002 [L00] Write LEARNING-SPEC.md for OpenAI Agents SDK skill
  - What: Production agent development with OpenAI Agents SDK
  - Why: Enable students to build Digital FTEs
  - Success criteria: Can build multi-agent systems with context, handoffs, guardrails, sessions, tracing, MCP, RAG

- [x] T003 [L00] Fetch OpenAI Agents SDK documentation via Context7
  - **Skill**: `fetching-library-docs`
  - Library: `openai-agents-python`
  - Focus: Agent class, Runner, tools, handoffs, sessions, tracing, MCP

- [x] T004 [L00] Research GitHub examples for production patterns
  - Source: `github.com/openai/openai-agents-python/examples/`
  - Patterns: customer_service, financial_research_agent, agent_patterns, memory, mcp

- [x] T005 [L00] Create/update `building-with-openai-agents` skill
  - **Skill**: `creating-skills`
  - Location: `/mnt/c/Users/HP/Documents/colearning-python/.claude/skills/building-with-openai-agents/SKILL.md`
  - Include: Persona, Logic, Context, MCP references, API patterns, Safety guardrails

- [x] T006 [L00] Verify skill produces consistent outputs
  - Test: Build simple agent with skill guidance
  - Validate: Patterns match official examples

**Checkpoint**: `building-with-openai-agents` skill ready for chapter implementation

---

## Phase 2: Layer 1 - Manual Foundation (L01-L02)

**Purpose**: Students learn SDK primitives manually before AI collaboration

**Layer**: 1 (Manual Foundation - NO AI collaboration yet)

### Lesson 1: SDK Setup & First Agent

**Maps to**: US1 (First Agent with LiteLLM), FR-001 to FR-005, SC-001 (partial)

- [x] T007 [L01] Implement Lesson 1: SDK Setup & First Agent (530 lines)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/01-sdk-setup-first-agent.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-the-2025-inflection-point.md`
  - **SKILLS**:
    - `learning-objectives` (generate measurable outcomes for B1 proficiency)
    - `exercise-designer` (3 exercises: install SDK, run hello world, try LiteLLM)
  - **CONTENT REQUIREMENTS**:
    - Show `pip install openai-agents` and `pip install "openai-agents[litellm]"`
    - Demonstrate `OPENAI_API_KEY` configuration
    - Implement basic Agent → Runner.run_sync() pattern
    - Show LitellmModel with Anthropic
    - Explain `set_tracing_disabled(True)` for non-OpenAI
  - **Doc**: Fetch OpenAI Agents SDK docs via Context7 for Agent/Runner patterns
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)

- [x] T008 [L01] Verify L01 code examples execute correctly
  - Test all code blocks against live API
  - Capture execution logs

### Lesson 2: Function Tools & Context Objects

**Maps to**: US2 (Context Objects for State), FR-006 to FR-010, SC-001

- [x] T009 [L02] Implement Lesson 2: Function Tools & Context Objects (526 lines)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/02-function-tools-context-objects.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - Quality reference: same as T007
  - **SKILLS**:
    - `learning-objectives` (B1 proficiency)
    - `exercise-designer` (3 exercises: @function_tool, Pydantic context, TaskManagerContext)
  - **CONTENT REQUIREMENTS**:
    - Implement @function_tool with type hints and docstrings
    - Create TaskManagerContext Pydantic model
    - Demonstrate `RunContextWrapper[ContextType]` in tool signature
    - Show context mutations persisting across tool calls
    - Build TaskManager with context tracking
  - **Doc**: Fetch OpenAI Agents SDK docs via Context7 for function_tool decorator
  - **VALIDATION**: educational-validator (MUST PASS)

- [x] T010 [L02] Verify L02 code examples execute correctly
  - Test context persistence patterns
  - Capture execution logs

**Checkpoint**: Layer 1 complete - students have manual SDK foundation

---

## Phase 3: Layer 2 - AI Collaboration (L03-L07)

**Purpose**: Students experience Three Roles (Teacher/Student/Co-Worker) through practice

**Layer**: 2 (AI Collaboration - Three Roles demonstrations, INVISIBLE framework)

### Lesson 3: Agents as Tools & Orchestration

**Maps to**: US3 (Agents as Tools), US4 (Agent Cloning), FR-011 to FR-015, SC-002

- [ ] T011 [L03] Implement Lesson 3: Agents as Tools & Orchestration
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/03-agents-as-tools-orchestration.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - `learning-objectives` (B1-B2 proficiency)
    - `exercise-designer` (3 exercises)
    - `ai-collaborate-teaching` (Three Roles: Teacher suggests patterns, Student validates, Co-Worker iterates)
  - **CONTENT REQUIREMENTS**:
    - Demonstrate `agent.as_tool(tool_name, tool_description)`
    - Implement `custom_output_extractor` for structured outputs
    - Show orchestrator pattern (manager calls sub-agents)
    - Demonstrate `agent.clone(tools=[...])` for dynamic composition
    - Contrast with handoff pattern (who owns conversation)
  - **THREE ROLES** (invisible, no framework labels):
    - AI as Teacher: Suggests agent.as_tool() pattern
    - AI as Student: Learns student's information needs
    - Co-Worker: Iterates toward dynamic composition
  - **Doc**: Fetch financial_research_agent example patterns
  - **VALIDATION**: educational-validator (MUST PASS)

- [ ] T012 [L03] Verify L03 code examples execute correctly

### Lesson 4: Handoffs & Message Filtering

**Maps to**: US5 (Handoff Callbacks), US6 (Message Filtering), FR-016 to FR-020, SC-003

- [ ] T013 [L04] Implement Lesson 4: Handoffs & Message Filtering
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/04-handoffs-message-filtering.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - `learning-objectives` (B1-B2)
    - `exercise-designer` (3 exercises)
    - `ai-collaborate-teaching` (Three Roles)
  - **CONTENT REQUIREMENTS**:
    - Implement basic handoffs list: `handoffs=[agent1, agent2]`
    - Demonstrate `handoff(agent, on_handoff=callback)` pattern
    - Implement `input_filter` with `HandoffInputData`
    - Show `handoff_filters.remove_all_tools` usage
    - Demonstrate bidirectional handoffs (specialist → triage)
  - **Doc**: Fetch handoffs/message_filter.py example patterns
  - **VALIDATION**: educational-validator (MUST PASS)

- [ ] T014 [L04] Verify L04 code examples execute correctly

### Lesson 5: Guardrails & Agent-Based Validation

**Maps to**: US7 (Agent-Based Guardrails), FR-021 to FR-025, SC-004

- [ ] T015 [L05] Implement Lesson 5: Guardrails & Agent-Based Validation
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/05-guardrails-agent-validation.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - `learning-objectives` (B2)
    - `exercise-designer` (3 exercises)
    - `ai-collaborate-teaching` (Three Roles)
  - **CONTENT REQUIREMENTS**:
    - Implement `@input_guardrail` with tripwire
    - Implement `@output_guardrail` with structured output check
    - Demonstrate agent-based guardrail (guardrail calls agent)
    - Handle `InputGuardrailTripwireTriggered` exception
    - Show practical PII/topic detection example
  - **Doc**: Fetch agent_patterns/input_guardrails.py example
  - **VALIDATION**: educational-validator (MUST PASS)

- [ ] T016 [L05] Verify L05 code examples execute correctly

### Lesson 6: Sessions & Conversation Memory

**Maps to**: US8 (SQLite Sessions), US9 (Advanced Sessions), FR-026 to FR-030, SC-005

- [ ] T017 [L06] Implement Lesson 6: Sessions & Conversation Memory
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/06-sessions-conversation-memory.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - `learning-objectives` (B2)
    - `exercise-designer` (3 exercises)
    - `ai-collaborate-teaching` (Three Roles)
  - **CONTENT REQUIREMENTS**:
    - Implement `SQLiteSession(session_id)` basic usage
    - Show file-based persistence: `SQLiteSession(id, "file.db")`
    - Demonstrate `session.get_items(limit=N)`
    - Implement `AdvancedSQLiteSession` with usage tracking
    - Show conversation branching with `create_branch_from_turn()`
  - **Doc**: Fetch memory/sqlite_session_example.py patterns
  - **VALIDATION**: educational-validator (MUST PASS)

- [ ] T018 [L06] Verify L06 code examples execute correctly

### Lesson 7: Tracing, Hooks & Observability

**Maps to**: US10 (Lifecycle Hooks), US11 (Tracing), FR-031 to FR-035, SC-006, SC-007

- [ ] T019 [L07] Implement Lesson 7: Tracing, Hooks & Observability
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/07-tracing-hooks-observability.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - `learning-objectives` (B2 → C1)
    - `exercise-designer` (3 exercises)
    - `ai-collaborate-teaching` (Three Roles)
  - **CONTENT REQUIREMENTS**:
    - Implement `RunHooks` with all lifecycle methods
    - Demonstrate `gen_trace_id()` and dashboard URL construction
    - Implement `custom_span()` for sub-operations
    - Show `group_id` for linking conversation turns
    - Track `context.usage` for token monitoring
  - **Doc**: Fetch basic/lifecycle_example.py patterns
  - **VALIDATION**: educational-validator (MUST PASS)

- [ ] T020 [L07] Verify L07 code examples execute correctly

**Checkpoint**: Layer 2 complete - students mastered AI collaboration with SDK

---

## Phase 4: Layer 3 - Intelligence Design (L08-L09)

**Purpose**: Students create reusable skills from accumulated patterns

**Layer**: 3 (Intelligence Design - Create reusable MCP and RAG skills)

### Lesson 8: MCP Integration

**Maps to**: US12 (MCP Integration), FR-036 to FR-041, SC-008

- [ ] T021 [L08] Implement Lesson 8: MCP Integration
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/08-mcp-integration.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - `learning-objectives` (C1)
    - `exercise-designer` (3 exercises)
    - `ai-collaborate-teaching` (Three Roles)
  - **CONTENT REQUIREMENTS**:
    - Demonstrate `MCPServerStreamableHttp` with remote server URL
    - Connect to Context7 MCP server for documentation lookup
    - Show `mcp_servers=[server]` parameter on Agent
    - Implement agent that uses MCP tools (resolve-library-id, get-library-docs)
    - Handle async context manager pattern for MCP server lifecycle
    - Show practical example: TaskManager getting library documentation
  - **SKILL CREATION**: Guide students to create `mcp-agent-integration` skill
  - **Doc**: Fetch Context7 MCP integration patterns
  - **VALIDATION**: educational-validator (MUST PASS)

- [ ] T022 [L08] Verify L08 code examples execute correctly

### Lesson 9: RAG with FileSearchTool

**Maps to**: US13 (RAG with FileSearchTool), FR-042 to FR-047, SC-009

- [ ] T023 [L09] Implement Lesson 9: RAG with FileSearchTool
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/09-rag-filesearchtool.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - `learning-objectives` (C1)
    - `exercise-designer` (3 exercises)
    - `ai-collaborate-teaching` (Three Roles)
  - **CONTENT REQUIREMENTS**:
    - Demonstrate `FileSearchTool` with vector_store_ids
    - Explain OpenAI hosted vector store creation (dashboard or API)
    - Show `max_num_results` parameter for controlling retrieval
    - Implement agentic RAG pattern (agent decides when to retrieve)
    - Demonstrate grounded responses from retrieved content
    - Show practical example: TaskManager with project knowledge base
  - **SKILL CREATION**: Guide students to create `agentic-rag-integration` skill
  - **Doc**: Fetch OpenAI FileSearchTool documentation
  - **VALIDATION**: educational-validator (MUST PASS)

- [ ] T024 [L09] Verify L09 code examples execute correctly

**Checkpoint**: Layer 3 complete - students created reusable MCP and RAG skills

---

## Phase 5: Layer 4 - Spec-Driven Capstone (L10)

**Purpose**: Students build production Digital FTE using spec-first approach

**Layer**: 4 (Spec-Driven Integration - Spec FIRST, then implementation)

### Lesson 10: Capstone - Customer Support Digital FTE

**Maps to**: US14 (Full Customer Support FTE), FR-048 to FR-055, SC-010, SC-011, SC-012

- [ ] T025 [L10] Implement Lesson 10: Capstone - Customer Support Digital FTE
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/10-capstone-customer-support.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
  - **SKILLS**:
    - `learning-objectives` (C1)
    - `exercise-designer` (capstone project structure)
    - `ai-collaborate-teaching` (Three Roles for implementation phase)
  - **CONTENT REQUIREMENTS**:
    - **Part 1**: Specification writing (spec.md BEFORE code)
    - **Part 2**: Pattern analysis (map L1-L9 patterns to requirements)
    - **Part 3**: Component composition (agents, tools, handoffs, guardrails)
    - **Part 4**: AI orchestration with Three Roles
    - **Part 5**: Validation against spec criteria
    - **Part 6**: Monetization discussion (subscription/success fee/hybrid)
    - **Part 7**: What's Next (Ch42 DISTRIBUTE, Part 7 DEPLOY)
  - **INTEGRATION REQUIREMENTS**:
    - Implement full customer_service pattern from repo
    - Include: context object, tools with context, handoff callbacks
    - Implement bidirectional handoffs between 3+ agents
    - Add input guardrail for abuse detection
    - Trace entire conversation with group_id
    - Implement full conversation loop with `to_input_list()`
    - Integrate MCP (Context7 for documentation lookup)
    - Integrate RAG (FileSearchTool for FAQ knowledge base)
  - **Doc**: Fetch customer_service/main.py complete example
  - **VALIDATION**: educational-validator (MUST PASS)

- [ ] T026 [L10] Verify L10 capstone code is production-ready
  - Full integration test with MCP + RAG
  - Trace generation validation

**Checkpoint**: Layer 4 complete - students built sellable Digital FTE

---

## Phase 6: Chapter Assessment

**Purpose**: Validate student learning across all success criteria

### Chapter Quiz

**Maps to**: SC-001 through SC-012 assessment

- [ ] T027 [QUIZ] Create Chapter 34 Quiz
  - **SUBAGENT**: assessment-architect
  - **SKILL**: `assessment-builder`
    - 50 questions covering all 12 success criteria
    - Question distribution:
      - SC-001 (Context): 4 questions
      - SC-002 (Orchestrator): 4 questions
      - SC-003 (Handoffs): 4 questions
      - SC-004 (Guardrails): 4 questions
      - SC-005 (Sessions): 4 questions
      - SC-006 (Hooks): 4 questions
      - SC-007 (Tracing): 4 questions
      - SC-008 (MCP): 5 questions
      - SC-009 (RAG): 5 questions
      - SC-010 (Capstone integration): 5 questions
      - SC-011 (Monetization): 3 questions
      - SC-012 (Journey): 4 questions
    - Bloom's distribution: 60%+ non-recall (Apply, Analyze, Evaluate)
  - Output path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/11-chapter-quiz.md`
  - **SKILL**: `quiz-generator` for formatting

- [ ] T028 [QUIZ] Validate quiz answer distribution
  - **SKILL**: `quiz-generator` (redistribute_answers.py)
  - Ensure no answer bias

**Checkpoint**: Assessment complete - chapter ready for validation

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final quality checks and consistency validation

- [ ] T029 [P] Update Chapter README with final lesson list
  - Path: `/mnt/c/Users/HP/Documents/colearning-python/apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/README.md`
  - Verify Digital FTE journey table accurate

- [ ] T030 [P] Verify TaskManager running example consistency across L01-L09
  - TaskManager should evolve progressively
  - No contradictions between lessons

- [ ] T031 [P] Validate all code examples have execution logs
  - Every code block tested against live API

- [ ] T032 Run full chapter validation
  - **SUBAGENT**: validation-auditor
  - Check:
    - Layer progression (L1 → L2 → L3 → L4)
    - Three Roles present in L2 lessons (invisible)
    - Zero meta-commentary violations
    - All 12 success criteria mapped
    - All 55 functional requirements covered
    - Capstone includes monetization and journey

- [ ] T033 Verify all lessons pass educational-validator
  - Re-run validation on any lessons that were modified

- [ ] T034 Generate chapter summary for part-level index
  - Update Part 6 README if needed

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup/Skill) → Phase 2 (L1-L2) → Phase 3 (L3-L7) → Phase 4 (L8-L9) → Phase 5 (L10) → Phase 6 (Quiz) → Phase 7 (Polish)
```

### Layer Dependencies

| Layer | Lessons | Depends On |
|-------|---------|------------|
| Layer 1 | L01-L02 | Phase 1 complete |
| Layer 2 | L03-L07 | L01-L02 complete |
| Layer 3 | L08-L09 | L01-L07 complete |
| Layer 4 | L10 | L01-L09 complete |

### Parallel Opportunities

**Within Phase 2** (after L01 complete):
- T009 (L02) can start after T007-T008 complete

**Within Phase 3** (lessons are sequential):
- Each lesson builds on previous - NOT parallelizable

**Within Phase 7** (Polish):
- T029, T030, T031 can run in parallel

---

## User Story to Task Mapping

| User Story | Priority | Task(s) | Lesson |
|------------|----------|---------|--------|
| US1 (First Agent) | P1 | T007-T008 | L01 |
| US2 (Context Objects) | P1 | T009-T010 | L02 |
| US3 (Agents as Tools) | P1 | T011-T012 | L03 |
| US4 (Agent Cloning) | P2 | T011-T012 | L03 |
| US5 (Handoff Callbacks) | P1 | T013-T014 | L04 |
| US6 (Message Filtering) | P2 | T013-T014 | L04 |
| US7 (Agent Guardrails) | P1 | T015-T016 | L05 |
| US8 (SQLite Sessions) | P2 | T017-T018 | L06 |
| US9 (Advanced Sessions) | P3 | T017-T018 | L06 |
| US10 (Lifecycle Hooks) | P2 | T019-T020 | L07 |
| US11 (Tracing) | P2 | T019-T020 | L07 |
| US12 (MCP Integration) | P1 | T021-T022 | L08 |
| US13 (RAG FileSearchTool) | P1 | T023-T024 | L09 |
| US14 (Customer Support FTE) | P1 | T025-T026 | L10 |

---

## Success Criteria Coverage

| SC | Description | Task(s) | Verified By |
|----|-------------|---------|-------------|
| SC-001 | Context objects persist | T009, T011, T025 | L02, L03, L10 validation |
| SC-002 | Orchestrator with 3+ agents | T011, T025 | L03, L10 validation |
| SC-003 | Handoff with callback | T013, T025 | L04, L10 validation |
| SC-004 | Agent-based guardrail | T015, T025 | L05, L10 validation |
| SC-005 | AdvancedSQLiteSession branching | T017, T025 | L06, L10 validation |
| SC-006 | Full RunHooks | T019, T025 | L07, L10 validation |
| SC-007 | Multi-agent tracing | T019, T025 | L07, L10 validation |
| SC-008 | MCP StreamableHTTP | T021, T025 | L08, L10 validation |
| SC-009 | Agentic RAG | T023, T025 | L09, L10 validation |
| SC-010 | Capstone integration | T025 | L10 validation |
| SC-011 | Monetization articulation | T025 | L10 validation |
| SC-012 | Journey understanding | T025 | L10 validation |

---

## Implementation Strategy

### MVP First (L01-L02 Only)

1. Complete Phase 1: Setup/Skill building
2. Complete T007-T010: L01-L02
3. **STOP and VALIDATE**: Test Layer 1 foundation
4. Students can run basic agents before continuing

### Incremental Delivery

1. L01-L02 → Manual foundation ready
2. L03-L07 → AI collaboration mastered
3. L08-L09 → Skills created
4. L10 → Digital FTE built
5. Quiz → Learning validated

---

## Notes

- All lessons use content-implementer subagent for quality consistency
- All lessons require educational-validator PASS before marking complete
- Code examples MUST be tested against live API
- Three Roles framework INVISIBLE in student-facing content
- Skill invocations documented in each task for reproducibility
- Total: 34 tasks covering 10 lessons + quiz + polish
