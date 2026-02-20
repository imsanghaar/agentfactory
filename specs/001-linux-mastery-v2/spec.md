# Feature Specification: Linux Mastery for Digital FTEs v2.0

**Feature Branch**: `001-linux-mastery-v2`
**Created**: 2026-02-08
**Status**: Draft
**Input**: Comprehensive rewrite addressing 21 identified issues from in-depth chapter analysis
**Supersedes**: `specs/001-linux-mastery/spec.md` (v1.0)

## Executive Summary

This specification defines the **v2 rewrite** of Chapter 10: Linux Mastery for Digital FTEs. The v1 chapter (9 lessons, grade B+) has been analyzed and found to have critical gaps: missing foundational topics (file operations, SSH, text editing, networking basics), oversized lessons requiring splits (L4 and L8), a visible/formulaic Three Roles Framework violating content rules, factual inaccuracies (`stat -f%z` macOS syntax), contradictory prerequisites (references to non-existent Chapters 40-42), and redundant content (health check scripts repeated 4 times).

The v2 restructures the chapter from 9 lessons to **13 lessons + 1 quiz**, adding 4 new lessons for critical missing topics and splitting 2 oversized lessons. All lessons will have the Three Roles Framework made **invisible** (no explicit "AI as Teacher/Student/Co-Worker" labels). Factual errors, code bugs, and prerequisite references will be corrected.

**Target grade**: A- (from current B+)

## Change Summary (v1 → v2)

| Change Type | Count | Details |
| --- | --- | --- |
| New lessons added | 4 | File Operations, Text Editing & Pipes, Networking Basics, SSH Remote Access |
| Lessons split | 2 | L4 → 2 lessons (Scripting + Text Processing), L8 → 2 lessons (Patterns + Skills) |
| Lessons rewritten | 9 | All existing lessons updated for Three Roles invisibility, factual fixes, exercises |
| Factual fixes | 3 | `stat -f%z` → `stat -c%s`, Restart= contradiction, psutil install |
| Structural fixes | 3 | Prerequisites corrected, quiz syntax fixed, redundant health scripts consolidated |
| Content additions | 2 | Interactive exercises with verification, networking fundamentals before debugging |

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Basic computer literacy (files, directories, applications)
- Concept of "servers" vs "personal computers"
- What an "AI agent" is (from Part 1 chapters on agent foundations)
- Basic command-line exposure (from earlier chapters using git)
- Understanding that code runs on servers somewhere

**What this chapter must explain from scratch**:
- Linux filesystem structure (/, /home, /etc, /var, /usr)
- What a "shell" is and how it differs from a terminal
- Basic file operations (create, copy, move, delete, read)
- Text editing in the terminal (nano basics)
- Pipe philosophy and stdin/stdout/stderr
- Networking fundamentals (ports, localhost, curl)
- SSH protocol and remote server access
- sudo and root user concept
- Permissions model (user/group/others, read/write/execute)
- What a "daemon" or "service" is
- Environment variables and scoping (export vs no export)
- System logging concepts

**Prerequisites corrected from v1**:
- ~~Chapter 9 (version control)~~ → Part 1 agent foundations only
- ~~Chapter 11 (AI agents)~~ → Part 1 covers this; no forward references
- ~~Chapters 40-42 (FastAPI)~~ → REMOVED entirely. No FastAPI knowledge assumed. Chapter provides its own sample agent files.
- "No prior Linux experience required" is now genuinely true — no contradictions

## User Scenarios & Testing

### User Story 1 - Terminal Fundamentals & File Mastery (Priority: P1)

A student new to Linux needs to develop core CLI fluency: navigating the filesystem, creating/copying/moving/deleting files, reading file contents, and understanding the filesystem hierarchy — all before touching any tooling or customization.

**Why this priority**: Without basic file operations, students cannot do anything productive. Navigation alone (v1 L1) is insufficient — students need to manipulate files from day one. This is the absolute foundation.

**Independent Test**: Student can navigate to any directory, create a directory structure, copy/move files between directories, read file contents with cat/head/tail/less, use wildcards for batch operations, and find help with man/--help.

**Acceptance Scenarios**:

1. **Given** a fresh terminal session, **When** student runs `pwd`, `ls -la`, `cd`, **Then** they can navigate to any directory and understand their location in the filesystem
2. **Given** need to create project structure, **When** student uses `mkdir -p`, `touch`, **Then** directory tree is created correctly
3. **Given** existing files, **When** student uses `cp`, `mv`, `rm`, **Then** files are copied/moved/deleted safely (with `-i` flag awareness)
4. **Given** a text file, **When** student uses `cat`, `head -n`, `tail -n`, `less`, **Then** they can read specific portions of file content
5. **Given** a directory of mixed files, **When** student uses wildcards (`*.log`, `agent-*`), **Then** they can target specific file groups
6. **Given** an unfamiliar command, **When** student uses `man` or `--help`, **Then** they can find usage information independently

---

### User Story 2 - Text Editing, Pipes & Modern Terminal Environment (Priority: P1)

A student needs to edit configuration files in the terminal, understand how Linux commands compose via pipes and I/O streams, install packages, and set up modern productivity tools — before moving to more complex topics.

**Why this priority**: Students are told to "edit with nano" throughout the chapter but never learn it. Pipes are the Unix superpower but are used without explanation. Package management gates all tool installation.

**Independent Test**: Student can edit files with nano, understand stdin/stdout/stderr, pipe commands together, install packages with apt, and configure shell aliases and environment variables.

**Acceptance Scenarios**:

1. **Given** need to edit a config file, **When** student opens nano, **Then** they can navigate, edit, save (Ctrl+O), and exit (Ctrl+X)
2. **Given** a command that produces output, **When** student pipes to `grep` or `wc`, **Then** they understand data flows through stdin/stdout
3. **Given** error messages mixed with output, **When** student uses `2>`, `2>&1`, `>`, `>>`, **Then** they can separate and redirect streams
4. **Given** need to install a tool, **When** student runs `sudo apt update && sudo apt install`, **Then** package installs with understanding of each step
5. **Given** repetitive commands, **When** student creates aliases in `.bashrc`, **Then** shortcuts work in new terminal sessions after `source`
6. **Given** modern navigation needs, **When** student installs zoxide and fzf, **Then** they can jump directories and search history efficiently

---

### User Story 3 - Persistent Sessions with tmux (Priority: P2)

A student working on long-running agent tasks needs terminal sessions that survive disconnections and enable multi-pane workflows for monitoring and editing simultaneously.

**Why this priority**: AI agents run for hours or days. Sessions must persist beyond connection drops. This is critical for production agent management but requires file and editing basics first.

**Independent Test**: Student can create tmux sessions, split panes, detach safely, reattach after disconnect, and create session scripts for repeatable layouts.

**Acceptance Scenarios**:

1. **Given** a remote server connection, **When** student creates tmux session, **Then** session persists after SSH disconnect
2. **Given** need for side-by-side monitoring, **When** student splits panes horizontally/vertically, **Then** they can view logs alongside code
3. **Given** multiple projects, **When** student creates named sessions, **Then** they can switch between project contexts instantly
4. **Given** a complex preferred layout, **When** student writes a session script, **Then** exact layout is reproducible with one command
5. **Given** an accidentally closed terminal, **When** student reattaches (`tmux a -t name`), **Then** all processes and layout are intact

---

### User Story 4 - Bash Scripting Foundations (Priority: P1)

A student needs to automate repetitive agent management tasks by writing bash scripts with proper error handling, variables, functions, and control flow.

**Why this priority**: Automation is core to the "Digital FTE" concept. This covers scripting fundamentals only — text processing is separated into its own lesson to manage cognitive load.

**Independent Test**: Student can write executable .sh scripts with shebang, variables, error handling (`set -euo pipefail`), functions, conditionals, and loops.

**Acceptance Scenarios**:

1. **Given** repetitive agent setup steps, **When** student writes bash script with `#!/bin/bash` and `set -euo pipefail`, **Then** setup executes consistently and fails safely on error
2. **Given** configurable values, **When** student uses variables with proper quoting (`"${VAR}"`), **Then** scripts handle spaces and special characters correctly
3. **Given** reusable logic, **When** student writes functions, **Then** common operations are encapsulated and testable
4. **Given** conditional requirements, **When** student uses if/else and test commands, **Then** scripts adapt to different environments
5. **Given** multiple items to process, **When** student uses for/while loops, **Then** batch operations execute efficiently

---

### User Story 5 - Text Processing & Automation (Priority: P1)

A student needs to parse logs, extract data, transform text, and schedule automated tasks using Linux text processing tools and cron.

**Why this priority**: Split from v1's overloaded L4. Text processing (grep/sed/awk) and automation (cron) are distinct skill areas that deserve focused attention. Log parsing is essential for agent debugging.

