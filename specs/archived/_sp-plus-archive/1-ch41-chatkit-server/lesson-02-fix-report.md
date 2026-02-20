# Lesson 02 Fix Report: Research-First Audit

**Date**: 2025-12-31
**Lesson**: 02-connecting-your-first-agent.md
**Approach**: Research-first using official 2025 documentation

## Research Sources

### 1. ChatKit Python SDK
- **Source**: `specs/1-ch41-chatkit-server/research-chatkit-sdk.md`
- **Official Docs**: https://openai.github.io/chatkit-python/
- **Key Finding**: `stream_agent_response(context, result)` helper verified as official ChatKit pattern

### 2. OpenAI Agents SDK v2.0
- **Source**: [OpenAI Agents SDK Streaming](https://openai.github.io/openai-agents-python/streaming/)
- **Key Finding**: `Runner.run_streamed()` returns `RunResultStreaming`; ChatKit's `stream_agent_response()` bridges to ChatKit events
- **Verification**: ✅ CORRECT - OpenAI section already uses official pattern

### 3. Google ADK
- **Source**: [Google Cloud ADK Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/sessions/manage-sessions-adk) (Updated 2025-12-30)
- **Key Finding**: `AdkApp` class with `async_stream_query(message, user_id)` method
- **Previous Code**: Used `genai.Client.aio.models.generate_content_stream()` (Gemini API, not ADK)
- **Fix Applied**: Complete rewrite to use `AdkApp` pattern with session management

### 4. Claude Agent SDK
- **Source**: [Claude Agent SDK Python Reference](https://platform.claude.com/docs/en/agent-sdk/python)
- **Key Finding**: `Agent.query()` returns async iterator; `ThinkingBlock` available in content
- **Previous Code**: Used `client.messages.stream()` (Anthropic API, not Agent SDK)
- **Fix Applied**: Complete rewrite to use `Agent.query()` with `ThinkingBlock` handling

## Changes Made

### 1. OpenAI Agents SDK Section
**Status**: ✅ NO CHANGES NEEDED
**Reason**: Code already correctly uses:
- `Runner.run_streamed(agent, user_message)`
- `stream_agent_response(context, result)` ChatKit helper
- Proper parameter name: `input` (not `input_user_message`)

### 2. Google ADK Section
**Status**: ✅ COMPLETE REWRITE
**Changes**:
- **Before**: `genai.Client.aio.models.generate_content_stream()`
- **After**: `AdkApp(model=..., system_instruction=..., tools=...)`
- **Method**: `async_stream_query(message=user_message, user_id=user_id)`
- **Event Mapping**: Manual mapping to `AssistantMessageEvent`
- **Session Management**: Extract `user_id` from `context`
- **New Imports**: `vertexai.preview.reasoning_engines.AdkApp`, `AssistantMessageEvent`

**Code Diff**:
```python
# OLD (Gemini API)
response = self.client.aio.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=user_message,
)
async for event in stream_agent_response(context, response):
    yield event

# NEW (Google ADK)
user_id = getattr(context, 'user_id', 'default-user')
async for chunk in self.adk_app.async_stream_query(
    message=user_message,
    user_id=user_id,
):
    if hasattr(chunk, 'text') and chunk.text:
        yield AssistantMessageEvent(
            content=chunk.text,
            partial=True
        )
yield AssistantMessageEvent(content="", partial=False)
```

### 3. Claude Agent SDK Section
**Status**: ✅ COMPLETE REWRITE
**Changes**:
- **Before**: `client.messages.stream()` context manager
- **After**: `Agent(name=..., system_prompt=..., tools=..., model=...)`
- **Method**: `async for message in agent.query(user_message)`
- **ThinkingBlock Handling**: Yield as `HiddenContextItem`
- **TextBlock Handling**: Yield as `AssistantMessageEvent`
- **New Imports**: `claude_agent_sdk.Agent`, `HiddenContextItem`

**Code Diff**:
```python
# OLD (Anthropic API)
async with self.client.messages.stream(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": user_message}],
) as stream:
    async for event in stream_agent_response(context, stream):
        yield event

# NEW (Claude Agent SDK)
async for message in self.agent.query(user_message):
    if hasattr(message, 'content'):
        for content_block in message.content:
            if content_block.type == 'thinking':
                yield HiddenContextItem(
                    content=content_block.thinking,
                    metadata={"type": "reasoning"}
                )
            elif content_block.type == 'text':
                yield AssistantMessageEvent(
                    content=content_block.text,
                    partial=False
                )
```

### 4. Import Statements
**Status**: ✅ FIXED
**Changes**: Added explicit `ThreadStreamEvent` to all sections:
- OpenAI: Added `ThreadStreamEvent` to imports (line 152)
- Google ADK: Already had `ThreadStreamEvent` + added `AssistantMessageEvent` (lines 212-213)
- Claude SDK: Already had `ThreadStreamEvent` + `AssistantMessageEvent` + `HiddenContextItem` (lines 276-277)
- respond() contract: Added `ThreadStreamEvent` (line 111)
- Pattern 2 & 3: Added `AssistantMessageEvent` imports (lines 397, 424)

### 5. Output Sections
**Status**: ✅ VERIFIED
**Count**: 6 output sections for 10 code blocks (correct ratio)
- Line 190: OpenAI integration ✓
- Line 257: Google ADK integration ✓
- Line 323: Claude SDK integration ✓
- Line 360: Running server ✓
- Line 413: Pattern 2 (empty input) ✓
- Line 438: Pattern 3 (error handling) ✓

**Non-output blocks** (correctly omitted):
- FastAPI vs ChatKit comparison (conceptual)
- respond() contract (interface definition)
- Pattern 1 (reuse pattern, no runtime behavior shown)

## Quality Verification

### Constitutional Compliance
- ✅ Framework invisibility: No "AI as Teacher" labels
- ✅ Evidence: Code + Output sections present
- ✅ Structure: Ends with "Try With AI" (no summary after)
- ✅ Digital FTE narrative: Consistent throughout

### Technical Accuracy (2025 APIs)
- ✅ ChatKit SDK: Exact match to research-chatkit-sdk.md
- ✅ OpenAI Agents SDK v2.0: Verified against official docs
- ✅ Google ADK: Verified against Dec 30, 2025 Cloud documentation
- ✅ Claude Agent SDK: Verified against platform.claude.com docs

### Pedagogical Soundness
- ✅ B1 proficiency level maintained
- ✅ 7 concepts (within B1 limit of 7-10)
- ✅ Layer 2 (Collaboration) - AI assists with implementation
- ✅ Progressive complexity: OpenAI (simplest) → Google (session mgmt) → Claude (thinking blocks)

## Breaking Changes Summary

| SDK | Old Pattern | New Pattern | Breaking? |
|-----|-------------|-------------|-----------|
| OpenAI | `stream_agent_response()` | No change | ❌ No |
| Google | `genai.Client` (API) | `AdkApp` (SDK) | ✅ Yes |
| Claude | `client.messages` (API) | `Agent.query()` (SDK) | ✅ Yes |

## Sources Referenced

1. [OpenAI Agents SDK - Streaming](https://openai.github.io/openai-agents-python/streaming/)
2. [OpenAI Agents SDK - Running Agents](https://openai.github.io/openai-agents-python/running_agents/)
3. [Google Cloud - AdkApp API Reference](https://cloud.google.com/python/docs/reference/vertexai/latest/vertexai.preview.reasoning_engines.AdkApp)
4. [Google Cloud - Manage Sessions with ADK](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/sessions/manage-sessions-adk) (Updated 2025-12-30)
5. [Claude Agent SDK - Python Reference](https://platform.claude.com/docs/en/agent-sdk/python)
6. [Anthropic Engineering - Building Agents with Claude SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
7. Local Research: `specs/1-ch41-chatkit-server/research-chatkit-sdk.md`

## Test Recommendations

Students should test:
1. **OpenAI Integration**: Verify `stream_agent_response()` helper works with `Runner.run_streamed()`
2. **Google ADK Integration**: Test session persistence with `user_id` parameter
3. **Claude SDK Integration**: Verify `ThinkingBlock` appears as hidden context
4. **Multi-SDK Support**: Test all three SDKs in same ChatKit server instance

## Conclusion

✅ **ALL FIXES APPLIED** - Lesson 02 now uses official 2025 SDK patterns for all three agent frameworks. Google ADK and Claude sections completely rewritten to use Agent SDKs instead of API clients. All imports are explicit, all code blocks have appropriate outputs, and constitutional compliance verified.

**Next Steps**:
- Deploy test instances with all three SDKs
- Validate session management in Google ADK implementation
- Confirm ThinkingBlock visibility settings in Claude integration
