---
title: "Summary: Always On Duty"
sidebar_label: "Summary"
sidebar_position: 10.5
---

# Lesson 10 Summary: Always On Duty

## Key Concepts

1. **Three Operation Modes**: PM2 for continuous processes (watchers), cron for scheduled tasks (reports), Stop hooks for persistent multi-step work

2. **PM2 Process Management**: Start processes with auto-restart on crash, persist across reboots with `pm2 startup` + `pm2 save`, monitor with `pm2 monit`

3. **Cron Scheduling**: Five-field syntax (`minute hour day month weekday`), use `crontab -e` to schedule recurring tasks like weekly briefings

4. **Task Persistence Loop**: Claude Code Stop hook pattern — exit code 2 means "I'm not done yet, keep going", enabling multi-step autonomous work sessions

5. **Graceful Degradation**: When services are unavailable, log the error and continue with available data rather than crashing the entire pipeline

## Deliverables

- Watcher running under PM2 with auto-restart and boot persistence
- Cron job scheduling weekly CEO Briefing generation
- Stop hook configuration in `.claude/settings.json`
- Understanding of graceful degradation patterns

## Key Code Snippets

### PM2 Commands

```bash
pm2 start inbox_watcher.py --name inbox-watcher
pm2 startup    # Generate boot script
pm2 save       # Save current process list
pm2 monit      # Real-time monitoring
```

### Cron Expression

```bash
# Every Monday at 7:00 AM
0 7 * * 1 cd ~/Employee_Vault && claude -p "Run /ceo-briefing"
```

## Skills Practiced

| Skill                  | Proficiency | Assessment                               |
| ---------------------- | ----------- | ---------------------------------------- |
| PM2 Process Management | A2          | Start, monitor, persist processes        |
| Cron Scheduling        | A2          | Write cron expressions, verify execution |
| Claude Code Stop Hook  | B1          | Implement exit-code-2 persistence        |
| Graceful Degradation   | A2          | Explain fallback patterns                |

## Duration

30 minutes

## Next Lesson

[Lesson 11: Silver Capstone - CEO Briefing](./11-silver-capstone-ceo-briefing.md) - Build autonomous weekly business audit
