### Core Concept
Sampling lets servers request LLM inference from clients without managing API keys. Server asks "Can you run Claude on this?", client responds with result. Costs shift to client, server stays provider-agnostic, complexity vanishes.

### Key Mental Models
- **Cost shifting**: Client pays for inference, not server—aligns incentives
- **Provider agnostic**: Server doesn't know which LLM client uses; just requests reasoning
- **Hybrid systems**: Fast deterministic operations on server, reasoning via sampling
- **Never embed API keys**: Sampling eliminates server-side credential management

### Critical Patterns
- Server-side: `await ctx.session.create_message(messages=[...], max_tokens=1000, system_prompt="...")`
- Message structure: `SamplingMessage(role="user", content=TextContent(type="text", text="..."))`
- Response handling: `result.content[0].text` for text responses
- Use cases: Summarization, code analysis, content moderation, decision support

### AI Collaboration Keys
- Server fetches/formats data; Claude synthesizes via sampling
- Combine deterministic operations (search, filter) with AI reasoning (summarize, analyze)
- Client bears token costs—use sampling responsibly

### Common Mistakes
- Embedding API keys in server (use sampling instead)
- Using sampling for purely deterministic operations (wastes tokens)
- Not handling sampling failures gracefully

### Connections
- **Builds on**: Context Object & Server Lifespan (Lesson 1)
- **Leads to**: Progress & Logging Notifications (Lesson 3)
