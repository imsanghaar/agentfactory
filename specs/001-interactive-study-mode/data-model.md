# Data Model: Interactive Study Mode

**Date**: 2026-01-23
**Feature**: Interactive Study Mode

---

## Overview

This feature is **stateless on the backend**. All entities exist either:
- In the API request/response cycle (transient)
- In the browser (client-side state)

**No database. No backend session state.**

---

## Entities

### 1. Message

Represents a single chat message in the conversation.

```typescript
interface Message {
  role: 'user' | 'assistant';
  content: string;
  timestamp: string; // ISO 8601
}
```

**Storage**: Client-side only (React state or sessionStorage)

---

### 2. ChatRequest

The request payload sent from frontend to backend.

```typescript
interface ChatRequest {
  lessonPath: string;        // e.g., "/docs/01-foundations/03-principles/01-intro"
  userMessage: string;       // The user's current message
  conversationHistory: Message[];  // Previous messages for context
  mode: 'teach' | 'ask';     // Interaction mode
}
```

**Validation Rules**:
- `lessonPath`: Required, must be valid URL path format
- `userMessage`: Required, 1-5000 characters
- `conversationHistory`: Optional, array of Message objects
- `mode`: Required, must be 'teach' or 'ask'

---

### 3. ChatResponse

The response payload returned from backend to frontend.

```typescript
interface ChatResponse {
  assistantMessage: string;  // AI-generated response
  metadata: ResponseMetadata;
}

interface ResponseMetadata {
  model: string;             // e.g., "gpt-4" or "claude-3-opus"
  tokensUsed: number;        // For monitoring/logging
  processingTimeMs: number;  // Latency tracking
}
```

---

### 4. ErrorResponse

Standard error format for API failures.

```typescript
interface ErrorResponse {
  error: {
    code: string;            // e.g., "RATE_LIMITED", "AI_UNAVAILABLE"
    message: string;         // Human-readable message
  };
}
```

**Error Codes**:
| Code | HTTP Status | Description |
|------|-------------|-------------|
| `VALIDATION_ERROR` | 400 | Invalid request payload |
| `RATE_LIMITED` | 429 | Exceeded 60 req/hour limit |
| `LESSON_NOT_FOUND` | 404 | Lesson content couldn't be loaded |
| `AI_UNAVAILABLE` | 503 | AI provider error |
| `INTERNAL_ERROR` | 500 | Unexpected server error |

---

### 5. LessonContext (Internal)

Used internally by the backend to construct AI prompts. Not exposed in API.

```typescript
interface LessonContext {
  path: string;
  title: string;
  content: string;           // Markdown content (may be truncated)
  chapterNumber: number;
  lessonNumber: number;
}
```

---

## Client-Side State

### ConversationState

Managed in React component state or Context.

```typescript
interface ConversationState {
  messages: Message[];
  mode: 'teach' | 'ask';
  isLoading: boolean;
  error: string | null;
  lessonPath: string;
}
```

### Persistence Strategy

| Storage | Scope | Use Case |
|---------|-------|----------|
| React State | Component lifecycle | Active conversation |
| sessionStorage | Browser tab | Persist across page navigations |
| None (server) | N/A | **No backend persistence** |

---

## Entity Relationships

```
┌─────────────────────────────────────────────────────────────┐
│                        BROWSER                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ConversationState                                           │
│  ├── messages: Message[]                                     │
│  ├── mode: 'teach' | 'ask'                                  │
│  └── lessonPath: string                                     │
│                                                              │
│         │                                                    │
│         │ (user sends message)                              │
│         ▼                                                    │
│                                                              │
│  ChatRequest ─────────────────────────────────────────────┐ │
│  { lessonPath, userMessage, conversationHistory, mode }   │ │
│                                                           │ │
└───────────────────────────────────────────────────────────┼─┘
                                                            │
                              HTTP POST /api/chat           │
                                                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     API (Stateless)                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Validate ChatRequest                                     │
│  2. Load LessonContext from filesystem                       │
│  3. Construct AI prompt (mode-specific)                      │
│  4. Call AI provider                                         │
│  5. Return ChatResponse                                      │
│                                                              │
│  (No state stored. Each request is independent.)            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                                                            │
                              HTTP 200                       │
                                                            ▼
┌─────────────────────────────────────────────────────────────┐
│                        BROWSER                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ChatResponse                                                │
│  { assistantMessage, metadata }                             │
│         │                                                    │
│         │ (update state)                                    │
│         ▼                                                    │
│  ConversationState.messages.push(newMessage)                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Volume Estimates

| Data | Typical Size | Max Size |
|------|--------------|----------|
| Single Message | 100-500 bytes | 5KB (5000 chars) |
| Conversation (10 msgs) | 1-5 KB | 50 KB |
| Lesson Content | 5-50 KB | 100 KB |
| API Request | 10-60 KB | 150 KB |
| API Response | 500 bytes - 5 KB | 10 KB |

**Note**: Large lesson content may need truncation to fit AI context windows.