**Independent Test**: Student can use grep for pattern matching, sed for text transformation, awk for field extraction, chain them via pipes, and create cron jobs for scheduled tasks.

**Acceptance Scenarios**:

1. **Given** large log files, **When** student uses `grep -E` with regex, **Then** they can find specific patterns (errors, timestamps, IPs)
2. **Given** need to transform text, **When** student uses `sed 's/old/new/g'`, **Then** text is modified in-place or in pipeline
3. **Given** structured data (CSV, logs), **When** student uses `awk '{print $1, $3}'`, **Then** specific columns/fields are extracted
4. **Given** multi-step data pipeline, **When** student chains grep | sed | awk, **Then** complex transformations execute in single command
5. **Given** periodic agent health checks, **When** student creates cron job with `crontab -e`, **Then** checks run automatically on schedule with correct permissions

---

### User Story 6 - Security Hardening & Least Privilege (Priority: P1)

A student deploying production AI agents needs to implement security best practices: dedicated users, file permissions, SSH key authentication, and secret management.

**Why this priority**: Security is non-negotiable for production systems. Running agents as root or hardcoding credentials creates unacceptable risk.

**Independent Test**: Student can create dedicated agent users, restrict file permissions, generate SSH key pairs, configure key-based authentication, and pass secrets via environment variables with proper scoping.

**Acceptance Scenarios**:

1. **Given** new agent deployment, **When** student creates dedicated non-root user with `useradd`, **Then** agent runs with minimal required permissions
2. **Given** sensitive configuration files, **When** student uses `chmod 600` and `chown`, **Then** files are readable only by necessary users
3. **Given** need for secure remote access, **When** student generates SSH keys with `ssh-keygen`, **Then** they can authenticate without passwords
4. **Given** need to restrict access, **When** student disables password-based SSH login in `sshd_config`, **Then** only key-based auth is permitted
5. **Given** API keys needed for agent, **When** student uses `export` in `.env` files (sourced, not committed), **Then** credentials are never hardcoded
6. **Given** confusion about variable scoping, **When** student tests `export` vs non-exported variables in subshells, **Then** they understand which processes can see which variables

---

### User Story 7 - Networking Fundamentals & SSH Remote Access (Priority: P1)

A student needs to understand networking concepts (ports, localhost, protocols) and establish SSH connections to remote servers before learning process management or debugging.

**Why this priority**: v1 had no networking lesson and no SSH lesson — both are critical missing topics. The capstone assumes nginx and SSH knowledge never taught. This lesson fills both gaps.

**Independent Test**: Student can explain ports, localhost vs 0.0.0.0, use curl for HTTP requests, establish SSH connections, configure SSH config files, and test connectivity.

**Acceptance Scenarios**:

1. **Given** an agent listening on port 8000, **When** student uses `curl localhost:8000`, **Then** they understand what "port" means and can test locally
2. **Given** need to understand network addresses, **When** student compares `127.0.0.1` vs `0.0.0.0`, **Then** they know why binding matters for remote access
3. **Given** a remote server, **When** student uses `ssh user@host`, **Then** they can connect and execute commands remotely
4. **Given** multiple remote servers, **When** student configures `~/.ssh/config`, **Then** they can connect with short aliases (`ssh prod-server`)
5. **Given** a network connectivity issue, **When** student uses layered diagnostics (ping → curl → ss), **Then** they can isolate failure at correct layer
6. **Given** a firewall requirement, **When** student uses basic `ufw` commands (allow/deny/status), **Then** they can manage port access for agents

---

### User Story 8 - Process Control & Systemd Services (Priority: P1)

A student needs to deploy AI agents as system services that automatically restart on failure, start on boot, and can be monitored for resource consumption.

**Why this priority**: Production agents must be reliable. Systemd makes agents "unkillable" by auto-restarting and ensures they survive server reboots.

**Independent Test**: Student can write .service files, enable services, configure restart policies correctly from the start, monitor processes, and set resource limits.

**Acceptance Scenarios**:

1. **Given** agent that needs to run continuously, **When** student writes a `.service` file with `Restart=on-failure`, **Then** agent runs as managed service and restarts correctly on crash
2. **Given** server reboot, **When** service is enabled with `systemctl enable`, **Then** agent starts automatically without manual intervention
3. **Given** need to check service status, **When** student uses `systemctl status` and `journalctl -u`, **Then** they can see running state and recent logs
4. **Given** agent consuming excessive resources, **When** student adds `MemoryMax=` and `CPUQuota=` to service file, **Then** resource consumption is bounded
5. **Given** multiple similar agents, **When** student creates a service template (`agent@.service`), **Then** they can manage instances with `systemctl start agent@1`

