---
sidebar_position: 9
chapter: 11
lesson: 9
title: "Networking Fundamentals & SSH Remote Access"
description: "Understand ports, localhost vs 0.0.0.0 binding, test endpoints with curl, establish SSH connections with key-based authentication, configure ~/.ssh/config for multiple servers, and protect agent ports with ufw firewall rules."
keywords:
  [
    "networking",
    "ports",
    "localhost",
    "ssh",
    "curl",
    "ufw",
    "firewall",
    "ssh config",
    "remote access",
    "agent deployment",
    "0.0.0.0",
  ]
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "Port and Service Binding"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Communication and Collaboration"
    measurable_at_this_level: "Student can explain what a port number represents, distinguish well-known ports from ephemeral ports, and predict whether an agent will be reachable based on its binding address"

  - name: "Localhost vs Network Interface Binding"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Communication and Collaboration"
    measurable_at_this_level: "Student can diagnose whether an agent is unreachable due to binding to 127.0.0.1 instead of 0.0.0.0 and explain the security implications of each"

  - name: "HTTP Endpoint Testing with curl"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication and Collaboration"
    measurable_at_this_level: "Student can use curl to send GET and POST requests, inspect HTTP status codes, and verify agent health endpoints"

  - name: "SSH Connection Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can establish SSH connections using key-based authentication and configure sshd_config safely without lockout"

  - name: "SSH Config for Multiple Servers"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication and Collaboration"
    measurable_at_this_level: "Student can write ~/.ssh/config entries with Host aliases, custom ports, identity files, and user fields"

  - name: "Firewall Management with ufw"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can enable ufw, allow specific ports, deny access, check status, and explain why default-deny protects agent services"

learning_objectives:
  - objective: "Explain ports, localhost vs 0.0.0.0, and why binding address matters for agents"
    proficiency_level: "B2"
    bloom_level: "Understand"
    assessment_method: "Student predicts whether an agent bound to 127.0.0.1:8000 is reachable from another machine and explains why"

  - objective: "Use curl to test HTTP endpoints locally"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student uses curl to send a GET request to localhost:8000/health and interprets the HTTP status code"

  - objective: "Establish SSH connections and configure ~/.ssh/config for multiple servers"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates an SSH config entry with a Host alias and connects using the alias instead of the full hostname"

  - objective: "Configure basic firewall rules with ufw"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student enables ufw, allows SSH (port 22) and their agent port, denies everything else, and verifies with ufw status"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "Ports and services (what port 8000 means, well-known ports, agent binding)"
    - "localhost vs 0.0.0.0 (loopback vs all interfaces, security implications)"
    - "curl for HTTP testing (GET, POST, checking agent health endpoints)"
    - "SSH connection (ssh user@host, key-based auth)"
    - "SSH config file (~/.ssh/config for multiple server aliases)"
    - "Basic firewall with ufw (allow/deny/status, protecting agent ports)"
  assessment: "6 concepts at B2 level (within 7-10 limit). Concepts follow a diagnostic progression: binding -> testing -> connecting -> securing."

differentiation:
  extension_for_advanced: "Explore SSH tunneling for forwarding agent ports through firewalls (ssh -L). Investigate fail2ban for automatic IP banning after failed SSH attempts. Research iptables for fine-grained firewall rules beyond ufw's abstraction."
  remedial_for_struggling: "Focus on curl and SSH connection first. Practice curl against a known endpoint until comfortable reading status codes. Master basic ssh user@host before attempting SSH config. Skip ufw until SSH is solid."

