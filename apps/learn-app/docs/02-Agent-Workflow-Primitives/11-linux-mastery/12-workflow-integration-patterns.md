---
sidebar_position: 12
chapter: 11
lesson: 12
title: "Lesson 12: Advanced Workflow Integration Patterns"
description: "Combine scripting, systemd, security, and monitoring into integrated deployment workflows with blue-green patterns, log rotation, and disk alerts."
keywords: ["deployment patterns", "blue-green deployment", "log rotation", "monitoring", "zero-downtime", "rollback", "logrotate", "disk alerts", "cron", "production workflow"]
duration_minutes: 65

# HIDDEN SKILLS METADATA
skills:
  - name: "Multi-Step Deployment Workflows"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student designs and implements a complete deployment workflow combining user creation, service installation, health verification, and rollback capability"

  - name: "Blue-Green Deployment Pattern"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student implements a blue-green deployment with dual systemd services, health check gating, and traffic switching"

  - name: "Basic Monitoring Setup"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student configures log rotation with logrotate, writes a disk space alert script, and schedules health checks with cron"

  - name: "Deployment Pattern Selection"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student compares restart, blue-green, and rolling deployment strategies and justifies selection for a given scenario with trade-off analysis"

  - name: "Docker Awareness"
    proficiency_level: "C1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Information and Data Literacy"
    measurable_at_this_level: "Student articulates when systemd-based deployment is sufficient and when container-based deployment adds value, without needing to use Docker yet"

learning_objectives:
  - objective: "Evaluate deployment patterns (restart vs blue-green vs rolling) and justify selection for specific scenarios"
    proficiency_level: "C1"
    bloom_level: "Evaluate"
    assessment_method: "Student analyzes a deployment scenario and produces a written justification selecting one of three patterns with trade-off analysis"

  - objective: "Design a monitoring setup combining log rotation, disk alerts, and health checks"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Student configures logrotate, writes a disk alert script, and schedules health checks via cron on a server"

  - objective: "Implement a multi-step deployment workflow combining scripting, systemd, and monitoring"
    proficiency_level: "C1"
    bloom_level: "Apply"
    assessment_method: "Student runs a deployment script that creates a user, installs a service, starts the agent, and verifies health — all in one automated pass"

  - objective: "Compare systemd-based deployment with container-based approaches (Docker awareness)"
    proficiency_level: "C1"
    bloom_level: "Analyze"
    assessment_method: "Student writes a short comparison explaining when systemd is sufficient and when Docker adds value for agent deployment"

cognitive_load:
  new_concepts: 5
  concepts_list:
    - "Multi-step deployment workflows (combining script + systemd + security)"
    - "Blue-green deployment pattern (zero-downtime updates with dual services)"
    - "Basic monitoring setup (log rotation + disk alerts + health check scheduling)"
    - "Deployment pattern selection (restart vs blue-green vs rolling — trade-off analysis)"
    - "Docker awareness (systemd vs Docker comparison, why Docker is deferred)"
  assessment: "5 concepts at C1 level (within the 4-7 range). Progressive complexity: pattern comparison -> blue-green implementation -> monitoring integration -> full workflow -> Docker context."

differentiation:
  extension_for_advanced: "Add a rolling deployment pattern that updates multiple agent instances one at a time with automatic rollback, or integrate Prometheus node_exporter for metric collection alongside the bash-based monitoring."
  remedial_for_struggling: "Start with just the simple restart pattern and one logrotate config. Get those working before attempting blue-green deployment. Use the health check script from Lesson 10 without modification."

