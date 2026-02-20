---
sidebar_position: 11
chapter: 11
lesson: 11
title: "Lesson 11: Debugging & Troubleshooting"
description: "Diagnose production agent failures systematically using journalctl, network diagnosis, disk monitoring, and process debugging. When your Digital FTE stops working, you'll know exactly where to look."
keywords: ["debugging", "troubleshooting", "journalctl", "logs", "network diagnostics", "disk monitoring", "strace", "lsof", "triage", "agent debugging"]
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "journalctl Filtering"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student uses journalctl with --since, --until, -p, and -u flags to isolate specific error messages from service logs"

  - name: "Real-Time Log Monitoring"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student streams live log output with journalctl -f and tail -f to observe agent behavior as events occur"

  - name: "Layered Network Diagnosis"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student applies a local-to-remote diagnostic sequence (localhost curl, ss, ping, curl remote) to isolate network failures"

  - name: "Disk Space Monitoring"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student identifies disk space problems with df -h and locates space-consuming directories with du -sh"

  - name: "Process Debugging"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student uses strace and lsof to inspect system calls and open files for a running agent process"

  - name: "Structured Triage Methodology"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student follows the logs-network-disk-processes triage order to systematically diagnose agent failures without guessing"

learning_objectives:
  - objective: "Use journalctl with filters to diagnose systemd service failures"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Given a failing agent service, student uses journalctl -u, -p, --since, and --until to identify the root cause error"

  - objective: "Apply layered network diagnosis (local to DNS to remote) to isolate failures"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Given a connectivity complaint, student tests localhost, checks port binding with ss, verifies DNS with ping, and tests remote HTTP to pinpoint the failure layer"

  - objective: "Identify disk space issues using df and du"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student runs df -h to check overall usage and du -sh to find the largest directories consuming space"

  - objective: "Apply structured triage methodology (logs to network to disk to processes) to diagnose agent failures"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Given an unknown agent failure, student follows the four-phase triage order and documents findings at each phase before moving to the next"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "journalctl filtering (--since, --until, -p for priority, -u for unit)"
    - "Real-time monitoring (tail -f, journalctl -f)"
    - "Layered network diagnosis (local to DNS to remote)"
    - "Disk monitoring (df -h, du -sh)"
    - "Process debugging (strace, lsof)"
    - "Structured triage methodology (logs to network to disk to processes)"
  assessment: "6 concepts at B2 level (within the 4-7 range). Progressive application: triage methodology taught first, then applied in each diagnostic section."

differentiation:
  extension_for_advanced: "Explore advanced tools like tcpdump for packet capture, iotop for I/O monitoring, or write a bash script that runs the full triage sequence automatically and outputs a diagnostic report."
  remedial_for_struggling: "Focus on journalctl and df -h first. Get comfortable reading logs and checking disk space before adding network and process debugging. Practice one diagnostic category at a time."

teaching_guide:
  lesson_type: "core"
  session_group: 4
  session_title: "Production Agent Deployment"
  key_points:
    - "The triage methodology (logs -> network -> disk -> processes) is a systematic approach that prevents random guessing — follow the order every time"
    - "journalctl filtering (--since, --until, -p, -u) is the systemd equivalent of the grep log analysis from lesson 7 — same concept, systemd-specific tools"
    - "Disk space exhaustion from unrotated logs (lesson 7) is the #1 silent killer of production agents — df -h and du -sh are the first diagnostic pair"
    - "The layered network diagnosis (localhost -> port binding -> DNS -> remote) reuses curl and ss from lesson 9 in a structured diagnostic sequence"
  misconceptions:
    - "Students jump to restarting the service instead of reading logs first — emphasize that restarting without understanding the failure means the same crash will happen again"
    - "Students think strace is required for every debugging session — strace is a last resort for when logs reveal nothing; most problems are caught at the log or network layer"
    - "Students confuse df (disk space) with du (directory sizes) — df shows overall filesystem usage, du shows what is consuming space within a specific directory"
  discussion_prompts:
    - "Your agent stopped responding at 3 AM. You have no error alerts configured. Walk through the triage methodology — what is the first command you run, and why?"
    - "How does the structured triage approach compare to 'googling the error message'? When is each strategy appropriate?"
  teaching_tips:
    - "Present the triage methodology as a checklist before teaching any specific tools — students who learn the framework first apply individual commands more effectively"
    - "Create a simulated failure scenario and walk through the triage live — a stopped service, a full disk, or a port conflict makes the methodology concrete"
    - "Connect journalctl filtering back to grep from lesson 7 — same filtering concept (by time, by severity, by service) but using systemd's built-in tools"
    - "Spend most time on logs and disk (most common issues) and less on strace/lsof (advanced, rarely needed for typical agent failures)"
  assessment_quick_check:
    - "Ask: what is the correct triage order? (Expected: logs -> network -> disk -> processes)"
    - "Ask students to write a journalctl command that shows errors from the last hour for a specific service (expected: journalctl -u service-name -p err --since '1 hour ago')"
    - "Ask: df -h shows 95% disk usage. What command do you run next to find what is consuming space? (Expected: du -sh /var/log/* or similar)"

