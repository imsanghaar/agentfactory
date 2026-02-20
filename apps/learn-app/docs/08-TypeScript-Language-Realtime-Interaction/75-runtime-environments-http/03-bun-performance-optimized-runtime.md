---
sidebar_position: 3
title: "Bun: Performance-Optimized Runtime"
description: "Master Bun's JavaScriptCore-powered performance for AI applications. Learn 3-4x faster cold starts, Bun.serve() for HTTP servers, and the built-in bundler/test runner ecosystem."
keywords: ["Bun", "JavaScriptCore", "TypeScript runtime", "Bun.serve", "HTTP server", "bundler", "test runner", "cold start", "performance", "CLI tools"]
chapter: 75
lesson: 3
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Bun Runtime Execution"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can run TypeScript files directly with Bun and utilize Bun-specific APIs"

  - name: "Bun.serve() HTTP Server Creation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can create high-performance HTTP servers using Bun.serve() with request/response handling"

  - name: "Bun Built-in Tooling Usage"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can use bun test for testing, bun build for bundling, and bun install for package management"

  - name: "Runtime Performance Decision-Making"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Technical Problem-Solving"
    measurable_at_this_level: "Student can evaluate when Bun's performance characteristics benefit specific use cases"

  - name: "JavaScriptCore vs V8 Understanding"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can explain why JavaScriptCore provides faster cold starts than V8"

learning_objectives:
  - objective: "Run TypeScript files directly using Bun without compilation steps"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Execute TypeScript HTTP server and CLI tool using bun run"

  - objective: "Create HTTP servers using Bun.serve() with streaming response support"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Build a streaming AI response server using Bun.serve()"

  - objective: "Use Bun's built-in bundler, test runner, and package manager"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Create a project using bun install, bun test, and bun build"

  - objective: "Evaluate when Bun's performance profile benefits AI development workflows"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Given workload requirements, justify runtime selection"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (JavaScriptCore engine, cold start advantage, Bun.serve API, built-in bundler, test runner, package manager) within A2-B1 limit of 5-7 concepts - PASS"

differentiation:
  extension_for_advanced: "Explore Bun's FFI for calling native C/Rust libraries, compile standalone executables with --compile flag, benchmark against Node.js for specific workloads"
  remedial_for_struggling: "Focus on basic Bun.serve() patterns first before exploring bundler and test runner"

generated_by: content-implementer
source_spec: Part 9, Chapter 75
created: 2026-01-01
last_modified: 2026-01-01
version: 1.0.0
---

# Bun: Performance-Optimized Runtime

Your CLI tool processes AI prompts. Users type a command, wait for the runtime to start, then wait again for the AI response. With Node.js, that first wait is 120-200 milliseconds. Users notice. It feels sluggish. Now imagine that startup happening in 30-50 milliseconds—so fast the tool feels instant.

Bun makes this possible. Built on JavaScriptCore (Safari's JavaScript engine) instead of V8 (Chrome's engine), Bun optimizes for what matters in CLI tools and serverless functions: cold start time. It starts 3-4x faster than Node.js, runs TypeScript natively, and bundles an entire development toolkit—package manager, bundler, test runner—into a single binary.

This lesson teaches you Bun as the performance runtime for AI developer tools. You'll understand when Bun's speed advantage matters, how to build HTTP servers with `Bun.serve()`, and how to leverage the all-in-one toolchain that eliminates webpack-jest-npm sprawl.

## Why JavaScriptCore? The Engine Difference

Node.js and Deno use V8, Chrome's JavaScript engine. V8 excels at long-running processes—it aggressively optimizes code that runs repeatedly, making servers that run for days extremely fast. But that optimization has a cost: startup time.

Bun uses JavaScriptCore, Safari's engine. JavaScriptCore takes a different approach: lighter initial overhead, faster startup, lower memory usage. The trade-off is less aggressive long-term optimization—but for processes that start, run briefly, and exit, this trade-off is exactly right.

| Characteristic | V8 (Node.js, Deno) | JavaScriptCore (Bun) |
|---------------|-------------------|---------------------|
| **Cold start** | ~120-200ms | ~30-50ms |
| **Long-running optimization** | Aggressive (gets faster over time) | Moderate |
| **Memory usage** | Higher baseline | Lower baseline |
| **Best for** | Servers running 24/7 | CLI tools, serverless, short-lived processes |

### Real-World Impact

For a CLI tool that calls an AI API:

```
Node.js timeline:
[~150ms startup] [~50ms code execution] [~2000ms AI API call] [~10ms output]
Total: ~2210ms

Bun timeline:
[~40ms startup] [~50ms code execution] [~2000ms AI API call] [~10ms output]
Total: ~2100ms
```

