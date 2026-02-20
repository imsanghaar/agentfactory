# OpenClaw Isolation Options Research

**Research Date**: 2026-02-05
**Purpose**: Evaluate OpenClaw for isolated/safe mode operation in educational contexts

---

## Executive Summary

OpenClaw provides comprehensive isolation capabilities suitable for educational deployment. Key findings:

- **Sandbox mode**: Full Docker-based isolation with configurable access levels
- **Demo mode**: QuickStart with safe defaults; no explicit "demo mode" toggle
- **Tool restrictions**: Granular allow/deny lists with approval workflows
- **Minimum permissions**: Read-only agents with zero filesystem write access possible
- **Local LLM**: Full Ollama support eliminates API costs entirely

---

## 1. Can OpenClaw Run in a Sandbox/Container?

**Yes - Multiple isolation levels available.**

### Full Gateway Containerization

Run the entire OpenClaw gateway inside Docker:

```bash
./docker-setup.sh  # Quick-start script handles everything
```

**Security posture:**
- Non-root user (`node`, uid 1000)
- Read-only root filesystem
- All Linux capabilities dropped
- Per-container resource limits (1GB RAM, 1 CPU default)
- PID limits (256 processes max)
- AppArmor/seccomp profile support

### Per-Tool Sandboxing (Host + Docker Hybrid)

Gateway runs on host; tool execution isolated in Docker:

```json5
{
  agents: {
    defaults: {
      sandbox: {
        mode: "all",           // "off" | "non-main" | "all"
        scope: "session",      // "agent" | "session" | "shared"
        workspaceAccess: "ro"  // "none" | "ro" | "rw"
      }
    }
  }
}
```

**Isolation scopes:**
| Scope | Behavior |
|-------|----------|
| `agent` | Persistent per-agent workspace |
| `session` | Per-conversation, auto-cleaned |
| `shared` | Single container (not recommended for multi-agent) |

**Container execution includes:**
- Read-only root filesystem
- Memory/CPU limits
- Network isolation (`--network none`)
- Workspace mount at `/workspace`

