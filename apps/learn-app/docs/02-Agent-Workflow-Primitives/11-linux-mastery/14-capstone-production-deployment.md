---
sidebar_position: 14
chapter: 11
lesson: 14
title: "Lesson 14: Capstone — Spec-First Production Deployment"
description: "Synthesize all chapter skills into a complete production deployment: write a deployment specification, implement it step-by-step, validate with layered checks, and package as a repeatable script."
keywords: ["capstone", "production deployment", "systemd", "deployment specification", "layered validation", "deploy script", "spec-first", "agent deployment", "linux mastery"]
duration_minutes: 90

# HIDDEN SKILLS METADATA
skills:
  - name: "Deployment Specification Design"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student writes a complete DEPLOYMENT-SPEC.md covering service definition, security requirements, monitoring plan, and validation criteria before any implementation begins"

  - name: "Production Architecture Implementation"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student implements a complete systemd service with direct port binding, resource limits, restart protection, and dedicated non-root user following a written specification"

  - name: "AI-Orchestrated Deployment"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student directs AI to review specifications and optimize deployment using reusable skills from L13, incorporating AI feedback into the deployment process"

  - name: "Layered Validation"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student runs a five-layer validation script (service, network, security, monitoring, resources) and interprets pass/fail results against the deployment specification"

  - name: "Deployment Packaging"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student packages the entire deployment into an idempotent deploy.sh script that produces a running, validated agent on a clean server"

learning_objectives:
  - objective: "Write a deployment specification (DEPLOYMENT-SPEC.md) covering service, security, monitoring, and validation"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Specification document contains all four sections with measurable success criteria and validation commands"

  - objective: "Implement a complete agent deployment using only skills taught in this chapter"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Running systemd service with dedicated user, resource limits, restart protection, and firewall rules — all built from chapter skills"

  - objective: "Validate deployment against specification using layered verification"
    proficiency_level: "C1"
    bloom_level: "Evaluate"
    assessment_method: "Five-layer validation script passes all checks: service active, network responding, correct user, logs flowing, resource limits applied"

  - objective: "Package the deployment as a reproducible script"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Running deploy.sh on a clean workspace produces a fully operational agent that passes all validation layers"

cognitive_load:
  new_concepts: 5
  concepts_list:
    - "DEPLOYMENT-SPEC.md methodology (write specification before implementation)"
    - "Production architecture (systemd + direct port binding with resource controls)"
    - "AI-orchestrated deployment (using reusable skills from L13)"
    - "Layered validation script (service, network, security, monitoring, resources)"
    - "Deployment packaging for repeatability (idempotent deploy.sh)"
  assessment: "5 concepts at C1 level. This capstone integrates all previous chapter skills rather than introducing fundamentally new tools. The cognitive challenge is synthesis and orchestration, not new tool learning."

differentiation:
  extension_for_advanced: "Add environment-aware deployment (dev vs production configs), automated rollback on validation failure, or systemd timer-based health monitoring that restarts the service if the health endpoint stops responding."
  remedial_for_struggling: "Start with just the specification — write DEPLOYMENT-SPEC.md without implementing it. Then implement one section at a time: create user first, then service file, then validation. Build confidence through incremental success."

