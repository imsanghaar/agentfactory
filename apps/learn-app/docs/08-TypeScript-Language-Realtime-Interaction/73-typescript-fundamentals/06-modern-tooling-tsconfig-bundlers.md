---
sidebar_position: 6
title: "Modern Tooling: tsconfig, Bundlers, ESM"
description: "Configure TypeScript projects with tsconfig.json, understand ES Modules vs CommonJS, and use fast build tools like esbuild and Vite for modern development."
keywords: ["tsconfig.json", "TypeScript configuration", "ESM", "CommonJS", "esbuild", "Vite", "Node.js TypeScript", "bundlers"]
chapter: 73
lesson: 6
duration_minutes: 25

# HIDDEN SKILLS METADATA
skills:
  - name: "TypeScript Project Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Technical Problem-Solving"
    measurable_at_this_level: "Student can create a tsconfig.json with correct target, module, and strict settings"

  - name: "Module System Selection"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can explain when to use ESM vs CommonJS and configure appropriately"

  - name: "Build Tool Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Technical Problem-Solving"
    measurable_at_this_level: "Student can set up esbuild for fast TypeScript compilation"

  - name: "Development Environment Setup"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can run TypeScript directly with Node.js 22+ or configure Vite for browser projects"

learning_objectives:
  - objective: "Configure tsconfig.json with essential options for Node.js projects"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates working tsconfig.json that compiles TypeScript without errors"

  - objective: "Explain the difference between ESM and CommonJS module systems"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student correctly identifies import/export syntax and explains why ESM is preferred"

  - objective: "Use esbuild for fast TypeScript compilation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student compiles TypeScript to JavaScript using esbuild command"

  - objective: "Run TypeScript directly in Node.js 22+ without compilation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student executes .ts file using node --experimental-strip-types"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (tsconfig.json structure, target/module options, strict mode, ESM syntax, CommonJS syntax, esbuild, Vite basics) at A2 limit - manageable with scaffolding"

differentiation:
  extension_for_advanced: "Explore path aliases, project references for monorepos, and custom transformer plugins"
  remedial_for_struggling: "Focus on tsconfig.json and one build tool (esbuild). Skip Vite until comfortable with basic compilation"

generated_by: content-implementer
created: 2026-01-01
last_modified: 2026-01-01
version: 1.0.0
---

# Modern Tooling: tsconfig, Bundlers, ESM

You've written TypeScript code. Now you need to ship it. Unlike Python where you run `.py` files directly, TypeScript requires configuration decisions: Which JavaScript version should it compile to? Should files use modern ES Modules or legacy CommonJS? How do you compile fast enough that development doesn't become painful?

These questions matter because the TypeScript ecosystem evolved rapidly. Projects from 2020 use different patterns than projects started in 2025. When you inherit code or follow tutorials, you'll encounter conflicting configurations. Understanding the tooling lets you make informed choices instead of copying settings blindly.

This lesson covers the three essential pieces: configuring TypeScript with `tsconfig.json`, choosing between module systems, and using modern build tools that compile 100x faster than the default TypeScript compiler.

## The tsconfig.json File

Every TypeScript project needs a `tsconfig.json` file. It tells the compiler how to process your code. Think of it like Python's `pyproject.toml`—it configures project behavior.

### Creating Your First Configuration

Create a new project directory and initialize TypeScript:

```bash
mkdir ts-project && cd ts-project
npm init -y
npm install typescript --save-dev
npx tsc --init
```

**Output:**
```
Created a new tsconfig.json with:
  target: es2016
  module: commonjs
  strict: true
  esModuleInterop: true
  ...
```

This generates a `tsconfig.json` with many options. Most are commented out. Here's a minimal configuration for modern Node.js projects:

```json
{
  "compilerOptions": {
    "target": "ES2024",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### Understanding Key Options

Each option controls how TypeScript processes your code:

| Option | Purpose | Recommendation |
|--------|---------|----------------|
| `target` | JavaScript version to compile to | `ES2024` for Node.js 22+, `ES2020` for broader support |
| `module` | Module system for output | `NodeNext` for Node.js, `ESNext` for bundlers |
| `moduleResolution` | How imports are resolved | Match your `module` setting |
| `strict` | Enable all strict type checks | Always `true` for new projects |
| `esModuleInterop` | Better CommonJS/ESM interop | Always `true` |
| `skipLibCheck` | Skip type checking in node_modules | `true` for faster compilation |
| `outDir` | Where compiled JavaScript goes | `./dist` is conventional |
| `rootDir` | Where source TypeScript lives | `./src` is conventional |

### The Strict Mode Decision

The `strict` option enables multiple type-checking flags at once:

```json
{
  "compilerOptions": {
    "strict": true
    // This enables:
    // - strictNullChecks: null and undefined are distinct types
    // - strictFunctionTypes: function parameter types are checked
    // - strictBindCallApply: bind, call, apply are type-checked
    // - strictPropertyInitialization: class properties must be initialized
    // - noImplicitAny: variables must have explicit types
    // - noImplicitThis: 'this' must have explicit type
    // - alwaysStrict: emit "use strict" in JavaScript
  }
}
```

**Always enable strict mode for new projects.** It catches bugs at compile time instead of runtime. The errors feel annoying at first, but they prevent real problems.

### Testing Your Configuration

Create a source file to verify the configuration works:

```typescript
// src/index.ts
interface User {
  id: number;
  name: string;
  email: string;
}

