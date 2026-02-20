### Core Concept
Workflow drift occurs when memories injected at turn 1 become irrelevant by turn 20—the AI's actual needs drift from the initial context. Mid-stream memory injection via PreToolUse hooks uses the AI's current thinking as the query, retrieving memories relevant to what it's doing NOW rather than what you asked for originally.

### Key Mental Models
- **Workflow Drift**: Turn 1 memories were selected for turn 1's intent. By turn 20, the task has evolved. Memories that would help turn 20 are sitting unused in your memory store.
- **Two Injection Points**: UserPromptSubmit fires once when you send a message—good for session setup. PreToolUse fires before each tool execution—provides multiple opportunities to inject evolving context throughout the workflow.
- **Thinking Blocks as Queries**: The AI's thinking contains current intent, decision context, and constraints. Embedding this thinking and searching for similar memories retrieves context relevant to the current action, not the original prompt.

### Critical Patterns
- Extract last ~1,500 characters of thinking block for embedding
- Query vector database for similar memories; inject top N results via `additionalContext`
- Implement deduplication using thinking hashes—prevent repeated injection if thinking hasn't changed
- Keep injection under 500ms to avoid workflow delays

### Common Mistakes
- Memories too generic—they match everything. Make them specific: "Acme's GC requires dollar ranges in risk summaries"
- Over-injecting early: UserPromptSubmit handles early turns; PreToolUse adds value in longer workflows
- Forgetting to combine strategies: UserPromptSubmit for baseline context + PreToolUse for evolving relevance

### Connections
- **Builds on**: Progress files and session architecture (Lesson 7)
- **Leads to**: Context isolation for multi-agent coordination (Lesson 9)
