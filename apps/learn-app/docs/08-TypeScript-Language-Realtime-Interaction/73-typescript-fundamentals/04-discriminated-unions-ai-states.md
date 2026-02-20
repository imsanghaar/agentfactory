---
sidebar_position: 4
title: "Discriminated Unions for AI States"
description: "Model complex AI response states with exhaustive type checking using TypeScript's discriminated unions—the killer feature for streaming UIs."
keywords: ["TypeScript", "discriminated unions", "tagged unions", "type narrowing", "AI states", "streaming UI", "exhaustive checking", "never type"]
chapter: 73
lesson: 4
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Discriminated Union Design"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can define discriminated unions with literal type discriminators for AI response states"

  - name: "Exhaustive Switch Pattern"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can write switch statements with never-type exhaustiveness checks"

  - name: "Type Narrowing in Practice"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can explain how TypeScript narrows union types inside switch cases"

  - name: "AI State Machine Modeling"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "AI Application Development"
    measurable_at_this_level: "Student can model AI streaming states (idle, loading, streaming, complete, error) with type safety"

learning_objectives:
  - objective: "Define discriminated unions using literal type discriminators"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates union type with type property distinguishing variants"

  - objective: "Implement exhaustive switch statements with never type checks"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student writes switch with default case that catches unhandled variants at compile time"

  - objective: "Explain how TypeScript narrows types inside switch cases"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student describes how accessing state.content is only valid inside streaming case"

  - objective: "Model tool call responses vs content responses with discriminated unions"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates union distinguishing tool_call and content response types"

cognitive_load:
  new_concepts: 5
  assessment: "5 new concepts (discriminated unions, literal discriminator, exhaustive switch, never type, type narrowing in switch) within A2 limit of 7 - PASS"

differentiation:
  extension_for_advanced: "Implement nested discriminated unions for complex tool call states; create generic discriminated union factories"
  remedial_for_struggling: "Focus on the streaming state example only; skip tool call modeling until pattern is comfortable"

generated_by: content-implementer
created: 2026-01-01
last_modified: 2026-01-01
version: 1.0.0
---

# Discriminated Unions for AI States

Your AI agent is streaming a response. The user sees "Thinking..." then tokens start appearing. Suddenly, the model decides to call a tool—the UI needs to show a different component. Then the tool returns, and streaming resumes. Finally, the response completes with usage statistics.

How do you represent these distinct states in TypeScript? How do you ensure your code handles *every* possible state? How do you prevent the bug where your UI tries to render `content` when you're actually in a `loading` state with no content at all?

This is where TypeScript's discriminated unions become essential. They're not just a nice feature—they're the difference between streaming UIs that crash mysteriously and streaming UIs that handle every edge case correctly.

## The Problem: AI Responses Have Many Shapes

Consider what happens during a streaming AI response:

```typescript
// At different moments, your response looks completely different:

// Moment 1: Just started
{ status: "loading" }

// Moment 2: Tokens arriving
{ status: "streaming", content: "Here's the answer...", tokens: 15 }

// Moment 3: Complete
{ status: "complete", content: "Here's the full answer.", usage: { total: 127 } }

// Moment 4: Something went wrong
{ status: "error", message: "Rate limit exceeded", code: 429 }
```

In Python, you might handle this with `isinstance()` checks or dictionary access with `.get()`. But there's no compile-time safety—you discover bugs at runtime when users report crashes.

TypeScript offers something better.

## Discriminated Unions: The Pattern

A **discriminated union** (also called a "tagged union") is a union type where every variant shares a common property with a literal type value. That property is the **discriminator**—it tells TypeScript which variant you have.

```typescript
// Each variant has a 'type' property with a LITERAL value
type StreamingState =
  | { type: "idle" }
  | { type: "loading" }
  | { type: "streaming"; content: string; tokens: number }
  | { type: "complete"; content: string; usage: { total: number } }
  | { type: "error"; message: string; code: number };
```

**Output:**
```
// TypeScript now understands:
// - When type is "idle", no other properties exist
// - When type is "streaming", content and tokens MUST exist
// - When type is "error", message and code MUST exist
```

The key insight: `type: "idle"` is not the same as `type: string`. It's a **literal type**—it can ONLY be the string `"idle"`, nothing else.

### Why This Matters for AI Applications

Compare with a naive approach:

```typescript
// WRONG: No type safety
type BadState = {
  status: string;
  content?: string;
  tokens?: number;
  message?: string;
  code?: number;
  usage?: { total: number };
};

function handleBadState(state: BadState) {
  if (state.status === "streaming") {
    // TypeScript doesn't know content exists!
    console.log(state.content.length); // Could crash: content is possibly undefined
  }
}
```

**Output:**
```
Error: Cannot read property 'length' of undefined
```

With discriminated unions, TypeScript **proves** that properties exist:

```typescript
// CORRECT: Full type safety
function handleState(state: StreamingState) {
  if (state.type === "streaming") {
    // TypeScript KNOWS content exists here!
    console.log(state.content.length); // Safe: content is string
  }
}
```