teaching_approach: "Methodology-first (learn the triage framework, then apply it across each diagnostic category)"
modality: "Hands-on diagnosis with AI collaboration"

# Generation metadata
generated_by: "content-implementer v2.0.0"
created: "2026-02-11"
version: "2.0.0"
---

# Debugging & Troubleshooting

Your agent failed. Now what?

In Lesson 10, you deployed `agent_main.py` as a systemd service with restart policies, resource limits, and a health check script. That infrastructure keeps your agent running through routine crashes. But when something genuinely breaks -- a memory leak, a full disk, a network timeout at 3 AM -- automatic restarts won't help. You need to find the root cause.

Production debugging is not about memorizing commands. It is about **systematic diagnosis**: gathering evidence, isolating the problem, and fixing the root cause instead of blindly restarting the service.

By the end of this lesson, you will have a four-phase triage methodology and the specific tools to execute each phase. When your Digital FTE fails, you will know exactly where to look.

---

## Structured Triage Methodology

Before diving into individual tools, learn the system. Every production issue falls into one of four categories, and diagnosing them in the right order saves time:

**Phase 1: Logs** -- What did the agent say before it died?
**Phase 2: Network** -- Can the agent reach its dependencies?
**Phase 3: Disk** -- Is there space for the agent to operate?
**Phase 4: Processes** -- Is the agent consuming resources abnormally?

This order matters. Logs answer "what happened" immediately in 80% of cases. If logs are clean, check network connectivity. If the network is fine, check disk space. If disk is fine, inspect the process itself. Skipping phases or jumping to process debugging first wastes time on symptoms instead of causes.

```
Agent fails → Check logs (journalctl)
                  ↓ logs clean?
              Check network (curl, ss, ping)
                  ↓ network fine?
              Check disk (df, du)
                  ↓ disk fine?
              Check process (ps, strace, lsof)
```

The rest of this lesson teaches the tools for each phase, applied to the `my-agent` service you created in [Lesson 10](10-process-control-systemd.md).

---

## Phase 1: Log Analysis with journalctl

When a systemd service fails, the answer is almost always in the logs. journalctl reads the system journal where systemd captures all stdout and stderr from your service.

### Read Service Logs

Check the current status first:

```bash
sudo systemctl status my-agent
```

**Output (failed service):**
```
● my-agent.service - Sample Digital FTE Agent
     Loaded: loaded (/etc/systemd/system/my-agent.service; enabled; preset: enabled)
     Active: failed (Result: exit-code) since Tue 2026-02-11 14:32:15 UTC; 2min ago
    Process: 12345 ExecStart=/usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000 (code=exited, status=1/FAILURE)
   Main PID: 12345 (code=exited, status=1/FAILURE)
```

Now pull the full logs for this service:

```bash
journalctl -u my-agent
```

This shows every log entry for `my-agent` since the journal began. For a service that has been running for days, this is too much output. Filter it down.

### Filter by Recency

Show only the last 50 lines:

```bash
journalctl -u my-agent -n 50
```

**Output:**
```
Feb 11 14:32:10 server uvicorn[12345]: INFO:     Processing request batch 847
Feb 11 14:32:12 server uvicorn[12345]: WARNING:  Memory usage at 490MB
Feb 11 14:32:14 server python[12345]: MemoryError: Unable to allocate 128MB array
Feb 11 14:32:15 server systemd[1]: my-agent.service: Main process exited, code=exited, status=1/FAILURE
Feb 11 14:32:15 server systemd[1]: my-agent.service: Failed with result 'exit-code'
```

