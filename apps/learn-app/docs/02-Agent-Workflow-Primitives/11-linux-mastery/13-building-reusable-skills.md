---
sidebar_position: 13
chapter: 11
lesson: 13
title: "Lesson 13: Building Reusable Agent Operations Skills"
description: "Transform recurring deployment patterns from L05-L12 into reusable skills using the Persona + Questions + Principles format, creating portable automation that works on fresh systems."
keywords: ["reusable skills", "SKILL.md", "automation patterns", "deployment skill", "persona questions principles", "agent operations", "portable scripts", "fresh-system testing"]
duration_minutes: 55

# HIDDEN SKILLS METADATA
skills:
  - name: "Recurring Pattern Recognition"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student identifies 3+ recurring operational patterns from prior lessons and documents their trigger condition, steps, and expected outcome"

  - name: "Pattern-to-Skill Decision Framework"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student applies the frequency + complexity + value framework to decide which patterns justify becoming reusable skills"

  - name: "Skill File Authoring"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student writes a SKILL.md file with correct YAML frontmatter and Persona + Questions + Principles body structure"

  - name: "Deployment Skill Implementation"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student creates a comprehensive deploy-agent skill that encapsulates user creation, service installation, and health verification"

  - name: "Fresh-System Validation"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student tests a skill on a clean workspace with no prior configuration and identifies hidden assumptions that break portability"

learning_objectives:
  - objective: "Identify recurring operational patterns that justify creating reusable automation"
    proficiency_level: "C1"
    bloom_level: "Analyze"
    assessment_method: "Student documents 3+ recurring patterns from L05-L12 with trigger condition, steps, and expected outcome for each"

  - objective: "Design a deployment skill specification using Persona + Questions + Principles pattern"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Student writes a SKILL.md file with YAML frontmatter, persona definition, key questions, and operational principles"

  - objective: "Implement a reusable deployment script encapsulating L01-L12 knowledge"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Student creates a bash script that combines user creation, service file generation, permission setting, and health verification"

  - objective: "Test reusable skills on fresh systems to validate completeness"
    proficiency_level: "C1"
    bloom_level: "Evaluate"
    assessment_method: "Student runs their skill on a temporary workspace with no prior setup and identifies all hidden assumptions"

cognitive_load:
  new_concepts: 5
  concepts_list:
    - "Recognizing recurring operational patterns (from L05-L12 work)"
    - "Pattern-to-skill decision framework (frequency + complexity + value)"
    - "Skill file structure (SKILL.md with YAML frontmatter: name, description)"
    - "Creating a linux-agent-ops skill (Persona + Questions + Principles)"
    - "Testing skills on fresh systems (hidden assumptions, portability)"
  assessment: "5 concepts at C1 level (within the 4-7 range). Progressive abstraction: recognize patterns -> decide which to formalize -> write the skill file -> implement as script -> validate on fresh system."

differentiation:
  extension_for_advanced: "Parameterize the skill to handle multiple runtimes (Python, Node.js, Go), add GPU passthrough support, or create a skill library with dependency resolution between skills."
  remedial_for_struggling: "Start by listing every command you ran in L10 and L11. Group commands that always appear together. That grouping is your first pattern. Write the skill file for just that one pattern before adding more."

