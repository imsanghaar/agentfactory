# Implementation Plan: Interactive Study Mode

**Branch**: `feature/interactive-study-mode` | **Date**: 2026-01-23 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-interactive-study-mode/spec.md`

---

## Summary

Add an AI-powered "Teach Me" / "Ask AI" interactive learning assistant to the AgentFactory book. Students can engage with lesson content through two modes: **Teach** (guided instruction) and **Ask** (Q&A). The feature uses a platform-agnostic Node.js/TypeScript API backend with provider-agnostic AI integration (OpenAI/Anthropic).

**Key Constraints**:
- No database
- No authentication
- No backend session state
- Client-side state only (sessionStorage)
- Platform-agnostic code
- Extend existing components (minimal PR scope)

---

## Technical Context

**Language/Version**: TypeScript 5.x, Node.js 18+
**React Version**: Use existing repo version (do not assume specific version)
**Primary Dependencies**: OpenAI SDK, Anthropic SDK
**Storage**: Client-side sessionStorage only (no database)
**Testing**: Vitest (frontend), Jest or Vitest (API)
**Target Platform**: Decasaurus-based documentation site (Docusaurus-compatible) + Platform-agnostic API
**Project Type**: Web application (frontend + API)
**Performance Goals**: <10s AI response time, <200ms panel open
**Constraints**: 60 req/hr/IP rate limit, no message logging, WCAG 2.1 AA
**Scale/Scope**: 100 concurrent users (MVP)

---

## Constitution Check

*GATE: Verified against AgentFactory constitution*

| Principle | Status | Notes |
|-----------|--------|-------|
| Specification Primacy | PASS | Spec complete before planning |
| Platform-Agnostic | PASS | No vendor lock-in in code |
| No Unnecessary State | PASS | Client-side only, no DB |
| Privacy-Preserving | PASS | No message content logging |
| Accessibility | PASS | WCAG 2.1 AA required |

---

## Project Structure

### Documentation (this feature)

```text
specs/001-interactive-study-mode/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Phase 0 research output
├── data-model.md        # Entity definitions
├── quickstart.md        # Developer setup guide
├── contracts/           # References api/openapi.yaml (no duplication)
└── tasks.md             # Task breakdown (created by /sp.tasks)
```

### Source Code (repository root)

```text
api/
├── openapi.yaml               # SINGLE SOURCE OF TRUTH for API contract
├── src/
│   ├── handlers/
│   │   └── chat.ts            # Platform-agnostic chat handler
│   ├── services/
│   │   ├── ai-provider.ts     # Provider adapter (OpenAI/Anthropic)
│   │   ├── lesson-loader.ts   # Load lesson content from filesystem
│   │   └── rate-limiter.ts    # IP-based rate limiting
│   ├── prompts/
│   │   ├── teach-mode.ts      # System prompt for Teach mode
│   │   └── ask-mode.ts        # System prompt for Ask mode
│   └── types.ts               # TypeScript interfaces
├── adapters/
│   └── vercel.ts              # OPTIONAL: Vercel serverless adapter
├── package.json
└── tsconfig.json

apps/learn-app/src/
├── components/
│   └── TeachMePanel/          # NEW: Chat panel component
│       ├── index.tsx
│       ├── ChatMessages.tsx
│       ├── ChatInput.tsx
│       ├── ModeToggle.tsx
│       └── useStudyMode.ts
├── contexts/
│   └── StudyModeContext.tsx   # NEW: Global state for panel
└── theme/
    └── DocItem/
        └── Content/
            └── index.tsx      # MODIFY: Add Teach Me button to existing
```

**Structure Decision**: Extend existing Decasaurus theme/components. Minimize new directories. API in existing `api/` folder with optional deployment adapters.

---

## Component Architecture

### Frontend Components

```
┌────────────────────────────────────────────────────────────────┐
│                    DocItem/Content (EXISTING)                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    Lesson Content                         │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────┐                                          │
│  │ FloatingActions  │ ← ADD "Teach Me" button here             │
│  │ [Zen] [Teach Me] │                                          │
│  └──────────────────┘                                          │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │               TeachMePanel (slide-out)                    │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │ Header: [Teach] [Ask] toggle  [New Chat] [Close X] │  │  │
│  │  ├────────────────────────────────────────────────────┤  │  │
│  │  │              ChatMessages                          │  │  │
│  │  ├────────────────────────────────────────────────────┤  │  │
│  │  │ ChatInput: [Type message...] [Send]               │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

