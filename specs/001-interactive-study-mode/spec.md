# Feature Specification: Interactive Study Mode

**Feature Branch**: `feature/interactive-study-mode`
**Created**: 2026-01-23
**Status**: Draft
**Input**: User description: "Interactive Study Mode - A 'Teach Me' / 'Ask AI' interactive learning system for the AgentFactory book using ChatKit UI, OpenAPI-based backend, and provider-agnostic AI agents (OpenAI/Anthropic). Backend: Node.js (TypeScript). Streaming: Simple HTTP for MVP. Context: Frontend passes lesson path, backend reads content. Two modes: Teach (guided) and Ask (Q&A)."

---

## Overview

Interactive Study Mode adds an AI-powered learning assistant to the AgentFactory book that helps students understand lesson content through two distinct interaction modes:

1. **Teach Mode**: Guided, pedagogical interaction where the AI proactively explains concepts, asks comprehension questions, and leads students through the material in a structured way
2. **Ask Mode**: Open Q&A where students can ask any question about the current lesson and receive contextual answers

This feature embodies the Three Roles Framework (AI as Teacher, Student, Co-Worker) by enabling real-time AI collaboration during the learning experience.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Student Requests Explanation (Priority: P1)

A student reading a lesson clicks "Teach Me" to receive guided instruction on the current topic. The AI explains key concepts, checks understanding, and adapts based on student responses.

**Why this priority**: Core value proposition - transforms passive reading into active learning. Without this, the feature has no purpose.

**Independent Test**: Can be fully tested by opening any lesson, clicking "Teach Me", and receiving a contextual explanation that references specific content from that lesson.

**Acceptance Scenarios**:

1. **Given** a student is viewing Lesson 3 of Chapter 11, **When** they click "Teach Me", **Then** the AI provides an explanation specifically about that lesson's topic (not generic responses)
2. **Given** the AI has provided an explanation, **When** the student responds with confusion, **Then** the AI adapts by simplifying or providing additional examples
3. **Given** the chat panel is open, **When** the student navigates to a different lesson, **Then** the context updates to reflect the new lesson content

---

### User Story 2 - Student Asks Specific Question (Priority: P1)

A student has a specific question about something in the lesson. They switch to "Ask" mode and type their question. The AI provides a contextual answer grounded in the lesson content.

**Why this priority**: Equally critical as Teach mode - addresses students' immediate learning needs and prevents frustration.

**Independent Test**: Can be tested by asking a specific question about a code example or concept in the current lesson and verifying the answer references that specific content.

**Acceptance Scenarios**:

1. **Given** a student is in Ask mode viewing a lesson about Docker, **When** they ask "What does the FROM instruction do?", **Then** the AI answers with reference to how FROM is used in that specific lesson
2. **Given** the student asks a question unrelated to the lesson, **When** the AI responds, **Then** it acknowledges the question is off-topic and offers to help with lesson-related questions
3. **Given** the student asks about code in the lesson, **When** the AI responds, **Then** it can reference specific line numbers or code blocks from the lesson

---

### User Story 3 - Mode Switching (Priority: P2)

A student starts in Teach mode receiving guided instruction but wants to ask a specific question. They switch to Ask mode, ask their question, then switch back to continue the guided learning.

**Why this priority**: Enhances usability by allowing fluid transitions between learning styles, but not required for MVP functionality.

**Independent Test**: Can be tested by switching modes mid-conversation and verifying conversation context is preserved.

**Acceptance Scenarios**:

1. **Given** a student is in Teach mode with active conversation, **When** they switch to Ask mode, **Then** the conversation history is preserved and the AI's behavior changes to Q&A style
2. **Given** a student switches from Ask to Teach mode, **When** the AI responds, **Then** it resumes guided instruction style without repeating previous explanations

---

### User Story 4 - Chat Panel UI Interaction (Priority: P2)

A student opens the chat panel from a "Teach Me" button visible on each lesson page. The panel slides in from the side without disrupting the lesson content.

**Why this priority**: Critical for UX but technically simpler than AI interaction logic.

**Independent Test**: Can be tested by clicking the Teach Me button and verifying the panel appears with proper styling and doesn't break lesson layout.

**Acceptance Scenarios**:

1. **Given** a student is reading a lesson, **When** they click "Teach Me", **Then** a chat panel slides in from the right side
2. **Given** the chat panel is open, **When** the student clicks a close button, **Then** the panel slides out and lesson content returns to full width
3. **Given** the student is on mobile, **When** they open the chat panel, **Then** it opens as a full-screen overlay (responsive design)

---

### User Story 5 - Conversation Persistence (Priority: P3)

A student has an active conversation, navigates away to another page, then returns. Their conversation should be preserved.

**Why this priority**: Nice-to-have for MVP - improves experience but not critical for initial launch.

**Independent Test**: Can be tested by having a conversation, navigating away and back, and verifying messages are restored.

**Acceptance Scenarios**:

1. **Given** a student has an active conversation on Lesson 5, **When** they navigate to Lesson 6 and back to Lesson 5, **Then** the Lesson 5 conversation is restored
2. **Given** a student closes the browser tab, **When** they return to the same lesson within the same session, **Then** conversation is preserved (session-based persistence)

---

### Edge Cases

- **What happens when** the lesson content cannot be loaded by the backend?
  - System displays friendly error message and suggests refreshing or contacting support
- **What happens when** the AI service is unavailable?
  - System displays graceful degradation message: "AI assistant temporarily unavailable. Please try again shortly."
- **What happens when** the student sends an empty message?
  - Input is disabled until user types content; send button is inactive
- **What happens when** the student sends extremely long messages (>5000 characters)?
  - System truncates with warning or prevents submission with character limit indicator
- **What happens when** multiple tabs have the same lesson open?
  - Each tab maintains independent conversation state
- **What happens when** the lesson has no markdown content (error state)?
  - AI acknowledges it cannot access lesson context and offers limited general assistance

---

## Requirements *(mandatory)*

### Functional Requirements

#### Chat Interface (UI)

- **FR-001**: System MUST display a "Teach Me" button on every lesson page
- **FR-002**: System MUST provide a slide-out chat panel that doesn't disrupt lesson reading
- **FR-003**: System MUST support two interaction modes: "Teach" (guided) and "Ask" (Q&A)
- **FR-004**: System MUST allow users to switch between modes during a conversation
- **FR-005**: System MUST display conversation history with clear visual distinction between user and AI messages
- **FR-006**: System MUST show a loading indicator while waiting for AI responses
- **FR-007**: System MUST be responsive and work on mobile devices (panel becomes overlay)
- **FR-021**: System MUST provide a "New Chat" button to allow users to manually reset the conversation
- **FR-022**: System MUST persist conversation within browser session until user explicitly resets (no auto-reset on navigation)

#### AI Interaction (Backend)

- **FR-008**: System MUST pass the current lesson path to the backend with each request
- **FR-009**: System MUST read lesson content from the filesystem based on the lesson path
- **FR-010**: System MUST provide lesson-aware responses that reference specific content from the current lesson
- **FR-011**: System MUST support provider-agnostic AI integration (initial providers: OpenAI and Anthropic)
- **FR-012**: System MUST implement distinct AI behaviors for Teach mode vs Ask mode:
  - **Teach mode**: Proactive explanation, comprehension checks, structured guidance
  - **Ask mode**: Direct answers to user questions, contextual to lesson
- **FR-013**: System MUST include lesson content as context in AI prompts (not exposed to user)

#### API Contract

- **FR-014**: System MUST expose an API for chat interactions following OpenAPI specification
- **FR-015**: System MUST accept: lesson path, user message, conversation history, and mode selection
- **FR-016**: System MUST return: AI response text and any metadata needed for UI rendering
- **FR-017**: System MUST use simple HTTP request/response (no streaming for MVP)

#### Error Handling

- **FR-018**: System MUST display user-friendly error messages when AI service is unavailable
- **FR-019**: System MUST handle lesson content loading failures gracefully
- **FR-020**: System MUST validate input (non-empty messages, reasonable length limits)

### Non-Functional Requirements

