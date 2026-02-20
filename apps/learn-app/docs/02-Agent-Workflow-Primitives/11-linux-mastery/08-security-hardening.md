---
sidebar_position: 8
chapter: 11
lesson: 8
title: "Security Hardening & Least Privilege"
description: "Create dedicated service users, configure file permissions with chmod and chown, manage environment variables with proper scoping, and handle secrets using .env files -- all following the principle of least privilege."
keywords:
  [
    "security",
    "least privilege",
    "chmod",
    "chown",
    "useradd",
    "permissions",
    "environment variables",
    "ssh-keygen",
    "env files",
    "secrets",
  ]
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "User and Group Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can create dedicated non-root service users with restricted shells and verify their configuration"

  - name: "File Permissions Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can set file permissions using both numeric and symbolic chmod notation and verify the result"

  - name: "File Ownership Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can transfer ownership of files and directories using chown and chgrp"

  - name: "SSH Key Generation"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can generate ed25519 SSH key pairs and explain the public/private key relationship"

  - name: "Environment Variable Scoping"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can predict whether a variable will be visible in a subshell based on whether it was exported"

  - name: "Secret Management with .env Files"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can create, source, and secure .env files with correct permissions and gitignore rules"

learning_objectives:
  - objective: "Create dedicated non-root users for agent processes with restricted shells"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates agent-runner user with nologin shell and verifies uid/gid and passwd entry"

  - objective: "Configure file permissions using chmod and chown following the least-privilege principle"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates config file readable only by agent-runner, verifies with ls -la"

  - objective: "Manage environment variables with proper scoping including export vs non-export and subshell visibility"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Student demonstrates that exported variables propagate to subshells while non-exported variables do not"

  - objective: "Handle secrets using environment variables sourced from .env files that are never committed to version control"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates secured .env file, sources it in a script, and adds .env to .gitignore"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "User/group management (useradd, usermod, groups)"
    - "File permissions (chmod numeric and symbolic)"
    - "Ownership (chown, chgrp)"
    - "SSH key generation (ssh-keygen)"
    - "Environment variable scoping (export vs no export, subshells)"
    - ".env file management (source, never commit)"
  assessment: "6 concepts at B2 level (within 7-10 limit). Concepts build sequentially from identity to access to secrets."

differentiation:
  extension_for_advanced: "Explore ACLs (Access Control Lists) with setfacl for fine-grained permissions. Investigate Linux capabilities (setcap) for granting specific privileges without root. Research secret management tools like HashiCorp Vault for production environments."
  remedial_for_struggling: "Focus on useradd and chmod first. Practice creating users and setting permissions on simple files before working with environment variables. Use ls -la after every permission change to verify results."

teaching_guide:
  lesson_type: "core"
  session_group: 3
  session_title: "Text Processing and Automation"
  key_points:
    - "Least privilege is the core principle — even when code has bugs, restricted users limit damage to one agent's workspace instead of the entire server"
    - "chmod numeric notation (600, 700, 750, 755) must become second nature — the permission guidelines table maps file types to recommended permissions for agent deployments"
    - ".env files with chmod 600 are the standard for secret management — secrets in source code are a security incident waiting to happen"
    - "export vs non-export variable scoping determines whether child processes (like agent scripts) can access API keys — this is the #1 cause of 'my agent cannot find its API key'"
  misconceptions:
    - "Students think running as root is fine for testing — the security incident scenario shows that test habits become production habits, and root access multiplies damage"
    - "Students confuse chmod 777 (everyone can do everything) with chmod 700 (only owner) — emphasize that 777 is almost never correct and is a red flag in code review"
    - "Students expect non-exported variables to be visible in scripts they run — the subshell exercise demonstrates that only exported variables propagate"
    - "Students think removing a committed .env from git history fixes the leak — once pushed, consider all secrets compromised; rotate immediately"
  discussion_prompts:
    - "In the security incident scenario, three failures compounded into a breach. Which single fix would have prevented the most damage, and why?"
    - "Your team says 'just use root, it is faster.' How would you explain the risk in terms they understand — using the blast radius concept from this lesson?"
  teaching_tips:
    - "Open with the security incident scenario — it makes abstract concepts concrete and motivates every defense taught in the lesson"
    - "The permission guidelines table (file type to chmod value) is a reference card moment — students will use this when deploying agents in lesson 14"
    - "Demo the export vs non-export exercise live — students seeing an empty variable in a subshell is the proof they need to understand scoping"
    - "The .env + .gitignore workflow should be practiced as a sequence: create file, chmod 600, add to .gitignore — make it muscle memory"
  assessment_quick_check:
    - "Ask: what chmod value makes a file readable only by its owner? (Expected: 600)"
    - "Ask students to demonstrate that an exported variable is visible in a subshell but a non-exported one is not"
    - "Give an ls -la output and ask students to identify which files have overly permissive permissions (look for 777 or world-readable secrets)"

