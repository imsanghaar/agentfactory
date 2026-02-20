---
sidebar_position: 5
title: "Packaging and Distribution"
description: "Package your TypeScript CLI as an npm package and publish it to the world. Master package.json configuration, the bin field, prepublishOnly scripts, npm link testing, and the npm publish workflow."
keywords: ["npm publish", "TypeScript CLI", "package.json bin", "npm link", "prepublishOnly", "CLI distribution", "npm package", "TypeScript packaging", "global npm install", "npx"]
chapter: 78
lesson: 5
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "npm Package Configuration"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can configure package.json with bin field, files array, and scripts for CLI distribution"

  - name: "Local Package Testing"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can use npm link to test CLI installation locally before publishing"

  - name: "npm Publishing Workflow"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can authenticate with npm, configure scoped packages, and publish with appropriate access settings"

  - name: "Build Automation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can configure prepublishOnly and prepare scripts to automate build before publish"

  - name: "CLI Distribution Strategy"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Technical Problem-Solving"
    measurable_at_this_level: "Student can evaluate distribution options (npm, npx, binary) and choose appropriate strategy for target audience"

learning_objectives:
  - objective: "Configure package.json with bin field to create executable CLI commands"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates working package.json where npm link creates a globally accessible command"

  - objective: "Test CLI packages locally using npm link before publishing"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student successfully links and tests their CLI from any directory"

  - objective: "Implement prepublishOnly scripts that build before publish"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student's package automatically compiles TypeScript when npm publish runs"

  - objective: "Publish scoped packages to npm with appropriate access settings"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student successfully publishes a package that can be installed globally with npm install -g"

  - objective: "Analyze distribution strategies and choose appropriate methods for different audiences"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Student can explain tradeoffs between npm publish, npx, and binary distribution"

cognitive_load:
  new_concepts: 6
  assessment: "6 new concepts (bin field, files array, npm link, prepublishOnly, scoped packages, npm publish) within B2 limit of 7-10 concepts - PASS"

differentiation:
  extension_for_advanced: "Explore binary distribution with pkg or deno compile. Create a Homebrew formula for macOS distribution. Implement GitHub Actions for automated npm publishing on release."
  remedial_for_struggling: "Focus on npm link first to understand the bin field. Build intuition for what 'global installation' means before tackling publishing."

generated_by: content-implementer
source_spec: chapter-66-readme
created: 2025-01-01
last_modified: 2025-01-01
version: 1.0.0
---

# Packaging and Distribution

You've built a working AI chat CLI. It runs beautifully on your machine with `tsx src/index.ts`. But that's useless to anyone else. Your colleague can't type `ai-chat "Hello"` and have it work. Your CLI only exists in your development environment.

The gap between "works for me" and "works for everyone" is distribution. This lesson teaches you to cross that gap: package your TypeScript CLI so anyone can install it with a single `npm install -g` command and immediately start using it.

Every tool you use daily went through this journey. When Anthropic built Claude Code, they didn't just write the code; they packaged it so you could run `claude` from any terminal. That's what you'll learn here: the professional workflow for turning TypeScript source into a distributable npm package.

## The Distribution Problem

Your CLI currently exists as TypeScript source files. To run it, you need:

1. Node.js installed
2. The project cloned
3. Dependencies installed with `npm install`
4. Either `tsx` for direct execution or a build step

That's four steps before someone can try your tool. Compare that to:

```bash
npm install -g @yourname/ai-chat
ai-chat "Hello, world!"
```

Two commands. No cloning, no build setup, no TypeScript tooling. This is what distribution enables.

## Package.json: The Distribution Contract

The `package.json` file defines how npm packages, installs, and runs your CLI. Here's a complete configuration:

```json
{
  "name": "@yourname/ai-chat",
  "version": "1.0.0",
  "description": "AI chat CLI with streaming support",
  "type": "module",
  "bin": {
    "ai-chat": "./dist/index.js"
  },
  "files": [
    "dist"
  ],
  "scripts": {
    "build": "tsc",
    "prepublishOnly": "npm run build"
  },
  "engines": {
    "node": ">=18.0.0"
  },
  "keywords": ["cli", "ai", "chat", "typescript"],
  "author": "Your Name <you@example.com>",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/yourname/ai-chat-cli"
  },
  "dependencies": {
    "commander": "^12.0.0",
    "chalk": "^5.3.0",
    "ora": "^8.0.0"
  },
  "devDependencies": {
    "typescript": "^5.4.0",
    "@types/node": "^20.0.0"
  }
}
```