- **NFR-001**: AI response time SHOULD be under 10 seconds for typical queries
- **NFR-002**: Chat panel SHOULD open within 200ms of button click
- **NFR-003**: System SHOULD NOT break existing book functionality or navigation
- **NFR-004**: System SHOULD work without authentication for MVP (public access)
- **NFR-005**: System MUST implement IP-based rate limiting at 60 requests per hour per IP address to prevent abuse
- **NFR-006**: System MUST log errors, AI API calls (model, tokens, latency), and rate limit events in structured format
- **NFR-007**: System MUST NOT log message content to protect student privacy
- **NFR-008**: System MUST meet WCAG 2.1 AA accessibility standards (keyboard navigation, screen reader support, sufficient color contrast)

### Key Entities

- **Message**: Represents a single chat message (role: user/assistant, content, timestamp)
- **Conversation**: A collection of messages for a specific lesson (lessonPath, messages[], mode)
- **LessonContext**: Metadata about the current lesson (path, title, content summary for AI context)
- **ChatRequest**: User's request to the API (lessonPath, userMessage, conversationHistory, mode)
- **ChatResponse**: API response (assistantMessage, metadata)

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can initiate an AI-powered learning conversation within 3 clicks from any lesson
- **SC-002**: 80% of AI responses reference specific content from the current lesson (not generic answers)
- **SC-003**: Chat panel opens and is interactive within 1 second of button click
- **SC-004**: System handles 100 concurrent users without degradation
- **SC-005**: Mode switching (Teach ↔ Ask) completes within 500ms
- **SC-006**: Error recovery displays user-friendly message within 2 seconds of failure detection
- **SC-007**: Mobile users can access full chat functionality (responsive design verification)

### Qualitative Outcomes

- **SC-008**: Students report the AI "understands" the lesson context (validated via user feedback)
- **SC-009**: Teach mode feels different from Ask mode (distinct AI personalities/behaviors)
- **SC-010**: Feature integrates seamlessly without disrupting existing book reading experience

---

## Assumptions

1. **Lesson content is accessible**: Backend has read access to lesson markdown files in the docs directory
2. **AI API keys are configured**: Environment variables for OpenAI/Anthropic API keys are set in deployment
3. **No authentication required**: MVP is publicly accessible; authentication can be added later
4. **Single language**: English only for MVP; internationalization is out of scope
5. **Session-based persistence**: Conversations persist within browser session only; no database storage for MVP
6. **Docusaurus routing**: Lesson paths can be derived from Docusaurus URL structure
7. **Reasonable message length**: Users won't send messages exceeding 5000 characters
8. **Standard browser support**: Modern browsers (Chrome, Firefox, Safari, Edge) from last 2 years

---

## Out of Scope (Non-Goals)

- **Streaming responses**: MVP uses simple HTTP; streaming can be added in future iteration
- **User authentication**: Feature works for all visitors; gated access is future enhancement
- **Conversation persistence across sessions**: No database storage; session-only for MVP
- **Multi-language support**: English only
- **Voice input/output**: Text-only interaction
- **Image/diagram generation**: Text responses only
- **Lesson modification suggestions**: AI cannot edit or suggest edits to lesson content
- **Analytics/tracking**: No tracking of AI interactions for MVP (can be added later)
- **Rate limiting per user**: Since no auth, rate limiting by IP is acceptable for MVP
- **Offline mode**: Requires internet connection for AI features

---

## Dependencies

1. **Existing learn-app**: Must integrate with current Docusaurus theme without breaking changes
2. **AI Provider APIs**: Requires valid API keys for OpenAI and/or Anthropic
3. **Filesystem access**: Backend needs read access to lesson markdown files
4. **Deployment infrastructure**: Must be deployable alongside existing Docusaurus site

---

## Clarifications

### Session 2026-01-23

- Q: What abuse prevention strategy for public API access? → A: IP-based rate limiting at 60 requests per hour per IP address
- Q: What observability/logging requirements? → A: Basic structured logging (errors, AI API calls with model/tokens/latency, rate limit hits) without message content for student privacy
- Q: What is the conversation lifecycle? → A: User-controlled persistence with "New Chat" button; conversations persist in session until user manually resets (ChatGPT-style)
- Q: What accessibility requirements? → A: Basic WCAG 2.1 AA compliance (keyboard navigation, screen reader support, sufficient color contrast)

---

## Open Questions

None - all requirements are sufficiently specified for planning phase.