**Factual fix from v1**: Lessons will teach `Restart=on-failure` as the production-correct default from the start, not `Restart=always` followed by a correction. The pedagogical contradiction is eliminated.

---

### User Story 9 - Debugging & Troubleshooting (Priority: P2)

A student troubleshooting agent issues needs to diagnose problems using structured analysis of logs, network, disk, and processes.

**Why this priority**: When agents fail (and they will), students need systematic debugging skills. This lesson now builds on networking fundamentals already taught.

**Independent Test**: Student can use journalctl for log analysis, diagnose network failures layered approach, identify disk space issues, and apply structured troubleshooting methodology.

**Acceptance Scenarios**:

1. **Given** a failed systemd service, **When** student uses `journalctl -u agent.service --since "1 hour ago"`, **Then** they can identify the error
2. **Given** agent timeout errors, **When** student applies layered network diagnosis (local → DNS → remote), **Then** they isolate failure point
3. **Given** server running slowly, **When** student checks disk with `df -h` and finds culprit with `du -sh /var/log/*`, **Then** they can free space
4. **Given** mysterious agent behavior, **When** student uses `strace -p PID` or `tail -f` on logs, **Then** they can observe real-time behavior
5. **Given** multiple simultaneous issues, **When** student applies structured triage (check logs → check network → check disk → check processes), **Then** they resolve issues methodically

---

### User Story 10 - Advanced Workflow Integration Patterns (Priority: P2)

A student ready to combine individual Linux skills into production workflows needs to learn deployment patterns, zero-downtime strategies, and monitoring approaches.

**Why this priority**: Split from v1's oversized L8. This lesson focuses on combining skills into coherent workflows — the "integration" phase before the capstone.

**Independent Test**: Student can implement a multi-step deployment workflow, configure basic monitoring, and choose appropriate patterns for different scenarios.

**Acceptance Scenarios**:

1. **Given** need to deploy updated agent, **When** student uses blue-green deployment pattern (new service alongside old), **Then** downtime is minimized
2. **Given** multiple Linux skills learned, **When** student combines them (script + systemd + monitoring + security), **Then** they see how pieces fit together
3. **Given** production agent running, **When** student sets up basic monitoring (log rotation + disk alerts + health checks), **Then** they get proactive notifications
4. **Given** choice between deployment strategies, **When** student evaluates options (restart vs blue-green vs rolling), **Then** they can justify pattern choice for scenario

---

### User Story 11 - Building Reusable Agent Operations Skills (Priority: P3)

A student who has mastered individual Linux skills needs to package recurring operations into reusable automation (the L3 Intelligence layer).

**Why this priority**: Split from v1's oversized L8. This lesson is about recognizing patterns and creating reusable skills — a higher-order capability that bridges to the capstone.

**Independent Test**: Student can identify recurring operational patterns and create a reusable skill definition that encapsulates Linux agent management expertise.

**Acceptance Scenarios**:

1. **Given** recurring operational patterns, **When** student identifies 2+ repetitions, **Then** they create reusable scripts or skill definitions
2. **Given** need for agent deployment automation, **When** student creates a comprehensive deployment skill, **Then** it includes setup, configuration, security, and monitoring steps
3. **Given** a defined skill, **When** student tests it on a fresh system, **Then** the skill produces consistent, correct results

---

### User Story 12 - Capstone: Spec-First Production Deployment (Priority: P2)

A student applies ALL chapter skills to deploy a production-ready agent using specification-first methodology — the L4 Spec-Driven layer.

**Why this priority**: The capstone synthesizes everything. It remains the chapter's strongest lesson but is updated to remove nginx dependency and include a sample agent file.

**Independent Test**: Student can write a deployment specification, implement it using all chapter skills, validate the deployment, and package it for repeatability.

**Acceptance Scenarios**:

1. **Given** a deployment requirement, **When** student writes DEPLOYMENT-SPEC.md, **Then** specification covers all aspects (service, security, monitoring, validation)
2. **Given** the specification, **When** student implements step-by-step, **Then** each component (user, permissions, service, monitoring) is correctly configured
3. **Given** deployed agent, **When** student runs layered validation script, **Then** all checks pass (service running, ports open, logs flowing, permissions correct)
4. **Given** need for reproducibility, **When** student packages deployment as script, **Then** deployment can be repeated on a fresh server