### Follow Logs in Real Time

Watch logs as they appear (like `tail -f` for the journal):

```bash
journalctl -u my-agent -f
```

**Output (live stream):**
```
Feb 11 14:35:00 server uvicorn[12400]: INFO:     192.168.1.5:42386 - "GET /health HTTP/1.1" 200
Feb 11 14:35:05 server uvicorn[12400]: INFO:     Processing request batch 1
Feb 11 14:35:10 server uvicorn[12400]: INFO:     192.168.1.5:42388 - "GET /tasks HTTP/1.1" 200
```

Press `Ctrl+C` to stop following.

### Filter by Priority

Show only errors (skip informational messages):

```bash
journalctl -p err --since "1 hour ago"
```

**Output:**
```
Feb 11 14:32:14 server python[12345]: MemoryError: Unable to allocate 128MB array
Feb 11 14:32:15 server systemd[1]: my-agent.service: Failed with result 'exit-code'
```

Priority levels from most to least severe:

| Level | Name | Meaning |
|-------|------|---------|
| 0 | `emerg` | System is unusable |
| 1 | `alert` | Immediate action required |
| 2 | `crit` | Critical condition |
| 3 | `err` | Error condition |
| 4 | `warning` | Warning condition |
| 5 | `notice` | Normal but significant |
| 6 | `info` | Informational |
| 7 | `debug` | Debug-level detail |

Using `-p err` shows levels 0 through 3 (emerg, alert, crit, err). This cuts through noise fast.

### Filter by Time Range

Show logs from a specific window:

```bash
journalctl -u my-agent --since "2026-02-11 14:00" --until "2026-02-11 15:00"
```

**Output:**
```
Feb 11 14:05:30 server systemd[1]: Started Sample Digital FTE Agent.
Feb 11 14:05:31 server uvicorn[12345]: INFO:     Application startup complete.
Feb 11 14:32:14 server python[12345]: MemoryError: Unable to allocate 128MB array
Feb 11 14:32:15 server systemd[1]: my-agent.service: Failed with result 'exit-code'
```

Combine unit, priority, and time filters for precision:

```bash
journalctl -u my-agent -p err --since "1 hour ago"
```

This gives you only errors from your service in the last hour -- the exact information you need for triage.

### journalctl Quick Reference

| Command | Purpose |
|---------|---------|
| `journalctl -u my-agent` | All logs for the service |
| `journalctl -u my-agent -n 50` | Last 50 lines |
| `journalctl -u my-agent -f` | Follow live output |
| `journalctl -p err --since "1 hour ago"` | Errors from last hour |
| `journalctl -u my-agent --since "2026-02-11 14:00" --until "2026-02-11 15:00"` | Specific time window |
| `journalctl -u my-agent -b` | Since last boot |

### Real-World Scenario: MemoryError Crash

Your agent has been running fine for three days. This morning, it shows `failed` in `systemctl status`. Here is how you diagnose it:

```bash
# Step 1: What happened?
journalctl -u my-agent -p err --since "6 hours ago"
```

**Output:**
```
Feb 11 03:14:22 server python[12345]: MemoryError: Unable to allocate 128MB array
Feb 11 03:14:22 server systemd[1]: my-agent.service: Main process exited, code=exited, status=1/FAILURE
```

The agent crashed at 3:14 AM with a `MemoryError`. Now check whether this is a server-wide RAM issue or a process-specific limit:

```bash
free -h
```

**Output:**
```
              total        used        free      shared  buff/cache   available
Mem:          1.0Gi       780Mi        50Mi        12Mi       170Mi       120Mi
Swap:            0B          0B          0B
```

Only 120 MB available system-wide. Check if the service has a memory limit:

```bash
systemctl show my-agent --property=MemoryMax
```

**Output:**
```
MemoryMax=536870912
```

The service is capped at 512 MB by the `MemoryMax` directive from Lesson 10. The agent tried to allocate beyond that limit. You now have two paths: increase the limit or optimize your agent's memory usage.

---

## Phase 2: Network Diagnosis

If logs show connection errors, timeouts, or "Connection refused" messages, the problem is in the network layer. Diagnose from local to remote -- this builds on the networking foundations from Lesson 9.

