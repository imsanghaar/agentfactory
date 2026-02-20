---
title: "Practice: Linux Mastery Exercises"
practice_exercise: ch11-linux
sidebar_position: 15
chapter: 11
lesson: 15
duration_minutes: 180

primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Hands-on practice applying Lessons 1-14 Linux operations workflows through 14 guided exercises and 3 capstones"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

skills:
  - name: "Linux System Administration"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student applies filesystem navigation, text processing, scripting, service management, and debugging workflows to realistic server scenarios"

  - name: "Production Debugging"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student diagnoses service failures, security violations, broken scripts, and cascading errors by systematic layer-by-layer investigation"

  - name: "Deployment Pipeline Design"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student designs and implements complete automated deployment pipelines combining user creation, file management, service configuration, and validation"

learning_objectives:
  - objective: "Apply filesystem navigation, text processing, scripting, and service management to realistic agent deployment scenarios"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful completion of Build exercises across 6 modules"
  - objective: "Diagnose server failures including broken scripts, service startup failures, security violations, and cascading dependency errors"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Accurate identification of all planted bugs and root causes in Debug exercises"
  - objective: "Design and implement complete automated deployment pipelines that are idempotent, secure, and validated"
    proficiency_level: "B2"
    bloom_level: "Create"
    assessment_method: "Capstone project completion with deployment spec, implementation, and verification"

cognitive_load:
  new_concepts: 3
  assessment: "3 meta-concepts (workflow application, systematic debugging, pipeline design) — within B1-B2 range. Exercises reinforce existing L01-L14 knowledge rather than introducing new tools."

differentiation:
  extension_for_advanced: "Complete all 3 capstone projects; attempt exercises with minimal prompts; write reusable automation scripts"
  remedial_for_struggling: "Start with Module 1 only; use the starter prompts provided; focus on Build exercises before Debug"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 5
  session_title: "Skills, Capstone, and Practice"
  key_points:
    - "These exercises close the gap between understanding commands and using them under pressure — fluency requires practice beyond reading lessons"
    - "Each module pairs a Build exercise (apply skills) with a Debug exercise (diagnose failures) — both are essential for production readiness"
    - "The three capstone projects test end-to-end integration: deployment pipeline, security audit remediation, and monitoring system design"
    - "Exercise files are real configs, log files, and broken scripts — not sanitized examples; messy reality is where learning happens"
  misconceptions:
    - "Students think completing the lessons means they are ready for production — exercises reveal gaps between understanding a concept and applying it under constraints"
    - "Students skip Debug exercises because they are harder — diagnosing failures is more valuable than building from scratch because production work is mostly debugging"
    - "Students try to complete all 17 exercises in one session — recommend one module per sitting to prevent fatigue and allow reflection"
  discussion_prompts:
    - "Which exercise was hardest? What did the difficulty reveal about gaps in your understanding from the lessons?"
    - "When debugging a broken exercise, how did you decide where to start investigating? Did you follow the triage methodology from lesson 11?"
  teaching_tips:
    - "This is the chapter closer for practice — set expectations that students should complete at least 7 exercises (one per module) plus one capstone to demonstrate proficiency"
    - "Encourage students to attempt exercises without the starter prompts first — the starter prompts are safety nets, not starting points"
    - "The Debug exercises are where the real learning happens — allocate more class time to debugging than building, as students need practice with the triage mindset"
    - "Have students reflect after each module using the provided questions — reflection cements the operational intuition that makes Linux skills automatic"
  assessment_quick_check:
    - "Ask students which module they found most challenging and why — the answer reveals which lessons need review"
    - "Ask: in a Debug exercise, what is the first thing you check? (Expected: read the error message or logs — not restart the service)"
    - "Have students describe their approach to one capstone project in 3 sentences — this tests synthesis, not recall"
---

# Practice: Linux Mastery Exercises

You've learned to navigate Linux filesystems, edit configs with pipes and streams, script deployments in bash, harden security, manage systemd services, and debug production failures. That's real capability. But knowing the commands and using them under pressure when a production agent is down at 3am are different things. The gap between understanding `grep` and using it to isolate the one log line that explains why your agent crashed across 50,000 lines of output is where most people stall. These exercises close the gap between understanding and fluency.

These 14 exercises plus 3 capstone projects cover the full range of Linux operations you've studied in Lessons 1-14. Each module gives you two exercises: a **Build** exercise where you apply skills to a realistic server scenario, and a **Debug** exercise where you diagnose what went wrong in a broken system. Three skills run through every exercise: **Linux system administration** (applying filesystem navigation, text processing, scripting, and service management), **production debugging** (diagnosing failures by systematic layer-by-layer investigation), and **deployment pipeline design** (combining all skills into automated, idempotent workflows).

Every exercise uses real starter files — actual configs, log files, broken scripts, and service definitions you'll investigate, fix, and deploy. This isn't hypothetical. By the end, you'll have practiced every Linux operations workflow on messy, realistic server scenarios where one wrong `chmod` can lock you out and one missed log line can hide the root cause for hours.