**Fixes from v1**: Capstone no longer assumes nginx knowledge. Architecture uses systemd + direct port binding (nginx/reverse proxy mentioned as optional future enhancement, not required).

---

### Edge Cases

- What happens when student accidentally deletes critical system files while learning permissions? → Each dangerous operation includes a safety warning and `rm -i` habit before `rm -rf`
- How does system handle running out of disk space due to runaway agent logs? → Log rotation taught in L5 (text processing) and L10 (workflow integration)
- What happens when systemd service enters restart loop? → Explicit `RestartSec=` and `StartLimitBurst` taught in L8
- How does student recover lost tmux session if server reboots? → Session scripts taught as recovery mechanism in L3
- What happens when cron job fails silently? → Cron output redirection and mail notification taught in L5
- How does SSH lockout occur if student misconfigures authentication? → Step-by-step lockout prevention protocol in L7 (test key auth BEFORE disabling password)
- What happens when student runs `chmod 000` on their own directory? → Recovery steps taught alongside permission commands
- How does student handle conflicting Python versions? → Environment isolation mentioned but deferred to Docker chapter (explicit cross-reference)
- What happens when systemd service fails to start with cryptic error? → L10 teaches `systemctl status` + `journalctl -xe` for structured diagnosis

## Requirements

### Functional Requirements

**Content Structure Requirements**:

- **FR-001**: Chapter MUST contain exactly 13 lessons + 1 quiz (14 files total)
- **FR-002**: Lessons MUST progress through pedagogical layers: L1 (Manual, lessons 1-4) → L2 (AI Collaboration, lessons 5-11) → L3 (Intelligence, lessons 12-13) → L4 (Spec-Driven, lesson 14)
- **FR-003**: Proficiency MUST progress: B1 (lessons 1-4) → B2 (lessons 5-11) → C1 (lessons 12-14)
- **FR-004**: Each lesson MUST have complete YAML frontmatter with skills, learning_objectives, cognitive_load, and differentiation sections
- **FR-005**: Each lesson MUST include exactly 3 "Try With AI" prompts with "What you're learning" explanations
- **FR-006**: Three Roles Framework MUST be invisible — validated by:
  - Zero instances of exact phrases "AI as Teacher", "AI as Student", "AI as Co-Worker" in lesson body
  - Zero section headings containing "Role:", "Three Roles:", or "Co-Worker convergence"
  - Zero paragraphs starting with "In this role, the AI will..." or "Key moment:"
  - Natural AI prompts ("Ask Claude to explain...") are ALLOWED; role labeling is NOT
  - Validation: `grep -rEi "(AI as (Teacher|Student|Co-Worker)|Three Roles:|Key moment:)" lessons/` returns empty

**New Lesson Requirements (v1 gaps)**:

- **FR-007**: New "File Operations" lesson MUST cover: cat, cp, mv, rm (with -i safety), mkdir -p, touch, head, tail, less, wildcards (*, ?, [])
- **FR-008**: New "Text Editing & Pipes" lesson MUST cover: nano basics (open, edit, save, exit), stdin/stdout/stderr, pipe operator (|), redirection (>, >>, 2>), man pages and --help
- **FR-009**: New "Networking & SSH" lesson MUST cover: ports, localhost vs 0.0.0.0, curl basics, ssh user@host, ~/.ssh/config, basic ufw firewall rules
- **FR-010**: Lesson split: Old L4 MUST be split into "Bash Scripting Foundations" (variables, error handling, functions, control flow) AND "Text Processing & Automation" (grep, sed, awk, pipes, cron)
- **FR-011**: Lesson split: Old L8 MUST be split into "Workflow Integration Patterns" (deployment patterns, monitoring) AND "Building Reusable Skills" (skill creation, pattern recognition)

**Factual Correction Requirements**:

- **FR-012**: All `stat -f%z` occurrences MUST be replaced with `stat -c%s` (Linux syntax, not macOS)
- **FR-013**: systemd `Restart=on-failure` MUST be taught as default from the start — no "teach wrong then correct" pattern
- **FR-014**: All Python scripts using `psutil` MUST include installation instructions (`pip install psutil`)
- **FR-015**: All scripts referencing `/var/agents/` MUST include directory creation in setup steps

**Content Quality Requirements**:

- **FR-016**: Every lesson MUST include 2+ interactive exercises with explicit verification:
  - Exercise format: "Task: [action]. Verify: [command showing expected output]"
  - Minimum 2 exercises per lesson, maximum 5
  - Verification command MUST be executable (not "check that..." or "confirm...")
  - Example: "Task: Create user `agent-runner`. Verify: `id agent-runner` shows uid/gid"
