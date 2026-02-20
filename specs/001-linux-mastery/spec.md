# Feature Specification: Linux Mastery for Digital FTEs

**Feature Branch**: `001-linux-mastery`
**Created**: 2026-02-08
**Status**: Draft
**Input**: User description: "Linux Mastery for Digital FTEs - Comprehensive Linux command-line and system administration skills for AI agent development"

## Executive Summary

This specification defines Chapter 10: Linux Mastery for Digital FTEs, a comprehensive educational chapter teaching students the Linux command-line and system administration skills required to deploy, manage, and monitor AI agents (Digital FTEs) in production environments. The chapter progresses from terminal fundamentals through advanced topics like systemd services, security hardening, and debugging techniques.

**Key Insight**: AI agents run on Linux servers. Understanding Linux is not optional—it's the interface through which you control, monitor, and secure your Digital FTEs.

## User Scenarios & Testing

### User Story 1 - Terminal Cockpit & Environment Setup (Priority: P1)

A student new to Linux command-line needs to transform their mindset from "GUI user" to "terminal architect" by learning essential CLI navigation, package management, and shell customization techniques that enable efficient agent development and deployment.

**Why this priority**: Without terminal proficiency, students cannot effectively deploy, monitor, or debug AI agents. This is the foundation upon which all other skills build. The terminal is the native interface for AI Agent execution.

**Independent Test**: Student can navigate to any directory using modern tools (zoxide, fzf), install packages via apt, customize their shell with aliases, and explain why CLI is superior for AI agent operations. Can be tested by having student set up a complete development environment and perform common navigation tasks.

**Acceptance Scenarios**:

1. **Given** a fresh Ubuntu/Debian system, **When** student opens terminal, **Then** they can explain the CLI mindset and why it's essential for AI agents
2. **Given** need to install a package, **When** student runs `sudo apt update && sudo apt install`, **Then** package installs safely with understanding of what each command does
3. **Given** frequent directory navigation needs, **When** student installs and configures zoxide, **Then** they can jump to any previously visited directory with fuzzy matching
4. **Given** need to search command history, **When** student uses fzf, **Then** they can find and execute previous commands in milliseconds
5. **Given** repetitive command patterns, **When** student edits .bashrc/.zshrc, **Then** they have aliases and environment variables configured for their workflow

---

### User Story 2 - Persistent Session Management with tmux (Priority: P2)

A student working on long-running agent tasks needs to maintain terminal sessions that survive network disconnections, closed laptops, and SSH timeouts while enabling multi-pane workflows for monitoring logs and editing code simultaneously.

**Why this priority**: AI agents run for hours or days. Students need sessions that persist beyond connection drops and the ability to monitor multiple processes simultaneously. This is critical for production agent management.

**Independent Test**: Student can create tmux sessions, split panes, detach safely, and reattach later. Can be tested by starting a long-running process, detaching, disconnecting, reconnecting, and verifying process continued running.

**Acceptance Scenarios**:

1. **Given** SSH connection to remote server, **When** student creates tmux session, **Then** session persists after SSH disconnect
2. **Given** need to monitor agent logs while editing code, **When** student splits window into panes, **Then** they can view logs in one pane and edit in another
3. **Given** complex workflow layout, **When** student saves session configuration, **Then** they can restore exact layout after system reboot
4. **Given** multiple concurrent projects, **When** student creates named sessions, **Then** they can switch between project contexts instantly
5. **Given** accidentally closed terminal, **When** student reattaches to tmux session, **Then** all previous processes and layout are intact

---

### User Story 3 - Agentic Automation & Shell Scripting (Priority: P1)

A student needs to automate repetitive agent management tasks (setup, execution, maintenance) by writing bash scripts that chain commands together, process text data, and run on schedules.

**Why this priority**: Automation is core to the "Digital FTE" concept. Students must script common agent operations to avoid repetitive manual work and ensure consistency. This directly enables agent lifecycle management.

**Independent Test**: Student can write executable .sh scripts that automate setup/execution/maintenance, use grep/sed/awk for log parsing, and create cron jobs for scheduled tasks. Can be tested by having student automate a complete agent deployment workflow.

**Acceptance Scenarios**:

1. **Given** repetitive agent setup steps, **When** student writes bash script, **Then** setup executes consistently with single command
2. **Given** large log files from agent runs, **When** student uses grep/sed/awk, **Then** they can extract specific data patterns without manual scrolling
3. **Given** need to chain multiple commands, **When** student uses pipes and redirection, **Then** output flows efficiently between commands
4. **Given** need for periodic agent health checks, **When** student creates cron job, **Then** checks run automatically on schedule
5. **Given** script failure, **When** student adds error handling, **Then** script provides meaningful error messages and safe failure modes

---

### User Story 4 - System Governance & Least Privilege Security (Priority: P1)

A student deploying production AI agents needs to implement security best practices by creating non-root users, managing permissions with chmod/chown, securing SSH access, and safely managing API keys without hardcoding.

**Why this priority**: Security is non-negotiable for production systems. Running agents as root or hardcoding credentials creates unacceptable risk. This teaches essential "least privilege" principles.

**Independent Test**: Student can create dedicated agent users, restrict file permissions, generate SSH key pairs, disable password logins, and pass secrets via environment variables. Can be tested by having student harden a server for agent deployment.

**Acceptance Scenarios**:

1. **Given** new agent deployment, **When** student creates dedicated non-root user, **Then** agent runs with minimal required permissions
2. **Given** sensitive configuration files, **When** student uses chmod/chown, **Then** files are readable only by necessary users
3. **Given** need for secure remote access, **When** student generates SSH keys, **Then** they can authenticate without passwords
4. **Given** password-based security risks, **When** student disables password logins, **Then** SSH requires key-based authentication only
5. **Given** API keys needed for agent, **When** student uses environment variables, **Then** credentials are never hardcoded in scripts or configs

---

### User Story 5 - Process Control & Systemd Reliability (Priority: P1)

A student needs to deploy AI agents as system services that automatically restart on failure, start on boot, and can be monitored for resource consumption using htop/btop.

**Why this priority**: Production agents must be reliable. Systemd makes agents "unkillable" by auto-restarting and ensures they survive server reboots. This is essential for production deployments.

**Independent Test**: Student can write .service files, enable services, configure restart policies, and monitor processes. Can be tested by having student deploy an agent as a service, kill it manually, and verify auto-restart.

**Acceptance Scenarios**:

1. **Given** agent that needs to run continuously, **When** student writes .service file, **Then** agent runs as managed system service
2. **Given** agent crashes during operation, **When** Restart=always is configured, **Then** systemd automatically restarts agent
3. **Given** server reboot, **When** service is enabled, **Then** agent starts automatically without manual intervention
4. **Given** agent consuming excessive resources, **When** student monitors with htop/btop, **Then** they can identify and kill runaway processes
5. **Given** need to run agent in background, **When** student uses & or nohup, **Then** process continues after terminal closes

---

### User Story 6 - Networking, Logs & Debugging Sensors (Priority: P2)

A student troubleshooting agent issues needs to diagnose network connectivity problems, review system logs, monitor agent output in real-time, and manage disk space to prevent log-related failures.

**Why this priority**: When agents fail (and they will), students need debugging skills to diagnose issues. This teaches systematic troubleshooting using Linux's built-in monitoring tools.

**Independent Test**: Student can test network connectivity, diagnose failures, read journalctl logs, stream logs with tail -f, and check disk usage. Can be tested by simulating common failure scenarios and having student diagnose root cause.

**Acceptance Scenarios**:

1. **Given** agent cannot reach external API, **When** student uses curl/wget, **Then** they can test connectivity and identify failure point
2. **Given** network connectivity issue, **When** student uses ip addr/netstat/ping, **Then** they can diagnose whether problem is local, network, or remote
3. **Given** systemd service failing to start, **When** student reads journalctl logs, **Then** they can identify error causing failure
4. **Given** agent running but behaving unexpectedly, **When** student uses tail -f on logs, **Then** they can observe agent behavior in real-time
5. **Given** server running out of disk space, **When** student uses df -h and du, **Then** they can identify which directories/files are consuming space

---

### Edge Cases

- What happens when student accidentally deletes critical system files while learning permissions?
- How does system handle running out of disk space due to runaway agent logs?
- What happens when systemd service fails to start and enters restart loop?
- How does student recover lost tmux session if server reboots without persistence configuration?
- What happens when cron job fails silently due to permission issues?
- How does system handle SSH lockout if student misconfigures authentication?
- What happens when agent requires specific Python version conflicting with system Python?
- How does student diagnose issues when both network and local problems occur simultaneously?