:::info Download Exercise Files
**[Download Linux Mastery Exercises (ZIP)](https://github.com/imsanghaar/claude-code-linux-mastery-exercises/releases/latest/download/linux-mastery-exercises.zip)**

After downloading, unzip the file. Each exercise has its own folder with an `INSTRUCTIONS.md` and starter files you need.

If the download link doesn't work, visit the [repository releases page](https://github.com/imsanghaar/claude-code-linux-mastery-exercises/releases) directly.
:::

---

## How to Use These Exercises

The workflow for every exercise is the same:

1. **Open the exercise folder** from the `claude-code-linux-mastery-exercises/` directory
2. **Read the INSTRUCTIONS.md** inside the folder — it describes the scenario and starter files
3. **Read the walkthrough below** for context on what you're practicing and why
4. **Start Claude Code** and point it at the exercise folder
5. **Work through the exercise** — write your own prompts (use starters only if stuck)
6. **Reflect** using the questions provided — this is where the real learning happens

You don't need to complete all 17 exercises in one sitting. Work through one module at a time. Each module builds on the workflows from specific chapter lessons.

---

## Tool Guide

- **Claude Code** — Required for all exercises. Linux operations are terminal work: navigating servers, editing configs, writing scripts, managing services, reading logs. Claude Code runs these operations directly.
- **Cowork** — Can be used for Exercise 4.2 (analyzing security audit findings) and capstone planning where you're designing deployment architectures on paper before executing. But Claude Code is strongly preferred since every exercise involves manipulating real files, configs, and services.

---

## Key Differences from Chapter Lessons

In Lessons 1-14, you learned each Linux skill in isolation with guided walkthroughs. These exercises are different in four ways:

- **No step-by-step instructions.** The exercises describe the scenario and the goal. You decide the approach, choose the commands, and handle edge cases yourself.
- **Build + Debug pairing.** Every module has a Build exercise (apply the skill) and a Debug exercise (diagnose someone else's broken system). Debugging someone else's server develops different skills than setting up your own — you learn to read logs, trace dependencies, and think backwards from symptoms to root causes.
- **Increasing independence.** Modules 1-2 provide starter prompts to scaffold your learning. Modules 3-6 remove the scaffolding. Capstones remove everything — you design the entire approach.
- **Real server scenarios.** These aren't toy files — they're configs, services, logs, and security issues modeled on actual production failures. The broken script in Module 3 has the exact kinds of bugs that cause 3am incidents.

By Module 6, you should be able to face a production server problem and instinctively reach for the right investigation, fix, and verification workflow without needing to review the chapter lessons.

---

## The Linux Operations Framework

Use this for every exercise:

1. **Investigate** — What's the current state? Check before assuming. Run `ls -la`, read logs, check service status. Never change anything until you know what you're working with.
2. **Plan** — Design your approach before executing. What files will you change? What's the rollback strategy? Write it down.
3. **Backup** — Safety net before destructive changes. Copy configs before editing. Snapshot state before modifying services. `cp nginx.conf nginx.conf.bak` takes 2 seconds and saves 2 hours.
4. **Execute** — One change at a time. Make a single modification, then verify before making the next. Batch changes are batch disasters when something goes wrong.
5. **Verify** — Did it work? Check with specific commands. `systemctl status` after service changes. `curl localhost` after config changes. `nginx -t` before reloading. Trust commands, not assumptions.
6. **Document** — Record what you did and why. Future-you debugging at 3am will thank present-you for writing down which config line you changed and what it fixed.
7. **Automate** — If you did it twice, script it. The third time should be `bash deploy.sh`, not 47 manual commands you half-remember.

This framework applies to every server operations task, not just these exercises. Whether you're deploying an agent, hardening a server, or recovering from an outage, these seven steps prevent the mistakes that turn a 10-minute fix into a 4-hour recovery. Notice that steps 1-3 happen before any changes. That's intentional — most server disasters come from skipping investigation and jumping straight to "let me try this."

---

## Assessment Rubric

For each exercise, evaluate yourself on:

| Criteria          |             Beginner (1)             |        Developing (2)        |                   Proficient (3)                    |            Advanced (4)            |
| ----------------- | :----------------------------------: | :--------------------------: | :-------------------------------------------------: | :--------------------------------: |
| **Investigation** | Changed files without checking state | Some checks, missed key info |  Systematic state verification before every change  |   Reusable investigation scripts   |
| **Operations**    |   No backups, single large changes   |     Some safety measures     | Backup-first, atomic operations, verified each step | Scripted operations with rollback  |
| **Security**      |  Ran as root, no permission checks   |  Basic permission awareness  |      Least privilege, SSH keys, firewall rules      | Security as architectural default  |
| **Debugging**     |     Random changes hoping to fix     |       Some log reading       |         Systematic layer-by-layer diagnosis         |      Automated health checks       |
| **Automation**    |        All manual operations         |         Some scripts         |             Complete deployment scripts             |    Idempotent, tested pipelines    |
| **Documentation** |          Nothing documented          |          Some notes          |      Full server maps, audit reports, fix logs      | Runbooks and operational playbooks |

---

## Module 1: Filesystem Recon

> **Core Skill:** Mapping an unfamiliar server before touching anything (Lessons 1-2)

<ExerciseCard id="1.1" title="Agent Server Recon" />

### Exercise 1.1 — Agent Server Recon (Build)

**The Problem:**
Open the `module-1-filesystem-recon/exercise-1.1-agent-server-recon/` folder. You'll find a simulated server directory structure with 3 AI agents deployed across it: a chatbot agent in `/opt/agents/chatbot/`, a data-pipeline agent in `/opt/agents/pipeline/`, and a monitoring agent in `/opt/agents/monitor/`. Each agent has its own configs, logs, data directories, virtual environments, and systemd service files scattered across `/etc/`, `/var/log/`, `/opt/`, and `/home/`. There's no documentation. The previous admin left without a handoff.

**Your Task:**
Map the entire server. Produce a `SERVER-MAP.md` that documents: every agent's file locations (binaries, configs, logs, data, services), the directory tree of each agent's deployment, disk usage per agent, which services are defined, which ports are configured, which users own which files, and any symlinks or cross-references between agents. Someone reading your server map should be able to find any file for any agent within 30 seconds.

**What You'll Learn:**

- How to systematically map an unfamiliar server instead of randomly exploring directories
- Which commands (`find`, `du -sh`, `ls -la`, `stat`, `readlink`, `grep -r`) reveal the most about a deployment's layout
- That a thorough 15-minute recon prevents the "I didn't know that config existed" surprises that cause production incidents

**Starter Prompt (Intentionally Vague):**

> "What's running on this server?"

**Better Prompt (Build Toward This):**

After exploring with `find /opt/agents -type f | head -40`, `du -sh /opt/agents/*/`, and `ls -la /etc/systemd/system/agent-*`: "Map this entire server's agent deployment. Create SERVER-MAP.md with: (1) each agent's name, purpose, and file locations (binaries, configs, logs, data, service files), (2) directory tree per agent, (3) disk usage per agent, (4) systemd service definitions with configured ports, (5) file ownership and permissions summary, (6) symlinks and cross-references between agents, (7) a 2-sentence summary of the overall deployment architecture."

**Reflection Questions:**

1. How many files did your initial `ls /opt/agents` miss that a deeper `find` across `/etc/`, `/var/log/`, and `/home/` revealed?
2. Did any agent have files owned by unexpected users? What security implications does that create?
3. How long did the full recon take? Compare that to how long you'd spend recovering from modifying the wrong agent's config because you didn't know the layout.

---

<ExerciseCard id="1.2" title="Misplaced Deployment" />

### Exercise 1.2 — Misplaced Deployment (Debug)

**The Problem:**
Open the `module-1-filesystem-recon/exercise-1.2-misplaced-deployment/` folder. You'll find a server where someone deployed an agent incorrectly. Files are in the wrong Linux directories: application binaries in `/tmp/`, config files in `/home/deploy/` instead of `/etc/`, logs writing to `/opt/` instead of `/var/log/`, the systemd service file pointing to wrong paths, and data directories with wrong permissions. The agent technically starts but is fragile — a reboot would break it, a cleanup cron would delete its binaries, and logs are invisible to standard monitoring.

**Your Task:**
Identify every misplaced file and incorrect permission. For each problem, document: what's wrong, why it matters (what would break), where the file should be, and the command to fix it. Create a `FIX-PLAN.md` with the correct Linux filesystem hierarchy for this agent, then execute the fixes and verify the agent would survive a reboot.

**What You'll Learn:**

- The Linux Filesystem Hierarchy Standard (FHS) and why `/tmp/` is not a deployment directory
- How to distinguish "works right now" from "works correctly" — fragile deployments survive until they don't
- The specific commands (`mv`, `chown`, `chmod`, `systemctl daemon-reload`) for relocating a deployed application

**Starter Prompt (Intentionally Vague):**

> "Is this agent deployed correctly?"

**Better Prompt (Build Toward This):**

After running `find / -name "agent-*" -type f 2>/dev/null` and `systemctl cat agent-chatbot.service`: "Audit this agent deployment against the Linux Filesystem Hierarchy Standard. For each misplaced file, document: (1) current location, (2) what's wrong with that location, (3) correct location per FHS, (4) the specific risk (reboot, cron cleanup, permission escalation), (5) the fix command. Output to FIX-PLAN.md, then execute all fixes and verify with systemctl status and a test request."

**Reflection Questions:**

1. How many misplaced files did you find? Which one posed the greatest risk to production stability?
2. Would the agent have survived a server reboot before your fixes? What specifically would have broken?
3. What's your checklist for verifying a Linux deployment follows FHS? Would you use this checklist for every future deployment?

---

## Module 2: Text & Pipes

> **Core Skill:** Transforming and assembling data with pipes and text tools (Lessons 3-4)

<ExerciseCard id="2.1" title="Config Pipeline" />

### Exercise 2.1 — Config Pipeline (Build)

**The Problem:**
Open the `module-2-text-and-pipes/exercise-2.1-config-pipeline/` folder. You'll find `config-fragments/` — a directory with 12 partial configuration files. The previous admin kept agent configurations split across multiple fragment files: `base.conf`, `database.env`, `auth-secrets.template`, `nginx-upstream.conf`, `rate-limits.yaml`, and more. Each fragment has placeholder variables like `{{AGENT_PORT}}`, `{{DB_HOST}}`, and `{{LOG_LEVEL}}`. There's also a `variables.env` file with the actual values.

**Your Task:**
Build a pipeline that assembles 3 complete configuration files from the fragments: `agent.conf` (combining base + auth + rate limits), `nginx.conf` (combining upstream + server blocks), and `docker-compose.yml` (combining service definitions + env vars). Use `cat`, `sed`, `envsubst`, `grep`, and pipes to substitute variables, merge fragments, strip comments, and validate the output. Each final config must be syntactically valid.

**What You'll Learn:**

- How to chain text processing tools (`cat | sed | grep | sort`) into pipelines that transform raw fragments into usable configs
- That variable substitution with `sed` or `envsubst` replaces manual copy-paste and eliminates typos
- The discipline of validating output at each pipeline stage, not just at the end

**Starter Prompt (Intentionally Vague):**

> "Combine these config files."

**Better Prompt (Build Toward This):**

After running `ls config-fragments/` and `cat variables.env`: "Build a config assembly pipeline: (1) Read variables.env and export all variables, (2) For agent.conf: cat base.conf auth-secrets.template rate-limits.yaml, pipe through envsubst to replace all `{{VAR}}` placeholders, strip comment lines with grep -v '^#', output to agent.conf, (3) Repeat for nginx.conf and docker-compose.yml with their respective fragments, (4) Validate each output — check nginx.conf with nginx -t syntax, verify YAML with python -c 'import yaml', confirm no unresolved `{{}}` placeholders remain."

**Reflection Questions:**

1. How many pipeline stages did your longest pipeline require? Could you have achieved the same result with fewer stages?
2. Did any variable substitution produce unexpected results? What happens when a variable value contains special characters that `sed` interprets?
3. If you needed to change one variable (say, the port number) and regenerate all configs, how long would it take with your pipeline versus doing it manually?

---

<ExerciseCard id="2.2" title="Broken Pipeline Diagnosis" />

### Exercise 2.2 — Broken Pipeline Diagnosis (Debug)

**The Problem:**
Open the `module-2-text-and-pipes/exercise-2.2-broken-pipeline/` folder. You'll find `pipeline.sh` — a 4-stage text processing pipeline that should extract, transform, filter, and format agent deployment logs into a clean report. The pipeline runs without errors but produces wrong output. Somewhere in the 4 stages, data is being corrupted: fields are swapped, some lines are silently dropped, timestamps are mangled, and the final count doesn't match the input count.

**Your Task:**
Diagnose which stage(s) introduce errors. Run each stage in isolation, comparing its output against expected output. For each bug, document: which stage, what goes wrong, why (the specific command or flag that causes the issue), and the fix. Create `PIPELINE-DIAGNOSIS.md` with your findings, then fix the pipeline and verify the corrected output.

**What You'll Learn:**

- How to debug a multi-stage pipeline by isolating each stage and checking intermediate output
- That pipelines fail silently — a wrong `awk` field separator can swap columns without any error message
- The technique of `tee` for inspecting intermediate output: `stage1 | tee /tmp/debug1 | stage2 | tee /tmp/debug2 | stage3`

**Starter Prompt (Intentionally Vague):**

> "This pipeline gives wrong output. Fix it."

**Better Prompt (Build Toward This):**

After running `cat pipeline.sh` and `head -5 input.log`: "Debug this 4-stage pipeline by running each stage in isolation. For each stage: (1) capture input with tee, (2) capture output with tee, (3) compare against expected intermediate output, (4) identify if this stage introduces errors. For every bug found, document: stage number, symptom, root cause (the specific flag/regex/separator), and the fix. Output to PIPELINE-DIAGNOSIS.md. Then apply all fixes and verify the corrected pipeline produces the expected final output."

**Reflection Questions:**

1. How many stages had bugs? Were any bugs in stages that appeared to work correctly at first glance?
2. Which debugging technique was most effective: running stages in isolation, using `tee`, or comparing line counts?
3. What convention would you adopt for writing pipelines that makes them easier to debug? (Hint: think about intermediate output and comments.)

---

## Module 3: Sessions & Scripting

> **Core Skill:** Persistent sessions and bash scripting for automation (Lessons 5-6)

<ExerciseCard id="3.1" title="Tmux Control Center" />

### Exercise 3.1 — Tmux Control Center (Build)

**The Problem:**
Open the `module-3-sessions-and-scripting/exercise-3.1-tmux-control-center/` folder. You'll find `agent-monitor-spec.md` — a specification for a tmux-based agent monitoring dashboard. The spec describes a tmux session with 3 windows: Window 1 shows live logs from all 3 agents (split into 3 panes, each tailing a different log file), Window 2 shows system resource usage (`htop` or `top`, `df -h`, `free -m` in 3 panes), and Window 3 is a command pane for running ad-hoc commands. The session must persist after SSH disconnection and auto-attach on login.

**Your Task:**
Write a `setup-monitoring.sh` script that creates this entire tmux environment. The script must: create the session, create all 3 windows with descriptive names, split panes in each window, start the correct commands in each pane, and add a line to `.bashrc` that auto-attaches on login. Test by running the script, detaching, and reattaching to verify everything persists.

**What You'll Learn:**

- How to script tmux sessions programmatically (`tmux new-session -d`, `tmux split-window`, `tmux send-keys`)
- That a monitoring control center is the foundation for every production deployment — you cannot manage what you cannot see
- The discipline of making setup scripts idempotent: running the script twice should not create duplicate sessions

**Reflection Questions:**

1. Did your script handle the case where the tmux session already exists? What happens if you run it twice?
2. How would you modify the script to add a 4th agent? Is that a one-line change or a restructure?
3. What information would you add to the monitoring dashboard that isn't in the spec? What would a 3am on-call engineer need to see first?

---

<ExerciseCard id="3.2" title="Script Autopsy" />

### Exercise 3.2 — Script Autopsy (Debug)

**The Problem:**
Open the `module-3-sessions-and-scripting/exercise-3.2-script-autopsy/` folder. You'll find `deploy-agent.sh` — a 60-line deployment script that's supposed to: create a deploy user, clone a repository, install dependencies, configure environment variables, set up the systemd service, and start the agent. The script has 5 bugs ranging from subtle to catastrophic. It was written in a hurry and never tested end-to-end.

**Your Task:**
Read the script line by line. Find all 5 bugs. For each bug, document: the line number, the symptom it would cause, the root cause, the severity (would it fail loudly, fail silently, or cause security issues?), and the fix. Create `SCRIPT-AUTOPSY.md` with your findings. Then fix all bugs and verify the corrected script by tracing through it with `bash -x deploy-agent.sh` (dry run).

**What You'll Learn:**

- The 5 most common bash script bugs: unquoted variables, missing error handling (`set -e`), hardcoded paths, race conditions, and permission errors
- How to read a script critically — not just "does this look right" but "what happens when this variable is empty?"
- That `bash -x` (trace mode) reveals exactly what each line executes, catching bugs that code review misses

**Reflection Questions:**

1. Which bug would cause the most damage in production? Which would be hardest to diagnose from the symptoms alone?
2. Did you find any bugs that you've written yourself in past scripts? What does that tell you about your scripting habits?
3. What checks would you add to the beginning of the script to catch problems early? (Hint: `set -euo pipefail`, prerequisite checks, root detection.)

---

## Module 4: Logs & Security

> **Core Skill:** Extracting intelligence from logs and auditing security posture (Lessons 7-8)

<ExerciseCard id="4.1" title="Agent Log Forensics" />

### Exercise 4.1 — Agent Log Forensics (Build)

**The Problem:**
Open the `module-4-logs-and-security/exercise-4.1-agent-log-forensics/` folder. You'll find `agent-logs/` — a directory with 5 log files totaling 500+ lines from 3 different agents over 48 hours. The logs contain a mix of INFO, WARN, ERROR, and DEBUG messages. Somewhere in these logs is the evidence of a performance degradation that started gradually and then caused a cascading failure. The agents are interdependent: the chatbot calls the pipeline agent, which calls an external API.

**Your Task:**
Extract the story from these logs. Build a `FORENSIC-REPORT.md` that documents: a timeline of events (when did things start going wrong?), the chain of causation (which agent failed first and how did it cascade?), key metrics (error rate over time, response time degradation), and the root cause. Use `grep`, `awk`, `sed`, `sort`, `uniq -c`, and `tail` to extract and analyze — don't just read the logs manually.

**What You'll Learn:**

- How to use `grep -c "ERROR" agent-*.log` and `awk '{print $1}' | sort | uniq -c` to quantify log patterns instead of guessing
- That log forensics is about building a timeline, not just finding errors — the sequence matters more than the individual messages
- The technique of correlating logs across multiple services by timestamp to trace cascading failures

**Starter Prompt (Intentionally Vague):**

> "What went wrong in these logs?"

**Better Prompt (Build Toward This):**

After running `wc -l agent-logs/*.log` and `grep -c ERROR agent-logs/*.log`: "Analyze these agent logs forensically. (1) Extract all ERROR and WARN lines, sort by timestamp, (2) Count errors per hour per agent to find when degradation started, (3) Correlate timestamps across agents to trace cascade order, (4) Extract response times with awk and calculate averages per hour, (5) Identify root cause. Output a FORENSIC-REPORT.md with: timeline of events, cascade chain, key metrics (error counts, response time trend), and root cause analysis."

**Reflection Questions:**

1. How long did it take to identify the root cause? Would reading the logs manually have been faster or slower than using grep/awk pipelines?
2. Which agent's logs contained the actual root cause? Was it the agent that failed most visibly, or a different one?
3. What log format improvements would make future forensics easier? What information was missing from these logs that you wished you had?

---

<ExerciseCard id="4.2" title="Security Audit" />

### Exercise 4.2 — Security Audit (Apply)

**The Problem:**
Open the `module-4-logs-and-security/exercise-4.2-security-audit/` folder. You'll find a simulated server directory structure with 8+ deliberate security violations: world-readable SSH keys, a passwordless sudo configuration, services running as root, open ports without firewall rules, a `.env` file with plaintext API keys committed to a git repo, overly permissive file permissions on config files, a cron job running an unverified remote script, and weak file ownership on sensitive directories.

**Your Task:**
Audit the entire server for security violations. For each finding, document: what you found, where (file path and permissions), why it's dangerous (specific attack vector), severity (Critical/High/Medium/Low), and the remediation command. Create a `SECURITY-REPORT.md` organized by severity. Then apply all remediations and verify each fix.

**What You'll Learn:**

- The systematic approach to security auditing: check users, permissions, services, network, cron, and secrets in that order
- That security violations often look harmless in isolation but combine into attack chains — a world-readable key + passwordless sudo = full compromise
- The specific commands (`find / -perm -o+w`, `ss -tlnp`, `crontab -l`, `grep -r "API_KEY"`) that reveal common vulnerabilities

**Reflection Questions:**

1. Which violation did you consider most critical? Would a real attacker agree with your severity rankings?
2. Did any violations combine into a chain where fixing one would prevent exploitation of another?
3. How long did your audit take? What would you automate for a recurring weekly audit?

---

## Module 5: Networking & Services

> **Core Skill:** Configuring production services and diagnosing startup failures (Lessons 9-10)

<ExerciseCard id="5.1" title="Systemd from Scratch" />

### Exercise 5.1 — Systemd from Scratch (Build)

**The Problem:**
Open the `module-5-networking-and-services/exercise-5.1-systemd-from-scratch/` folder. You'll find `agent-app/` — a Python-based AI agent application with its source code, requirements, and a README describing how to run it manually (`python main.py`). There's no systemd service file. Your job is to create a production-grade service that goes beyond `ExecStart=python main.py`.

**Your Task:**
Write a complete `agent-chatbot.service` file that includes: proper `After=` dependencies (network, database), a dedicated service user with minimal privileges, environment file loading from `/etc/agent-chatbot/env`, working directory configuration, restart policy with backoff (`RestartSec=5`, `StartLimitBurst=3`), resource limits (`MemoryMax=512M`, `CPUQuota=50%`), logging to journal with a syslog identifier, and a `prestart` script that validates the config. Install, enable, start, and verify the service. Test the restart policy by killing the process and confirming it recovers.

**What You'll Learn:**

- That a production systemd service is 30+ lines of defense-in-depth: each directive prevents a specific class of failure
- How `MemoryMax` prevents a memory leak from taking down the entire server, and `CPUQuota` prevents a runaway loop from starving other services
- Why `RestartSec` with backoff prevents a crash loop from flooding logs and consuming resources

**Reflection Questions:**

1. How many directives did your final service file contain? Which one would have the highest impact if omitted?
2. What happens when the agent's config file is invalid? Does your `prestart` check catch it before the service starts?
3. How would you adapt this service file for a different agent? Which lines are agent-specific and which are boilerplate?

---

<ExerciseCard id="5.2" title="Why Won't It Start?" />

### Exercise 5.2 — Why Won't It Start? (Debug)

**The Problem:**
Open the `module-5-networking-and-services/exercise-5.2-why-wont-it-start/` folder. You'll find 3 systemd service files (`agent-alpha.service`, `agent-beta.service`, `agent-gamma.service`) that all fail to start. Each failure has a different root cause: one has a dependency cycle, one has a wrong `ExecStart` path, and one has a permission error on its environment file. The symptom is the same for all three — `systemctl start agent-X` fails — but the diagnostic path is different for each.

**Your Task:**
Diagnose each failure independently. For each service, document: the symptom (`systemctl status` output), the diagnostic commands you ran (`journalctl -u`, `systemctl cat`, `ls -la`, `namei -l`), the root cause, and the fix. Create `SERVICE-DIAGNOSIS.md` with all three cases. Fix each one and verify all three services start cleanly.

**What You'll Learn:**

- The diagnostic ladder for systemd failures: `systemctl status` (quick check) -> `journalctl -u` (detailed logs) -> `systemctl cat` (verify unit file) -> path/permission checks (verify filesystem)
- That the error message in `systemctl status` is often a symptom, not the root cause — you need `journalctl` for the real story
- How three completely different bugs produce the same "failed to start" symptom, proving that diagnosis requires investigation, not pattern matching

**Reflection Questions:**

1. Which failure was hardest to diagnose? Was the difficulty in finding the right log line or in understanding what it meant?
2. Did `systemctl status` give you enough information for any of the three? When did you need to go deeper with `journalctl`?
3. What's your personal diagnostic checklist for "service won't start" going forward? Order the steps by how quickly they narrow down the cause.

---

## Module 6: Debugging & Workflows

> **Core Skill:** Tracing failures across layers and building end-to-end automation (Lessons 11-12)

<ExerciseCard id="6.1" title="Cascade Failure" />

### Exercise 6.1 — Cascade Failure (Build)

**The Problem:**
Open the `module-6-debugging-and-workflows/exercise-6.1-cascade-failure/` folder. You'll find a simulated multi-layer agent deployment: an nginx reverse proxy, a Python API gateway, a chatbot agent, a Redis cache, and a PostgreSQL database. The user reports: "The chatbot returns HTTP 502." The actual root cause is 5 layers deep — but you don't know that yet. Each layer's logs contain clues that point to the next layer.

**Your Task:**
Trace the failure from the user-facing symptom (HTTP 502) through all 5 layers to the root cause. At each layer, document: what you checked, what you found, and why it pointed to the next layer. Create a `CASCADE-TRACE.md` that reads like a detective story — someone should be able to follow your investigation step by step and understand the reasoning at each stage.

**What You'll Learn:**

- That HTTP 502 means "the proxy got a bad response from upstream" — the bug is always deeper than the symptom
- How to trace a request through nginx logs -> API gateway logs -> application logs -> cache logs -> database logs, following the thread
- The discipline of documenting your investigation as you go — not reconstructing it after the fact when you've forgotten which log line led where

**Key Investigation Path:**

```
502 at nginx → Check nginx error log → "upstream connection refused"
→ Check API gateway → "connection timeout to chatbot:8080"
→ Check chatbot logs → "Redis connection failed, falling back to DB"
→ Check Redis → "maxmemory reached, evicting keys"
→ Check PostgreSQL → "too many connections" (root cause)
```

**Reflection Questions:**

1. At which layer were you tempted to stop and declare "found it"? Was that actually the root cause, or just another symptom?
2. How long did the full trace take? Would having pre-built monitoring dashboards have shortened it?
3. What single change at the architecture level would prevent this specific cascade from recurring?

---

<ExerciseCard id="6.2" title="Deploy Pipeline" />

### Exercise 6.2 — Deploy Pipeline (Build)

**The Problem:**
Open the `module-6-debugging-and-workflows/exercise-6.2-deploy-pipeline/` folder. You'll find `deploy-spec.md` — a specification for a complete agent deployment pipeline that chains every skill from Lessons 1-14. The spec describes deploying a new agent to a fresh server: create user, set up directories, clone code, install dependencies, configure nginx, create systemd service, set permissions, configure firewall, run health check, and send notification.

**Your Task:**
Implement `deploy-agent.sh` — a single script that executes the entire deployment pipeline. The script must be: **idempotent** (running it twice produces the same result, not duplicate users or broken configs), **logged** (every action written to `/var/log/agent-deploy.log`), **validated** (each step checks prerequisites before running), and **reversible** (a companion `rollback-agent.sh` undoes the deployment). Test by running deploy, verifying the agent works, running rollback, and deploying again.

**What You'll Learn:**

- How to chain filesystem operations, text processing, scripting, security, networking, and service management into a single automated workflow
- That idempotency is the hardest property to achieve: `useradd` fails if the user exists, `mkdir` fails if the directory exists, `systemctl enable` is already idempotent — you need to handle each case
- The value of a rollback script: knowing you can undo gives you confidence to deploy

**Reflection Questions:**

1. How many lines is your deploy script? Which section was most complex — user setup, config generation, or service management?
2. What happens if the script fails halfway through? Does your logging help you resume from where it stopped?
3. Test your idempotency: run the deploy script 3 times in a row. Does the third run produce exactly the same state as the first? If not, what's different?

---

## Module 7: Capstone Projects

> **Choose one (or more). This is where everything comes together — no starter prompts provided.**

Capstones are different from the exercises above. There are no guided prompts — you design the entire approach yourself. Each project requires applying skills from across all 14 lessons to solve a realistic production scenario. Where module exercises test individual skills, capstones test your ability to orchestrate those skills into a coherent, documented pipeline. The quality of your documentation matters as much as the result — someone should be able to follow your process and reproduce it on a different server.

<ExerciseCard id="A" title="Full Production Deployment" />

### Capstone A — Full Production Deployment

Open the `module-7-capstones/capstone-A-full-production-deployment/` folder. You'll find `deployment-spec.md` — a specification for deploying 2 agents (a chatbot and a data pipeline) to a production server from scratch. The spec defines: server requirements, agent configurations, security requirements, monitoring requirements, and success criteria.

Take this deployment through the complete Linux Operations Framework:

1. **Investigate** — Audit the "server" (exercise directory simulating a fresh install). What's already there? What's missing?
2. **Plan** — Write a `DEPLOYMENT-PLAN.md` with: user accounts, directory structure, firewall rules, service configs, monitoring setup
3. **Backup** — Create a snapshot of the server's initial state before any changes
4. **Execute** — Deploy both agents, configure nginx as reverse proxy, set up systemd services, harden security
5. **Verify** — Health checks for both agents, security audit of the deployment, resource limit verification
6. **Document** — Complete server map, service documentation, runbook for common operations
7. **Automate** — Convert your manual deployment into `deploy-all.sh` with idempotency and rollback

**Deliverables:**

- `DEPLOYMENT-PLAN.md` — Full deployment architecture and task sequence
- `SERVER-MAP.md` — Complete map of deployed server state
- `deploy-all.sh` — Idempotent deployment script for both agents
- `rollback-all.sh` — Complete rollback to initial state
- `SECURITY-AUDIT.md` — Post-deployment security verification
- `RUNBOOK.md` — Operational procedures for monitoring, restarting, and troubleshooting

**Reflection Questions:**

1. Which step took the longest? Which step prevented the most potential problems?
2. Did any step's output force you to revise an earlier step? (For example, did the security audit reveal issues in your deployment plan?)
3. How would you adapt this pipeline for deploying to 10 servers instead of 1? What changes are needed?

---

<ExerciseCard id="B" title="Server Rescue" />

### Capstone B — Server Rescue

Open the `module-7-capstones/capstone-B-server-rescue/` folder. You'll find a simulated server that has 7 simultaneous problems: a crashed agent service, a full disk partition, a misconfigured firewall blocking legitimate traffic, a broken cron job spamming logs, an exposed `.env` file with API keys, a runaway process consuming 100% CPU, and a corrupt nginx config that returns 500 on all routes.

Your job is triage. Prioritize the 7 issues by impact (what's causing the most damage right now?), fix them in order, and document everything. There's no spec — just a broken server and your skills.

**Deliverables:**

- `TRIAGE-REPORT.md` — All 7 problems listed with severity rankings and justification for priority order
- `FIX-LOG.md` — Chronological log of every fix applied: what, why, command, verification
- `POST-MORTEM.md` — Root cause analysis: how did each problem occur, and what preventive measures would stop recurrence?
- `HEALTH-CHECK.sh` — A script that tests for all 7 categories of problems and reports pass/fail

**Reflection Questions:**

1. What was your triage order? Would a different order have been more effective in hindsight?
2. Did fixing one problem affect another? (For example, did clearing disk space allow the crashed service to restart?)
3. How long did the rescue take? What percentage was diagnosis versus actual fixing? What does that ratio tell you about the value of investigation skills?

---

<ExerciseCard id="C" title="Your Own Agent" />

### Capstone C — Your Own Agent

Open the `module-7-capstones/capstone-C-your-own-agent/` folder for a self-assessment template. Then close it — this capstone uses YOUR actual project.

Pick a real project you've built (or are building) and deploy it as a production-grade Linux service:

1. **Investigate** your project's requirements — what does it need to run? (runtime, dependencies, ports, env vars, data directories)
2. **Plan** a proper Linux deployment — user accounts, directory structure, service config, security, monitoring
3. **Backup** your current state before any system-level changes
4. **Execute** the deployment on your local machine or a VM — real configs, real services, real firewall rules
5. **Verify** it works end-to-end: process starts, responds to requests, survives restart, logs correctly
6. **Document** the deployment so someone else could reproduce it
7. **Automate** with a deployment script that's idempotent and reversible

**What Makes This Special:**
Unlike Capstones A and B, this one has real consequences. The project you're deploying is code you actually care about. The service file must actually work. The security hardening must not break your application. This is where the Linux Operations Framework proves its value — or exposes gaps in your understanding.

**Deliverables:**

- `REQUIREMENTS.md` — What your project needs to run in production
- `DEPLOYMENT-PLAN.md` — Complete deployment architecture
- `deploy-my-agent.sh` — Working, tested, idempotent deployment script
- `agent.service` — Production-grade systemd service file
- `VERIFICATION-REPORT.md` — Evidence that everything works (screenshots, command output, health check results)
- `WHAT-I-LEARNED.md` — What worked, what surprised you, what you'd do differently

**Reflection Questions:**

1. Were your project's deployment requirements simpler or more complex than you expected? What surprised you?
2. Which part of the deployment was hardest — the service file, the security hardening, or the automation script?
3. Will you maintain this deployment going forward? What's the minimum maintenance effort to keep it running?

---

## What's Next

You've practiced the full range of Linux operations across 14 exercises and 3 capstone projects — filesystem recon, text processing, session management, scripting, log forensics, security auditing, service configuration, cascade debugging, and deployment automation. More importantly, you've practiced them on messy, realistic server scenarios where commands have consequences and one wrong permission can cascade into a production outage.

The Linux Operations Framework you've internalized (Investigate, Plan, Backup, Execute, Verify, Document, Automate) transfers to any domain where you direct General Agents to operate on servers, deploy services, or manage infrastructure. Whether you're deploying a new agent, recovering from a server failure, or hardening a production environment, the same seven steps prevent the same classes of mistakes.

These patterns become the foundation for the Digital FTE vision in later chapters. The investigation habits, the security instincts, the automation discipline, and the documentation practices you built here are exactly what AI Employees need to operate independently on production infrastructure. The deploy scripts you wrote, the forensic reports you compiled, and the verification workflows you practiced are the building blocks of autonomous agent operations — they just need those patterns encoded as skills rather than typed as prompts.