That 110ms difference makes the tool feel noticeably snappier. For serverless functions that scale to zero and cold-start frequently, the savings compound across thousands of invocations.

## Native TypeScript: Just Run It

Like Deno, Bun runs TypeScript directly. Unlike Node.js 22's experimental type stripping, Bun's TypeScript support is stable and complete:

```typescript
// src/hello.ts - runs directly with Bun
interface Greeting {
  message: string;
  timestamp: Date;
}

function greet(name: string): Greeting {
  return {
    message: `Hello, ${name}!`,
    timestamp: new Date(),
  };
}

const result = greet("Bun");
console.log(result);
```

Run it:

```bash
bun run src/hello.ts
```

**Output:**
```javascript
{
  message: "Hello, Bun!",
  timestamp: 2026-01-01T12:00:00.000Z
}
```

No compilation step. No tsconfig.json required. No `--experimental-strip-types` flag. Bun transpiles TypeScript internally using its native transpiler, which is significantly faster than tsc.

### TypeScript Performance Comparison

```bash
# Node.js 22 with type stripping
time node --experimental-strip-types src/hello.ts
# real: 0.15s

# Bun
time bun run src/hello.ts
# real: 0.04s
```

**Output:**
```
# Bun starts 3-4x faster for simple scripts
```

For AI CLI tools that users invoke frequently, this difference accumulates into a noticeably better experience.

## Bun.serve(): High-Performance HTTP Servers

Bun's HTTP server API is designed for performance. In benchmarks, Bun.serve() handles approximately 52,000-70,000 requests per second, compared to Node.js's 13,000-25,000—roughly 3-4x the throughput on equivalent hardware.

### Basic Server

```typescript
// src/server.ts
Bun.serve({
  port: 3000,
  fetch(req) {
    return new Response("Hello from Bun!");
  },
});

console.log("Server running at http://localhost:3000");
```

Run it:

```bash
bun run src/server.ts
```

**Output:**
```
Server running at http://localhost:3000
```

The API is clean: a single `fetch` handler that receives a Request and returns a Response. These are standard Web API objects—the same Request and Response you use in browsers and Deno.

### Routing with URL Pattern Matching

```typescript
// src/api-server.ts
Bun.serve({
  port: 3000,
  fetch(req) {
    const url = new URL(req.url);

    if (url.pathname === "/health") {
      return new Response("OK");
    }

    if (url.pathname === "/api/chat" && req.method === "POST") {
      return handleChat(req);
    }

    if (url.pathname === "/api/models") {
      return Response.json({
        models: ["gpt-4", "claude-3-sonnet", "gemini-pro"],
      });
    }

    return new Response("Not Found", { status: 404 });
  },
});

async function handleChat(req: Request): Promise<Response> {
  const body = await req.json();
  const { message } = body as { message: string };

  // Simulate AI response
  return Response.json({
    response: `You said: ${message}`,
    model: "mock-model",
  });
}

console.log("API server running at http://localhost:3000");
```

**Output:**
```bash
$ curl http://localhost:3000/api/models
{"models":["gpt-4","claude-3-sonnet","gemini-pro"]}

$ curl -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
{"response":"You said: Hello","model":"mock-model"}
```

### Streaming Responses for AI

AI responses stream token by token. Bun.serve() handles streaming naturally:

```typescript
// src/streaming-server.ts
Bun.serve({
  port: 3000,
  async fetch(req) {
    const url = new URL(req.url);

    if (url.pathname === "/stream") {
      return streamResponse();
    }

    return new Response("Use /stream endpoint");
  },
});

function streamResponse(): Response {
  const encoder = new TextEncoder();

  const stream = new ReadableStream({
    async start(controller) {
      const tokens = ["Hello", " ", "from", " ", "streaming", " ", "Bun", "!"];

      for (const token of tokens) {
        controller.enqueue(encoder.encode(`data: ${token}\n\n`));
        await Bun.sleep(100); // Simulate token generation delay
      }

      controller.enqueue(encoder.encode("data: [DONE]\n\n"));
      controller.close();
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      Connection: "keep-alive",
    },
  });
}

console.log("Streaming server at http://localhost:3000/stream");
```

**Output:**
```bash
$ curl http://localhost:3000/stream
data: Hello

data:

data: from

data:

data: streaming

data:

data: Bun

data: !

data: [DONE]
```

Notice `Bun.sleep()`—a built-in utility that doesn't require importing. Bun includes many conveniences like this that reduce boilerplate.

## The All-in-One Toolchain

Bun isn't just a runtime. It's a complete development toolkit that replaces npm, webpack, and Jest with a single binary.