## Requirements

### Functional Requirements

**FR-001**: Student MUST be able to navigate Linux filesystem using modern tools (zoxide for smart directory jumping, fzf for fuzzy finding)

**FR-002**: Student MUST be able to install system packages using apt package manager with understanding of update/upgrade/install workflow

**FR-003**: Student MUST be able to customize shell environment (.bashrc/.zshrc) with aliases, functions, and environment variables

**FR-004**: Student MUST be able to create, detach, and reattach tmux sessions that persist beyond SSH disconnections

**FR-005**: Student MUST be able to split tmux windows into multiple panes for simultaneous monitoring and editing

**FR-006**: Student MUST be able to write executable bash scripts that automate agent setup, execution, and maintenance tasks

**FR-007**: Student MUST be able to use grep, sed, and awk for text processing and log parsing

**FR-008**: Student MUST be able to chain commands using pipes (|) and redirection (>, >>)

**FR-009**: Student MUST be able to schedule automated tasks using cron

**FR-010**: Student MUST be able to manage file permissions using chmod and ownership using chown

**FR-011**: Student MUST be able to create dedicated non-root Linux users for running agents

**FR-012**: Student MUST be able to generate SSH key pairs and configure key-based authentication

**FR-013**: Student MUST be able to disable password-based SSH logins for hardened security

**FR-014**: Student MUST be able to pass secrets to agents using environment variables without hardcoding

**FR-015**: Student MUST be able to monitor system resources using htop or btop

**FR-016**: Student MUST be able to manage processes using ps, kill, and background execution (&)

**FR-017**: Student MUST be able to write systemd .service files for agent deployment

**FR-018**: Student MUST be able to configure systemd services for auto-restart on failure

**FR-019**: Student MUST be able to enable services to start on system boot

**FR-020**: Student MUST be able to test network connectivity using curl and wget

**FR-021**: Student MUST be able to diagnose network issues using ip addr, netstat, and ping

**FR-022**: Student MUST be able to read system logs using journalctl

**FR-023**: Student MUST be able to stream log output in real-time using tail -f

**FR-024**: Student MUST be able to monitor disk usage using df -h and analyze directory sizes using du

**FR-025**: Content MUST explain WHY CLI is superior to GUI for AI agent operations (architect mindset)

**FR-026**: Content MUST emphasize "least privilege" security principles throughout

**FR-027**: Content MUST demonstrate how each Linux skill applies specifically to AI agent lifecycle

**FR-028**: Examples MUST use realistic agent deployment scenarios (not generic Linux examples)

**FR-029**: Security warnings MUST be included for dangerous operations (rm -rf, chmod 777, running as root)

**FR-030**: Content MUST progress from basic to advanced within each topic area

### Assumed Knowledge

**What students know BEFORE this chapter**:
- Basic computer literacy (files, directories, applications)
- Concept of "servers" vs "personal computers"
- What an "AI agent" is (from Chapter 11)
- Basic command-line exposure (from earlier chapters using git, npm, etc.)
- Understanding that code runs on servers somewhere

**What this chapter must explain from scratch**:
- Linux filesystem structure (/, /home, /etc, /var, /usr)
- What a "shell" is and how it differs from a terminal
- sudo and root user concept
- Permissions model (user/group/others, read/write/execute)
- What a "daemon" or "service" is
- Environment variables and why they matter
- SSH protocol basics
- System logging concepts

### Key Entities