teaching_guide:
  lesson_type: "core"
  session_group: 4
  session_title: "Production Agent Deployment"
  key_points:
    - "Blue-green deployment achieves zero downtime by running two instances and switching traffic after health check passes — this is the key pattern for production agent updates"
    - "The three deployment patterns (restart, blue-green, rolling) have clear trade-offs in downtime, complexity, and resource cost — students must justify their choice for each scenario"
    - "Monitoring (log rotation + disk alerts + health checks via cron) is not optional — it is what keeps deployed agents running after the initial deployment"
    - "Docker awareness at this stage means understanding when systemd is sufficient (single server, few agents) versus when containers add value (multi-server, reproducibility) — Docker itself is deferred"
  misconceptions:
    - "Students think blue-green requires containers or Kubernetes — this lesson implements it with two systemd services and a symlink switch, proving it works with basic Linux tools"
    - "Students assume logrotate is only for syslog — logrotate works on any log file you configure, including agent-specific logs in custom directories"
    - "Students think deployment scripts are run once and forgotten — production deployment must be idempotent (safe to re-run) because you will deploy updates repeatedly"
  discussion_prompts:
    - "Your agent serves paying customers. You need to deploy an update. Compare restart deployment (30 seconds downtime) versus blue-green (zero downtime) — when is 30 seconds acceptable?"
    - "Why is monitoring a deployment concern and not just an operations concern? What happens if you deploy without health checks or disk alerts?"
  teaching_tips:
    - "Start with the pattern comparison table — students should understand the trade-offs before implementing any specific pattern"
    - "Demo the blue-green switch live: show the active service, deploy to the standby, health check, then switch the symlink — seeing zero-downtime switching is the 'wow' moment"
    - "The logrotate config is a practical reference — walk through each directive (size, rotate, compress, copytruncate) because students will copy this for their own agents"
    - "This is an integration lesson — explicitly connect each component to the lesson where it was first taught (scripts from L6, systemd from L10, security from L8, monitoring from L7)"
  assessment_quick_check:
    - "Ask: what are the three deployment patterns and their key trade-off? (Expected: restart = downtime but simple, blue-green = no downtime but double resources, rolling = gradual but complex)"
    - "Ask students to explain the blue-green switch: what happens to the old instance when the new one passes health checks?"
    - "Ask: what does the copytruncate directive do in logrotate? (Expected: copies the log file and truncates the original in place, avoiding the need to restart the agent)"

teaching_approach: "Integration and Evaluation (Compare patterns -> Implement blue-green -> Add monitoring -> Combine into workflow)"
modality: "Hands-on implementation with AI collaboration"

# Generation metadata
generated_by: "content-implementer v2.0.0"
created: "2026-02-11"
version: "2.0.0"
---

# Advanced Workflow Integration Patterns

You've deployed agents one at a time. You can write a service file, set restart policies, configure start-limit protection, and check health endpoints. Each skill works in isolation.

But production deployment is never one skill at a time. You need to update an agent without downtime. You need logs that don't fill the disk. You need alerts when disk space runs low. You need a single script that creates a user, installs a service, starts the agent, and verifies health -- all in one automated pass.

The jump from "deploy one agent" to "deploy reliably every time" requires **patterns**. This lesson teaches three deployment patterns, shows you how to implement the most important one (blue-green), and then layers monitoring on top so your deployments stay healthy after they go live.

---

## Deployment Patterns: Three Approaches

Not every deployment needs the same strategy. Here are three patterns, each with different trade-offs.

### Simple Restart

Stop the old version, deploy the new code, start the service.

```bash
# Simple restart deployment
sudo systemctl stop my-agent
# Deploy new code (copy files, update configs)
sudo cp -r /tmp/agent-v2/* /opt/agent/
sudo systemctl start my-agent
```

**Output:**
```
(no output -- stop and start complete silently on success)
```

**Pros**: Simple. One service file. No extra infrastructure.

**Cons**: Downtime between stop and start. If the new version fails, you must manually restore the old code and restart. During the gap, any requests to your agent fail.

### Blue-Green Deployment

Run two copies of your agent (blue and green). One is live, the other is idle. Deploy to the idle one, verify it works, then switch traffic. If the new version fails, switch back instantly.

**Pros**: Zero downtime. Instant rollback. You verify before switching.

**Cons**: Requires two service files and temporarily uses double the resources during the switch.

### Rolling Deployment

If you run multiple instances of the same agent (say three copies behind a load balancer), update them one at a time. Each instance gets the new code while the others continue serving.

**Pros**: Gradual rollout. If one instance fails, the others still serve traffic.

**Cons**: Mixed versions run simultaneously during the rollout. Requires multiple instances and a load balancer (more infrastructure than a single-server setup typically has).

### When to Use Each Pattern

| Pattern | Best For | Downtime | Rollback Speed | Resource Cost | Complexity |
|---------|----------|----------|----------------|---------------|------------|
| **Simple restart** | Development, staging, low-traffic agents | Seconds to minutes | Manual (slow) | 1x (minimal) | Low |
| **Blue-green** | Production single-server agents | Zero | Instant (switch back) | 2x during switch | Medium |
| **Rolling** | Multi-instance production agents | Zero | Gradual (per instance) | 1x + 1 instance | High |

