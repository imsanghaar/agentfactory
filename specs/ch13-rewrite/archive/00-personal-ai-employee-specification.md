---
sidebar_position: 0
title: "The Personal AI Employee - Complete Specification"
sidebar_label: "L00: Complete Specification"
description: "Full architectural blueprint for building a Digital FTE - an AI agent that proactively manages your personal and business affairs 24/7 using Claude Code, Obsidian, and MCP."
keywords:
  - Digital FTE
  - Personal AI Employee
  - Claude Code
  - Obsidian
  - MCP
  - Watchers
  - Human-in-the-Loop
  - autonomous agent
chapter: 10
lesson: 0
duration_minutes: 30

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 (Specification) - Complete project requirements before implementation"
layer_1_foundation: "N/A (this IS the foundation document)"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "This lesson IS the capstone specification that all other lessons implement"

# HIDDEN SKILLS METADATA
skills:
  - name: "Digital FTE Architecture"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can explain Perception → Reasoning → Action architecture"
  - name: "Tiered Deliverable Planning"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can identify which tier matches their goals"
  - name: "Specification Reading"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can navigate technical specification to find implementation details"

learning_objectives:
  - objective: "Understand the Digital FTE concept and value proposition"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explain cost savings in Human vs Digital FTE comparison"
  - objective: "Comprehend the Perception → Reasoning → Action architecture"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Diagram the three layers and their components"
  - objective: "Select appropriate achievement tier based on goals and time"
    proficiency_level: "A2"
    bloom_level: "Evaluate"
    assessment_method: "Justify tier selection with specific deliverables"
  - objective: "Navigate specification to find implementation details"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Locate specific patterns (Watcher, HITL, etc.) in spec"

cognitive_load:
  new_concepts: 8
  assessment: "High concept count but this is a REFERENCE document - not meant for single-session mastery. Students return to this throughout the chapter."

differentiation:
  extension_for_advanced: "Read full security section; plan Gold Tier from start"
  remedial_for_struggling: "Focus only on Bronze Tier sections; skip security/error handling until needed"

teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "Chapter Blueprint and Architecture"
  key_points:
    - "Perception-Reasoning-Action architecture is the organizing framework for the entire chapter — every subsequent lesson implements one layer"
    - "Three achievement tiers (Bronze/Silver/Gold) define student commitment levels — students must choose before starting"
    - "Digital FTE cost comparison ($0.50 vs $5.00 per task) is the business case that justifies the entire chapter"
    - "Human-in-the-Loop is a safety pattern, not a limitation — approval files in /Pending_Approval/ prevent dangerous autonomous actions"
  misconceptions:
    - "Students think they need to read the entire spec before starting — this is a REFERENCE document they return to throughout the chapter"
    - "Students confuse 'Digital FTE' with chatbot — emphasize the 24/7 autonomous operation and proactive behavior (Watchers wake it up)"
    - "Students assume Gold Tier is always better — Bronze is a complete, useful product; tiers are about scope not quality"
    - "Students think the AI acts on its own for everything — the permission boundaries table shows most sensitive actions require human approval"
  discussion_prompts:
    - "Looking at the Human FTE vs Digital FTE table, which tasks in YOUR work would benefit most from 24/7 availability?"
    - "The spec says payments over $100 always require approval. Where would YOU draw the line for auto-approve vs require-approval in your domain?"
    - "Why does the architecture use file-based communication (Markdown files in folders) rather than a database or API?"
  teaching_tips:
    - "Start with the CEO Briefing example — it is the most concrete 'aha moment' showing AI as proactive business partner, not reactive chatbot"
    - "Walk through the architecture diagram layer by layer — students should be able to name all three layers and their tools before leaving this lesson"
    - "Have students choose their tier commitment NOW and write it down — this prevents scope confusion in later lessons"
    - "The end-to-end invoice flow walkthrough is the best section for demonstrating how all layers connect"
  assessment_quick_check:
    - "Name the three architecture layers and one tool each layer uses"
    - "Explain in one sentence why Watchers exist (what problem they solve)"
    - "Which tier are you targeting and what are its specific deliverables?"