teaching_guide:
  lesson_type: "capstone"
  session_group: 5
  session_title: "Skills, Capstone, and Practice"
  key_points:
    - "Spec-first deployment (write DEPLOYMENT-SPEC.md before touching the terminal) is the professional pattern — it prevents the 'type commands until it works' anti-pattern"
    - "This capstone integrates every skill from lessons 1-13: navigation, file ops, scripting, security, networking, systemd, debugging, patterns, and skills"
    - "Layered validation (service, network, security, monitoring, resources) catches failures that single-point checks miss — each layer tests a different dimension"
    - "Deployment packaging (idempotent deploy.sh) makes the deployment reproducible — anyone can run the same script on a clean server and get the same result"
  misconceptions:
    - "Students want to skip the specification and start typing commands — emphasize that the spec is what makes this a production deployment, not a hobby project"
    - "Students think validation means checking if the service is running — five-layer validation also checks permissions, firewall rules, resource limits, and log rotation"
    - "Students expect AI to write the entire deployment for them — AI reviews and optimizes, but the student must write the specification and understand every component"
  discussion_prompts:
    - "Compare your capstone deployment to the commands you typed in lesson 10. What is different about spec-first deployment versus 'just make it work'?"
    - "If you hand your deploy.sh to a colleague who has never seen your server, what would they need to know before running it? How does the DEPLOYMENT-SPEC.md help?"
  teaching_tips:
    - "This is the chapter closer — connect back to the chapter opener (lesson 1) where students could barely navigate the filesystem, showing how far they have come"
    - "Allow 90 minutes for this lesson — students need time to write the spec, implement, validate, and package; rushing the capstone undermines its purpose"
    - "The five-layer validation script is the most satisfying moment — seeing all checks pass is the reward for 13 lessons of progressive skill building"
    - "Have students deploy on a clean workspace (fresh /tmp directory) to prove their deploy.sh is truly reproducible — this connects to fresh-system testing from lesson 13"
  assessment_quick_check:
    - "Ask: what are the four sections of DEPLOYMENT-SPEC.md? (Expected: service definition, security requirements, monitoring plan, validation criteria)"
    - "Ask students to list the five validation layers (Expected: service active, network responding, correct user/permissions, logs flowing, resource limits applied)"
    - "Ask: what makes a deploy.sh script idempotent? (Expected: it can be run multiple times without breaking — checks if resources exist before creating them)"

teaching_approach: "Spec-first capstone: specification → implementation → validation → packaging"
modality: "Hands-on synthesis with AI collaboration"

# Generation metadata
generated_by: "content-implementer v2.0.0"
created: "2026-02-11"
version: "2.0.0"
---

# Capstone — Spec-First Production Deployment

Everything you've learned — CLI navigation, file operations, scripting, security, networking, systemd, debugging, deployment patterns, reusable skills — comes together here. This capstone is different from every other lesson in this chapter: you will write a specification FIRST, then implement it, then validate it. This is how production deployments work in professional environments.

The difference between a hobbyist deployment and a production deployment is not the tools. It is the process. Hobbyists type commands until the service starts. Production engineers define success criteria before touching a terminal, implement against those criteria, and validate systematically. You are going to do the second thing.

You will deploy the same `agent_main.py` from [Lesson 10](./10-process-control-systemd.md) — a FastAPI agent with a health check endpoint. But this time, the deployment will be specification-driven, validated layer by layer, and packaged so anyone can reproduce it.

---

## The Spec-First Approach

Think about what happens when you deploy without a specification. You SSH into a server, start typing commands, fix problems as they appear, and eventually something works. Three weeks later, the server reboots and the agent doesn't come back. You SSH in again, try to remember what you did, and spend an hour reconstructing the setup.

A deployment specification prevents this. It is a document that answers four questions before you touch the terminal:

| Question | Section in Spec | Example |
|----------|----------------|---------|
| What am I deploying? | Service Definition | FastAPI agent on port 8000, managed by systemd |
| How is it protected? | Security Requirements | Dedicated non-root user, firewall restricts access |
| How do I know it's healthy? | Monitoring Plan | Health endpoint, journalctl logs, disk alerts |
| How do I prove it works? | Validation Criteria | 5-layer check: service, network, security, logs, resources |

The specification becomes your implementation checklist. Every command you run traces back to a requirement. Every validation check maps to a success criterion. Nothing is ad-hoc.

---

## Writing Your DEPLOYMENT-SPEC.md

Here is the template. You will fill it out for `agent_main.py` before implementing anything.

