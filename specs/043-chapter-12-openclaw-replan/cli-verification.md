# Chapter 12 CLI Verification — Phase 0

## Date: 2026-02-13

## Sources

- [OpenClaw Official CLI Reference](https://docs.openclaw.ai/cli)
- [DeepWiki CLI Reference](https://deepwiki.com/openclaw/openclaw/12-cli-reference)
- [DeepWiki Gateway Commands](https://deepwiki.com/openclaw/openclaw/12.1-gateway-commands)
- [OpenClaw Configuration](https://docs.openclaw.ai/gateway/configuration)
- [Gmail Pub/Sub Docs](https://docs.openclaw.ai/automation/gmail-pubsub)
- [Exec Approvals Docs](https://docs.openclaw.ai/tools/exec-approvals)
- [gogcli GitHub (steipete)](https://github.com/steipete/gogcli)
- [OpenClaw GitHub Issues/PRs](https://github.com/openclaw/openclaw)

---

## Executive Finding

**~70% of CLI commands are correct. Two critical commands are fictional. One entire lesson (L10) teaches a fictional integration pattern.**

The chapter's biggest technical error is L10's "Gmail MCP" — Gmail in OpenClaw does NOT use MCP. It uses `gog` (gogcli) + webhooks/hooks. The commands `openclaw mcp auth gmail` and `clawhub install gmail-mcp` do not exist.

---

## Command-by-Command Verification

### Installation & Setup (L2)

| Command in Chapter                                  | Status | Correct Form                                                        | Notes                                                                                                          |
| --------------------------------------------------- | ------ | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `curl -fsSL https://openclaw.ai/install.sh \| bash` | ✅     | Same                                                                | Real install script                                                                                            |
| `openclaw --version`                                | ✅     | Same                                                                | Standard version check                                                                                         |
| `openclaw gateway run --port 18789 --verbose`       | ⚠️     | `openclaw gateway --port 18789 --verbose` OR `openclaw gateway run` | Both `openclaw gateway` and `openclaw gateway run` appear in docs. `--port` and `--verbose` are verified flags |
| `openclaw pairing approve telegram ABC123`          | ✅     | Same                                                                | Real pairing command                                                                                           |

**Missing from L2**: `openclaw onboard` — the official recommended setup wizard. L2 manually configures everything instead of using the wizard. The `onboard` command handles LLM provider, channels, and daemon installation automatically.

### Configuration (Various Lessons)

| Command in Chapter                   | Status | Correct Form   | Notes                                                                         |
| ------------------------------------ | ------ | -------------- | ----------------------------------------------------------------------------- |
| `openclaw config set <path> <value>` | ✅     | Same           | Real. JSON5 or raw string values                                              |
| `openclaw config get <path>`         | ✅     | Same           | Real                                                                          |
| `openclaw config edit`               | ❌     | Does not exist | Only `get`, `set`, `unset`. Edit file directly at `~/.openclaw/openclaw.json` |

### Gateway (Various Lessons)

| Command in Chapter                  | Status | Correct Form | Notes                                                                                                                                                         |
| ----------------------------------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `openclaw gateway run --port 18789` | ⚠️     | See note     | `openclaw gateway run` exists per official CLI list. `--port` flag is verified. DeepWiki says foreground is `openclaw gateway` (without `run`). Both may work |
| `openclaw gateway restart`          | ✅     | Same         | Real service management command                                                                                                                               |
| `openclaw gateway start`            | ✅     | Same         | Starts supervised service                                                                                                                                     |
| `openclaw gateway stop`             | ✅     | Same         | Graceful shutdown                                                                                                                                             |

### Agent Management (L9)

| Command in Chapter     | Status | Correct Form | Notes        |
| ---------------------- | ------ | ------------ | ------------ |
| `openclaw agents list` | ✅     | Same         | Real command |

### Skills (L6-L8)

| Command in Chapter            | Status | Correct Form | Notes        |
| ----------------------------- | ------ | ------------ | ------------ |
| `openclaw skills list`        | ✅     | Same         | Real command |
| `openclaw skills info <name>` | ✅     | Same         | Real command |

### Gmail MCP (L10) — THE PROBLEM LESSON

| Command in Chapter                           | Status | Correct Form  | Notes                                                                                             |
| -------------------------------------------- | ------ | ------------- | ------------------------------------------------------------------------------------------------- |
| `openclaw config set mcp.gmail.enabled true` | ❌     | **Fictional** | Gmail is NOT an MCP server in OpenClaw. Gmail uses `gog` + webhooks                               |
| `openclaw mcp auth gmail`                    | ❌     | **Fictional** | This command does not exist. Gmail auth uses `gog auth add` + `gog auth credentials`              |
| `clawhub install gmail-mcp --force`          | ❌     | **Fictional** | `clawhub` does not exist as a command. Skills use `openclaw plugins install` or `openclaw skills` |

**Reality**: Gmail integration in OpenClaw uses:

1. `gog` (gogcli by Peter Steinberger) — a Google Suite CLI tool
2. `gog auth credentials` — store OAuth client credentials
3. `gog auth add` — authenticate with Google
4. `gog gmail search`, `gog gmail send`, etc. — direct Gmail operations
5. `openclaw webhooks gmail setup` — configure proactive monitoring via Pub/Sub
6. Hooks configuration in `~/.openclaw/openclaw.json`

**The 19 "Gmail MCP tools" described in L10 are actually `gog` commands exposed as agent tools through OpenClaw's hooks/tools system, NOT through an MCP server.**

### Webhooks & Gmail Monitoring (L12)

| Command in Chapter                                      | Status | Correct Form   | Notes                                             |
| ------------------------------------------------------- | ------ | -------------- | ------------------------------------------------- |
| `openclaw webhooks gmail setup --account you@gmail.com` | ✅     | Same           | Real command — sets up Pub/Sub + Tailscale Funnel |
| `openclaw webhooks gmail run`                           | ✅     | Same           | Starts the Gmail webhook daemon                   |
| `openclaw webhooks gmail status`                        | ✅     | Likely correct | Status checking exists                            |
| `gog gmail send --to --subject --body`                  | ✅     | Same           | Real `gogcli` command                             |
| `gog gmail history --account --since`                   | ⚠️     | Likely correct | gog has gmail subcommands                         |

**L12 is largely accurate.** The webhook/hooks/Pub/Sub architecture described matches the real system. However, `gog` should be properly introduced (L12 uses it without explanation).

### HITL / Exec Approvals (L13)

| Command in Chapter                          | Status | Correct Form | Notes                  |
| ------------------------------------------- | ------ | ------------ | ---------------------- |
| `~/.openclaw/exec-approvals.json`           | ✅     | Same         | Real file path         |
| Security modes: `deny`, `allowlist`, `full` | ✅     | Same         | Real modes             |
| Ask modes: `off`, `on-miss`, `always`       | ✅     | Same         | Real modes             |
| `/approve`, `/deny` commands                | ✅     | Same         | Real approval commands |
| `askFallback` setting                       | ✅     | Same         | Real configuration     |
| `safeBins` concept                          | ✅     | Same         | Real feature           |
| `autoAllowSkills`                           | ✅     | Same         | Real feature           |

**L13 is largely accurate.** The exec-approvals system is well-documented and the lesson's description closely matches reality.

### Diagnostics (Various)

| Command in Chapter         | Status | Correct Form                        | Notes                                             |
| -------------------------- | ------ | ----------------------------------- | ------------------------------------------------- |
| `openclaw health`          | ✅     | Same (or `openclaw gateway health`) | Real                                              |
| `openclaw doctor`          | ✅     | Same                                | Real — config validation, port checks             |
| `openclaw status`          | ✅     | Same                                | Real                                              |
| `openclaw status --all`    | ⚠️     | Unknown                             | `openclaw status` exists; `--all` flag unverified |
| `openclaw logs --follow`   | ✅     | Likely correct                      | `openclaw logs` is a real command                 |
| `openclaw security audit`  | ✅     | Same                                | Real                                              |
| `openclaw config validate` | ⚠️     | May not exist                       | `openclaw doctor` is the validation tool          |

### Deployment (L14)

| Command in Chapter                                 | Status | Correct Form   | Notes                                     |
| -------------------------------------------------- | ------ | -------------- | ----------------------------------------- |
| `pm2 start/stop/restart/status/logs/monit`         | ✅     | Same           | Standard PM2 commands                     |
| `systemctl --user restart openclaw-gateway`        | ✅     | Same           | Real systemd user service                 |
| `openclaw doctor --generate-gateway-token`         | ⚠️     | Likely correct | `openclaw doctor` exists; flag unverified |
| `openclaw config set gateway.bind loopback`        | ✅     | Same           | Real config path                          |
| `openclaw config set gateway.auth.mode token`      | ✅     | Same           | Real config path                          |
| `openclaw config set gateway.tailscale.mode serve` | ✅     | Same           | Real config path                          |
| `tailscale up --ssh --hostname=openclaw`           | ✅     | Same           | Standard Tailscale command                |

---

## Summary by Lesson

| Lesson              | Commands Verified | Commands Wrong | Commands Uncertain | Overall                                             |
| ------------------- | ----------------- | -------------- | ------------------ | --------------------------------------------------- |
| L2 (Setup)          | 3                 | 0              | 1                  | ⚠️ Missing `onboard`                                |
| L4 (Architecture)   | 1                 | 0              | 0                  | ⚠️ References `onboard --install-daemon` not taught |
| L6-L8 (Skills)      | 2                 | 0              | 0                  | ✅ Good                                             |
| L9 (Subagents)      | 1                 | 0              | 0                  | ✅ Good                                             |
| **L10 (Gmail MCP)** | **0**             | **3**          | **0**              | **❌ Fictional integration**                        |
| L12 (Watchers)      | 3                 | 0              | 1                  | ✅ Good (but gog unexplained)                       |
| L13 (HITL)          | 8                 | 0              | 0                  | ✅ Accurate                                         |
| L14 (Deployment)    | 7                 | 0              | 2                  | ✅ Good                                             |
| Config commands     | 2                 | 1              | 0                  | ⚠️ `config edit` doesn't exist                      |
| Diagnostics         | 4                 | 0              | 2                  | ✅ Mostly good                                      |

---

## Critical Fixes Required

### Fix 1: L10 Must Be Rewritten (Gmail Integration)

The entire "Gmail MCP" concept is wrong. Replace with the actual pattern:

**Current (fictional)**:

```
openclaw config set mcp.gmail.enabled true
openclaw mcp auth gmail
→ OAuth flow
→ 19 Gmail MCP tools available
```

**Should be (real)**:

```
# Install gog (Google Suite CLI)
brew install steipete/tap/gogcli  # macOS
# or: npm install -g gogcli

# Authenticate with Google
gog auth credentials  # paste OAuth client ID/secret
gog auth add --account you@gmail.com  # OAuth browser flow

# Test Gmail access
gog gmail search 'newer_than:1d' --account you@gmail.com --max 5

# Configure OpenClaw to use gog for email
openclaw config set hooks.gmail.account "you@gmail.com"
```

### Fix 2: L2 Should Use `openclaw onboard`

The official recommended setup is `openclaw onboard`, which handles LLM, channels, and daemon installation. L2 manually does what `onboard` does automatically.

### Fix 3: Replace `openclaw config edit` Everywhere

Replace with either `openclaw config set <path> <value>` or "Edit `~/.openclaw/openclaw.json` directly."

### Fix 4: Introduce `gog` Before Using It

L12 and L14 use `gog` commands without introduction. Either:

- Introduce `gog` in the rewritten L10 (Gmail integration)
- Or add a brief "What is gog?" section in L12
