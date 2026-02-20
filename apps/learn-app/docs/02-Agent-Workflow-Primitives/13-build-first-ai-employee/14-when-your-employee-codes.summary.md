---
title: "Summary: When Your Employee Codes"
sidebar_label: "Summary"
sidebar_position: 14.5
---

# Summary: When Your Employee Codes

## Key Concepts

- **The Inversion**: Your Custom Agent (OpenClaw) orchestrates a General Agent (Claude Code) to write real software -- the configured agent commands the coding agent, not the other way around.
- **Delegation, Not Generation**: OpenClaw routes coding tasks to a specialist rather than generating code in chat. Claude Code has filesystem access, runs tests, and iterates autonomously.
- **Self-Building Pattern**: OpenClaw uses Claude Code to modify its own source code, completing the recursive loop where agents improve themselves.

## The Delegation Chain

```
You -> Phone -> Telegram -> OpenClaw Gateway -> coding-agent skill
  -> Claude Code (background PTY) -> code changes -> results
    -> OpenClaw -> Telegram -> Phone -> You
```

## Safety Mechanisms

- **PTY mode** (`pty:true`): Allocates a virtual terminal so interactive coding agents don't stall on missing terminal input.
- **Workdir isolation** (`workdir:~/project`): Restricts the coding agent to one directory -- filesystem-level state isolation.
- **Background mode** (`background:true`): Long tasks run without blocking conversation; returns a session ID for status polling.

## Quick Reference

```
General Agent (Claude Code) -- builds --> Custom Agent (OpenClaw)
Custom Agent (OpenClaw) -- orchestrates --> General Agent (Claude Code)
General Agent -- extends --> Custom Agent (now more capable)
... the loop continues
```
