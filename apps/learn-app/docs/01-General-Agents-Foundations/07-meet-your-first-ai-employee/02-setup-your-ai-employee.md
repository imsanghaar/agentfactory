---
sidebar_position: 2
title: "Setup Your AI Employee (Free)"
description: "Install OpenClaw, connect a free LLM provider, and chat with your AI Employee through Telegram and the Control UI in under 45 minutes"
keywords:
  [
    openclaw setup,
    telegram bot,
    ai employee installation,
    gemini free tier,
    openrouter free models,
    openclaw gateway,
    botfather telegram,
    ai agent setup,
  ]
chapter: 7
lesson: 2
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "CLI Installation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can install OpenClaw via CLI, run the onboarding wizard, and verify the installation with openclaw --version"

  - name: "Telegram Bot Setup"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can create a Telegram bot via BotFather, configure the bot token, and complete the pairing flow"

  - name: "Gateway Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can configure the OpenClaw gateway with an LLM provider, start the gateway, and access the Control UI"

learning_objectives:
  - objective: "Install OpenClaw and verify the installation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student runs openclaw --version and sees version output"

  - objective: "Create a Telegram bot and complete the pairing flow"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates bot via BotFather, configures token, approves pairing, and receives a response from bot"

  - objective: "Configure the gateway with a free LLM provider and access the Control UI"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student completes onboarding wizard with free provider, opens Control UI at 127.0.0.1:18789, and sends a test message"

  - objective: "Explain why the gateway binds to localhost and the security implications of changing it"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student articulates that 127.0.0.1 limits access to the local machine and that binding to 0.0.0.0 exposes the agent to the internet"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "CLI installation (curl/iwr install scripts)"
    - "Onboarding wizard (interactive configuration)"
    - "Telegram BotFather (bot token creation)"
    - "Gateway configuration (provider + channel settings)"
    - "Security acknowledgment (reading and accepting risk)"
    - "Localhost security (127.0.0.1 vs 0.0.0.0)"
  assessment: "6 concepts with hands-on practice at A2 level, within the 5-7 concept budget for beginners"

differentiation:
  extension_for_advanced: "Deploy OpenClaw to Oracle Cloud Always Free ARM instance for 24/7 operation. Configure SSH tunnel for remote access."
  remedial_for_struggling: "Focus on the Control UI (web browser) first. Skip Telegram setup and interact through the browser. Come back to Telegram once comfortable."

teaching_guide:
  lesson_type: "hands-on"
  session_group: 1
  session_title: "Setting Up Your AI Employee"
  key_points:
    - "The universal setup pattern (install, configure intelligence, connect I/O, verify, secure) applies to every agent framework students will encounter"
    - "Localhost binding (127.0.0.1) vs all-interfaces (0.0.0.0) is the single most important security concept in this lesson — it recurs in Lesson 5 and Chapter 11 deployment"
    - "Three channels (TUI, Telegram, Control UI) sharing one agent demonstrates the channel adapter pattern from Lesson 1"
    - "The onboarding conversation where students name and personalize the agent is not cosmetic — it seeds persistent memory that shapes all future interactions"
  misconceptions:
    - "Students think the Telegram bot IS the AI Employee — clarify that the bot is one channel adapter; the gateway + agent loop is the real system"
    - "Students assume localhost means 'safe from all threats' — it prevents network access but the agent itself can still execute risky actions locally"
    - "Students skip the security acknowledgment as boilerplate — reinforce that this habit of reading security warnings is the lesson within the lesson"
  discussion_prompts:
    - "Why did OpenClaw choose messaging apps (Telegram, WhatsApp) as the default interface instead of building a dedicated mobile app?"
    - "If your gateway accidentally bound to 0.0.0.0 on a public server, what could an attacker do with access to your AI Employee?"
    - "What is the practical difference between configuring a tool and onboarding a colleague — and why does the first conversation matter?"
  teaching_tips:
    - "Have students complete setup live in class — troubleshooting together builds confidence faster than solo debugging at home"
    - "When students hit PATH or Node.js errors, use it as a teaching moment: this is exactly the kind of environment debugging agents help with"
    - "Demo the three-channel pattern live: send same question via TUI, Telegram, and Control UI to show one agent, multiple interfaces"
    - "Spend extra time on the bind address table (127.0.0.1 vs 0.0.0.0) — draw it on a whiteboard with network boundaries"
  assessment_quick_check:
    - "Ask students to explain what 127.0.0.1 means and why it matters for an AI agent"
    - "Have students name the five steps of the universal setup pattern from memory"
    - "Ask: If you close your terminal, does your AI Employee stop working? Why or why not?"
---

# Setup Your AI Employee (Free)

In Lesson 1, you saw why the AI Employee paradigm matters and how OpenClaw validated it at scale. Now you build one yourself. In the next 30-45 minutes, you will have a working AI Employee on your phone -- not a demo, not a simulation, but a real agent that can research, write, analyze, and remember.

Everything in this lesson is free. Google Gemini's free tier gives you enough tokens to complete this entire chapter without spending a dollar. You need a computer with a terminal, a Google account, and a Telegram account. No API keys to create. No credit cards to enter.