```markdown
# DEPLOYMENT-SPEC.md — Agent Production Deployment

## Service Definition
- **Agent name**: agent-prod
- **Application**: agent_main.py (FastAPI with uvicorn)
- **Port**: 8000 (direct binding, no reverse proxy)
- **System user**: agent-prod (dedicated, no login shell)
- **Working directory**: /opt/agent-prod/
- **Restart policy**: on-failure (not always) with 5s delay
- **Start-limit protection**: max 5 restarts in 60 seconds
- **Resource limits**: MemoryMax=512M, CPUQuota=25%

## Security Requirements
- [ ] Dedicated system user `agent-prod` (no root execution)
- [ ] User has no login shell (/usr/sbin/nologin)
- [ ] Application files owned by agent-prod:agent-prod
- [ ] Service file permissions: 644 (root-owned)
- [ ] Firewall allows only port 8000/tcp for agent traffic
- [ ] No password-based SSH (key-based only — from L7)

## Monitoring Plan
- **Health check**: GET /health returns {"status": "healthy", ...}
- **Log location**: journalctl -u agent-prod (systemd journal)
- **Log rotation**: managed by journald (MaxRetentionSec, SystemMaxUse)
- **Disk alerts**: monitor /opt/agent-prod/ usage
- **Crash detection**: systemd restart counter + journal entries

## Validation Criteria
- [ ] Layer 1 — Service: `systemctl is-active agent-prod` returns "active"
- [ ] Layer 2 — Network: `curl -s localhost:8000/health` returns healthy JSON
- [ ] Layer 3 — Security: agent runs as agent-prod user, not root
- [ ] Layer 4 — Monitoring: logs appear in journalctl within last 5 minutes
- [ ] Layer 5 — Resources: MemoryMax shows 536870912 (512MB in bytes)
```

**Expected output** (after saving the file):
```
$ wc -l DEPLOYMENT-SPEC.md
30 DEPLOYMENT-SPEC.md
```

Read through each section. Notice how every requirement is testable. "Dedicated system user" is not a vague goal — it maps to a specific check: `ps -eo user,comm | grep uvicorn` must show `agent-prod`, not `root`. This is what separates a specification from a wish list.

---

## Implementing the Specification

Now you implement. Every step below references which spec section it satisfies. If a step does not trace to the spec, it does not belong here.

### Step 1: Create the Agent User (Security Requirements)

Create a dedicated system user with no login shell:

```bash
sudo useradd -r -s /usr/sbin/nologin agent-prod
```

**Expected output:**
```
(no output — silent success means the user was created)
```

Verify the user exists:

```bash
id agent-prod
```

**Expected output:**
```
uid=998(agent-prod) gid=998(agent-prod) groups=998(agent-prod)
```

The `-r` flag creates a system user (low UID, no home directory). The `-s /usr/sbin/nologin` flag prevents anyone from logging in as this user. The agent process runs as this user, but no human can SSH in as it.

### Step 2: Set Up the Working Directory (Service Definition)

Create the application directory and copy the agent:

```bash
sudo mkdir -p /opt/agent-prod
```

**Expected output:**
```
(no output — directory created)
```

```bash
sudo cp /opt/agent/agent_main.py /opt/agent-prod/
```

**Expected output:**
```
(no output — file copied)
```

This copies the same `agent_main.py` you deployed in [Lesson 10](./10-process-control-systemd.md). If you haven't set it up yet, create it now with the FastAPI agent code from that lesson.

### Step 3: Install Dependencies (Service Definition)

```bash
sudo pip install fastapi uvicorn
```

**Expected output:**
```
Requirement already satisfied: fastapi in /usr/local/lib/python3.10/dist-packages
Requirement already satisfied: uvicorn in /usr/local/lib/python3.10/dist-packages
```

If you see "Successfully installed" instead, that is also correct — it means the packages were not previously installed.

### Step 4: Set Ownership and Permissions (Security Requirements)

```bash
sudo chown -R agent-prod:agent-prod /opt/agent-prod
```

**Expected output:**
```
(no output — ownership changed)
```

Verify:

```bash
ls -la /opt/agent-prod/
```

**Expected output:**
```
total 12
drwxr-xr-x 2 agent-prod agent-prod 4096 Feb 11 10:00 .
drwxr-xr-x 4 root       root       4096 Feb 11 10:00 ..
-rw-r--r-- 1 agent-prod agent-prod  892 Feb 11 10:00 agent_main.py
```

Every file is owned by `agent-prod`. The agent process can read its own files, but the restricted user cannot modify system files outside this directory.

### Step 5: Write the systemd Service File (Service Definition + Security)

```bash
sudo nano /etc/systemd/system/agent-prod.service
```

Add this content:

