---
sidebar_position: 4
title: "Conversation History Management"
description: "Load thread history, serialize conversation context for agent memory, and create reusable conversation-history skill"
keywords: [chatkit, thread history, conversation memory, agent context, store API, pagination, skill creation]
chapter: 41
lesson: 4
duration_minutes: 40

# HIDDEN SKILLS METADATA
skills:
  - name: "Thread History Loading"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student loads thread history using store.load_thread_items() with pagination parameters and verifies correct item order"

  - name: "History Context Serialization"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student serializes thread history into agent-consumable format maintaining role-message structure"

  - name: "Reusable Skill Creation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student creates conversation-history skill matching canonical format with patterns, verification, and references sections"

learning_objectives:
  - objective: "Load thread history from ChatKit store using store.load_thread_items() API with pagination"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Code exercise: Load last 20 messages from thread and verify message ordering"

  - objective: "Serialize thread history into agent system prompt format for conversation memory"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Code exercise: Convert ThreadItem list to formatted history string"

  - objective: "Create conversation-history skill using canonical format from building-chat-interfaces"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Skill verification: conversation-history skill passes format validation and includes working code patterns"

cognitive_load:
  new_concepts: 9
  assessment: "B1 appropriate (9 concepts): store.load_thread_items API, pagination (after/limit/order), history serialization for agent context, context window management, conversation branching, history pruning strategies, token counting for context limits, skill extraction trigger (pattern recurs 2+), canonical skill format for history patterns. Scaffolded through manual practice then AI-assisted skill creation."

differentiation:
  extension_for_advanced: "Implement conversation branching (load from specific message ID), add semantic summarization for long histories (embed recent messages, summarize older context), or implement token-aware pruning (calculate token count, truncate to model limits)"
  remedial_for_struggling: "Start with simpler load_thread_items() call without pagination, use print() to inspect ThreadItem structure before serialization, reference building-chat-interfaces skill as skill creation template"
---

# Conversation History Management

Your agent responds to user messages but treats each interaction as brand new—no memory of previous questions, no continuity between sessions. The user asks, "What was that task we discussed earlier?" and your agent replies, "I don't see any previous discussion." The conversation context exists in the database, but it never reaches the agent's prompt.

This isn't a bug in ChatKit. It's a missing step in your respond() implementation. ChatKit provides the storage API—`store.load_thread_items()`—but leaves history serialization to you. This lesson shows you how to load conversation history, format it for agent consumption, and extract the recurring pattern into a reusable skill.

By the end, you'll have built the `conversation-history` skill that transforms ChatKit's thread storage into agent memory.

---

## Loading Thread History from Store

ChatKit stores every message in the thread database. The `store.load_thread_items()` method retrieves conversation history with control over ordering, pagination, and filtering.

**Method Signature**:

```python
from chatkit.types import Page, ThreadItem

async def load_thread_items(
    self,
    thread_id: str,
    *,
    after: str | None = None,
    limit: int | None = None,
    order: Literal["asc", "desc"] = "asc",
) -> Page[ThreadItem]:
```

**Parameters**:
- `thread_id`: Conversation identifier (from `thread.id` in respond())
- `after`: Load items after this item ID (pagination cursor)
- `limit`: Maximum number of items to return (default: all)
- `order`: `"asc"` (oldest first) or `"desc"` (newest first)

**Returns**: `Page[ThreadItem]` object containing `.data` (list of items) and pagination metadata

### Loading Recent History

Most agents don't need the entire conversation history—recent context suffices. Load the last 20 messages:

```python
from chatkit.server import ChatKitServer
from chatkit.types import ThreadMetadata, UserMessageItem, ThreadItem
from typing import AsyncIterator, Any

class MemoryAwareServer(ChatKitServer):
    async def respond(
        self,
        thread: ThreadMetadata,
        input: UserMessageItem | None,
        context: Any,
    ) -> AsyncIterator[ThreadStreamEvent]:
        # Load last 20 messages (newest first)
        page = await self.store.load_thread_items(
            thread.id,
            after=None,
            limit=20,
            order="desc",  # Newest messages first
            context=context,
        )

        # Extract items from Page object
        history_items = page.data

        # Reverse to chronological order (oldest → newest)
        history_items.reverse()

        # Now serialize history_items for agent...
```

**Output** (when thread has 5 messages):
```
Loaded 5 thread items from thread_abc123
Items in chronological order:
  1. user: "Create a task for the demo"
  2. assistant: "Task created: Demo preparation"
  3. user: "What's the deadline?"
  4. assistant: "The deadline is December 31st"
  5. user: "Can you extend it by one week?"
```