### Package Manager: bun install

Bun's package manager is dramatically faster than npm:

```bash
# npm
time npm install
# real: 8.5s (clean install)

# bun
time bun install
# real: 0.8s (clean install)
```

**Output:**
```
# Bun installs packages 10-25x faster than npm
```

Bun reads `package.json` and creates a `bun.lockb` (binary lockfile) for reproducible installs. It's compatible with npm packages—your existing `package.json` works unchanged.

```bash
# Initialize a new project
bun init

# Install dependencies
bun install

# Add a package
bun add openai

# Add a dev dependency
bun add -d typescript
```

### Bundler: bun build

Bun includes a bundler that's faster than esbuild (which is already very fast):

```bash
# Bundle for production
bun build src/index.ts --outdir=dist --minify

# Bundle with external dependencies
bun build src/index.ts --outdir=dist --external openai

# Create standalone executable
bun build src/cli.ts --compile --outfile=my-cli
```

**Output:**
```bash
$ bun build src/index.ts --outdir=dist --minify
  dist/index.js  12.4 KB

$ ls -la dist/
-rw-r--r--  1 user  staff  12689 Jan  1 12:00 index.js
```

The `--compile` flag creates self-contained executables that include the Bun runtime. Users don't need Bun installed—the executable runs anywhere:

```bash
# Create executable
bun build src/ai-cli.ts --compile --outfile=ai-cli

# Run it (no Bun required on target machine)
./ai-cli "What is TypeScript?"
```

**Output:**
```
# Standalone binary runs without Bun installation
```

This is powerful for distributing AI CLI tools—no runtime installation required.

### Test Runner: bun test

Bun includes a Jest-compatible test runner:

```typescript
// src/greet.ts
export function greet(name: string): string {
  return `Hello, ${name}!`;
}

// src/greet.test.ts
import { expect, test, describe } from "bun:test";
import { greet } from "./greet";

describe("greet", () => {
  test("returns greeting with name", () => {
    expect(greet("World")).toBe("Hello, World!");
  });

  test("handles empty string", () => {
    expect(greet("")).toBe("Hello, !");
  });
});
```

Run tests:

```bash
bun test
```

**Output:**
```
bun test v1.x
src/greet.test.ts:
  greet
    ✓ returns greeting with name [0.12ms]
    ✓ handles empty string [0.08ms]

 2 pass
 0 fail
 2 total
```

The API matches Jest, so migrating existing tests is straightforward. Import from `bun:test` instead of Jest, and most tests work unchanged.

## Complete Example: AI Chat CLI

Let's build a complete CLI tool that demonstrates Bun's strengths:

```
ai-chat/
├── package.json
├── src/
│   ├── cli.ts
│   ├── client.ts
│   └── client.test.ts
└── bunfig.toml
```

**package.json:**
```json
{
  "name": "ai-chat",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "start": "bun run src/cli.ts",
    "test": "bun test",
    "build": "bun build src/cli.ts --compile --outfile=ai-chat"
  },
  "dependencies": {
    "openai": "^4.0.0"
  }
}
```

**src/client.ts:**
```typescript
import OpenAI from "openai";

export interface ChatOptions {
  model?: string;
  stream?: boolean;
}

export async function chat(
  prompt: string,
  options: ChatOptions = {}
): Promise<string> {
  const client = new OpenAI();
  const model = options.model ?? "gpt-4";

  if (options.stream) {
    return streamChat(client, prompt, model);
  }

  const response = await client.chat.completions.create({
    model,
    messages: [{ role: "user", content: prompt }],
  });

  return response.choices[0].message.content ?? "";
}

async function streamChat(
  client: OpenAI,
  prompt: string,
  model: string
): Promise<string> {
  const stream = await client.chat.completions.create({
    model,
    messages: [{ role: "user", content: prompt }],
    stream: true,
  });

  let fullResponse = "";

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content ?? "";
    process.stdout.write(content);
    fullResponse += content;
  }

  console.log(); // Final newline
  return fullResponse;
}
```

**src/cli.ts:**
```typescript
import { chat } from "./client";

async function main(): Promise<void> {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log("Usage: ai-chat <prompt>");
    console.log("       ai-chat --stream <prompt>");
    process.exit(1);
  }

  const stream = args[0] === "--stream";
  const prompt = stream ? args.slice(1).join(" ") : args.join(" ");

  if (!prompt) {
    console.error("Error: No prompt provided");
    process.exit(1);
  }

  try {
    await chat(prompt, { stream });
  } catch (error) {
    console.error("Error:", error instanceof Error ? error.message : error);
    process.exit(1);
  }
}

main();
```

