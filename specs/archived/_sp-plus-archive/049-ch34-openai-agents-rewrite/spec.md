# Feature Specification: Chapter 34 - OpenAI Agents SDK (Complete Rewrite)

**Feature Branch**: `feature/049-ch34-openai-agents-rewrite`
**Created**: 2025-12-29
**Status**: Draft
**Proficiency Level**: B1-B2 (Build production agents with SDK)
**Source Material**: `context/17_ai_agents_first/` (28 lessons) + Context7 SDK docs

## Vision

This chapter teaches students to build production-ready AI agents using OpenAI's official Agents SDK. Following the Skill-First Learning Pattern, students build an `openai-agents` skill BEFORE learning the SDK, ensuring all knowledge is grounded in official documentation rather than AI memory.

By chapter end, students will have:
1. A production-ready `openai-agents` skill
2. Mastery of all SDK primitives (Agent, Runner, tools, handoffs, guardrails, sessions)
3. A capstone multi-agent customer support system

---

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Agent taxonomy, architecture patterns, agent loops (Chapter 33)
- Python async/await, type hints, Pydantic models (Part 5)
- Specification-driven development workflow (Part 4)
- Skill creation with `/skill-creator` and `/fetching-library-docs` (Chapter 5)

**What this chapter teaches from scratch**:
- OpenAI Agents SDK installation and configuration
- Agent class (dataclass design), Runner class (execution engine)
- @function_tool decorator for tool creation
- Context objects (Pydantic models for cross-agent state)
- Streaming with Runner.run_streamed()
- Agents as tools vs handoffs (when to use each)
- Agent.clone() for dynamic composition
- Handoff callbacks and message filters
- Input/output guardrails with tripwires
- SQLiteSession and AdvancedSQLiteSession for memory
- Tracing with gen_trace_id(), custom_span(), group_id
- MCP integration via MCPServerStreamableHttp
- FileSearchTool for agentic RAG

---

## Chapter Structure (13 Lessons)

Based on reference material from `context/17_ai_agents_first/` consolidated for book format:

| Lesson | Title | Reference Material |
|--------|-------|-------------------|
| L00 | Build Your OpenAI Agents Skill | Skill-First Pattern |
| L01 | SDK Setup & First Agent | 02_get_api_key, 03_hello_agent |
| L02 | Agent Configuration & Dynamic Instructions | 04_model_configuration, 06_model_settings, 08_dynamic_instructions |
| L03 | Function Tools & Structured Output | 05_basic_tools, 07_local_context, 14_advanced_tools, 16_structured_output |
| L04 | Agents as Tools & Cloning | 10_agent_clone, 12_agents_as_tool |
| L05 | Handoffs & Message Filtering | 13_basic_handsoff, 15_advanced_handoffs |
| L06 | Streaming Responses | 09_streaming |
| L07 | Guardrails & Validation | 17_guardrails |
| L08 | Tracing, Lifecycle & Hooks | 11_basic_tracing, 18_agent_lifecycle, 19_run_lifecycle, 24_external_tracing |
| L09 | Sessions & Memory Management | 20_session_memory, 21_memory_management, 25_sessions_context |
| L10 | RAG with FileSearch | 26_managed_rag_service |
| L11 | MCP Integration | 28_mcp_10x_development |
| L12 | Capstone - Customer Support FTE | Full integration |

---

## User Scenarios & Testing

### User Story 1 - Skill-First Foundation (Priority: P1)

Student builds an `openai-agents` skill before learning SDK details, ensuring grounded knowledge.

**Why this priority**: Skill-First pattern prevents hallucinated APIs and ensures first-time quality.

**Independent Test**: Student has working skill in `.claude/skills/openai-agents/` that generates correct SDK code.

**Acceptance Scenarios**:

1. **Given** skills-lab cloned, **When** student runs `/fetching-library-docs openai-agents-sdk`, **Then** official documentation retrieved
2. **Given** documentation fetched, **When** student runs `/skill-creator`, **Then** initial skill created with Agent, Runner, tools patterns
3. **Given** skill created, **When** student tests with sample prompt, **Then** generates valid SDK code

---

### User Story 2 - First Agent with Hello World (Priority: P1)

Student creates and runs their first agent using the SDK.

**Why this priority**: Foundation for all subsequent lessons.