# Generation metadata
generated_by: "manual creation from hackathon specification"
created: "2026-01-07"
version: "1.0.0"
---

# The Personal AI Employee - Complete Specification

**Your life and business on autopilot. Local-first, agent-driven, human-in-the-loop.**

This document is your complete architectural blueprint for building a "Digital FTE" (Full-Time Equivalent) - an AI agent that proactively manages your personal and business affairs 24/7. You can also think of it as a "Smart Consultant" or General Agent.

This chapter takes the concept of a "Personal AI Employee" to its logical extreme. It doesn't just wait for you to type; it proactively manages your **Personal Affairs** (Gmail, WhatsApp, Bank) and your **Business** (Social Media, Payments, Project Tasks) using **Claude Code** as the reasoning engine and **Obsidian** as the management dashboard.

**Standout Feature**: The "Monday Morning CEO Briefing," where the AI autonomously audits bank transactions and tasks to report revenue and bottlenecks, transforms the AI from a chatbot into a proactive business partner.

---

## Chapter Outcome: Three Achievement Tiers

Choose your target based on your experience and ambition:

### Bronze Tier: Working Email Assistant

**Time Investment**: ~4 hours (Lessons 1-7)

**Deliverables**:

- Obsidian vault with AGENTS.md governance and CLAUDE.md context
- Email skills: drafter, templates, summarizer, orchestrator
- Three email subagents: inbox-triager, response-suggester, follow-up-tracker
- Gmail MCP integration with 19 tools for real email operations
- Folder structure: `.claude/skills/`, `.claude/agents/`

**What You'll Have**: A working email assistant that triages your inbox, drafts professional responses, and sends them on your behalf.

### Silver Tier: Proactive Assistant

**Time Investment**: ~8 hours (Lessons 1-11)

**Deliverables**:

- All Bronze requirements plus:
- Watcher scripts that monitor Gmail and filesystem
- Human-in-the-loop approval workflow for sensitive actions
- Scheduled operations via cron or Task Scheduler
- Weekly Business Audit with CEO Briefing generation

**What You'll Have**: An assistant that wakes up on its own when emails arrive, asks permission before sensitive actions, and gives you a weekly business summary.

### Gold Tier: Autonomous Employee

**Time Investment**: ~12+ hours (Lessons 1-12)

**Deliverables**:

- All Silver requirements plus:
- Cross-domain integration (Email + Files + potentially WhatsApp/Banking)
- Multiple MCP servers for different action types
- Error recovery and graceful degradation
- Comprehensive audit logging
- Full architecture documentation

**What You'll Have**: A Digital FTE that operates 24/7, handles multiple domains, recovers from errors, and maintains audit trails.

---

## Digital FTE: The New Unit of Value

A Digital FTE (Full-Time Equivalent) is an AI agent that is built, "hired," and priced as if it were a human employee. This shifts the conversation from "software licenses" to "headcount budgets."

### Human FTE vs Digital FTE

| Feature       | Human FTE                     | Digital FTE                       |
| ------------- | ----------------------------- | --------------------------------- |
| Availability  | 40 hours / week               | 168 hours / week (24/7)           |
| Monthly Cost  | $4,000 – $8,000+              | $500 – $2,000                     |
| Ramp-up Time  | 3 – 6 Months                  | Instant (via Skills)              |
| Consistency   | Variable (85–95% accuracy)    | Predictable (99%+ consistency)    |
| Scaling       | Linear (Hire 10 for 10x work) | Exponential (Instant duplication) |
| Cost per Task | ~$3.00 – $6.00                | ~$0.25 – $0.50                    |
| Annual Hours  | ~2,000 hours                  | ~8,760 hours                      |

**The 'Aha!' Moment**: A Digital FTE works nearly 9,000 hours a year vs a human's 2,000. The cost per task reduction (from ~$5.00 to ~$0.50) is an **85–90% cost saving** — usually the threshold where a CEO approves a project without further debate.

---

## Architecture: Perception → Reasoning → Action