- **FR-017**: Health check scripts MUST appear in ONE canonical form in L10 (Process Control & Systemd), referenced elsewhere via markdown link: `See [Health Check Script](10-process-control-systemd.md#agent-health-checks)` — not duplicated as inline code blocks
- **FR-018**: Simulated AI conversations MUST be replaced with verifiable exercises:
  - AVOID: Scripted dialogues ("You: How do I...? AI: Here's how... You: Thanks!")
  - USE: "Try With AI" prompts that students execute and verify results on their system
  - Validation: `grep -c "^You:" lessons/` returns 0 (except inside "Try With AI" code blocks)
- **FR-019**: Each lesson MUST have max 6 new concepts (cognitive load limit); lessons exceeding this MUST be split
- **FR-020**: Capstone MUST NOT assume nginx knowledge — architecture uses systemd + direct port binding
- **FR-021**: Chapter MUST provide a sample FastAPI agent file (`agent_main.py`) with constraints:
  - Maximum 50 lines of Python code
  - Uses ONLY: FastAPI basics (`@app.get`, `uvicorn.run`), no database/auth/external APIs
  - Includes `/health` endpoint returning `{"status": "healthy", "agent": "running"}`
  - Includes one task endpoint (e.g., `/tasks` returning sample data)
  - All sections have inline comments explaining what each part does
  - File is self-contained — `pip install fastapi uvicorn` is the only setup required

**Prerequisite Requirements**:

- **FR-022**: README MUST reference only Part 1 (agent foundations) as prerequisite — no forward references to Chapters 40-42
- **FR-023**: Chapter MUST be self-contained: all tools and concepts used in later lessons MUST be taught in earlier lessons
- **FR-024**: README MUST accurately state "No prior Linux experience required" without contradictions

**Cross-Cutting Requirements** (apply to ALL 13 lessons):

- **FR-CC1**: FR-004 (YAML frontmatter), FR-005 (3 Try With AI prompts), FR-006 (Three Roles invisible), FR-016 (2+ exercises), FR-018 (no simulated conversations) apply to EVERY lesson without exception
- **FR-CC2**: Implementation must validate these cross-cutting requirements as a final pass across all lesson files

**Quiz Requirements**:

- **FR-025**: Quiz MUST be regenerated with 50 questions covering all 13 lessons (not just original 9)
- **FR-026**: Quiz JSON syntax MUST have no double-comma (`,,`) bugs
- **FR-027**: Quiz MUST include distractor options testing common misconceptions (not just wrong answers)

### Key Entities

- **Terminal/Shell**: Command-line interface; terminal = application, shell = interpreter (bash/zsh)
- **File Operations**: CRUD operations on filesystem objects (files, directories, symlinks)
- **Text Editor (nano)**: Terminal-based file editor with keyboard shortcuts
- **I/O Streams**: stdin (input), stdout (output), stderr (errors) — the data channels between commands
- **Pipe**: The `|` operator connecting stdout of one command to stdin of another
- **Package Manager (apt)**: System for installing, updating, and removing software
- **tmux Session**: Persistent terminal multiplexer session surviving disconnections
- **Bash Script**: Executable file containing sequenced shell commands with error handling
- **Text Processing Tools**: grep (search), sed (transform), awk (extract) — the Unix text processing trio
- **Cron Job**: Scheduled task running automatically at specified intervals
- **SSH Connection**: Encrypted remote server access using key-based authentication
- **Firewall (ufw)**: Port access control for network security
- **Systemd Service**: Background process managed by init system with auto-restart and boot-start capabilities
- **Service Template**: Parameterized systemd unit file for managing multiple similar services
- **Environment Variable**: Named value in shell environment; `export` makes visible to child processes
- **System Log (journalctl)**: Centralized log management for systemd services
- **Deployment Pattern**: Strategy for updating running services (restart, blue-green, rolling)

## Lesson Structure (New v2 Layout)

