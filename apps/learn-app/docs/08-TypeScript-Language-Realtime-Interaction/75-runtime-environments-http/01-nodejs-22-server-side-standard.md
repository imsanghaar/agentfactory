---
sidebar_position: 1
title: "Node.js 22+: The Server-Side Standard"
description: "Master Node.js 22+ as the production runtime for TypeScript—native TypeScript execution, ES2024 features, AsyncLocalStorage patterns, and when to choose Node.js over alternatives."
keywords: ["Node.js 22", "TypeScript", "experimental-strip-types", "ES2024", "AsyncLocalStorage", "Object.groupBy", "Promise.withResolvers", "runtime environments", "server-side JavaScript"]
chapter: 75
lesson: 1
duration_minutes: 25

# HIDDEN SKILLS METADATA
skills:
  - name: "Native TypeScript Execution"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can run TypeScript files directly using node --experimental-strip-types without a separate compilation step"

  - name: "ES2024 Feature Usage"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can use Object.groupBy and Promise.withResolvers in production TypeScript code"

  - name: "AsyncLocalStorage Context Propagation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can implement request context propagation without explicit parameter passing"

  - name: "Runtime Selection Decision-Making"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can justify when Node.js is the appropriate runtime choice versus alternatives"

  - name: "Node.js vs Python Runtime Model Comparison"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can explain the event loop model and contrast it with Python's asyncio"

learning_objectives:
  - objective: "Run TypeScript files directly using Node.js 22+ native TypeScript support"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Execute a TypeScript HTTP server without prior compilation"

  - objective: "Apply ES2024 features (Object.groupBy, Promise.withResolvers) to AI data processing"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Refactor array processing code using Object.groupBy"

  - objective: "Implement AsyncLocalStorage for request context propagation in HTTP servers"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Add request ID tracking to an existing HTTP handler"

  - objective: "Compare Node.js event loop with Python's asyncio to make informed runtime decisions"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Given a workload description, justify which runtime is appropriate"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (native TypeScript, experimental flags, Object.groupBy, Promise.withResolvers, AsyncLocalStorage, event loop, runtime selection criteria) at upper bound of B1 limit (7-10) - PASS with careful scaffolding"

differentiation:
  extension_for_advanced: "Explore --experimental-transform-types for enums/namespaces, implement structured logging with AsyncLocalStorage, benchmark cold start times"
  remedial_for_struggling: "Focus on native TypeScript execution and one ES2024 feature (Object.groupBy) before introducing AsyncLocalStorage patterns"

generated_by: content-implementer
source_spec: Part 9, Chapter 75
created: 2026-01-01
last_modified: 2026-01-01
version: 1.0.0
---

# Node.js 22+: The Server-Side Standard

Your AI agent processes 10,000 chat messages per hour. Each message arrives as JSON, gets classified by type (user prompt, tool call, system message), routed to the appropriate handler, and logged with a request ID that traces the entire processing chain. You could write this in Python, but your frontend team already uses TypeScript, and they want type-safe contracts between the chat UI and the backend.

Node.js 22+ is the answer. It runs TypeScript natively, supports modern ES2024 features like `Object.groupBy` for message classification, and provides `AsyncLocalStorage` for request tracing without threading request IDs through every function. More importantly, it's the runtime your frontend developers already understand.

This lesson teaches you Node.js 22+ as the production standard for server-side TypeScript. You'll learn to run TypeScript without compilation, use features that simplify AI message processing, and understand why Node.js remains the default choice for enterprise TypeScript applications.

## Native TypeScript Execution

Until 2024, running TypeScript meant a compilation step. You wrote `.ts` files, compiled them to `.js` with `tsc`, then ran the JavaScript. Node.js 22.6.0 changed this with the `--experimental-strip-types` flag, and Node.js 23+ makes it even simpler.

### The Old Way (Pre-Node.js 22)

```bash
# Before: compile then run
tsc src/index.ts --outDir dist
node dist/index.js

# Or use ts-node (adds overhead)
npx ts-node src/index.ts
```

**Output:**
```
# Multiple steps, additional dependencies, slower iteration
```

### The New Way (Node.js 22+)

