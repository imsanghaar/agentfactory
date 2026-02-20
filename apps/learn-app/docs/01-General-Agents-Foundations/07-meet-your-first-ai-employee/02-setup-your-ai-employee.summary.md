---
title: "Summary: Setup Your AI Employee (Free)"
sidebar_label: "Summary"
sidebar_position: 2.5
---

# Summary: Setup Your AI Employee (Free)

## Key Concepts

- **QuickStart Wizard**: Interactive onboarding that configures your LLM provider, gateway, Telegram channel, and optional skills in one pass
- **Gemini CLI OAuth**: Browser-based Google authentication for LLM access -- no API keys to create or manage
- **Gateway**: Local server (port 18789) that routes messages between channels and the LLM provider, installed as a background service (LaunchAgent on macOS)
- **Localhost Binding**: Gateway defaults to 127.0.0.1 so only your machine can access the admin interface
- **Hatching**: First-contact moment where you personalize your AI Employee through conversation
- **Universal Setup Pattern**: Install runtime, configure intelligence, connect I/O channels, verify end-to-end, secure the boundary

## Key Commands

- `curl -fsSL https://openclaw.ai/install.sh | bash` -- install OpenClaw (setup starts automatically)
- `openclaw tui` -- open the terminal chat interface
- `openclaw pairing approve telegram <CODE>` -- approve a Telegram user's pairing request
- `openclaw gateway start` / `stop` / `status` -- manage the background gateway service
- `openclaw dashboard` -- open the Control UI in your browser
- `cat ~/.openclaw/logs/gateway.log | tail -50` -- review recent gateway logs

## Common Mistakes

- Binding gateway to `0.0.0.0` without authentication (exposes agent to the network)
- Clicking through the security warning without reading it (builds bad habits)
- Sharing bot tokens or gateway tokens publicly (treat both like passwords)
- Skipping the hatching step (personalization makes the agent more useful)

## Quick Reference

| Bind Address           | Who Can Access        | Safe?                |
| ---------------------- | --------------------- | -------------------- |
| `127.0.0.1` (default)  | Only your machine     | Yes                  |
| `0.0.0.0` without auth | Anyone on network     | **Never**            |
| `0.0.0.0` with token   | Anyone with the token | Yes (remote servers) |