teaching_approach: "Socratic. Present a security incident, ask what went wrong, then build the defense."
modality: "Socratic Dialogue (security incident analysis leading to defensive practices)"

# Generation metadata
generated_by: "content-implementer"
created: "2026-02-09"
version: "2.0.0"
---

# Security Hardening & Least Privilege

In Lesson 7, you learned to process text and automate repetitive tasks with grep, sed, awk, and cron. Those tools are powerful -- and power without restraint is dangerous. Now you'll learn to lock down who can do what on your server.

Here is a scenario that happens more often than anyone admits: A developer deploys an AI agent as root because "it's just a test." The agent has a bug that deletes files it shouldn't. Since it runs as root, nothing stops it -- the agent wipes `/var/log`, taking down monitoring for every service on the server.

The fix is not better code. The fix is **least privilege** -- ensuring that even when code fails, the damage is contained. An agent running as a restricted user with access only to its own directory cannot touch system logs or modify other services. The bug still exists, but the blast radius shrinks from "entire server" to "one agent's workspace."

---

## What Went Wrong? A Security Incident

Before learning the defenses, examine this failure. A team deployed three AI agents on a shared server:

```bash
# How the agents were deployed (WRONG)
sudo python3 /opt/agents/log-reader/main.py &
sudo python3 /opt/agents/email-sender/main.py &
sudo python3 /opt/agents/backup-agent/main.py &
```

All three agents ran as root. The email-sender had an API key hardcoded in its script:

```bash
# Inside email-sender/main.py (WRONG)
API_KEY = "sk-prod-abc123def456"
```

**What went wrong**: A junior developer committed the script to a public GitHub repository. Within hours, automated scrapers found the API key. The attacker used the key to send spam through the email API, racking up charges. Since the agents ran as root, the attacker also exploited a vulnerability in the email-sender to read files belonging to the other two agents -- including the backup agent's database credentials.

**Three failures, three fixes**:

| Failure                              | Fix You'll Learn                     |
| ------------------------------------ | ------------------------------------ |
| All agents ran as root               | User/group management                |
| Agents could read each other's files | chmod/chown least privilege          |
| API key in source code               | Environment variables and .env files |

---

## Creating Dedicated Service Users

Your agents need their own identities on the system. A dedicated service user ensures the agent can only access what it needs.

### Creating a Service User with No Login Shell

```bash
sudo useradd --system --shell /usr/sbin/nologin --home-dir /opt/agent-runner --create-home agent-runner
```

**Output:**

```
(no output on success)
```

Verify the user was created:

```bash
id agent-runner
```

**Output:**

```
uid=998(agent-runner) gid=998(agent-runner) groups=998(agent-runner)
```

Check the passwd entry:

```bash
grep agent-runner /etc/passwd
```

**Output:**

```
agent-runner:x:998:998::/opt/agent-runner:/usr/sbin/nologin
```

**What each flag does**:

| Flag                           | Purpose                                                      |
| ------------------------------ | ------------------------------------------------------------ |
| `--system`                     | System account (UID below 1000, hidden from login screen)    |
| `--shell /usr/sbin/nologin`    | Prevents interactive login -- nobody can SSH in as this user |
| `--home-dir /opt/agent-runner` | Sets the home directory                                      |
| `--create-home`                | Creates the home directory if it doesn't exist               |

The `/usr/sbin/nologin` shell is the critical security decision. Even if someone obtains this user's credentials, they cannot open a terminal session.

### Adding Your Account to the Agent's Group

To manage agent files without switching users, add yourself to the agent's group:

```bash
sudo usermod -aG agent-runner $USER
groups $USER
```

**Output:**

```
yourname sudo agent-runner
```

You may need to log out and back in for group changes to take effect. Now files with group permissions for `agent-runner` are accessible without `sudo`.

---