**For most single-server agent deployments, blue-green is the sweet spot.** It eliminates downtime without requiring the multi-instance infrastructure that rolling deployments need. The rest of this lesson focuses on implementing it.

---

## Implementing Blue-Green Deployment

Blue-green deployment uses two systemd services -- one "blue" and one "green." At any time, exactly one is live (receiving traffic). The other is idle, waiting for the next deployment.

### Step 1: Create Two Service Files

The blue service runs on port 8000, the green on port 8001. A symlink determines which one is "live."

Create the blue service:

```bash
sudo nano /etc/systemd/system/my-agent-blue.service
```

```ini
[Unit]
Description=Agent Blue Instance
After=network.target
StartLimitIntervalSec=60
StartLimitBurst=5

[Service]
Type=simple
User=nobody
WorkingDirectory=/opt/agent-blue
ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5
MemoryMax=512M
CPUQuota=25%

[Install]
WantedBy=multi-user.target
```

Create the green service:

```bash
sudo nano /etc/systemd/system/my-agent-green.service
```

```ini
[Unit]
Description=Agent Green Instance
After=network.target
StartLimitIntervalSec=60
StartLimitBurst=5

[Service]
Type=simple
User=nobody
WorkingDirectory=/opt/agent-green
ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8001
Restart=on-failure
RestartSec=5
MemoryMax=512M
CPUQuota=25%

[Install]
WantedBy=multi-user.target
```

Set up the directory structure:

```bash
sudo mkdir -p /opt/agent-blue /opt/agent-green
sudo cp /opt/agent/agent_main.py /opt/agent-blue/
sudo cp /opt/agent/agent_main.py /opt/agent-green/
```

**Output:**
```
(no output -- directories and files created silently)
```

Reload systemd and start the blue instance as the initial live version:

```bash
sudo systemctl daemon-reload
sudo systemctl start my-agent-blue
sudo systemctl enable my-agent-blue
```

**Output:**
```
Created symlink /etc/systemd/system/multi-user.target.wants/my-agent-blue.service → /etc/systemd/system/my-agent-blue.service.
```

Verify it's running:

```bash
curl -s http://localhost:8000/health | python3 -m json.tool
```

**Output:**
```json
{
    "status": "healthy",
    "agent": "running",
    "timestamp": "2026-02-11T10:30:01.234567"
}
```

### Step 2: Track Which Instance Is Live

Use a simple file to record the active color:

```bash
echo "blue" | sudo tee /opt/agent-active-color
```

**Output:**
```
blue
```

This file is the single source of truth. Scripts read it to know which instance is currently serving traffic.

### Step 3: The Blue-Green Deploy Script

This script automates the full deployment: deploy to the idle instance, verify health, switch, and provide rollback.

```bash
sudo nano /usr/local/bin/blue-green-deploy.sh
```

