# Feature Specification: Chapter 41 - ChatKit Server for Agents

**Feature Branch**: `1-ch41-chatkit-server`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "Implement Chapter 41: ChatKit Server for Agents - 8 lessons covering ChatKit architecture, agent integration, streaming, conversation management, session lifecycle, authentication, UI integration, and capstone"

## Educational Content Metadata

**Part**: 6 - AI Native Software Development
**Chapter Number**: 41
**Chapter Title**: ChatKit Server for Agents
**Proficiency Level**: B1 (Intermediate)
**Prerequisites**:
- Chapter 40: FastAPI for Agents (API fundamentals)
- Chapters 34-36: Agent SDK experience (OpenAI, Google, Anthropic)
- Part 5: Python Fundamentals (async/await, streaming patterns)

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Building REST APIs with FastAPI (Chapter 40)
- Creating agents with OpenAI/Google/Anthropic SDKs (Chapters 34-36)
- Python async/await patterns and asyncio (Chapter 31)
- Pydantic models for data validation (Chapter 30)
- HTTP request/response lifecycle and status codes
- Basic authentication concepts (tokens, headers)

**What this chapter must explain from scratch**:
- ChatKit Server architecture and conversation primitives
- Streaming vs request/response patterns for conversational AI
- Thread and ThreadItem lifecycle management
- RequestContext for multi-tenant user isolation
- respond() method and event streaming patterns
- Session state management and persistence
- React hooks for chat UI integration (useChatKit)

**Why this distinction matters**:
- Students already know how to build APIs (Ch40) but not conversational services
- They can create agents (Ch34-36) but haven't connected them to persistent chat sessions
- Layer 1 lessons build on API knowledge to introduce conversation primitives

## User Scenarios & Testing

### User Story 1 - Understanding ChatKit Architecture (Priority: P1)

A developer who completed Chapter 40 (FastAPI) and Chapter 34 (OpenAI Agents) needs to understand how ChatKit Server differs from REST APIs and why conversational infrastructure requires different patterns than request/response.

**Why this priority**: Foundation for all subsequent lessons. Without understanding the architecture, students cannot implement the patterns.

**Independent Test**: Student can explain (in writing or verbally) the difference between ChatKitServer.respond() and a FastAPI route handler, and can diagram the ThreadItem lifecycle.

**Acceptance Scenarios**:

1. **Given** a student has built REST APIs in Chapter 40, **When** they read Lesson 1, **Then** they understand why streaming responses require different server patterns than REST endpoints
2. **Given** a student knows OpenAI Agents SDK, **When** they learn ChatKitServer architecture, **Then** they can identify where agent execution fits in the respond() method
3. **Given** a student sees a conversation with 10 messages, **When** they analyze the ThreadItem lifecycle, **Then** they can trace user messages → assistant responses → tool calls flow

---

### User Story 2 - Connecting First Agent to ChatKit (Priority: P1)

A developer needs to take an existing OpenAI agent (from Chapter 34) and wire it into ChatKit Server so users can have streaming conversations with it.

**Why this priority**: First hands-on implementation. Proves ChatKit works with their existing agent knowledge.

**Independent Test**: Student creates a minimal ChatKitServer that responds to user messages by calling an OpenAI agent and streaming results back.

**Acceptance Scenarios**:

1. **Given** an existing OpenAI agent, **When** student implements ChatKitServer.respond(), **Then** the agent processes user messages and streams responses
2. **Given** a user sends "Hello", **When** the ChatKit server receives it, **Then** the response appears token-by-token in real-time
3. **Given** a conversation with 3 messages, **When** student inspects thread storage, **Then** all messages persist correctly

---

### User Story 3 - Implementing Streaming Patterns (Priority: P2)

A developer needs to handle streaming responses properly: token-by-token output, progress indicators for long operations, and handling interruptions when users send new messages before responses complete.