```ini
[Unit]
Description=Production Digital FTE Agent
After=network.target

[Service]
Type=simple
User=agent-prod
Group=agent-prod
WorkingDirectory=/opt/agent-prod
ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000

# Restart policy: recover from crashes, not intentional stops
Restart=on-failure
RestartSec=5

# Start-limit protection: stop retrying after repeated failures
StartLimitBurst=5
StartLimitIntervalSec=60

# Resource limits: prevent runaway consumption
MemoryMax=512M
CPUQuota=25%

[Install]
WantedBy=multi-user.target
```

**Expected output** (after saving):
```
(no output — file saved)
```

Each directive traces to the specification:

| Directive | Spec Requirement |
|-----------|-----------------|
| `User=agent-prod` | Security: dedicated non-root user |
| `Restart=on-failure` | Service: restart on crash, stay stopped on intentional stop |
| `RestartSec=5` | Service: 5-second delay between restarts |
| `StartLimitBurst=5` | Service: max 5 restarts in the interval |
| `StartLimitIntervalSec=60` | Service: 60-second window for counting restarts |
| `MemoryMax=512M` | Service: 512MB memory ceiling |
| `CPUQuota=25%` | Service: 25% CPU ceiling |

Why `Restart=on-failure` and not `Restart=always`? Because `always` restarts the service even after you deliberately run `systemctl stop`. That means you cannot cleanly stop your own service — you would have to disable it first. `on-failure` gives you control: crashes get automatic recovery, intentional stops stay stopped.

### Step 6: Enable and Start the Service (Service Definition)

```bash
sudo systemctl daemon-reload
```

**Expected output:**
```
(no output — daemon-reload completes silently on success)
```

```bash
sudo systemctl enable agent-prod
```

**Expected output:**
```
Created symlink /etc/systemd/system/multi-user.target.wants/agent-prod.service → /etc/systemd/system/agent-prod.service.
```

```bash
sudo systemctl start agent-prod
```

**Expected output:**
```
(no output — a silent start means success)
```

Verify it is running:

```bash
sudo systemctl status agent-prod
```

**Expected output:**
```
● agent-prod.service - Production Digital FTE Agent
     Loaded: loaded (/etc/systemd/system/agent-prod.service; enabled; preset: enabled)
     Active: active (running) since Tue 2026-02-11 10:05:00 UTC; 5s ago
   Main PID: 5432 (uvicorn)
      Tasks: 2 (limit: 4915)
     Memory: 48.3M (max: 512.0M)
        CPU: 320ms
     CGroup: /system.slice/agent-prod.service
             └─5432 /usr/local/bin/python3 /usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000
```

Look at the `Memory` line — it shows `(max: 512.0M)`, confirming your resource limit is applied.

### Step 7: Configure the Firewall (Security Requirements)

```bash
sudo ufw allow 8000/tcp
```

**Expected output:**
```
Rule added
Rule added (v6)
```

Verify the rule:

```bash
sudo ufw status | grep 8000
```

**Expected output:**
```
8000/tcp                   ALLOW       Anywhere
8000/tcp (v6)              ALLOW       Anywhere (v6)
```

Port 8000 is now open for agent traffic. All other ports remain blocked (except SSH on port 22, which you configured in [Lesson 8](./08-security-hardening.md)).

:::tip Future Enhancement
When you learn nginx in a future chapter, you can add a reverse proxy in front for SSL termination and load balancing. For now, direct port binding keeps the architecture simple and gives you one fewer component to debug.
:::

### Step 8: Verify the Health Endpoint (Monitoring Plan)

```bash
curl -s localhost:8000/health
```

**Expected output:**
```json
{"status":"healthy","agent":"running","timestamp":"2026-02-11T10:05:15.234567"}
```

This is the same health check endpoint from [Lesson 10](./10-process-control-systemd.md). It confirms the agent is alive and responding to requests.

Your implementation is complete. Every step traced back to a requirement in the specification. Now you validate.

---

## Layered Validation

Validation is not "it seems to work." Validation is systematic proof that every requirement in your specification is met. Each layer tests a different dimension of the deployment.

### Layer 1 — Service

Is the service running?

```bash
systemctl is-active agent-prod
```

**Expected output (PASS):**
```
active
```

**Expected output (FAIL):**
```
inactive
```