**Why reverse after loading?** ChatKit's `order="desc"` gives newest messages first (efficient pagination), but agents expect chronological order (oldest → newest) for conversation flow.

---

## Serializing History for Agent Context

Agents consume conversation history as formatted strings in their system prompt or as message arrays. ChatKit's `ThreadItem` objects need conversion to agent-consumable format.

**ThreadItem Structure** (simplified):

```python
@dataclass
class ThreadItem:
    id: str                    # Message identifier
    role: Literal["user", "assistant", "tool"]
    content: str               # Message text
    created_at: int            # Unix timestamp
    # ... additional fields
```

### Building History String

Convert `ThreadItem` list to formatted conversation:

```python
def serialize_history(items: list[ThreadItem]) -> str:
    """Convert thread items to conversation history string."""
    lines = []
    for item in items:
        if item.role == "user":
            lines.append(f"User: {item.content}")
        elif item.role == "assistant":
            lines.append(f"Assistant: {item.content}")
        # Skip tool messages (internal agent operations)

    return "\n".join(lines)

# Usage in respond()
history_string = serialize_history(history_items)

# Include in agent system prompt
system_prompt = f"""You are a TaskManager assistant.

Previous conversation:
{history_string}

Current request follows. Maintain continuity with conversation history."""
```

**Output**:
```
You are a TaskManager assistant.

Previous conversation:
User: Create a task for the demo
Assistant: Task created: Demo preparation
User: What's the deadline?
Assistant: The deadline is December 31st
User: Can you extend it by one week?

Current request follows. Maintain continuity with conversation history.
```

### Alternative: Message Array Format

Some agent frameworks (like OpenAI SDK) accept message arrays:

```python
def serialize_to_messages(items: list[ThreadItem]) -> list[dict]:
    """Convert thread items to message array format."""
    messages = []
    for item in items:
        if item.role in ("user", "assistant"):
            messages.append({
                "role": item.role,
                "content": item.content
            })
    return messages

# Usage with OpenAI SDK
from agents import Agent, Runner

history_messages = serialize_to_messages(history_items)

result = Runner.run_streamed(
    agent=agent,
    messages=[
        *history_messages,  # Previous conversation
        {"role": "user", "content": input.content}  # Current input
    ]
)
```

**Output** (message array):
```python
[
    {"role": "user", "content": "Create a task for the demo"},
    {"role": "assistant", "content": "Task created: Demo preparation"},
    {"role": "user", "content": "What's the deadline?"},
    {"role": "assistant", "content": "The deadline is December 31st"},
    {"role": "user", "content": "Can you extend it by one week?"}
]
```

**Choosing serialization format**: Use string format for simple agents (concatenate into system prompt), use message array for SDK-based agents (Runner.run_streamed() accepts messages parameter).

---

## Context Window Management Strategies

Not all conversation history fits in the agent's context window. Long threads require pruning strategies to stay within token limits.

| Strategy | When to Use | Trade-offs |
|----------|-------------|------------|
| **Recent Window** | General conversations | Loses older context but maintains recent continuity |
| **Token-Aware Pruning** | Production systems | Prevents context overflow, requires token counting |
| **Semantic Summarization** | Long-running support threads | Preserves key information, adds summarization cost |
| **Conversation Branching** | Multi-topic threads | Isolates topics, requires explicit branching UI |

### Recent Window Strategy (Simplest)

Load fixed number of recent messages:

```python
# Load last 20 messages
page = await self.store.load_thread_items(
    thread.id,
    after=None,
    limit=20,
    order="desc",
    context=context,
)
history_items = page.data
history_items.reverse()
```

**Pros**: Simple, predictable memory usage
**Cons**: Hard cutoff may lose important context mid-conversation

### Token-Aware Pruning Strategy

Calculate token count and truncate to model limits:

```python
import tiktoken  # OpenAI tokenizer

def prune_to_token_limit(
    items: list[ThreadItem],
    max_tokens: int = 8000  # Leave room for response
) -> list[ThreadItem]:
    """Keep most recent messages within token budget."""
    encoding = tiktoken.encoding_for_model("gpt-4")

    pruned_items = []
    total_tokens = 0

    # Process newest → oldest, keep until budget exceeded
    for item in reversed(items):
        item_tokens = len(encoding.encode(item.content))
        if total_tokens + item_tokens > max_tokens:
            break  # Stop before exceeding budget

        pruned_items.insert(0, item)  # Maintain chronological order
        total_tokens += item_tokens

    return pruned_items

# Usage
page = await self.store.load_thread_items(
    thread.id,
    after=None,
    order="desc",
    context=context,
)
history_items = prune_to_token_limit(page.data, max_tokens=8000)
```