Let's break down the critical fields.

### The bin Field: Creating Commands

The `bin` field maps command names to executable files:

```json
{
  "bin": {
    "ai-chat": "./dist/index.js"
  }
}
```

When someone installs your package globally, npm creates a symlink from `ai-chat` to your script. The user types `ai-chat`, and npm runs `./dist/index.js`.

**Output:**
```bash
# After: npm install -g @yourname/ai-chat
which ai-chat
# /usr/local/bin/ai-chat (symlink to your package)

ai-chat --version
# 1.0.0
```

**Multiple commands**: If your CLI has subcommands as separate entry points:

```json
{
  "bin": {
    "ai-chat": "./dist/index.js",
    "ai-config": "./dist/config.js"
  }
}
```

### The files Field: What Gets Published

The `files` array specifies what npm includes in the published package:

```json
{
  "files": [
    "dist"
  ]
}
```

This is an allowlist. Only the `dist` folder (your compiled JavaScript) gets published. Your TypeScript source, test files, and configuration stay behind.

**Why this matters:**

| Without files field | With files: ["dist"] |
|---------------------|----------------------|
| Publishes everything | Publishes only dist |
| Package size: 2MB | Package size: 50KB |
| Includes src/, test/, .env | Clean, minimal package |
| Exposes internal details | Professional distribution |

**Default exclusions**: npm automatically excludes `node_modules`, `.git`, and files in `.gitignore`. But without `files`, it includes everything else.

### The Shebang: Making Files Executable

Your entry point needs a shebang so the shell knows to run it with Node:

```typescript
#!/usr/bin/env node

import { program } from "commander";
import chalk from "chalk";

program
  .name("ai-chat")
  .description("Chat with AI from your terminal")
  .version("1.0.0");

// ... rest of CLI
```

The `#!/usr/bin/env node` line tells the operating system to find `node` in the PATH and use it to execute this file. Without it, trying to run `ai-chat` directly results in a syntax error.

**Output:**
```bash
# Without shebang:
ai-chat "Hello"
# ./dist/index.js: line 1: import: command not found

# With shebang:
ai-chat "Hello"
# (Works correctly, runs with Node.js)
```

## Local Testing with npm link

Before publishing, test your package as if it were installed globally. The `npm link` command creates a global symlink to your local development version.

```bash
# In your project directory
npm run build
npm link
```

**Output:**
```bash
npm link
# added 1 package in 2s

which ai-chat
# /usr/local/bin/ai-chat -> /usr/local/lib/node_modules/@yourname/ai-chat/dist/index.js

ai-chat --version
# 1.0.0
```

Now you can test from anywhere:

```bash
cd /tmp
ai-chat "Explain what npm link does"
# (Your CLI runs, streaming the response)
```

**The development workflow:**

```bash
# 1. Make changes to src/
vim src/index.ts

# 2. Rebuild
npm run build

# 3. Test immediately (no re-linking needed)
ai-chat "Test my changes"
```

The symlink points to your built files. Rebuilding updates what the command runs.

**Cleaning up:**

```bash
# Remove the global link
npm unlink -g @yourname/ai-chat

# Or from project directory
npm unlink
```

## Build Automation with prepublishOnly

The `prepublishOnly` script runs automatically before `npm publish`. This ensures your package is always built before publishing:

```json
{
  "scripts": {
    "build": "tsc",
    "prepublishOnly": "npm run build"
  }
}
```

**What happens when you publish:**

```bash
npm publish --access public
# > @yourname/ai-chat@1.0.0 prepublishOnly
# > npm run build
#
# > @yourname/ai-chat@1.0.0 build
# > tsc
#
# npm notice Publishing to https://registry.npmjs.org/
# + @yourname/ai-chat@1.0.0
```

**Output:**
```
npm notice 📦  @yourname/ai-chat@1.0.0
npm notice === Tarball Contents ===
npm notice 1.2kB  dist/index.js
npm notice 856B   dist/commands/chat.js
npm notice 423B   dist/lib/streaming.js
npm notice 2.1kB  package.json
npm notice === Tarball Details ===
npm notice name:          @yourname/ai-chat
npm notice version:       1.0.0
npm notice filename:      yourname-ai-chat-1.0.0.tgz
npm notice package size:  1.8 kB
npm notice unpacked size: 4.6 kB
npm notice total files:   4
```

