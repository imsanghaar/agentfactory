### Core Concept
**Production debugging is not about memorizing commands — it is about systematic diagnosis: gathering evidence in the right order, isolating the problem layer, and fixing the root cause instead of blindly restarting the service.** When your Digital FTE fails at 3 AM, a structured triage methodology tells you exactly where to look.

### Key Mental Models
- **Four-Phase Triage Order**: Logs → Network → Disk → Processes. This sequence matters because logs answer "what happened" in 80% of cases. Only move to the next phase when the current one is clean. Skipping phases wastes time on symptoms instead of causes.
- **Local-to-Remote Network Diagnosis**: Test in layers — can the agent respond locally? Is the port bound? Can you resolve DNS? Can you reach the remote service? Each layer isolates a different failure point.
- **Evidence Before Action**: Collect diagnostic data at each phase before attempting a fix. Restarting a service without reading logs means you'll face the same failure again.

### Critical Patterns
- **journalctl filtering**: `-u service` for unit logs, `-f` for live streaming, `-p err` for errors only, `--since`/`--until` for time ranges.
- **Network layer testing**: `curl -v localhost:8000/health` tests local response, `ss -tlnp` checks port binding, `ping` tests DNS, `ufw status` checks firewall.
- **Disk monitoring**: `df -h` shows overall usage (danger above 90%), `du -sh /path/*` finds largest consumers.
- **Process debugging**: `strace -p PID` traces system calls, `lsof -p PID` shows open files and sockets.

### Common Mistakes
- **Blindly restarting without reading logs**: The most common reaction and the least effective. The same failure returns if you don't address the root cause.
- **Jumping to process debugging first**: Checking strace and lsof before reading logs wastes time. Logs explain the failure directly in 80% of cases.
- **Ignoring disk space**: Full disks cause cryptic errors — "write failed," silent hangs, or service crashes. Check `df -h` early in triage, especially for services that generate logs or cache data.
