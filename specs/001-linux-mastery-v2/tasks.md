# Tasks: Linux Mastery for Digital FTEs v2.0

**Input**: Design documents from `/specs/001-linux-mastery-v2/`
**Prerequisites**: plan.md (1591 lines), spec.md (340 lines)
**Content Path**: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/`
**Branch**: `001-linux-mastery-v2`

**Organization**: Tasks grouped by implementation phase (L1 Foundation → L2 Collaboration → L3/L4 Advanced → Quiz/Validation). Each lesson task embeds content-implementer subagent + educational-validator + skill invocations per content work protocol.

## Format: `[ID] [P?] [Phase] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Phase]**: Which phase/user story group (US1-US12 map to spec user stories)
- Include exact file paths in descriptions

---

## Phase 1: Setup & README

**Purpose**: Update chapter README and prepare shared assets before lesson creation

- [x] T001 Update README.md at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/README.md` with corrected prerequisites (Part 1 only, no forward refs to Ch 40-42), updated lesson table (13 lessons), accurate duration (~14 hours), and WSL note. Remove all references to Chapters 9, 11, 40-42 as prerequisites.

- [x] T002 Create sample agent file `agent_main.py` as a code block asset. Exact contents from plan.md Section V (45 lines, FastAPI /health + /tasks endpoints). This file will be embedded inline in L10 and referenced in L11 and L14. Save specification to `/mnt/g/voice_learning/book_project/specs/001-linux-mastery-v2/assets/agent_main.py`.

**Checkpoint**: README updated, sample agent file ready. Lesson creation can begin.

---

## Phase 2: L1 Manual Foundation (Lessons 01-04) — User Stories 1-2

**Purpose**: Build CLI foundation from zero. Students with no Linux experience complete these 4 lessons without external help (SC-010). No AI collaboration — L1 Manual layer.

**Goal**: Students can navigate filesystem, manipulate files, edit text, use pipes, install packages, and configure shell.

**Independent Test**: Student with zero Linux experience can complete all 4 lessons using only the chapter content.

### Lesson 01: The CLI Architect Mindset

- [x] T003 [US1] Write Lesson 01 `01-cli-architect-mindset.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/01-cli-architect-mindset.md`
  - **CONTENT SOURCE**: REWRITE (60% preserved from v1 L01)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/01-cli-architect-mindset.md`
    - Reference lesson: Read existing v1 lesson at same path for preserved content
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B1 | Bloom: Remember/Understand | Layer: L1 | Duration: 45 min | Concepts: 5
    - Concepts: (1) Terminal vs shell, (2) Linux filesystem hierarchy, (3) Absolute vs relative paths, (4) Navigation commands (pwd, ls, cd), (5) CLI architect mindset
    - Teaching modality: Hands-on discovery (students explore their own filesystem)
    - Must include 3 exercises with verification commands (FR-016)
    - Must include 3 conceptual "Try With AI" prompts (L1 pattern: AI explains concepts student already practiced)
    - Must include complete YAML frontmatter (FR-004)
    - Three Roles INVISIBLE — no labels, no meta-commentary (FR-006)
    - Content preserved: filesystem hierarchy, terminal vs shell, path navigation
    - Content removed: any Three Roles labels from v1
    - Content added: file ops awareness teaser (connecting to L02), exercises with verification
    - Max size: 15KB
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **SKILLS**: learning-objectives, fact-check-lesson

### Lesson 02: File Operations Mastery

