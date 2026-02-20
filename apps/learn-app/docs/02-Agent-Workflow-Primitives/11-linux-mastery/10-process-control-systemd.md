---
sidebar_position: 10
chapter: 11
lesson: 10
title: "Lesson 10: Process Control & Systemd Services"
description: "Deploy AI agents as production systemd services with restart policies, start-limit protection, resource limits, and centralized logging."
keywords: ["systemd", "service", "daemon", "restart policy", "journalctl", "resource limits", "agent deployment", "production", "MemoryMax", "CPUQuota"]
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "systemd Service File Structure"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student writes a .service file with correct [Unit], [Service], and [Install] sections that passes systemd-analyze verify"

  - name: "Restart Policy Configuration"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student configures Restart=on-failure with start-limit protection and explains why Restart=always is problematic"

  - name: "Start-Limit Protection"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student configures StartLimitBurst and StartLimitIntervalSec to prevent restart storms and explains the math behind values"

  - name: "Service Lifecycle Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student uses systemctl start/stop/enable/disable/status to manage service lifecycle"

  - name: "Service Log Analysis"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student uses journalctl -u with -f and --since flags to monitor and search service logs"

  - name: "Resource Limit Configuration"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student sets MemoryMax and CPUQuota in a service file and verifies limits are applied with systemctl show"

learning_objectives:
  - objective: "Write a systemd .service file with correct [Unit], [Service], and [Install] section structure"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates a .service file for agent_main.py that passes systemd-analyze verify"

  - objective: "Configure restart policies (Restart=on-failure) with start-limit protection to prevent restart storms"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Student configures RestartSec, StartLimitBurst, and StartLimitIntervalSec and explains the interaction between these directives"

  - objective: "Monitor services using systemctl status and journalctl -u to diagnose operational issues"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student retrieves service status, follows live logs, and filters logs by time range"

  - objective: "Set resource limits (MemoryMax, CPUQuota) for agent processes to prevent resource exhaustion"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student adds resource limits to a service file and verifies they are applied using systemctl show"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "systemd service file structure ([Unit], [Service], [Install])"
    - "Restart policy (Restart=on-failure as correct production default)"
    - "Start-limit protection (StartLimitBurst, StartLimitIntervalSec, RestartSec)"
    - "Service lifecycle (systemctl start/stop/enable/disable/status)"
    - "Service logs (journalctl -u, -f for follow, --since for time ranges)"
    - "Resource limits (MemoryMax, CPUQuota in service file)"
  assessment: "6 concepts at B2 level (at the upper boundary of the 4-7 range). Progressive complexity: minimal service -> restart policy -> start-limit -> monitoring -> resource limits -> health check."

differentiation:
  extension_for_advanced: "Explore systemd timers for scheduled agent tasks, socket activation for on-demand starting, or Type=notify for advanced startup tracking with sd_notify."
  remedial_for_struggling: "Start with a minimal 5-line service file (no restart policy). Get systemctl start and status working before adding restart configuration. Use systemctl cat to see existing service files for reference."

