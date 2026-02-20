# OpenClaw Reference for Content Implementers

**Purpose**: Consolidated reference from official OpenClaw docs for lesson content creation.
**Source**: `/workspace/openclaw-main/docs/`

---

## Quick Setup Commands

### Installation (3 options)

```bash
# Option 1: One-line install (recommended)
curl -fsSL https://openclaw.ai/install.sh | bash

# Option 2: npm global
npm install -g openclaw@latest

# Option 3: pnpm global
pnpm add -g openclaw@latest
```

### Onboarding Wizard

```bash
openclaw onboard --install-daemon
```

The wizard configures:
- Model/auth (OAuth or API key)
- Gateway settings
- Channels (WhatsApp/Telegram/Discord)
- Pairing defaults
- Workspace bootstrap + skills
- Optional background service

---

## LLM Provider Setup

### Moonshot Kimi K2.5 (Best Free Option)

```bash
openclaw onboard --auth-choice moonshot-api-key
```

**Config snippet:**
```json5
{
  env: { MOONSHOT_API_KEY: "sk-..." },
  agents: {
    defaults: {
      model: { primary: "moonshot/kimi-k2.5" }
    }
  },
  models: {
    providers: {
      moonshot: {
        baseUrl: "https://api.moonshot.ai/v1",
        apiKey: "${MOONSHOT_API_KEY}",
        api: "openai-completions"
      }
    }
  }
}
```

**Available Kimi K2 Models:**
- `kimi-k2.5` - Default, recommended
- `kimi-k2-0905-preview`
- `kimi-k2-turbo-preview`
- `kimi-k2-thinking` - Reasoning model
- `kimi-k2-thinking-turbo`

**Limits**: ~1.5M tokens/day free, 256K context window

### Google Gemini (Easiest Setup)

```bash
openclaw onboard --auth-choice google-gemini-cli
# OAuth flow - no API key needed
```

**Limits**: 1000 requests/day (Flash-Lite), 1M context window

### Ollama (Free Forever, Local)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5-coder:14b

# Configure OpenClaw
export OLLAMA_API_KEY="ollama-local"
openclaw config set agents.defaults.model.primary "ollama/qwen2.5-coder:14b"
```

---

## Telegram Setup

### Creating a Bot (BotFather)

1. Open Telegram, message **@BotFather** ([direct link](https://t.me/BotFather))
2. Run `/newbot`
3. Follow prompts (name + username ending in `bot`)
4. Copy the token

### Configuration

```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "123:abc",
      dmPolicy: "pairing"  // Requires approval code for new users
    }
  }
}
```

Or via CLI:
```bash
openclaw config set channels.telegram.botToken "YOUR_TOKEN"
```

### Pairing Flow

1. User DMs the bot
2. Bot returns a pairing code
3. Approve with: `openclaw pairing approve telegram <CODE>`

### Group Configuration

```json5
{
  channels: {
    telegram: {
      groups: {
        "*": { requireMention: true }  // All groups, mention-only
      }
    }
  }
}
```

---

## Workspace & Bootstrap Files

### Default Location

`~/.openclaw/workspace/`

### Bootstrap Files (Injected Every Session)

| File | Purpose |
|------|---------|
| `AGENTS.md` | Operating instructions, "how to behave" |
| `SOUL.md` | Persona, tone, boundaries |
| `USER.md` | Who the user is, how to address them |
| `IDENTITY.md` | Agent's name, vibe, emoji |
| `TOOLS.md` | Notes about local tools and conventions |
| `HEARTBEAT.md` | Optional tiny checklist for heartbeat runs |
| `BOOTSTRAP.md` | One-time first-run ritual (deleted after) |
| `memory/YYYY-MM-DD.md` | Daily memory log |

### Example SOUL.md (Branding Expert)

```markdown
# Soul

You are a Branding Expert AI Employee named "BrandBot".

## Persona
- Creative, strategic thinker
- Specializes in YouTube content, trend analysis, video themes
- Direct and actionable communication style

## Tone
- Professional but approachable
- Uses industry terminology naturally
- Proactive - suggests improvements without being asked

## Boundaries
- Don't make financial decisions without approval
- Don't publish content without explicit confirmation
- Always cite sources for trend data
```

### Example AGENTS.md (Operating Instructions)

```markdown
# Operating Instructions

## Daily Routine
1. Check YouTube trends and competitor activity
2. Draft content ideas for the week
3. Summarize insights in daily memory