**Why this priority**: Core UX pattern for conversational AI. Without proper streaming, chat feels unresponsive.

**Independent Test**: Student implements streaming with stream_agent_response() helper and can demonstrate partial responses appearing in real-time.

**Acceptance Scenarios**:

1. **Given** an agent generating a long response, **When** tokens stream back, **Then** each token appears immediately (not buffered until complete)
2. **Given** an agent performing a 10-second operation, **When** it streams progress events, **Then** UI shows "Analyzing documents..." during execution
3. **Given** a user sends a new message mid-response, **When** the server handles interruption, **Then** the previous stream terminates and new response begins

---

### User Story 4 - Managing Conversation History (Priority: P2)

A developer needs to persist conversation history, include it in agent prompts, and handle context window limits when conversations grow long.

**Why this priority**: Agents need conversation memory to provide contextual responses. Critical for useful chat experiences.

**Independent Test**: Student implements history persistence where agents reference previous messages in their responses.

**Acceptance Scenarios**:

1. **Given** a conversation with 10 messages, **When** user asks "What did I ask about earlier?", **Then** agent references previous messages accurately
2. **Given** a thread with 50 messages (exceeding context window), **When** agent responds, **Then** system includes most recent N messages without errors
3. **Given** conversation metadata (user preferences), **When** stored in thread.metadata, **Then** agent can access it across all messages

---

### User Story 5 - Session Lifecycle Management (Priority: P3)

A developer needs to create new chat sessions, resume existing sessions, handle timeouts, and clean up old sessions to prevent resource leaks.

**Why this priority**: Production requirement but not needed for basic functionality. Can defer until deployment.

**Independent Test**: Student implements session create/resume/timeout logic and demonstrates sessions persisting across server restarts.

**Acceptance Scenarios**:

1. **Given** a new user visits, **When** they start chatting, **Then** system creates a new session with unique ID
2. **Given** a user returns after 1 hour, **When** they provide session ID, **Then** conversation history resumes from where they left off
3. **Given** a session inactive for 24 hours, **When** cleanup runs, **Then** session expires and storage reclaims space

---

### User Story 6 - Authentication and Security (Priority: P2)

A developer needs to secure ChatKit endpoints so only authenticated users can access conversations, and ensure users cannot see each other's conversation history.

**Why this priority**: Security is critical before production but not needed for local development/testing.

**Independent Test**: Student implements RequestContext with user_id isolation and demonstrates users cannot access other users' threads.

**Acceptance Scenarios**:

1. **Given** two users (Alice, Bob), **When** each creates conversations, **Then** Alice cannot see Bob's threads and vice versa
2. **Given** an unauthenticated request, **When** it hits ChatKit endpoint, **Then** server returns 401 Unauthorized
3. **Given** a user's JWT token in request header, **When** server validates it, **Then** RequestContext contains correct user_id for all operations

---

### User Story 7 - React UI Integration (Priority: P3)

A developer needs to connect ChatKit's React components to their backend server using useChatKit hook with custom authentication and page context injection.

**Why this priority**: Frontend integration is valuable but optional (built-in UI exists for testing). Can defer to end of chapter.

**Independent Test**: Student creates a React component that uses useChatKit to connect to their ChatKit server with custom fetch interceptor.

**Acceptance Scenarios**:

1. **Given** a React app, **When** student adds useChatKit hook, **Then** chat widget renders and connects to backend
2. **Given** authentication tokens in httpOnly cookies, **When** user sends message, **Then** custom fetch interceptor includes auth headers
3. **Given** user on specific page, **When** they ask question, **Then** page context (URL, title, headings) flows to agent via metadata

---

### User Story 8 - Complete Conversational Agent (Capstone) (Priority: P1)

A developer needs to build a production-ready conversational agent that combines all chapter concepts: ChatKitServer, streaming, history, sessions, authentication, and UI—following spec-driven development from Chapter 14.

**Why this priority**: Validates mastery of all concepts through integrated application. Essential capstone experience.