### Layer 1: Is the Local Service Responding?

Test whether your agent is listening on its port:

```bash
curl -v localhost:8000/health
```

**Output (working):**
```
*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /health HTTP/1.1
< HTTP/1.1 200 OK
{"status":"healthy","agent":"running","timestamp":"2026-02-11T14:40:01.234567"}
```

**Output (not working):**
```
*   Trying 127.0.0.1:8000...
* connect to 127.0.0.1 port 8000 failed: Connection refused
```

If connection is refused, check whether anything is listening on that port:

```bash
ss -tlnp | grep 8000
```

**Output (listening):**
```
LISTEN   0   128   0.0.0.0:8000   0.0.0.0:*   users:(("uvicorn",pid=12400,fd=7))
```

**Output (not listening):**
```
(no output -- nothing is bound to port 8000)
```

No output means the agent process is not running or is listening on a different port. Go back to Phase 1 and check logs.

### Layer 2: Can You Reach External Hosts?

Test DNS resolution and basic connectivity:

```bash
ping -c 3 api.example.com
```

**Output (working):**
```
PING api.example.com (93.184.216.34): 56 data bytes
64 bytes from 93.184.216.34: icmp_seq=0 ttl=56 time=11.4 ms
64 bytes from 93.184.216.34: icmp_seq=1 ttl=56 time=11.2 ms
64 bytes from 93.184.216.34: icmp_seq=2 ttl=56 time=11.3 ms
```

**Output (DNS failure):**
```
ping: api.example.com: Name or service not known
```

If DNS fails, the problem is name resolution, not the remote server. Check `/etc/resolv.conf` for DNS configuration.

### Layer 3: Can You Reach the Remote Service?

Test HTTP connectivity to an external API your agent depends on:

```bash
curl -o /dev/null -s -w "%{http_code}" https://api.example.com
```

**Output:**
```
200
```

A `200` means the remote service is reachable and responding. Other common codes:

| Code | Meaning | Action |
|------|---------|--------|
| `000` | Connection failed entirely | Check network, DNS, firewall |
| `403` | Forbidden | Check API key or IP allowlist |
| `429` | Rate limited | Back off, check request volume |
| `502/503` | Remote server error | Not your problem -- wait or contact provider |

### Layer 4: Is the Firewall Blocking Traffic?

```bash
sudo ufw status
```

**Output:**
```
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
8000/tcp                   ALLOW       Anywhere
```

If port 8000 is not listed and you need external access, add it:

```bash
sudo ufw allow 8000/tcp
```

### Network Diagnosis Summary

Follow this sequence every time:

```bash
# 1. Is the agent listening locally?
curl -v localhost:8000/health

# 2. Is the port bound?
ss -tlnp | grep 8000

# 3. Can you resolve and reach external hosts?
ping -c 3 api.example.com

# 4. Does HTTP to the remote service work?
curl -o /dev/null -s -w "%{http_code}" https://api.example.com

# 5. Is the firewall blocking?
sudo ufw status
```

If step 1 fails, the problem is local. If steps 1-2 pass but step 3 fails, the problem is DNS or routing. If steps 1-3 pass but step 4 fails, the problem is the remote service or a firewall.

---

## Phase 3: Disk Monitoring

When disk space runs out, services crash with cryptic errors -- "No space left on device," write failures, or silent hangs. Agents that generate logs, cache responses, or store outputs can fill a disk faster than you expect.

### Check Overall Disk Usage

```bash
df -h
```

**Output:**
```
Filesystem      Size  Used Avail Use%  Mounted on
/dev/sda1        20G   18G  1.2G  94%  /
tmpfs           512M     0  512M   0%  /dev/shm
```

If `Use%` is above 90%, you are in the danger zone. Above 95%, services will start failing.

### Find What Is Consuming Space

```bash
du -sh /var/log/* | sort -rh | head -5
```

**Output:**
```
1.2G    /var/log/journal
340M    /var/log/syslog
128M    /var/log/auth.log
45M     /var/log/kern.log
12M     /var/log/dpkg.log
```

The journal is consuming 1.2 GB. For agent-specific directories:

```bash
du -sh /opt/agent/*
```

**Output:**
```
4.0K    /opt/agent/agent_main.py
256M    /opt/agent/cache
890M    /opt/agent/outputs
```