| # | Filename | Title | CEFR | Bloom's | Layer | Duration | Concepts | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | `01-cli-architect-mindset.md` | The CLI Architect Mindset | B1 | Remember/Understand | L1 | 45 min | 5 | Rewrite (add file ops awareness) |
| 02 | `02-file-operations-mastery.md` | File Operations Mastery | B1 | Apply | L1 | 45 min | 6 | **NEW** |
| 03 | `03-text-editing-pipes-streams.md` | Text Editing, Pipes & I/O Streams | B1 | Apply | L1 | 50 min | 6 | **NEW** |
| 04 | `04-modern-terminal-environment.md` | Modern Terminal Environment | B1 | Apply | L1 | 50 min | 5 | Rewrite (nano moved out, env var scoping added) |
| 05 | `05-persistent-sessions-tmux.md` | Persistent Sessions with tmux | B2 | Apply | L2 | 55 min | 6 | Rewrite (Three Roles invisible) |
| 06 | `06-bash-scripting-foundations.md` | Bash Scripting Foundations | B2 | Apply | L2 | 55 min | 6 | **SPLIT** from old L4 |
| 07 | `07-text-processing-automation.md` | Text Processing & Automation | B2 | Apply | L2 | 55 min | 6 | **SPLIT** from old L4 |
| 08 | `08-security-hardening.md` | Security Hardening & Least Privilege | B2 | Apply/Analyze | L2 | 60 min | 6 | Rewrite (env var scoping, Three Roles invisible) |
| 09 | `09-networking-ssh-remote-access.md` | Networking Fundamentals & SSH | B2 | Apply/Analyze | L2 | 60 min | 6 | **NEW** |
| 10 | `10-process-control-systemd.md` | Process Control & Systemd Services | B2 | Analyze | L2 | 60 min | 6 | Rewrite (Restart= fix, Three Roles invisible) |
| 11 | `11-debugging-troubleshooting.md` | Debugging & Troubleshooting | B2 | Analyze | L2 | 60 min | 6 | Rewrite (networking prereq now satisfied) |
| 12 | `12-workflow-integration-patterns.md` | Advanced Workflow Integration | C1 | Evaluate | L3 | 65 min | 5 | **SPLIT** from old L8 |
| 13 | `13-building-reusable-skills.md` | Building Reusable Agent Ops Skills | C1 | Create | L3 | 55 min | 5 | **SPLIT** from old L8 |
| 14 | `14-capstone-production-deployment.md` | Capstone: Spec-First Deployment | C1 | Create | L4 | 90 min | 5 | Rewrite (no nginx dependency, sample agent file) |
| -- | `15-chapter-quiz.md` | Chapter Quiz | -- | -- | -- | 30 min | -- | Regenerate (13 lessons, fix syntax) |

**Layer Boundary Rationale**: L1 (Manual) = lessons 1-4 (pure CLI foundation, no AI needed). L2 (AI Collaboration) begins at L5 (tmux enables multi-pane workflows ideal for AI-assisted work: monitoring in one pane, AI prompting in another). L3 (Intelligence) = lessons 12-13 (pattern recognition, skill creation). L4 (Spec-Driven) = lesson 14 (capstone orchestration).

**Total Duration**: ~835 minutes (~14 hours)

**Bloom's Progression**: Remember → Understand → Apply → Analyze → Evaluate → Create (smooth, no steep jumps)

**CEFR Progression**: B1 (lessons 1-4, L1 Manual) → B2 (lessons 5-11, L2 AI Collaboration) → C1 (lessons 12-14, L3 Intelligence + L4 Spec-Driven)

## Success Criteria

### Measurable Outcomes

- **SC-001**: All 21 identified issues from the analysis report are resolved (tracked via checklist)
- **SC-002**: No lesson exceeds 35KB (v1 had 48KB and 39KB lessons)
- **SC-003**: No lesson introduces more than 6 new concepts (cognitive load ceiling)
- **SC-004**: Three Roles Framework is invisible in all lessons — zero instances of explicit "AI as Teacher/Student/Co-Worker" labels
- **SC-005**: All Linux commands use correct Linux syntax (no macOS-specific flags)
- **SC-006**: No forward references to unwritten chapters in prerequisites
- **SC-007**: Every lesson includes at least 2 interactive exercises with explicit verification commands
- **SC-008**: Health check scripts appear in ONE canonical form, referenced elsewhere (not duplicated 4 times)
- **SC-009**: Quiz has 50 well-formed questions covering all 13 lessons with valid JSON syntax
- **SC-010**: Students with zero Linux experience can complete lessons 1-4 without external help
- **SC-011**: Students can deploy a real agent as a systemd service by lesson 14 using ONLY skills taught in this chapter
- **SC-012**: Chapter grade improves from B+ to A- as assessed by content-evaluation-framework

## Assumptions