If it fails, check the journal: `journalctl -u agent-prod -n 20 --no-pager`

### Layer 2 — Network

Is the agent responding to requests?

```bash
curl -s localhost:8000/health | python3 -m json.tool
```

**Expected output (PASS):**
```json
{
    "status": "healthy",
    "agent": "running",
    "timestamp": "2026-02-11T10:10:00.123456"
}
```

**Expected output (FAIL):**
```
curl: (7) Failed to connect to localhost port 8000: Connection refused
```

If it fails but the service is active, check that uvicorn is binding to the correct port: `ss -tlnp | grep 8000`

### Layer 3 — Security

Is the agent running as the correct user (not root)?

```bash
ps -eo user,comm | grep uvicorn
```

**Expected output (PASS):**
```
agent-p+ uvicorn
```

**Expected output (FAIL):**
```
root     uvicorn
```

The `agent-p+` is a truncated display of `agent-prod`. If you see `root`, the `User=` directive in your service file is wrong or missing.

### Layer 4 — Monitoring

Are logs flowing?

```bash
journalctl -u agent-prod --since "5 min ago" --no-pager | head -5
```

**Expected output (PASS):**
```
Feb 11 10:05:00 server systemd[1]: Started Production Digital FTE Agent.
Feb 11 10:05:01 server uvicorn[5432]: INFO:     Started server process [5432]
Feb 11 10:05:01 server uvicorn[5432]: INFO:     Waiting for application startup.
Feb 11 10:05:01 server uvicorn[5432]: INFO:     Application startup complete.
Feb 11 10:05:01 server uvicorn[5432]: INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Expected output (FAIL):**
```
-- No entries --
```

If no entries appear, either the service has not started recently or journald is not capturing its output.

### Layer 5 — Resources

Are resource limits applied?

```bash
systemctl show agent-prod --property=MemoryMax
```

**Expected output (PASS):**
```
MemoryMax=536870912
```

**Expected output (FAIL):**
```
MemoryMax=infinity
```

The value `536870912` is 512 MB in bytes. If you see `infinity`, the `MemoryMax=512M` directive is missing from the `[Service]` section or you forgot to run `systemctl daemon-reload` after editing.

### The Complete Validation Script

Combine all five layers into a single executable script:

```bash
#!/bin/bash
# validate-deployment.sh — Layered deployment validation
# Runs 5 validation layers against DEPLOYMENT-SPEC.md requirements

set -u  # Exit on undefined variables

AGENT_NAME="agent-prod"
AGENT_PORT="8000"
AGENT_USER="agent-prod"
EXPECTED_MEMORY="536870912"

PASS=0
FAIL=0

check() {
    local layer="$1"
    local description="$2"
    local result="$3"

    if [ "$result" -eq 0 ]; then
        echo "  PASS: $description"
        PASS=$((PASS + 1))
    else
        echo "  FAIL: $description"
        FAIL=$((FAIL + 1))
    fi
}

echo "=== Deployment Validation: $AGENT_NAME ==="
echo ""

# LAYER 1: Service
echo "[Layer 1] Service"
systemctl is-active --quiet "$AGENT_NAME"
check "1" "Service is active" $?

systemctl is-enabled --quiet "$AGENT_NAME"
check "1" "Service is enabled (starts on boot)" $?

echo ""

# LAYER 2: Network
echo "[Layer 2] Network"
HEALTH=$(curl -s -o /dev/null -w "%{http_code}" "localhost:$AGENT_PORT/health" 2>/dev/null)
[ "$HEALTH" = "200" ]
check "2" "Health endpoint returns 200" $?

curl -s "localhost:$AGENT_PORT/health" | grep -q '"status":"healthy"'
check "2" "Health response contains status:healthy" $?

echo ""

# LAYER 3: Security
echo "[Layer 3] Security"
SERVICE_USER=$(ps -eo user,comm --no-headers | grep uvicorn | awk '{print $1}' | head -1)
[ "$SERVICE_USER" = "$AGENT_USER" ] || [ "$SERVICE_USER" = "agent-p+" ]
check "3" "Agent runs as $AGENT_USER (not root)" $?

