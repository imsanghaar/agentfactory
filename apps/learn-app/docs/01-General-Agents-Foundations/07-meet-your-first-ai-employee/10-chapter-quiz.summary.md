---
title: "Summary: Chapter Quiz"
sidebar_label: "Summary"
sidebar_position: 11
---

# Summary: Chapter 7 Quiz & What Comes Next

## Key Takeaways

1. An AI Employee is an autonomous system built on 6 universal patterns, not just a smarter chatbot.
2. The implementation details change entirely between frameworks; the patterns are identical.
3. OpenClaw proved demand exists, UX drives adoption, and architecture is engineering not research.
4. Unsolved problems remain: enterprise security, governance, reliability at scale, cost control, founder dependency.
5. Your AI Employee can delegate to Claude Code via tmux (L06) -- but only when you explicitly design the delegation pattern and verify it.
6. Specification-driven design (define what you need before building) is the foundation for building your own AI Employee.

## What Transfers Forward

The 6 patterns from L04 map directly: OpenClaw's Gateway becomes Claude Code's CLI, Telegram channels become MCP servers, JSONL sessions become conversation context, workspace SKILL.md becomes `.claude/skills/`, MEMORY.md + daily logs become CLAUDE.md + Obsidian vault, and Cron + Heartbeat become Cron + git hooks. The explicit delegation pattern from L06 becomes your multi-agent architecture. Google Workspace from L07 becomes MCP servers you configure. See L04 for the full cross-framework comparison across 4 frameworks.

## Quiz Coverage

| Lessons   | Topics                                                                                         | Questions |
| --------- | ---------------------------------------------------------------------------------------------- | --------- |
| L01-L02   | AI Employee definition, OpenClaw growth, setup, free LLMs                                      | 4         |
| L03       | Agent loop phases, autonomous invocation, scheduled tasks                                      | 2         |
| L04       | Architecture, 6 patterns, memory, progressive disclosure, cross-framework mapping              | 7         |
| L05       | ClawHavoc, security checklist, lethal trifecta, Gateway binding, incident response             | 5         |
| L06       | Explicit delegation via tmux, verification over trust, parallel sessions, Agent Factory thesis | 4         |
| L07       | gog CLI, OAuth setup, Google Workspace, least privilege, security audit                        | 7         |
| L08       | Composability, use case evaluation, unsolved problems                                          | 4         |
| L09       | NanoClaw, Body+Brain, portable intelligence, Programmatic Tool Calling                         | 4         |
| L10       | Specification-driven design, forward bridge                                                    | 1         |
| **Total** |                                                                                                | **38**    |