**Alternative: prepare script**

The `prepare` script runs on both `npm install` (for local development) and before `npm publish`:

```json
{
  "scripts": {
    "build": "tsc",
    "prepare": "npm run build"
  }
}
```

Use `prepare` if you want `npm install` to automatically build. Use `prepublishOnly` if you only want builds before publishing.

## Publishing to npm

### Step 1: Create an npm Account

If you don't have an npm account:

```bash
npm adduser
```

Follow the prompts. For existing accounts:

```bash
npm login
```

**Output:**
```bash
npm login
# npm WARN adduser `adduser` will be replaced by `login` in a future version
# Login at:
# https://www.npmjs.com/login?next=/login/cli/abc123
# Press ENTER to open in the browser...
```

### Step 2: Choose a Package Name

Scoped packages (`@yourname/package`) are easier to get unique names for:

```json
{
  "name": "@yourname/ai-chat"
}
```

**Naming rules:**

| Rule | Example |
|------|---------|
| Lowercase only | `ai-chat` not `AI-Chat` |
| No spaces | `ai-chat` not `ai chat` |
| URL-safe characters | Letters, numbers, hyphens, underscores |
| Max 214 characters | Keep it short |

Check if a name is available:

```bash
npm view @yourname/ai-chat
# npm ERR! 404 Not Found

# Name is available!
```

### Step 3: Publish

For scoped packages, you must specify public access (scoped packages default to private):

```bash
npm publish --access public
```

**Output:**
```bash
npm publish --access public
# npm notice
# npm notice 📦  @yourname/ai-chat@1.0.0
# npm notice === Tarball Contents ===
# npm notice 1.2kB  dist/index.js
# npm notice 2.1kB  package.json
# npm notice === Tarball Details ===
# npm notice name:          @yourname/ai-chat
# npm notice version:       1.0.0
# npm notice package size:  1.8 kB
# npm notice shasum:        abc123...
# npm notice integrity:     sha512-...
# npm notice total files:   2
# npm notice
# + @yourname/ai-chat@1.0.0
```

Your package is now live! Anyone can install it:

```bash
npm install -g @yourname/ai-chat
ai-chat "Hello from the published package!"
```

### Publishing Updates

To publish a new version:

```bash
# Update version (patch: 1.0.0 -> 1.0.1)
npm version patch

# Or minor: 1.0.0 -> 1.1.0
npm version minor

# Or major: 1.0.0 -> 2.0.0
npm version major

# Publish
npm publish --access public
```

**Output:**
```bash
npm version patch
# v1.0.1

npm publish --access public
# + @yourname/ai-chat@1.0.1
```

## Distribution Options Beyond npm

npm publish covers developers who have Node.js installed. For broader distribution:

| Method | Audience | Pros | Cons |
|--------|----------|------|------|
| **npm install -g** | Node.js developers | Familiar, easy updates | Requires Node.js |
| **npx** | Quick users | No install needed | Slower startup, requires Node.js |
| **pkg binary** | Non-developers | Single executable, no dependencies | Larger file, per-platform builds |
| **Homebrew** | macOS developers | Native feel, auto-updates | macOS only, formula maintenance |
| **GitHub Releases** | All platforms | Universal access | Manual downloads |

### npx: Zero-Install Execution

Users can run your CLI without installing:

```bash
npx @yourname/ai-chat "Quick question"
```

**Output:**
```bash
npx @yourname/ai-chat "Hello"
# Need to install the following packages:
#   @yourname/ai-chat@1.0.0
# Ok to proceed? (y) y
#
# Hello! How can I help you today?
```

npx downloads, caches, and runs in one command. Great for one-time use.

### Binary Distribution with pkg

The `pkg` tool bundles Node.js with your code into a single executable:

```bash
npm install -g pkg
pkg dist/index.js --targets node18-macos-x64,node18-linux-x64,node18-win-x64
```

**Output:**
```bash
pkg dist/index.js --targets node18-macos-x64,node18-linux-x64,node18-win-x64
# > pkg@5.8.1
# > Targets:
#   node18-macos-x64
#   node18-linux-x64
#   node18-win-x64
# > Output:
#   index-macos
#   index-linux
#   index-win.exe
```

Users download one file and run it directly. No Node.js required.

## Complete Example: From Source to Published

Here's the full workflow:

```bash
# 1. Project structure
ai-chat-cli/
├── src/
│   └── index.ts
├── dist/           # (generated)
├── package.json
└── tsconfig.json

# 2. package.json
cat package.json
```

```json
{
  "name": "@yourname/ai-chat",
  "version": "1.0.0",
  "description": "AI chat CLI with streaming support",
  "type": "module",
  "bin": {
    "ai-chat": "./dist/index.js"
  },
  "files": [
    "dist"
  ],
  "scripts": {
    "build": "tsc",
    "prepublishOnly": "npm run build"
  },
  "engines": {
    "node": ">=18.0.0"
  },
  "dependencies": {
    "commander": "^12.0.0",
    "chalk": "^5.3.0",
    "ora": "^8.0.0"
  },
  "devDependencies": {
    "typescript": "^5.4.0",
    "@types/node": "^20.0.0"
  }
}
```

```bash
# 3. Entry point with shebang
head -5 src/index.ts
```

```typescript
#!/usr/bin/env node

import { program } from "commander";
// ...
```

```bash
# 4. Build and test locally
npm run build
npm link
ai-chat --version
# 1.0.0

ai-chat "Test"
# (Response streams to terminal)

# 5. Publish
npm login
npm publish --access public
# + @yourname/ai-chat@1.0.0

# 6. Verify
npm unlink -g @yourname/ai-chat
npm install -g @yourname/ai-chat
ai-chat "Hello from npm!"
# (Works!)
```

**Output:**
```
+ @yourname/ai-chat@1.0.0
added 1 package in 2s
```

## Common Mistakes

### Missing shebang

```typescript
// WRONG - no shebang
import { program } from "commander";

// RIGHT - with shebang
#!/usr/bin/env node
import { program } from "commander";
```

### Pointing bin to TypeScript

```json
// WRONG - can't execute .ts directly
{
  "bin": {
    "ai-chat": "./src/index.ts"
  }
}

// RIGHT - point to compiled JavaScript
{
  "bin": {
    "ai-chat": "./dist/index.js"
  }
}
```

### Forgetting files field

```json
// RISKY - publishes everything
{
  "name": "@yourname/ai-chat",
  "bin": { "ai-chat": "./dist/index.js" }
}

// SAFE - publishes only dist
{
  "name": "@yourname/ai-chat",
  "bin": { "ai-chat": "./dist/index.js" },
  "files": ["dist"]
}
```

### Publishing without building

```bash
# WRONG - publishes stale code
npm publish

# RIGHT - prepublishOnly builds automatically
{
  "scripts": {
    "prepublishOnly": "npm run build"
  }
}
npm publish
```

## Try With AI

### Prompt 1: Debug a Failed npm link

```
I'm trying to test my CLI with npm link but it's not working.

Here's my setup:
- package.json has: "bin": { "mycli": "./dist/index.js" }
- I ran npm link and it succeeded
- But when I type "mycli" I get "command not found"

Help me debug this. What are the common causes and how do I fix each one?
```

**What you're learning:** Systematic debugging of distribution issues. Understanding where symlinks are created and why they might fail helps you troubleshoot real packaging problems.

### Prompt 2: Design a Version Strategy

```
I'm publishing my first npm package. I need to understand semantic versioning:

1. When do I bump patch vs minor vs major?
2. What happens if I publish a breaking change as a patch?
3. How do I handle pre-releases (beta, rc versions)?
4. What's the npm version command doing under the hood?

Give me practical examples for a CLI tool.
```

**What you're learning:** Professional versioning practices that communicate change magnitude to users. Getting this right builds trust with your package consumers.

### Prompt 3: Plan Multi-Platform Distribution

```
My AI CLI is popular with developers (npm works fine) but I want to
distribute to non-technical users who don't have Node.js.

Help me plan a distribution strategy:
1. What are my options for creating standalone binaries?
2. How do I handle platform-specific builds (macOS, Windows, Linux)?
3. How do I set up automated releases on GitHub?
4. What's the tradeoff between binary size and convenience?

I want this to be professional, like how Claude Code is distributed.
```

**What you're learning:** Enterprise distribution thinking. Understanding the full spectrum from npm packages to standalone binaries prepares you for production-grade tool delivery.

---

**Safety note:** Before publishing, verify you're not including sensitive data. Check your published package contents with `npm pack --dry-run` before `npm publish`. Never include `.env` files, API keys, or credentials in your package. The `files` field is your defense: explicitly list only what should be public.