- **Terminal/Shell**: The command-line interface through which students interact with Linux systems
- **Package Manager (apt)**: System for installing, updating, and removing software
- **tmux Session**: A persistent terminal multiplexer session that survives disconnections
- **Bash Script**: Executable text file containing sequence of shell commands
- **Systemd Service**: Background process managed by systemd init system with auto-restart capabilities
- **Environment Variable**: Named value stored in shell environment accessible to running processes
- **SSH Key Pair**: Cryptographic key pair (public/private) for secure authentication
- **System Log**: Recorded events from system services and applications
- **Process**: Running instance of a program with unique PID
- **Cron Job**: Scheduled task that runs automatically at specified intervals

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can set up a complete Linux development environment with modern navigation tools in under 30 minutes
- **SC-002**: Students can explain the CLI "architect mindset" and why it's essential for AI agent operations
- **SC-003**: 95% of students successfully create and manage persistent tmux sessions for long-running agent tasks
- **SC-004**: Students can write a bash script that automates a complete agent deployment (install deps, configure, start) in under 50 lines
- **SC-005**: Students can harden a server by creating non-root users, disabling password SSH, and configuring permissions in under 20 minutes
- **SC-006**: 90% of students successfully deploy an agent as a systemd service with auto-restart and start-on-boot
- **SC-007**: Students can diagnose common agent failures (network, permissions, missing deps) using system tools in under 10 minutes
- **SC-008**: Students demonstrate understanding of "least privilege" by correctly justifying permission choices in all exercises
- **SC-009**: Students can monitor agent health and resource consumption in real-time using appropriate tools
- **SC-010**: Quiz completion rate above 85% with average score above 80%

### Quality Metrics

- **Content Quality**: All examples use realistic agent scenarios (generic "hello world" examples prohibited)
- **Safety Coverage**: Every dangerous operation includes explicit warning and safer alternative
- **Progression Validation**: Each lesson builds directly on previous lesson concepts
- **Practical Application**: Every command/tool is tied to specific agent use case
- **Troubleshooting Coverage**: Common failure modes included for each major topic

### Educational Outcomes

- Students shift from "Linux is scary" to "Linux is my agent control panel"
- Students understand that production deployment = Linux administration
- Students can confidently SSH into servers and manage agent deployments
- Students have mental models for diagnosing agent issues systematically
- Students practice safe security habits by default (least privilege, no hardcoded secrets)

## Assumptions

1. Students have access to a Linux system (Ubuntu/Debian assumed, concepts apply broadly)
2. Students have sudo privileges on their learning system
3. Students are comfortable with typing commands (fear of "breaking things" addressed early)
4. Students understand AI agents run on servers (not on their laptop)
5. Students have basic Git experience from Chapter 9
6. Learning environment allows mistakes (VM, container, or non-production server)
7. SSH access to remote server is available or can be simulated locally
8. Standard Linux tools are available (no exotic package requirements)

## Constraints & Non-Goals

### Constraints

- MUST focus on Ubuntu/Debian Linux (most common for servers)
- MUST NOT assume GUI access (all tasks possible via SSH)
- MUST emphasize safety and recovery from mistakes
- MUST tie every concept to agent deployment/use case
- MUST progress from simple to complex within each topic

### Non-Goals (Explicitly Out of Scope)

- Deep Linux internals (kernel architecture, system calls)
- Advanced kernel customization or compilation
- Network protocol deep-dives (TCP/IP stacks, routing protocols)
- Container technology (Docker covered in Chapter 49)
- Cloud platform specifics (AWS/GCP/Azure CLI tools)
- Performance tuning at kernel level
- SELinux or AppArmor advanced security
- High-availability clustering or load balancing
- Linux distribution comparisons (Ubuntu vs CentOS vs Alpine)

## Dependencies

### Prerequisite Chapters

- Chapter 9: Version Control (Git command-line experience)
- Chapter 11: Introduction to AI Agents (understands what agents are)
- Chapter 40-42: FastAPI/ChatKit (understands agent server architecture)

### Related Future Chapters

- Chapter 49: Docker for AI Services (builds on Linux skills)
- Chapter 50: Kubernetes (builds on systemd concepts)
- Chapter 58: Production Security (builds on SSH/permissions)

### External Resources

- Ubuntu/Debian official documentation
- tmux official documentation
- systemd official documentation
- bash scripting guides

## Out of Scope

The following are explicitly out of scope for this chapter:

- GUI Linux desktop usage
- Linux installation or dual-boot setup
- Windows Subsystem for Linux (WSL) specific configuration
- Mac OS X command-line differences
- Advanced bash programming (arrays, associative arrays, advanced string manipulation)
- Network security beyond basic SSH hardening
- Firewall configuration (ufw, iptables)
- Backup and recovery strategies
- Linux performance profiling (perf, strace)
- Cross-platform compatibility considerations

## Open Questions

[None - specification is complete for planning phase]

---

**Document Version**: 1.0.0
**Last Updated**: 2026-02-08
**Ready for Planning**: Yes