id "$AGENT_USER" > /dev/null 2>&1
check "3" "Dedicated user $AGENT_USER exists" $?

echo ""

# LAYER 4: Monitoring
echo "[Layer 4] Monitoring"
LOGCOUNT=$(journalctl -u "$AGENT_NAME" --since "5 min ago" --no-pager 2>/dev/null | wc -l)
[ "$LOGCOUNT" -gt 1 ]
check "4" "Logs flowing in journal (found $LOGCOUNT lines)" $?

echo ""

# LAYER 5: Resources
echo "[Layer 5] Resources"
ACTUAL_MEMORY=$(systemctl show "$AGENT_NAME" --property=MemoryMax --value)
[ "$ACTUAL_MEMORY" = "$EXPECTED_MEMORY" ]
check "5" "MemoryMax is $EXPECTED_MEMORY (512MB)" $?

echo ""
echo "=== Results: $PASS passed, $FAIL failed ==="

if [ "$FAIL" -eq 0 ]; then
    echo "ALL CHECKS PASSED — deployment meets specification"
    exit 0
else
    echo "VALIDATION FAILED — review failed checks against DEPLOYMENT-SPEC.md"
    exit 1
fi
```

Save this as `validate-deployment.sh` and run it:

```bash
chmod +x validate-deployment.sh
sudo bash validate-deployment.sh
```

**Expected output (all passing):**
```
=== Deployment Validation: agent-prod ===

[Layer 1] Service
  PASS: Service is active
  PASS: Service is enabled (starts on boot)

[Layer 2] Network
  PASS: Health endpoint returns 200
  PASS: Health response contains status:healthy

[Layer 3] Security
  PASS: Agent runs as agent-prod (not root)
  PASS: Dedicated user agent-prod exists

[Layer 4] Monitoring
  PASS: Logs flowing in journal (found 12 lines)

[Layer 5] Resources
  PASS: MemoryMax is 536870912 (512MB)

=== Results: 8 passed, 0 failed ===
ALL CHECKS PASSED — deployment meets specification
```

**Expected output (with failure):**
```
=== Deployment Validation: agent-prod ===

[Layer 1] Service
  PASS: Service is active
  PASS: Service is enabled (starts on boot)

[Layer 2] Network
  FAIL: Health endpoint returns 200
  FAIL: Health response contains status:healthy

...

=== Results: 6 passed, 2 failed ===
VALIDATION FAILED — review failed checks against DEPLOYMENT-SPEC.md
```

When a layer fails, work backward: Layer 2 (Network) failed but Layer 1 (Service) passed means the service is running but not responding. Check if uvicorn bound to the right port (`ss -tlnp | grep 8000`) or if the firewall is blocking local connections.

---

## Packaging for Repeatability

Your deployment works. But can someone else reproduce it? Can YOU reproduce it on a new server next month? Packaging turns your manual commands into a script that does everything in one run.

### The Complete deploy.sh

```bash
#!/bin/bash
# deploy.sh — Automated agent deployment
# Implements DEPLOYMENT-SPEC.md requirements in a single script
# Usage: sudo bash deploy.sh

set -e  # Exit on any error

AGENT_NAME="agent-prod"
AGENT_USER="agent-prod"
AGENT_PORT="8000"
AGENT_DIR="/opt/$AGENT_NAME"
SERVICE_FILE="/etc/systemd/system/$AGENT_NAME.service"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Deploying $AGENT_NAME ==="

# Step 1: Create dedicated user (idempotent)
echo "[1/7] Creating user $AGENT_USER..."
if id "$AGENT_USER" &>/dev/null; then
    echo "  User $AGENT_USER already exists — skipping"
else
    useradd -r -s /usr/sbin/nologin "$AGENT_USER"
    echo "  Created system user $AGENT_USER"
fi

# Step 2: Create working directory
echo "[2/7] Setting up $AGENT_DIR..."
mkdir -p "$AGENT_DIR"
echo "  Directory ready"

# Step 3: Copy application
echo "[3/7] Copying agent_main.py..."
cp "$SCRIPT_DIR/agent_main.py" "$AGENT_DIR/"
echo "  Application copied"

# Step 4: Install dependencies
echo "[4/7] Installing Python dependencies..."
pip install --quiet fastapi uvicorn
echo "  Dependencies installed"

