### Core Concept
**Least privilege means ensuring that even when code fails, the damage is contained — an agent running as a restricted user with access only to its own directory cannot destroy system files or steal secrets from other services.** Security isn't about writing better code; it's about limiting the blast radius when code inevitably breaks.

### Key Mental Models
- **Blast Radius Containment**: Running as root gives unlimited power. Running as a dedicated user limits damage to that user's files — even if the agent is compromised.
- **Three Layers of Defense**: Identity (who runs it → `useradd`), Access (what files they touch → `chmod`/`chown`), Secrets (how credentials are stored → `.env` files).
- **Export vs No Export**: A variable without `export` exists only in the current shell. An exported variable passes to child processes. This distinction controls whether agents launched as subprocesses can see configuration values.

### Critical Patterns
- **Dedicated service users**: Create non-root users with `useradd --system --shell /usr/sbin/nologin` — the nologin shell prevents anyone from SSH-ing in as the agent user.
- **Numeric permissions**: `700` = owner only, `600` = owner read/write, `755` = owner full + others read/execute. Always set the minimum permissions needed.
- **chown for ownership transfer**: `chown -R agent-runner:agent-runner /opt/agent/` assigns all files to the agent user recursively.
- **Secrets in .env files, never in code**: Store API keys in `.env` files, source them in scripts, restrict permissions to `600`, and add `.env` to `.gitignore`.
- **SSH key generation**: Use `ssh-keygen -t ed25519` for key-based authentication — keys are more secure than passwords and required for automated access.

### Common Mistakes
- **Running agents as root**: The most common and most dangerous mistake. Even "just a test" can delete critical system files if the code has a bug.
- **Hardcoding secrets in source code**: API keys in source files get committed to repositories and exposed to anyone with access. Use environment variables instead.
- **Setting 777 permissions**: Giving everyone read/write/execute access defeats the purpose of permissions entirely. Use the minimum permission set needed.
