# Quickstart: Interactive Study Mode

**Date**: 2026-01-23
**Feature**: Interactive Study Mode

---

## Prerequisites

- Node.js 18+ installed
- pnpm installed
- API key for OpenAI or Anthropic

## Environment Setup

Create a `.env.local` file in the repository root:

```bash
# AI Provider (choose one)
OPENAI_API_KEY=sk-...
# OR
ANTHROPIC_API_KEY=sk-ant-...

# Provider selection (default: anthropic)
AI_PROVIDER=anthropic  # or "openai"
```

## Local Development

### 1. Install Dependencies

```bash
pnpm install
```

### 2. Start the Learn App (Docusaurus)

```bash
pnpm nx serve learn-app
```

The book will be available at `http://localhost:3000`.

### 3. Start the API (Development Mode)

```bash
# From api/ directory
pnpm dev
```

The API will be available at `http://localhost:3001/api/chat`.

## Testing the Feature

### Manual Test

1. Open any lesson page in the book
2. Click the "Teach Me" button (floating action)
3. Type a message and press Enter
4. Verify AI responds with lesson-aware content

### API Test (curl)

```bash
curl -X POST http://localhost:3001/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "lessonPath": "/docs/01-foundations/01-intro",
    "userMessage": "Explain this lesson to me",
    "conversationHistory": [],
    "mode": "teach"
  }'
```

Expected response:

```json
{
  "assistantMessage": "Welcome to the Agent Factory! Let me guide you through...",
  "metadata": {
    "model": "claude-3-opus",
    "tokensUsed": 450,
    "processingTimeMs": 2340
  }
}
```

## Deployment

### Vercel (Recommended for MVP)

1. Push to GitHub
2. Connect repo to Vercel
3. Add environment variables in Vercel dashboard:
   - `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`
   - `AI_PROVIDER`
4. Deploy

### Other Platforms

The API handlers are platform-agnostic. For other platforms:

1. Create a thin adapter that calls the handler functions
2. Configure environment variables
3. Deploy as standard Node.js application

## Troubleshooting

### Rate Limited

If you see `RATE_LIMITED` errors, wait 1 hour or use a different IP.

### AI Unavailable

Check that your API key is valid and has sufficient credits.

### Lesson Not Found

Ensure the lesson path matches a valid path in `apps/learn-app/docs/`.
