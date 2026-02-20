### Core Concept
ClaudeSDKClient enables multi-turn conversations with persistent context. Unlike query() (single-turn, stateless), the client maintains session state across sequential queries. Message generators enable dynamic streaming input with images and files.

### Key Mental Models
- **query() vs ClaudeSDKClient**: query = one-shot autonomous; client = multi-turn conversational
- **Context accumulation**: Each turn adds constraints, agent builds on prior understanding
- **Streaming generators**: Yield message parts dynamically for programmatic control

### Critical Patterns
- Multi-turn: `async with ClaudeSDKClient(options) as client:` + multiple `await client.query()`
- Streaming input: `async def generator(): yield {"type": "user", "message": {...}}`
- Image insertion: Yield base64 image in message content array
- Interrupt: `await client.interrupt()` pauses long-running analysis

### AI Collaboration Keys
- Use ClaudeSDKClient for specification accumulation (add constraints progressively)
- Streaming generators enable complex multi-file analysis requests
- Combine streaming + client: complex first turn, then interactive follow-ups

### Common Mistakes
- Using query() for iterative refinement (loses context between calls)
- Building complete prompts when generators could compose dynamically
- Not capturing session for resumption in long-running conversations

### Connections
- **Builds on**: Custom MCP Tools (Lesson 11)
- **Leads to**: Cost Tracking and Billing (Lesson 13)