teaching_guide:
  lesson_type: "core"
  session_group: 3
  session_title: "Text Processing and Automation"
  key_points:
    - "localhost (127.0.0.1) vs 0.0.0.0 binding is the #1 reason agents are unreachable — binding to localhost means only the same machine can connect"
    - "curl is the essential diagnostic tool for agent health checks — curl localhost:8000/health is the first command when debugging a deployed agent"
    - "SSH key-based auth (generated in lesson 8) replaces passwords — ~/.ssh/config aliases simplify managing multiple agent servers"
    - "ufw default-deny policy means only explicitly allowed ports are open — this is the firewall foundation for protecting agent services"
  misconceptions:
    - "Students think 127.0.0.1 and 0.0.0.0 are the same — 127.0.0.1 is loopback (local only), 0.0.0.0 binds to all network interfaces (reachable from outside)"
    - "Students expect agents to be reachable without opening firewall ports — ufw blocks everything by default, so agent ports must be explicitly allowed"
    - "Students confuse SSH config Host aliases with actual hostnames — the alias is a shortcut you define, the HostName field is the real server address"
  discussion_prompts:
    - "Your agent is running on port 8000 but your client cannot connect from another machine. Walk through the diagnostic steps: is the agent running, what address is it bound to, is the firewall blocking?"
    - "Why would you bind an agent to 127.0.0.1 during development but 0.0.0.0 in production (behind a reverse proxy)? What are the security implications?"
  teaching_tips:
    - "Start with the 'can I reach my agent?' question and build diagnostic layers — this matches how students will actually troubleshoot in practice"
    - "Demo curl against a real endpoint (even a simple Python HTTP server) — seeing HTTP status codes and JSON responses makes networking concrete"
    - "The SSH config file is a productivity win — show students connecting with 'ssh agent-prod' instead of typing full user@host:port every time"
    - "Demo ufw status before and after enabling — seeing the default-deny policy in action is more memorable than describing it"
  assessment_quick_check:
    - "Ask: an agent is bound to 127.0.0.1:8000. Can a user on another machine connect? (Expected: no, because 127.0.0.1 is loopback only)"
    - "Ask students to write a curl command that sends a GET request to localhost:8000/health and checks the status code"
    - "Ask: after enabling ufw, what is the default policy for incoming traffic? (Expected: deny — all ports are blocked unless explicitly allowed)"

teaching_approach: "Layered discovery -- start from 'can I reach my agent?' and build diagnostic layers."
modality: "Layered discovery with progressive diagnostic depth"

# Generation metadata
generated_by: "content-implementer"
created: "2026-02-09"
version: "1.0.0"
---

# Networking Fundamentals & SSH Remote Access

In Lesson 8, you locked down your server with dedicated users, restrictive permissions, and SSH keys. Your agent is secure -- but secure from everyone, including you, if you cannot reach it across a network. Security without connectivity is a locked room with no door.

Here is a scenario that every agent deployer encounters: You deploy an AI agent on a cloud server. It starts successfully. You check the logs -- everything looks clean. Then you open your browser to test the health endpoint and get "connection refused." You try from the command line -- same result. The agent is running. The server is on. But nothing can reach it. What went wrong?

The answer is almost always one of three things: the agent is bound to the wrong address, a firewall is blocking the port, or you are connecting to the wrong port entirely. This lesson gives you the diagnostic toolkit to identify and fix each of these problems, establish secure remote connections with SSH, and protect your agent ports with a firewall.

---

## Ports and Services: What Port 8000 Means

A port is a numbered endpoint on a machine that identifies a specific service. When your agent listens on port 8000, it is saying: "Send requests to this machine on door number 8000, and I will answer." Ports range from 0 to 65535, and some numbers are reserved by convention.

### Well-Known Ports

The Internet Assigned Numbers Authority (IANA) maintains a registry of port assignments. The most important ones for agent deployment:

| Port | Service    | Why You Care                     |
| ---- | ---------- | -------------------------------- |
| 22   | SSH        | Remote access to your server     |
| 80   | HTTP       | Unencrypted web traffic          |
| 443  | HTTPS      | Encrypted web traffic            |
| 5432 | PostgreSQL | Database your agent may use      |
| 8000 | Convention | Common for Python/FastAPI agents |
| 8080 | Convention | Alternative HTTP port            |

Ports 0-1023 are "well-known" and require root privileges to bind. Ports 1024-49151 are "registered" and available to any user. This is why your agent uses port 8000 instead of port 80 -- binding to 8000 does not require root access, which aligns with the least-privilege principle from Lesson 8.

### Checking What is Listening

Use `ss` (socket statistics) to see which ports have active listeners:

```bash
ss -tlnp
```

**Output:**

```
State    Recv-Q   Send-Q     Local Address:Port     Peer Address:Port  Process
LISTEN   0        128              0.0.0.0:22            0.0.0.0:*      users:(("sshd",pid=892,fd=3))
LISTEN   0        5              127.0.0.1:8000          0.0.0.0:*      users:(("python3",pid=1234,fd=5))
```

Each line shows a listening service. The flags mean:

| Flag | Purpose                                              |
| ---- | ---------------------------------------------------- |
| `-t` | TCP connections only                                 |
| `-l` | Listening sockets only (not established connections) |
| `-n` | Show port numbers instead of service names           |
| `-p` | Show the process using each port                     |

The output above reveals two services: SSH listening on port 22 (accessible from anywhere, `0.0.0.0`) and a Python agent on port 8000 (accessible only from localhost, `127.0.0.1`). That distinction is the next concept.

---

## Localhost vs 0.0.0.0: The Binding Address

The **binding address** determines who can reach your service. This single configuration choice is the most common reason agents are unreachable from other machines.

### 127.0.0.1 (localhost): Loopback Only

When a service binds to `127.0.0.1` (also called `localhost`), it only accepts connections from the same machine:

```bash
# This agent is ONLY reachable from the server itself
python3 -m http.server 8000 --bind 127.0.0.1 &
curl http://127.0.0.1:8000/
```

**Output:**

```
Serving HTTP on 127.0.0.1 port 8000 (http://127.0.0.1:8000/) ...
<!DOCTYPE HTML>
<html lang="en">
<head>...
```

The request succeeds because you are on the same machine. But from your laptop or any other machine, this agent is invisible.

### 0.0.0.0: All Network Interfaces

When a service binds to `0.0.0.0`, it accepts connections from every network interface -- localhost, LAN, and the internet:

```bash
# Stop the previous server
kill %1 2>/dev/null

# This agent is reachable from anywhere
python3 -m http.server 8000 --bind 0.0.0.0 &
curl http://127.0.0.1:8000/
```

**Output:**

```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
<!DOCTYPE HTML>
<html lang="en">
<head>...
```

Now the same agent is reachable from other machines on the network (assuming no firewall blocks it).

### When to Use Each

| Binding     | Use When                                                                    | Security                                |
| ----------- | --------------------------------------------------------------------------- | --------------------------------------- |
| `127.0.0.1` | Agent should only be accessed locally (development, internal-only services) | Safest -- nothing external can reach it |
| `0.0.0.0`   | Agent must be accessible from other machines (production, remote clients)   | Requires firewall protection            |

:::tip Agent Framework Defaults
Many web frameworks default to `127.0.0.1` for safety. When deploying to production, you must explicitly set the binding address. For FastAPI with uvicorn: `uvicorn main:app --host 0.0.0.0 --port 8000`. For Flask: `flask run --host 0.0.0.0`.
:::

:::note WSL2 Users
WSL2 networking is more complex than native Linux. WSL2 runs in a virtual machine with its own network interface. To access a service running inside WSL2 from Windows, you typically use `localhost` -- WSL2 handles the forwarding automatically on recent Windows versions. If that does not work, check your WSL2 IP with `ip addr show eth0` and use that address instead.
:::

### Cleaning Up the Test Server

```bash
kill %1 2>/dev/null
```

**Output:**

```
[1]+  Terminated              python3 -m http.server 8000 --bind 0.0.0.0
```

---

## Testing Endpoints with curl

`curl` is the command-line tool for making HTTP requests. Think of it as a browser that runs in the terminal and shows you exactly what the server returns -- no rendering, no JavaScript, just raw HTTP.

### Basic GET Request

```bash
curl http://localhost:8000/
```

**Output:**

```
<!DOCTYPE HTML>
<html lang="en">
<head>
<title>Directory listing for /</title>
</head>
...
```

If the agent is not running, you get a clear error:

```bash
curl http://localhost:8000/
```

**Output:**

```
curl: (7) Failed to connect to localhost port 8000 after 0 ms: Connection refused
```

"Connection refused" means nothing is listening on that port. This is different from a timeout (something is blocking the connection) or a 404 (something is listening but does not have the requested resource).

### Checking HTTP Status Codes

The `-o /dev/null -s -w` flags let you extract just the status code:

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/
```

**Output:**

```
200
```

| Status Code | Meaning           | Action                            |
| ----------- | ----------------- | --------------------------------- |
| `200`       | Success           | Agent is healthy                  |
| `404`       | Not found         | Endpoint path is wrong            |
| `500`       | Server error      | Agent crashed or has a bug        |
| `000`       | Connection failed | Nothing is listening on that port |

### Sending POST Requests

Agent APIs often accept POST requests with JSON data:

```bash
curl -X POST http://localhost:8000/api/process \
  -H "Content-Type: application/json" \
  -d '{"task": "analyze", "input": "test data"}'