Your Personal AI Employee has three layers:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PERSONAL AI EMPLOYEE                         │
│                      SYSTEM ARCHITECTURE                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      EXTERNAL SOURCES                           │
├─────────────────┬─────────────────┬─────────────────────────────┤
│     Gmail       │    WhatsApp     │     Bank APIs    │  Files   │
└────────┬────────┴────────┬────────┴─────────┬────────┴────┬─────┘
         │                 │                  │             │
         ▼                 ▼                  ▼             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PERCEPTION LAYER                             │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐             │
│  │ Gmail Watcher│ │WhatsApp Watch│ │ File Watcher │             │
│  │  (Python)    │ │ (Playwright) │ │   (Python)   │             │
│  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘             │
└─────────┼────────────────┼────────────────┼─────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    OBSIDIAN VAULT (Memory)                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ /Needs_Action/  │ /Plans/  │ /Done/  │ /Logs/            │   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │ Dashboard.md    │ Company_Handbook.md │ Business_Goals.md│   │
│  ├──────────────────────────────────────────────────────────┤   │
│  │ /Pending_Approval/  │  /Approved/  │  /Rejected/         │   │
│  └──────────────────────────────────────────────────────────┘   │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                    REASONING LAYER                              │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                      CLAUDE CODE                          │  │
│  │   Read → Think → Plan → Write → Request Approval          │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────────┬────────────────────────────────┘
                                 │
              ┌──────────────────┴───────────────────┐
              ▼                                      ▼
┌────────────────────────────┐    ┌────────────────────────────────┐
│    HUMAN-IN-THE-LOOP       │    │         ACTION LAYER           │
│  ┌──────────────────────┐  │    │  ┌─────────────────────────┐   │
│  │ Review Approval Files│──┼───▶│  │    MCP SERVERS          │   │
│  │ Move to /Approved    │  │    │  │  ┌──────┐ ┌──────────┐  │   │
│  └──────────────────────┘  │    │  │  │Email │ │ Browser  │  │   │
│                            │    │  │  │ MCP  │ │   MCP    │  │   │
└────────────────────────────┘    │  │  └──┬───┘ └────┬─────┘  │   │
                                  │  └─────┼──────────┼────────┘   │
                                  └────────┼──────────┼────────────┘
                                           │          │
                                           ▼          ▼
                                  ┌────────────────────────────────┐
                                  │     EXTERNAL ACTIONS           │
                                  │  Send Email │ Make Payment     │
                                  │  Post Social│ Update Calendar  │
                                  └────────────────────────────────┘
