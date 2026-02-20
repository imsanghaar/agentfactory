# ChatKit Python SDK Research

**Research Date**: 2025-12-31
**Purpose**: Gather accurate ChatKit Server patterns for Chapter 41 lesson content

## Official Documentation Sources

- **Main Documentation**: https://openai.github.io/chatkit-python/
- **Server Integration Guide**: https://openai.github.io/chatkit-python/server/
- **Respond to User Message Guide**: https://openai.github.io/chatkit-python/guides/respond-to-user-message/
- **Thread Stream Events**: https://openai.github.io/chatkit-python/concepts/thread-stream-events/
- **GitHub Repository**: https://github.com/openai/chatkit-python/

## Core Architecture

### ChatKitServer Base Class

The ChatKitServer base class is the main building block of the ChatKit server implementation. The `respond` method is executed each time a user sends a message and is responsible for providing an answer by streaming a set of events.

### respond() Method Signature

```python
async def respond(
    self,
    thread: ThreadMetadata,
    input: UserMessageItem | None,
    context: Any,
) -> AsyncIterator[ThreadStreamEvent]:
```

**Parameters**:
- `thread`: ThreadMetadata - Contains conversation container with metadata (thread ID, etc.)
- `input`: UserMessageItem | None - The user's message content
- `context`: Any - RequestContext with user identity and session information

**Returns**: AsyncIterator[ThreadStreamEvent] - Stream of events (assistant messages, tool status, workflows, tasks, widgets)

### Key Primitives

1. **Thread**: Conversation container with metadata
2. **ThreadItem**: Individual message (user/assistant/tool)
3. **ThreadMetadata**: Thread-level information (ID, timestamps)
4. **UserMessageItem**: User input message type
5. **RequestContext**: User identity and session context
6. **ThreadStreamEvent**: Events yielded during response streaming

## Streaming Patterns

ChatKit uses Server-Sent Events (SSE) for streaming:
- Token-by-token output
- Progressive UI updates
- Event-driven architecture
- stream_agent_response() helper for Agents SDK integration

## Integration with Agents SDK

ChatKit provides helpers to implement respond() using the OpenAI Agents SDK:

```python
from chatkit.agents import stream_agent_response
from agents import Agent, Runner

# Inside respond() method:
agent = Agent(name="Assistant", tools=[...], instructions="...")
result = Runner.run_streamed(agent, user_message)
async for event in stream_agent_response(context, result):
    yield event
```

## Capabilities

The respond() method can return:
- Assistant messages
- Tool status messages
- Workflows
- Tasks
- Widgets

## Conversation Persistence

Unlike stateless REST APIs, ChatKitServer manages ongoing conversation relationships:
- Thread history loaded from store
- Conversation state maintained across requests
- Multi-tenant isolation via RequestContext

## Key Differences from FastAPI

| Aspect | FastAPI | ChatKitServer |
|--------|---------|---------------|
| Pattern | Request/response | Event streaming |
| State | Stateless | Stateful conversation |
| Output | Single response | Async iterator of events |
| Lifecycle | One-shot | Ongoing relationship |
| Method | Route handler | respond() method |

## Notes for Lessons

**L01 (Architecture)**: Focus on Thread, ThreadItem, RequestContext, respond() signature, streaming vs request/response paradigm

**L02 (First Agent)**: Demonstrate stream_agent_response() helper, basic agent integration

**L03 (Streaming)**: Deep dive into ThreadStreamEvent types, async iteration patterns

**L04 (History)**: Load thread items from store, build history context for agent

**L05 (Sessions)**: RequestContext for user isolation, session management patterns

**L06 (Auth)**: Multi-tenant authentication, context metadata validation

**L07 (React)**: Coordinate with research-chatkit-react.md for useChatKit patterns

**L08 (Capstone)**: Integrate all primitives into production TaskManager agent
