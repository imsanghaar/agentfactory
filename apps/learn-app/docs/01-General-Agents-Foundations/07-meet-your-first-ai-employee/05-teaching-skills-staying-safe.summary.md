---
title: "Summary: Teaching Skills & Staying Safe"
sidebar_label: "Summary"
sidebar_position: 5.5
---

# Summary: Teaching Skills & Staying Safe

## Key Concepts

- **AI-Generated Skills**: Your AI Employee can create SKILL.md files on request -- you shift from writer (Chapter 3) to reviewer
- **Skill Evaluation Checklist**: Activation specificity, instruction clarity, output format, error handling -- the same criteria from Chapter 3, now applied as judgment
- **From Trust to Threat**: You trust skills your employee creates. The same trust breaks when skills come from strangers on ClawHub
- **ClawHavoc**: Coordinated campaign of 335 malicious skills deploying Atomic Stealer (AMOS) via fake prerequisite error messages on ClawHub
- **CVE-2026-25253**: Critical (CVSS 8.8) WebSocket origin bypass enabling one-click remote code execution on OpenClaw instances
- **Lethal Trifecta**: Private data access + untrusted content + external communication in a single process -- the fundamental, unsolvable architectural tension in all agent systems

## Security Checklist

1. **Never bind to 0.0.0.0** -- exposes your agent to the entire internet
2. **Always read skills before installing** -- 12% of ClawHub was malicious
3. **Use Gateway authentication token** -- prevents unauthorized WebSocket connections
4. **Keep OpenClaw updated** -- security patches ship for known vulnerabilities
5. **Enable sandboxing for untrusted skills** -- isolates tool execution from your host
6. **Never store secrets in skill instructions** -- skill text passes through LLM context in plaintext

## Common Mistakes

- Installing community skills without reading every line of the SKILL.md
- Binding to `0.0.0.0` for remote access convenience (135,000+ instances were exposed)
- Trusting marketplace rankings as a proxy for safety (the #1 ranked skill was malware)
- Accepting AI-generated skills without reviewing activation, instructions, output, and error handling
- Skipping iteration after the first test (ambiguous instructions only show up at runtime)

## Quick Reference

| Check        | What to Look For                | Fix If...                             |
| ------------ | ------------------------------- | ------------------------------------- |
| Activation   | `description` field is specific | Too vague or too narrow               |
| Instructions | Step-by-step, actionable        | Vague steps like "research the topic" |
| Output       | Format and location defined     | No output format specified            |
| Errors       | Failure scenarios handled       | No error handling section             |