1. Students have access to a Linux system (Ubuntu/Debian; WSL2 on Windows is acceptable)
2. Students have sudo privileges on their learning system
3. Learning environment allows mistakes (VM, container, or non-production server)
4. Standard Linux tools are available (no exotic package requirements)
5. A sample FastAPI agent file will be provided within the chapter (no external dependency)
6. Chapter numbering conflict (duplicate `10-*` folders) will be resolved separately — this spec focuses on content quality only
7. Chapter placement within Part 2 may change — this spec is placement-agnostic

## Constraints & Non-Goals

### Constraints

- MUST focus on Ubuntu/Debian Linux (most common for servers)
- MUST NOT assume GUI access (all tasks possible via SSH)
- MUST NOT assume any prior Linux or programming experience beyond Part 1
- MUST emphasize safety and recovery from mistakes
- MUST tie every concept to agent deployment use cases
- MUST keep all lessons under 35KB
- MUST keep new concepts per lesson at 6 or fewer
- MUST use invisible Three Roles Framework (structural, not labeled)

### Non-Goals (Explicitly Out of Scope)

- nginx configuration (mentioned as optional future enhancement in capstone, not required)
- Docker (covered in separate chapter; brief awareness note in L12 only)
- Deep Linux internals (kernel architecture, system calls)
- Advanced kernel customization or compilation
- Network protocol deep-dives (TCP/IP stacks, routing protocols)
- Cloud platform specifics (AWS/GCP/Azure CLI tools)
- Performance tuning at kernel level
- SELinux or AppArmor advanced security
- High-availability clustering or load balancing
- Linux distribution comparisons
- WSL setup guidance (mentioned in README as note, not a full lesson)

## Dependencies

### Prerequisite Chapters (Corrected)

- Part 1: Agent Foundations (understanding what agents are and why they need servers)
- No other prerequisites — chapter is self-contained

### Related Future Chapters

- Docker chapter (builds on Linux skills taught here)
- Kubernetes chapter (builds on systemd concepts)
- Production Security chapter (builds on SSH/permissions)

### External Resources

- Ubuntu/Debian official documentation
- tmux official documentation
- systemd official documentation
- GNU Bash reference manual
- OpenSSH documentation

## Issue Tracking Matrix

This matrix maps each of the 21 identified issues to their resolution in this spec.

| # | Issue | Priority | Resolution | Lesson |
| --- | --- | --- | --- | --- |
| 1 | Duplicate 10-* conflict | P1 | Deferred (numbering out of scope per user request) | README |
| 2 | Wrong prerequisites (Ch 40-42) | P1 | FR-022, FR-023: Only Part 1 required, self-contained | README |
| 3 | Missing File Operations lesson | P1 | FR-007: New lesson 02 | L02 |
| 4 | Missing SSH Remote Access | P1 | FR-009: New lesson 09 | L09 |
| 5 | Three Roles visible/formulaic | P1 | FR-006: Invisible in all lessons | All |
| 6 | Split L4 (overloaded) | P2 | FR-010: L06 + L07 | L06, L07 |
| 7 | Split L8 (overloaded) | P2 | FR-011: L12 + L13 | L12, L13 |
| 8 | Missing nano/text editing | P2 | FR-008: New lesson 03 | L03 |
| 9 | Simulated AI conversations | P2 | FR-018: Replaced with verifiable exercises | All |
| 10 | Missing networking basics | P2 | FR-009: New lesson 09 | L09 |
| 11 | Add interactive exercises | P3 | FR-016: Every lesson has verification exercises | All |
| 12 | Add cheat sheet | P3 | Included as summary in README | README |
| 13 | Cover man/--help | P3 | FR-008: Covered in L03 | L03 |
| 14 | Docker awareness | P3 | Brief note in L12 comparing systemd vs Docker | L12 |
| 15 | Fix stat -f%z | P3 | FR-012: Corrected to stat -c%s | L06 |
| 16 | Fix quiz syntax | P3 | FR-026: Regenerated with valid JSON | Quiz |
| 17 | Chapter placement | P3 | Deferred (placement out of scope per user request) | N/A |
| 18 | WSL/Windows guidance | P4 | README note only | README |
| 19 | Linux command reference | P4 | Summary appendix in README | README |
| 20 | Sample agent file | P4 | FR-021: Provided within chapter | L14 |
| 21 | systemctl cheat sheet | P4 | Included in L10 summary | L10 |

---

**Document Version**: 2.0.0
**Last Updated**: 2026-02-08
**Ready for Planning**: Yes
**Predecessor**: `specs/001-linux-mastery/spec.md` v1.0.0