```bash
#!/bin/bash
# blue-green-deploy.sh - Zero-downtime deployment for agent_main.py
set -euo pipefail

NEW_CODE_DIR="${1:?Usage: blue-green-deploy.sh /path/to/new/code}"
ACTIVE_COLOR_FILE="/opt/agent-active-color"

# Determine current and target colors
CURRENT_COLOR=$(cat "$ACTIVE_COLOR_FILE")
if [ "$CURRENT_COLOR" = "blue" ]; then
    TARGET_COLOR="green"
    TARGET_PORT=8001
    CURRENT_PORT=8000
else
    TARGET_COLOR="blue"
    TARGET_PORT=8000
    CURRENT_PORT=8001
fi

echo "=== Blue-Green Deployment ==="
echo "Current live: $CURRENT_COLOR (port $CURRENT_PORT)"
echo "Deploying to: $TARGET_COLOR (port $TARGET_PORT)"
echo ""

# Step 1: Deploy new code to target
echo "[1/5] Deploying new code to $TARGET_COLOR..."
sudo cp -r "$NEW_CODE_DIR"/* "/opt/agent-${TARGET_COLOR}/"
echo "Done."

# Step 2: Start the target instance
echo "[2/5] Starting my-agent-${TARGET_COLOR}..."
sudo systemctl start "my-agent-${TARGET_COLOR}"
sleep 3
echo "Done."

# Step 3: Health check the target
echo "[3/5] Checking health on port ${TARGET_PORT}..."
HEALTH_RESPONSE=$(curl -sf "http://localhost:${TARGET_PORT}/health" 2>&1) || {
    echo "FAILED: Health check did not pass on $TARGET_COLOR."
    echo "Rolling back: stopping $TARGET_COLOR."
    sudo systemctl stop "my-agent-${TARGET_COLOR}"
    exit 1
}
echo "Health response: $HEALTH_RESPONSE"
echo "Health check passed."

# Step 4: Switch traffic (update the active-color file)
echo "[4/5] Switching live traffic to $TARGET_COLOR..."
echo "$TARGET_COLOR" | sudo tee "$ACTIVE_COLOR_FILE" > /dev/null
echo "Live instance is now: $TARGET_COLOR (port $TARGET_PORT)"

# Step 5: Stop the old instance
echo "[5/5] Stopping old instance (my-agent-${CURRENT_COLOR})..."
sudo systemctl stop "my-agent-${CURRENT_COLOR}"
echo "Done."

echo ""
echo "=== Deployment Complete ==="
echo "Active: $TARGET_COLOR on port $TARGET_PORT"
echo "Rolled back instance (${CURRENT_COLOR}) is stopped."
echo ""
echo "To rollback, run:"
echo "  sudo systemctl start my-agent-${CURRENT_COLOR}"
echo "  sudo systemctl stop my-agent-${TARGET_COLOR}"
echo "  echo ${CURRENT_COLOR} | sudo tee ${ACTIVE_COLOR_FILE}"
```

Make it executable:

```bash
sudo chmod +x /usr/local/bin/blue-green-deploy.sh
```

**Output:**
```
(no output -- permissions set silently)
```

### Step 4: Run the Deployment

Simulate deploying a new version by updating the code in a staging directory and running the script:

```bash
sudo mkdir -p /tmp/agent-v2
sudo cp /opt/agent/agent_main.py /tmp/agent-v2/
```

Run the blue-green deploy:

```bash
sudo blue-green-deploy.sh /tmp/agent-v2
```

**Output:**
```
=== Blue-Green Deployment ===
Current live: blue (port 8000)
Deploying to: green (port 8001)

[1/5] Deploying new code to green...
Done.
[2/5] Starting my-agent-green...
Done.
[3/5] Checking health on port 8001...
Health response: {"status":"healthy","agent":"running","timestamp":"2026-02-11T10:35:12.456789"}
Health check passed.
[4/5] Switching live traffic to green...
Live instance is now: green (port 8001)
[5/5] Stopping old instance (my-agent-blue)...
Done.

=== Deployment Complete ===
Active: green on port 8001
Rolled back instance (blue) is stopped.

To rollback, run:
  sudo systemctl start my-agent-blue
  sudo systemctl stop my-agent-green
  echo blue | sudo tee /opt/agent-active-color
```

### Step 5: Rollback Procedure

If the new version has a bug that the health check didn't catch, rollback is three commands:

```bash
sudo systemctl start my-agent-blue
sudo systemctl stop my-agent-green
echo blue | sudo tee /opt/agent-active-color
```

**Output:**
```
blue
```

Verify the rollback:

```bash
curl -s http://localhost:8000/health | python3 -m json.tool
```

**Output:**
```json
{
    "status": "healthy",
    "agent": "running",
    "timestamp": "2026-02-11T10:36:45.123456"
}
```

The old version is back in under 10 seconds. No redeployment needed.

---

## Monitoring Integration

Deploying an agent is half the job. Keeping it healthy afterward requires monitoring: rotating logs before they fill the disk, alerting when disk space runs low, and verifying health on a schedule.

### Log Rotation with logrotate

Your agent writes logs. Without rotation, those logs grow until they fill the disk and crash everything.

`logrotate` is a standard Linux tool that rotates, compresses, and removes old log files automatically.

Create a logrotate configuration for your agent:

```bash
sudo nano /etc/logrotate.d/agent-logs
```

```
/var/log/agent/*.log {
    weekly
    rotate 4
    compress
    delaycompress
    missingok
    notifempty
    create 0640 nobody nobody
    postrotate
        systemctl reload my-agent-blue my-agent-green 2>/dev/null || true
    endscript
}
```

Each directive serves a purpose:

| Directive | What It Does |
|-----------|-------------|
| `weekly` | Rotate logs once per week |
| `rotate 4` | Keep 4 rotated files (4 weeks of history) |
| `compress` | Compress rotated files with gzip |
| `delaycompress` | Wait one rotation before compressing (so the most recent rotated file is still plain text for easy reading) |
| `missingok` | Don't error if a log file is missing |
| `notifempty` | Skip rotation if the log file is empty |
| `create 0640 nobody nobody` | Create new log file with these permissions and ownership |
| `postrotate` | After rotating, signal the service to reopen log files |

Create the log directory:

```bash
sudo mkdir -p /var/log/agent
sudo chown nobody:nobody /var/log/agent
```

**Output:**
```
(no output -- directory created and ownership set)
```

Test the configuration (dry run):

```bash
sudo logrotate -d /etc/logrotate.d/agent-logs
```

**Output:**
```
reading config file /etc/logrotate.d/agent-logs

Handling 1 log files in /var/log/agent/*.log
  glob pattern expanded to:
    /var/log/agent/agent.log

considering log /var/log/agent/agent.log
  Now: 2026-02-11 10:40
  Last rotated at 2026-02-11 00:00
  log does not need rotating (log has been rotated within the last week)
```

The `-d` flag runs a dry run -- it shows what logrotate *would* do without actually doing it. Use this to verify your configuration before trusting it with production logs.

### Disk Space Alerts

Log rotation prevents gradual disk fill, but other things consume space too -- temporary files, core dumps, downloaded models. A simple bash script can check disk usage and alert you.

```bash
sudo nano /usr/local/bin/check-disk-space.sh
```

```bash
#!/bin/bash
# check-disk-space.sh - Alert when disk usage exceeds threshold
set -euo pipefail

THRESHOLD=80
ALERT_LOG="/var/log/agent/disk-alerts.log"

# Get disk usage percentage for the root filesystem
USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$TIMESTAMP] WARNING: Disk usage at ${USAGE}% (threshold: ${THRESHOLD}%)" | tee -a "$ALERT_LOG"

    # Show top space consumers
    echo "Top 5 directories by size:" | tee -a "$ALERT_LOG"
    du -sh /var/log/* /opt/* /tmp/* 2>/dev/null | sort -rh | head -5 | tee -a "$ALERT_LOG"
else
    echo "Disk usage OK: ${USAGE}%"
fi
```

Make it executable:

```bash
sudo chmod +x /usr/local/bin/check-disk-space.sh
```

**Output:**
```
(no output -- permissions set silently)
```

Test it:

```bash
sudo check-disk-space.sh
```

**Output (when disk usage is normal):**
```
Disk usage OK: 36%
```

**Output (when disk usage exceeds the threshold):**
```
[2026-02-11 10:45:00] WARNING: Disk usage at 85% (threshold: 80%)
Top 5 directories by size:
4.2G    /var/log/journal
1.8G    /opt/agent-blue
1.8G    /opt/agent-green
512M    /tmp/model-cache
128M    /var/log/agent
```

### Health Check Scheduling with cron

In [Lesson 10](./10-process-control-systemd.md), you created the canonical health check script at `/usr/local/bin/check-agent-health.sh`. Instead of duplicating that script here, schedule it with cron so it runs automatically.

Add cron entries for both health checks and disk monitoring:

```bash
sudo crontab -e
```

Add these lines:

```
# Agent health check every 5 minutes
*/5 * * * * /usr/local/bin/check-agent-health.sh my-agent-blue >> /var/log/agent/health-check.log 2>&1

# Disk space check every hour
0 * * * * /usr/local/bin/check-disk-space.sh >> /var/log/agent/disk-alerts.log 2>&1
```

Verify the cron entries were saved:

```bash
sudo crontab -l
```

**Output:**
```
# Agent health check every 5 minutes
*/5 * * * * /usr/local/bin/check-agent-health.sh my-agent-blue >> /var/log/agent/health-check.log 2>&1

# Disk space check every hour
0 * * * * /usr/local/bin/check-disk-space.sh >> /var/log/agent/disk-alerts.log 2>&1
```

Now your agent is monitored around the clock. Health checks run every 5 minutes, disk alerts run every hour, and logs rotate weekly with 4 weeks of compressed history.

---

## The Complete Deployment Workflow