**Output:**
```
15  // No crash—TypeScript guarantees content exists
```

## Exhaustive Switch Statements

The real power appears when you use `switch` statements. TypeScript tracks which variants you've handled:

```typescript
function handleState(state: StreamingState): string {
  switch (state.type) {
    case "idle":
      return "Ready to start";
    case "loading":
      return "Thinking...";
    case "streaming":
      return state.content; // TypeScript knows: content exists
    case "complete":
      return `Done! ${state.usage.total} tokens used`;
    case "error":
      return `Error ${state.code}: ${state.message}`;
  }
}
```

**Output:**
```typescript
handleState({ type: "idle" })
// "Ready to start"

handleState({ type: "streaming", content: "Hello", tokens: 5 })
// "Hello"

handleState({ type: "error", message: "Timeout", code: 504 })
// "Error 504: Timeout"
```

Inside each `case`, TypeScript **narrows** the type automatically. When you're in `case "streaming"`, the variable `state` has type `{ type: "streaming"; content: string; tokens: number }`—not the full union.

### The never Type: Catching Missing Cases

What happens if you add a new state but forget to handle it? Without protection, your code silently does nothing. With TypeScript, you can make this a compile-time error:

```typescript
function handleState(state: StreamingState): string {
  switch (state.type) {
    case "idle":
      return "Ready";
    case "loading":
      return "Loading...";
    case "streaming":
      return state.content;
    case "complete":
      return `Done: ${state.usage.total} tokens`;
    case "error":
      return `Error: ${state.message}`;
    default:
      // This line is the exhaustiveness check
      const _exhaustive: never = state;
      throw new Error(`Unhandled state: ${_exhaustive}`);
  }
}
```

**Output:**
```typescript
// If all cases handled: _exhaustive is never reached, no error
// If you add a new variant and forget to handle it:
// Error: Type '{ type: "cancelled" }' is not assignable to type 'never'
```

Here's why this works:

1. After handling all cases, `state` has type `never`—meaning "this can never happen"
2. If you add `{ type: "cancelled" }` to the union but don't add a case, `state` in the default branch has type `{ type: "cancelled" }`
3. Assigning `{ type: "cancelled" }` to `never` fails—TypeScript reports an error

**This catches bugs at compile time, not in production.**

## Modeling Tool Calls vs Content

AI responses often have fundamentally different structures depending on whether the model generated content or called a tool:

```typescript
type AIResponse =
  | {
      type: "content";
      text: string;
      finish_reason: "stop" | "length";
    }
  | {
      type: "tool_call";
      name: string;
      arguments: Record<string, unknown>;
      call_id: string;
    }
  | {
      type: "tool_result";
      call_id: string;
      result: unknown;
    };
```

**Output:**
```typescript
// Example responses from an AI API:
const content: AIResponse = {
  type: "content",
  text: "The weather in Tokyo is sunny.",
  finish_reason: "stop"
};

const toolCall: AIResponse = {
  type: "tool_call",
  name: "get_weather",
  arguments: { city: "Tokyo" },
  call_id: "call_abc123"
};
```

Now handle each type safely:

```typescript
function processResponse(response: AIResponse): void {
  switch (response.type) {
    case "content":
      // TypeScript knows: text and finish_reason exist
      console.log(`AI said: ${response.text}`);
      if (response.finish_reason === "length") {
        console.log("(response was truncated)");
      }
      break;

    case "tool_call":
      // TypeScript knows: name, arguments, call_id exist
      console.log(`Calling tool: ${response.name}`);
      console.log(`Arguments: ${JSON.stringify(response.arguments)}`);
      break;

    case "tool_result":
      // TypeScript knows: call_id, result exist
      console.log(`Tool ${response.call_id} returned: ${response.result}`);
      break;

    default:
      const _exhaustive: never = response;
      throw new Error(`Unhandled: ${_exhaustive}`);
  }
}
```

**Output:**
```
processResponse({ type: "content", text: "Hello!", finish_reason: "stop" })
// AI said: Hello!

processResponse({ type: "tool_call", name: "search", arguments: { q: "TypeScript" }, call_id: "123" })
// Calling tool: search
// Arguments: {"q":"TypeScript"}
```

## Complete Example: Streaming State Machine

Here's a production-ready state machine for AI streaming:

```typescript
// Define all possible states
type StreamState =
  | { status: "idle" }
  | { status: "connecting" }
  | { status: "streaming"; chunks: string[]; tokenCount: number }
  | { status: "paused"; chunks: string[]; tokenCount: number }
  | { status: "complete"; content: string; usage: { prompt: number; completion: number } }
  | { status: "error"; error: Error; retryable: boolean };

// State handler with exhaustive checking
function renderUI(state: StreamState): string {
  switch (state.status) {
    case "idle":
      return "Press Start to begin";

    case "connecting":
      return "Connecting to AI...";

    case "streaming":
      return state.chunks.join("") + " ▊"; // Blinking cursor

    case "paused":
      return state.chunks.join("") + " (paused)";

    case "complete":
      return `${state.content}\n\n---\nTokens: ${state.usage.completion}`;

    case "error":
      const retryHint = state.retryable ? " (click to retry)" : "";
      return `Error: ${state.error.message}${retryHint}`;

    default:
      const _exhaustive: never = state;
      throw new Error(`Unhandled state: ${JSON.stringify(_exhaustive)}`);
  }
}
```