## Tools You Use
- YouTube API for trend data
- Browser for research
- Gmail for scheduling reminders

## Memory Protocol
- Write daily summaries to `memory/YYYY-MM-DD.md`
- Tag important insights with #important
- Reference yesterday's memory for context
```

---

## Skills System

### Skill Locations (Precedence)

1. `<workspace>/skills/` - Workspace-specific (highest)
2. `~/.openclaw/skills/` - Managed/local
3. Bundled - Shipped with install (lowest)

### Skill Format (SKILL.md)

```markdown
---
name: email-drafter
description: Draft professional emails with appropriate tone and formatting
metadata: { "openclaw": { "always": true } }
---

# Email Drafter Skill

You are an expert email writer. When asked to draft an email:

1. Ask for: recipient, purpose, key points, tone
2. Draft the email with proper formatting
3. Offer variations if requested

## Output Format
Always use this structure:
- Subject line
- Greeting
- Body paragraphs
- Call to action
- Professional closing
```

### Installing Skills from ClawHub

```bash
clawhub install <skill-slug>
clawhub update --all
```

---

## Oracle Cloud Free Tier Setup

### Instance Configuration

- **Shape**: `VM.Standard.A1.Flex` (Ampere ARM)
- **OCPUs**: 2-4 (free)
- **Memory**: 12-24 GB (free)
- **Boot volume**: 50-200 GB (free)
- **Image**: Ubuntu 24.04 (aarch64)

### Setup Steps

```bash
# 1. Connect via SSH
ssh ubuntu@YOUR_PUBLIC_IP

# 2. Update system
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential

# 3. Install Tailscale (for secure access)
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --ssh --hostname=openclaw

# 4. Install OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash
source ~/.bashrc

# 5. Configure for loopback + Tailscale
openclaw config set gateway.bind loopback
openclaw config set gateway.auth.mode token
openclaw doctor --generate-gateway-token
openclaw config set gateway.tailscale.mode serve

# 6. Start service
systemctl --user restart openclaw-gateway
```

### Verify

```bash
openclaw --version
systemctl --user status openclaw-gateway
tailscale serve status
curl http://localhost:18789
```

---

## Gateway Commands

```bash
# Status and health
openclaw status
openclaw health
openclaw security audit --deep

# Gateway control
openclaw gateway run --port 18789 --verbose
openclaw gateway status

# Channel management
openclaw channels status
openclaw channels login  # WhatsApp QR

# Pairing
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>

# Configuration
openclaw config set <path> <value>
openclaw configure --section web

# Diagnostics
openclaw doctor
openclaw logs --follow
```

---

## Common Config Paths

| Path | Purpose |
|------|---------|
| `gateway.bind` | Network binding (loopback, public) |
| `gateway.auth.mode` | Auth mode (token, none) |
| `gateway.auth.token` | Gateway token |
| `agents.defaults.workspace` | Workspace directory |
| `agents.defaults.model.primary` | Default model |
| `channels.telegram.botToken` | Telegram bot token |
| `channels.telegram.dmPolicy` | DM access (pairing, allowlist, open) |
| `models.providers.*` | LLM provider config |

---

## Security Checklist for Teaching

- [ ] Gateway bound to loopback (`gateway.bind: "loopback"`)
- [ ] Token auth enabled (`gateway.auth.mode: "token"`)
- [ ] Credentials have proper permissions (`chmod 700 ~/.openclaw`)
- [ ] No secrets in workspace repo
- [ ] Security audit passes (`openclaw security audit`)

---

## Key URLs

| Resource | URL |
|----------|-----|
| OpenClaw Docs | https://docs.openclaw.ai |
| ClawHub Skills | https://clawhub.com |
| Moonshot Platform | https://platform.moonshot.ai |
| Google AI Studio | https://aistudio.google.com |
| Ollama | https://ollama.com |
| Oracle Cloud Free | https://cloud.oracle.com/free |

---

## Source Documentation Paths

For deeper reference, these docs are in `/workspace/openclaw-main/docs/`:

| Topic | Path |
|-------|------|
| Getting Started | `start/getting-started.md` |
| Agent Runtime | `concepts/agent.md` |
| Agent Workspace | `concepts/agent-workspace.md` |
| Skills | `tools/skills.md` |
| Telegram | `channels/telegram.md` |
| Moonshot | `providers/moonshot.md` |
| Oracle Cloud | `platforms/oracle.md` |
| Security | `gateway/security.md` |
| Configuration | `gateway/configuration.md` |
