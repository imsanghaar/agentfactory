---
title: "Summary: Your Employee Delegating to Claude Code"
sidebar_label: "Summary"
sidebar_position: 6.5
---

# Summary: Your Employee Delegating to Claude Code

## Key Concepts

- Delegation does not happen automatically -- **you instruct your employee** when and how to delegate
- tmux provides **verifiable infrastructure**: background sessions you can attach to and watch
- The **two-tier delegation pattern**: you manage the employee, the employee manages Claude Code
- **Verification matters**: always check that work actually happened (tmux ls, tmux attach, check output files)
- Context stays with your employee (research, intent, MEMORY.md); coding goes to Claude Code
- You are the **architect of the delegation pattern** -- it exists because you designed it

## The Delegation Chain

```
You (Telegram) → Employee (OpenClaw) → Claude Code (in tmux) → Code/Files
                 ↑ reports status        ↑ you can attach and watch
```

| Layer             | Role        | What They Handle                                         |
| ----------------- | ----------- | -------------------------------------------------------- |
| **You**           | Manager     | High-level instructions, review output                   |
| **Your Employee** | Coordinator | Interprets intent, creates tmux sessions, reports status |
| **Claude Code**   | Coder       | Writes actual code in a verifiable tmux session          |

## Key Commands

| Command               | What It Does                                   |
| --------------------- | ---------------------------------------------- |
| `tmux ls`             | Lists all active tmux sessions                 |
| `tmux attach -t name` | Attaches to a session so you can watch it live |
| `Ctrl+B` then `D`     | Detaches from a session without stopping it    |

## Common Mistakes

- Assuming delegation happens automatically (it does not -- you must instruct it)
- Not verifying with tmux ls (your employee may claim to delegate without doing it)
- Writing vague delegation rules (be explicit: use Claude Code, use tmux, report the session name)
- Skipping verification of output files (always check the working directory)

## What Transfers

| Concept                     | In This Lesson                            | In Any Framework                          |
| --------------------------- | ----------------------------------------- | ----------------------------------------- |
| Explicit delegation         | You told your employee to use Claude Code | Orchestrators are configured, not magic   |
| Verification infrastructure | tmux sessions you can attach to           | Logging, monitoring, audit trails         |
| Context vs capability split | Employee researches, Claude Code codes    | Orchestrator holds state, workers execute |
| Human designs the pattern   | You wrote the delegation rule             | Engineers define agent architectures      |