**Independent Test**: Student writes specification, then implements complete ChatKit-powered agent with persistent conversations and authentication.

**Acceptance Scenarios**:

1. **Given** a product requirement, **When** student writes specification (Layer 4), **Then** spec includes conversation flows, authentication requirements, and session management
2. **Given** approved specification, **When** student implements ChatKitServer, **Then** all requirements pass acceptance tests
3. **Given** deployed agent, **When** multiple users interact simultaneously, **Then** conversations remain isolated and history persists correctly

---

### Edge Cases

- **Rapid message sending**: What happens when user sends 5 messages in 1 second before agent completes first response?
- **Concurrent requests**: How does server handle two browser tabs sending messages to same thread simultaneously?
- **Malformed thread data**: How does system recover if thread storage corrupts?
- **Context window overflow**: What happens when conversation history exceeds LLM's maximum context?
- **Network interruption mid-stream**: How does client handle lost connection during streaming response?
- **Stale session tokens**: What happens when user's JWT expires mid-conversation?
- **Database connection loss**: How does server handle temporary database unavailability?

## Requirements

### Functional Requirements

#### Lesson Structure

- **FR-001**: Chapter MUST contain exactly 8 lessons (L01-L08) following the structure in README.md
- **FR-002**: Each lesson MUST follow 4-Layer Teaching Method progression appropriate to its position
- **FR-003**: L01 MUST be Layer 1 (Manual) teaching ChatKit architecture without AI assistance
- **FR-004**: L02 MUST implement first agent connection with step-by-step guidance
- **FR-005**: L08 (Capstone) MUST be Layer 4 (Spec-Driven) requiring students to write specification first
- **FR-006**: All lessons MUST include full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
- **FR-007**: All lessons MUST include "Try With AI" sections with 3 prompts and "What you're learning" explanations

#### Content Quality

- **FR-008**: All code examples MUST use ChatKit Python SDK 2025 syntax (verified against official docs)
- **FR-009**: All statistics and dates MUST be verified via WebSearch before inclusion
- **FR-010**: Lessons MUST NOT expose pedagogical frameworks through meta-commentary
- **FR-011**: Each lesson MUST include narrative opening (2-3 paragraphs) with real-world scenario
- **FR-012**: All lessons MUST include safety notes relevant to production ChatKit deployment

#### Technical Accuracy

- **FR-013**: Code examples MUST demonstrate correct ChatKitServer inheritance pattern
- **FR-014**: Examples MUST show proper respond() method signature with ThreadMetadata, UserMessageItem, RequestContext
- **FR-015**: Streaming examples MUST use stream_agent_response() helper correctly
- **FR-016**: Authentication examples MUST demonstrate RequestContext user isolation
- **FR-017**: React integration MUST show correct useChatKit hook usage with custom fetch

#### Pedagogical Progression

- **FR-018**: L01 MUST build vocabulary (Thread, ThreadItem, RequestContext, respond()) needed for later lessons
- **FR-019**: L02-L07 MUST build progressively on previous lessons without backtracking
- **FR-020**: L08 capstone MUST require synthesizing all concepts from L01-L07
- **FR-021**: Each lesson MUST connect to Agent Factory paradigm (how this enables Digital FTEs)

### Key Entities

#### Educational Entities

- **Chapter**: Contains 8 lessons, prerequisites, learning outcomes, README.md structure
- **Lesson**: Individual markdown file with YAML frontmatter, narrative opening, concept explanation, code examples, Try With AI section, safety notes
- **Skill**: Proficiency progression mapped to CEFR (B1), Bloom's taxonomy, DigComp framework
- **Learning Objective**: Measurable outcome with assessment method

#### Technical Entities (Content Subject Matter)