**Output** (with 15,000 token conversation):
```
Original: 42 messages (15,247 tokens)
Pruned: 28 messages (7,983 tokens)
Removed 14 oldest messages to fit context window
```

**When to use**: Production systems where context overflow causes failures. Requires `tiktoken` library (`uv add tiktoken`).

---

## Extract Your conversation-history Skill

You've implemented history loading, serialization, and context management. This pattern will recur across every ChatKit server you build—customer support, code review, content moderation. Time to harvest this intelligence.

**Layer 3 trigger**: Pattern recurs 2+ times across projects → Create reusable intelligence

### Step: Extract the Skill

Copy and paste this prompt:

```
Using your skill-creator skill, study the conversation history implementation
code I just wrote in this lesson and extract it into a reusable
conversation-history skill.

Encapsulate: loading thread history with Page.data extraction, serialization
patterns (string/array formats), token-aware pruning with tiktoken, and
common pitfalls with fixes.
```

Claude will:
1. Review the implementation code from this lesson
2. Use `skill-creator` to generate the skill structure
3. Populate patterns: load history, serialize, prune tokens
4. Create reference docs with string/array serialization formats
5. Add verification checklist matching canonical format

Your skill appears at `.claude/skills/conversation-history/`.

---

## Integrating History into Agent Workflow

With the skill created, apply it to your ChatKit server:

```python
from chatkit.server import ChatKitServer
from chatkit.agents import stream_agent_response
from agents import Agent, Runner

class TaskManagerServer(ChatKitServer):
    async def respond(self, thread, input, context):
        # STEP 1: Load conversation history (conversation-history skill)
        page = await self.store.load_thread_items(
            thread.id,
            after=None,
            limit=20,
            order="desc",
            context=context,
        )
        history_items = page.data
        history_items.reverse()

        # STEP 2: Serialize to message array format
        history_messages = [
            {"role": item.role, "content": item.content}
            for item in history_items
            if item.role in ("user", "assistant")
        ]

        # STEP 3: Create agent with history context
        agent = Agent(
            name="TaskManager",
            instructions="You are a task management assistant. Maintain conversation continuity.",
            tools=[]  # Add task management tools
        )

        # STEP 4: Run agent with history
        result = Runner.run_streamed(
            agent=agent,
            messages=[
                *history_messages,  # Previous conversation
                {"role": "user", "content": input.content}  # Current input
            ]
        )

        # STEP 5: Stream response
        async for event in stream_agent_response(context, result):
            yield event
```

**Output** (user continues conversation from previous session):
```
User: Can you extend it by one week?

[Agent loads history, sees previous deadline discussion]
Agent: Extended deadline from December 31st to January 7th. Task updated.
```

Agent remembers the December 31st deadline from history and calculates the one-week extension correctly.

**Safety Note**: Always validate thread ownership in production (check `context.user_id` matches thread owner) before loading history. Multi-tenant systems must enforce thread access controls to prevent unauthorized history access.

---

## Try With AI: Apply Your conversation-history Skill

You've extracted the conversation history patterns into a reusable skill. Now test it on new scenarios.

### Prompt 1: Semantic Conversation Branching

```
Using my conversation-history skill, implement conversation branching that
loads history from a specific message ID (not just the most recent 20).

This enables users to "rewind" the conversation to an earlier point and
continue from there, creating a conversation tree.
```

**What you're learning**: How to extend skill patterns beyond the basic implementation. Your skill provides the foundation (load history, serialize), and you add branching logic on top.

### Prompt 2: Multi-User Conversation Filtering

```
Using my conversation-history skill, modify the history loading to filter by
user_id. This enables group chat scenarios where each user only sees messages
relevant to them (private DMs mixed with group messages).
```

**What you're learning**: How to compose skills with security requirements. Your conversation-history skill handles loading/serialization; you add access control filtering.

### Prompt 3: Semantic Summarization

```
Using my conversation-history skill, add a summarization layer that embeds
recent messages verbatim but summarizes older messages to save tokens.

Recent 10 messages: Full text
Messages 11-50: Summarized to 2 sentences each
Messages 51+: Single paragraph summary of entire history
```

**What you're learning**: How skills become platforms for experimentation. Your conversation-history skill provides the primitives (load, serialize, prune); you layer advanced features (embedding, summarization) on top without rewriting the foundation.