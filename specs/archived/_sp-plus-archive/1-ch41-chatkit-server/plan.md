# Implementation Plan: Chapter 41 - ChatKit Server for Agents

**Branch**: `1-ch41-chatkit-server` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Chapter spec from `/specs/1-ch41-chatkit-server/spec.md`

---

## Summary

This plan structures Chapter 41 to teach students how to build conversational infrastructure for AI agents using ChatKitServer. Following the 4-Layer Teaching Method, students progress from manual architecture understanding (L01) through progressive implementation (L02-L07) to specification-driven capstone (L08) that produces a deployable Digital FTE.

**Key Pedagogical Innovation**: Unlike Chapter 40 (FastAPI) which used Skill-First pattern, this chapter uses **Architecture-First pattern**—students build vocabulary and mental models for conversational infrastructure before implementation, enabling them to reason about streaming, session management, and multi-user isolation.

---

## Educational Context

**Part**: 6 - AI Native Software Development
**Chapter Number**: 41
**Proficiency Level**: B1 (Intermediate)
**Lesson Count**: 8 lessons (L01-L08) following 4-Layer progression

**Prerequisites Met**:
- Chapter 40 (FastAPI fundamentals) → Students understand API development, async patterns
- Chapters 34-36 (Agent SDKs) → Students can create agents with OpenAI/Google/Anthropic
- Part 5 (Python) → Students know async/await, streaming patterns, Pydantic models
- Chapter 5 (Skills) → Students understand canonical skill format

**Assumed Knowledge**:
- Building REST APIs with FastAPI routes
- Creating agents with SDK (Agent, Runner, function_tool patterns)
- Python async/await and asyncio patterns
- HTTP request/response lifecycle
- Basic authentication (tokens, headers)

**Must Explain from Scratch**:
- ChatKit Server architecture (Thread, ThreadItem, RequestContext primitives)
- Streaming vs request/response patterns for conversational AI
- Session lifecycle and conversation persistence
- Multi-tenant user isolation via RequestContext
- Event streaming patterns (respond() method)

---

## Constitution Check