**Honest time estimate**: Budget 45 minutes. The happy path takes 15-20 minutes, but Node.js version issues, network hiccups, and shell PATH problems are common first-time obstacles. Troubleshooting is where real learning happens.

:::tip Alternative: OpenRouter
If you prefer not to use Google, OpenRouter ([openrouter.ai](https://openrouter.ai/)) provides free models through a single API key. Select OpenRouter instead of Google when the QuickStart wizard asks for your provider.
:::

---

## Install OpenClaw

OpenClaw installs through a single terminal command. The installer detects your OS, checks prerequisites (Homebrew and Node.js on macOS), and installs the OpenClaw package automatically.

::::os-tabs

::macos

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

::windows

Open PowerShell as Administrator:

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

::linux

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

::::

The installer handles everything: checking for Node.js (installing it if needed), installing the OpenClaw npm package, and creating your configuration directory at `~/.openclaw/`. When it finishes, you see a version confirmation:

```
OpenClaw 2026.2.15 (3fe22ea)
```

**What happens next is important**: the installer transitions directly into the setup wizard. You do not need to run a separate onboarding command. Read what the installer asks you -- do not blindly press Enter.

:::tip npm Alternative
If the install script fails, install directly via npm: `npm install -g openclaw@latest`, then run `openclaw` to start the wizard.
:::

---

## The Security Warning

The first thing the wizard shows you is a security acknowledgment. Read it.

OpenClaw tells you directly: it is a hobby project, still in beta, and a bad prompt can trick it into doing unsafe things. It recommends a security baseline -- pairing and allowlists, sandboxing, least-privilege access -- and links to [docs.openclaw.ai/gateway/security](https://docs.openclaw.ai/gateway/security).

You must acknowledge: "I understand this is powerful and inherently risky. Continue?"

**This is a teaching moment, not a formality.** An agent with access to your email, calendar, and files is a high-value target. The habit of reading security warnings starts here.

---

## QuickStart Onboarding

Select **QuickStart** when the wizard asks. It configures sensible defaults: gateway port 18789, loopback binding (127.0.0.1), token-based auth, Tailscale off. These are secure for local development.

### Connect Your AI (Google Gemini)

Select **Google** as your model provider, then **Google Gemini CLI OAuth** as the authentication method.

A browser window opens for Google sign-in. Authorize the connection. The wizard completes authentication automatically via an OAuth callback on localhost -- no keys or tokens to copy.

The wizard then asks you to pick a model:

- `gemini-2.0-flash` -- fast, lightweight
- `gemini-2.5-flash` -- reasoning capable, 1024k context (recommended)
- `gemini-2.5-pro` -- most capable, slower
- `gemini-3-flash-preview` / `gemini-3-pro-preview` -- latest previews

**Select `gemini-2.5-flash`.** It balances capability with speed for this chapter.

### Connect Telegram

Select **Telegram (Bot API)**. The wizard walks you through creating a bot:

1. Open Telegram and search for **@BotFather** (verified blue checkmark)
2. Send `/newbot`
3. Enter a **display name** (e.g., `My AI Employee`)
4. Enter a **username** ending in `bot` (e.g., `myai_employee_bot`)
5. Copy the **bot token** BotFather gives you

Paste the token into the wizard. No manual JSON editing -- the installer writes the configuration for you.

:::caution Protect Your Bot Token
Your bot token grants full control over your Telegram bot. Treat it like a password. Never share it publicly or commit it to Git.
:::

:::tip Alternative Channels
If Telegram is unavailable in your region or you prefer another platform, OpenClaw supports Discord, Slack, and WhatsApp channels. Select your preferred channel when the wizard asks. The pairing and security steps are similar across all channels. This chapter's examples use Telegram, but every task works identically through any connected channel or the Control UI.
:::

### Skills and Gateway

The wizard offers optional skills to install (`clawhub`, `gog`, `obsidian`, and others). Skip or select what interests you -- none are required for this chapter.

The installer then configures the gateway as a background service (LaunchAgent on macOS, systemd on Linux) and starts it automatically. You see:

```
Telegram: ok (@your_bot_name)
```

Your AI Employee's infrastructure is live.

---

## Meet Your AI Employee

The wizard offers first contact options. Select **Hatch in TUI (recommended)**.

The terminal opens an interactive session. OpenClaw sends: "Wake up, my friend!" Your AI Employee responds: "Hey there! I just came online. Who am I? Who are you?"

Give it a name. Tell it what you do. Describe the work you want help with. The agent remembers this first conversation and uses it to shape future interactions.

**This matters more than it seems.** The difference between a generic chatbot and a personal AI Employee starts with this moment of personalization. You are not configuring a tool. You are onboarding a colleague.

---

## Connect on Telegram

Your bot is running, but Telegram requires one more step: **pairing**. This is a security feature -- your bot ignores messages from anyone it has not explicitly approved.

1. Open Telegram and search for your bot's username (the one ending in `bot`)
2. Send `/start`
3. Your bot replies with a pairing code:

```
OpenClaw: access not configured.
Your Telegram user id: 1234567890
Pairing code: XZ2UC9MN
Ask the bot owner to approve with:
openclaw pairing approve telegram XZ2UC9MN
```

4. In your terminal, approve the pairing:

```bash
openclaw pairing approve telegram XZ2UC9MN
```

**Output:**

```
Approved telegram sender 1234567890.
```

5. Go back to Telegram and send a message. Your AI Employee responds -- same agent, same memory as the TUI session, just a different channel.

**If your bot does not reply at all** (no pairing code, nothing): check the gateway logs at `~/.openclaw/logs/gateway.log`. The most common cause is a mistyped bot token.

---

## The Control UI

You also have a browser-based chat at:

```
http://127.0.0.1:18789/
```

If the plain URL asks for authentication, use the token URL shown during setup (`#token=...`).

Three channels, one agent: TUI, Telegram, and the Control UI all reach the same AI Employee with the same memory. That is the channel adapter pattern from Lesson 1.

---

## Security Checkpoint

Your AI Employee is running. Understand one critical security setting before moving forward.

### Why the Gateway Binds to 127.0.0.1

The gateway only accepts connections from your machine. The address `127.0.0.1` (localhost) means "this computer only." No other device on your network -- and no one on the internet -- can reach your gateway directly.

**This is intentional.** Your AI Employee can read files, browse the web, and execute actions on your behalf. Limiting access to localhost ensures only you interact with the admin interface.

If you change the bind address to `0.0.0.0` (all interfaces), your gateway becomes accessible to anyone on your network -- or the entire internet on a server without a firewall.

| Bind Address                 | Who Can Access             | Use Case                          |
| ---------------------------- | -------------------------- | --------------------------------- |
| `127.0.0.1` (default)        | Only your machine          | Local development, personal use   |
| `0.0.0.0` without auth       | Anyone on network/internet | **Never do this**                 |
| `0.0.0.0` with gateway token | Anyone with the token      | Remote server with authentication |

**The rule**: Never bind to `0.0.0.0` without setting a gateway authentication token first. Use an SSH tunnel or Tailscale for remote access.

---

## Troubleshooting Quick Reference

| Symptom                            | Likely Cause                       | Fix                                                            |
| ---------------------------------- | ---------------------------------- | -------------------------------------------------------------- |
| `command not found: openclaw`      | PATH not updated                   | Close and reopen terminal; run install script again if needed  |
| Installer fails on prerequisites   | Network or permissions             | Run with `sudo` on Linux; ensure Homebrew works on macOS       |
| Google OAuth window won't open     | Browser or firewall                | Copy the URL from terminal and paste into browser manually     |
| OAuth callback fails               | Port 8085 in use                   | Kill the process on port 8085, retry setup                     |
| Bot does not respond on Telegram   | Gateway not running or token wrong | Check `~/.openclaw/logs/gateway.log`                           |
| Gateway won't start                | Port 18789 in use                  | Run `lsof -i :18789`, then `kill` the PID                      |
| Control UI loads but chat fails    | LLM provider unreachable           | Check internet; re-run setup to refresh OAuth tokens           |
| Agent stops after closing terminal | Gateway service not running        | Run `openclaw gateway start` to restart the background service |

**Managing the gateway**: `openclaw gateway status` checks if it is running, `openclaw gateway start` starts it, and `openclaw gateway stop` stops it.

**Getting logs**: Run `cat ~/.openclaw/logs/gateway.log | tail -50` to review recent errors.

---

## The Universal Setup Pattern

Every agent system you will ever encounter follows the same setup sequence:

1. **Install the runtime** -- get the software on your machine
2. **Configure the intelligence** -- connect an LLM provider
3. **Connect I/O channels** -- give the agent ways to communicate
4. **Verify end-to-end** -- send a test message and confirm the round trip
5. **Secure the boundary** -- ensure only authorized users can access the agent

You just completed all five steps. The specifics change between systems, but this pattern is universal. When you encounter a new agent framework, you will already know the shape of the setup process.

---

## Try With AI

Now that your AI Employee is running, use it to deepen your understanding of what you just built.

**Prompt 1 -- Trace the Message Flow:**

```
Walk me through what happens technically when I send a message
to you on Telegram. Trace the message from my phone to the LLM
and back. What systems does it pass through? What could fail at
each step?
```

**What you're learning:** The end-to-end message architecture. Understanding this flow means you can diagnose problems at any point in the chain.

**Prompt 2 -- Security Awareness:**

```
What security risks exist when running a local AI agent that has
access to the internet and can execute actions on my behalf?
List 5 specific risks and how I should mitigate each one.
```

**What you're learning:** As agents gain more capabilities (file access, web browsing, code execution), the attack surface grows. Understanding risks now prevents problems later.

**Prompt 3 -- Troubleshooting Practice:**

```
My OpenClaw Telegram bot is set up but not responding to messages.
Walk me through a systematic troubleshooting checklist. For each
step: what to check, the exact command, expected output, and what
to do if it fails.
```

**What you're learning:** Debugging agent systems systematically. Check the simplest things first, verify each layer independently.