teaching_guide:
  lesson_type: "core"
  session_group: 5
  session_title: "Skills, Capstone, and Practice"
  key_points:
    - "Recurring patterns (useradd + chmod + service file + health check) should become reusable skills — this is the transition from manual operations to encoded expertise"
    - "The Persona + Questions + Principles format structures a skill so AI agents can execute it without supervision — this is how Digital FTEs scale"
    - "Fresh-system testing exposes hidden assumptions (pre-existing users, installed packages, directory structures) that break portability — always test on a clean workspace"
    - "The pattern-to-skill decision framework (frequency + complexity + value) prevents over-engineering — not every pattern deserves to be a skill"
  misconceptions:
    - "Students think skills are just scripts with a fancy name — a skill includes persona (who executes), questions (decision logic), and principles (guardrails), not just commands"
    - "Students assume their deployment works everywhere because it works on their machine — fresh-system testing reveals dependencies on pre-existing state that scripts silently rely on"
    - "Students try to make every pattern a skill — the decision framework exists to filter; only patterns that recur frequently AND are complex AND have high value should become skills"
  discussion_prompts:
    - "Look back at lessons 5-12. Which operational patterns did you repeat most often? Which of those would benefit from being encoded as a reusable skill?"
    - "What is the difference between a bash script and a skill? Why would you write a SKILL.md file instead of just saving the script?"
  teaching_tips:
    - "Have students list their most-repeated command sequences from lessons 5-12 before introducing the skill format — this makes the abstraction concrete"
    - "The pattern-to-skill decision framework (3 questions: how often, how complex, how valuable) is a reference card moment — students should evaluate at least 5 patterns against it"
    - "Walk through the complete SKILL.md structure with the deploy-agent example — seeing a real skill file is more effective than describing the format"
    - "The fresh-system validation exercise is the most important part — it teaches a mindset (test assumptions) that applies far beyond this lesson"
  assessment_quick_check:
    - "Ask students to name 3 recurring patterns from lessons 5-12 and explain which one they would turn into a skill first (using the frequency + complexity + value criteria)"
    - "Ask: what are the three sections of a skill's body? (Expected: Persona, Questions, Principles)"
    - "Ask: your skill works on your machine but fails on a clean server. What is the most likely cause? (Expected: hidden assumptions about pre-existing users, packages, or directories)"

teaching_approach: "Progressive abstraction (Pattern Recognition -> Decision Framework -> Skill Authoring -> Implementation -> Validation)"
modality: "Hands-on skill creation with AI collaboration"

# Generation metadata
generated_by: "content-implementer v2.0.0"
created: "2026-02-11"
version: "2.0.0"
---

# Building Reusable Agent Operations Skills

You have deployed agents five or more times following similar patterns across Lessons 5 through 12. Every time: create a user, set permissions, write a service file, enable the service, verify health. You have typed `sudo useradd` so many times you could do it blindfolded. You have written `Restart=on-failure` into enough service files that your fingers type it automatically.

This chapter's thesis: recurring patterns should become reusable intelligence. Every time you repeated a deployment sequence, you were executing tacit knowledge -- expertise locked inside your head. Time to extract those patterns into a structured, portable skill file that an AI coding agent can use without your supervision.

---

## Recognizing Recurring Patterns

Before you can formalize anything, you need to see the repetition clearly. Look back at your work in Lessons 5 through 12:

| Operation | Lessons Where It Appeared | Count |
|-----------|--------------------------|-------|
| Create a dedicated user (`useradd`) | L07, L08, L10, L12 | 4+ |
| Set file permissions (`chown`, `chmod`) | L05, L07, L08, L10, L11, L12 | 6+ |
| Write a systemd service file | L10, L12 | 3+ |
| Enable and start a service | L10, L12 | 3+ |
| Verify a health endpoint (`curl /health`) | L10, L11, L12 | 4+ |
| Write a bash script with `set -euo pipefail` | L06, L08, L12 | 3+ |

That is not coincidence. That is a pattern.

### When Does a Pattern Deserve to Become a Skill?

Not every repeated command needs a skill file. Apply three criteria:

| Criterion | Threshold | Why |
|-----------|-----------|-----|
| **Frequency** | Recurring 2+ times | One-off operations are not worth formalizing |
| **Complexity** | More than 3 steps | Simple commands do not need orchestration |
| **Value** | Saves time or prevents errors | Creation effort must pay for itself |

Apply the framework:

| Pattern | Freq | Complex | Value | Verdict |
|---------|------|---------|-------|---------|
| Create user + set permissions | 4+ | 4 steps | Prevents security mistakes | **Skill** |
| Write + enable systemd service | 3+ | 5 steps | Prevents config errors | **Skill** |
| Health check sequence | 4+ | 3 steps | Catches silent failures | **Skill** |
| Run `ls` | 100+ | 1 step | Trivial | Not a skill |
| Full deploy pipeline (all above) | 3+ | 12+ steps | Saves 20+ min per deploy | **Skill** |

The full deployment pipeline passes all three thresholds. That is what you will formalize.

---

## The Skill File Structure