function greetUser(user: User): string {
  return `Hello, ${user.name}!`;
}

const user: User = { id: 1, name: "Alice", email: "alice@example.com" };
console.log(greetUser(user));
```

Compile with the TypeScript compiler:

```bash
npx tsc
```

Check the output:

```bash
cat dist/index.js
```

**Output:**
```javascript
"use strict";
function greetUser(user) {
    return `Hello, ${user.name}!`;
}
const user = { id: 1, name: "Alice", email: "alice@example.com" };
console.log(greetUser(user));
```

The types disappear—they're only for compile-time checking. The output is plain JavaScript that Node.js runs directly.

## ES Modules vs CommonJS

JavaScript has two module systems. Understanding both is essential because you'll encounter both in real projects.

### CommonJS (Legacy)

CommonJS was Node.js's original module system. You'll see it in older code:

```javascript
// math.js (CommonJS)
function add(a, b) {
  return a + b;
}

module.exports = { add };
```

```javascript
// app.js (CommonJS)
const { add } = require('./math');
console.log(add(2, 3)); // 5
```

**Characteristics:**
- Uses `require()` and `module.exports`
- Synchronous loading
- Default in Node.js until recently
- File extension: `.js` or `.cjs`

### ES Modules (Modern Standard)

ES Modules (ESM) are the JavaScript standard. Use this for new projects:

```typescript
// math.ts (ESM)
export function add(a: number, b: number): number {
  return a + b;
}
```

```typescript
// app.ts (ESM)
import { add } from './math.js';  // Note: .js extension even for .ts files
console.log(add(2, 3)); // 5
```

**Characteristics:**
- Uses `import` and `export`
- Can be asynchronous (dynamic imports)
- Works in browsers natively
- File extension: `.js`, `.mjs`, or `.ts`

### Why ESM is the Future

| Feature | CommonJS | ESM |
|---------|----------|-----|
| **Browser support** | No (requires bundler) | Yes (native) |
| **Static analysis** | Limited | Excellent (tree-shaking) |
| **Top-level await** | No | Yes |
| **Spec standard** | Node.js specific | JavaScript standard |
| **Future support** | Maintenance mode | Active development |

### Configuring Node.js for ESM

To use ESM in Node.js, add `"type": "module"` to `package.json`:

```json
{
  "name": "ts-project",
  "type": "module",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
  }
}
```

With this setting, Node.js treats `.js` files as ES Modules by default.

## Fast Compilation with esbuild

The TypeScript compiler (`tsc`) is thorough but slow. It type-checks and compiles. For large projects, compilation takes seconds or minutes.

**esbuild** is 100x faster because it only transforms code—it skips type checking. Use `tsc` for type checking, esbuild for building.

### Installing esbuild

```bash
npm install esbuild --save-dev
```

### Compiling a Single File

```bash
npx esbuild src/index.ts --bundle --outfile=dist/index.js --platform=node
```

**Output:**
```
  dist/index.js  142b

⚡ Done in 2ms
```

Compare to `tsc` which typically takes 500ms-2000ms for the same file.

### esbuild Options Explained

| Option | Purpose |
|--------|---------|
| `--bundle` | Include all dependencies in output |
| `--outfile` | Single output file |
| `--outdir` | Output directory (multiple files) |
| `--platform=node` | Target Node.js (vs browser) |
| `--format=esm` | Output ES Modules |
| `--minify` | Compress output for production |
| `--sourcemap` | Generate source maps for debugging |

### Development Workflow

For development, combine both tools:

```json
{
  "scripts": {
    "typecheck": "tsc --noEmit",
    "build": "esbuild src/index.ts --bundle --outfile=dist/index.js --platform=node --format=esm",
    "dev": "esbuild src/index.ts --bundle --outfile=dist/index.js --platform=node --format=esm --watch",
    "start": "node dist/index.js"
  }
}
```

- `typecheck`: Verify types without generating JavaScript
- `build`: Fast compilation for production
- `dev`: Watch mode—rebuilds on file changes (instant)
- `start`: Run the compiled JavaScript

Run type checking separately:

```bash
npm run typecheck && npm run build
```

**Output:**
```
> tsc --noEmit
# (no output means no type errors)

> esbuild src/index.ts --bundle --outfile=dist/index.js --platform=node --format=esm
  dist/index.js  142b