```bash
# After: run TypeScript directly
node --experimental-strip-types src/index.ts
```

**Output:**
```
# Single command, no compilation step, faster development
```

Let's verify this works. Create a TypeScript file:

```typescript
// src/index.ts - runs directly without compilation
import { createServer, IncomingMessage, ServerResponse } from "http";

interface APIResponse {
  message: string;
  timestamp: string;
}

const server = createServer((req: IncomingMessage, res: ServerResponse) => {
  const response: APIResponse = {
    message: "Hello from TypeScript!",
    timestamp: new Date().toISOString(),
  };

  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify(response));
});

server.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});
```

Run it:

```bash
node --experimental-strip-types src/index.ts
```

**Output:**
```
Server running at http://localhost:3000
```

Test with curl:

```bash
curl http://localhost:3000
```

**Output:**
```json
{"message":"Hello from TypeScript!","timestamp":"2026-01-01T12:00:00.000Z"}
```

### How Type Stripping Works

Node.js doesn't compile your TypeScript to JavaScript in the traditional sense. It *strips* type annotations, removing everything TypeScript-specific and running the remaining JavaScript. This is fast because it's a simple text transformation, not full compilation.

```typescript
// What you write:
function greet(name: string): string {
  return `Hello, ${name}!`;
}

// What Node.js sees after stripping:
function greet(name        )         {
  return `Hello, ${name}!`;
}
```

The spaces preserve source maps for debugging. Your line numbers match between TypeScript source and runtime errors.

### Limitations of Type Stripping

Type stripping handles annotation syntax but not TypeScript-only features that require transformation:

| Feature | Works with --experimental-strip-types | Requires --experimental-transform-types |
|---------|--------------------------------------|----------------------------------------|
| Type annotations | Yes | N/A |
| Interfaces | Yes (stripped entirely) | N/A |
| Generics | Yes | N/A |
| Enums | No | Yes |
| Namespaces | No | Yes |
| Parameter properties | No | Yes |

For most AI backend code, type stripping is sufficient. Avoid enums by using union types:

```typescript
// Instead of enum (requires transform)
enum MessageRole { User, Assistant, System }

// Use union type (works with strip)
type MessageRole = "user" | "assistant" | "system";
```

**Output:**
```
# Union types provide the same type safety without requiring transformation
```

### Node.js 23+ Default Behavior

Node.js 23.6.0 and later enable type stripping by default. You can run TypeScript files without any flag:

```bash
# Node.js 23+: no flag needed
node src/index.ts
```

For Node.js 22, continue using the explicit flag to ensure consistent behavior across environments.

## ES2024 Features in Node.js 22+

Node.js 22+ supports ES2024, the JavaScript standard finalized in June 2024. Two features transform how you process AI data: `Object.groupBy` and `Promise.withResolvers`.

### Object.groupBy: Classifying AI Messages

AI chat histories contain mixed message types. Before ES2024, grouping required manual reduce operations:

```typescript
// Before ES2024: manual grouping with reduce
interface ChatMessage {
  type: "content" | "tool_call" | "tool_result";
  text?: string;
  name?: string;
}

const messages: ChatMessage[] = [
  { type: "content", text: "Hello" },
  { type: "tool_call", name: "search" },
  { type: "content", text: "World" },
  { type: "tool_result", text: "Search results..." },
];

// Verbose and error-prone
const grouped = messages.reduce((acc, msg) => {
  const key = msg.type;
  if (!acc[key]) acc[key] = [];
  acc[key].push(msg);
  return acc;
}, {} as Record<string, ChatMessage[]>);

console.log(grouped);
```

**Output:**
```javascript
{
  content: [
    { type: "content", text: "Hello" },
    { type: "content", text: "World" }
  ],
  tool_call: [ { type: "tool_call", name: "search" } ],
  tool_result: [ { type: "tool_result", text: "Search results..." } ]
}
```

With ES2024, this becomes a single line:

```typescript
// ES2024: Object.groupBy
const grouped = Object.groupBy(messages, (msg) => msg.type);

console.log(grouped);
```

