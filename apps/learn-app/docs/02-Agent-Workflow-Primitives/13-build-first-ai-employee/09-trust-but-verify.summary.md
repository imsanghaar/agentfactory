---
title: "Summary: Trust But Verify"
sidebar_label: "Summary"
sidebar_position: 9.5
---

# Lesson 9 Summary: Trust But Verify

## Key Concepts

1. **The Trust Spectrum**: Actions range from full autonomy (reading files) to full human control (financial transactions) — your employee needs clear boundaries

2. **Permission Boundaries**: Three zones — auto-approve (read, draft, organize), require-approval (send emails, schedule meetings), never-auto (financial, delete, share credentials)

3. **Folder-Based Approval Workflow**: `/Pending_Approval/` → human moves to `/Approved/` or `/Rejected/` → watcher processes result → `/Done/`

4. **Approval Request Format**: YAML-frontmatter files with action type, urgency, proposed action, draft content, and clear approve/reject instructions

5. **Approval Watcher**: Python script monitoring `/Approved/` folder, executes the approved action, moves completed requests to `/Done/`

## Deliverables

- Permission boundaries document defining auto-approve vs require-approval thresholds
- Folder structure: `/Pending_Approval/`, `/Approved/`, `/Rejected/`, `/Done/`
- Approval request template with YAML frontmatter
- Working approval watcher script
- Tested full cycle: create request → approve → verify execution → test rejection

## Key Code Snippets

### Approval Request Template

```markdown
---
action: send-email
urgency: normal
created: 2025-01-15
---

## Proposed Action

Send follow-up email to client

## To Approve

Move this file to /Approved/

## To Reject

Move this file to /Rejected/
```

## Skills Practiced

| Skill                      | Proficiency | Assessment                                         |
| -------------------------- | ----------- | -------------------------------------------------- |
| Permission Boundary Design | B1          | Define auto-approve vs require-approval thresholds |
| Approval Request Format    | A2          | Create YAML-frontmatter approval files             |
| Folder-Based Workflow      | A2          | Implement Pending → Approved/Rejected → Done       |
| Approval Watcher Script    | B1          | Build and test Python approval watcher             |

## Duration

30 minutes

## Next Lesson

[Lesson 10: Always On Duty](./10-always-on-duty.md) - Configure 24/7 operation with PM2, cron, and Stop hooks