- **ChatKitServer**: Python class students extend to implement conversational infrastructure
- **Thread**: Persistent conversation container with metadata and message history
- **ThreadItem**: Individual message (user/assistant/tool call) in conversation
- **RequestContext**: User identity and session information for multi-tenant isolation
- **Event Stream**: Async iterator yielding token-by-token responses

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can explain ChatKit architecture differences from REST APIs (measured via quiz achieving 80%+ on architecture questions)
- **SC-002**: Students successfully wire existing agents (from Ch34-36) into ChatKit within 30 minutes of completing L02
- **SC-003**: Students implement streaming responses that appear token-by-token with <100ms latency per token
- **SC-004**: Students create conversation history that persists across server restarts and correctly includes prior messages in agent prompts
- **SC-005**: Students implement session management where conversations resume correctly after 24-hour gaps
- **SC-006**: Students secure ChatKit endpoints where authentication failures return 401 and user isolation prevents cross-user data access
- **SC-007**: Students integrate React UI that successfully connects to backend with custom authentication within 20 minutes of completing L07
- **SC-008**: 90% of students complete L08 capstone producing working conversational agent that passes all acceptance tests from their specification
- **SC-009**: All code examples execute without errors against ChatKit Python SDK (current 2025 version)
- **SC-010**: All factual claims (release dates, adoption numbers, quotes) verified via WebSearch with sources cited

### Quality Gates

- **SC-011**: All lessons pass educational-validator with zero constitution violations
- **SC-012**: All lessons pass factual-verifier with zero hallucinated statistics or dates
- **SC-013**: Chapter quiz achieves 50 questions covering all 8 lessons with balanced distribution across Bloom's taxonomy levels
- **SC-014**: "Try With AI" sections produce measurable skill improvement (student self-reported confidence increases by 40%+ after completing prompts)

## Dependencies

### Prerequisites (Students Must Have)

- Chapter 40 completion (FastAPI fundamentals)
- Chapters 34-36 completion (Agent SDKs - at least one of OpenAI/Google/Anthropic)
- Part 5 completion (Python async/await, Pydantic, OOP)
- Access to OpenAI API key (for running ChatKit examples)

### Platform Requirements

- Python 3.11+ with uv package manager
- ChatKit Python SDK (`pip install chatkit-sdk`)
- OpenAI Agents SDK (`pip install agents`)
- Node.js 18+ (for React integration lesson)
- PostgreSQL or SQLite (for conversation persistence examples)

### Documentation Dependencies