**Output:**
```javascript
{
  content: [
    { type: "content", text: "Hello" },
    { type: "content", text: "World" }
  ],
  tool_call: [ { type: "tool_call", name: "search" } ],
  tool_result: [ { type: "tool_result", text: "Search results..." } ]
}
```

Same result, but the intent is clear: group by type. No reduce ceremony, no manual accumulator initialization.

### Real AI Use Case: Processing Model Responses

Claude and GPT-4 return message blocks of different types. `Object.groupBy` makes processing natural:

```typescript
interface ContentBlock {
  type: "text" | "tool_use" | "tool_result";
  text?: string;
  id?: string;
  name?: string;
  input?: Record<string, unknown>;
}

function processResponse(blocks: ContentBlock[]): void {
  const grouped = Object.groupBy(blocks, (block) => block.type);

  // Handle each type appropriately
  const textBlocks = grouped.text ?? [];
  const toolCalls = grouped.tool_use ?? [];
  const toolResults = grouped.tool_result ?? [];

  // Combine all text for display
  const fullText = textBlocks.map((b) => b.text).join("");

  // Log tool usage for analytics
  toolCalls.forEach((tool) => {
    console.log(`Tool called: ${tool.name}`);
  });

  console.log(`Response: ${fullText}`);
  console.log(`Tool calls: ${toolCalls.length}`);
}

// Example usage
const response: ContentBlock[] = [
  { type: "text", text: "Let me search for that. " },
  { type: "tool_use", id: "call_1", name: "web_search", input: { query: "Node.js 22" } },
  { type: "text", text: "Based on the search results..." },
];

processResponse(response);
```

**Output:**
```
Tool called: web_search
Response: Let me search for that. Based on the search results...
Tool calls: 1
```

### Promise.withResolvers: External Promise Control

Traditional Promise creation buries resolve/reject inside the executor:

```typescript
// Traditional Promise: resolve/reject trapped in executor
function waitForEvent(): Promise<string> {
  let resolveFunc: (value: string) => void;

  const promise = new Promise<string>((resolve) => {
    resolveFunc = resolve;
  });

  // resolveFunc available outside, but awkward setup
  setTimeout(() => resolveFunc("event occurred"), 1000);

  return promise;
}
```

**Output:**
```
# Works, but the setup is verbose and resolve is assigned awkwardly
```

`Promise.withResolvers` exposes all three components directly:

```typescript
// ES2024: Promise.withResolvers
function waitForEvent(): Promise<string> {
  const { promise, resolve, reject } = Promise.withResolvers<string>();

  // resolve and reject available immediately
  setTimeout(() => resolve("event occurred"), 1000);

  return promise;
}

// Usage
const result = await waitForEvent();
console.log(result);
```

**Output:**
```
event occurred
```

### Real AI Use Case: Streaming with Cancellation

When streaming AI responses, you need external control over the promise. User clicks "Stop Generating," and you need to reject the stream promise from outside:

```typescript
interface StreamController {
  promise: Promise<string>;
  cancel: () => void;
}

function createCancellableStream(url: string): StreamController {
  const { promise, resolve, reject } = Promise.withResolvers<string>();
  const controller = new AbortController();

  fetch(url, { signal: controller.signal })
    .then((res) => res.text())
    .then(resolve)
    .catch(reject);

  return {
    promise,
    cancel: () => {
      controller.abort();
      reject(new Error("Stream cancelled by user"));
    },
  };
}

// Usage
const stream = createCancellableStream("https://api.example.com/stream");

// Later, user clicks "Stop"
// stream.cancel();

// Or wait for completion
const result = await stream.promise;
console.log(result);
```

**Output:**
```
# Stream result or "Stream cancelled by user" if cancel() was called
```

The pattern separates stream creation from stream control, making the API cleaner for UI integration.

## AsyncLocalStorage: Request Context Without Prop Drilling

Every HTTP request needs a unique ID for logging and tracing. Without special tooling, you pass this ID through every function:

```typescript
// Without AsyncLocalStorage: prop drilling nightmare
function handleRequest(requestId: string, data: unknown): void {
  log(requestId, "Received request");
  processData(requestId, data);
}

function processData(requestId: string, data: unknown): void {
  log(requestId, "Processing data");
  validateData(requestId, data);
  saveData(requestId, data);
}

function validateData(requestId: string, data: unknown): void {
  log(requestId, "Validating");
  // requestId threaded through every call
}
```