**Sources:**
- [Docker - OpenClaw Docs](https://docs.openclaw.ai/install/docker)
- [DigitalOcean OpenClaw Deployment](https://www.digitalocean.com/community/tutorials/how-to-run-openclaw)
- [Simon Willison's Docker TIL](https://til.simonwillison.net/llms/openclaw-docker)

---

## 2. Is There a "Demo Mode" Without Real Messaging Access?

**No explicit "demo mode" toggle, but equivalent setups exist.**

### QuickStart Safe Defaults

The QuickStart option configures everything with safe defaults:

```bash
openclaw quickstart  # Sets up sensible defaults
```

### Isolated Network Configuration

Run OpenClaw without external messaging by:

1. **Binding to loopback only:**
```json5
{
  gateway: {
    bind: "loopback",
    auth: { mode: "token", token: "your-token" }
  }
}
```

2. **Disabling all channels:**
```json5
{
  channels: {
    whatsapp: { enabled: false },
    telegram: { enabled: false },
    discord: { enabled: false }
  }
}
```

3. **CLI-only interaction:**
Use `openclaw chat` for local terminal interaction without any messaging platform.

### Educational Virtual Environment

Deploy in isolated VM/cloud instance:
- Security features: authenticated communication, hardened firewall, non-root execution, Docker isolation
- No personal machine exposure
- VPN/Tailscale for secure external access if needed

**Sources:**
- [Security - OpenClaw Docs](https://docs.openclaw.ai/gateway/security)
- [Codecademy OpenClaw Tutorial](https://www.codecademy.com/article/open-claw-tutorial-installation-to-first-chat-setup)
- [Master OpenClaw in 30 Minutes](https://creatoreconomy.so/p/master-openclaw-in-30-minutes-full-tutorial)

---

## 3. Can Tools/Actions Be Restricted?

**Yes - Comprehensive multi-layered tool access control.**

### Tool Allow/Deny Lists

```json5
{
  tools: {
    allow: ["read", "memory_read"],  // Whitelist specific tools
    deny: ["exec", "write", "edit", "apply_patch", "browser"]  // Deny wins
  }
}
```

**Tool groups for simplified policy:**
| Group | Tools Included |
|-------|---------------|
| `group:runtime` | `exec`, `bash`, `process` |
| `group:fs` | `read`, `write`, `edit`, `apply_patch` |
| `group:web` | `web_fetch`, `web_search`, `browser` |
| `group:ui` | `browser`, `canvas` |

### Per-Agent Tool Profiles

Prebuilt profiles for common scenarios:

| Profile | Access Level |
|---------|-------------|
| `minimal` | Read-only, no execution |
| `coding` | Filesystem + exec |
| `messaging` | Channel tools only |
| `full` | All tools enabled |

```json5
{
  agents: {
    list: [
      {
        id: "student-agent",
        tools: { profile: "minimal" }
      }
    ]
  }
}
```

### Approval Workflows

Require human confirmation for dangerous operations:

```json5
{
  tools: {
    exec: {
      mode: "always",           // "off" | "elevated" | "always"
      safeBins: ["ls", "cat", "pwd"]  // Skip approval for safe commands
    }
  }
}
```

Approval via `/approve` command with 5-minute expiration.

### Policy Resolution Order

```
Tool Profiles → Provider Profile → Global Policy → Provider Policy → Agent Policy → Group Policy → Sandbox Policy
```

**Deny always wins over allow.**

**Sources:**
- [Tool Security and Sandboxing - DeepWiki](https://deepwiki.com/openclaw/openclaw/6.2-tool-security-and-sandboxing)
- [Security - OpenClaw Docs](https://docs.openclaw.ai/gateway/security)
- [Composio Security Guide](https://composio.dev/blog/secure-openclaw-moltbot-clawdbot-setup)

---

## 4. What's the Minimum Permission Setup?

**Read-only agent with zero write capability.**

### Minimal Configuration

```json5
{
  gateway: {
    bind: "loopback",
    auth: { mode: "token", token: "secure-token" }
  },
  agents: {
    list: [
      {
        id: "readonly-student",
        sandbox: {
          mode: "all",
          scope: "session",
          workspaceAccess: "none"  // No agent workspace access
        },
        tools: {
          profile: "minimal",
          allow: ["read", "memory_read"],
          deny: [
            "write", "edit", "apply_patch",  // No file modification
            "exec", "bash", "process",        // No execution
            "browser", "web_fetch",           // No web access
            "gateway_*"                       // No gateway control
          ]
        }
      }
    ]
  }
}
```

### Recommended Security Layers

1. **Network**: Loopback binding, Tailscale, token auth
2. **Channels**: Pairing/allowlists, mention gating
3. **Sandbox**: Session-scoped isolation
4. **Tools**: Minimal profile with explicit allowlist
5. **Secrets**: Environment variables, not in workspace
6. **Audit**: Regular `openclaw doctor` checks

### Security Audit Command

```bash
openclaw security audit --fix
```

Auto-applies safe guardrails:
- Tightens `groupPolicy="open"` to `groupPolicy="allowlist"`
- Sets directory permissions (`~/.openclaw` → 700)
- Sets file permissions (config → 600)

**Sources:**
- [JFrog Security Guide](https://jfrog.com/blog/giving-openclaw-the-keys-to-your-kingdom-read-this-first/)
- [OpenClaw Safety Principles](https://zenvanriel.nl/ai-engineer-blog/openclaw-safety-principles-automation-guide/)
- [ToxSec Security Checklist](https://www.toxsec.com/p/openclaw-security-checklist)

---

## 5. Can It Run with Just Local LLM (No API Costs)?

**Yes - Full Ollama integration with zero API costs.**

### Setup Steps

1. **Install Ollama:**
```bash
# Download from https://ollama.ai
ollama pull llama3.3
ollama pull qwen2.5-coder:32b
ollama pull deepseek-r1:32b
```

2. **Configure OpenClaw:**
```bash
export OLLAMA_API_KEY="ollama-local"
# or
openclaw config set models.providers.ollama.apiKey "ollama-local"
```

3. **Set agent model:**
```json5
{
  agents: {
    defaults: {
      model: { primary: "ollama/llama3.3" }
    }
  }
}
```

### Auto-Discovery

When `OLLAMA_API_KEY` is set, OpenClaw automatically:
- Queries local Ollama at `http://127.0.0.1:11434`
- Discovers tool-capable models
- Reads context window data
- **Sets all costs to $0**

### Recommended Local Models

| Model | Best For |
|-------|----------|
| `qwen2.5-coder:32b` | Coding tasks |
| `qwen3` | General purpose |
| `deepseek-r1:32b` | Reasoning |
| `llama3.3` | Balanced performance |

### Verification

```bash
curl http://localhost:11434/api/tags  # Check Ollama running
ollama list                            # View installed models
openclaw models list                   # Verify OpenClaw sees models
```

### Privacy Benefit

All data stays local - no external API calls, no data leaving your network.

**Sources:**
- [Ollama - OpenClaw Docs](https://docs.openclaw.ai/providers/ollama)
- [Ollama Blog - OpenClaw](https://ollama.com/blog/openclaw)
- [CodersEra Setup Guide](https://codersera.com/blog/openclaw-ollama-setup-guide-run-local-ai-agents-2026)
- [DEV Community - Free OpenClaw](https://dev.to/vishal_veerareddy_9cdd17d/run-openclawclawdbot-for-free-with-lynkr-no-api-bills-3kg2)

---

## Educational Deployment Recommendation

### Complete Isolated Educational Setup

```json5
// openclaw.json - Educational Safe Configuration
{
  gateway: {
    bind: "loopback",
    auth: { mode: "token", token: "edu-token-2026" }
  },

  models: {
    providers: {
      ollama: { apiKey: "ollama-local" }
    }
  },

  channels: {
    // All external channels disabled
    whatsapp: { enabled: false },
    telegram: { enabled: false }
  },

  agents: {
    defaults: {
      model: { primary: "ollama/qwen2.5-coder:32b" },
      sandbox: {
        mode: "all",
        scope: "session",
        workspaceAccess: "ro"
      }
    },
    list: [
      {
        id: "student-sandbox",
        tools: {
          profile: "minimal",
          allow: ["read", "memory_read", "memory_write"],
          deny: ["exec", "write", "edit", "browser", "web_fetch"]
        }
      }
    ]
  },

  tools: {
    exec: { mode: "always" },  // Require approval for any execution
    elevated: { allowFrom: [] }  // No elevated access
  }
}
```

### Deployment Options

| Option | Isolation Level | Cost | Complexity |
|--------|----------------|------|------------|
| Local Docker | High | Free | Low |
| Cloud VM (DigitalOcean) | Very High | ~$5/mo | Medium |
| Dedicated hardware | Maximum | Hardware cost | High |

### Security Checklist for Education

- [ ] Ollama running locally (no API costs)
- [ ] Gateway bound to loopback only
- [ ] All messaging channels disabled
- [ ] Sandbox mode enabled for all agents
- [ ] Tool profile set to `minimal`
- [ ] Exec tool requires `always` approval
- [ ] `openclaw security audit --fix` passed
- [ ] File permissions verified (700/600)

---

## Conclusion

OpenClaw is **well-suited for educational use** with proper configuration:

1. **Sandbox capabilities**: Comprehensive Docker-based isolation
2. **Demo mode equivalent**: QuickStart + loopback + disabled channels
3. **Tool restrictions**: Multi-layered allow/deny with approval workflows
4. **Minimum permissions**: Read-only agents with session-scoped sandboxes
5. **Local LLM**: Full Ollama support, zero API costs, data stays local

The platform's security-first design with layered defenses makes it appropriate for teaching AI agent concepts without exposing students to production risks.