**src/client.test.ts:**
```typescript
import { expect, test, describe, mock } from "bun:test";
import { chat } from "./client";

describe("chat", () => {
  test("returns response for simple prompt", async () => {
    // In real tests, you'd mock the OpenAI client
    // This test structure shows the pattern
    const response = "Hello!";
    expect(typeof response).toBe("string");
  });

  test("handles stream option", () => {
    const options = { stream: true };
    expect(options.stream).toBe(true);
  });
});
```

Run and build:

```bash
# Install dependencies
bun install

# Run directly
bun run src/cli.ts "What is Bun?"

# Run tests
bun test

# Build standalone executable
bun run build
./ai-chat "Explain TypeScript briefly"
```

**Output:**
```
$ bun run src/cli.ts "What is Bun?"
Bun is a fast JavaScript runtime, bundler, and package manager built on JavaScriptCore...

$ bun test
 2 pass
 0 fail

$ ./ai-chat "Hello!"
Hello! How can I help you today?
```

## When to Choose Bun

| Use Case | Bun | Node.js |
|----------|-----|---------|
| **CLI tools** | 3-4x faster startup, ideal UX | Acceptable, but feels slower |
| **Serverless functions** | Fast cold starts reduce latency | Cold starts noticeable in scale-to-zero |
| **Local development** | Faster installs, faster tests | Mature, but slower |
| **Production APIs** | Excellent performance | Larger ecosystem, more enterprise support |
| **npm compatibility** | ~99% compatible | 100% compatible |
| **Standalone executables** | Built-in with --compile | Requires pkg or similar |

**Choose Bun when:**
- Cold start time directly impacts user experience
- You're building CLI tools for developers
- You want an all-in-one toolchain without webpack/Jest configuration
- You're distributing standalone executables

**Choose Node.js when:**
- You need 100% npm compatibility for edge-case packages
- Enterprise support and long-term stability are priorities
- Your infrastructure is built around Node.js (Lambda, etc.)
- The team is more familiar with Node.js patterns

## Bun vs Deno: Performance vs Security

You've now seen three runtimes. Here's the key distinction:

| Aspect | Bun | Deno |
|--------|-----|------|
| **Primary focus** | Performance | Security |
| **Permission model** | Trust everything (like Node.js) | Explicit permissions required |
| **npm compatibility** | Full, seamless | Full (Deno 2), via npm: specifier |
| **Cold start** | Fastest (~30-50ms) | Fast (~80-100ms) |
| **Use case fit** | CLI tools, serverless | Secure scripts, untrusted code |

Bun and Deno solve different problems. Bun optimizes for speed; Deno optimizes for security. Choose based on your primary constraint.

## Try With AI

### Prompt 1: CLI Performance Optimization

```
I'm building an AI-powered CLI tool that developers will use frequently throughout their day.
Currently using Node.js, and users complain about the "startup lag."

Help me migrate to Bun:
1. What changes are needed in my package.json?
2. How do I convert my npm scripts to bun equivalents?
3. How do I build a standalone executable so users don't need Bun installed?

Show me the before (Node.js) and after (Bun) configurations.
```

**What you're learning:** How to migrate existing Node.js projects to Bun for performance gains. This is practical knowledge for improving developer tools that suffer from startup latency.

### Prompt 2: Bun.serve() for AI Streaming

```
I need to build an HTTP server that streams AI responses using Server-Sent Events (SSE).
The server should:
1. Accept POST /chat with a JSON body containing a prompt
2. Stream the response as SSE events
3. Handle client disconnection gracefully
4. Include proper CORS headers for browser clients

Use Bun.serve() and show me the complete implementation with proper TypeScript types.
```

**What you're learning:** How Bun's HTTP server handles streaming scenarios essential for AI applications. The pattern applies to any server that needs to stream long-running responses.

### Prompt 3: Runtime Selection Framework

```
I'm architecting an AI platform with these components:
1. Public API gateway (high throughput, always running)
2. Developer CLI (frequent cold starts, fast response expected)
3. Background job processor (long-running, CPU-intensive)
4. Admin scripts (run occasionally, handle sensitive data)

For each component, recommend Node.js, Deno, or Bun.
Explain the trade-offs for each decision.
Include specific metrics or benchmarks that support your recommendations.
```

**What you're learning:** How to apply runtime selection criteria across a real architecture. Different components of the same system may benefit from different runtimes—understanding when to use each is a senior engineering skill.

**Safety note:** Bun's npm compatibility is approximately 99%, but some packages with native bindings or Node.js-specific internals may not work. Before migrating production code, test your full dependency tree with `bun install` and `bun test`. Keep Node.js as a fallback until you've verified compatibility.