teaching_guide:
  lesson_type: "core"
  session_group: 4
  session_title: "Production Agent Deployment"
  key_points:
    - "systemd replaces tmux for production — tmux is for interactive sessions, systemd is for services that must survive reboots and restart on failure automatically"
    - "Restart=on-failure (not Restart=always) is the correct production default — always-restart masks bugs by restarting infinitely without fixing the root cause"
    - "Start-limit protection (StartLimitBurst + StartLimitIntervalSec) prevents restart storms — without it, a crashing agent can consume all system resources through rapid restarts"
    - "Resource limits (MemoryMax, CPUQuota) contain runaway agents — a memory leak in one agent cannot take down the entire server"
  misconceptions:
    - "Students think Restart=always is safer than Restart=on-failure — always-restart hides bugs by endlessly restarting, while on-failure stops after too many crashes, forcing investigation"
    - "Students expect systemd to find their Python scripts without absolute paths — ExecStart must use the full path to the interpreter and script"
    - "Students confuse systemctl enable (start on boot) with systemctl start (start now) — enable does NOT start the service, it only configures boot behavior"
    - "Students think journalctl shows all logs — journalctl -u service-name filters to that specific service, which is what you almost always want"
  discussion_prompts:
    - "Your agent crashes and restarts 50 times per minute. What is worse: the agent being down, or the restart storm consuming all CPU and memory? How does start-limit protection solve this?"
    - "When would you choose tmux (lesson 5) over systemd for running an agent? What are the tradeoffs between interactive and service-managed deployment?"
  teaching_tips:
    - "Start with the minimal 5-line service file and progressively add restart policy, start-limit, and resource limits — each addition solves a specific production problem"
    - "Demo systemctl status live — the colored output showing active/failed/inactive is much more memorable than describing it"
    - "The restart policy comparison (always vs on-failure) is a whiteboard moment — draw the restart storm scenario to show why always-restart is dangerous"
    - "journalctl -u -f (follow mode) is the systemd equivalent of tail -f from lesson 2 — connecting these tools builds on prior knowledge"
  assessment_quick_check:
    - "Ask: what is the difference between systemctl start and systemctl enable? (Expected: start runs it now, enable configures it to start on boot)"
    - "Ask students to write the three-section structure of a .service file from memory ([Unit], [Service], [Install])"
    - "Ask: what does StartLimitBurst=5 with StartLimitIntervalSec=300 mean? (Expected: if the service fails 5 times within 300 seconds, stop trying to restart)"

teaching_approach: "Progressive complexity (minimal service -> restart policy -> start-limit -> resource limits -> health check)"
modality: "Hands-on discovery with AI collaboration"

# Generation metadata
generated_by: "content-implementer"
created: "2026-02-10"
version: "2.0.0"
---

# Process Control & Systemd Services

In Lesson 9, you learned to connect to remote servers with SSH and verify network connectivity with curl. Now you'll make your agent permanent -- a service that starts on boot, restarts after crashes, and runs under resource limits that prevent it from consuming your entire server.

Here is the reality of production agent deployment: servers reboot. Processes crash. Memory leaks accumulate. A Digital FTE that requires you to SSH in and manually restart it every time something goes wrong is not a production system -- it's a babysitting obligation. **systemd** transforms your agent from a fragile manual process into an unkillable system service managed by the operating system itself.

By the end of this lesson, you'll deploy the sample `agent_main.py` as a systemd service with automatic restart, crash protection, resource limits, and a canonical health check script that other lessons in this chapter reference.

---

## Deploying agent_main.py

Before creating a service, you need an agent to run. Throughout this chapter, we use a sample FastAPI agent. Let's get it onto the server.

Create the agent directory and file:

```bash
sudo mkdir -p /opt/agent
```

```bash
sudo nano /opt/agent/agent_main.py
```

Add this content:

```python
"""
Sample AI Agent for Linux Mastery Chapter
==========================================
A minimal FastAPI agent used throughout Chapter 11 to practice
deployment, monitoring, and management on Linux servers.

Requirements: pip install fastapi uvicorn
Run directly: uvicorn agent_main:app --host 0.0.0.0 --port 8000
"""

from datetime import datetime
from fastapi import FastAPI

app = FastAPI(
    title="Sample Digital FTE Agent",
    description="A minimal agent for practicing Linux deployment skills",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "agent": "running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/tasks")
def list_tasks():
    return {
        "tasks": [
            {"id": 1, "name": "Process customer inquiry", "status": "pending"},
            {"id": 2, "name": "Generate daily report", "status": "completed"},
            {"id": 3, "name": "Update knowledge base", "status": "in_progress"}
        ],
        "total": 3,
        "agent_uptime": "running since startup"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Install the dependencies and verify the agent starts:

```bash
pip install fastapi uvicorn
```

```bash
cd /opt/agent && uvicorn agent_main:app --host 0.0.0.0 --port 8000 &
curl -s http://localhost:8000/health
```

**Output:**
```json
{"status":"healthy","agent":"running","timestamp":"2026-02-10T14:00:01.234567"}
```

Stop the background process before continuing:

```bash
kill %1
```

**Output:**
```
[1]+  Terminated              uvicorn agent_main:app --host 0.0.0.0 --port 8000
```

The agent works. Now let's make it permanent.

---

## Your First systemd Service File

A systemd service file has three sections. Each section serves a distinct purpose.

Create the service file:

```bash
sudo nano /etc/systemd/system/my-agent.service
```

Add this minimal configuration:

```ini
[Unit]
Description=Sample Digital FTE Agent
After=network.target