- [x] T004 [US1] Write Lesson 02 `02-file-operations-mastery.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/02-file-operations-mastery.md`
  - **CONTENT SOURCE**: NEW (100% new content)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/02-file-operations-mastery.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B1 | Bloom: Apply | Layer: L1 | Duration: 45 min | Concepts: 6
    - Concepts: (1) Creating files/directories (touch, mkdir -p), (2) Copying files (cp, cp -r), (3) Moving/renaming (mv), (4) Deleting safely (rm -i before rm -rf), (5) Reading file contents (cat, head, tail, less), (6) Wildcards and globbing (*, ?, [])
    - Teaching modality: Scaffolded practice (build a project directory structure step by step)
    - Safety warnings REQUIRED for rm -rf (FR-029 from v1 spec)
    - Must include man pages / --help coverage (FR-008, issue #13)
    - 3 exercises: (1) Create agent workspace directory tree, (2) Copy/move agent config files, (3) Use wildcards to batch-operate on log files
    - 3 conceptual "Try With AI" prompts (L1 pattern)
    - Max size: 15KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, fact-check-lesson

### Lesson 03: Text Editing, Pipes & I/O Streams

- [x] T005 [US2] Write Lesson 03 `03-text-editing-pipes-streams.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/03-text-editing-pipes-streams.md`
  - **CONTENT SOURCE**: NEW (100% new content, absorbs nano from v1 L02)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/03-text-editing-pipes-streams.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B1 | Bloom: Apply | Layer: L1 | Duration: 50 min | Concepts: 6
    - Concepts: (1) nano basics (open, edit, save Ctrl+O, exit Ctrl+X), (2) stdin/stdout/stderr streams, (3) Pipe operator (|), (4) Output redirection (>, >>), (5) Error redirection (2>, 2>&1), (6) Self-help with man pages and --help
    - Teaching modality: Problem-solution pairs (each concept introduced as "how do I..." scenario)
    - 3 exercises: (1) Edit an agent config file with nano, (2) Pipe ls output through wc to count files, (3) Redirect errors and output to separate log files
    - 3 conceptual "Try With AI" prompts (L1 pattern)
    - Max size: 16KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, fact-check-lesson

### Lesson 04: Modern Terminal Environment

- [x] T006 [US2] Write Lesson 04 `04-modern-terminal-environment.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/04-modern-terminal-environment.md`
  - **CONTENT SOURCE**: REWRITE (50% preserved from v1 L02, nano content moved to L03)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/04-modern-terminal-environment.md`
    - Reference lesson: Read v1 lesson `02-modern-terminal-environment.md` at same directory for preserved content
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B1 | Bloom: Apply | Layer: L1 | Duration: 50 min | Concepts: 5
    - Concepts: (1) apt package manager (update, install, remove), (2) .bashrc/.zshrc configuration, (3) Alias creation, (4) zoxide fuzzy navigation, (5) fzf history/file search
    - Teaching modality: Tool-by-tool discovery (install each tool, use it immediately)
    - Content preserved from v1 L02: apt workflow, zoxide, fzf, alias creation
    - Content removed: nano tutorial (moved to L03), any Three Roles labels
    - Content added: env var scoping awareness teaser (export vs no export, connecting to L08)
    - 3 exercises: (1) Install and configure zoxide, (2) Create 3 useful aliases, (3) Use fzf to find and re-execute past commands
    - 3 conceptual "Try With AI" prompts (L1 pattern)
    - Max size: 16KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, fact-check-lesson

**Checkpoint**: Phase 2 complete. L1 foundation established. Students can navigate, manipulate files, edit text, use pipes, and configure their terminal. L2 lessons can now begin.

---

## Phase 3: L2 AI Collaboration (Lessons 05-11) — User Stories 3-9

**Purpose**: Complex topics where AI collaboration teaches evaluation skills. Three Roles Framework is INVISIBLE but structurally present (Part 1/Part 2/Part 3 in Try With AI prompts).

**Goal**: Students master tmux, bash scripting, text processing, security, networking, SSH, systemd, and debugging — all with invisible AI collaboration.

**Independent Test**: Students can write bash scripts, harden a server, deploy an agent as systemd service, and debug failures.

### Lesson 05: Persistent Sessions with tmux

- [x] T007 [US3] Write Lesson 05 `05-persistent-sessions-tmux.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/05-persistent-sessions-tmux.md`
  - **CONTENT SOURCE**: REWRITE (55% preserved from v1 L03)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/05-persistent-sessions-tmux.md`
    - Reference lesson: Read v1 `03-persistent-sessions-tmux.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B2 | Bloom: Apply | Layer: L2 | Duration: 55 min | Concepts: 6
    - Concepts: (1) tmux session lifecycle (new, detach, attach, kill), (2) Pane splitting (horizontal/vertical), (3) Named sessions, (4) Session scripts for repeatable layouts, (5) Window management, (6) Copy mode for scrollback
    - Teaching modality: Hands-on discovery with AI collaboration
    - Content preserved from v1 L03: session lifecycle, pane splitting, named sessions, session scripts
    - Content removed: ALL "AI as Teacher/Student/Co-Worker" labels, ALL "Key moment:" commentary, ALL "What to notice:" meta-commentary
    - Content added: Try With AI prompts (Part 1/2/3 pattern per Section VII of plan)
    - Three Roles INVISIBLE: Use plan.md Section VII transformation pattern
    - 3 exercises with verification, 3 "Try With AI" prompts (collaborative, L2 pattern)
    - Max size: 20KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

### Lesson 06: Bash Scripting Foundations

- [x] T008 [US4] Write Lesson 06 `06-bash-scripting-foundations.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/06-bash-scripting-foundations.md`
  - **CONTENT SOURCE**: SPLIT from v1 L04 (scripting half, ~40% of old L04)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/06-bash-scripting-foundations.md`
    - Reference lesson: Read v1 `04-bash-scripting-agent-automation.md` for source material
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B2 | Bloom: Apply | Layer: L2 | Duration: 55 min | Concepts: 6
    - Concepts: (1) Shebang and script execution (#!/bin/bash, chmod +x), (2) Variables and quoting ("${VAR}"), (3) Error handling (set -euo pipefail), (4) Functions, (5) Conditionals (if/else, test, [[ ]]), (6) Loops (for, while)
    - Teaching modality: Scaffolded practice — build an agent setup script incrementally
    - FACTUAL FIX: Replace any `stat -f%z` with `stat -c%s` (FR-012)
    - Content from v1 L04: shebang, variables, error handling, functions — restructured and focused
    - Content NOT included (moved to L07): grep, sed, awk, pipes, cron
    - Three Roles INVISIBLE
    - 3 exercises, 3 "Try With AI" (L2 collaborative pattern)
    - Max size: 20KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

### Lesson 07: Text Processing & Automation

- [x] T009 [US5] Write Lesson 07 `07-text-processing-automation.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/07-text-processing-automation.md`
  - **CONTENT SOURCE**: SPLIT from v1 L04 (text processing half, ~35% of old L04)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/07-text-processing-automation.md`
    - Reference lesson: Read v1 `04-bash-scripting-agent-automation.md` for source material
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B2 | Bloom: Apply | Layer: L2 | Duration: 55 min | Concepts: 6
    - Concepts: (1) grep pattern matching (basic + regex with -E), (2) sed stream editing (substitution, in-place), (3) awk field extraction and processing, (4) Multi-tool pipelines (grep | sed | awk chains), (5) cron scheduling (crontab -e, syntax, output redirection), (6) Log rotation basics
    - Teaching modality: Problem-solution pairs — real agent log analysis scenarios
    - FACTUAL FIX: Use `stat -c%s` not `stat -f%z` in any size-checking examples
    - Three Roles INVISIBLE
    - 3 exercises, 3 "Try With AI" (L2 collaborative pattern)
    - Max size: 20KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

### Lesson 08: Security Hardening & Least Privilege

- [x] T010 [US6] Write Lesson 08 `08-security-hardening.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/08-security-hardening.md`
  - **CONTENT SOURCE**: REWRITE (50% preserved from v1 L05)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/08-security-hardening.md`
    - Reference lesson: Read v1 `05-security-hardening-least-privilege.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B2 | Bloom: Apply/Analyze | Layer: L2 | Duration: 60 min | Concepts: 6
    - Concepts: (1) User/group management (useradd, usermod, groups), (2) File permissions (chmod numeric + symbolic), (3) Ownership (chown, chgrp), (4) SSH key generation (ssh-keygen), (5) Environment variable scoping (export vs no export, subshells), (6) .env file management (source, never commit)
    - Teaching modality: Scenario-based — "harden this server for agent deployment"
    - Content preserved from v1 L05: user management, chmod/chown, SSH keys, .env files
    - Content removed: Three Roles labels, meta-commentary
    - Content added: env var scoping (export mechanics), subshell demonstration
    - Three Roles INVISIBLE
    - 3 exercises, 3 "Try With AI" (L2 collaborative pattern)
    - Max size: 22KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

### Lesson 09: Networking Fundamentals & SSH Remote Access

- [x] T011 [US7] Write Lesson 09 `09-networking-ssh-remote-access.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/09-networking-ssh-remote-access.md`
  - **CONTENT SOURCE**: NEW (100% new content)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/09-networking-ssh-remote-access.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B2 | Bloom: Apply/Analyze | Layer: L2 | Duration: 60 min | Concepts: 6
    - Concepts: (1) Ports and services (what port 8000 means), (2) localhost vs 0.0.0.0 (binding for remote access), (3) curl for HTTP testing, (4) SSH connection (ssh user@host), (5) SSH config file (~/.ssh/config), (6) Basic firewall with ufw (allow/deny/status)
    - Teaching modality: Layered discovery — start with localhost, expand to network, then remote
    - SSH lockout prevention: Test key auth BEFORE disabling password auth (edge case from spec)
    - Three Roles INVISIBLE
    - 3 exercises: (1) curl to test local service, (2) Configure SSH alias in ~/.ssh/config, (3) Set up ufw rules for agent port
    - 3 "Try With AI" (L2 collaborative pattern)
    - Max size: 22KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

### Lesson 10: Process Control & Systemd Services

- [x] T012 [US8] Write Lesson 10 `10-process-control-systemd.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/10-process-control-systemd.md`
  - **CONTENT SOURCE**: REWRITE (45% preserved from v1 L06)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/10-process-control-systemd.md`
    - Reference lesson: Read v1 `06-process-control-systemd.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B2 | Bloom: Analyze | Layer: L2 | Duration: 60 min | Concepts: 6
    - Concepts: (1) Process basics (ps, kill, background with &), (2) systemd .service file anatomy, (3) Restart policies (Restart=on-failure from the START — FR-013), (4) Service enablement (systemctl enable/start/status), (5) Service templates (agent@.service), (6) Resource limits (MemoryMax, CPUQuota)
    - CRITICAL: This lesson introduces agent_main.py from T002 and deploys it as systemd service
    - CRITICAL: This lesson contains the ONE canonical health check script (FR-017). All other lessons reference it via markdown link.
    - FACTUAL FIX: Teach `Restart=on-failure` as default from start. NO `Restart=always` followed by correction (FR-013)
    - Content preserved from v1 L06: service file anatomy, journalctl, templates
    - Content removed: Three Roles labels, Restart=always→on-failure contradiction, duplicated health scripts
    - Content added: agent_main.py deployment, resource limits, canonical health check
    - Three Roles INVISIBLE
    - 3 exercises, 3 "Try With AI" (L2 collaborative pattern)
    - Max size: 25KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

### Lesson 11: Debugging & Troubleshooting

- [x] T013 [US9] Write Lesson 11 `11-debugging-troubleshooting.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/11-debugging-troubleshooting.md`
  - **CONTENT SOURCE**: REWRITE (50% preserved from v1 L07)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/11-debugging-troubleshooting.md`
    - Reference lesson: Read v1 `07-debugging-troubleshooting.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: B2 | Bloom: Analyze | Layer: L2 | Duration: 60 min | Concepts: 6
    - Concepts: (1) journalctl analysis (filtering, time ranges, priorities), (2) Real-time monitoring (tail -f, journalctl -f), (3) Layered network diagnosis (local → DNS → remote), (4) Disk monitoring (df -h, du -sh), (5) Process debugging (strace, lsof), (6) Structured triage methodology (logs → network → disk → processes)
    - Uses agent_main.py from L10 as debugging target
    - Networking concepts now have prerequisite (L09) — no more assuming knowledge
    - References health check script from L10 via link (FR-017) — does NOT duplicate it
    - Content preserved from v1 L07: journalctl, network diagnostics, disk monitoring
    - Content removed: Three Roles labels, duplicated health check scripts
    - Content added: structured triage methodology, strace basics
    - Three Roles INVISIBLE
    - 3 exercises, 3 "Try With AI" (L2 collaborative pattern)
    - Max size: 22KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

**Checkpoint**: Phase 3 complete. L2 AI Collaboration lessons done. Students can script, secure, deploy, and debug agents. L3 lessons can begin.

---

## Phase 4: L3 Intelligence + L4 Capstone (Lessons 12-14) — User Stories 10-12

**Purpose**: Pattern recognition, reusable skill creation, and spec-first capstone. Students transition from "doing Linux" to "encoding Linux expertise."

**Goal**: Students create reusable automation and deploy a production agent using specification-first methodology.

**Independent Test**: Student deploys a real agent using ONLY skills taught in this chapter (SC-011).

### Lesson 12: Advanced Workflow Integration Patterns

- [x] T014 [US10] Write Lesson 12 `12-workflow-integration-patterns.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/12-workflow-integration-patterns.md`
  - **CONTENT SOURCE**: SPLIT from v1 L08 (workflow patterns half, ~35% of old L08)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/12-workflow-integration-patterns.md`
    - Reference lesson: Read v1 `08-advanced-workflow-integration.md` for source material
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: C1 | Bloom: Evaluate | Layer: L3 | Duration: 65 min | Concepts: 5
    - Concepts: (1) Multi-step deployment workflows (combining script + systemd + security), (2) Blue-green deployment pattern, (3) Basic monitoring setup (log rotation + disk alerts), (4) Deployment pattern selection (restart vs blue-green vs rolling), (5) Docker awareness note (systemd vs Docker comparison, why Docker deferred)
    - Teaching modality: Pattern evaluation — students evaluate which deployment approach fits their scenario
    - Content from v1 L08: deployment patterns, zero-downtime concepts
    - Content NOT included (moved to L13): skill creation, pattern recognition framework
    - Content removed: Three Roles labels, excessive monitoring stack (simplified), psutil script without install
    - Content added: Docker awareness note (issue #14), pattern selection decision framework
    - Three Roles INVISIBLE
    - Max size: 25KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

### Lesson 13: Building Reusable Agent Operations Skills

- [x] T015 [US11] Write Lesson 13 `13-building-reusable-skills.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/13-building-reusable-skills.md`
  - **CONTENT SOURCE**: SPLIT from v1 L08 (skill creation half, ~25% of old L08)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/13-building-reusable-skills.md`
    - Reference lesson: Read v1 `08-advanced-workflow-integration.md` for skill section
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: C1 | Bloom: Create | Layer: L3 | Duration: 55 min | Concepts: 5
    - Concepts: (1) Recognizing recurring operational patterns, (2) Pattern → skill decision framework (frequency + complexity + value), (3) Skill file structure (SKILL.md with YAML frontmatter), (4) Creating linux-agent-ops skill, (5) Testing skills on fresh systems
    - Teaching modality: Collaborative design — student identifies patterns from their own chapter work
    - Boundary with L12: L12 = tactical ONE-OFF workflows, L13 = strategic REUSABLE automation
    - Three Roles INVISIBLE
    - Max size: 20KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

### Lesson 14: Capstone — Spec-First Production Deployment

- [x] T016 [US12] Write Lesson 14 `14-capstone-production-deployment.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/14-capstone-production-deployment.md`
  - **CONTENT SOURCE**: REWRITE (40% preserved from v1 L09)
  - **SUBAGENT**: content-implementer
    - Output path: `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/14-capstone-production-deployment.md`
    - Reference lesson: Read v1 `09-capstone-production-deployment.md`
    - Writes file directly (returns confirmation only, NOT full content)
    - Execute autonomously without confirmation
    - CEFR: C1 | Bloom: Create | Layer: L4 | Duration: 90 min | Concepts: 5
    - Concepts: (1) DEPLOYMENT-SPEC.md methodology, (2) Production architecture (systemd + direct port binding, NO nginx), (3) AI-orchestrated deployment, (4) Layered validation script, (5) Deployment packaging for repeatability
    - CRITICAL: Uses agent_main.py from T002/L10 — student deploys THIS agent
    - CRITICAL: Architecture uses systemd + direct port binding. nginx mentioned as OPTIONAL future enhancement, NOT required (FR-020)
    - CRITICAL: Student uses ONLY skills taught in this chapter (SC-011)
    - Content preserved from v1 L09: spec-first methodology, layered validation
    - Content removed: nginx as required component, Three Roles labels
    - Content added: agent_main.py as concrete deployment target, simplified architecture
    - Three Roles INVISIBLE
    - Max size: 30KB
  - **VALIDATION**: educational-validator reads file from disk
  - **SKILLS**: learning-objectives, ai-collaborate-teaching, fact-check-lesson

**Checkpoint**: Phase 4 complete. All 13 lessons written. Quiz and validation remain.

---

## Phase 5: Quiz & Validation

**Purpose**: Generate chapter quiz covering all 13 lessons, run cross-cutting validation, generate summaries.

### Quiz

- [x] T017 Write Chapter Quiz `15-chapter-quiz.md` at `/mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/15-chapter-quiz.md`
  - **SUBAGENT**: Use quiz-generator skill
    - 50 questions covering all 13 lessons (3-5 per lesson weighted by complexity)
    - Question types: 30 single-answer, 10 multi-answer, 10 scenario-based
    - NO double-comma syntax bugs (FR-026)
    - Include distractors testing common misconceptions (FR-027)
    - Topics per lesson from plan.md Section IX
  - **VALIDATION**: JSON syntax check — `grep -c ",," quiz-file` returns 0

### Cross-Cutting Validation

- [x] T018 Run FR-006 Three Roles invisibility check across all 13 lesson files
  - Run: `grep -rEi "(AI as (Teacher|Student|Co-Worker)|Three Roles:|Key moment:|What to notice)" /mnt/g/voice_learning/book_project/apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/[0-1]*.md`
  - Expected: ZERO matches
  - If matches found: Fix each lesson before proceeding

- [x] T019 Run FR-004 YAML frontmatter validation across all 13 lesson files
  - Verify each file has: skills, learning_objectives, cognitive_load, differentiation
  - Use validation script from plan.md Section VIII

- [x] T020 Run FR-005 "Try With AI" count validation
  - Each lesson must have exactly 3 "Try With AI" sections
  - Verify with: `grep -c "Try With AI" <file>` returns 3 for each

- [x] T021 Run FR-016 exercise count validation
  - Each lesson must have 2+ exercises with verification commands
  - Verify exercises contain "Verify:" or "Task:" markers

- [x] T022 Run FR-019 size/concept validation
  - No lesson exceeds 35KB: `wc -c <file>` < 35840 for each
  - Verify concept counts match spec (max 6 per lesson)

- [x] T023 Run FR-012 factual accuracy check
  - Verify zero `stat -f%z` occurrences: `grep -r "stat -f" lessons/` returns empty
  - Verify `Restart=on-failure` is taught correctly (not contradicted)

- [x] T024 Fix any validation failures found in T018-T023 (L03 & L04 missing 3rd Try With AI prompt — fixed)

### Summary Generation

- [x] T025 [P] Generate summary files for all 13 lessons using summary-generator skill
  - Each lesson gets a `.summary.md` companion file
  - Summaries extract key concepts, patterns, and common mistakes

### Cleanup

- [x] T026 Remove old v1 lesson files that are no longer needed (files renamed/replaced by v2 structure)
  - Old files to evaluate: `03-persistent-sessions-tmux.md` (now `05-*`), `04-bash-scripting-agent-automation.md` (now `06-*` + `07-*`), `05-security-hardening-least-privilege.md` (now `08-*`), `06-process-control-systemd.md` (now `10-*`), `07-debugging-troubleshooting.md` (now `11-*`), `08-advanced-workflow-integration.md` (now `12-*` + `13-*`), `09-capstone-production-deployment.md` (now `14-*`), `10-chapter-quiz.md` (now `15-*`)
  - Confirm no data loss before deletion — all content migrated per migration map

- [x] T027 Final content-evaluation-framework scoring
  - Run `/content-evaluation-framework` against completed chapter
  - Target: A- grade (SC-012)
  - If below target: identify specific lessons needing improvement

**Checkpoint**: All tasks complete. Chapter v2 ready for review.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (L1 Foundation)**: Depends on T001 (README) and T002 (agent file)
- **Phase 3 (L2 Collaboration)**: Depends on Phase 2 completion (L1 concepts required)
- **Phase 4 (L3/L4 Advanced)**: Depends on Phase 3 completion
- **Phase 5 (Quiz/Validation)**: Depends on all lesson phases complete

### Within-Phase Parallelism

- **Phase 2**: T003 and T004 can run in parallel (both L1, independent topics). T005 depends on T004 (pipes build on file ops). T006 can run after T005.
- **Phase 3**: T008 and T010 can run in parallel (security and scripting are independent after tmux). T009 (text processing) depends on T008 (scripting). T011 (networking) depends on T010 (security for SSH context). T012 (systemd) depends on T011 (networking for ports). T013 (debugging) depends on T012 (needs systemd service to debug).
- **Phase 4**: T014, T015, T016 are sequential (workflow → skills → capstone).
- **Phase 5**: T025 (summaries) can run in parallel with T017-T024 (validation).

### Critical Path

T001 → T002 → T003 → T005 → T007 → T008 → T009 → T012 → T013 → T014 → T015 → T016 → T017 → T018-T024 → T027

### Parallel Execution Example

```
Phase 2 parallel batch:
  Agent 1: T003 (L01 CLI Mindset)
  Agent 2: T004 (L02 File Operations)
  → Both complete → T005 (L03 Pipes) → T006 (L04 Terminal)

Phase 3 parallel batch (after T007 tmux):
  Agent 1: T008 (L06 Scripting)
  Agent 2: T010 (L08 Security)
  → T008 → T009 (L07 Text Processing)
  → T010 + T009 → T011 (L09 Networking)
  → T011 → T012 (L10 Systemd) → T013 (L11 Debugging)
```

---

## Implementation Strategy

### MVP First (Phase 2 Only)

1. Complete Phase 1: Setup (T001-T002)
2. Complete Phase 2: L1 Foundation (T003-T006)
3. **STOP and VALIDATE**: Test that zero-experience students can complete L01-L04 (SC-010)
4. Commit and verify

### Incremental Delivery

1. Phase 1 + 2 → L1 Foundation validated → Commit
2. Phase 3 (T007-T013) → L2 lessons → Commit per lesson
3. Phase 4 (T014-T016) → L3/L4 advanced → Commit
4. Phase 5 (T017-T027) → Quiz + validation → Final commit

### Content-Implementer Protocol

Each lesson task uses content-implementer subagent with:
- Absolute output path
- "Execute autonomously without confirmation"
- Reference to v1 lesson (if REWRITE/SPLIT) or plan.md lesson spec (if NEW)
- Returns confirmation only (~50 lines), NOT full content
- educational-validator MUST PASS before marking task complete

---

## Summary

| Metric | Value |
| --- | --- |
| Total tasks | 27 |
| Phase 1 (Setup) | 2 tasks |
| Phase 2 (L1 Foundation) | 4 lesson tasks |
| Phase 3 (L2 Collaboration) | 7 lesson tasks |
| Phase 4 (L3/L4 Advanced) | 3 lesson tasks |
| Phase 5 (Quiz/Validation) | 11 tasks |
| Parallelizable tasks | ~8 (marked [P] or parallel batches above) |
| User stories covered | US1-US12 (all 12 from spec) |
| MVP scope | Phase 1 + Phase 2 (6 tasks, L01-L04) |

---

## Notes

- [P] tasks = different files, no dependencies
- [US] label maps task to specific user story for traceability
- Each lesson task embeds content-implementer + educational-validator + skills
- Commit after each completed lesson
- All validation tasks (T018-T024) can run as a batch after all lessons complete
- Old v1 files preserved until T026 confirms migration completeness