```

**Output:**

```
{"status": "processed", "result": "analysis complete"}
```

The flags:

| Flag       | Purpose                        |
| ---------- | ------------------------------ |
| `-X POST`  | Use POST method instead of GET |
| `-H "..."` | Set a request header           |
| `-d '...'` | Send data in the request body  |

### Verbose Mode for Debugging

When something is not working and you need to see the full HTTP conversation:

```bash
curl -v http://localhost:8000/health
```

**Output:**

```
*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /health HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.81.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/json
< Content-Length: 15
<
{"status":"ok"}
```

Lines starting with `>` are what you sent. Lines starting with `<` are what the server returned. Lines starting with `*` are curl's own connection status.

---

## SSH Connections: Reaching Your Server

SSH (Secure Shell) is the standard protocol for connecting to remote Linux servers. In Lesson 8, you generated an SSH key pair. Now you will use those keys to connect to a server.

### Basic SSH Connection

```bash
ssh yourname@192.168.1.100
```

**Output:**

```
The authenticity of host '192.168.1.100 (192.168.1.100)' can't be established.
ED25519 key fingerprint is SHA256:abc123def456...
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.1.100' (ED25519) to the list of known hosts.
yourname@server:~$
```

The first time you connect to a server, SSH asks you to verify its fingerprint. This prevents man-in-the-middle attacks. After accepting, the fingerprint is saved in `~/.ssh/known_hosts` and SSH will not ask again.

### Key-Based Authentication

If your public key is already on the server (in `~/.ssh/authorized_keys`), SSH authenticates automatically without a password. To copy your key to a server:

```bash
ssh-copy-id yourname@192.168.1.100
```

**Output:**

```
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/yourname/.ssh/id_ed25519.pub"
Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'yourname@192.168.1.100'"
and check to make sure that only the key(s) you wanted were added.
```

After this, future connections use your key instead of a password:

```bash
ssh yourname@192.168.1.100
```

**Output:**

```
yourname@server:~$
```

No password prompt -- the key handled authentication silently.

### Specifying a Port or Key File

If SSH runs on a non-standard port or you have multiple keys:

```bash
ssh -p 2222 -i ~/.ssh/agent-deploy-key yourname@192.168.1.100
```

**Output:**

```
yourname@server:~$
```

| Flag                         | Purpose                                    |
| ---------------------------- | ------------------------------------------ |
| `-p 2222`                    | Connect to port 2222 instead of default 22 |
| `-i ~/.ssh/agent-deploy-key` | Use a specific private key file            |

---

## SSH Config: Managing Multiple Servers

Typing `ssh -p 2222 -i ~/.ssh/agent-deploy-key yourname@192.168.1.100` every time is tedious and error-prone. The SSH config file lets you create aliases.

### Creating Your SSH Config

```bash
nano ~/.ssh/config
```

Add entries for each server:

```
Host agent-prod
    HostName 192.168.1.100
    User deploy
    Port 2222
    IdentityFile ~/.ssh/agent-deploy-key

Host agent-staging
    HostName 10.0.0.50
    User deploy
    Port 22
    IdentityFile ~/.ssh/id_ed25519

Host db-server
    HostName 10.0.0.51
    User dbadmin
    IdentityFile ~/.ssh/db-key