```

### Layer 1: Perception (The "Watchers")

Since Claude Code can't "listen" to the internet 24/7, you use lightweight **Python Sentinel Scripts** running in the background:

- **Gmail Watcher**: Monitors Gmail API for urgent/important messages, saves as `.md` files in `/Needs_Action/`
- **WhatsApp Watcher**: Uses Playwright to monitor WhatsApp Web for keywords like "urgent", "invoice", "payment"
- **File Watcher**: Monitors a drop folder for new files to process

These watchers solve the "lazy agent" problem by waking the agent up rather than waiting for user input.

### Layer 2: Reasoning (Claude Code)

When a Watcher detects a change, it triggers Claude Code:

1. **Read**: Check `/Needs_Action/` and relevant folders
2. **Think**: Analyze what needs to be done
3. **Plan**: Create a `Plan.md` in Obsidian with checkboxes
4. **Write**: Draft responses, create files
5. **Request Approval**: For sensitive actions, create approval request files

### Layer 3: Action (MCP Servers)

Claude uses MCP servers to act on the external world:

| Server       | Capabilities                | Use Case                |
| ------------ | --------------------------- | ----------------------- |
| filesystem   | Read, write, list files     | Built-in, use for vault |
| gmail-mcp    | Send, draft, search emails  | Gmail integration       |
| browser-mcp  | Navigate, click, fill forms | Payment portals         |
| calendar-mcp | Create, update events       | Scheduling              |

---

## Technical Specifications

### 1. Vault Structure

```
ai-vault/
├── .claude/
│   ├── skills/           # Reusable expertise (SKILL.md format)
│   └── agents/           # Autonomous workers
├── Needs_Action/         # Watcher deposits files here
├── Plans/                # Claude creates plans here
├── Pending_Approval/     # Sensitive actions await approval
├── Approved/             # Human moves files here to approve
├── Rejected/             # Human moves files here to reject
├── Done/                 # Completed items archive
├── Logs/                 # Audit trail (JSON)
├── Accounting/           # Financial tracking
├── references/           # Supporting documents
├── Dashboard.md          # Real-time summary
├── Company_Handbook.md   # Rules of engagement
├── Business_Goals.md     # Objectives and metrics
├── CLAUDE.md             # Entry point for Claude Code
└── AGENTS.md             # Governance rules
```

### 2. Watcher Pattern

All Watchers follow this pattern:

| Method                     | Purpose                                            | Output               |
| -------------------------- | -------------------------------------------------- | -------------------- |
| `check_for_updates()`      | Poll external source (Gmail API, filesystem, etc.) | List of new items    |
| `create_action_file(item)` | Convert item to markdown in `/Needs_Action/`       | Path to created file |
| `run()`                    | Infinite loop: check → process → sleep             | Continuous operation |

**Key requirements:**

- Configurable check interval (default: 60 seconds)
- Error handling with logging (never crash silently)
- Output files trigger Claude Code reasoning

_Full implementation provided in L08: Your Employee's Senses_

### 3. Human-in-the-Loop Pattern

For sensitive actions, Claude writes an approval request file instead of acting directly:

```markdown
# /Vault/Pending_Approval/PAYMENT_Client_A_2026-01-07.md

---

type: approval_request
action: payment
amount: 500.00
recipient: Client A
reason: Invoice #1234 payment
created: 2026-01-07T10:30:00Z
expires: 2026-01-08T10:30:00Z
status: pending

---

## Payment Details

- Amount: $500.00
- To: Client A (Bank: XXXX1234)
- Reference: Invoice #1234

## To Approve

Move this file to /Approved folder.

## To Reject

Move this file to /Rejected folder.
```

### 4. Permission Boundaries

| Action Category | Auto-Approve Threshold | Always Require Approval    |
| --------------- | ---------------------- | -------------------------- |
| Email replies   | To known contacts      | New contacts, bulk sends   |
| Payments        | < $50 recurring        | All new payees, > $100     |
| Social media    | Scheduled posts        | Replies, DMs               |
| File operations | Create, read           | Delete, move outside vault |

### 5. Continuous vs Scheduled Operations

| Operation Type    | Example Task                            | Trigger                |
| ----------------- | --------------------------------------- | ---------------------- |
| **Scheduled**     | Daily Briefing at 8:00 AM               | cron / Task Scheduler  |
| **Continuous**    | Watch for "Pricing" keyword in WhatsApp | Python watchdog script |
| **Project-Based** | Categorize 3 months of expenses         | Manual file drop       |

---

## The CEO Briefing (Silver Tier Feature)

The signature feature that transforms AI from chatbot to business partner:

### Trigger

A scheduled task runs every Sunday night.

### Process

Claude Code reads:

1. `Business_Goals.md` - Your objectives and metrics
2. `/Done/` folder - Completed tasks this week
3. `Accounting/` - Bank transactions and revenue

### Deliverable

A "Monday Morning CEO Briefing" highlighting:

- **Revenue**: Total earned this week
- **Bottlenecks**: Tasks that took too long
- **Proactive Suggestions**: "I noticed we spent $200 on unused software subscriptions"

### Template

```markdown
# /Vault/Briefings/2026-01-06_Monday_Briefing.md

---

generated: 2026-01-06T07:00:00Z
period: 2025-12-30 to 2026-01-05

---

# Monday Morning CEO Briefing

## Executive Summary

Strong week with revenue ahead of target. One bottleneck identified.

## Revenue

- **This Week**: $2,450
- **MTD**: $4,500 (45% of $10,000 target)
- **Trend**: On track