[Service]
Type=simple
User=nobody
WorkingDirectory=/opt/agent
ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Each section controls a different aspect of the service:

| Section | Purpose | Key Directives |
|---------|---------|----------------|
| **[Unit]** | Identity and ordering | `Description` names the service. `After=network.target` ensures networking is available before starting. |
| **[Service]** | How to run the process | `Type=simple` means the process runs directly. `User=nobody` avoids running as root. `ExecStart` is the exact command. |
| **[Install]** | Boot integration | `WantedBy=multi-user.target` makes the service start during normal boot. |

### Why Restart=on-failure (Not Restart=always)

Notice we use `Restart=on-failure`, not `Restart=always`. This distinction matters:

- `Restart=on-failure` restarts the service only when it exits with a non-zero exit code (a crash). If you intentionally stop it with `systemctl stop`, it stays stopped.
- `Restart=always` restarts the service regardless of how it stopped -- including after you deliberately run `systemctl stop`. This means you cannot cleanly stop your own service without disabling it first.

For production agents, `Restart=on-failure` is the correct default. It gives you control: crashes get automatic recovery, but intentional stops stay stopped.

### Activate the Service

Tell systemd about the new service file:

```bash
sudo systemctl daemon-reload
```

**Output:**
```
(no output -- daemon-reload completes silently on success)
```

Start the service:

```bash
sudo systemctl start my-agent
```

**Output:**
```
(no output -- a silent start means success)
```

Check its status:

```bash
sudo systemctl status my-agent
```

**Output:**
```
● my-agent.service - Sample Digital FTE Agent
     Loaded: loaded (/etc/systemd/system/my-agent.service; disabled; preset: enabled)
     Active: active (running) since Mon 2026-02-10 14:05:30 UTC; 5s ago
   Main PID: 4521 (uvicorn)
      Tasks: 2 (limit: 4915)
     Memory: 52.3M
        CPU: 1.234s
     CGroup: /system.slice/my-agent.service
             └─4521 /usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000
```

Verify the agent responds:

```bash
curl -s http://localhost:8000/health | python3 -m json.tool
```

**Output:**
```json
{
    "status": "healthy",
    "agent": "running",
    "timestamp": "2026-02-10T14:05:35.678901"
}
```

Your agent is running as a system service.

---

## Service Lifecycle Commands

These five commands manage the full lifecycle of any systemd service:

```bash
# Start the service
sudo systemctl start my-agent

# Stop the service
sudo systemctl stop my-agent

# Enable start-on-boot
sudo systemctl enable my-agent

# Disable start-on-boot
sudo systemctl disable my-agent

# Check current status
sudo systemctl status my-agent
```

Enable the service now so it survives reboots:

```bash
sudo systemctl enable my-agent
```

**Output:**
```
Created symlink /etc/systemd/system/multi-user.target.wants/my-agent.service → /etc/systemd/system/my-agent.service.
```

Verify the enabled state:

```bash
systemctl is-enabled my-agent
```

**Output:**
```
enabled
```

| Command | When to Use |
|---------|-------------|
| `systemctl start` | Launch a stopped service |
| `systemctl stop` | Gracefully shut down a running service |
| `systemctl restart` | Stop and start (picks up config changes) |
| `systemctl enable` | Ensure service starts on boot |
| `systemctl disable` | Prevent service from starting on boot |
| `systemctl status` | See current state, PID, recent logs |
| `systemctl is-active` | Quick check: returns `active` or `inactive` |

---

## Start-Limit Protection

Restart policies alone are not enough. Consider what happens when an agent has a fatal bug -- it crashes immediately on startup, every time. Without protection, systemd restarts it endlessly, consuming CPU cycles in a tight loop of crash-restart-crash.

Start-limit protection solves this by allowing a maximum number of restarts within a time window.

Update the service file:

```bash
sudo nano /etc/systemd/system/my-agent.service
```

Add start-limit directives to the `[Service]` section:

```ini
[Unit]
Description=Sample Digital FTE Agent
After=network.target
StartLimitIntervalSec=60
StartLimitBurst=5

[Service]
Type=simple
User=nobody
WorkingDirectory=/opt/agent
ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Reload and restart:

```bash
sudo systemctl daemon-reload
sudo systemctl restart my-agent
```

**Output:**
```
(no output -- silent success)
```

Here is how the three directives work together:

| Directive | Value | Meaning |
|-----------|-------|---------|
| `RestartSec=5` | 5 seconds | Wait 5 seconds between restart attempts |
| `StartLimitBurst=5` | 5 attempts | Allow at most 5 starts... |
| `StartLimitIntervalSec=60` | 60 seconds | ...within a 60-second window |

**The math**: If the agent crashes 5 times within 60 seconds, systemd concludes it has a fatal bug and stops trying. The status changes to:

```
Active: failed (Result: start-limit-hit)
```

This is the correct behavior. A restart loop on a fatally broken agent wastes resources and floods logs. When you see `start-limit-hit`, investigate the root cause instead of endlessly restarting.

After fixing the bug, reset the failure counter and start again:

```bash
sudo systemctl reset-failed my-agent
sudo systemctl start my-agent
```

**Output:**
```
(no output -- counter reset and service restarted)
```

---

## Reading Service Logs with journalctl

systemd captures all output from your service (both stdout and stderr) in the system journal. The `journalctl` command reads it.

### View Recent Logs

```bash
sudo journalctl -u my-agent -n 20
```

**Output:**
```
Feb 10 14:05:30 server systemd[1]: Started Sample Digital FTE Agent.
Feb 10 14:05:31 server uvicorn[4521]: INFO:     Started server process [4521]
Feb 10 14:05:31 server uvicorn[4521]: INFO:     Waiting for application startup.
Feb 10 14:05:31 server uvicorn[4521]: INFO:     Application startup complete.
Feb 10 14:05:31 server uvicorn[4521]: INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Follow Logs in Real Time

```bash
sudo journalctl -u my-agent -f
```

**Output:**
```
Feb 10 14:10:00 server uvicorn[4521]: INFO:     192.168.1.5:42386 - "GET /health HTTP/1.1" 200
Feb 10 14:10:05 server uvicorn[4521]: INFO:     192.168.1.5:42388 - "GET /tasks HTTP/1.1" 200
```

Press `Ctrl+C` to stop following.

### Filter by Time Range

```bash
sudo journalctl -u my-agent --since "1 hour ago"
```

**Output:**
```
Feb 10 13:15:00 server systemd[1]: Started Sample Digital FTE Agent.
Feb 10 13:15:01 server uvicorn[4521]: INFO:     Application startup complete.
...
```

```bash
sudo journalctl -u my-agent --since "2026-02-10 14:00" --until "2026-02-10 14:10"
```

**Output:**
```
Feb 10 14:05:30 server systemd[1]: Started Sample Digital FTE Agent.
Feb 10 14:05:31 server uvicorn[4521]: INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Common journalctl Patterns

| Command | Purpose |
|---------|---------|
| `journalctl -u my-agent -n 50` | Last 50 lines |
| `journalctl -u my-agent -f` | Follow live (like `tail -f`) |
| `journalctl -u my-agent --since today` | Today's logs only |
| `journalctl -u my-agent --since "1 hour ago"` | Last hour |
| `journalctl -u my-agent -p err` | Only error-level messages |
| `journalctl -u my-agent -b` | Since last boot |

---

## Resource Limits

A production agent that leaks memory or spins the CPU can take down the entire server. systemd provides built-in resource limits through Linux cgroups -- no external monitoring tools needed.

Update the service file to add limits:

```bash
sudo nano /etc/systemd/system/my-agent.service
```

Add resource directives to `[Service]`:

```ini
[Unit]
Description=Sample Digital FTE Agent
After=network.target
StartLimitIntervalSec=60
StartLimitBurst=5

[Service]
Type=simple
User=nobody
WorkingDirectory=/opt/agent
ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5

# Resource limits
MemoryMax=512M
CPUQuota=25%