```

Save and exit (`Ctrl+O`, Enter, `Ctrl+X`).

### Set Correct Permissions

SSH refuses to use a config file with loose permissions:

```bash
chmod 600 ~/.ssh/config
```

**Output:**

```
(no output on success)
```

### Connect Using Aliases

Now instead of the full command, use the alias:

```bash
ssh agent-prod
```

**Output:**

```
deploy@agent-prod:~$
```

SSH reads the config file, finds the `agent-prod` entry, and fills in the hostname, user, port, and key automatically.

### Verify Your Config

```bash
grep -c "Host " ~/.ssh/config
```

**Output:**

```
3
```

Three server entries configured. You can add as many as you need -- production servers, staging environments, database hosts, CI/CD runners.

---

## Hardening SSH on Your Server

Once key authentication works, disable password login to prevent brute-force attacks. This is a safety-critical change that requires careful sequencing.

:::warning SSH Lockout Prevention Protocol

**ALWAYS keep a backup session open when modifying sshd_config.** If you misconfigure SSH and close your only connection, you are locked out of the server. Follow these steps in exact order:

1. Open **two** SSH sessions to the server
2. In session 1, make sshd_config changes
3. In session 1, restart SSH and test
4. In session 2, verify you can still connect with a **new** connection
5. Only after session 2 confirms access, close session 1

If session 2 cannot connect, use session 1 (which is still open) to revert your changes.
:::

### Step 1: Verify Key Authentication Works First

Before disabling passwords, confirm key login succeeds:

```bash
ssh -o PasswordAuthentication=no yourname@your-server
```

**Output:**

```
yourname@server:~$
```

If this fails with "Permission denied (publickey)", your key is not properly configured. Fix key authentication before proceeding -- disabling passwords now would lock you out.

### Step 2: Edit sshd_config (In Session 1)

```bash
sudo nano /etc/ssh/sshd_config
```

Find and change these settings:

```
PasswordAuthentication no
PermitRootLogin no
PubkeyAuthentication yes
```

**Output:**

```
(nano editor with changes applied)
```

| Setting                     | Value                   | Why                                      |
| --------------------------- | ----------------------- | ---------------------------------------- |
| `PasswordAuthentication no` | Disables password login | Prevents brute-force attacks             |
| `PermitRootLogin no`        | Blocks direct root SSH  | Forces use of sudo from regular accounts |
| `PubkeyAuthentication yes`  | Enables key-based auth  | Should already be yes by default         |

### Step 3: Test Configuration Before Restarting

```bash
sudo sshd -t
```

**Output:**

```
(no output means configuration is valid)
```

If there is a syntax error, sshd -t will report it. Fix any errors before restarting.

### Step 4: Restart SSH Service

```bash
sudo systemctl restart sshd
```

**Output:**

```
(no output on success)
```

### Step 5: Verify from Session 2

In your **second** SSH session (the backup), open a new connection:

```bash
ssh yourname@your-server
```

**Output:**

```
yourname@server:~$
```

If this works, your configuration is correct. If it fails, use session 1 to revert the sshd_config changes and restart sshd again.

---

## Basic Firewall with ufw

`ufw` (Uncomplicated Firewall) is Ubuntu's front-end for the kernel's netfilter firewall. It follows a simple model: set a default policy, then add exceptions.

### Install and Check Status

```bash
sudo apt install -y ufw
sudo ufw status
```

**Output:**

```
Status: inactive
```

The firewall is installed but not active. Before enabling it, you must allow SSH -- otherwise enabling the firewall will immediately cut off your remote session.

### Allow SSH Before Enabling

```bash
sudo ufw allow 22/tcp
```

**Output:**

```
Rules updated
Rules updated (v6)
```

### Allow Your Agent Port

```bash
sudo ufw allow 8000/tcp
```

**Output:**

```
Rules updated
Rules updated (v6)
```

### Set Default Deny and Enable

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
```

**Output:**

```
Default incoming policy changed to 'deny'
Default outgoing policy changed to 'allow'
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
```

The default policy is **deny incoming** -- all ports are blocked unless explicitly allowed. Outgoing connections (your server reaching out to APIs, package repos) are allowed.

### Check Your Rules

```bash
sudo ufw status numbered
```

**Output:**

```
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    Anywhere
[ 2] 8000/tcp                   ALLOW IN    Anywhere
[ 3] 22/tcp (v6)                ALLOW IN    Anywhere (v6)
[ 4] 8000/tcp (v6)              ALLOW IN    Anywhere (v6)
```

Two ports are open: 22 (SSH) and 8000 (your agent). Everything else is blocked.

### Removing a Rule

If you need to close a port:

```bash
sudo ufw delete allow 8000/tcp
```

**Output:**

```
Rule deleted
Rule deleted (v6)
```

### Denying a Specific IP

If you see suspicious access attempts:

```bash
sudo ufw deny from 203.0.113.50
```

**Output:**

```
Rule added
```

:::warning Always Allow SSH First
If you enable ufw without allowing port 22, you will immediately lose SSH access to your server. Always run `sudo ufw allow 22/tcp` before `sudo ufw enable`. If you make this mistake on a cloud server, you may need to use your provider's console access to fix it.
:::

---

## Putting It All Together: Diagnostic Checklist

When your agent is unreachable, work through this diagnostic sequence:

| Step                         | Command                             | What It Tells You                                        |
| ---------------------------- | ----------------------------------- | -------------------------------------------------------- |
| 1. Is it running?            | `ss -tlnp \| grep 8000`             | Whether anything is listening on the port                |
| 2. What address?             | Check the `Local Address` column    | `127.0.0.1` = local only, `0.0.0.0` = network accessible |
| 3. Can I reach it locally?   | `curl http://localhost:8000/health` | Whether the agent responds at all                        |
| 4. Is the firewall blocking? | `sudo ufw status`                   | Whether the port is allowed through                      |
| 5. Can I reach it remotely?  | `curl http://server-ip:8000/health` | Whether end-to-end connectivity works                    |

This sequence moves from inside-out: first check the agent itself, then check network accessibility. Most problems are caught at step 1 or step 2.

---

## Exercises

### Exercise 1: Test Port Connectivity with curl

**Task:** Use curl to check whether anything is listening on port 8000 locally.

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8000
```

**Expected output (if nothing is running):**

```
000
```

**Expected output (if an agent is listening):**

```
200
```

A status code of `000` means nothing is listening. `200` means a healthy response. Any other code (404, 500) means something is listening but not responding as expected.

### Exercise 2: Generate and Display SSH Keys

**Task:** If you already generated SSH keys in Lesson 8, verify they exist. If not, generate a new pair and display the public key.

```bash
ls ~/.ssh/id_ed25519* 2>/dev/null || ssh-keygen -t ed25519 -C "agent-deploy@mycompany.com" -N "" -f ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

**Verify:**

```bash
ls ~/.ssh/id_ed25519*
```

**Expected output:**

```
/home/yourname/.ssh/id_ed25519
/home/yourname/.ssh/id_ed25519.pub
```

Both files present: private key (no extension) and public key (`.pub`).

### Exercise 3: Create an SSH Config Entry

**Task:** Create an SSH config entry with a server alias.

```bash
mkdir -p ~/.ssh
touch ~/.ssh/config
chmod 600 ~/.ssh/config

cat >> ~/.ssh/config << 'EOF'
Host my-agent-server
    HostName 192.168.1.100
    User deploy
    IdentityFile ~/.ssh/id_ed25519
EOF
```

**Output:**

```
(no output on success)
```

**Verify:**

```bash
grep -c "Host " ~/.ssh/config
```

**Expected output:**

```
1
```

One host entry confirmed. Add more entries as you set up additional servers.

---

## Try With AI

**Diagnosing a Connection Problem:**

```
My AI agent is running on port 8000 but I can only reach it from
the server itself, not from my laptop. Walk me through the
diagnostic steps to figure out why.
```

**What you're learning:** AI walks you through a systematic networking diagnostic: first checking the binding address (is it 127.0.0.1 or 0.0.0.0?), then checking the firewall (is port 8000 allowed?), then checking routing (is there a NAT or proxy in the way?). This layered approach is how experienced system administrators diagnose connectivity problems -- starting from the service and working outward through each network layer.

**Building Your SSH Config:**

```
I have 5 servers I SSH into regularly. Here are their details:
- Production API: api.mycompany.com, user: deploy, port 2222, key: ~/.ssh/prod-key
- Staging: staging.mycompany.com, user: deploy, port 22, key: ~/.ssh/id_ed25519
- Database: db.internal.mycompany.com, user: dbadmin, key: ~/.ssh/db-key
- CI Runner: 10.0.0.200, user: ci, port 22, key: ~/.ssh/ci-key
- Dev sandbox: dev.mycompany.com, user: myname, key: ~/.ssh/id_ed25519

Generate my complete ~/.ssh/config file with short aliases.
```

**What you're learning:** Translating your specific infrastructure into SSH configuration is a task where AI collaboration saves significant time. You provide the domain knowledge (your servers, users, keys), AI handles the formatting. Review the output to verify the syntax matches what you learned in this lesson -- the Host, HostName, User, Port, and IdentityFile fields.

**Locking Down SSH Safely:**

```
I want to lock down SSH on my agent server. Walk me through the
changes to sshd_config step by step, but make sure I don't lock
myself out. I want to:
1. Disable password authentication
2. Disable root login
3. Limit SSH to specific users
Include a rollback plan for each step in case something goes wrong.
```

**What you're learning:** Safety-critical configuration changes benefit from step-by-step collaboration where each change is verified before proceeding to the next. AI provides the sequence and rollback commands, but you execute and verify each step -- this is the pattern for all security-sensitive system changes: change one thing, test, confirm, then proceed.
