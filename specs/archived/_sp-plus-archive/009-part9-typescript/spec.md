# Feature Specification: Part 9 - TypeScript for Agentic AI Interfaces

**Feature Branch**: `009-part9-typescript`
**Created**: 2026-01-01
**Status**: Complete (2026-01-01)
**Input**: Part 9: TypeScript — The Language of Realtime and Interaction

## Executive Summary

Part 9 teaches TypeScript as the language for building user-facing AI experiences. Students who've mastered Python backends (Part 5), agentic architectures (Part 6), and cloud-native infrastructure (Part 7) now learn the frontend layer that connects humans to AI systems.

**Scope**: 6 chapters, 37 lessons, ~13.5 hours of content

---

## Assumed Knowledge

**What students know BEFORE Part 9**:
- Python programming fundamentals (Part 5)
- Async/await concepts from Python's asyncio
- Type hints and their purpose (Python Part 5)
- AI agent patterns: tools, streaming, conversation (Part 6)
- FastAPI backend development (Part 6)
- Docker and Kubernetes deployment (Part 7)
- MCP fundamentals and server building (Part 6)
- YAML syntax (throughout book)
- Command-line proficiency (Chapter 7)

**What this part must explain from scratch**:
- JavaScript/TypeScript syntax differences from Python
- TypeScript type system (more expressive than Python's)
- npm/pnpm/bun package management
- Node.js, Deno, Bun runtime differences
- Browser vs server JavaScript contexts
- ES Modules vs CommonJS
- Promises and the event loop
- SSE and WebSocket protocols
- SDK architecture patterns
- CLI tool development

---

## Part Overview

**Proficiency Progression**: A2 → B1 → B2

| Chapter | Proficiency | Focus |
|---------|-------------|-------|
| 73 | A2 (Elementary) | Language fundamentals, type system basics |
| 74 | A2-B1 | Async patterns, streaming fundamentals |
| 75 | B1 (Intermediate) | Runtime environments, HTTP communication |
| 76 | B1-B2 | SDK architecture, type-safe API clients |
| 77 | B1 | Testing patterns for AI applications |
| 78 | B2 (Upper-Int) | CLI tools, developer experience, packaging |

**Teaching Progression**: 4-Layer Method throughout
- All chapters use Layer 1 (Manual Foundation) for core concepts
- All chapters include Layer 2 (AI Collaboration) via "Try With AI" sections
- Capstone projects use Layer 4 (Spec-Driven) approach
- Select chapters include Layer 3 (Intelligence Design) for creating skills

---

## Chapter Specifications

### Chapter 73: TypeScript Fundamentals for AI Engineers

**Position**: Part 9, Chapter 73
**Proficiency**: A2 (Elementary)
**Duration**: ~2.5 hours (7 lessons)

**Thread**: Students translate their Python knowledge to TypeScript, building a type-safe library for AI response structures.

**Lesson Breakdown**:

| # | Title | Duration | Key Concepts |
|---|-------|----------|--------------|
| 1 | From Python to TypeScript | 20 min | Variable declarations, functions, control flow, type annotations syntax |
| 2 | The Type System Deep Dive | 25 min | Union types, intersection types, literal types, type narrowing |
| 3 | Generics and Utility Types | 25 min | Generic functions, constraints, Partial, Required, Pick, Omit |
| 4 | Discriminated Unions for AI States | 20 min | Tagged unions, exhaustive switching, AI response state modeling |
| 5 | Type Guards and Type Assertions | 20 min | typeof, instanceof, custom type predicates, as keyword |
| 6 | Modern Tooling: tsconfig and Bundlers | 25 min | tsconfig.json, target/module settings, esbuild, Vite |
| 7 | Package Management and Monorepos | 20 min | pnpm workspaces, lockfiles, dependency resolution |

**Capstone**: AI Response Type Library - Type definitions for ChatGPT/Claude API responses with discriminated unions for streaming states.

**User Story (P1)**: A Python developer wants to write type-safe TypeScript for AI applications without memorizing syntax from scratch.

**Acceptance Criteria**:
- Student can translate Python function to TypeScript equivalent within 2 minutes
- Student can model AI response with discriminated union (`loading | streaming | complete | error`)
- Student can configure tsconfig.json for Node.js 22+ target

---

### Chapter 74: Async Patterns and Streaming

**Position**: Part 9, Chapter 74
**Proficiency**: A2-B1
**Duration**: ~2.5 hours (7 lessons)

**Thread**: Students implement streaming patterns essential for real-time AI interfaces, culminating in a streaming CLI client.

**Lesson Breakdown**:

| # | Title | Duration | Key Concepts |
|---|-------|----------|--------------|
| 1 | Promises and async/await | 20 min | Promise anatomy, async functions, await, error propagation |
| 2 | Error Handling for Async Operations | 20 min | try/catch, Promise.catch, unhandled rejections, partial failures |
| 3 | AbortController and Timeouts | 25 min | Signal propagation, fetch cancellation, timeout patterns |
| 4 | Server-Sent Events Deep Dive | 30 min | SSE protocol, EventSource, parsing streams, reconnection |
| 5 | Streamable HTTP: The MCP Standard | 25 min | POST-based streaming, session management, Mcp-Session-Id |
| 6 | Retry Logic and Circuit Breakers | 25 min | Exponential backoff, jitter, circuit breaker pattern |
| 7 | Concurrent Requests and Rate Limiting | 20 min | Promise.all, Promise.allSettled, concurrency limits |

**Capstone**: Streaming AI CLI - Command-line tool that streams AI responses with Ctrl+C cancellation.

**User Story (P1)**: A developer wants to build AI interfaces that stream responses token-by-token with proper cancellation support.

**Acceptance Criteria**:
- Student can implement SSE client that parses OpenAI-format streaming responses
- Student can implement Streamable HTTP client for MCP servers
- Student can cancel in-flight requests with AbortController
- Student can implement retry with exponential backoff

**Critical Update**: Lesson 5 must cover MCP Streamable HTTP (SDK 1.10.0+) which replaces deprecated SSE for MCP transport.

---

### Chapter 75: Runtime Environments and HTTP Communication (NEW)

**Position**: Part 9, Chapter 75
**Proficiency**: B1 (Intermediate)
**Duration**: ~2 hours (6 lessons)

**Thread**: Students understand where TypeScript runs and build HTTP servers/clients that work across environments.

**Lesson Breakdown**:

| # | Title | Duration | Key Concepts |
|---|-------|----------|--------------|
| 1 | Node.js 22+: The Server-Side Standard | 25 min | Native TS (--experimental-strip-types), ES2024, async local storage |
| 2 | Deno 2: Security-First Runtime | 20 min | Permission model, npm compatibility, first-class TypeScript |
| 3 | Bun: Performance-Optimized Runtime | 20 min | JavaScriptCore engine, built-in bundler, native TypeScript |
| 4 | Edge Functions: Low-Latency AI | 20 min | Cloudflare Workers, Vercel Edge, Deno Deploy, limitations |
| 5 | HTTP Client Patterns | 20 min | fetch API, Request/Response, headers, cross-runtime compatibility |
| 6 | Building HTTP Servers | 20 min | Fastify, Hono (edge), ElysiaJS (Bun), streaming responses |

**Capstone**: Cross-Runtime HTTP Client - A fetch wrapper that works in Node, Deno, Bun, and browsers with consistent API.

**User Story (P1)**: A developer needs to understand runtime options and build code that works across Node.js, Deno, Bun, and edge functions.

**Acceptance Criteria**:
- Student can run same TypeScript code on Node.js 22, Deno 2, and Bun
- Student can identify which runtime to use for specific use cases
- Student can build HTTP server that streams AI responses

---

### Chapter 76: Building Type-Safe AI SDKs (NEW)

**Position**: Part 9, Chapter 76
**Proficiency**: B1-B2
**Duration**: ~2.5 hours (6 lessons)

**Thread**: Students build a type-safe SDK for their FastAPI AI backend from Part 7, learning patterns used by OpenAI, Anthropic, and Vercel.

**Lesson Breakdown**:

| # | Title | Duration | Key Concepts |
|---|-------|----------|--------------|
| 1 | SDK Architecture Patterns | 25 min | Centralized HTTP, abstraction layers, unknown vs any, cross-runtime |
| 2 | Zod for Schema Validation | 25 min | Runtime validation, type inference, safeParse, transforms |
| 3 | OpenAI/Anthropic SDK Patterns | 25 min | Streaming iterators, tool calls, message accumulation |
| 4 | Vercel AI SDK 5 Integration | 25 min | streamText, generateObject, useChat, Agent class |
| 5 | MCP TypeScript SDK | 25 min | Server implementation, Streamable HTTP, session management |
| 6 | tRPC for Internal APIs | 25 min | End-to-end types, procedures, React/Next.js integration |

**Capstone**: FastAPI Agent SDK - Type-safe TypeScript SDK for their Part 7 FastAPI AI backend with Zod validation.

**User Story (P1)**: A developer needs to build a type-safe SDK wrapper around an AI API with runtime validation.

**Acceptance Criteria**:
- Student can build SDK with Zod schema validation for API responses
- Student can implement streaming with async iterators
- Student can integrate with Vercel AI SDK for chat UIs
- Student can use tRPC for full-stack type safety

---

### Chapter 77: Testing TypeScript for AI Applications (NEW)

**Position**: Part 9, Chapter 77
**Proficiency**: B1 (Intermediate)
**Duration**: ~2 hours (6 lessons)

**Thread**: Students learn to test AI applications with mocked responses, streaming tests, and contract validation.

**Lesson Breakdown**:

| # | Title | Duration | Key Concepts |
|---|-------|----------|--------------|
| 1 | Vitest Fundamentals | 20 min | Modern test runner, TypeScript-native, watch mode, coverage |
| 2 | Mocking AI APIs | 25 min | vi.mock, vi.fn, mockResolvedValue, vi.mocked for types |
| 3 | Testing Streaming Responses | 25 min | Mock SSE/Streamable HTTP, async generator tests, cancellation |
| 4 | Contract Testing | 20 min | Zod as contracts, frontend-backend compatibility, schema evolution |
| 5 | Integration Testing Patterns | 20 min | Real API tests, recorded fixtures, deterministic seeds, cost management |
| 6 | Type-Driven Development | 15 min | Compiler as test, @ts-expect-error, type narrowing verification |

**Capstone**: SDK Test Suite - Comprehensive tests for the Chapter 76 SDK with mocked AI responses and streaming tests.

**User Story (P2)**: A developer needs to test AI applications reliably without making expensive API calls.

**Acceptance Criteria**:
- Student can mock OpenAI API responses with Vitest
- Student can test streaming responses with async generators
- Student can implement contract tests using Zod schemas
- Test suite runs in <5 seconds with no real API calls

---

### Chapter 78: CLI Tools and Developer Experience (NEW)

**Position**: Part 9, Chapter 78
**Proficiency**: B2 (Upper-Intermediate)
**Duration**: ~2 hours (5 lessons)

**Thread**: Students build a publishable CLI tool that connects to their AI backend with streaming, history, and professional UX.

**Lesson Breakdown**:

| # | Title | Duration | Key Concepts |
|---|-------|----------|--------------|
| 1 | CLI Foundations with Commander.js | 25 min | Commands, options, arguments, help generation, subcommands |
| 2 | Interactive CLI Features | 25 min | Streaming output, ora spinners, chalk colors, progress bars |
| 3 | tsx for Development | 20 min | Zero-config execution, shebang scripts, watch mode, npm link |
| 4 | Building an AI Chat CLI | 30 min | Full implementation: streaming, history, tool calls, Ctrl+C |
| 5 | Packaging and Distribution | 20 min | npm publish, binary with pkg, cross-platform, Homebrew |

**Capstone**: Published AI CLI Tool - npm-publishable CLI that connects to their FastAPI backend with streaming and conversation history.

**User Story (P2)**: A developer wants to build and publish a professional CLI tool for AI interactions.

**Acceptance Criteria**:
- CLI streams AI responses token-by-token to terminal
- CLI supports conversation history within session
- CLI handles Ctrl+C gracefully with AbortController
- CLI is packaged and ready for npm publish

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can write TypeScript with 80% proficiency after Chapter 73 (validated by quiz)
- **SC-002**: Students can implement streaming AI client within 30 minutes after Chapter 74
- **SC-003**: Students can identify correct runtime for a use case after Chapter 75
- **SC-004**: Students can build type-safe SDK with Zod in 1 hour after Chapter 76
- **SC-005**: Students can achieve 90%+ test coverage on AI code after Chapter 77
- **SC-006**: Students have npm-publishable CLI after Chapter 78

### Quality Gates

- **QG-001**: All code examples compile with TypeScript 5.5+ strict mode
- **QG-002**: All code examples run on Node.js 22+, Deno 2, and Bun 1.x where applicable
- **QG-003**: Framework invisibility maintained (no meta-commentary on pedagogy)
- **QG-004**: All "Try With AI" sections use action prompts, not reflection prompts
- **QG-005**: Constitutional compliance validated for all lessons
- **QG-006**: All lessons have YAML frontmatter with skills, learning objectives, cognitive load

---

## Key Technologies

### Runtimes (2026 versions)
| Runtime | Version | Key Feature |
|---------|---------|-------------|
| Node.js | 22+ | Native TypeScript (--experimental-strip-types) |
| Deno | 2.x | npm compatibility, security-first |
| Bun | 1.x | 3-4x faster, built-in tools |

### TypeScript
| Version | Key Features |
|---------|--------------|
| 5.5 | Inferred type predicates |
| 5.6 | Region-prioritized diagnostics (3x faster LSP) |
| 5.7 | ES2024 target support |
| 5.8+ | Compile caching |

### AI SDKs
| SDK | Purpose |
|-----|---------|
| Vercel AI SDK 5 | Chat UI integration, streaming |
| OpenAI SDK | Official API client |
| Anthropic SDK | Claude API client |
| MCP TypeScript SDK | Streamable HTTP, tools/resources |

### Testing/Tooling
| Tool | Purpose |
|------|---------|
| Vitest | Modern test runner |
| Zod | Schema validation |
| tRPC | End-to-end type safety |
| Commander.js | CLI framework |
| tsx | TypeScript execution |

---

## Dependencies

### Internal Dependencies
- **Part 5**: Python fundamentals (programming concepts transfer)
- **Part 6**: FastAPI backend (SDK will wrap this)
- **Part 7**: Docker/K8s (deployment context)
- **Chapter 38**: MCP servers (TypeScript SDK chapter builds on this)

### External Dependencies
- Node.js 22+ (with native TypeScript support)
- npm/pnpm/bun package manager
- OpenAI or Anthropic API key (for live testing in capstones)

---

## Out of Scope

- React/Next.js frontend development (Part 10)
- React hooks and component patterns (Part 10)
- WebSocket implementation details (Part 10 covers realtime)
- Full-stack frameworks (Next.js, Remix) (Part 10)
- GraphQL (not essential for AI backends)
- Database access from TypeScript (Prisma, Drizzle) - separate topic
- Mobile development (React Native)
- Desktop apps (Electron, Tauri)

---

## ADR Log

### ADR-001: 6 Chapters vs 2 Chapters

**Decision**: Expand Part 9 from 2 chapters (16 lessons) to 6 chapters (37 lessons).

**Context**: Initial structure only covered TypeScript fundamentals and async patterns. Research showed critical gaps in runtime environments, SDK building, testing, and CLI development.

**Rationale**:
- TypeScript ecosystem in 2026 requires understanding Node.js 22+, Deno 2, Bun, and edge functions
- AI SDK patterns (Vercel AI SDK, MCP SDK) require dedicated coverage
- Testing AI applications has unique patterns (mocking streaming, contract testing)
- CLI tools are essential for AI developer experience
- Students need to build publishable assets, not just learn syntax

**Consequences**:
- Part 9 duration increases from ~4 hours to ~13.5 hours
- Requires 4 new chapter READMEs
- Stronger foundation for Part 10 React/Next.js work

### ADR-002: MCP Streamable HTTP vs SSE

**Decision**: Teach MCP Streamable HTTP as the primary MCP transport, with SSE as legacy context.

**Context**: MCP SDK 1.10.0+ deprecated SSE in favor of Streamable HTTP (POST-based bidirectional streaming).

**Rationale**:
- Streamable HTTP is the current MCP standard (2025+)
- SSE is still used by OpenAI/Anthropic APIs, so must be covered
- Students need both patterns but should default to Streamable HTTP for new MCP work

**Consequences**:
- Chapter 74 Lesson 5 is "Streamable HTTP: The MCP Standard" instead of generic streaming
- SSE remains in Lesson 4 for OpenAI/Anthropic API compatibility

### ADR-003: Zod as Primary Validation Library

**Decision**: Use Zod as the primary schema validation library throughout Part 9.

**Context**: Multiple options exist (Zod, TypeBox, Valibot, io-ts).

**Rationale**:
- Zod has largest ecosystem adoption
- MCP TypeScript SDK uses Zod
- Vercel AI SDK uses Zod
- Type inference from schemas is excellent
- `safeParse()` pattern is intuitive for error handling

**Consequences**:
- All schema examples use Zod
- TypeBox mentioned as faster alternative in performance contexts
- Students learn the most widely-used validation library

### ADR-004: Parallelized Content Generation

**Decision**: Generate lessons in parallel using content-implementer subagents with explicit output paths.

**Context**: 37 lessons is substantial work. Sequential generation would be slow and context-inefficient.

**Rationale**:
- Parallel agent execution reduces wall-clock time by ~80%
- Each lesson is independent once chapter README exists
- Explicit absolute paths prevent wrong-directory writes
- Agent completion verification ensures no missing files

**Consequences**:
- All 37 lessons generated in ~2 hours of agent work
- Consistent quality via shared reference lessons
- Validation scores 87-88/100 across all lessons

---

## Implementation Order

1. Update Part 9 README with expanded structure
2. Create/update Chapter 73-78 READMEs
3. Implement Chapter 73 lessons (foundation for all other chapters)
4. Implement Chapter 74 lessons (async patterns needed throughout)
5. Implement Chapter 75 lessons (runtime context for SDK/CLI work)
6. Implement Chapter 76 lessons (SDK patterns before testing)
7. Implement Chapter 77 lessons (testing the SDK)
8. Implement Chapter 78 lessons (CLI capstone)
9. Run educational-validator on all content
10. Run factual-verifier on technical claims