## Completed Tasks

- [x] Client A invoice sent and paid
- [x] Project Alpha milestone 2 delivered
- [x] Weekly social media posts scheduled

## Bottlenecks

| Task              | Expected | Actual | Delay   |
| ----------------- | -------- | ------ | ------- |
| Client B proposal | 2 days   | 5 days | +3 days |

## Proactive Suggestions

### Cost Optimization

- **Notion**: No team activity in 45 days. Cost: $15/month.
  - [ACTION] Cancel subscription? Move to /Pending_Approval

### Upcoming Deadlines

- Project Alpha final delivery: Jan 15 (9 days)
- Quarterly tax prep: Jan 31 (25 days)

---

_Generated by Personal AI Employee v1.0_
```

---

## Security & Privacy Requirements

### Credential Management

- Never store credentials in plain text or in your Obsidian vault
- Use environment variables for API keys
- Create a `.env` file (add to `.gitignore` immediately)
- Rotate credentials monthly

### Sandboxing

- **DEV_MODE flag**: Prevents real external actions during development
- **--dry-run flag**: Logs intended actions without executing
- **Rate limiting**: Max 10 emails/hour, max 3 payments/hour

### Audit Logging

Every action must be logged:

```json
{
  "timestamp": "2026-01-07T10:30:00Z",
  "action_type": "email_send",
  "actor": "claude_code",
  "target": "client@example.com",
  "parameters": { "subject": "Invoice #123" },
  "approval_status": "approved",
  "approved_by": "human",
  "result": "success"
}
```

Store logs in `/Vault/Logs/YYYY-MM-DD.json` and retain for minimum 90 days.

---

## Error Handling & Recovery

### Error Categories

| Category       | Examples                        | Recovery Strategy             |
| -------------- | ------------------------------- | ----------------------------- |
| Transient      | Network timeout, API rate limit | Exponential backoff retry     |
| Authentication | Expired token, revoked access   | Alert human, pause operations |
| Logic          | Claude misinterprets message    | Human review queue            |
| Data           | Corrupted file, missing field   | Quarantine + alert            |
| System         | Orchestrator crash, disk full   | Watchdog + auto-restart       |

### Graceful Degradation

- **Gmail API down**: Queue outgoing emails locally, process when restored
- **Banking API timeout**: Never retry payments automatically, always require fresh approval
- **Claude Code unavailable**: Watchers continue collecting, queue grows for later processing

---

## Chapter Roadmap

| Lesson | Title                           | Implements                  | Tier      |
| ------ | ------------------------------- | --------------------------- | --------- |
| L00    | Complete Specification          | This document               | Reference |
| L01    | Your Employee's Memory          | Vault/Memory Layer          | Bronze    |
| L02    | Teaching Your Employee to Write | Skills pattern              | Bronze    |
| L03    | Teaching Professional Formats   | Skills pattern              | Bronze    |
| L04    | Teaching Email Intelligence     | Skills pattern              | Bronze    |
| L05    | Hiring Specialists              | Subagents pattern           | Bronze    |
| L06    | Granting Email Access           | Action Layer (MCP)          | Bronze    |
| L07    | Bronze Capstone                 | Complete email assistant    | Bronze    |
| L08    | Your Employee's Senses          | Perception Layer (Watchers) | Silver    |
| L09    | Trust But Verify                | HITL pattern                | Silver    |
| L10    | Always On Duty                  | Scheduled/Continuous ops    | Silver    |
| L11    | Silver Capstone                 | CEO Briefing                | Silver    |
| L12    | Gold Capstone                   | Full autonomous employee    | Gold      |
| L13    | Chapter Assessment              | Quiz & submission           | —         |

---

## Prerequisites Checklist

Before starting this chapter:

### Required Software

| Component   | Requirement                                             | Purpose                         |
| ----------- | ------------------------------------------------------- | ------------------------------- |
| Claude Code | Active subscription (Pro/Max) or Free Gemini via Router | Primary reasoning engine        |
| Obsidian    | v1.10.6+ (free)                                         | Knowledge base & dashboard      |
| Python      | 3.13 or higher                                          | Watcher scripts & orchestration |
| Node.js     | v24+ LTS                                                | MCP servers                     |
| Git         | Latest stable                                           | Version control                 |

### Hardware Requirements

- Minimum: 8GB RAM, 4-core CPU, 20GB free disk
- For always-on operation: Consider dedicated mini-PC or cloud VM

### Skill Prerequisites

- Completed Chapter 3: Claude Code Features and Workflows
- Comfortable with command-line interfaces
- Familiarity with APIs (what they are, how to call them)

### Pre-Chapter Checklist

Before starting Lesson 1:

- [ ] Install all required software listed above
- [ ] Create a new Obsidian vault named `ai-vault`
- [ ] Verify Claude Code works: `claude --version`
- [ ] Set up a Python project with `uv` or `venv`
- [ ] (Optional) Join the Wednesday Research Meeting for live support

---

## Learning Resources

These resources provide foundational knowledge for building your Personal AI Employee.

### Prerequisites (Before Starting)

| Topic                 | Resource                                                                                                                             | Time    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| AI Native IDEs        | [Chapter 11: AI Native IDEs](/docs/SDD-RI-Fundamentals/ai-native-ides)                                                               | 3 hours |
| Obsidian Fundamentals | [help.obsidian.md/Getting+started](https://help.obsidian.md/Getting+started)                                                         | 30 min  |
| Python File I/O       | [realpython.com/read-write-files-python](https://realpython.com/read-write-files-python/)                                            | 1 hour  |
| MCP Introduction      | [modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction)                                                 | 1 hour  |
| Agent Skills          | [platform.claude.com/docs/agents-and-tools/agent-skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | 2 hours |

### Core Learning (During Chapter)

| Topic                         | Resource                                                                                         | Type     |
| ----------------------------- | ------------------------------------------------------------------------------------------------ | -------- |
| Claude + Obsidian Integration | [youtube.com/watch?v=sCIS05Qt79Y](https://www.youtube.com/watch?v=sCIS05Qt79Y)                   | Video    |
| Building MCP Servers          | [modelcontextprotocol.io/quickstart](https://modelcontextprotocol.io/quickstart)                 | Tutorial |
| Claude Agent Teams            | [youtube.com/watch?v=0J2_YGuNrDo](https://www.youtube.com/watch?v=0J2_YGuNrDo)                   | Video    |
| Gmail API Setup               | [developers.google.com/gmail/api/quickstart](https://developers.google.com/gmail/api/quickstart) | Docs     |
| Playwright Automation         | [playwright.dev/python/docs/intro](https://playwright.dev/python/docs/intro)                     | Docs     |

### Deep Dives (After Chapter)

- **MCP Server Development**: [github.com/anthropics/mcp-servers](https://github.com/anthropics/mcp-servers)
- **Production Automation**: "Automate the Boring Stuff with Python" (free online)
- **Security Best Practices**: OWASP API Security Top 10

---

## Process Management: Why Watchers Need Supervision

Your Watchers (Gmail, File monitors) are **daemon processes** — designed to run indefinitely. But standard Python scripts are fragile:

- They terminate when your terminal closes
- They crash on unhandled exceptions (API timeouts, network blips)
- They don't auto-recover after system reboot

**The Solution**: A process manager (PM2, supervisord, or systemd) that:

- **Auto-restarts** crashed processes immediately
- **Persists across reboots** via OS init system hooks
- **Captures logs** for debugging silent failures

**Quick Setup** (covered in L10):

```bash
# Install PM2
npm install -g pm2

