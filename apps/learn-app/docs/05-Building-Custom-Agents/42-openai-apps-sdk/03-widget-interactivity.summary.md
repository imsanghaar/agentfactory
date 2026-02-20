### Core Concept
`sendFollowUpMessage` triggers new conversation turns from widget buttons. Button click → message appears → model processes → tool called → widget updates. Optional chaining (`window.openai?.`) prevents crashes outside ChatGPT.

### Key Mental Models
- **Widget-to-conversation**: Button clicks insert user messages into conversation
- **API availability**: `window.openai` only exists inside ChatGPT—use optional chaining
- **structuredContent flow**: Server data → `window.openai.toolOutput` → widget display
- **Round-trip pattern**: Click → sendFollowUpMessage → tool call → new widget

### Critical Patterns
- Safe API call: `window.openai?.sendFollowUpMessage?.({ prompt: "Refresh" })`
- Data access: `const data = window.openai?.toolOutput`
- Button handler: `onclick="refresh()"` with async function
- Server response: `structuredContent={"message": "...", "timestamp": now}`

### AI Collaboration Keys
- Prompt 1: Add multiple buttons with different prompts
- Prompt 2: Add loading state during API call
- Prompt 3: Collect user input and send as prompt

### Common Mistakes
- Forgetting optional chaining (crashes in browser preview)
- Not using `structuredContent` (widget can't read server data)
- Calling `window.openai.sendFollowUpMessage` without `?.` (fails outside ChatGPT)

### Connections
- **Builds on**: Your First Widget (Lesson 2)
- **Leads to**: Displaying Tasks (Lesson 4)