## File Permissions: chmod and chown

Every file has three permission sets -- owner, group, and others -- each with read (`r`=4), write (`w`=2), and execute (`x`=1) bits. Add the values for numeric notation: `700` means owner gets 7 (read+write+execute), group gets 0, others get 0.

| Numeric | Symbolic    | Meaning                               |
| ------- | ----------- | ------------------------------------- |
| `700`   | `rwx------` | Owner full access, nobody else        |
| `600`   | `rw-------` | Owner read/write only                 |
| `755`   | `rwxr-xr-x` | Owner full, group/others read+execute |
| `640`   | `rw-r-----` | Owner read/write, group read only     |

### Setting Permissions on Agent Files

Create the agent's workspace and a configuration file:

```bash
sudo mkdir -p /opt/agent-runner/config
sudo touch /opt/agent-runner/config/settings.yaml
```

**Output:**

```
(no output on success)
```

Transfer ownership to the agent user:

```bash
sudo chown -R agent-runner:agent-runner /opt/agent-runner
```

**Output:**

```
(no output on success)
```

The `-R` flag applies ownership recursively to all files and subdirectories.

Now set permissions so only the agent user can read the config:

```bash
sudo chmod 600 /opt/agent-runner/config/settings.yaml
```

**Output:**

```
(no output on success)
```

Verify:

```bash
ls -la /opt/agent-runner/config/settings.yaml
```

**Output:**

```
-rw------- 1 agent-runner agent-runner 0 Feb  9 15:30 settings.yaml
```

**What `600` achieves**: Only `agent-runner` can read or write this file. Your personal account, other agents, and any other user on the system cannot access it -- unless they use `sudo`.

### Symbolic chmod (Targeted Changes)

Numeric notation sets all permissions at once. Symbolic notation modifies specific bits without resetting others:

```bash
# Add group read permission
sudo chmod g+r /opt/agent-runner/config/settings.yaml
ls -la /opt/agent-runner/config/settings.yaml
```

**Output:**

```
-rw-r----- 1 agent-runner agent-runner 0 Feb  9 15:30 settings.yaml
```

| Notation  | Meaning                          |
| --------- | -------------------------------- |
| `u+x`     | Add execute for **u**ser (owner) |
| `g+r`     | Add read for **g**roup           |
| `o-w`     | Remove write for **o**thers      |
| `u-x,g+r` | Combine multiple changes         |

### Permission Guidelines for Agent Deployments

| File Type         | Recommended    | Why                                                 |
| ----------------- | -------------- | --------------------------------------------------- |
| Agent scripts     | `700`          | Only the agent user can execute                     |
| Config files      | `600` or `640` | Secrets stay private; `640` lets group members read |
| Log directories   | `750`          | Agent writes, group can read for monitoring         |
| `.env` files      | `600`          | Contains secrets -- owner only                      |
| Public key files  | `644`          | Public keys are meant to be shared                  |
| Private key files | `600`          | Private keys must stay private                      |

---

## Generating SSH Key Pairs

SSH keys use asymmetric cryptography instead of passwords. A private key stays on your machine; its matching public key goes on servers you want to access. You'll configure SSH connections and `sshd_config` in Lesson 9 -- here you generate the key pair.

### Generating an Ed25519 Key Pair

```bash
ssh-keygen -t ed25519 -C "agent-deploy@mycompany.com"
```

**Output:**

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/yourname/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/yourname/.ssh/id_ed25519
Your public key has been saved in /home/yourname/.ssh/id_ed25519.pub
```

This creates two files: `~/.ssh/id_ed25519` (private key -- never share) and `~/.ssh/id_ed25519.pub` (public key -- place on servers).

:::danger Never Share Your Private Key

Your private key (`id_ed25519` without `.pub`) must never be copied, emailed, committed to git, or pasted into a chat. If exposed, an attacker can impersonate you on every server that trusts your public key. Generate a new pair immediately if you suspect compromise.

:::

### Verifying Key Permissions

SSH is strict about file permissions. If your private key is readable by others, SSH refuses to use it:

```bash
ls -la ~/.ssh/id_ed25519
```

**Output:**

```
-rw------- 1 yourname yourname 411 Feb  9 15:45 /home/yourname/.ssh/id_ed25519
```

The permissions must be `600` (owner read/write only). If they're wrong:

```bash
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

**Output:**

```
(no output on success)
```

