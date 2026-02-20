---
title: "Summary: Your Employee's Senses"
sidebar_label: "Summary"
sidebar_position: 8.5
---

# Lesson 8 Summary: Your Employee's Senses

## Key Concepts

1. **The Perception Gap**: Without watchers, your employee only acts when explicitly asked — watchers add a perception layer that makes it proactive

2. **Watcher Pattern**: Check for updates → Process new items → Deposit results — the universal pattern for all event monitoring

3. **watchdog Library**: Python library for filesystem event monitoring; `FileSystemEventHandler` with `on_created` callback detects new files in watched directories

4. **Action File Generation**: Watchers create markdown files with YAML frontmatter metadata that trigger downstream processing by Claude Code

5. **Gmail Watcher Architecture**: Shown as a design pattern (full implementation in Hackathon) — polls Gmail API via MCP, creates action files for new emails

## Deliverables

- Working Python filesystem watcher using `watchdog` library
- `InboxHandler` class monitoring `/Inbox/` for new files
- Action files generated in `/Actions/` with metadata
- Understanding of Gmail watcher architecture for Hackathon tier

## Key Code Snippets

### Watcher Installation

```bash
pip install watchdog
```

### Core Pattern

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class InboxHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Process new file, create action file
```

## Skills Practiced

| Skill                        | Proficiency | Assessment                                      |
| ---------------------------- | ----------- | ----------------------------------------------- |
| Filesystem Event Monitoring  | A2          | Use watchdog to detect file creation            |
| Action File Generation       | B1          | Create markdown action files with YAML metadata |
| Watcher Pattern Design       | B1          | Explain check-process-deposit pattern           |
| Background Process Operation | A2          | Run watcher as background process               |

## Duration

30 minutes

## Next Lesson

[Lesson 9: Trust But Verify](./09-trust-but-verify.md) - Implement Human-in-the-Loop approval workflows