[Install]
WantedBy=multi-user.target
```

Reload and restart:

```bash
sudo systemctl daemon-reload
sudo systemctl restart my-agent
```

**Output:**
```
(no output -- silent success)
```

Verify the limits are applied:

```bash
systemctl show my-agent --property=MemoryMax,CPUQuota
```

**Output:**
```
MemoryMax=536870912
CPUQuota=25%
```

The `MemoryMax` value is in bytes (536870912 = 512 * 1024 * 1024 = 512 MB).

Check current resource consumption:

```bash
systemctl show my-agent --property=MemoryCurrent,CPUUsageNSec
```

**Output:**
```
MemoryCurrent=54857728
CPUUsageNSec=1234567890
```

That is approximately 52 MB of memory and 1.2 seconds of CPU time -- well within limits.

| Directive | What It Controls | Example |
|-----------|-----------------|---------|
| `MemoryMax=512M` | Hard memory ceiling. If exceeded, the process is killed with SIGKILL. | Prevents a memory leak from consuming all RAM. |
| `CPUQuota=25%` | Maximum CPU time as percentage of one core. `100%` = one full core. | Prevents a runaway computation from starving other services. |
| `TasksMax=256` | Maximum number of threads/processes the service can create. | Prevents fork bombs. |
| `LimitNOFILE=65536` | Maximum number of open file descriptors. | Needed for high-connection agents. |

:::warning Resource Limits Are Safety Nets

Set `MemoryMax` for every production agent. Without it, a slow memory leak will eventually consume all available RAM and crash the entire server -- not just your agent.

:::

---

## Agent Health Checks

Health checking is how you verify an agent is not just running but actually working. A service can be `active (running)` according to systemd while the application inside has deadlocked or stopped responding to requests.

This is the canonical agent health check script for this chapter. Other lessons reference it by link.

Create the script:

```bash
sudo nano /usr/local/bin/check-agent-health.sh
```

Add this content:

```bash
#!/bin/bash
# Canonical agent health check - referenced from other lessons
# Location: Taught in Lesson 10, section "Agent Health Checks"
set -euo pipefail

SERVICE_NAME="${1:?Usage: check-agent-health.sh <service-name>}"

check_service() {
    systemctl is-active --quiet "$SERVICE_NAME"
}

check_health_endpoint() {
    local port="${2:-8000}"
    curl -sf "http://localhost:${port}/health" > /dev/null 2>&1
}

check_resources() {
    local mem_usage
    mem_usage=$(systemctl show "$SERVICE_NAME" --property=MemoryCurrent --value)
    echo "Memory: ${mem_usage}"
}

main() {
    echo "=== Agent Health Check: $SERVICE_NAME ==="

    if check_service; then
        echo "[OK] Service is running"
    else
        echo "[FAIL] Service is not running"
        exit 1
    fi

    if check_health_endpoint; then
        echo "[OK] Health endpoint responding"
    else
        echo "[WARN] Health endpoint not responding"
    fi

    check_resources
    echo "=== Check complete ==="
}

main "$@"
```

Make it executable:

```bash
sudo chmod +x /usr/local/bin/check-agent-health.sh
```

**Output:**
```
(no output -- permissions set silently)
```

Run it:

```bash
check-agent-health.sh my-agent
```

**Output:**
```
=== Agent Health Check: my-agent ===
[OK] Service is running
[OK] Health endpoint responding
Memory: 54857728
=== Check complete ===
```

The script checks three things:

1. **Service state** -- Is systemd reporting the service as active?
2. **Health endpoint** -- Does the application respond to HTTP requests?
3. **Resource usage** -- How much memory is the service consuming?

This script builds directly on skills from earlier lessons: `set -euo pipefail` from Lesson 6, `curl` from Lesson 9, and `systemctl` from this lesson.

---

## The Complete Production Service File

Combining everything from this lesson, here is a production-ready service file:

```ini
[Unit]
Description=Sample Digital FTE Agent
After=network.target
StartLimitIntervalSec=60
StartLimitBurst=5

[Service]
Type=simple
User=nobody
WorkingDirectory=/opt/agent
ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000

# Restart policy
Restart=on-failure
RestartSec=5

# Resource limits
MemoryMax=512M
CPUQuota=25%

# Logging
StandardOutput=journal
StandardError=journal
SyslogIdentifier=my-agent