You'll use these keys to connect to remote servers in Lesson 9, where you'll configure `sshd_config`, set up `authorized_keys`, and disable password authentication.

---

## Environment Variable Scoping

Environment variables are the standard mechanism for passing configuration and secrets to processes. But their visibility depends on how you define them -- and misunderstanding scoping is a common source of security bugs.

### Exported vs Non-Exported Variables

When you set a variable in the shell, it exists only in that shell by default:

```bash
MY_LOCAL="this stays here"
echo $MY_LOCAL
```

**Output:**

```
this stays here
```

But if you launch a subshell (a child process), that variable is invisible:

```bash
MY_LOCAL="this stays here"
bash -c 'echo "In subshell: [$MY_LOCAL]"'
```

**Output:**

```
In subshell: []
```

The subshell sees nothing. Now try with `export`:

```bash
export MY_EXPORT="this propagates"
bash -c 'echo "In subshell: [$MY_EXPORT]"'
```

**Output:**

```
In subshell: [this propagates]
```

`export` marks the variable for inheritance by child processes. Without `export`, the variable is local to the current shell.

### Why This Matters for Agent Deployment

When you run an agent script, the script runs in a subshell. If you set API keys without `export`, your agent cannot see them:

```bash
# WRONG: Agent won't see this
OPENAI_API_KEY="sk-abc123"
sudo -u agent-runner /opt/agent-runner/start.sh
# The script cannot access $OPENAI_API_KEY

# RIGHT: Agent inherits the variable
export OPENAI_API_KEY="sk-abc123"
sudo -u agent-runner --preserve-env=OPENAI_API_KEY /opt/agent-runner/start.sh
```

**Output:**

```
(depends on your script)
```

:::warning sudo Strips Environment Variables

By default, `sudo` removes most environment variables for security reasons. Use `--preserve-env=VAR_NAME` to pass specific variables through. Never use `sudo --preserve-env` (without specifying variables) in production -- it passes everything, including potentially sensitive shell state.

:::

**The rule**: If a child process needs a variable, `export` it. If a variable should stay private to the current shell, do not export it.

---

## Managing Secrets with .env Files

Hardcoded secrets in source code are a ticking time bomb. Environment variables solve the immediate problem, but typing `export API_KEY=...` in a terminal is temporary and error-prone. Production deployments use `.env` files.

### Creating a Secure .env File

```bash
sudo -u agent-runner bash -c 'cat > /opt/agent-runner/.env << EOF
# Agent configuration
OPENAI_API_KEY=sk-prod-abc123def456
AGENT_NAME=log-reader
LOG_LEVEL=info
DATA_DIR=/opt/agent-runner/data
EOF'
```

**Output:**

```
(no output on success)
```

Lock down the permissions immediately:

```bash
sudo chmod 600 /opt/agent-runner/.env
ls -la /opt/agent-runner/.env
```

**Output:**

```
-rw------- 1 agent-runner agent-runner 118 Feb  9 16:00 /opt/agent-runner/.env
```

Only `agent-runner` can read this file. No other user, no other agent, no web server process can access these secrets.

### Sourcing .env Files in Scripts

The `source` command reads a file and executes each line in the current shell, making the variables available. A production startup script combines sourcing with validation:

```bash
sudo -u agent-runner bash -c '
source /opt/agent-runner/.env
echo "Agent: $AGENT_NAME"
echo "Log level: $LOG_LEVEL"
echo "API key set: $([ -n "$OPENAI_API_KEY" ] && echo YES || echo NO)"
'
```

**Output:**

```
Agent: log-reader
Log level: info
API key set: YES
```

For scripts that spawn child processes (like Python agents), use `set -a` before sourcing to auto-export all variables, then `set +a` to stop:

```bash
set -a
source /opt/agent-runner/.env
set +a
# Now all .env variables are exported to child processes
```

**Output:**

```
(no output -- variables are now in the environment)
```

### Never Commit .env Files

:::danger .env Files Must Never Enter Version Control

If your project uses git, add `.env` to `.gitignore` immediately:

```bash
echo ".env" >> /opt/agent-runner/.gitignore
```

**Output:**

```
(no output on success)
```

Verify:

```bash
cat /opt/agent-runner/.gitignore
```

**Output:**

```
.env
```

If you accidentally commit a `.env` file containing real API keys, consider those keys compromised. Rotate them immediately -- removing the file from git history is not sufficient because the keys may already be cached or scraped.