# Start watcher with auto-restart
pm2 start gmail_watcher.py --interpreter python3

# Persist across reboots
pm2 save && pm2 startup
```

---

## Troubleshooting FAQ

### Setup Issues

**Q: Claude Code says "command not found"**
A: Ensure Claude Code is installed globally and your PATH is configured. Run `npm install -g @anthropic/claude-code`, then restart your terminal.

**Q: Obsidian vault isn't being read by Claude**
A: Run Claude Code from the vault directory, or use `--cwd /path/to/vault`. Verify file permissions allow read access.

**Q: Gmail API returns 403 Forbidden**
A: Your OAuth consent screen may need verification, or you haven't enabled the Gmail API in Google Cloud Console.

### Runtime Issues

**Q: Watcher scripts stop running overnight**
A: Use PM2 or supervisord to keep them alive (see L10: Always On Duty).

**Q: Claude is making incorrect decisions**
A: Review your `Company_Handbook.md` rules. Add more specific examples. Lower autonomy thresholds so more actions require approval.

**Q: MCP server won't connect**
A: Check the server process is running (`ps aux | grep mcp`). Verify paths in `mcp.json` are absolute.

### Security Concerns

**Q: How do I know my credentials are safe?**
A: Never commit `.env` files. Use environment variables. Rotate credentials monthly. Implement audit logging.

**Q: What if Claude tries to pay the wrong person?**
A: That's why HITL is critical for payments. Any payment action creates an approval file first. Never auto-approve payments to new recipients.

---

## Example: End-to-End Invoice Flow

This walkthrough demonstrates a complete flow from trigger to action.

### Scenario

A client sends a WhatsApp message asking for an invoice. The AI Employee should: (1) detect the request, (2) generate the invoice, (3) send it via email, and (4) log the transaction.

### Step 1: Detection (WhatsApp Watcher)

```
# Detected message:
# From: Client A
# Text: "Hey, can you send me the invoice for January?"