**Independent Test**: Student runs `hello_agent.py` and receives response from agent.

**Acceptance Scenarios**:

1. **Given** `pip install openai-agents` completed, **When** student imports Agent, Runner, **Then** no import errors
2. **Given** `OPENAI_API_KEY` set, **When** student runs basic agent, **Then** response received within 10 seconds
3. **Given** agent with instructions, **When** `Runner.run_sync(agent, "Hello")` called, **Then** result.final_output contains response

---

### User Story 3 - Tool-Augmented Agent (Priority: P1)

Student creates agents with function tools that interact with external systems.

**Why this priority**: Tools are core to agent functionality.

**Independent Test**: Agent successfully calls tool and uses result in response.

**Acceptance Scenarios**:

1. **Given** `@function_tool` decorated function, **When** agent needs information, **Then** tool called automatically
2. **Given** tool with type hints and docstring, **When** agent runs, **Then** schema auto-generated from signature
3. **Given** Pydantic output_type, **When** agent responds, **Then** structured data returned

---

### User Story 4 - Multi-Agent Handoffs (Priority: P1)

Student implements agent-to-agent handoffs for specialized task routing.

**Why this priority**: Production systems require multi-agent coordination.

**Independent Test**: Triage agent correctly routes to specialist agents.

**Acceptance Scenarios**:

1. **Given** triage agent with `handoffs=[billing_agent, refund_agent]`, **When** billing question asked, **Then** handoff to billing_agent
2. **Given** `handoff(agent, on_handoff=callback)`, **When** handoff occurs, **Then** callback runs before target agent
3. **Given** `input_filter` on handoff, **When** handoff occurs, **Then** message history filtered

---

### User Story 5 - Agent Safety with Guardrails (Priority: P1)

Student implements input/output validation to prevent misuse.

**Why this priority**: Production agents require safety mechanisms.

**Independent Test**: Inappropriate requests blocked before reaching main agent.

**Acceptance Scenarios**:

1. **Given** `@input_guardrail` with tripwire, **When** bad input detected, **Then** `InputGuardrailTripwireTriggered` raised
2. **Given** guardrail agent for detection, **When** parallel validation runs, **Then** full LLM reasoning available
3. **Given** `@output_guardrail`, **When** sensitive data in output, **Then** response blocked

---

### User Story 6 - Persistent Conversations (Priority: P2)

Student implements session memory for multi-turn conversations.

**Why this priority**: Chat applications require conversation persistence.

**Independent Test**: Agent remembers information across multiple runs.

**Acceptance Scenarios**:

1. **Given** `SQLiteSession("user_123")`, **When** multiple runs with same session, **Then** history preserved
2. **Given** `session.get_items(limit=10)`, **When** called, **Then** returns last 10 conversation items
3. **Given** persistent session file, **When** process restarts, **Then** conversation continues

---

### User Story 7 - Observable Agent Behavior (Priority: P2)

Student implements tracing for debugging and monitoring.

**Why this priority**: Production debugging requires visibility.

**Independent Test**: Agent runs visible in OpenAI tracing dashboard.

**Acceptance Scenarios**:

1. **Given** `gen_trace_id()`, **When** passed to run, **Then** dashboard URL constructible
2. **Given** `group_id` parameter, **When** multiple runs share it, **Then** grouped in dashboard
3. **Given** `RunHooks` with lifecycle methods, **When** agent runs, **Then** all events logged

---

### User Story 8 - MCP Tool Integration (Priority: P2)

Student connects agents to MCP servers for external tool access.

**Why this priority**: MCP enables agent tool ecosystems.

**Independent Test**: Agent uses Context7 MCP server to retrieve documentation.

**Acceptance Scenarios**:

1. **Given** `MCPServerStreamableHttp` configured, **When** agent runs, **Then** MCP tools available
2. **Given** Context7 server connected, **When** user asks about library, **Then** agent retrieves documentation
3. **Given** multiple MCP servers, **When** configured, **Then** all tools accessible

---

### User Story 9 - RAG-Enabled Agent (Priority: P2)

Student implements retrieval-augmented generation with FileSearchTool.

**Why this priority**: Knowledge bases enhance agent capabilities.

**Independent Test**: Agent retrieves and cites information from vector store.

**Acceptance Scenarios**:

1. **Given** `FileSearchTool(vector_store_ids=[...])`, **When** agent needs facts, **Then** retrieval occurs
2. **Given** retrieved chunks, **When** agent responds, **Then** answer grounded in content
3. **Given** agentic RAG pattern, **When** user asks factual question, **Then** agent decides when to retrieve

---

### User Story 10 - Production Customer Support System (Priority: P1)

Student builds complete multi-agent system integrating all skills.

**Why this priority**: Capstone validates all learning.

**Independent Test**: Full customer support conversation with routing, memory, and safety.

**Acceptance Scenarios**:

1. **Given** triage + specialist agents, **When** user asks FAQ, **Then** routed to FAQ agent
2. **Given** guardrails on triage, **When** abuse detected, **Then** request blocked
3. **Given** session memory, **When** conversation spans multiple turns, **Then** context preserved
4. **Given** MCP + RAG, **When** user needs documentation, **Then** retrieved and cited

---

### Edge Cases

- What happens when API key is invalid or missing?
- How does agent behave when tool raises exception?
- What happens when handoff creates circular routing?
- How does guardrail handle ambiguous edge cases?
- What happens when session storage fails?
- How does streaming handle network interruption?

---

## Requirements

### Functional Requirements

#### L00: Build Your OpenAI Agents Skill
- **FR-001**: MUST clone fresh skills-lab repository
- **FR-002**: MUST write LEARNING-SPEC.md with goals
- **FR-003**: MUST use `/fetching-library-docs openai-agents-sdk` for official docs
- **FR-004**: MUST use `/skill-creator` to build initial skill
- **FR-005**: MUST verify skill generates correct SDK code

#### L01: SDK Setup & First Agent
- **FR-006**: MUST show `pip install openai-agents` installation
- **FR-007**: MUST demonstrate `OPENAI_API_KEY` configuration
- **FR-008**: MUST explain Agent class as dataclass design
- **FR-009**: MUST implement `Runner.run_sync()` pattern
- **FR-010**: MUST show async `await Runner.run()` alternative

#### L02: Agent Configuration & Dynamic Instructions
- **FR-011**: MUST demonstrate model selection (gpt-4o, gpt-4o-mini)
- **FR-012**: MUST show LiteLLM integration for other providers
- **FR-013**: MUST implement dynamic instructions (callable returning string)
- **FR-014**: MUST explain temperature, top_p parameters
- **FR-015**: MUST show `set_tracing_disabled(True)` for non-OpenAI models

#### L03: Function Tools & Structured Output
- **FR-016**: MUST implement `@function_tool` decorator pattern
- **FR-017**: MUST show type hints and docstrings for schema generation
- **FR-018**: MUST demonstrate tool with Pydantic input validation
- **FR-019**: MUST implement context access via `RunContextWrapper`
- **FR-020**: MUST show `output_type=PydanticModel` for structured responses

#### L04: Agents as Tools & Cloning
- **FR-021**: MUST implement `agent.as_tool(tool_name, tool_description)`
- **FR-022**: MUST demonstrate `custom_output_extractor` for result formatting
- **FR-023**: MUST contrast agents-as-tools vs handoffs (ownership)
- **FR-024**: MUST implement `agent.clone(tools=[...])` for dynamic composition
- **FR-025**: MUST show orchestrator pattern calling multiple sub-agents

#### L05: Handoffs & Message Filtering
- **FR-026**: MUST implement `handoffs=[agent1, agent2]` list
- **FR-027**: MUST demonstrate `handoff(agent, on_handoff=callback)`
- **FR-028**: MUST implement `input_filter` with `HandoffInputData`
- **FR-029**: MUST show `handoff_filters.remove_all_tools`
- **FR-030**: MUST implement bidirectional handoffs (back to triage)

#### L06: Streaming Responses
- **FR-031**: MUST implement `Runner.run_streamed()` pattern
- **FR-032**: MUST handle `stream_events()` async iteration
- **FR-033**: MUST process `tool_call_output_item` and `message_output_item`
- **FR-034**: MUST use `ItemHelpers.text_message_output()` for display
- **FR-035**: MUST handle streaming with tools

#### L07: Guardrails & Validation
- **FR-036**: MUST implement `@input_guardrail` with tripwire
- **FR-037**: MUST implement `@output_guardrail` for response validation
- **FR-038**: MUST demonstrate agent-based guardrail (guardrail calls agent)
- **FR-039**: MUST handle `InputGuardrailTripwireTriggered` exception
- **FR-040**: MUST show practical PII/abuse detection example