:::

### Secret Rotation

API keys should be rotated periodically. With `.env` files, rotation is a one-line edit followed by a restart -- not a code change, commit, build, and deploy cycle:

1. Update the `.env` file with the new key
2. Restart the agent process (it re-reads `.env` on startup)
3. Revoke the old key from the API provider's dashboard

---

## Exercises

### Exercise 1: Create a Restricted Service User

**Task:** Create a user called `agent-runner` with no login shell, suitable for running an AI agent process.

```bash
sudo useradd --system --shell /usr/sbin/nologin --home-dir /opt/agent-runner --create-home agent-runner
```

**Verify:**

```bash
id agent-runner
```

**Expected output:**

```
uid=998(agent-runner) gid=998(agent-runner) groups=998(agent-runner)
```

```bash
grep agent-runner /etc/passwd
```

**Expected output:**

```
agent-runner:x:998:998::/opt/agent-runner:/usr/sbin/nologin
```

The UID may differ (any number below 1000 confirms a system account). The critical fields are the nologin shell and correct home directory.

### Exercise 2: Create a Locked-Down Config File

**Task:** Create a configuration file at `/opt/agent-runner/config.yaml` that is readable and writable only by `agent-runner` -- no group access, no other access.

```bash
sudo touch /opt/agent-runner/config.yaml
sudo chown agent-runner:agent-runner /opt/agent-runner/config.yaml
sudo chmod 600 /opt/agent-runner/config.yaml
```

**Verify:**

```bash
ls -la /opt/agent-runner/config.yaml
```

**Expected output:**

```
-rw------- 1 agent-runner agent-runner 0 Feb  9 16:30 config.yaml
```

Confirm that the permissions show `-rw-------` (600) and the owner is `agent-runner`.

### Exercise 3: Export vs Non-Export Variable Visibility

**Task:** Set two variables -- one exported, one not -- and verify which one is visible in a subshell.

```bash
export MY_EXPORT="visible_in_subshell"
MY_LOCAL="invisible_in_subshell"

bash -c 'echo "MY_EXPORT=[$MY_EXPORT]"; echo "MY_LOCAL=[$MY_LOCAL]"'
```

**Expected output:**

```
MY_EXPORT=[visible_in_subshell]
MY_LOCAL=[]
```

The exported variable propagates to the subshell. The non-exported variable does not. This is the exact behavior that determines whether your agent can access the API keys you set.

---

## Try With AI

**Designing a Minimum Permission Set:**

```
I'm deploying an AI agent that needs to read API keys and write to a
log directory. What's the minimum permission set this agent needs?
Assume it runs as user agent-runner. List the specific chmod values
for each file and directory, and explain why each permission is the
minimum necessary.
```

**What you're learning:** AI applies least-privilege analysis systematically, often suggesting restrictions you might skip for convenience. Compare its recommendations against the permission guidelines table from this lesson and see where they align or differ.

**Evaluating Non-Root Port Binding:**

```
The agent also needs to bind to port 8080, but I don't want it
running as root. What are my options? Compare the security
implications of each approach: setcap, reverse proxy with nginx,
and using a high port (>1024).
```

**What you're learning:** The trade-off between setcap, reverse proxy, and high ports has real security implications. Evaluate which approach AI recommends and whether its reasoning accounts for your specific deployment constraints.

**Auditing Your Permission Setup:**

```
Audit this permission setup I created. Here's my ls -la output for
/opt/agent-runner/:

total 20
drwxr-xr-x 3 agent-runner agent-runner 4096 Feb  9 16:00 .
drwxr-xr-x 5 root         root         4096 Feb  9 15:00 ..
-rw------- 1 agent-runner agent-runner  118 Feb  9 16:00 .env
-rwxrwxrwx 1 agent-runner agent-runner  245 Feb  9 16:00 start.sh
-rw-r--r-- 1 agent-runner agent-runner   45 Feb  9 16:00 config.yaml
drwxrwxrwx 2 agent-runner agent-runner 4096 Feb  9 16:00 logs

What security issues do you see? What chmod commands would fix them?
```

**What you're learning:** A security review from another perspective catches oversights in your setup. In this example, `start.sh` and `logs/` have overly permissive settings (`777`) that a fresh pair of eyes -- whether human or AI -- should flag immediately.
