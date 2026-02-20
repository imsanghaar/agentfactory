---
title: "Summary: NanoClaw and the Agent Factory"
sidebar_label: "Summary"
sidebar_position: 9.5
---

# Summary: NanoClaw and the Agent Factory

## Key Concepts

- **Body + Brain separation** is NanoClaw's core architecture: NanoClaw (Body) provides always-on infrastructure with container isolation (~500 lines core TypeScript), Claude Agent SDK (Brain) provides deep reasoning with Programmatic Tool Calling, and OpenAI Agents SDK (Orchestrator) provides model-agnostic multi-agent routing. Each component upgrades independently.
- **Container isolation** inverts the security default from Lesson 5: OpenClaw's "everything accessible unless restricted" becomes NanoClaw's "nothing accessible unless granted" -- addressing CVE-2026-25253 at the OS level.
- **Agent Skills + MCP** are two open standards creating portable vertical intelligence: Skills encode domain knowledge (how to think), MCP servers encode domain tools (how to act). Both work across Claude Code, Codex, NanoClaw, OpenClaw, Cursor, Copilot, Gemini CLI, and every major platform. The SKILL.md format from Lesson 5 is already the standard.
- **Layer 3 (Intelligence) is the only fully platform-independent layer** in the six-layer reference architecture. Your investment in Skills and MCP servers survives any infrastructure change.
- **Agents building agents**: NanoClaw's "skills over features" philosophy means new capabilities are Claude Code skills, not code contributions. Setup is three steps: `git clone`, `cd nanoclaw`, `claude`. The recursive loop: Claude Code builds NanoClaw, which runs Claude Agent SDK, which uses Claude Code skills to extend itself.
- **Programmatic Tool Calling** keeps sensitive data inside the container boundary -- the Brain generates code that runs locally, and only results (never raw data) return to the LLM, making regulated AI Employees architecturally possible.

## NanoClaw's Seven Body Capabilities

Container isolation, multi-channel presence (WhatsApp + extensible), per-group memory (isolated per conversation), cron scheduling, Agent Swarms (parallel Claude instances in isolated containers), MCP integration, full auditability (~8 min review).

## The Six-Layer Reference Architecture

| Layer | Name             | Purpose                                           | Platform-Independent? |
| ----- | ---------------- | ------------------------------------------------- | --------------------- |
| 6     | Body             | Always-on presence, scheduling, Agent Swarms      | No                    |
| 5     | Orchestration    | Multi-agent routing, handoffs, guardrails, tracing | No                    |
| 4     | Brain            | Deep reasoning, Programmatic Tool Calling         | No                    |
| 3     | **Intelligence** | Portable domain knowledge + executable tools      | **Yes**               |
| 2     | Data             | Persistent state, domain knowledge, vector search | No                    |
| 1     | Security         | Container isolation, sandboxes, audit logging     | No                    |

## Common Mistakes

- Treating NanoClaw as a replacement for OpenClaw -- it is a different architectural approach (container isolation vs shared memory), not a direct upgrade
- Building vertical intelligence tied to a single platform instead of using portable standards (Agent Skills + MCP)
- Overlooking Programmatic Tool Calling as essential for regulated industries -- sending raw patient data or financial records through external LLM APIs violates HIPAA, SOX, and similar regulations
- Thinking NanoClaw concepts are disconnected from Chapter 7 -- every concept (container isolation, Agent Swarms, portable skills, per-group memory) grows directly from patterns learned in Lessons 1-8
- Treating the six-layer architecture as all-or-nothing -- start with the layers you need and add complexity as requirements demand