Every function signature includes `requestId`. Every call site passes it. This is prop drilling, and it pollutes your entire codebase.

### AsyncLocalStorage Solution

AsyncLocalStorage provides implicit context that flows through async operations without explicit passing:

```typescript
import { AsyncLocalStorage } from "async_hooks";
import { createServer, IncomingMessage, ServerResponse } from "http";
import { randomUUID } from "crypto";

// Create storage instance
const requestContext = new AsyncLocalStorage<{ requestId: string }>();

// Logger that reads context automatically
function log(message: string): void {
  const ctx = requestContext.getStore();
  const requestId = ctx?.requestId ?? "no-context";
  console.log(`[${requestId}] ${message}`);
}

// Functions don't need requestId parameter
function processData(data: unknown): void {
  log("Processing data");
  validateData(data);
  saveData(data);
}

function validateData(data: unknown): void {
  log("Validating");
}

function saveData(data: unknown): void {
  log("Saving");
}

// HTTP server wraps each request in context
const server = createServer((req: IncomingMessage, res: ServerResponse) => {
  const requestId = randomUUID();

  // Run handler inside context
  requestContext.run({ requestId }, () => {
    log("Request received");
    processData({ example: "data" });

    res.writeHead(200);
    res.end("OK");
  });
});

server.listen(3000);
```

**Output:**
```
[550e8400-e29b-41d4-a716-446655440000] Request received
[550e8400-e29b-41d4-a716-446655440000] Processing data
[550e8400-e29b-41d4-a716-446655440000] Validating
[550e8400-e29b-41d4-a716-446655440000] Saving
```

The request ID propagates automatically. `processData`, `validateData`, and `saveData` don't mention request IDs in their signatures, yet every log line includes the correct ID.

### How AsyncLocalStorage Works

`requestContext.run(store, callback)` creates a context "bubble." Any code executed within that callback—including async operations and their callbacks—can access the store via `getStore()`. Different concurrent requests have isolated stores.

```
Request A arrives (ID: abc-123)
  └─> run({ requestId: "abc-123" }, () => { ... })
       └─> log() reads "abc-123"
       └─> await dbQuery()
            └─> log() still reads "abc-123"

Request B arrives (ID: xyz-789)
  └─> run({ requestId: "xyz-789" }, () => { ... })
       └─> log() reads "xyz-789" (isolated from A)
```

### Real AI Use Case: Tracing AI Agent Calls

When your agent makes tool calls, you want every operation traced back to the originating request:

```typescript
interface RequestContext {
  requestId: string;
  userId: string;
  startTime: number;
}

const context = new AsyncLocalStorage<RequestContext>();

async function handleAgentRequest(userId: string, prompt: string): Promise<string> {
  const ctx: RequestContext = {
    requestId: randomUUID(),
    userId,
    startTime: Date.now(),
  };

  return context.run(ctx, async () => {
    log("Starting agent request");

    const response = await callLLM(prompt);

    if (needsToolCall(response)) {
      await executeToolCall(response.toolCall);
    }

    const duration = Date.now() - ctx.startTime;
    log(`Completed in ${duration}ms`);

    return response.text;
  });
}

async function executeToolCall(tool: ToolCall): Promise<void> {
  // Context flows through automatically
  log(`Executing tool: ${tool.name}`);
  // ... tool execution
  log(`Tool completed: ${tool.name}`);
}
```

**Output:**
```
[req-123] Starting agent request
[req-123] Executing tool: web_search
[req-123] Tool completed: web_search
[req-123] Completed in 1523ms
```

## Node.js vs Python: Runtime Models

You know Python's asyncio. How does Node.js compare? Understanding the difference helps you write idiomatic code in each.

### Python's asyncio Model

Python uses explicit async/await with a single-threaded event loop:

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)  # Explicit await
    return "data"

async def main():
    result = await fetch_data()  # Must await
    print(result)