✅ **Specification Primacy**: All lessons show specification BEFORE implementation
✅ **Progressive Complexity**: B1 tier, max 7-10 concepts per lesson
✅ **Factual Accuracy**: All code verified against ChatKit SDK, claims WebSearch-verified
✅ **4-Layer Progression**: L01 (Manual) → L02-L07 (Collaboration/Intelligence) → L08 (Spec-Driven)
✅ **Agent Factory Alignment**: Each lesson contributes to Digital FTE production
✅ **Anti-Convergence**: Architecture-First pattern (different from Ch40's Skill-First)
✅ **Minimal Sufficient Content**: Lessons end with "Try With AI" only

---

## Pedagogical Arc: Foundation → Mastery

### The Architecture-First Progression

**Why NOT Skill-First like Chapter 40?**

Chapter 40 (FastAPI) used Skill-First because FastAPI is well-documented with stable patterns. ChatKit is newer with evolving patterns—students benefit from understanding ARCHITECTURE (mental models) before creating skills.

**Layer Mapping**:

```
L01: Manual Foundation (Layer 1)
├── Build vocabulary: Thread, ThreadItem, RequestContext, respond()
├── Manual architecture diagramming (no AI collaboration yet)
└── NO code implementation (conceptual understanding only)

L02-L07: AI Collaboration & Intelligence Design (Layers 2-3)
├── L02: First agent connection (Layer 2 - AI as Teacher/Student/Co-Worker)
├── L03: Streaming patterns (Layer 2 with Three Roles)
├── L04: Conversation history (Layer 2 + Layer 3 skill creation opportunity)
├── L05: Session lifecycle (Layer 2 + Layer 3 skill creation opportunity)
├── L06: Authentication & security (Layer 2 + Layer 3 skill creation opportunity)
└── L07: React UI integration (Layer 2 final application)

L08: Spec-Driven Capstone (Layer 4)
├── Write specification FIRST (intent, constraints, success criteria)
├── Compose accumulated skills from L02-L07
├── AI orchestrates implementation from spec
└── Output: Deployable Digital FTE (conversational agent product)
```

---

## Lesson-by-Lesson Structure

### Lesson 1: ChatKit Architecture Foundations (Layer 1 - Manual)

**Duration**: 25-30 minutes
**Proficiency**: B1 (transition from A2 to B1)
**Layer**: 1 (Manual Foundation)
**Teaching Modality**: Architecture diagramming + Socratic discovery (NO code yet)

**Learning Objectives** (Evals-First from Spec SC-001):
1. **LO-001** (Bloom's: Understand): Explain ChatKitServer architecture differences from FastAPI request/response
   - **Maps to eval**: SC-001 (80%+ quiz on architecture differences)
   - **Assessment**: Written explanation comparing ChatKitServer.respond() vs FastAPI route handler
   - **Proficiency**: B1 (independent explanation)

2. **LO-002** (Bloom's: Analyze): Diagram ThreadItem lifecycle from user message → assistant response → tool calls
   - **Maps to eval**: SC-001 (trace ThreadItem flow in 10-message conversation)
   - **Assessment**: Draw lifecycle diagram, trace sample conversation
   - **Proficiency**: B1 (analysis without assistance)

3. **LO-003** (Bloom's: Remember): Identify ChatKit primitives (Thread, ThreadItem, RequestContext)
   - **Maps to eval**: SC-001 (define primitives accurately)
   - **Assessment**: Definition quiz, label architecture diagram
   - **Proficiency**: A2→B1 (recognition to understanding)

**New Concepts Introduced** (count: 7 ≤ B1 limit of 10):
1. Thread (conversation container with metadata)
2. ThreadItem (user/assistant/tool message)
3. RequestContext (user identity + session info)
4. respond() method signature
5. Streaming vs request/response paradigm
6. Event-driven architecture for chat
7. Conversation persistence vs stateless APIs

**Cognitive Load Validation**: 7 concepts ≤ 10 (B1 limit) ✅ WITHIN LIMIT

**Agent Factory Connection**:
"Understanding ChatKit architecture is the foundation for building sellable conversational agents. REST APIs serve requests; ChatKitServer manages ongoing relationships. This is the infrastructure layer of your Digital FTE toolkit."

**Content Elements**:
- Architecture diagrams comparing FastAPI (stateless) vs ChatKitServer (stateful)
- ThreadItem lifecycle visualization (user → assistant → tool call → assistant)
- RequestContext isolation diagram (multi-tenant user separation)
- Manual walkthroughs: "Trace this 5-message conversation through ChatKit"
- NO code examples yet (vocabulary building only)
- NO AI collaboration yet (Layer 1 requirement)

**Teaching Approach** (Anti-Convergence):
- Socratic dialogue: "What happens when 2 users send messages simultaneously?"
- Discovery learning: Give sample conversation, ask students to identify ThreadItems
- Diagramming exercises: Students draw architecture before seeing official diagrams
- **Different from Chapter 40**: Ch40 showed code first, this shows concepts first

**Try With AI**:
Not included in Layer 1 lessons (AI collaboration begins Layer 2)

**Safety Note** (embedded in narrative):
"ChatKitServer handles multi-user conversations—authentication must prevent users from accessing each other's threads. We'll implement this in Lesson 6."

**Estimated Time**: 25-30 minutes (lighter cognitive load, foundational concepts)

---

### Lesson 2: Connecting Your First Agent (Layer 2 - AI Collaboration)

**Duration**: 25-30 minutes
**Proficiency**: B1 (Intermediate)
**Layer**: 2 (AI Collaboration with Three Roles)
**Teaching Modality**: Hands-on implementation with AI as Teacher/Student/Co-Worker

**Learning Objectives** (Evals-First from Spec SC-002, SC-003):
1. **LO-004** (Bloom's: Apply): Implement ChatKitServer.respond() that wires OpenAI agent to streaming responses
   - **Maps to eval**: SC-002 (wire existing agent within 30 minutes)
   - **Assessment**: Working ChatKitServer responding to user messages
   - **Proficiency**: B1 (independent implementation)

2. **LO-005** (Bloom's: Apply): Stream agent responses token-by-token using stream_agent_response() helper
   - **Maps to eval**: SC-003 (streaming with <100ms latency per token)
   - **Assessment**: Validate streaming appears in real-time
   - **Proficiency**: B1 (application with validation)

3. **LO-006** (Bloom's: Analyze): Validate conversation persistence by inspecting thread storage
   - **Maps to eval**: SC-002 (3-message conversation persists correctly)
   - **Assessment**: Inspect storage, verify all ThreadItems saved
   - **Proficiency**: B1 (diagnostic analysis)

**New Concepts Introduced** (count: 5 ≤ B1 limit of 10):
1. ChatKitServer class inheritance pattern
2. respond() method signature (thread, input_user_message, context parameters)
3. stream_agent_response() helper function
4. Agent integration within respond() method
5. Thread storage and retrieval

**Cognitive Load Validation**: 5 concepts ≤ 10 (B1 limit) ✅ WITHIN LIMIT

**Agent Factory Connection**:
"Lesson 2 proves that ChatKit connects your existing agent knowledge (from Ch34-36) to conversational infrastructure. You're not learning ChatKit from scratch—you're integrating accumulated intelligence into sellable chat products."

**Three Roles Demonstrations** (REQUIRED for Layer 2):

**Role 1: AI as Teacher**
- **Scenario**: Student implements basic respond() method but forgets to pass context to agent
- **AI suggests**: "I notice you're creating the agent without thread history. Here's why context matters:
  - Previous messages inform current responses
  - Agents need conversation memory for coherent dialogue
  - Pass history string as part of system prompt"
- **What student learns**: Context passing pattern they didn't know

**Role 2: AI as Student**
- **Scenario**: AI generates comprehensive respond() with all possible parameters
- **Student responds**: "Too complex for MVP. Just handle user messages, skip thread metadata for now."
- **AI adapts**: "Understood. For MVP, simplified respond() that:
  - Accepts user message only
  - Skips metadata handling
  - Returns basic streaming response
  - Defer advanced features to Lesson 4"
- **What AI learns**: Student's MVP constraint (speed over completeness)

**Role 3: AI as Co-Worker**
- **Scenario**: Student and AI iterate on streaming implementation
- **Iteration 1**: AI generates buffered responses (no real-time streaming)
- **Student feedback**: "Responses appear all at once, not token-by-token"
- **Iteration 2**: AI uses stream_agent_response() correctly
- **Convergence**: Together they validated streaming works (student: UX requirement, AI: implementation pattern, result: better than either alone)

**Content Elements**:
- Specification: "Build ChatKitServer that streams TaskManager agent responses"
- Step-by-step implementation with AI collaboration
- Code examples: ChatKitServer class, respond() method, stream_agent_response()
- Validation: Test streaming, inspect thread storage
- **HIDDEN**: No explicit "AI as Teacher" labels (students EXPERIENCE roles)

**Try With AI** (3 prompts + "What you're learning"):

**Prompt 1: Initial Implementation**
```
Ask AI: "Help me implement ChatKitServer.respond() that connects my TaskManager agent from Chapter 34 and streams responses."
```
**What you're learning**: How to integrate existing agents into ChatKit infrastructure (convergence pattern from previous work).

**Prompt 2: Validation & Refinement**
```
Tell AI your constraints: "I need streaming to appear token-by-token, not buffered. And I need to verify conversation persists across requests."
```
**What you're learning**: How to specify non-functional requirements (performance, persistence) that AI must validate.

**Prompt 3: Edge Case Handling**
```
Ask AI: "What happens if user sends message while previous response is streaming? How should I handle interruptions?"
```
**What you're learning**: Production considerations that manual tutorials skip (AI suggests patterns from real-world use).

**Safety Note** (embedded in Try With AI):
"When testing streaming, verify tokens appear immediately. Buffered responses indicate misconfiguration that hurts user experience."

**Estimated Time**: 25-30 minutes

---

### Lesson 3: Streaming Patterns for Professional UX (Layer 2 - AI Collaboration)

**Duration**: 25-30 minutes
**Proficiency**: B1
**Layer**: 2 (AI Collaboration)
**Teaching Modality**: Error analysis + collaborative debugging (different from L02's hands-on implementation)

**Learning Objectives** (Evals-First from Spec SC-003):
1. **LO-007** (Bloom's: Apply): Implement progress events for long-running operations
   - **Maps to eval**: SC-003 (progress indicators during 10-second operations)
   - **Assessment**: Demonstrate "Analyzing documents..." during agent execution
   - **Proficiency**: B1 (application of streaming patterns)

2. **LO-008** (Bloom's: Analyze): Handle stream interruptions when users send new messages mid-response
   - **Maps to eval**: SC-003 (handle interruption correctly)
   - **Assessment**: Terminate previous stream, begin new response
   - **Proficiency**: B1 (analysis + implementation)

3. **LO-009** (Bloom's: Evaluate): Compare buffered vs streaming responses for UX impact
   - **Maps to eval**: Not directly mapped, supports SC-003 understanding
   - **Assessment**: Explain tradeoffs, justify streaming choice
   - **Proficiency**: B1 (evaluation with justification)

**New Concepts Introduced** (count: 6 ≤ B1 limit of 10):
1. Event types in ChatKit (text delta, progress, tool call, etc.)
2. Progress event streaming for long operations
3. Stream interruption handling
4. Partial response management
5. Client-side streaming consumption (SSE)
6. Buffering vs real-time streaming tradeoffs

**Cognitive Load Validation**: 6 concepts ≤ 10 (B1 limit) ✅ WITHIN LIMIT

**Agent Factory Connection**:
"Streaming UX is what separates hobbyist chatbots from professional Digital FTEs. Users pay for responsiveness—streaming shows value immediately, not after 30-second waits."

**Three Roles Demonstrations**:

**Role 1: AI as Teacher**
- **Scenario**: Student's agent performs 10-second file analysis without progress updates
- **AI suggests**: "I see the UX gap. Here's why progress events matter:
  - Users abandon after 5 seconds without feedback
  - Progress events keep users engaged during waits
  - Stream 'Analyzing 50 documents...' as status updates"
- **What student learns**: Progress pattern for production UX

**Role 2: AI as Student**
- **Scenario**: AI generates complex interruption handling with queue management
- **Student responds**: "Too complex. Just cancel previous stream and start new one."
- **AI adapts**: "Understood. Simplified interruption handling:
  - Terminate existing stream on new message
  - Clear partial response state
  - Begin fresh response
  - No queue needed for MVP"
- **What AI learns**: Simplicity over completeness for MVP

**Role 3: AI as Co-Worker**
- **Scenario**: Student and AI debug "jumpy" streaming where tokens batch unexpectedly
- **Iteration 1**: Student reports buffering issue
- **AI diagnosis**: "Check flush() calls after each token"
- **Iteration 2**: Student adds flush(), still batches
- **AI diagnosis**: "Network middleware may buffer SSE. Try chunked encoding."
- **Convergence**: Together they isolated nginx buffering (student: observed symptom, AI: diagnosed root cause, result: production fix)

**Content Elements**:
- Specification: "Add progress events to TaskManager agent for file processing operations"
- Error scenarios: "Streaming batches tokens instead of real-time"
- Debugging walkthrough with AI collaboration
- Code examples: Progress events, interruption handling
- Comparative analysis: Buffered vs streaming UX

**Try With AI** (3 prompts):

**Prompt 1: Progress Events**
```
Ask AI: "My agent analyzes documents for 10 seconds. How do I stream progress events like 'Processing document 15 of 50...' so users see activity?"
```
**What you're learning**: Production UX patterns that official docs gloss over.

**Prompt 2: Interruption Handling**
```
Tell AI: "User sends new message while previous response streams. What's the simplest way to handle this? I don't need queue management yet."
```
**What you're learning**: How to constrain AI toward MVP solutions (teaching AI your priorities).

**Prompt 3: Debugging Buffering**
```
Ask AI: "My streaming appears in 5-token bursts, not token-by-token. What could cause this? Walk me through debugging steps."
```
**What you're learning**: Systematic debugging with AI (diagnosis, not just fixes).

**Safety Note** (embedded):
"Test streaming on slow networks. Progress events prevent user frustration during delays."

**Estimated Time**: 25-30 minutes

---

### Lesson 4: Managing Conversation History (Layer 2 → Layer 3 Transition)

**Duration**: 25-30 minutes
**Proficiency**: B1
**Layer**: 2 (AI Collaboration) + Layer 3 (Intelligence Design opportunity)
**Teaching Modality**: Specification-first implementation + skill creation opportunity

**Learning Objectives** (Evals-First from Spec SC-004):
1. **LO-010** (Bloom's: Apply): Implement conversation history persistence where agents reference previous messages
   - **Maps to eval**: SC-004 (agent references previous messages in 10-message conversation)
   - **Assessment**: Agent responds to "What did I ask earlier?" with correct reference
   - **Proficiency**: B1 (independent implementation)

2. **LO-011** (Bloom's: Analyze): Handle context window limits when conversations exceed 50 messages
   - **Maps to eval**: SC-004 (50-message conversation includes recent N messages without errors)
   - **Assessment**: System handles long conversations gracefully
   - **Proficiency**: B1 (analysis + constraint handling)

3. **LO-012** (Bloom's: Create): Design reusable conversation-history skill (Layer 3 intelligence)
   - **Maps to eval**: Not directly mapped, contributes to Layer 4 capstone
   - **Assessment**: Skill encapsulates history patterns for future projects
   - **Proficiency**: B1→B2 (creation of reusable component)

**New Concepts Introduced** (count: 7 ≤ B1 limit of 10):
1. Thread storage and retrieval patterns
2. Conversation history as system prompt context
3. Context window limits (token budgets)
4. History truncation strategies
5. Thread metadata storage (user preferences, domain context)
6. History inclusion in agent prompts
7. Reusable conversation-history skill design

**Cognitive Load Validation**: 7 concepts ≤ 10 (B1 limit) ✅ WITHIN LIMIT

**Agent Factory Connection**:
"Conversation memory is what makes Digital FTEs valuable. Stateless APIs forget context; ChatKitServer maintains relationships. This is the difference between tool and teammate."

**Layer 3 Intelligence Opportunity**:
**Pattern Recognition**: History management pattern recurs across all conversational agents (frequency: every chat project)
**Complexity**: 5+ decision points (when to truncate, how to format, metadata handling)
**Organizational Value**: Applies to all future ChatKit projects
→ **Decision**: Create reusable `conversation-history` skill (Persona + Questions + Principles pattern)

**Skill Design Framework**:
**Persona**: "Think like a conversation architect managing context budgets and memory optimization."
**Questions**:
- "What's the context window limit for this LLM?"
- "Which messages are most relevant to current query?"
- "What metadata should persist across conversation?"
**Principles**:
- Recency bias: Recent messages more relevant than old
- Compression over truncation: Summarize old messages before discarding
- Metadata preservation: User preferences outlive individual messages

**Three Roles Demonstrations**:

**Role 1: AI as Teacher**
- **Scenario**: Student implements history by loading all messages into prompt
- **AI suggests**: "I see a scaling issue. Here's why:
  - 50-message conversation exceeds 4K token context window
  - All messages in prompt causes overflow errors
  - Truncation strategy needed: keep recent N, summarize old"
- **What student learns**: Context window constraints they didn't consider

**Role 2: AI as Student**
- **Scenario**: AI generates complex sliding window with embeddings-based retrieval
- **Student responds**: "Too complex for now. Just keep most recent 10 messages."
- **AI adapts**: "Understood. Simplified history strategy:
  - Load last 10 messages from thread
  - Format as 'User: ... Assistant: ...' string
  - Include in system prompt
  - Defer semantic search to advanced chapter"
- **What AI learns**: MVP prioritization (simple first, optimize later)

**Role 3: AI as Co-Worker**
- **Scenario**: Student and AI design history metadata schema
- **Iteration 1**: Student wants to save user preferences
- **AI suggests**: "Use thread.metadata JSON field"
- **Iteration 2**: Student asks how to structure metadata
- **AI proposes**: `{"userPrefs": {...}, "domainContext": {...}}`
- **Convergence**: Together they designed extensible schema (student: requirements, AI: schema design, result: future-proof structure)

**Content Elements**:
- Specification: "Build conversation history that persists across server restarts and includes context in agent prompts"
- Implementation: History retrieval, formatting, prompt integration
- Code examples: Thread storage, history truncation, metadata handling
- **Skill creation**: Guide students to create `conversation-history` skill using Chapter 5 patterns
- Validation: Test history with 10-message, 50-message conversations

**Try With AI** (3 prompts):

**Prompt 1: History Implementation**
```
Ask AI: "Help me implement conversation history that loads last 10 messages from thread and includes them in agent prompt. Agent should reference previous messages when relevant."
```
**What you're learning**: History as context pattern (foundational for all conversational AI).

**Prompt 2: Context Window Handling**
```
Tell AI: "My agent uses GPT-4 (8K context). When conversation exceeds 50 messages, how do I prevent context overflow? Keep solution simple for MVP."
```
**What you're learning**: Constraint handling through AI collaboration (teaching AI your limits).

**Prompt 3: Skill Creation**
```
Ask AI: "I want to create a reusable conversation-history skill for future projects. What should it include? Use Persona + Questions + Principles pattern from Chapter 5."
```
**What you're learning**: Intelligence accumulation (Layer 3 skill design).

**Safety Note** (embedded):
"Test history with 100+ message conversations. Agents silently fail when context overflows—validate truncation works."

**Estimated Time**: 25-30 minutes

---

### Lesson 5: Session Lifecycle Management (Layer 2 → Layer 3)

**Duration**: 25-30 minutes
**Proficiency**: B1
**Layer**: 2 (AI Collaboration) + Layer 3 (Intelligence Design)
**Teaching Modality**: Production patterns + skill creation

**Learning Objectives** (Evals-First from Spec SC-005):
1. **LO-013** (Bloom's: Apply): Implement session create/resume/timeout logic
   - **Maps to eval**: SC-005 (sessions persist across server restarts, resume after 24-hour gap)
   - **Assessment**: Create session, restart server, resume conversation
   - **Proficiency**: B1 (independent implementation)

2. **LO-014** (Bloom's: Analyze): Design session expiration policy balancing storage costs and UX
   - **Maps to eval**: SC-005 (24-hour timeout, cleanup reclaims storage)
   - **Assessment**: Explain timeout choice, implement cleanup
   - **Proficiency**: B1 (analysis with justification)

3. **LO-015** (Bloom's: Create): Design reusable session-lifecycle skill
   - **Maps to eval**: Contributes to Layer 4 capstone
   - **Assessment**: Skill encapsulates session patterns
   - **Proficiency**: B1→B2 (skill creation)

**New Concepts Introduced** (count: 6 ≤ B1 limit of 10):
1. Session ID generation and tracking
2. Session creation vs resumption logic
3. Timeout policies (idle timeout, absolute expiration)
4. Session cleanup and garbage collection
5. Session persistence across server restarts
6. Reusable session-lifecycle skill design

**Cognitive Load Validation**: 6 concepts ≤ 10 (B1 limit) ✅ WITHIN LIMIT

**Agent Factory Connection**:
"Session management enables multi-user Digital FTEs. Without it, conversations reset on every server restart. With it, you build reliable products that customers trust."

**Layer 3 Intelligence Opportunity**:
**Pattern**: Session lifecycle recurs in all stateful conversational systems
**Complexity**: 5+ decision points (when to create, when to expire, cleanup scheduling)
**Value**: Applies to every ChatKit project
→ **Decision**: Create `session-lifecycle` skill

**Skill Design**:
**Persona**: "Think like a resource manager balancing user experience and storage costs."
**Questions**:
- "What timeout duration balances cost and UX?"
- "When should cleanup run (idle periods, scheduled batches)?"
- "What happens when user resumes expired session?"
**Principles**:
- Graceful degradation: Expired session → Create new, don't error
- Predictable costs: Cleanup prevents unbounded storage growth
- Audit trail: Log session lifecycle events for debugging

**Three Roles Demonstrations**:

**Role 1: AI as Teacher**
- **Scenario**: Student asks about session timeout duration
- **AI suggests**: "I see a product design decision. Here's the framework:
  - Short timeout (1 hour): Lower storage cost, frustrates users
  - Medium timeout (24 hours): Balanced UX and cost
  - Long timeout (30 days): Better UX, higher storage cost
  - Your choice depends on business model (free tier vs paid)"
- **What student learns**: Product tradeoffs, not just technical implementation

**Role 2: AI as Student**
- **Scenario**: AI generates complex distributed session management with Redis
- **Student responds**: "Too complex. Just store sessions in PostgreSQL with created_at timestamp."
- **AI adapts**: "Understood. Simplified session storage:
  - Add created_at, last_accessed_at to thread table
  - Query for expired sessions: WHERE last_accessed_at < NOW() - INTERVAL '24 hours'
  - Cleanup: DELETE expired sessions daily
  - Defer Redis to scaling chapter"
- **What AI learns**: Simplicity constraint for MVP

**Role 3: AI as Co-Worker**
- **Scenario**: Student and AI design cleanup strategy
- **Iteration 1**: Student wants cleanup on every request
- **AI warns**: "Performance issue—cleanup queries slow requests"
- **Iteration 2**: Student asks for alternative
- **AI proposes**: "Background cron job runs cleanup at 3am daily"
- **Convergence**: Together they balanced cleanup frequency and performance

**Content Elements**:
- Specification: "Implement session lifecycle where conversations persist 24 hours, cleanup runs daily"
- Implementation: Session create/resume, timeout policy, cleanup cron
- Code examples: Session table schema, cleanup query, resume logic
- Skill creation: `session-lifecycle` skill design
- Validation: Test session persistence, timeout, cleanup

**Try With AI** (3 prompts):

**Prompt 1: Session Implementation**
```
Ask AI: "Help me implement session management where new users get unique session IDs and returning users resume existing sessions. Sessions should persist across server restarts."
```
**What you're learning**: Stateful session patterns for production systems.

**Prompt 2: Timeout Policy Design**
```
Tell AI: "I need to choose a timeout duration. Help me understand tradeoffs between 1-hour, 24-hour, and 7-day expiration for a productivity assistant."
```
**What you're learning**: Product design through AI collaboration (not just code).

**Prompt 3: Cleanup Strategy**
```
Ask AI: "What's the best way to clean up expired sessions? Should I check on every request or use a background job? Keep it simple for MVP."
```
**What you're learning**: Performance optimization through systematic analysis.

**Safety Note** (embedded):
"Test session cleanup on large datasets (1000+ sessions). Cleanup queries must not block production traffic."

**Estimated Time**: 25-30 minutes

---

### Lesson 6: Authentication and Security (Layer 2 → Layer 3)

**Duration**: 25-30 minutes
**Proficiency**: B1
**Layer**: 2 (AI Collaboration) + Layer 3 (Intelligence Design)
**Teaching Modality**: Security patterns + threat modeling

**Learning Objectives** (Evals-First from Spec SC-006):
1. **LO-016** (Bloom's: Apply): Implement RequestContext with user_id isolation
   - **Maps to eval**: SC-006 (users cannot access other users' threads)
   - **Assessment**: Test isolation, verify cross-user access fails
   - **Proficiency**: B1 (independent implementation)

2. **LO-017** (Bloom's: Analyze): Validate JWT tokens and extract user identity
   - **Maps to eval**: SC-006 (unauthenticated requests return 401)
   - **Assessment**: Test auth success/failure, verify JWT validation
   - **Proficiency**: B1 (security analysis)

3. **LO-018** (Bloom's: Evaluate): Assess threat model for multi-tenant chat security
   - **Maps to eval**: SC-006 (isolation prevents cross-user data access)
   - **Assessment**: Identify attack vectors, justify defenses
   - **Proficiency**: B1→B2 (security evaluation)

**New Concepts Introduced** (count: 8 ≤ B1 limit of 10):
1. RequestContext structure (user_id, metadata)
2. JWT token validation (decode, verify signature)
3. Multi-tenant isolation (row-level security)
4. Authentication middleware patterns
5. Authorization (who can access what)
6. JWKS endpoint for public key retrieval
7. Security testing (auth success/failure cases)
8. Reusable auth-security skill design

**Cognitive Load Validation**: 8 concepts ≤ 10 (B1 limit) ✅ WITHIN LIMIT

**Agent Factory Connection**:
"Security is what makes Digital FTEs enterprise-ready. Hobbyist chatbots ignore auth; professional products enforce multi-tenant isolation. This is the trust layer that enables monetization."

**Layer 3 Intelligence Opportunity**:
**Pattern**: JWT validation + multi-tenant isolation recurs in all customer-facing agents
**Complexity**: 6+ decision points (token validation, user extraction, isolation enforcement)
**Value**: Applies to all production ChatKit deployments
→ **Decision**: Create `chatkit-auth-security` skill

**Three Roles Demonstrations**:

**Role 1: AI as Teacher**
- **Scenario**: Student implements basic user_id but doesn't validate JWT
- **AI suggests**: "I see a critical security gap. Here's why JWT validation matters:
  - User can forge user_id in request without validation
  - JWT signature verification proves token authenticity
  - Without validation, users access other users' data
  - Always verify JWT before trusting user_id"
- **What student learns**: Security vulnerability they didn't recognize

**Role 2: AI as Student**
- **Scenario**: AI generates comprehensive auth with RBAC and permissions
- **Student responds**: "Too complex. Just verify JWT and extract user_id. No role-based access yet."
- **AI adapts**: "Understood. Simplified auth for MVP:
  - Verify JWT signature using JWKS
  - Extract user_id from token payload
  - Pass user_id to RequestContext
  - Defer RBAC to future iteration"
- **What AI learns**: MVP security (essential controls only)

**Role 3: AI as Co-Worker**
- **Scenario**: Student and AI design row-level security for thread isolation
- **Iteration 1**: Student wants to filter threads by user_id in code
- **AI warns**: "Code-level filtering is error-prone—one missing WHERE clause leaks data"
- **Iteration 2**: Student asks for alternative
- **AI proposes**: "Database row-level security policies enforce isolation automatically"
- **Convergence**: Together they chose defense-in-depth (student: identified risk, AI: proposed solution, result: stronger security)

**Content Elements**:
- Specification: "Secure ChatKit endpoints where only authenticated users access their own conversations"
- Threat model: Attack vectors (JWT forgery, cross-user access, token theft)
- Implementation: JWT validation, RequestContext, row-level security
- Code examples: Auth middleware, JWKS retrieval, isolation testing
- Skill creation: `chatkit-auth-security` skill
- Validation: Test auth success, failure, cross-user access prevention

**Try With AI** (3 prompts):

**Prompt 1: JWT Implementation**
```
Ask AI: "Help me implement JWT validation for ChatKit. Extract user_id from token and pass to RequestContext. If token invalid, return 401."
```
**What you're learning**: Production authentication patterns (not just tutorials).

**Prompt 2: Isolation Testing**
```
Tell AI: "I need to verify users cannot see each other's conversations. How do I test multi-tenant isolation? What attack vectors should I check?"
```
**What you're learning**: Security testing through threat modeling.

**Prompt 3: Defense in Depth**
```
Ask AI: "I'm filtering threads by user_id in application code. What additional security layers should I add? Keep it practical for MVP."
```
**What you're learning**: Layered security (not single point of failure).

**Safety Note** (embedded):
"NEVER trust user_id from client requests without JWT verification. Always validate tokens server-side."

**Estimated Time**: 25-30 minutes

---

### Lesson 7: React UI Integration (Layer 2 Final Application)

**Duration**: 25-30 minutes
**Proficiency**: B1
**Layer**: 2 (AI Collaboration—final hands-on application)
**Teaching Modality**: Full-stack integration (frontend + backend)

**Learning Objectives** (Evals-First from Spec SC-007):
1. **LO-019** (Bloom's: Apply): Integrate useChatKit hook with custom backend
   - **Maps to eval**: SC-007 (chat widget connects to backend within 20 minutes)
   - **Assessment**: Working React component sending messages to ChatKitServer
   - **Proficiency**: B1 (independent integration)

2. **LO-020** (Bloom's: Apply): Implement custom fetch interceptor with authentication
   - **Maps to eval**: SC-007 (custom fetch includes auth headers)
   - **Assessment**: Requests include JWT token, backend validates
   - **Proficiency**: B1 (application of auth patterns)

3. **LO-021** (Bloom's: Create): Inject page context (URL, title, headings) into agent metadata
   - **Maps to eval**: SC-007 (page context flows to agent)
   - **Assessment**: Agent responses reference current page
   - **Proficiency**: B1→B2 (creative context injection)

**New Concepts Introduced** (count: 7 ≤ B1 limit of 10):
1. useChatKit hook configuration
2. Custom fetch interceptor pattern
3. Page context extraction (DOM scraping)
4. Metadata injection into requests
5. Script loading detection (web components)
6. SSE streaming consumption (client-side)
7. httpOnly cookie proxy (Next.js pattern)

**Cognitive Load Validation**: 7 concepts ≤ 10 (B1 limit) ✅ WITHIN LIMIT

**Agent Factory Connection**:
"React UI integration completes the Digital FTE stack. Backend (ChatKitServer) provides intelligence; frontend (useChatKit) provides accessibility. Together they form customer-facing products."

**Three Roles Demonstrations**:

**Role 1: AI as Teacher**
- **Scenario**: Student tries to read httpOnly cookie from JavaScript
- **AI suggests**: "I see a browser security constraint. Here's why:
  - httpOnly cookies prevent JavaScript access (XSS protection)
  - You need server-side proxy to read cookie
  - Next.js API route reads cookie, forwards to backend
  - Pattern: Client → Next.js route → ChatKitServer"
- **What student learns**: Browser security model they didn't understand

**Role 2: AI as Student**
- **Scenario**: AI generates complex page context with full DOM traversal
- **Student responds**: "Too much data. Just send URL, title, and first 5 headings."
- **AI adapts**: "Understood. Simplified page context:
  - Extract URL, title from window/document
  - Select first 5 h1/h2/h3 headings
  - Format as JSON in metadata
  - Defer full content extraction to advanced use cases"
- **What AI learns**: Minimal viable context (essentials only)

**Role 3: AI as Co-Worker**
- **Scenario**: Student and AI debug script loading race condition
- **Iteration 1**: Component renders before ChatKit script loads
- **AI diagnosis**: "Check customElements.whenDefined('openai-chatkit')"
- **Iteration 2**: Still renders too early
- **AI proposes**: "Use state to track script status, render only when 'ready'"
- **Convergence**: Together they solved async script loading (student: observed symptom, AI: diagnosed timing, result: reliable initialization)

**Content Elements**:
- Specification: "Build React component that connects to ChatKitServer with custom auth and page context"
- Implementation: useChatKit configuration, custom fetch, page context extraction
- Code examples: React component, fetch interceptor, Next.js proxy route
- Full-stack integration: Frontend → Next.js route → ChatKitServer → Agent
- Validation: Test message sending, auth flow, context injection

**Try With AI** (3 prompts):

**Prompt 1: Basic Integration**
```
Ask AI: "Help me integrate useChatKit in Next.js app. Backend is at http://localhost:8000/chatkit. Show me minimal setup to send messages."
```
**What you're learning**: Frontend-backend integration patterns.

**Prompt 2: Auth Implementation**
```
Tell AI: "My auth tokens are in httpOnly cookies. How do I pass them to ChatKitServer? I'm using Next.js 14."
```
**What you're learning**: Security patterns for cookie-based auth (real-world constraint).

**Prompt 3: Page Context**
```
Ask AI: "I want agent to know what page user is on (URL, title, headings). How do I extract this from DOM and send to backend? Keep it simple."
```
**What you're learning**: Context engineering for conversational AI.

**Safety Note** (embedded):
"NEVER send sensitive page content to agent. Extract public information only (URLs, headings, not form data)."

**Estimated Time**: 25-30 minutes

---

### Lesson 8: Capstone - Complete Conversational Agent (Layer 4 - Spec-Driven)

**Duration**: 30-40 minutes
**Proficiency**: B1→B2 (transition to advanced)
**Layer**: 4 (Spec-Driven Integration → Digital FTE Production)
**Teaching Modality**: Specification-first design + orchestration

**Learning Objectives** (Evals-First from Spec SC-008):
1. **LO-022** (Bloom's: Create): Write specification for production conversational agent
   - **Maps to eval**: SC-008 (spec includes conversation flows, auth, session management)
   - **Assessment**: Specification completeness, clarity
   - **Proficiency**: B2 (synthesis of all chapter concepts)

2. **LO-023** (Bloom's: Create): Orchestrate accumulated skills from L02-L07 into integrated system
   - **Maps to eval**: SC-008 (implementation uses conversation-history, session-lifecycle, auth-security skills)
   - **Assessment**: System demonstrates skill composition
   - **Proficiency**: B2 (orchestration without guidance)

3. **LO-024** (Bloom's: Evaluate): Validate implementation against specification through acceptance tests
   - **Maps to eval**: SC-008 (all requirements pass acceptance tests)
   - **Assessment**: Test suite validates spec ↔ implementation alignment
   - **Proficiency**: B2 (evaluation with validation)

4. **LO-025** (Bloom's: Create): Package as deployable Digital FTE product
   - **Maps to eval**: SC-008 (deployed agent handles multiple users simultaneously with isolated conversations)
   - **Assessment**: Production deployment passes multi-user load test
   - **Proficiency**: B2 (production-ready output)

**New Concepts Introduced** (count: 5 ≤ B1-B2 transition limit):
1. Specification-first workflow for conversational systems
2. Skill composition patterns (accumulated intelligence from L02-L07)
3. Acceptance test design for conversational AI
4. Multi-user deployment and isolation validation
5. Digital FTE packaging and productization

**Cognitive Load Validation**: 5 concepts ≤ 10 (B1 limit, transitioning to B2 synthesis) ✅ WITHIN LIMIT

**Agent Factory Connection**:
"Lesson 8 capstone is where you produce your first sellable conversational Digital FTE. Everything from L01-L07 was building blocks. Now you orchestrate them into a customer-ready product that generates value."

**Specification Quality Framework** (Layer 4 requirement):

**Intent Clarity**:
- WHAT: Build conversational productivity assistant for project managers
- WHY: Automate task tracking, provide insights, enable voice-first workflows
- SUCCESS: Users create/update tasks via chat, agent provides status summaries

**Constraint Definition**:
- Non-goals: No calendar integration (future feature), no team collaboration (MVP is single-user)
- Architecture: ChatKitServer + TaskManager agent from Ch40 + Neon database
- Quality: Sub-200ms response latency (p95), 24-hour session persistence, 99.9% uptime

**Intelligence Composition**:
- Skills from L04: conversation-history (10-message context)
- Skills from L05: session-lifecycle (24-hour timeout, daily cleanup)
- Skills from L06: chatkit-auth-security (JWT validation, multi-tenant isolation)
- Skills from L07: page-context injection (React integration)
- Gap analysis: Need new skill for task-agent integration (create during capstone)

**Content Elements**:
- Specification template: Intent, Constraints, Success Criteria, Skill Composition
- Student-written spec (NOT provided—Layer 4 requires student creation)
- AI orchestration: AI implements from spec using composed skills
- Validation framework: Acceptance tests from spec success criteria
- Deployment guide: Production checklist (database, auth, hosting)
- **Digital FTE packaging**: Branding, documentation, monetization options

**Try With AI** (3 prompts):

**Prompt 1: Specification Writing**
```
"Help me write a specification for a conversational productivity assistant that helps project managers track tasks via chat. Include:
- Intent (what/why/success criteria)
- Constraints (what NOT to build, architecture choices)
- Skill composition (which skills from L02-L07 apply)
Review my spec and suggest improvements."
```
**What you're learning**: Specification-first design (primary skill for AI-native development).

**Prompt 2: Orchestration**
```
"Here's my approved spec [paste spec]. Implement ChatKitServer using these skills:
- conversation-history from L04
- session-lifecycle from L05
- chatkit-auth-security from L06
Show me how to compose them into working system."
```
**What you're learning**: Skill orchestration through AI (Layer 4 delegation).

**Prompt 3: Validation**
```
"Generate acceptance tests from my spec's success criteria:
- Users create tasks via chat
- Agent provides status summaries
- Conversations persist 24 hours
- Multi-user isolation works
Run tests and report pass/fail."
```
**What you're learning**: Specification-driven validation (evals-first enforcement).

**Safety Note** (embedded):
"Test multi-user isolation with production load simulator (100+ concurrent users). Isolation failures leak data—validate before deployment."

**Estimated Time**: 30-40 minutes (longest lesson—capstone synthesis)

---

## Skill Composition Map (Layer 3 → Layer 4)

**Skills Created in Chapter 41**:

| Lesson | Skill Name | Purpose | Complexity | Reusability |
|--------|-----------|---------|------------|-------------|
| L04 | conversation-history | Manage conversation context and history | 5+ decision points | All ChatKit projects |
| L05 | session-lifecycle | Handle session create/resume/timeout/cleanup | 5+ decision points | All stateful chat systems |
| L06 | chatkit-auth-security | JWT validation + multi-tenant isolation | 6+ decision points | All production ChatKit deployments |

**Skills Assumed from Previous Chapters**:
- skill-creator (Chapter 5) → Used to create conversation-history, session-lifecycle, chatkit-auth-security skills
- fetching-library-docs (Chapter 5) → Used in L00 (if following Skill-First pattern)
- fastapi-agent-api (Chapter 40) → Agent backend knowledge

**Capstone (L08) Composes**:
- conversation-history + session-lifecycle + chatkit-auth-security → Complete ChatKitServer
- fastapi-agent-api + ChatKitServer → Conversational API integration
- React useChatKit + custom auth → Frontend integration
→ **Result**: Deployable Digital FTE (conversational productivity assistant)

---

## Validation Criteria (Pre-Implementation Gates)

**Before implementing any lesson, verify**:

1. ✅ **Specification Primacy**: Every lesson shows specification BEFORE code
2. ✅ **Cognitive Load**: Each lesson ≤ 10 new concepts (B1 tier limit)
3. ✅ **Layer Progression**: L01 (Manual) → L02-L07 (Layers 2-3) → L08 (Layer 4)
4. ✅ **Three Roles Integration**: L02-L07 demonstrate AI as Teacher/Student/Co-Worker
5. ✅ **No Meta-Commentary**: Lessons NEVER expose "AI as Teacher" labels
6. ✅ **Anti-Convergence**: Architecture-First pattern (different from Ch40 Skill-First)
7. ✅ **Agent Factory Alignment**: Each lesson contributes to Digital FTE production
8. ✅ **Evals Mapping**: All lessons map to success criteria from spec (SC-001 through SC-008)
9. ✅ **Skill Creation**: L04, L05, L06 produce reusable skills for Layer 4 composition
10. ✅ **Canonical Format**: If teaching skills, match format from `.claude/skills/building-chat-interfaces/SKILL.md`

---

## Quality Gates (Post-Implementation Validation)

**After implementing chapter, validate**:

| Gate | Criterion | Validation Method |
|------|-----------|-------------------|
| **Code Accuracy** | All code examples tested against ChatKit SDK | Run pytest on all examples |
| **Factual Claims** | All statistics/dates verified via WebSearch | Citation check + source verification |
| **Constitutional Compliance** | No meta-commentary, no scaffolding exposure | Grep for forbidden patterns |
| **Pedagogical Progression** | Lessons build sequentially without backtracking | Dependency analysis |
| **Skill Composition** | L08 capstone uses skills from L04-L06 | Code review + skill invocation check |
| **Digital FTE Output** | L08 produces deployable conversational agent | Production deployment test |

---

## Success Metrics

**This plan succeeds when**:

**Learning Outcomes** (from spec success criteria):
- ✅ SC-001: 80%+ students explain ChatKit architecture differences (quiz validation)
- ✅ SC-002: Students wire existing agents within 30 minutes of L02 completion
- ✅ SC-003: Students implement streaming with <100ms token latency
- ✅ SC-004: Conversation history persists and includes prior messages correctly
- ✅ SC-005: Sessions persist 24 hours, cleanup reclaims storage
- ✅ SC-006: Authentication prevents cross-user data access (isolation validated)
- ✅ SC-007: React integration connects to backend within 20 minutes of L07
- ✅ SC-008: 90%+ students complete capstone producing working conversational agent

**Pedagogical Quality**:
- ✅ Zero specification violations (code NEVER before spec)
- ✅ Zero meta-commentary (scaffolding hidden from students)
- ✅ All lessons demonstrate Three Roles (L02-L07)
- ✅ Skills created in L04-L06 used in L08 capstone
- ✅ Anti-convergence achieved (Architecture-First ≠ Ch40 Skill-First)

**Agent Factory Alignment**:
- ✅ L08 capstone produces sellable Digital FTE (conversational assistant)
- ✅ 3+ reusable skills created (conversation-history, session-lifecycle, auth-security)
- ✅ Students understand General Agent (ChatKit SDK) vs Custom Agent (their deployed product) distinction

---

## Implementation Guidance for Content-Implementer

**When implementing lessons from this plan**:

1. **Read context FIRST**: Spec.md, plan.md (this file), Constitution
2. **Reference quality lesson**: Chapter 40, Lesson 2 (for AI collaboration patterns)
3. **Verify canonical formats**: `.claude/skills/building-chat-interfaces/SKILL.md` for skill structure
4. **Code validation**: Test all examples against ChatKit Python SDK before publishing
5. **Fact-checking**: WebSearch all statistics, dates, ChatKit release information
6. **Three Roles enforcement**: EVERY L02-L07 lesson demonstrates Teacher/Student/Co-Worker (hidden from students)
7. **Skill creation**: L04, L05, L06 MUST guide students to create reusable skills using Chapter 5 patterns
8. **Capstone validation**: L08 MUST compose skills from L04-L06 into working system

**Parallel implementation opportunity**:
- L01 (architecture-only, no code) can be written first
- L02-L07 can be implemented in parallel AFTER L01 complete (each builds on L01 foundation)
- L08 capstone requires L02-L07 complete (orchestrates accumulated skills)

---

## Cross-Chapter Integration

**Prerequisites Validated**:
- Chapter 40 (FastAPI) → L02 assumes students understand API development, async patterns
- Chapters 34-36 (Agent SDKs) → L02 assumes students can create agents
- Part 5 (Python) → L03 assumes students understand async/await, streaming
- Chapter 5 (Skills) → L04-L06 assume students know skill creation patterns

**Prepares for Future Chapters**:
- Chapter 42 (OpenAI Apps SDK) → ChatKit patterns transfer to widget development
- Chapter 48 (Multi-Agent Orchestration) → Session management patterns scale to handoffs
- Chapter 43 (RAG Systems) → Conversation history patterns integrate with retrieval

---

## Teaching Pattern Rationale

**Why Architecture-First (not Skill-First like Chapter 40)?**

Chapter 40 (FastAPI) used Skill-First because:
- FastAPI is mature with stable, well-documented patterns
- Official docs provide comprehensive examples
- Skill creation FIRST maximizes documentation value

Chapter 41 (ChatKit) uses Architecture-First because:
- ChatKit is newer with evolving patterns (released 2024)
- Architecture understanding (Thread, RequestContext, streaming) is prerequisite to skill creation
- Building vocabulary (L01) BEFORE implementation (L02+) prevents confusion

**Both patterns serve learning—context determines which applies.**

---

## Constitutional Compliance Statement

This plan aligns with Constitution v7.0.0:

- ✅ **Agent Factory Thesis**: Every lesson contributes to Digital FTE production
- ✅ **Specification Primacy**: All lessons show spec BEFORE code
- ✅ **AI Amplification**: Students learn spec-first discipline (NOT Vibe Coding)
- ✅ **4-Layer Progression**: L01 (Manual) → L02-L07 (Layers 2-3) → L08 (Layer 4)
- ✅ **Three Roles Framework**: L02-L07 demonstrate bidirectional co-learning (hidden from students)
- ✅ **Progressive Complexity**: B1 tier, max 10 concepts per lesson
- ✅ **Intelligence Accumulation**: Skills from L04-L06 compose in L08 capstone
- ✅ **Anti-Convergence**: Architecture-First pattern (different from Ch40)
- ✅ **Digital FTE Output**: L08 produces sellable conversational agent

---

**Plan Status**: Ready for implementation by content-implementer
**Next Step**: `/sp.tasks` to create implementation checklist
**Validation**: All lessons map to spec success criteria (SC-001 through SC-008)

---

*Generated by chapter-planner agent v2.0.0 (Reasoning-Activated — Constitution v7.0.0)*
*Plan follows 4-Layer Teaching Method with Architecture-First pedagogical pattern*
*Ready for content-implementer → educational-validator workflow*
