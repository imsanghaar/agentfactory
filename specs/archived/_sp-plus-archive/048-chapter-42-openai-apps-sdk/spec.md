# Feature Specification: Chapter 42 - Apps SDK (Building Interactive ChatGPT Apps)

**Feature Branch**: `048-chapter-42-openai-apps-sdk`
**Created**: 2025-12-28
**Status**: Draft
**Input**: User description: "Create a chapter for OpenAI Apps SDK. This would be chapter 42 in part-6. Check what has been covered previously and connect with that rather than creating lessons for already covered topics. The chapter lessons should be in progressive way as per our constitution."

---

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Chapter 33: Agent taxonomy, architecture patterns, tool-use concepts
- Chapter 34: OpenAI Agents SDK - agents, tools, handoffs, guardrails, sessions, tracing
- Chapter 37-38: MCP fundamentals, building MCP servers with FastMCP
- Chapter 40: FastAPI for Agents - REST API patterns, HTTP endpoints
- Python async/await, type hints, Pydantic models (Part 5)

**What this chapter must explain from scratch**:
- Widget rendering inside ChatGPT conversations (iframe sandbox)
- `window.openai` API for widget-host communication
- `text/html+skybridge` MIME type for widget resources
- Tool metadata for widget integration (`openai/outputTemplate`, `openai/widgetAccessible`)
- `structuredContent` vs `_meta` payload separation
- React hooks for widget state management (`useWidgetState`, `useOpenAiGlobal`)
- Display modes (inline, pip, fullscreen)
- Developer Mode and ngrok workflow for testing
- OAuth 2.1 authentication for ChatGPT Apps (optional advanced topic)

**Proficiency Level**: B1 (Intermediate)

---

## Chapter Overview

Chapter 42 teaches developers to build ChatGPT Apps with interactive widgets using OpenAI's Apps SDK. Unlike the OpenAI Agents SDK (Chapter 34) which creates backend agents, the Apps SDK creates user-facing applications that render rich UI inside ChatGPT conversations. This chapter bridges MCP server knowledge (Chapter 37-38) with the visual, interactive capabilities unique to the Apps SDK.

**Why Apps SDK after Agents SDK?** The Agents SDK creates intelligent backends. The Apps SDK creates the visual layer that users see and interact with. Together, they form complete ChatGPT experiences where agents process requests and widgets display results.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Understanding Apps SDK Architecture (Priority: P1)

A developer who has built MCP servers wants to understand how the Apps SDK differs and how widgets fit into ChatGPT's conversation flow.

**Why this priority**: Without understanding the three-layer architecture (ChatGPT UI → Widget iframe → MCP Server), learners cannot reason about subsequent implementation decisions.

**Independent Test**: Learner can draw the architecture diagram from memory and explain the data flow from user prompt to widget render.

**Acceptance Scenarios**:

1. **Given** a developer familiar with MCP servers, **When** they complete Lesson 1, **Then** they can explain the difference between standard MCP tools and Apps SDK tools with widgets
2. **Given** the three-layer architecture diagram, **When** asked to trace a user interaction, **Then** the developer correctly identifies: prompt → model → tool call → server response → widget render → model narration
3. **Given** the official Apps SDK examples repository, **When** exploring the kitchen_sink example, **Then** the developer identifies widget HTML, MCP server code, and tool metadata

---

### User Story 2 - Building First Widget (Priority: P1)

A developer wants to create their first ChatGPT App with a simple widget that displays data returned from an MCP tool.

**Why this priority**: Hands-on experience with the development workflow (server, ngrok, developer mode) is essential before adding complexity.

**Independent Test**: Learner can create a working ChatGPT App that displays a "Hello World" widget when the tool is invoked.

**Acceptance Scenarios**:

1. **Given** a new project directory, **When** following the lesson, **Then** the developer creates a FastMCP server with a tool that returns widget HTML
2. **Given** a running local server, **When** setting up ngrok tunnel, **Then** the developer exposes their server with an HTTPS URL
3. **Given** ChatGPT Developer Mode, **When** registering the app with the ngrok URL, **Then** the tool appears in @mentions
4. **Given** the registered app, **When** invoking the tool via conversation, **Then** the widget renders inside ChatGPT