# Step 5: Set permissions
echo "[5/7] Setting ownership and permissions..."
chown -R "$AGENT_USER:$AGENT_USER" "$AGENT_DIR"
echo "  Ownership set to $AGENT_USER"

# Step 6: Write and activate systemd service (idempotent)
echo "[6/7] Configuring systemd service..."
cat > "$SERVICE_FILE" << 'EOF'
[Unit]
Description=Production Digital FTE Agent
After=network.target

[Service]
Type=simple
User=agent-prod
Group=agent-prod
WorkingDirectory=/opt/agent-prod
ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5
StartLimitBurst=5
StartLimitIntervalSec=60
MemoryMax=512M
CPUQuota=25%

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable "$AGENT_NAME"
echo "  Service configured and enabled"

# Step 7: Configure firewall (idempotent)
echo "[7/7] Configuring firewall..."
if ufw status | grep -q "$AGENT_PORT/tcp"; then
    echo "  Firewall rule for $AGENT_PORT/tcp already exists — skipping"
else
    ufw allow "$AGENT_PORT/tcp"
    echo "  Firewall rule added for port $AGENT_PORT"
fi

# Start the service
echo ""
echo "Starting $AGENT_NAME..."
systemctl restart "$AGENT_NAME"
sleep 2

# Quick verification
if systemctl is-active --quiet "$AGENT_NAME"; then
    echo "Service is active"
else
    echo "WARNING: Service failed to start — check: journalctl -u $AGENT_NAME -n 20"
    exit 1
fi

HEALTH=$(curl -s "localhost:$AGENT_PORT/health" 2>/dev/null || echo "UNREACHABLE")
echo "Health check: $HEALTH"

echo ""
echo "=== Deployment complete ==="
echo "Next: Run validate-deployment.sh for full layered validation"
```

**Expected output:**
```
=== Deploying agent-prod ===
[1/7] Creating user agent-prod...
  Created system user agent-prod
[2/7] Setting up /opt/agent-prod/...
  Directory ready
[3/7] Copying agent_main.py...
  Application copied
[4/7] Installing Python dependencies...
  Dependencies installed
[5/7] Setting ownership and permissions...
  Ownership set to agent-prod
[6/7] Configuring systemd service...
  Service configured and enabled
[7/7] Configuring firewall...
  Firewall rule added for port 8000

Starting agent-prod...
Service is active
Health check: {"status":"healthy","agent":"running","timestamp":"2026-02-11T10:15:00.123456"}

