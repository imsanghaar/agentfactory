---
title: "Summary: How Your Employee Works"
sidebar_label: "Summary"
sidebar_position: 4.5
---

# Summary: How Your Employee Works

## Key Concepts

- **Gateway**: Central daemon that routes all messages, manages sessions, authenticates users, loads skills, and coordinates the queue.
- **Channels**: I/O adapters (Telegram, WhatsApp, Discord, 30+) that normalize platform-specific messages into a common format.
- **Sessions**: Isolated per-conversation state stored as append-only JSONL files with auto-compaction for long conversations.
- **Agent Loop**: The 6-phase cycle (ingestion, access control, context assembly, model invocation, tool execution, response delivery) that processes every request.
- **Lane Queue**: FIFO concurrency control serializing runs per-session (1), capping main parallelism (4) and subagent parallelism (8).
- **Memory**: Three layers -- curated MEMORY.md, daily append-only logs, and vector search for semantic recall beyond the context window.
- **Workspace Bootstrap Files**: AGENTS.md (behavior), SOUL.md (identity), USER.md (operator info), IDENTITY.md (persona), HEARTBEAT.md (periodic check-ins), BOOT.md (startup instructions) -- define agent identity before any conversation.
- **Skills**: Portable SKILL.md directories with YAML frontmatter, progressively disclosed (name/description at start, full content on invocation).
- **Heartbeat vs Cron**: Cron runs at fixed times (scheduled tasks). Heartbeat is a periodic pulse where the agent checks standing instructions and decides what needs attention. Cron is a clock; Heartbeat is ambient awareness.

## Universal Pattern Map (4 Frameworks)

| Pattern                   | OpenClaw         | Claude Code          | ChatGPT             | LangGraph         |
| ------------------------- | ---------------- | -------------------- | ------------------- | ----------------- |
| **Orchestration**         | Gateway daemon   | CLI process          | API orchestrator    | StateGraph        |
| **I/O Adapters**          | Channels (30+)   | Terminal/MCP         | Web UI/API          | Input nodes       |
| **State Isolation**       | Sessions (JSONL) | Conversation context | Thread IDs          | State checkpoints |
| **Capability Packaging**  | SKILL.md files   | SKILL.md files       | Custom GPTs/Actions | Tool nodes        |
| **Externalized Memory**   | MEMORY.md + logs | CLAUDE.md + memory   | Memory feature      | State persistence |
| **Concurrency Control**   | Lane queue       | Serialized ops       | Rate limiting       | Node scheduling   |
| **Autonomous Invocation** | Cron + Heartbeat | Cron + hooks         | Scheduled actions   | Trigger nodes     |

## Why These 6?

Remove any single pattern and the system breaks in a specific, predictable way. You could add patterns (logging, authentication, rate limiting), but those are operational concerns, not architectural requirements. These 6 are the minimum set that makes something an AI Employee rather than a chatbot.

## Common Mistakes

- Skipping concurrency control: two parallel runs on the same session corrupt state.
- Loading full skill content upfront instead of using progressive disclosure (wastes tokens).
- Sharing session state across users (breaks state isolation, leaks private data).

## Quick Reference

These 6 patterns appear in every agent framework (OpenClaw, Claude Code, ChatGPT, LangGraph). The names change; the engineering necessities do not. Master them once, recognize them everywhere.