⚡ Done in 3ms
```

## Running TypeScript Directly

Node.js 22+ can run TypeScript files directly without any compilation step. This is experimental but increasingly practical.

### Using --experimental-strip-types

```bash
node --experimental-strip-types src/index.ts
```

**Output:**
```
Hello, Alice!
```

Node.js strips the types at runtime, similar to what esbuild does. You get instant execution without a build step.

### Limitations

Type stripping has constraints:

- **No enums**: Use `const` objects or string unions instead
- **No namespaces**: Use ES Modules
- **No decorators with emitDecoratorMetadata**: Legacy decorator syntax not supported
- **No const enums**: Regular enums also unsupported

For AI engineering work, these limitations rarely matter. The features you need (interfaces, type annotations, generics) all work.

### When to Use Direct Execution

| Use Case | Approach |
|----------|----------|
| **Quick scripts** | `node --experimental-strip-types` |
| **Development** | esbuild with watch mode |
| **Production** | esbuild bundled output |
| **Libraries** | `tsc` for declaration files |

## Vite for Browser Projects

When building browser-based AI interfaces, Vite provides the fastest development experience.

### Setting Up a Vite Project

```bash
npm create vite@latest ai-chat-ui -- --template react-ts
cd ai-chat-ui
npm install
npm run dev
```

**Output:**
```
  VITE v6.x.x  ready in 200 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

Vite features:
- **Instant server start**: No bundling during development
- **Hot Module Replacement**: Changes appear without page refresh
- **TypeScript built-in**: No configuration needed
- **Optimized builds**: esbuild for dependencies, Rollup for production

### Vite Configuration

Vite works out of the box, but you can customize `vite.config.ts`:

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    target: 'es2022',
    sourcemap: true
  },
  server: {
    port: 3000
  }
})
```

For AI chat interfaces that stream responses, Vite's fast refresh makes development feel instantaneous.

## Comparing Python and TypeScript Tooling

Coming from Python, here's how the tools map:

| Python | TypeScript | Purpose |
|--------|------------|---------|
| `pyproject.toml` | `tsconfig.json` | Project configuration |
| `pip` / `uv` | `npm` / `pnpm` | Package management |
| `venv` | `node_modules` | Dependency isolation |
| `python script.py` | `node --experimental-strip-types script.ts` | Direct execution |
| `mypy` | `tsc --noEmit` | Type checking |
| `ruff` / `black` | `prettier` / `eslint` | Formatting and linting |

The concepts transfer directly. The main difference is TypeScript has more compilation options because JavaScript evolved with multiple module systems.

## Common Configuration Patterns

### Node.js Backend (API Server)

```json
{
  "compilerOptions": {
    "target": "ES2024",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### Browser Library (npm Package)

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### React/Vite Frontend

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

Notice that frontend configs often use `"noEmit": true` because Vite handles the actual compilation. TypeScript only provides type checking.

## Troubleshooting Common Issues

**Issue: "Cannot find module" errors**

Your module resolution doesn't match your imports:

```json
{
  "compilerOptions": {
    "moduleResolution": "NodeNext"  // For Node.js 16+
    // OR
    "moduleResolution": "bundler"   // For Vite/webpack
  }
}
```

**Issue: "Relative imports must include file extensions"**

With `"module": "NodeNext"`, you must include extensions:

```typescript
// Wrong
import { add } from './math';

// Correct
import { add } from './math.js';  // .js even for .ts files
```

**Issue: esbuild doesn't catch type errors**

esbuild only transforms code. Run `tsc --noEmit` separately:

```bash
npm run typecheck && npm run build
```

**Issue: Node.js doesn't recognize TypeScript**

Ensure you're using Node.js 22+ and the experimental flag:

```bash
node --version  # Should be v22.x.x or higher
node --experimental-strip-types src/index.ts
```

## Try With AI

### Prompt 1: Configuration Review

```
Review this tsconfig.json for a Node.js 22+ backend project:

{
  "compilerOptions": {
    "target": "ES5",
    "module": "CommonJS",
    "strict": false
  }
}

What should I change for a modern setup? Explain why each change matters.
```

**What you're learning:** How to evaluate TypeScript configurations and understand the reasoning behind each option

### Prompt 2: Build Tool Selection

```
I'm building an AI chat interface that streams responses token-by-token.
Users interact through a React frontend, and I need fast development iteration.

Should I use:
1. tsc alone
2. esbuild
3. Vite
4. Node.js direct execution

Explain which tool fits this use case and why.
```

**What you're learning:** Matching build tools to project requirements based on use case analysis

### Prompt 3: Migration Exercise

```
I have a Python project structure:
- src/
  - main.py
  - utils/
    - helpers.py
- tests/
- pyproject.toml
- requirements.txt

Create an equivalent TypeScript project structure with:
- tsconfig.json
- package.json with scripts
- Appropriate directory layout

Show me the configuration files and explain what each does.
```

**What you're learning:** Translating Python project patterns to TypeScript equivalents, reinforcing the conceptual mapping between ecosystems