### Backend Architecture

```
    Client                      API                         AI Provider
      │                          │                               │
      │  POST /api/chat          │                               │
      │ ─────────────────────────>│                               │
      │                          │ 1. Rate limit check           │
      │                          │ 2. Validate request           │
      │                          │ 3. Load lesson content        │
      │                          │ 4. Select mode prompt         │
      │                          │ 5. Call AI provider ─────────>│
      │                          │<───────────────────────────────│
      │                          │ 6. Log metrics (no content)   │
      │<──────────────────────────│                               │
```

---

## Implementation Phases

### Phase 1: API Backend (Priority: P1) - MOCK-FIRST

| Task | Description | Dependencies |
|------|-------------|--------------|
| 1.1 | Create TypeScript interfaces from OpenAPI | None |
| 1.2 | Implement AI provider adapter (OpenAI + Anthropic) | 1.1 |
| 1.3 | Implement lesson loader (filesystem) | 1.1 |
| 1.4 | Create Teach mode system prompt | 1.1 |
| 1.5 | Create Ask mode system prompt | 1.1 |
| 1.6 | Implement rate limiter (IP-based, in-memory) | 1.1 |
| 1.7 | Implement chat handler (orchestrates all) | 1.2-1.6 |
| 1.8 | Add structured logging | 1.7 |
| 1.9 | Create Vercel adapter (OPTIONAL) | 1.7 |

### Phase 2: Frontend UI (Priority: P1)

| Task | Description | Dependencies |
|------|-------------|--------------|
| 2.1 | Create StudyModeContext | None |
| 2.2 | Create ChatMessages component | 2.1 |
| 2.3 | Create ChatInput component | 2.1 |
| 2.4 | Create ModeToggle component | 2.1 |
| 2.5 | Create TeachMePanel component | 2.2-2.4 |
| 2.6 | Create useStudyMode hook (API calls) | 2.1 |
| 2.7 | Add "Teach Me" button to DocItem/Content | 2.5, 2.6 |
| 2.8 | Implement sessionStorage persistence | 2.6 |
| 2.9 | Add "New Chat" button functionality | 2.5 |

### Phase 3: Integration & Polish (Priority: P2)

| Task | Description | Dependencies |
|------|-------------|--------------|
| 3.1 | Connect frontend to backend API | 1.7, 2.7 |
| 3.2 | Add loading states and error handling | 3.1 |
| 3.3 | Implement mobile responsive design | 2.5 |
| 3.4 | Add keyboard accessibility (WCAG 2.1 AA) | 2.5 |
| 3.5 | Add screen reader support | 2.5 |
| 3.6 | End-to-end testing | 3.1-3.5 |

### Phase 4: Deployment (Priority: P2)

| Task | Description | Dependencies |
|------|-------------|--------------|
| 4.1 | Configure environment variables | None |
| 4.2 | Deploy to target platform | 3.6, 4.1 |

---

## Testing Strategy (Mock-First)

### Phase 1 Testing Approach

1. **Mock AI Providers First**: Test handler logic without real API calls
2. **Contract Tests**: Validate request/response matches OpenAPI spec
3. **Real Provider Tests**: Integration tests with actual AI APIs (staging only)

### Unit Tests

| Component | Test Focus |
|-----------|------------|
| `ai-provider.ts` | Provider selection, mock responses, error handling |
| `rate-limiter.ts` | IP tracking, limit enforcement, reset logic |
| `lesson-loader.ts` | Path resolution, content loading, error cases |
| `chat.ts` handler | Request validation, response format, orchestration |

---

## OpenAPI Source of Truth

The API contract is defined in `api/openapi.yaml`. This is the **single source of truth**.

- Specs reference this file (no duplication)
- TypeScript types generated from this file
- SDK generation uses this file
- Tests validate against this contract

---

## Next Steps

1. Run `/sp.tasks` to generate detailed task breakdown
2. **Start Phase 1 with mock-first testing**
3. Implement API handlers with mocked AI providers
4. Add real provider integration after mock tests pass
5. Proceed to Phase 2 (Frontend) after Phase 1 complete