**Output:**
```typescript
renderUI({ status: "idle" })
// "Press Start to begin"

renderUI({ status: "streaming", chunks: ["Hello", " world"], tokenCount: 2 })
// "Hello world ▊"

renderUI({ status: "error", error: new Error("Timeout"), retryable: true })
// "Error: Timeout (click to retry)"
```

### Type Guards for State Transitions

You can also create type guards to check states outside switch statements:

```typescript
// Type guard function
function isStreamingOrPaused(
  state: StreamState
): state is { status: "streaming" | "paused"; chunks: string[]; tokenCount: number } {
  return state.status === "streaming" || state.status === "paused";
}

// Usage
function getCurrentContent(state: StreamState): string | null {
  if (isStreamingOrPaused(state)) {
    // TypeScript knows: chunks exists
    return state.chunks.join("");
  }
  if (state.status === "complete") {
    return state.content;
  }
  return null;
}
```

**Output:**
```typescript
getCurrentContent({ status: "streaming", chunks: ["Test"], tokenCount: 1 })
// "Test"

getCurrentContent({ status: "idle" })
// null
```

## Common Patterns

### Pattern 1: Status + Data

The most common discriminated union pattern for AI:

```typescript
type RequestState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: Error };

// Usage with AI response types
type ChatMessage = { role: string; content: string };
type ChatState = RequestState<ChatMessage[]>;
```

### Pattern 2: Event Types

For streaming event handling:

```typescript
type StreamEvent =
  | { event: "start"; timestamp: number }
  | { event: "delta"; content: string }
  | { event: "tool_start"; name: string }
  | { event: "tool_end"; result: unknown }
  | { event: "end"; usage: { tokens: number } };
```

### Pattern 3: Action Discriminators

For state reducers (useful with React or other UI frameworks):

```typescript
type StreamAction =
  | { type: "START" }
  | { type: "CHUNK"; text: string }
  | { type: "COMPLETE"; usage: { total: number } }
  | { type: "ERROR"; error: Error }
  | { type: "RESET" };
```

## Key Differences from Python

| Aspect | Python | TypeScript |
|--------|--------|------------|
| **Union definition** | `Union[A, B]` or `A \| B` | `A \| B` |
| **Discriminator** | No built-in pattern | Literal type property |
| **Type narrowing** | Manual `isinstance()` | Automatic in `if`/`switch` |
| **Exhaustiveness** | No compile-time check | `never` type pattern |
| **Runtime cost** | `isinstance()` overhead | Zero (types erased) |

Python's type system supports unions but doesn't have built-in exhaustiveness checking. You'd need third-party libraries like `typing_extensions` with `assert_never`. TypeScript makes this a first-class pattern.

## Try With AI

### Prompt 1: Design Your Own State Machine

```
I'm building an AI chat interface. Help me design a discriminated union
for message states. Each message can be:
- sending (user typed it, not yet sent)
- sent (sent to server, awaiting response)
- streaming (AI is responding, partial content)
- complete (full response received)
- failed (something went wrong)

What properties does each state need? Write the type and an
exhaustive handler function.
```

**What you're learning:** How to identify the distinct states in your application and model them with appropriate properties per state. The AI helps you think through what data each state actually needs.

### Prompt 2: Add States to Existing Union

```
I have this streaming state type:

type StreamState =
  | { status: "idle" }
  | { status: "streaming"; content: string }
  | { status: "complete"; content: string };

I need to add:
1. A "rate_limited" state with retry_after seconds
2. A "cancelled" state (user stopped generation)

Update my type and show me how the exhaustive switch catches
the new states I need to handle.
```

**What you're learning:** How adding variants to a discriminated union forces you to handle them everywhere—this is exactly the safety net that prevents bugs when requirements change.

### Prompt 3: Nested Discriminated Unions

```
My AI can respond with content OR tool calls. When it's a tool call,
the tool can be "function" (with name/arguments) or "code_interpreter"
(with code/output). Help me model this with nested discriminated unions:

- Content response: has text and finish_reason
- Tool call response: has tool_type discriminator
  - Function tool: has name and arguments
  - Code interpreter: has code and output

Write the types and a handler that processes each case.
```

**What you're learning:** Complex AI responses often have multiple levels of discrimination. Nesting unions keeps each level focused and type-safe.

---

**Safety Note:** When modeling AI states, always include an error state. AI APIs can fail unexpectedly—rate limits, network issues, model errors. Your discriminated union should make it impossible to forget error handling.
