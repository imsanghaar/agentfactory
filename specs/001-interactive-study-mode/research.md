# Research: Interactive Study Mode

**Date**: 2026-01-23
**Feature**: Interactive Study Mode
**Researcher**: Claude (via Explore agent)

---

## 1. Existing Infrastructure Analysis

### Docusaurus Theme Structure

| Component | Location | Reusability |
|-----------|----------|-------------|
| `DocItem/Content/index.tsx` | `apps/learn-app/src/theme/` | **INTEGRATION POINT** - Add Teach Me button here |
| `DocItem/Layout/index.tsx` | `apps/learn-app/src/theme/` | Minimal wrapper, no changes needed |
| `Root.tsx` | `apps/learn-app/src/theme/` | Global providers - may add TeachModeContext |
| `FloatingActions` | Inside DocItem/Content | Already has zen mode toggle - add alongside |

**Decision**: Add "Teach Me" button to `DocItem/Content/index.tsx` FloatingActions section (line ~181)

### Existing Chat Components

| Component | Location | Assessment |
|-----------|----------|------------|
| `ChatPanel.tsx` | `src/components/HeroIDESimulation/` | **REUSABLE** - Full chat UI with typing animation |
| `AgentChat.tsx` | `src/components/HeroIDESimulation/` | Simpler variant, less featured |

**Decision**: Extract and adapt `ChatPanel.tsx` for TeachMePanel component

---

## 2. Monorepo Structure

### Current Apps

```
apps/
├── learn-app/     # Docusaurus (port 3000) - Main book
├── sso/           # Next.js (port 3001) - Auth server
└── panaversity-fs-py/  # Python/FastAPI - Backend service
```

### API Skeleton (Already Created)

```
api/
├── openapi.yaml       # Empty - needs spec
├── routes/
│   └── chat.ts        # Empty - needs implementation
└── agents/
    ├── teachingAgent.ts  # Empty - needs implementation
    └── askAgent.ts       # Empty - needs implementation
```

**Decision**: Use existing `api/` folder structure. Code is platform-agnostic Node.js/TypeScript.

---

## 3. Deployment Configuration

### Platform-Agnostic Design

**Principle**: API code is standard Node.js/Express-style handlers. Deployment target (Vercel, Cloud Run, Docker, etc.) is a separate concern.

**API Handler Pattern**:
```typescript
// Platform-agnostic handler
export async function handleChatRequest(req: ChatRequest): Promise<ChatResponse> {
  // Business logic here - no platform-specific code
}

// Vercel adapter (if deployed to Vercel)
export default async function handler(req, res) {
  const result = await handleChatRequest(req.body);
  res.json(result);
}
```

**Decision**: Write platform-agnostic handlers. Deployment adapters are thin wrappers.

---

## 4. Dependencies Analysis

### Already Available in learn-app

- `react` 19.0.0
- `@radix-ui/*` - UI components (dialogs, dropdowns)
- `tailwindcss` 4.0.0

### Need to Add (API)

| Package | Purpose | Version |
|---------|---------|---------|
| `openai` | OpenAI API client | ^4.x |
| `@anthropic-ai/sdk` | Claude API client | ^0.x |

**Decision**: Add both AI provider SDKs for provider-agnostic support. No database or session libraries needed.

---

## 5. Architectural Decisions

### ADR-001: API Architecture

**Context**: Need backend for AI chat proxying with rate limiting and logging.

**Decision**: Platform-agnostic Node.js/TypeScript handlers in `api/` folder.

**Rationale**:
- Standard HTTP handlers work anywhere
- No platform lock-in
- Easy to deploy to Vercel, Cloud Run, Docker, etc.

### ADR-002: Response Format

**Context**: Spec says "simple HTTP for MVP" (no streaming).

**Decision**: Standard JSON request/response.

**Rationale**:
- Simpler implementation
- Easier error handling
- Streaming can be added later without API contract changes

### ADR-003: Session Handling

**Context**: Conversations persist in browser session only (per spec).

**Decision**: **Client-side only**. No backend session state.

**Constraints**:
- NO database
- NO authentication
- NO backend session storage
- All state lives in browser (sessionStorage or React state)

**Rationale**:
- Simplest architecture
- Privacy-preserving (nothing stored server-side)
- Stateless backend is easier to scale

### ADR-004: AI Provider Strategy

**Context**: Support both OpenAI and Anthropic (per spec).

**Decision**: Provider adapter pattern with environment variable selection.

**Rationale**:
- Single API contract
- Provider switching via config
- Easy to add more providers later

---

## 6. Integration Points

### Frontend → Backend

```
TeachMePanel (React)
    │
    ├─ POST /api/chat
    │   ├─ Request: { lessonPath, userMessage, conversationHistory, mode }
    │   └─ Response: { assistantMessage, metadata }
    │
    └─ Rate limited: 60 req/hour/IP (implemented in handler)
```

### Backend → AI Provider

```
/api/chat handler (stateless)
    │
    ├─ Read lesson content from filesystem (or receive from frontend)
    ├─ Construct system prompt (Teach vs Ask mode)
    ├─ Call AI provider (OpenAI or Anthropic)
    └─ Return response + log metrics (structured, no message content)
```

### State Management (Client-Side Only)

```
Browser
    │
    ├─ React State: Current conversation, mode, panel open/closed
    ├─ sessionStorage (optional): Persist across page navigations
    └─ NO server-side state
```

---

## 7. Risk Mitigation

| Risk | Mitigation |
|------|------------|
| AI provider timeout | Reasonable timeout (30s), graceful error message |
| Rate limiting abuse | IP-based limiting in handler (platform-agnostic) |
| AI provider outage | Graceful error message; no fallback for MVP |
| Large lesson content | Summarize/truncate to fit context window |

---

## 8. Summary of Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| API Design | Platform-agnostic handlers | No vendor lock-in |
| Response Format | Simple HTTP (JSON) | Per spec, simpler implementation |
| Session Handling | **Client-side only** | No database, no backend state |
| Authentication | **None for MVP** | Public access per spec |
| AI Providers | OpenAI + Anthropic | Provider-agnostic per spec |
| Chat UI | Adapt existing ChatPanel.tsx | Reuse proven component |
| Integration Point | DocItem/Content FloatingActions | Natural placement, existing pattern |
| Rate Limiting | 60 req/hr/IP (in handler) | Per clarification session |
| Logging | Structured (no message content) | Per clarification session |