Agent outputs are consuming 890 MB. Clean old outputs or configure automatic rotation.

### Log Rotation with logrotate

Prevent logs from growing indefinitely. Create a logrotate configuration:

```bash
sudo nano /etc/logrotate.d/agent-logs
```

Add this content:

```
/opt/agent/logs/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 nobody nobody
}
```

This rotates logs daily, keeps 7 days of history, and compresses old files. Test without applying:

```bash
sudo logrotate -d /etc/logrotate.d/agent-logs
```

**Output:**
```
reading config file /etc/logrotate.d/agent-logs
considering log /opt/agent/logs/*.log
  log does not need rotating (log is empty)
```

Force an immediate rotation:

```bash
sudo logrotate -f /etc/logrotate.d/agent-logs
```

### Vacuum the System Journal

If `/var/log/journal` is consuming excessive space, limit it:

```bash
sudo journalctl --vacuum-size=500M
```

**Output:**
```
Vacuuming done, freed 724.0M of archived journals from /var/log/journal.
```

---

## Phase 4: Process Debugging

When logs are clean, the network is fine, and disk has space, the problem is inside the process itself. These tools let you inspect what a running agent is actually doing.

### Find the Agent Process

```bash
ps aux | grep agent
```

**Output:**
```
nobody   12400  2.3  5.1 234567 52340 ?   Ss   14:05   0:15 /usr/local/bin/uvicorn agent_main:app --host 0.0.0.0 --port 8000
root     12890  0.0  0.0  12345   672 pts/0 S+  14:45   0:00 grep --color=auto agent
```

The columns that matter: PID (12400), CPU% (2.3), MEM% (5.1), and the command.

### Monitor Resource Consumption

Watch a specific process in real time:

```bash
top -p 12400
```

**Output:**
```
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
12400 nobody    20   0  234567  52340  12456 S   2.3   5.1   0:15.42 uvicorn
```

Press `q` to exit. If `%MEM` keeps climbing over time, you have a memory leak.

### Trace System Calls

`strace` shows every system call a process makes. Attach to a running agent:

```bash
sudo strace -p 12400 -c
```

Let it run for 10-15 seconds, then press `Ctrl+C`:

**Output:**
```
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 45.23    0.004523          15       301           read
 30.11    0.003011          12       251           write
 12.45    0.001245           8       156           recvfrom
  8.33    0.000833           6       139           sendto
  3.88    0.000388           4        97           epoll_wait
------ ----------- ----------- --------- --------- ----------------
100.00    0.010000                   944           total
```

This summary shows where the process spends its time. If `read` or `write` dominates with high error counts, the process may be struggling with file I/O or network connections.

For detailed output (every individual call), use:

```bash
sudo strace -p 12400 -e trace=network 2>&1 | head -20
```

This filters to only network-related system calls -- useful when debugging connection issues.

### List Open Files

`lsof` shows every file and network connection a process has open:

```bash
sudo lsof -p 12400
```

**Output (abbreviated):**
```
COMMAND   PID   USER   FD   TYPE   DEVICE SIZE/OFF    NODE NAME
uvicorn 12400 nobody  cwd    DIR    8,1     4096    1234 /opt/agent
uvicorn 12400 nobody    3u  IPv4  56789      0t0     TCP *:8000 (LISTEN)
uvicorn 12400 nobody    7u  IPv4  56790      0t0     TCP 192.168.1.10:8000->192.168.1.5:42386 (ESTABLISHED)
uvicorn 12400 nobody    9r   REG    8,1   102400    5678 /opt/agent/cache/model.bin
```

This reveals: the process is listening on port 8000, has one active connection, and has a cache file open. If you see hundreds of `ESTABLISHED` connections or too many open files, that indicates a leak.

Count open files for the process:

```bash
sudo lsof -p 12400 | wc -l
```

**Output:**
```
42
```

If this number grows steadily over time, the agent is leaking file descriptors.

---

## Diagnostic Tool Comparison