- Official ChatKit Python SDK docs (https://openai.github.io/chatkit-python/)
- Official ChatKit.js docs (https://openai.github.io/chatkit-js/)
- OpenAI ChatKit advanced samples (https://github.com/openai/openai-chatkit-advanced-samples)

## Assumptions

### Technical Assumptions

1. **ChatKit SDK Version**: Using ChatKit Python SDK as of December 2025 release (current version at time of writing)
2. **Agent SDK Compatibility**: OpenAI Agents SDK patterns from Chapter 34 remain compatible with ChatKit integration
3. **React Version**: Using React 18+ for useChatKit hook examples
4. **Database**: Examples use SQLite for simplicity; production patterns mention PostgreSQL for scaling
5. **Authentication Method**: Examples demonstrate JWT token validation as standard pattern; OAuth2 mentioned for production

### Pedagogical Assumptions

1. **Layer Progression**: L01 (Manual) → L02-L07 (Collaboration/Intelligence) → L08 (Spec-Driven) follows natural skill building
2. **Cognitive Load**: 8 lessons at 25-30 minutes each = 200-240 minutes total chapter time is appropriate for B1 proficiency
3. **Prerequisite Knowledge**: Students completing Ch40 + Ch34-36 have sufficient async/API/agent knowledge for ChatKit concepts
4. **Hands-On Practice**: "Try With AI" sections with 3 prompts per lesson provide sufficient practice for concept retention

### Content Assumptions

1. **Running Example**: TaskManager agent from previous chapters continues as running example (consistent with Part 6 progression)
2. **Code Validation**: Code examples tested against ChatKit SDK (validation occurs during implementation phase)
3. **Fact-Checking**: All statistics, dates, quotes verified via WebSearch during content creation
4. **No Meta-Commentary**: Lessons avoid exposing Three Roles Framework or other pedagogical scaffolding to students

## Non-Goals

### Out of Scope for This Chapter

- **Advanced streaming patterns**: Server-sent events (SSE) internals, WebSocket implementation details (covered in future realtime chapters)
- **Production deployment**: Kubernetes, Docker, scaling strategies (covered in Part 7 Cloud Native chapters)
- **Advanced authentication**: OAuth2 provider setup, SAML integration (mentioned but not implemented)
- **Custom widget development**: Building interactive widgets beyond basic chat (covered in Chapter 42 Apps SDK)
- **Multi-agent orchestration**: Handoffs, agent-to-agent communication (covered in Chapter 48)
- **RAG integration**: Vector databases, retrieval strategies (covered in Chapter 43)
- **Fine-tuning**: Custom model training for conversations (covered in Part 8 LLMOps)

### Explicitly Not Teaching

- **ChatKit infrastructure internals**: How OpenAI hosts ChatKit servers (black box)
- **React framework fundamentals**: Assumes basic React knowledge for L07
- **Database administration**: Schema design, optimization (uses simple persistence patterns)
- **Network protocols**: TCP, HTTP/2, WebSocket specifications (abstractions suffice)

## Canonical Format References

### Skill Format (Critical for L00)

**Canonical Source**: `.claude/skills/building-chat-interfaces/SKILL.md`
**Also Reference**: Chapter 5 Lesson 7 (skill format teaching), `.claude/skills/creating-skills/SKILL.md`

**Required Format** (prevents format drift):
- Directory structure: `.claude/skills/chatkit-server/SKILL.md` (NOT flat file)
- YAML frontmatter with `name`, `description` (description starts with "This skill should be used when...")
- Sections: Overview, When to Use, Workflow, References, Examples
- Verification script: `.claude/skills/creating-skills/scripts/verify.py`

**Anti-Pattern**: Inventing new format contradicts Chapter 5 and causes format drift (Chapter 14 incident)

**L00 Lesson Must**:
- Guide students to read canonical source first
- Provide checklist validating against canonical format
- Reference `building-chat-interfaces` as working example

### Constitution Alignment (v7.0.0)

**Agent Factory Connection** (FR-021 requirement):

| Lesson | Agent Factory Concept | How It Enables Digital FTEs |
|--------|----------------------|----------------------------|
| L01 | ChatKit architecture vs REST | Conversational infrastructure = sellable chat agents |
| L02 | Agent integration | Connect existing agents to conversational products |
| L03 | Streaming patterns | Professional UX for customer-facing agents |
| L04 | Conversation memory | Agents with context = higher-value services |
| L05 | Session management | Multi-user support = scalable Digital FTE deployment |
| L06 | Authentication | Secure, multi-tenant agents = enterprise-ready products |
| L07 | React UI integration | Complete user-facing Digital FTE product |
| L08 | Capstone (Spec-Driven) | Layer 4 synthesis = sellable conversational agent |

**Three Roles Framework Application**:
- L01 (Manual/Layer 1): No AI collaboration - build vocabulary
- L02-L07 (Layers 2-3): AI as Teacher (suggests patterns), AI as Student (refines based on feedback), AI as Co-Worker (implements together)
- L08 (Layer 4): AI executes from specification students write

## Open Questions

**Resolved via Documented Assumptions**:
- Authentication pattern → Lesson content decision (belongs in plan phase)
- Deployment scope → Lesson content decision (belongs in plan phase)
- Error handling depth → Lesson content decision (belongs in plan phase)
- Cookie configuration → Lesson content decision (belongs in plan phase)

All implementation details deferred to `/sp.plan` where lesson-by-lesson structure is designed.