[Install]
WantedBy=multi-user.target
```

Every directive serves a purpose. There is no boilerplate here -- each line addresses a specific production concern.

---

## Exercises

### Exercise 1: Write a Minimal Service File

Write a `.service` file for `agent_main.py` with the three required sections. Include `Restart=on-failure` and `RestartSec=5`.

```bash
sudo nano /etc/systemd/system/my-agent.service
```

After writing the file, validate it:

```bash
systemd-analyze verify /etc/systemd/system/my-agent.service
```

**Expected output:**
```
(no output means no errors -- the file is valid)
```

If there are errors, the output will name the specific problem:

```
/etc/systemd/system/my-agent.service:7: Unknown key name 'Restartt' in section 'Service'
```

Fix any reported issues and verify again until the output is clean.

### Exercise 2: Check Status and View Logs

Start the service and verify it is running, then view the most recent log entries:

```bash
sudo systemctl daemon-reload
sudo systemctl start my-agent
sudo systemctl status my-agent
```

**Expected output (status):**
```
● my-agent.service - Sample Digital FTE Agent
     Active: active (running) since Mon 2026-02-10 ...
```

Now view the last 5 log entries:

```bash
journalctl -u my-agent --no-pager -n 5
```

**Expected output:**
```
Feb 10 14:05:30 server systemd[1]: Started Sample Digital FTE Agent.
Feb 10 14:05:31 server uvicorn[4521]: INFO:     Started server process [4521]
Feb 10 14:05:31 server uvicorn[4521]: INFO:     Waiting for application startup.
Feb 10 14:05:31 server uvicorn[4521]: INFO:     Application startup complete.
Feb 10 14:05:31 server uvicorn[4521]: INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Exercise 3: Add Resource Limits and Verify

Add `MemoryMax=512M` and `CPUQuota=25%` to the `[Service]` section, then verify the limits are applied:

```bash
sudo nano /etc/systemd/system/my-agent.service
```

After editing, reload and restart:

```bash
sudo systemctl daemon-reload
sudo systemctl restart my-agent
```

Verify:

```bash
systemctl show my-agent --property=MemoryMax
```

**Expected output:**
```
MemoryMax=536870912
```

The value 536870912 equals 512 MB in bytes. If you see `MemoryMax=infinity`, the directive was not applied -- check that it is in the `[Service]` section and re-run `daemon-reload`.

---

## Try With AI

**Design a resilient service file for a crash-prone agent:**

```
I have a FastAPI agent that crashes occasionally due to memory leaks.
Design a systemd service file that handles this gracefully -- automatic
restarts, but with protection against restart loops. Explain each
directive you include.
```

**What you're learning:** AI suggests protective mechanisms you might not know about (RestartSec, StartLimitBurst, StartLimitIntervalSec). When AI recommends a specific RestartSec value or burst count, ask why -- the reasoning behind the numbers teaches you how to size these values for your own agents.

**Translate specific constraints into systemd configuration:**

```
My agent needs exactly these constraints: max 512MB RAM, max 25% CPU,
restart on crash but stop after 5 failures in 60 seconds. Generate the
complete service file and explain the math behind the start-limit values.
```

**What you're learning:** You know what your agent needs; AI knows the directive syntax. This division of knowledge -- your operational requirements plus AI's systemd expertise -- produces a configuration faster and more correctly than either of you working alone. Pay attention to how AI translates "5 failures in 60 seconds" into the specific `StartLimitBurst` and `StartLimitIntervalSec` values.

**Get a production review of your service file:**

```
Review this service file I wrote for my production agent:
[paste your service file from Exercise 3]. What's missing?
What would you change for production reliability? Are there
any security improvements?
```

**What you're learning:** Multiple rounds of review progressively improve the service file. AI might suggest `ProtectSystem=strict` or `NoNewPrivileges=true` -- security hardening directives that are rarely covered in tutorials but standard in production. Each round catches issues you might miss on your own.

:::note Safety Reminder
Always test service configurations on a non-production server first. A misconfigured `ExecStart` path or wrong `User` will cause the service to fail silently. Use `systemctl status` and `journalctl -u` after every change to verify the service started correctly.
:::
