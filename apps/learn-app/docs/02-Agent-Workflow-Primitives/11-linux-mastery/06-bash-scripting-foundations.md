---
sidebar_position: 6
chapter: 11
lesson: 6
title: "Lesson 6: Bash Scripting Foundations"
description: "Write executable bash scripts with variables, error handling, functions, and control flow to automate repeatable agent deployment tasks."
keywords: ["bash scripting", "shell scripts", "error handling", "set -euo pipefail", "bash functions", "conditionals", "loops", "chmod", "shebang"]
duration_minutes: 55

# HIDDEN SKILLS METADATA
skills:
  - name: "Script Creation and Execution"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create executable bash scripts with shebang line and correct file permissions"

  - name: "Variables and Quoting"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can declare variables, use double-quoted expansion with ${VAR}, and apply command substitution"

  - name: "Error Handling with set Flags"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can implement set -euo pipefail and explain what each flag prevents"

  - name: "Bash Functions"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can define functions with local variables and parameters to encapsulate reusable logic"

  - name: "Conditionals and Tests"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can write if/else statements using [[ ]] tests for strings, files, and numeric comparisons"

  - name: "Loop Constructs"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can use for and while loops to iterate over file lists and repeat operations"

learning_objectives:
  - objective: "Write executable bash scripts with shebang and proper permissions"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates a script, sets permissions with chmod +x, and runs it successfully"

  - objective: "Use variables with proper quoting and error handling (set -euo pipefail)"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student writes a script using variables in double quotes and demonstrates that set -euo pipefail catches errors"

  - objective: "Implement functions for reusable script logic"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates functions with local variables and calls them with arguments"

  - objective: "Use conditionals (if/else, test) and loops (for, while) for control flow"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student writes scripts that branch on conditions and iterate over files"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "Shebang and script execution (#!/bin/bash, chmod +x)"
    - "Variables and quoting (\"${VAR}\")"
    - "Error handling (set -euo pipefail)"
    - "Functions with local variables and parameters"
    - "Conditionals (if/else, test, [[ ]])"
    - "Loops (for, while)"
  assessment: "6 concepts at B2 level (within 7-10 limit). Progressive complexity: each concept builds on the previous."

differentiation:
  extension_for_advanced: "Add trap for cleanup on script exit, implement getopts for command-line argument parsing, create functions that return values via stdout capture."
  remedial_for_struggling: "Focus on 3-line scripts first (shebang, one command, echo). Practice variable assignment and echo before moving to conditionals. Copy the error handling line (set -euo pipefail) as a template without memorizing it."

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Shell Customization and Tooling"
  key_points:
    - "set -euo pipefail is the single most important line in any bash script — it prevents silent failures that cause partial deployments and data loss"
    - "Variables must always be double-quoted (\"${VAR}\") — unquoted variables break on spaces and are the #1 source of bash bugs"
    - "Functions with local variables keep scripts organized — the deploy_agent pattern (name + port as arguments) is reused in the capstone (lesson 14)"
    - "Idempotent scripts (safe to run multiple times) are a production requirement — the check-before-create pattern should become default"
  misconceptions:
    - "Students think scripts will stop on errors by default — without set -e, bash happily continues after failures, potentially running destructive commands in wrong directories"
    - "Students confuse ${VAR} with $VAR — both work for simple cases, but ${VAR}log vs $VARlog demonstrates why braces matter for disambiguation"
    - "Students expect function arguments to work like Python (named parameters) — bash uses positional arguments ($1, $2) which must be documented in comments"
    - "Students forget chmod +x and try to debug 'Permission denied' as a code error rather than a permissions issue"
  discussion_prompts:
    - "Why is idempotency (safe to run multiple times) important for deployment scripts? What goes wrong if a setup script fails halfway and you re-run it?"
    - "The set -u flag prevents using undefined variables. How might this catch a typo that rm -rf ${TYPO}/ would otherwise turn into rm -rf /?"
  teaching_tips:
    - "Start with the 3-line script and build incrementally — adding variables, then error handling, then functions mirrors how real scripts evolve"
    - "Demo the broken.sh example (cd to nonexistent path, then rm) live — seeing a script continue after failure is the motivation for set -euo pipefail"
    - "The test operators table ([[ -d ]], [[ -f ]], [[ -z ]]) is a reference card moment — students will look this up repeatedly"
    - "Connect back to tmux session scripts from lesson 5 — students already wrote their first bash script there without realizing it"
  assessment_quick_check:
    - "Ask students to write a 3-line script: shebang, set -euo pipefail, and echo with a variable — verify they can make it executable and run it"
    - "Ask: what does set -euo pipefail do? (Expected: -e stops on errors, -u stops on undefined vars, -o pipefail catches pipe failures)"
    - "Give a function definition and ask students to call it with two arguments — verify they understand $1 and $2 positional parameters"

teaching_approach: "Progressive script building (3-line -> 10-line -> 30-line)"
modality: "Hands-on discovery with AI collaboration"

# Generation metadata
generated_by: "content-implementer"
created: "2026-02-09"
version: "1.0.0"
---

# Bash Scripting Foundations

In Lesson 5, you learned to keep terminal sessions alive across disconnections with tmux. Now you'll capture your knowledge as executable scripts -- reusable automation that runs the same way every time.

Every Digital FTE deployment involves a repeatable sequence: create directories, install dependencies, configure services, verify everything works. Typing these commands manually each time is slow and error-prone. One mistyped path or forgotten step can leave an agent partially deployed, silently broken.

Bash scripts solve this by encoding your deployment knowledge as executable files. A script captures the exact sequence, handles errors gracefully, and runs identically whether you execute it at 2 PM or 2 AM. By the end of this lesson, you'll write scripts that create agent workspaces, validate their own execution, and adapt to different environments through variables and functions.

---

## Your First Script: Three Lines

Every bash script starts with three elements: a shebang line, a command, and a way to run it.

Create a file called `hello-agent.sh`:

```bash
cat > /tmp/hello-agent.sh << 'EOF'
#!/bin/bash
echo "Agent deployment starting..."
echo "Timestamp: $(date)"
EOF
```

**Output:**
```
(no output -- the file was created silently)
```

The file exists but cannot run yet. Try executing it:

```bash
/tmp/hello-agent.sh
```

**Output:**
```
bash: /tmp/hello-agent.sh: Permission denied
```

Scripts need executable permission. Grant it with `chmod +x`:

```bash
chmod +x /tmp/hello-agent.sh
/tmp/hello-agent.sh
```

**Output:**
```
Agent deployment starting...
Timestamp: Sun Feb  9 14:30:00 UTC 2026
```

Three things made this work:

- `#!/bin/bash` -- The **shebang** tells the system which interpreter runs this file. Without it, the system doesn't know this is a bash script.
- `chmod +x` -- Adds **executable permission** so the file can be run as a program.
- `$(date)` -- **Command substitution** captures the output of `date` and inserts it into the string.

---

## Variables and Quoting

Hard-coded values break when anything changes. Variables make scripts flexible.

```bash
cat > /tmp/setup-agent.sh << 'EOF'
#!/bin/bash

AGENT_NAME="customer-support"
AGENT_DIR="/tmp/agents/${AGENT_NAME}"
LOG_DIR="${AGENT_DIR}/logs"

echo "Setting up ${AGENT_NAME}..."
echo "Directory: ${AGENT_DIR}"

mkdir -p "${AGENT_DIR}" "${LOG_DIR}"

echo "Created workspace for ${AGENT_NAME}"
EOF

chmod +x /tmp/setup-agent.sh
/tmp/setup-agent.sh
```

**Output:**
```
Setting up customer-support...
Directory: /tmp/agents/customer-support
Created workspace for customer-support
```

Verify the directories were created:

```bash
ls -R /tmp/agents/customer-support
```

**Output:**
```
/tmp/agents/customer-support:
logs

/tmp/agents/customer-support/logs:
```

### Why Quoting Matters

Always wrap variable expansions in double quotes. Without quotes, paths containing spaces break:

```bash
# WRONG -- breaks on spaces
DIR=/tmp/my agent
mkdir $DIR

# RIGHT -- preserves the full path
DIR="/tmp/my agent"
mkdir "${DIR}"
```

The `${VAR}` syntax with curly braces is clearest because it shows exactly where the variable name ends. Compare `$AGENT_NAMElog` (bash looks for variable `AGENT_NAMElog`) with `${AGENT_NAME}log` (bash uses `AGENT_NAME` and appends `log`).

### Environment Variables

Your scripts can read values set outside the script:

```bash
AGENT_NAME="sales-bot" /tmp/setup-agent.sh
```

**Output:**
```
Setting up sales-bot...
Directory: /tmp/agents/sales-bot
Created workspace for sales-bot
```

Same script, different agent -- no editing required.

---

## Error Handling: set -euo pipefail

Without error handling, scripts continue running after failures. This is dangerous for deployments.

### The Problem

```bash
cat > /tmp/broken.sh << 'EOF'
#!/bin/bash
cd /nonexistent/path
echo "This prints even though cd failed!"
rm -rf important-files/
EOF

chmod +x /tmp/broken.sh
/tmp/broken.sh
```

**Output:**
```
/tmp/broken.sh: line 2: cd: /nonexistent/path: No such file or directory
This prints even though cd failed!
```

The script kept running after `cd` failed. In a real deployment, subsequent commands would execute in the wrong directory.

### The Solution

Add `set -euo pipefail` immediately after the shebang:

```bash
cat > /tmp/safe.sh << 'EOF'
#!/bin/bash
set -euo pipefail

cd /nonexistent/path
echo "This never prints"
EOF

chmod +x /tmp/safe.sh
/tmp/safe.sh
```

**Output:**
```
/tmp/safe.sh: line 4: cd: /nonexistent/path: No such file or directory
```

The script stopped immediately. No further commands executed.

Each flag prevents a different class of bug:

| Flag | Prevents | Example |
|------|----------|---------|
| `set -e` | Continuing after errors | `cd /wrong/path` followed by `rm -rf *` |
| `set -u` | Using undefined variables | `rm -rf ${TYPO_VAR}/` deleting `/` |
| `set -o pipefail` | Hiding failures in pipes | `failing-cmd \| grep "ok"` masking the failure |

:::warning Always Use set -euo pipefail

This single line prevents the most common scripting disasters. Add it to every script you write, right after the shebang line. The one minute it takes to type saves hours of debugging silent failures.

:::

---

## Functions: Reusable Script Logic

When scripts grow beyond 20 lines, functions keep them organized and readable.

### Defining and Calling Functions

```bash
cat > /tmp/deploy-functions.sh << 'EOF'
#!/bin/bash
set -euo pipefail

create_workspace() {
    local agent_name="$1"
    local base_dir="/tmp/agents/${agent_name}"

    mkdir -p "${base_dir}"/{src,config,logs,data}
    echo "Created workspace: ${base_dir}"
}

verify_workspace() {
    local agent_name="$1"
    local base_dir="/tmp/agents/${agent_name}"

    if [[ -d "${base_dir}/src" ]] && [[ -d "${base_dir}/logs" ]]; then
        echo "Workspace verified: ${agent_name}"
    else
        echo "ERROR: Workspace incomplete for ${agent_name}" >&2
        return 1
    fi
}

# Main execution
create_workspace "analytics-engine"
verify_workspace "analytics-engine"
EOF

chmod +x /tmp/deploy-functions.sh
/tmp/deploy-functions.sh
```

**Output:**
```
Created workspace: /tmp/agents/analytics-engine
Workspace verified: analytics-engine
```

Key concepts in this script:

- `create_workspace()` -- Defines a function. Parentheses are required but always empty in bash.
- `local agent_name="$1"` -- `local` restricts the variable to this function. `$1` is the first argument passed to the function.
- `"$1"` -- Functions receive arguments positionally: `$1` is the first, `$2` the second, and so on.
- `return 1` -- Exits the function with error status (non-zero means failure).
- `>&2` -- Sends output to stderr (the error stream) instead of stdout.

### Functions with Multiple Arguments

```bash
cat > /tmp/multi-deploy.sh << 'EOF'
#!/bin/bash
set -euo pipefail

deploy_agent() {
    local name="$1"
    local port="$2"
    local base="/tmp/agents/${name}"

    mkdir -p "${base}"/{src,config,logs}
    echo "port: ${port}" > "${base}/config/settings.yaml"
    echo "Deployed ${name} on port ${port}"
}

deploy_agent "support-bot" 8000
deploy_agent "sales-bot" 8001
deploy_agent "analytics" 8002
EOF

chmod +x /tmp/multi-deploy.sh
/tmp/multi-deploy.sh
```

**Output:**
```
Deployed support-bot on port 8000
Deployed sales-bot on port 8001
Deployed analytics on port 8002
```

Verify one of the configurations:

```bash
cat /tmp/agents/support-bot/config/settings.yaml
```

**Output:**
```
port: 8000
```

One function, three deployments. This is how production scripts scale.

---

## Conditionals: Making Decisions

Scripts need to make decisions: Does a directory exist? Is a service running? Did the last command succeed?

### if/else with [[ ]] Tests

```bash
cat > /tmp/check-workspace.sh << 'EOF'
#!/bin/bash
set -euo pipefail

AGENT_NAME="${1:-customer-support}"
AGENT_DIR="/tmp/agents/${AGENT_NAME}"

if [[ -d "${AGENT_DIR}" ]]; then
    echo "${AGENT_NAME}: workspace exists at ${AGENT_DIR}"
    FILE_COUNT=$(ls "${AGENT_DIR}" | wc -l)
    echo "  Contains ${FILE_COUNT} items"
else
    echo "${AGENT_NAME}: workspace NOT found"
    echo "  Run setup script first"
fi
EOF

chmod +x /tmp/check-workspace.sh
/tmp/check-workspace.sh analytics-engine
```

**Output:**
```
analytics-engine: workspace exists at /tmp/agents/analytics-engine
  Contains 4 items
```

```bash
/tmp/check-workspace.sh nonexistent-agent
```

**Output:**
```
nonexistent-agent: workspace NOT found
  Run setup script first
```

Key patterns:

- `${1:-customer-support}` -- Uses the first argument if provided, otherwise defaults to `customer-support`.
- `[[ -d "${AGENT_DIR}" ]]` -- Tests if a directory exists. Double brackets `[[ ]]` are the modern, safer form.
- `$(ls "${AGENT_DIR}" | wc -l)` -- Command substitution counts items in the directory.

### Common Test Operators

| Test | Meaning |
|------|---------|
| `[[ -d path ]]` | Directory exists |
| `[[ -f path ]]` | Regular file exists |
| `[[ -z "${VAR}" ]]` | Variable is empty |
| `[[ -n "${VAR}" ]]` | Variable is not empty |
| `[[ "${A}" == "${B}" ]]` | Strings are equal |
| `[[ ${NUM} -gt 10 ]]` | Number is greater than 10 |

### Idempotent Directory Creation

A practical pattern -- creating directories only when they don't exist, with feedback:

```bash
cat > /tmp/safe-setup.sh << 'EOF'
#!/bin/bash
set -euo pipefail

setup_dir() {
    local dir_path="$1"
    if [[ -d "${dir_path}" ]]; then
        echo "Already exists: ${dir_path}"
    else
        mkdir -p "${dir_path}"
        echo "Created: ${dir_path}"
    fi
}

setup_dir "/tmp/agent-ws/logs"
setup_dir "/tmp/agent-ws/config"
setup_dir "/tmp/agent-ws/data"
EOF

chmod +x /tmp/safe-setup.sh
/tmp/safe-setup.sh
```

**Output (first run):**
```
Created: /tmp/agent-ws/logs
Created: /tmp/agent-ws/config
Created: /tmp/agent-ws/data
```

```bash
/tmp/safe-setup.sh
```

**Output (second run):**
```
Already exists: /tmp/agent-ws/logs
Already exists: /tmp/agent-ws/config
Already exists: /tmp/agent-ws/data
```

The script is **idempotent** -- safe to run multiple times without side effects.

---

## Loops: Repeating Operations

Loops let scripts process multiple items without duplicating code.

### for Loops

Iterate over a list of values:

```bash
cat > /tmp/setup-agents.sh << 'EOF'
#!/bin/bash
set -euo pipefail

AGENTS=("support-bot" "sales-bot" "analytics" "moderator")

for agent in "${AGENTS[@]}"; do
    mkdir -p "/tmp/agents/${agent}"/{src,config,logs}
    echo "Workspace ready: ${agent}"
done

echo "All ${#AGENTS[@]} agents configured"
EOF

chmod +x /tmp/setup-agents.sh
/tmp/setup-agents.sh
```

**Output:**
```
Workspace ready: support-bot
Workspace ready: sales-bot
Workspace ready: analytics
Workspace ready: moderator
All 4 agents configured
```

Key syntax:

- `AGENTS=("a" "b" "c")` -- Declares an array.
- `"${AGENTS[@]}"` -- Expands to all elements, each properly quoted.
- `${#AGENTS[@]}` -- The count of elements in the array.

### Iterating Over Files

Process all files matching a pattern:

```bash
cat > /tmp/count-logs.sh << 'EOF'
#!/bin/bash
set -euo pipefail

LOG_DIR="${1:-.}"

echo "Log file report for: ${LOG_DIR}"
echo "---"

for logfile in "${LOG_DIR}"/*.log; do
    if [[ -f "${logfile}" ]]; then
        lines=$(wc -l < "${logfile}")
        size=$(stat -c%s "${logfile}")
        echo "$(basename "${logfile}"): ${lines} lines, ${size} bytes"
    fi
done
EOF

chmod +x /tmp/count-logs.sh
```

Create some test log files and run it:

```bash
for i in 1 2 3; do
    for j in $(seq 1 $((i * 10))); do
        echo "Log entry ${j}" >> "/tmp/agents/support-bot/logs/agent-${i}.log"
    done
done

/tmp/count-logs.sh /tmp/agents/support-bot/logs/
```

**Output:**
```
Log file report for: /tmp/agents/support-bot/logs/
---
agent-1.log: 10 lines, 140 bytes
agent-2.log: 20 lines, 290 bytes
agent-3.log: 30 lines, 450 bytes
```

### while Loops

Use `while` for condition-based repetition:

```bash
cat > /tmp/wait-for-file.sh << 'EOF'
#!/bin/bash
set -euo pipefail

TARGET_FILE="${1:-/tmp/agent-ready.flag}"
MAX_WAIT=10
WAITED=0

echo "Waiting for ${TARGET_FILE}..."

while [[ ! -f "${TARGET_FILE}" ]] && [[ ${WAITED} -lt ${MAX_WAIT} ]]; do
    sleep 1
    ((WAITED++))
    echo "  Waiting... (${WAITED}/${MAX_WAIT}s)"
done

if [[ -f "${TARGET_FILE}" ]]; then
    echo "File found after ${WAITED} seconds"
else
    echo "ERROR: Timed out after ${MAX_WAIT} seconds" >&2
    exit 1
fi
EOF

chmod +x /tmp/wait-for-file.sh
```

Test it by creating the target file after a delay:

```bash
(sleep 3 && touch /tmp/agent-ready.flag) &
/tmp/wait-for-file.sh /tmp/agent-ready.flag
```

**Output:**
```
Waiting for /tmp/agent-ready.flag...
  Waiting... (1/10s)
  Waiting... (2/10s)
  Waiting... (3/10s)
File found after 3 seconds
```

This pattern is essential for deployment scripts that need to wait for services to become ready before proceeding.

---

## Exercises

### Exercise 1: Build an Agent Workspace

**Task:** Write a script that creates an agent workspace with `logs/`, `config/`, and `data/` subdirectories.

```bash
cat > /tmp/setup-workspace.sh << 'EOF'
#!/bin/bash
set -euo pipefail

WORKSPACE="/tmp/agent-ws"

mkdir -p "${WORKSPACE}"/{logs,config,data}
echo "Workspace created at ${WORKSPACE}"
EOF

chmod +x /tmp/setup-workspace.sh
```

**Verify:**

```bash
/tmp/setup-workspace.sh && ls /tmp/agent-ws/
```

**Expected output:**
```
Workspace created at /tmp/agent-ws
config  data  logs
```

All three directories should appear.

### Exercise 2: Add Idempotency and Functions

**Task:** Enhance the workspace script with `set -euo pipefail` and a function that checks if a directory exists before creating it. The second run should output "already exists" instead of recreating.

```bash
cat > /tmp/setup-workspace-v2.sh << 'EOF'
#!/bin/bash
set -euo pipefail

WORKSPACE="/tmp/agent-ws-v2"

ensure_dir() {
    local dir_path="$1"
    if [[ -d "${dir_path}" ]]; then
        echo "Already exists: $(basename "${dir_path}")"
    else
        mkdir -p "${dir_path}"
        echo "Created: $(basename "${dir_path}")"
    fi
}

ensure_dir "${WORKSPACE}/logs"
ensure_dir "${WORKSPACE}/config"
ensure_dir "${WORKSPACE}/data"
echo "Workspace ready at ${WORKSPACE}"
EOF

chmod +x /tmp/setup-workspace-v2.sh
```

**Verify (run twice):**

```bash
/tmp/setup-workspace-v2.sh
/tmp/setup-workspace-v2.sh
```

**Expected output (second run):**
```
Already exists: logs
Already exists: config
Already exists: data
Workspace ready at /tmp/agent-ws-v2
```

### Exercise 3: Process Log Files with a Loop

**Task:** Write a loop that processes all `.log` files in a directory and reports their line counts.

```bash
cat > /tmp/report-logs.sh << 'EOF'
#!/bin/bash
set -euo pipefail

LOG_DIR="${1:-.}"

for logfile in "${LOG_DIR}"/*.log; do
    if [[ -f "${logfile}" ]]; then
        lines=$(wc -l < "${logfile}")
        echo "$(basename "${logfile}"):${lines}"
    fi
done
EOF

chmod +x /tmp/report-logs.sh
```

**Verify:**

```bash
mkdir -p /tmp/test-logs
echo -e "line1\nline2\nline3" > /tmp/test-logs/app.log
echo -e "line1\nline2" > /tmp/test-logs/error.log
/tmp/report-logs.sh /tmp/test-logs/
```

**Expected output:**
```
app.log:3
error.log:2
```

Each line shows `filename:linecount` for every `.log` file in the directory.

---

## Try With AI

**Write a setup script and get a production review:**

```
Write a basic agent setup script that:
1. Creates a user called agent-runner
2. Creates directories /opt/agent/src, /opt/agent/config, /var/log/agents
3. Installs Python 3 and pip

Then review this script for production reliability. What error
conditions am I not handling? What happens if the disk is full,
the network is down, or the user already exists?
```

**What you're learning:** AI identifies failure modes you haven't experienced yet -- disk space exhaustion, network timeouts, duplicate user errors. These are the edge cases that separate development scripts from production-ready automation.

**Provide specific constraints and compare outputs:**

```
I need a setup script for a Python FastAPI agent that runs under
user agent-runner, stores logs in /var/log/agents/, and needs
Python 3.11 and uvicorn installed. Write this script with full
error handling (set -euo pipefail) and idempotent operations.

After generating it, tell me: what would happen if I ran this
script on a server where Python 3.11 isn't available in apt?
How should the script handle that case?
```

**What you're learning:** Providing precise constraints produces scripts tailored to your exact deployment. Asking "what if" questions surfaces assumptions the initial script makes implicitly.

**Iteratively refine edge case handling:**

```
Take the setup script you just generated. I tested it mentally
and found two problems:
1. If the agent-runner user already exists, useradd will fail
2. If /var/log/agents/ has wrong ownership, the agent can't write logs

Add handling for these edge cases. Then tell me what other edge
cases you can think of that we haven't addressed yet.
```

**What you're learning:** Iterative refinement catches real deployment issues that initial scripts miss. Each round of "what could go wrong?" makes the script more reliable.

:::note Safety Reminder
Always test scripts in a non-production environment first. Use a VM, container, or test server. A script with a typo in a path variable combined with `rm -rf` can cause irreversible damage. Preview destructive operations with `echo` before executing them for real.
:::