# Watcher creates:
# /Vault/Needs_Action/WHATSAPP_client_a_2026-01-07.md
```

### Step 2: Reasoning (Claude Code)

```markdown
# Claude creates: /Vault/Plans/PLAN_invoice_client_a.md

---

created: 2026-01-07T10:30:00Z
status: pending_approval

---

## Objective

Generate and send January invoice to Client A

## Steps

- [x] Identify client: Client A (client_a@email.com)
- [x] Calculate amount: $1,500 (from /Accounting/Rates.md)
- [ ] Generate invoice PDF
- [ ] Send via email (REQUIRES APPROVAL)
- [ ] Log transaction
```

### Step 3: Approval (Human-in-the-Loop)

Claude creates approval request. You review and move to `/Approved/`.

### Step 4: Action (Email MCP)

The system detects the approved file and sends the email with invoice attached.

### Step 5: Completion

Files move to `/Done/`, Dashboard updated, transaction logged.

---

## Ethics & Responsible Automation

### When Should AI NOT Act Autonomously?

- Emotional contexts: Condolence messages, conflict resolution
- Legal matters: Contract signing, regulatory filings
- Medical decisions: Health-related actions
- Financial edge cases: Unusual transactions, large amounts
- Irreversible actions: Anything that cannot be undone

### Transparency Principles

- Disclose AI involvement when appropriate
- Maintain audit trails for all actions
- Allow contacts to request human-only communication
- Schedule regular reviews of AI decisions

### The Human Remains Accountable

You are responsible for your AI Employee's actions. Regular oversight isn't optional:

- **Daily**: 2-minute dashboard check
- **Weekly**: 15-minute action log review
- **Monthly**: 1-hour comprehensive audit

---

## Try With AI

**Prompt 1: Understand the Architecture**

```
I just read the Personal AI Employee specification. Explain the Perception → Reasoning → Action architecture in your own words. What role does each layer play?
```

**What you're practicing**: Confirming you understand the core architecture before building.

**Prompt 2: Choose Your Tier**

```
Based on my goals of [describe your goals] and available time of [X hours/week], which tier (Bronze/Silver/Gold) should I target? What specific deliverables will I have?
```

**What you're practicing**: Making an informed decision about scope before starting.

**Prompt 3: Map Your Use Case**

```
I want to use this Personal AI Employee for [your domain - e.g., freelance consulting, real estate, content creation]. What would the equivalent of the "Email Assistant" be for my domain? What watchers, skills, and MCP integrations would I need?
```

**What you're practicing**: Translating the email example to your specific domain.