Here is what a full multi-step deployment looks like when you combine everything from this chapter: user creation, service installation, health verification, and monitoring setup -- all in one script.

```bash
sudo nano /usr/local/bin/full-deploy.sh
```

```bash
#!/bin/bash
# full-deploy.sh - Complete agent deployment workflow
# Combines: user creation, service install, start, health check, monitoring
set -euo pipefail

AGENT_NAME="${1:?Usage: full-deploy.sh <agent-name>}"
AGENT_DIR="/opt/${AGENT_NAME}"
AGENT_USER="agent-runner"
SERVICE_FILE="/etc/systemd/system/${AGENT_NAME}.service"

echo "=== Full Deployment: ${AGENT_NAME} ==="

# Step 1: Create dedicated user (if not exists)
echo "[1/6] Checking agent user..."
if id "$AGENT_USER" &>/dev/null; then
    echo "User $AGENT_USER already exists."
else
    sudo useradd -r -s /usr/sbin/nologin -d /opt -M "$AGENT_USER"
    echo "Created system user: $AGENT_USER"
fi

# Step 2: Create directory and deploy code
echo "[2/6] Deploying agent code..."
sudo mkdir -p "$AGENT_DIR"
sudo cp /tmp/agent-release/agent_main.py "$AGENT_DIR/"
sudo chown -R "$AGENT_USER":"$AGENT_USER" "$AGENT_DIR"
echo "Code deployed to $AGENT_DIR"

# Step 3: Install systemd service
echo "[3/6] Installing systemd service..."
sudo tee "$SERVICE_FILE" > /dev/null <<EOF
[Unit]
Description=Digital FTE Agent: ${AGENT_NAME}
After=network.target
StartLimitIntervalSec=60
StartLimitBurst=5

[Service]
Type=simple
User=${AGENT_USER}
WorkingDirectory=${AGENT_DIR}
ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5
MemoryMax=512M
CPUQuota=25%

[Install]
WantedBy=multi-user.target
EOF
echo "Service file installed: $SERVICE_FILE"

# Step 4: Start service
echo "[4/6] Starting service..."
sudo systemctl daemon-reload
sudo systemctl enable "$AGENT_NAME"
sudo systemctl start "$AGENT_NAME"
sleep 3
echo "Service started."

# Step 5: Health check
echo "[5/6] Verifying health..."
if curl -sf http://localhost:8000/health > /dev/null 2>&1; then
    echo "Health check PASSED."
else
    echo "Health check FAILED. Check logs:"
    echo "  sudo journalctl -u $AGENT_NAME -n 20"
    exit 1
fi

# Step 6: Confirm
echo "[6/6] Verifying final state..."
STATUS=$(systemctl is-active "$AGENT_NAME")
echo "Service status: $STATUS"

echo ""
echo "=== Deployment Complete ==="
echo "Service: $AGENT_NAME"
echo "Status:  $STATUS"
echo "Health:  http://localhost:8000/health"
echo "Logs:    sudo journalctl -u $AGENT_NAME -f"
```

Make it executable:

```bash
sudo chmod +x /usr/local/bin/full-deploy.sh
```

**Output:**
```
(no output -- permissions set silently)
```

Run the full deployment:

```bash
sudo mkdir -p /tmp/agent-release
sudo cp /opt/agent/agent_main.py /tmp/agent-release/
sudo full-deploy.sh my-agent
```

**Output:**
```
=== Full Deployment: my-agent ===
[1/6] Checking agent user...
User agent-runner already exists.
[2/6] Deploying agent code...
Code deployed to /opt/my-agent
[3/6] Installing systemd service...
Service file installed: /etc/systemd/system/my-agent.service
[4/6] Starting service...
Service started.
[5/6] Verifying health...
Health check PASSED.
[6/6] Verifying final state...
Service status: active

=== Deployment Complete ===
Service: my-agent
Status:  active
Health:  http://localhost:8000/health
Logs:    sudo journalctl -u my-agent -f
```

One command. User created, code deployed, service installed, agent started, health verified. This is the difference between a manual checklist and an automated workflow -- the script never forgets a step.

---

## A Note on Docker