---

### User Story 3 - Adding Widget Interactivity (Priority: P1)

A developer wants to add buttons and user interactions to their widget using the `window.openai` API.

**Why this priority**: Interactivity is the key differentiator of Apps SDK. Without it, widgets are just static HTML displays.

**Independent Test**: Learner can add an action button that triggers `sendFollowUpMessage` and see the follow-up message appear in the conversation.

**Acceptance Scenarios**:

1. **Given** a static widget, **When** adding a button with `sendFollowUpMessage`, **Then** clicking the button injects a message into the conversation
2. **Given** a widget with multiple actions, **When** implementing `callTool`, **Then** the widget can invoke another MCP tool and update its display
3. **Given** the `window.openai` API, **When** checking for API availability, **Then** the developer uses optional chaining (`window.openai?.methodName`) for safety

---

### User Story 4 - Managing Widget State (Priority: P2)

A developer wants their widget to persist user selections and preferences across tool invocations within a conversation.

**Why this priority**: State management enables complex multi-step workflows. Without it, widgets reset on each tool call.

**Independent Test**: Learner can implement a favorites list that persists when the user triggers follow-up actions.

**Acceptance Scenarios**:

1. **Given** a widget with selectable items, **When** user selects items and triggers a follow-up, **Then** the selections persist via `setWidgetState`
2. **Given** persisted widget state, **When** the widget reloads, **Then** it reads from `window.openai.widgetState` and restores the UI
3. **Given** the `useWidgetState` React hook, **When** implementing a React widget, **Then** state synchronizes automatically between component and host

---

### User Story 5 - Controlling Display Modes (Priority: P2)

A developer wants to offer fullscreen mode for their widget when displaying detailed data like tables or dashboards.

**Why this priority**: Display modes enhance user experience for data-heavy applications.

**Independent Test**: Learner can add a button that switches the widget to fullscreen mode.

**Acceptance Scenarios**:

1. **Given** an inline widget, **When** calling `requestDisplayMode({mode: "fullscreen"})`, **Then** the widget expands to full viewport
2. **Given** fullscreen mode, **When** user clicks back, **Then** the widget returns to inline mode
3. **Given** mobile viewport, **When** requesting pip mode, **Then** the system coerces to fullscreen (per platform behavior)

---

### User Story 6 - Building TaskManager ChatGPT App (Priority: P1)

A developer wants to build a complete TaskManager application as a ChatGPT App with task list widget, add/complete/delete functionality, and persistent state.

**Why this priority**: This capstone demonstrates all learned concepts in a realistic application.

**Independent Test**: Learner delivers a working TaskManager ChatGPT App that can be demonstrated to users.

**Acceptance Scenarios**:

1. **Given** the TaskManager spec, **When** implementing with Claude Code, **Then** the app includes: MCP server with 3+ tools, interactive widget, state persistence
2. **Given** the running app, **When** adding a task via conversation, **Then** the widget updates to show the new task
3. **Given** tasks in the widget, **When** clicking complete/delete, **Then** the task state updates via `callTool`
4. **Given** conversation context, **When** resuming after a follow-up, **Then** task list persists via `widgetState`

---

### Edge Cases

- What happens when `window.openai` is undefined? (Widget loaded outside ChatGPT)
- How does the widget handle network errors from `callTool`?
- What happens when widget HTML exceeds size limits?
- How does caching affect widget updates during development?
- What happens when oauth token expires mid-session?

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Chapter MUST include 7-8 lessons following L1→L2→L3→L4 pedagogical progression
- **FR-002**: Lesson 1 (L1) MUST explain Apps SDK architecture without AI assistance first
- **FR-003**: Lessons 2-5 (L2) MUST use Claude Code as pair programmer for implementation
- **FR-004**: Lesson 6-7 (L3/L4) MUST apply patterns to build complete TaskManager App
- **FR-005**: Each lesson MUST include 3 "Try With AI" prompts with learning explanations
- **FR-006**: All code examples MUST be verified against official Apps SDK documentation
- **FR-007**: Chapter MUST NOT repeat concepts already covered in Chapters 34, 37-38, 40
- **FR-008**: Chapter MUST reference and build upon MCP concepts from Chapter 37-38
- **FR-009**: All widget examples MUST use `text/html+skybridge` MIME type
- **FR-010**: All window.openai API usage MUST include availability checks