=== Deployment complete ===
Next: Run validate-deployment.sh for full layered validation
```

Notice the idempotency patterns: Step 1 checks if the user exists before creating it. Step 7 checks if the firewall rule exists before adding it. Running `deploy.sh` twice produces the same result as running it once. This matters because real deployments get re-run — after updates, after server migrations, after debugging. A script that fails on its second run is not production-ready.

---

## Production Readiness Checklist

Before declaring this deployment complete, verify every requirement from the specification:

| Requirement | Status | Verification Command |
|-------------|--------|---------------------|
| Service running | ✓ or ✗ | `systemctl is-active agent-prod` |
| Starts on boot | ✓ or ✗ | `systemctl is-enabled agent-prod` |
| Health check passing | ✓ or ✗ | `curl -s localhost:8000/health` |
| Runs as agent-prod | ✓ or ✗ | `ps -eo user,comm \| grep uvicorn` |
| No login shell | ✓ or ✗ | `grep agent-prod /etc/passwd` (shows `/usr/sbin/nologin`) |
| Correct file ownership | ✓ or ✗ | `ls -la /opt/agent-prod/` |
| Firewall configured | ✓ or ✗ | `sudo ufw status \| grep 8000` |
| Memory limit applied | ✓ or ✗ | `systemctl show agent-prod --property=MemoryMax` → 536870912 |
| CPU limit applied | ✓ or ✗ | `systemctl show agent-prod --property=CPUQuotaPerSecUSec` |
| Restart protection | ✓ or ✗ | `systemctl show agent-prod --property=StartLimitBurst` → 5 |
| Logs flowing | ✓ or ✗ | `journalctl -u agent-prod --since "5 min ago"` |
| Crash recovery works | ✓ or ✗ | Kill process, wait 10s, check `is-active` |

Every row links back to a line in DEPLOYMENT-SPEC.md. If any row shows ✗, you know exactly what to fix and how to verify the fix.

---

## Exercises

### Exercise 1: Write Your DEPLOYMENT-SPEC.md

Using the template from this lesson, write a complete `DEPLOYMENT-SPEC.md` for deploying `agent_main.py` to production. Fill in every section: Service Definition, Security Requirements, Monitoring Plan, and Validation Criteria.

**Verification:**

```bash
grep -c "##" DEPLOYMENT-SPEC.md
```

**Expected output:**
```
4
```

Your spec should have at least 4 section headers. Each section should contain specific, testable requirements — not vague goals.

### Exercise 2: Implement the Specification

Follow the implementation steps in this lesson to deploy the agent. Do not skip ahead — implement each step and verify it before moving to the next.

**Verification:**

```bash
systemctl is-active agent-prod
```

**Expected output:**
```
active
```

If you see `inactive` or `failed`, check the journal: `journalctl -u agent-prod -n 20 --no-pager`

### Exercise 3: Run the Layered Validation Script

Save the validation script from this lesson as `validate-deployment.sh`, make it executable, and run it.

**Verification:**

```bash
sudo bash validate-deployment.sh
```

**Expected output (final line):**
```
ALL CHECKS PASSED — deployment meets specification
```

If any layer fails, trace the failure to the corresponding spec requirement and fix the underlying issue before re-running.

### Exercise 4: Package into deploy.sh and Test

Save the deployment script, place `agent_main.py` alongside it, and test on a clean state. First, tear down the existing deployment:

```bash
sudo systemctl stop agent-prod
sudo systemctl disable agent-prod
sudo rm /etc/systemd/system/agent-prod.service
sudo systemctl daemon-reload
sudo userdel agent-prod
sudo rm -rf /opt/agent-prod
```

**Expected output:**
```
Removed /etc/systemd/system/multi-user.target.wants/agent-prod.service.
```

Now deploy from scratch:

```bash
sudo bash deploy.sh
```

**Verification:**

```bash
sudo bash validate-deployment.sh | tail -1
```

**Expected output:**
```
ALL CHECKS PASSED — deployment meets specification
```

A single script, from clean server to production-validated deployment. That is repeatability.

---

## Try With AI

Ask Claude: "Review my DEPLOYMENT-SPEC.md. Are there any production concerns I haven't addressed? Here is the spec: [paste your spec from Exercise 1]." Incorporate Claude's suggestions into your spec before implementing.

**What you're learning:** AI identifies gaps in specifications — backup strategy, update procedures, rollback plans — that specification authors commonly miss. A specification you think is complete often has blind spots that a second reviewer (human or AI) catches immediately.

Tell Claude your deployment constraints: "I'm deploying to a VPS with 1GB RAM and 20GB disk. The agent processes 100 requests/hour. Optimize my deployment for these constraints." Compare the response to your original MemoryMax and CPUQuota values.

**What you're learning:** Providing real constraints produces deployments optimized for YOUR situation, not generic best practices. An agent processing 100 requests per hour on a 1GB VPS needs very different resource limits than one handling 10,000 requests per hour on a 64GB server. AI can do the math if you give it the numbers.

After deployment, ask Claude: "My agent is deployed and passing health checks. What should I monitor over the next 24 hours to ensure stability? Create a monitoring checklist." Follow the checklist and report what you observe.

**What you're learning:** Production is not done at deployment — monitoring, alerting, and observability are ongoing responsibilities. The first 24 hours after deployment reveal patterns (memory growth, log volume, response time drift) that no amount of pre-deployment testing can predict.

:::note Safety Reminder
Production deployment involves system-level changes — creating users, modifying firewall rules, installing systemd services. Always test on a non-production server first (a VM, a cloud instance you can destroy, or a local container). Keep SSH access working at all times: if you lock yourself out by misconfiguring the firewall, you lose access to the server entirely. Run `sudo ufw status` before and after any firewall change to confirm you have not blocked your own SSH connection.
:::