Docker packages your application with its dependencies in a container -- an isolated environment that runs the same way regardless of the host system. For single-server deployments like the ones in this chapter, systemd is simpler and has zero overhead: your agent runs directly on the host OS with no abstraction layer. Docker excels when you need environment consistency across development, staging, and production servers, or when you're deploying to orchestrated environments like Kubernetes. You'll learn Docker in a dedicated chapter later in this book. For now, systemd is the right tool for your deployment -- it gives you service management, restart policies, resource limits, and logging with nothing extra to install.

---

## Exercises

### Exercise 1: Document a Blue-Green Deployment Plan

Write a deployment plan for updating your agent from v1 to v2 using the blue-green pattern. Your plan should include:

1. The name of the currently active service (and its port)
2. The name of the idle service you will deploy to (and its port)
3. The health check command you will run before switching
4. The exact commands to switch traffic
5. The exact rollback commands if something goes wrong

Write your plan as a text file:

```bash
nano ~/blue-green-plan.txt
```

**Verification** -- your plan should contain all five sections:

```bash
grep -c "active service\|idle service\|health check\|switch traffic\|rollback" ~/blue-green-plan.txt
```

**Expected output:**
```
5
```

If the count is lower than 5, your plan is missing sections. Review the blue-green deployment walkthrough above and add the missing pieces.

### Exercise 2: Configure logrotate for Agent Logs

Create a logrotate configuration that rotates agent logs weekly, keeps 4 weeks of history, and compresses old logs.

```bash
sudo nano /etc/logrotate.d/agent-logs
```

Write the configuration (refer to the logrotate section above), then verify:

```bash
cat /etc/logrotate.d/agent-logs
```

**Expected output:**
```
/var/log/agent/*.log {
    weekly
    rotate 4
    compress
    delaycompress
    missingok
    notifempty
    create 0640 nobody nobody
    postrotate
        systemctl reload my-agent-blue my-agent-green 2>/dev/null || true
    endscript
}
```

Confirm the configuration parses without errors:

```bash
sudo logrotate -d /etc/logrotate.d/agent-logs
```

**Expected output (no errors):**
```
reading config file /etc/logrotate.d/agent-logs
...
```

If you see `error: ...` in the output, check your syntax -- a common mistake is forgetting the `endscript` keyword after `postrotate`.

### Exercise 3: Write a Full Deployment Script

Write a deployment script that combines user creation, service file installation, service start, and health verification into one automated pass. You can use `full-deploy.sh` above as a reference, but write it yourself.

After writing and running your script, verify both conditions:

```bash
systemctl is-active my-agent
```

**Expected output:**
```
active
```

```bash
curl -s http://localhost:8000/health
```

**Expected output:**
```json
{"status":"healthy","agent":"running","timestamp":"..."}
```

Both checks must pass. If `systemctl is-active` shows `inactive` or `failed`, check `journalctl -u my-agent -n 20` for error details. If `curl` fails, verify the port number matches what's in your service file's `ExecStart`.

---

## Try With AI

"Ask Claude: 'I need to update my production agent with zero downtime. Compare restart, blue-green, and rolling deployment approaches for a single-server setup. Which do you recommend and why?'"

**What you're learning:** AI helps you evaluate production trade-offs by considering factors (resource overhead, complexity, rollback speed) that are hard to assess without experience. Notice how AI weighs the trade-offs differently for a single-server constraint versus a multi-server fleet.

"Tell Claude: 'I chose blue-green deployment. My constraint: only one server with 2GB RAM, so I can't run both versions simultaneously for long. Design a deployment script that minimizes overlap time.' Review the approach."

**What you're learning:** Providing real resource constraints forces practical solutions instead of textbook ideals. Compare AI's response to the script in this lesson -- it may suggest techniques like pre-pulling code, faster health checks, or immediate shutdown of the old instance to reduce the overlap window.

"Ask Claude: 'Review my complete deployment workflow: [paste your deployment script from Exercise 3]. What failure scenarios does it NOT handle? Add error handling for each one.'"

**What you're learning:** Production workflows need resilience against failures at every step -- something that emerges through iterative review. AI will likely identify scenarios you didn't consider: what if the user already exists with wrong permissions? What if the port is already in use? What if disk space is too low to copy files? Each failure mode AI finds teaches you to think more defensively about automation.

:::note Safety Reminder
Always test deployment scripts on a non-production server first. Blue-green deployments involve stopping services -- a typo in the active color or port number can take down your live agent. Run through the full cycle (deploy, verify, switch, rollback) in a staging environment before trusting the script with production traffic.
:::