| Tool | What It Checks | When to Use | Example Output |
|------|----------------|-------------|----------------|
| **journalctl -u** | Systemd service logs | Service crashes or fails to start | `MemoryError: Unable to allocate` |
| **journalctl -f** | Live log stream | Watching agent behavior in real time | Log lines appearing as events occur |
| **curl localhost** | Local HTTP connectivity | Agent not responding to requests | `HTTP/1.1 200 OK` or `Connection refused` |
| **ss -tlnp** | Port binding status | Checking if service is listening | `0.0.0.0:8000 LISTEN` |
| **ping** | DNS and ICMP connectivity | Testing if remote hosts are reachable | `64 bytes from... time=11.4 ms` |
| **df -h** | Disk space usage | Services crashing with write errors | `/dev/sda1 94% /` |
| **du -sh** | Directory sizes | Finding what consumes disk space | `890M /opt/agent/outputs` |
| **ps aux** | Process list and resource usage | Finding process PID and CPU/MEM | `nobody 12400 2.3 5.1 ... uvicorn` |
| **strace -p** | System calls of a running process | Process is stuck or behaving strangely | `45% read, 30% write` |
| **lsof -p** | Open files and connections | Suspected file descriptor leak | `42 open files` |

---

## Exercises

### Exercise 1: Find Error-Level Log Messages

Find all ERROR-level messages from the last hour across all services:

```bash
journalctl -p err --since "1 hour ago" | head -5
```

**Expected output (if errors exist):**
```
Feb 11 14:32:14 server python[12345]: MemoryError: Unable to allocate 128MB array
Feb 11 14:32:15 server systemd[1]: my-agent.service: Failed with result 'exit-code'
```

**Expected output (if no errors):**
```
-- No entries --
```

If you see `-- No entries --`, that means no errors occurred in the last hour. Try extending the range: `--since "24 hours ago"`.

### Exercise 2: Find the Largest Log Files

Check disk usage in `/var/log` and identify the largest files:

```bash
du -sh /var/log/* | sort -rh | head -3
```

**Expected output:**
```
1.2G    /var/log/journal
340M    /var/log/syslog
128M    /var/log/auth.log
```

Your numbers will differ, but the format shows the largest consumers first. If `/var/log/journal` dominates, consider running `sudo journalctl --vacuum-size=500M` to reclaim space.

### Exercise 3: Find All Listening Processes

List every process that is listening for network connections:

```bash
ss -tlnp | grep LISTEN
```

**Expected output:**
```
LISTEN   0   128   0.0.0.0:22      0.0.0.0:*   users:(("sshd",pid=1234,fd=3))
LISTEN   0   128   0.0.0.0:8000    0.0.0.0:*   users:(("uvicorn",pid=12400,fd=7))
```

Verify that your agent (uvicorn on port 8000) appears in the list. If it does not, the service is not running -- check `systemctl status my-agent` and review the logs.

For a comprehensive health check that combines service status, health endpoint, and resource usage, see [Health Check Script](10-process-control-systemd.md#agent-health-checks).

---

## Try With AI

**Ask Claude:** *"My agent service shows 'failed' in systemctl status. Here is the output: [paste your actual systemctl status output]. What's wrong and how do I fix it?"*

**What you're learning:** AI can parse complex error output and suggest targeted fixes faster than reading man pages. Pay attention to how it identifies the specific failure reason from the status output and maps it to a concrete fix.

**Tell Claude:** *"The agent was working yesterday but fails today. Nothing changed in the code. What environmental factors should I check?"* Then systematically verify each suggestion.

**What you're learning:** Debugging requires considering the full environment -- disk space, available memory, network changes, expired certificates, updated dependencies -- not just code. AI generates a checklist of non-obvious environmental factors that experienced sysadmins learn over years.

**Reproduce a common failure** (kill a dependency process or fill up `/tmp`), then work with Claude to diagnose it WITHOUT telling Claude what you did. See if AI's diagnostic process finds the real cause.

**What you're learning:** Testing diagnostic methodology by creating known failures and validating the troubleshooting process. This exercise builds diagnostic confidence -- you know the answer, so you can evaluate whether the triage approach actually works.

:::note Safety Reminder
When debugging on production servers, prefer read-only diagnostic commands (`journalctl`, `df`, `ps`, `ss`) before running anything that modifies state. Never run `strace` on a production process during peak traffic -- it adds overhead to every system call. Use `strace -c` for a summary instead of full tracing. Always check `systemctl status` and logs before restarting a service, so you capture the evidence before it is lost.
:::