### Directory and Frontmatter

```
.claude/skills/linux-agent-ops/SKILL.md
```

Every SKILL.md starts with YAML frontmatter:

```yaml
---
name: linux-agent-ops
description: |
  Expert guidance for deploying AI agents as systemd services on Linux.
  Use when creating agent users, writing service files, setting permissions,
  or verifying agent health. Covers the full deploy-verify-monitor cycle.
---
```

Two fields: `name` and `description`. The description must be specific enough that an AI agent knows when to invoke it.

### Body: Persona + Questions + Principles

After the frontmatter, the body follows a three-part pattern:

- **Persona** defines the expertise level and mindset
- **Questions** define what the skill needs to know before acting
- **Principles** define rules the skill never violates



---

## Creating Your Deploy-Agent Skill

Build the complete SKILL.md by constructing each section from chapter experience.

### Persona

```markdown
## Persona

You are a Linux operations engineer deploying AI agents to production
servers. Every step must be repeatable, every failure must be recoverable,
and nothing runs as root unless absolutely necessary.
```

### Key Questions

These come directly from variations you encountered across the chapter:

```markdown
## Key Questions

1. **What user should own the agent process?**
   Default: Dedicated `agent-runner` user with no login shell.

2. **What port does the agent listen on?**
   Default: 8000. Must not conflict with other services.

3. **What restart policy?**
   Default: Restart=on-failure with RestartSec=5. Never Restart=always.

4. **What resource limits?**
   Default: MemoryMax=512M, CPUQuota=50%.

5. **How to verify health?**
   Default: HTTP GET to /health returns 200.

6. **What runtime?**
   Options: Python (uvicorn), Node.js (node), compiled binary.
```

Each question has a default. Defaults make skills fast -- you only override what differs.

### Principles

Hard-won lessons encoded as rules:

```markdown
## Principles

1. Never run agents as root. Create a dedicated user.
2. Always use Restart=on-failure, never Restart=always.
3. Always set MemoryMax and CPUQuota resource limits.
4. Always include StartLimitBurst and StartLimitIntervalSec.
5. Always verify health after deployment via /health endpoint.
6. Script everything you do more than once.
```

Combine all three sections (persona, questions, principles) plus an Implementation section listing deploy steps into a single `.claude/skills/linux-agent-ops/SKILL.md` file. The implementation steps are: create user, create directory, set ownership, write service file, daemon-reload, enable, start, verify health.

An AI coding agent reads this file, understands the procedure, asks the right questions, follows the principles, and executes -- without a human walking it through.

---

## Implementing the Skill as a Script

The skill specification tells an AI agent *what* to do. This script *does* it. It combines user creation (L07), service file writing (L10), permissions (L05), and [health verification from Lesson 10](10-process-control-systemd.md):

```bash
#!/bin/bash
# deploy-agent.sh — Implements the linux-agent-ops skill
# Usage: sudo ./deploy-agent.sh <agent-name> <port> <exec-start-cmd>
set -euo pipefail

AGENT_NAME="${1:?Usage: deploy-agent.sh <name> <port> <exec-start>}"
AGENT_PORT="${2:?Missing port}"
EXEC_START="${3:?Missing ExecStart command}"
AGENT_USER="agent-runner"
AGENT_DIR="/opt/${AGENT_NAME}"
SERVICE_FILE="/etc/systemd/system/${AGENT_NAME}.service"

echo "=== Deploying ${AGENT_NAME} on port ${AGENT_PORT} ==="

# Step 1: Create dedicated user
if id "${AGENT_USER}" &>/dev/null; then
    echo "[OK] User ${AGENT_USER} exists"
else
    useradd -r -s /usr/sbin/nologin "${AGENT_USER}"
    echo "[OK] Created user ${AGENT_USER}"
fi

# Step 2: Create directory
mkdir -p "${AGENT_DIR}"
chown -R "${AGENT_USER}:${AGENT_USER}" "${AGENT_DIR}"
echo "[OK] Directory ${AGENT_DIR} ready"

# Step 3: Write systemd service file
cat > "${SERVICE_FILE}" <<EOF
[Unit]
Description=AI Agent: ${AGENT_NAME}
After=network.target
StartLimitIntervalSec=60
StartLimitBurst=5

[Service]
Type=simple
User=${AGENT_USER}
WorkingDirectory=${AGENT_DIR}
ExecStart=${EXEC_START}
Restart=on-failure
RestartSec=5
MemoryMax=512M
CPUQuota=50%

[Install]
WantedBy=multi-user.target
EOF
echo "[OK] Service file written"

# Step 4: Enable and start
systemctl daemon-reload
systemctl enable "${AGENT_NAME}"
systemctl start "${AGENT_NAME}"
echo "[OK] Service enabled and started"

# Step 5: Verify health
sleep 5
if systemctl is-active --quiet "${AGENT_NAME}"; then
    echo "[OK] Service is running"
else
    echo "[FAIL] Service failed to start"
    journalctl -u "${AGENT_NAME}" --no-pager -n 10
    exit 1
fi

if curl -sf "http://localhost:${AGENT_PORT}/health" > /dev/null 2>&1; then
    echo "[OK] Health endpoint responding"
else
    echo "[WARN] Health endpoint not responding"
fi

echo "=== Deployment complete: ${AGENT_NAME} ==="
```

