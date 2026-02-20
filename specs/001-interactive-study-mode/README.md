# Interactive Study Mode

A "Teach Me" / "Ask AI" interactive learning system for the AgentFactory book.

## Features

- **Teach Mode**: Guided instruction where AI explains concepts step-by-step
- **Ask Mode**: Q&A where students can ask any question about the lesson
- **ChatKit UI**: Professional chat interface using @chatscope/chat-ui-kit-react
- **Provider-Agnostic**: Supports OpenAI, Anthropic, or mock provider
- **Mobile Responsive**: Full-width panel on mobile, 400px slide-out on desktop
- **WCAG 2.1 AA Compliant**: Keyboard navigation, screen reader support, reduced motion

## Quick Start

### 1. Start the Frontend (Dev Server)

```bash
cd apps/learn-app
pnpm start
```

Open http://localhost:3000 and navigate to any lesson page.

### 2. Start the API Backend

```bash
cd api
cp .env.example .env
# Edit .env with your API keys
pnpm dev
```

The API runs at http://localhost:3001

### 3. Configure AI Provider

Edit `api/.env`:

```env
# Use mock provider (no API key needed)
AI_PROVIDER=mock

# Or use OpenAI
AI_PROVIDER=openai
OPENAI_API_KEY=sk-your-key-here

# Or use Anthropic
AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend (Docusaurus)                    │
├─────────────────────────────────────────────────────────────┤
│  TeachMePanel (ChatKit UI)                                  │
│    ├── ModeToggle (Teach/Ask)                               │
│    ├── MessageList (@chatscope)                             │
│    ├── MessageInput (@chatscope)                            │
│    └── TypingIndicator                                      │
├─────────────────────────────────────────────────────────────┤
│  StudyModeContext (React Context + sessionStorage)          │
│    ├── Panel state (open/closed)                            │
│    ├── Mode state (teach/ask)                               │
│    └── Conversations (per-lesson)                           │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ POST /api/chat
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     Backend (Node.js)                        │
├─────────────────────────────────────────────────────────────┤
│  Chat Handler                                               │
│    ├── Request validation                                   │
│    ├── Rate limiting (60 req/hr/IP)                         │
│    └── Structured logging                                   │
├─────────────────────────────────────────────────────────────┤
│  AI Provider (adapter pattern)                              │
│    ├── OpenAIProvider                                       │
│    ├── AnthropicProvider                                    │
│    └── MockProvider (for testing)                           │
├─────────────────────────────────────────────────────────────┤
│  Lesson Loader                                              │
│    └── Reads markdown content from filesystem               │
└─────────────────────────────────────────────────────────────┘
```

## API Endpoints

### POST /api/chat

Request:
```json
{
  "lessonPath": "/docs/01-foundations/01-intro",
  "userMessage": "Teach me about AI agents",
  "conversationHistory": [],
  "mode": "teach"
}
```

Response:
```json
{
  "assistantMessage": "Let me explain AI agents...",
  "metadata": {
    "model": "gpt-4o-mini",
    "tokensUsed": 150,
    "processingTimeMs": 1200
  }
}
```

### GET /api/health

Returns server status.

## File Structure

```
api/
├── src/
│   ├── handlers/chat.ts      # Main request handler
│   ├── services/
│   │   ├── ai-provider.ts    # OpenAI/Anthropic adapters
│   │   ├── lesson-loader.ts  # Content loading
│   │   └── rate-limiter.ts   # IP-based rate limiting
│   ├── prompts/
│   │   ├── teach-mode.ts     # Teach mode system prompt
│   │   └── ask-mode.ts       # Ask mode system prompt
│   ├── server.ts             # HTTP server
│   └── types.ts              # TypeScript interfaces
├── .env.example
└── package.json

apps/learn-app/src/
├── components/TeachMePanel/
│   ├── index.tsx             # Main panel (ChatKit)
│   ├── ModeToggle.tsx        # Teach/Ask toggle
│   ├── ChatMessages.tsx      # Legacy (kept for reference)
│   ├── ChatInput.tsx         # Legacy (kept for reference)
│   ├── useStudyModeAPI.ts    # API hook
│   └── styles.module.css     # Styles + ChatKit overrides
├── contexts/
│   └── StudyModeContext.tsx  # Global state
└── theme/
    ├── Root.tsx              # Provider wrapper
    └── DocItem/Content/      # "Teach Me" button
```

## Testing

### API Tests
```bash
cd api
pnpm test
```

### Integration Tests
```bash
cd apps/learn-app
pnpm test
```

## Deployment

### Vercel (Recommended)

1. Connect repository to Vercel
2. Add environment variables:
   - `AI_PROVIDER`
   - `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`
3. Deploy

### Self-Hosted

1. Build the frontend:
   ```bash
   cd apps/learn-app
   pnpm build
   ```

2. Start the API:
   ```bash
   cd api
   pnpm start
   ```

3. Serve the static files and proxy `/api` to the API server.

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `AI_PROVIDER` | `mock` | AI provider: `openai`, `anthropic`, or `mock` |
| `OPENAI_API_KEY` | - | OpenAI API key |
| `OPENAI_MODEL` | `gpt-4o-mini` | OpenAI model to use |
| `ANTHROPIC_API_KEY` | - | Anthropic API key |
| `ANTHROPIC_MODEL` | `claude-3-haiku-20240307` | Anthropic model |
| `RATE_LIMIT_REQUESTS_PER_HOUR` | `60` | Rate limit per IP |
| `CONTENT_BASE_PATH` | `../apps/learn-app/docs` | Path to lesson content |
| `PORT` | `3001` | API server port |

## Accessibility

- WCAG 2.1 AA compliant
- Full keyboard navigation (Tab, Enter, Escape)
- Screen reader announcements for messages
- Respects `prefers-reduced-motion`
- 44px touch targets on mobile

## Specification Documents

- [spec.md](./spec.md) - Feature specification
- [plan.md](./plan.md) - Implementation plan
- [accessibility-audit.md](./accessibility-audit.md) - WCAG audit results
- [mobile-responsive-verification.md](./mobile-responsive-verification.md) - Mobile testing