#### L08: Tracing, Lifecycle & Hooks
- **FR-041**: MUST implement `RunHooks` with lifecycle methods
- **FR-042**: MUST demonstrate `gen_trace_id()` and dashboard URL
- **FR-043**: MUST implement `custom_span()` for sub-operations
- **FR-044**: MUST show `group_id` for linking conversation turns
- **FR-045**: MUST track `context.usage` for token monitoring

#### L09: Sessions & Memory Management
- **FR-046**: MUST implement `SQLiteSession(session_id)` basic usage
- **FR-047**: MUST show persistent storage: `SQLiteSession(id, "file.db")`
- **FR-048**: MUST demonstrate `session.get_items(limit=N)`
- **FR-049**: MUST implement memory operations: add_items, pop_item, clear_session
- **FR-050**: MUST show AdvancedSQLiteSession with branching

#### L10: RAG with FileSearch
- **FR-051**: MUST demonstrate `FileSearchTool(vector_store_ids=[...])`
- **FR-052**: MUST explain OpenAI hosted vector store creation
- **FR-053**: MUST implement agentic RAG (agent decides when to retrieve)
- **FR-054**: MUST show grounded responses from retrieved content

#### L11: MCP Integration
- **FR-055**: MUST demonstrate `MCPServerStreamableHttp` configuration
- **FR-056**: MUST connect to Context7 MCP server
- **FR-057**: MUST show `mcp_servers=[server]` on Agent
- **FR-058**: MUST implement agent using MCP tools

#### L12: Capstone - Customer Support FTE
- **FR-059**: MUST implement context object (CustomerContext Pydantic model)
- **FR-060**: MUST create 3+ specialized agents (triage, FAQ, booking)
- **FR-061**: MUST implement bidirectional handoffs
- **FR-062**: MUST add input guardrail for abuse detection
- **FR-063**: MUST implement session memory for conversation
- **FR-064**: MUST integrate MCP for documentation lookup
- **FR-065**: MUST integrate RAG for FAQ knowledge base
- **FR-066**: MUST implement full conversation loop with `to_input_list()`

---

### Key Entities

- **Agent**: LLM with instructions, tools, and handoff capabilities
- **Runner**: Execution engine that runs agents and manages the agent loop
- **Tool**: Function that agent can call to interact with external systems
- **Handoff**: Mechanism for transferring control between agents
- **Guardrail**: Input/output validation with tripwire mechanism
- **Session**: Conversation memory storage (SQLite, Redis, custom)
- **Context**: Pydantic model for state shared across agents
- **Trace**: Debugging and monitoring record of agent execution

---

## Success Criteria

- **SC-001**: Students have working `openai-agents` skill grounded in official docs
- **SC-002**: Students can create agents with function tools
- **SC-003**: Students can implement multi-agent handoffs with callbacks
- **SC-004**: Students can add input/output guardrails with tripwires
- **SC-005**: Students can implement session memory for conversations
- **SC-006**: Students can trace agent behavior with custom spans
- **SC-007**: Students can connect agents to MCP servers
- **SC-008**: Students can implement agentic RAG with FileSearchTool
- **SC-009**: Capstone integrates all components into production-ready system
- **SC-010**: Chapter quiz validates understanding of all patterns

---

## Dependencies

- **Chapter 33**: Agent concepts (taxonomy, architecture, patterns)
- **Part 5**: Python fundamentals (async, Pydantic, type hints)
- **Chapter 5**: Skill creation tools (`/skill-creator`, `/fetching-library-docs`)
- **Part 4**: SDD-RI workflow for capstone

## Out of Scope

- Voice/realtime agents (specialized extension)
- Deployment infrastructure (Part 7)
- Custom model training/fine-tuning
- Enterprise SSO/authentication patterns
- OpenAI Assistants API (different from Agents SDK)

---

## Sources

- [OpenAI Agents SDK Documentation](https://openai.github.io/openai-agents-python/)
- [OpenAI Agents SDK GitHub](https://github.com/openai/openai-agents-python)
- [OpenAI Platform Agents Guide](https://platform.openai.com/docs/guides/agents-sdk)
- [PyPI openai-agents](https://pypi.org/project/openai-agents/)