**Expected output:**

```
=== Deploying my-agent on port 8000 ===
[OK] Created user agent-runner
[OK] Directory /opt/my-agent ready
[OK] Service file written
[OK] Service enabled and started
[OK] Service is running
[OK] Health endpoint responding
=== Deployment complete: my-agent ===
```

Every principle maps to the script:

| Principle | Script Implementation |
|-----------|----------------------|
| Never run as root | `User=${AGENT_USER}` in service file |
| Restart=on-failure | `Restart=on-failure` with `RestartSec=5` |
| Resource limits | `MemoryMax=512M`, `CPUQuota=50%` |
| Start-limit protection | `StartLimitBurst=5`, `StartLimitIntervalSec=60` |
| Verify health | `curl` to `/health` after startup |
| Script everything | The script replaces 12+ manual commands |

---

## Testing Skills on Fresh Systems

Your script works on your server. Done?

Not yet. Your development server has accumulated state: users already created, packages installed, directories existing. Your script may silently depend on that accumulated state.

### Common Hidden Assumptions

| Assumption | What Breaks | Fix |
|------------|-------------|-----|
| Python is installed | `uvicorn` not found | Add dependency check |
| `curl` is installed | Health check fails | Check `command -v curl` |
| Network is available | `curl` times out | Add readiness check |
| Previous service exists | Stale config loaded | Script writes fresh file |

### Validation Approach

Run prerequisite and post-deployment checks from a clean starting point. Check that `curl`, `systemctl`, and `useradd` exist before deploying, then verify that the user was created, the service file exists, the service is active, and the health endpoint responds. If any prerequisite fails on a fresh system, add a dependency check to the top of your deploy script:

```bash
# Add after set -euo pipefail in deploy-agent.sh
for cmd in curl systemctl useradd; do
    command -v "${cmd}" &>/dev/null || { echo "[FAIL] Missing: ${cmd}"; exit 1; }
done
echo "[OK] All prerequisites available"
```

**Expected output:**
```
[OK] All prerequisites available
```

This turns a mysterious mid-deployment failure into an immediate, clear error at the start.

---

## Connection to the Agent Factory Thesis

**Without the skill**: SSH in, type 12 commands from memory, hope you remember the right MemoryMax value. Takes 20 minutes. Error-prone. Cannot be delegated.

**With the skill**: An AI coding agent reads your SKILL.md, asks the right questions, follows the principles, runs the script. Takes 2 minutes. Consistent. Fully delegatable.

That gap -- between manual expertise and delegatable intelligence -- is the core of Digital FTE construction. Every skill you create makes your AI agents more capable. Every principle you encode prevents a class of errors permanently. This is how individual expertise becomes organizational capability.

---

## Exercises

### Exercise 1: Document Recurring Patterns

List three recurring operational patterns from Lessons 5 through 12 that you performed more than twice. For each, document:

- **Trigger condition**: What situation causes this pattern
- **Steps**: The exact command sequence
- **Expected outcome**: What success looks like

Example format:

```
Pattern: Create Dedicated Agent User
Trigger: Deploying a new agent that needs process isolation
Steps:
  1. sudo useradd -r -s /usr/sbin/nologin agent-runner
  2. sudo mkdir -p /opt/<agent-name>
  3. sudo chown -R agent-runner:agent-runner /opt/<agent-name>
Expected outcome: User exists, directory exists, ownership correct
```

**Verification**: Each pattern must have all three elements. A pattern without a trigger condition is just a procedure -- you need to know *when* to use it.

### Exercise 2: Write a Skill Specification

Write a SKILL.md for "deploy-agent" with YAML frontmatter (`name`, `description`), a Persona section, Key Questions (at least five covering user creation, service config, permissions, monitoring, validation), and Principles (at least four rules).

```bash
mkdir -p /tmp/test-skill/deploy-agent
nano /tmp/test-skill/deploy-agent/SKILL.md
```

**Verification** -- check that all five deployment dimensions appear:

```bash
grep -ci "user" /tmp/test-skill/deploy-agent/SKILL.md
grep -ci "service\|systemd" /tmp/test-skill/deploy-agent/SKILL.md
grep -ci "permission\|chown\|chmod" /tmp/test-skill/deploy-agent/SKILL.md
grep -ci "health\|monitor" /tmp/test-skill/deploy-agent/SKILL.md
grep -ci "valid\|verif\|test" /tmp/test-skill/deploy-agent/SKILL.md
```

**Expected output** (each line should show at least 1):
```
3
4
2
3
2
```

### Exercise 3: Implement and Test the Skill

Use the `deploy-agent.sh` from this lesson. Test it on a fresh `/tmp` workspace:

```bash
TEST_DIR=$(mktemp -d)
cp deploy-agent.sh "${TEST_DIR}/"
cd "${TEST_DIR}"
```

**Verification** -- all four checks must pass:

```bash
id agent-runner && echo "1. User: PASS" || echo "1. User: FAIL"
systemd-analyze verify /etc/systemd/system/my-agent.service 2>&1 \
  && echo "2. Service file: PASS" || echo "2. Service file: FAIL"
systemctl is-active my-agent \
  && echo "3. Running: PASS" || echo "3. Running: FAIL"
curl -sf http://localhost:8000/health \
  && echo "4. Health: PASS" || echo "4. Health: FAIL"
```

**Expected output:**
```
1. User: PASS
2. Service file: PASS
3. Running: PASS
4. Health: PASS
```

---

## Try With AI

**Formalize your deployment knowledge into a reusable skill:**

```
I've deployed agents 5 times following a similar pattern: create user,
set permissions, write service file, enable service, verify health.
Help me formalize this as a reusable deployment skill with a Persona,
Questions, and Principles structure.
```

What you're learning: AI helps transform tacit operational knowledge into explicit, structured, reusable intelligence. Notice how AI organizes the messy experience of "things I do every time" into clean categories. Compare the structure AI produces with the Persona + Questions + Principles pattern from this lesson.

**Parameterize the skill for real-world variation:**

```
Sometimes the agent uses Python, sometimes Node.js. Ports vary. Some
need GPU access. Refine the skill to handle these variations with
parameters instead of hardcoded values.
```

What you're learning: Good skill design is parameterized for variation, not hardcoded for one scenario. Watch how AI introduces variables, default values, and conditional logic. The best skills work for the common case without configuration and adapt to edge cases with minimal overrides.

**Test the skill by simulating a fresh system:**

```
Test my deploy-agent skill specification by mentally running it on a
fresh Ubuntu 22.04 server with nothing installed. What steps would
fail? What prerequisites am I assuming?
```

What you're learning: Fresh-system testing reveals hidden assumptions that make skills fail outside your configured environment. AI will likely identify missing package installations, assumed directory structures, and network dependencies. Every assumption AI catches is a portability bug fixed before it bites you in production.

:::note Safety Reminder
Always test deployment scripts on a non-production server or temporary virtual machine first. A script with `set -euo pipefail` stops on errors, but a script without it may continue after a failure, leaving your system partially configured. Verify every deployment on a clean test system before running it against production infrastructure.
:::