### Key Entities

- **Widget**: HTML/CSS/JS bundle rendered in ChatGPT iframe, communicates via `window.openai`
- **MCP Server**: Backend exposing tools and resources, built with FastMCP (Python) or TypeScript SDK
- **Tool Response**: Contains `structuredContent` (model sees), `content` (optional text), `_meta` (widget only)
- **Widget State**: Persisted UI state scoped to conversation message, accessed via `widgetState`/`setWidgetState`

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Learners can create a working ChatGPT App with widget from scratch in under 60 minutes
- **SC-002**: Learners can explain the three-layer architecture and data flow without referring to notes
- **SC-003**: TaskManager capstone demonstrates 4+ interactive features (add, list, complete, delete tasks)
- **SC-004**: All code examples execute successfully when copied from the lessons
- **SC-005**: Learners can extend the TaskManager with one additional feature independently
- **SC-006**: 90% of learners successfully complete the ngrok + Developer Mode setup on first attempt

---

## Lesson Structure

### Lesson 1: Apps SDK Architecture (L1 - Manual First)
- Three-layer architecture explanation
- Difference from OpenAI Agents SDK
- Exploring official examples (kitchen_sink)
- Data flow walkthrough (prompt → widget)
- **No AI assistance** - build mental model first

### Lesson 2: Your First ChatGPT App (L2 - AI Collaboration)
- Project setup with FastMCP
- Widget resource registration (`text/html+skybridge`)
- Tool definition with `openai/outputTemplate`
- Development workflow: ngrok + Developer Mode
- **With Claude Code** as pair programmer

### Lesson 3: Widget Interactivity (L2 - AI Collaboration)
- `window.openai` API deep dive
- `sendFollowUpMessage` for action buttons
- `callTool` for tool chaining
- API availability checks
- **With Claude Code** as pair programmer

### Lesson 4: Response Payload Design (L2 - AI Collaboration)
- `structuredContent` vs `_meta` separation
- What the model sees vs what the widget sees
- Tool metadata options
- **With Claude Code** as pair programmer

### Lesson 5: State and Display Modes (L2 - AI Collaboration)
- `widgetState` and `setWidgetState`
- React hooks: `useWidgetState`, `useOpenAiGlobal`
- Display modes: inline, pip, fullscreen
- **With Claude Code** as pair programmer

### Lesson 6: Building TaskManager Widget (L3 - Pattern Application)
- Spec-driven approach
- Implementing task list display
- Add/complete/delete interactions
- State persistence across follow-ups
- **Pattern extraction** for reusable widget components

### Lesson 7: TaskManager Capstone (L4 - Orchestration)
- Complete implementation review
- Testing and debugging
- Deployment considerations
- Future extensions (authentication, file uploads)
- **Full spec-driven orchestration**

### Lesson 8: Chapter Quiz
- 50-question assessment covering all concepts

---

## Assumptions

1. Learners have completed Chapters 33-34, 37-38, 40 or equivalent knowledge
2. Learners have Python 3.11+ and Node.js 18+ installed
3. Learners have access to ChatGPT Plus or Enterprise (for Developer Mode)
4. ngrok is available for tunneling (free tier sufficient)
5. Examples use Python/FastMCP for server (consistent with Part 6 pattern)
6. OAuth 2.1 authentication is optional advanced content (not required for basic apps)

---

## Dependencies

- **Chapter 34**: OpenAI Agents SDK concepts (agents, tools, runners)
- **Chapter 37-38**: MCP server implementation patterns
- **Chapter 40**: FastAPI patterns (HTTP, CORS, async handlers)
- **Skill**: `.claude/skills/building-chatgpt-apps/SKILL.md` - expertise source

---

## Out of Scope

- TypeScript/Node.js server implementation (mention as alternative)
- Complex OAuth 2.1 flows (brief mention, not hands-on)
- Production deployment (covered in Part 7)
- Multiple widget types in single app (advanced pattern)
- iframe embedding within widgets (increases review complexity)