asyncio.run(main())  # Explicit loop start
```

**Key characteristics:**
- Must explicitly mark functions as `async`
- Must explicitly `await` async operations
- Event loop is started explicitly with `asyncio.run()`
- Blocking I/O blocks the entire loop (use `aiohttp`, not `requests`)

### Node.js Event Loop Model

Node.js has a built-in event loop that's always running. All I/O is non-blocking by default:

```typescript
import { readFile } from "fs/promises";

async function fetchData(): Promise<string> {
  await new Promise((r) => setTimeout(r, 1000));
  return "data";
}

async function main(): Promise<void> {
  const result = await fetchData();
  console.log(result);
}

main();  // Event loop already running
```

**Key characteristics:**
- Event loop starts automatically when Node.js runs
- All built-in I/O is non-blocking
- Callbacks, Promises, and async/await all integrate with the same loop
- No need to choose special async libraries—standard `fs`, `http`, etc. are already async

### Comparison Table

| Aspect | Python asyncio | Node.js |
|--------|---------------|---------|
| Event loop start | Explicit (`asyncio.run()`) | Automatic |
| Default I/O | Blocking (need async libs) | Non-blocking |
| CPU-bound work | Blocks loop | Blocks loop (use worker_threads) |
| Concurrency model | Coroutines | Callbacks + Promises + async/await |
| Ecosystem | Growing async libs | Everything async by default |

### When to Choose Node.js

Node.js is the right choice when:

| Scenario | Why Node.js |
|----------|-------------|
| **Production TypeScript APIs** | Largest ecosystem, enterprise support, mature tooling |
| **Frontend team integration** | Same language as browser code, shared types |
| **Streaming responses** | Built-in streaming primitives, SSE support |
| **Real-time applications** | WebSocket handling, low-latency event processing |
| **npm ecosystem access** | 2M+ packages, most AI SDKs publish TypeScript types |

Node.js is *not* the best choice for CPU-intensive work (model inference, heavy computation). Keep that in Python with FastAPI.

## Try With AI

### Prompt 1: ES2024 Refactoring

```
I have this code that processes AI model responses. Each response has a status field (pending, processing, completed, failed). I'm using reduce to group them:

const grouped = responses.reduce((acc, r) => {
  if (!acc[r.status]) acc[r.status] = [];
  acc[r.status].push(r);
  return acc;
}, {});

Refactor this to use ES2024 Object.groupBy.
Then extend it to also group by model (gpt-4, claude-3, etc.)
using a compound key like "status:model".
```

**What you're learning:** How `Object.groupBy` simplifies data classification patterns that appear constantly when processing AI API responses. The compound key extension shows how to create meaningful groupings for analytics dashboards.

### Prompt 2: AsyncLocalStorage Implementation

```
I have a FastAPI-style route handler pattern in Node.js:

app.post("/chat", async (req, res) => {
  const userId = req.headers["x-user-id"];
  const response = await processChat(req.body.message, userId);
  await logAnalytics(userId, response);
  res.json(response);
});

Every function needs userId for logging and analytics.
Convert this to use AsyncLocalStorage so I don't have to pass userId through every function.
Show me how to set up the context and access it in nested functions.
```

**What you're learning:** How to eliminate prop drilling in real HTTP handlers. This pattern applies to any per-request context (user ID, request ID, feature flags, A/B test variants) and is how production frameworks like Express middleware work internally.

### Prompt 3: Runtime Selection Decision

```
I'm building an AI agent system with these components:
1. Chat API endpoint (receives user messages, returns responses)
2. Tool execution (calls external APIs, file system operations)
3. Background job processing (batch analysis of conversations)
4. CLI tool for local development

For each component, help me decide: Node.js, Deno, or Bun?
Consider: cold start time, npm compatibility, security requirements, and production readiness.
Give me specific reasoning for each choice.
```

**What you're learning:** How to apply runtime selection criteria to real architecture decisions. This decision framework prevents choosing runtimes based on hype rather than requirements—a critical skill for technical leadership roles.

**Safety note:** When running TypeScript with `--experimental-strip-types`, test your code with a full `tsc` check before deployment. Type stripping runs code but doesn't validate types—errors you'd catch in compilation can reach production. Use `tsc --noEmit` in your CI pipeline.
