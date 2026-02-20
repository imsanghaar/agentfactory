---
sidebar_position: 7
title: "Connecting Google Workspace"
description: "Connect your AI Employee to Gmail, Calendar, and Drive using gog, experience the moment your agent processes real email, and confront the security implications of OAuth access"
keywords:
  [
    google workspace,
    gmail,
    calendar,
    drive,
    gog,
    oauth,
    agent productivity,
    openclaw integration,
    real work,
  ]
chapter: 7
lesson: 7
duration_minutes: 35

# HIDDEN SKILLS METADATA
skills:
  - name: "OAuth Integration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can set up GCP OAuth credentials and connect their Google account to OpenClaw via gog"

  - name: "Productivity Integration"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can delegate Gmail, Calendar, and Drive tasks to their AI Employee and receive results via Telegram"

  - name: "Security Risk Assessment (Applied)"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can evaluate the security implications of granting OAuth access to an AI agent and apply the lethal trifecta framework to their own setup"

learning_objectives:
  - objective: "Install gog and connect your Google account to OpenClaw with appropriate OAuth scopes"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student successfully runs gog auth list and sees their connected account with configured services"

  - objective: "Delegate real Gmail, Calendar, and Drive tasks to your AI Employee"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student sends 3 Telegram messages that trigger real Google Workspace operations and receives useful results"

  - objective: "Evaluate the security implications of granting OAuth access to an AI agent"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student can explain how OAuth access makes the lethal trifecta from L05 concrete and identify which scopes are truly necessary"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (gog CLI, OAuth credential flow, Google Workspace integration, applied security assessment) -- within B1 range. OAuth setup is procedural, not conceptual, reducing cognitive load despite many steps."

differentiation:
  extension_for_advanced: "Set up Gmail Pub/Sub push notifications so your agent proactively summarizes new emails as they arrive, without you asking. This combines autonomous invocation (L03 Task 6) with Google Workspace access."
  remedial_for_struggling: "Focus on Gmail only. Skip Calendar, Drive, and advanced features. The key experience is: your agent reads YOUR email. That single moment is the lesson."

teaching_guide:
  lesson_type: "hands-on"
  session_group: 3
  session_title: "Connecting Real Productivity Tools"
  key_points:
    - "The moment the agent reads real email is the emotional turning point of the chapter — it transforms 'AI Employee' from metaphor to reality; make sure students pause and register this"
    - "Least privilege (granting minimum OAuth scopes) is the practical application of Lesson 5's security checklist on their own real account"
    - "The lethal trifecta table (before gog vs after gog) makes the abstract framework from Lesson 5 concrete — all three conditions are now met on the student's actual data"
    - "OAuth integration pattern (register credentials, authorize, scope permissions) is universal across every SaaS tool; students will repeat this pattern with Slack, GitHub, Notion, and Jira"
  misconceptions:
    - "Students think OAuth setup is a one-time formality — emphasize that the scopes they granted determine what their agent can do with their real data, including sending emails as them"
    - "Students assume read-only access is safe — even read-only Gmail access means the agent (and any malicious skill) can see every email, including password resets and financial statements"
    - "Students conflate the Google Cloud Console complexity with the actual integration — the OAuth setup is a one-time hurdle; daily use is just Telegram messages"
    - "Students think they need all six gog services from the start — least privilege means starting with only what you need and adding incrementally"
  discussion_prompts:
    - "Now that your agent can read your email, how does your threat model change? What is the worst realistic thing a malicious skill could do with Gmail access?"
    - "If you were advising a colleague to connect their AI Employee to Google Workspace, what three things would you warn them about first?"
    - "The lesson says tool access is what makes the employee label accurate. Do you agree? What else might be needed?"
  teaching_tips:
    - "If teaching in a classroom, have students use a dedicated test Google account rather than their primary one — this removes security anxiety and lets them experiment freely"
    - "The OAuth credential setup in GCP Console is the biggest friction point — consider doing this step as a live walkthrough with the class to prevent 15 minutes of individual troubleshooting"
    - "After Task 1 (email summary), pause the class and ask students to describe what they felt — the emotional response to an AI reading real email is the strongest retention anchor in the chapter"
    - "Use the before/after gog table as a whiteboard exercise: have students fill in what changes in each lethal trifecta dimension when you add Google Workspace access"
  assessment_quick_check:
    - "Ask students to explain least privilege in one sentence and give an example using gog scope flags"
    - "Have students describe how the lethal trifecta from Lesson 5 applies specifically to their gog setup"
    - "Ask: What is the gog command to limit your agent to only Gmail and Calendar access?"
---

# Connecting Google Workspace

In Lesson 6, you connected your AI Employee to a coding agent so it can delegate programming tasks to a specialist. Now you will cross the line that separates a demo from daily use: connecting your agent to your actual productivity tools.

Until now, every task you gave your AI Employee operated on information it generated itself -- competitor research from training data, goal files it created, reports it wrote. Useful, but self-contained. Your agent has been working in a sandbox of its own making.

This lesson breaks that sandbox. When it reads your real inbox, summarizes your actual calendar, and finds the document you were editing last week, the sandbox disappears. That is when a tutorial becomes something you want to open every morning.

This is the capability that drove 209,000 people to star OpenClaw. Not the chat interface. Not the agent loop. The moment your agent handles your real work -- your email, your schedule, your files -- is when "AI Employee" stops being a metaphor.

## What gog Connects

gog is a command-line tool that bridges OpenClaw and Google Workspace. One OAuth setup gives your AI Employee access to six Google services through a unified CLI:

| Service      | What Your Agent Can Do                                                   |
| ------------ | ------------------------------------------------------------------------ |
| **Gmail**    | Search messages, read threads, send mail, manage labels, handle drafts   |
| **Calendar** | List events, create meetings, check availability, respond to invitations |
| **Drive**    | Search files, upload and download documents, manage permissions          |
| **Contacts** | List and search your contact directory                                   |
| **Sheets**   | Read cells, update values, append rows, access metadata                  |
| **Docs**     | Export documents, display content as text                                |

Your agent accesses all six through subcommands: `gog gmail`, `gog calendar`, `gog drive`, and so on. Every command supports JSON output for scripting, which is how OpenClaw parses the results into natural language responses.

## Setting Up gog

:::tip Google Cloud Console Feeling Overwhelming?
The OAuth credential setup below is a one-time process. If you get stuck on any step, ask your AI Employee (via Telegram or TUI): "Help me set up Google Cloud OAuth credentials for a desktop app called gog." It can walk you through each screen. You can also skip this lesson entirely and return when you need Google Workspace access -- Lessons 1-6 work without it.
:::

The setup has three parts: install the CLI, register your Google OAuth credentials, and authorize your account.

### Part 1: Install gog

:::tip Selected gog During Setup?
If you chose `gog` from the skills picker during QuickStart in Lesson 2, it may already be installed. Run `gog --version` to check. If it works, skip to Part 2.
:::

**macOS (Homebrew):**

```bash
brew install steipete/tap/gogcli
```

**Output:**

```
==> Fetching steipete/tap/gogcli
==> Downloading https://github.com/steipete/gogcli/releases/...
==> Installing gogcli from steipete/tap
==> Summary
🍺  /opt/homebrew/Cellar/gogcli/...
```

Verify the installation:

```bash
gog --version
```

**Output:**

```
gog version 0.x.x (or similar version string)
```

**Linux (Arch):**

```bash
yay -S gogcli
```

**Linux (other distributions):** Build from source:

```bash
git clone https://github.com/steipete/gogcli.git
cd gogcli && make
./bin/gog --version
```

**Note:** gog requires a working Go toolchain for building from source. On macOS, Homebrew handles this automatically. On Linux, the Homebrew path also works if you have Linuxbrew installed. Check the [gog documentation](https://gogcli.sh/) for the latest installation options.

### Part 2: Create and Register OAuth Credentials

gog needs a Google Cloud OAuth client to authenticate. This is a one-time setup.

**Step 1:** Go to [console.cloud.google.com](https://console.cloud.google.com) and sign in with the Google account you want your agent to access.

**Step 2:** Create a project (or select an existing one). The project name does not matter -- something like "AI Employee" works fine.

**Step 3:** Enable the APIs your agent will use. Navigate to **APIs & Services > Library** and enable:

- Gmail API
- Google Calendar API
- Google Drive API

These are the three you will use in this lesson. You can enable Contacts API, Sheets API, and Docs API later if needed.

**Step 4:** Configure the OAuth consent screen. Go to **APIs & Services > OAuth consent screen**:

- Choose **External** (unless you have a Google Workspace organization)
- Fill in the required fields (app name, support email)
- Add your email as a test user

**Step 5:** Create credentials. Go to **APIs & Services > Credentials**:

- Click **Create Credentials > OAuth client ID**
- Application type: **Desktop app**
- Name it anything ("gog CLI" works)
- Click **Create**, then **Download JSON**

This downloads a file named something like `client_secret_123456.json`. Save it somewhere you can find it.

**Step 6:** Register the credentials with gog:

```bash
gog auth credentials ~/Downloads/client_secret_*.json
```

**Output:**

```
Credentials stored successfully.
```

### Part 3: Authorize Your Account

```bash
gog auth add you@gmail.com
```

Replace `you@gmail.com` with your actual email address. This opens your browser for the standard Google OAuth flow -- review the permissions and click **Allow**.

**Output:**

```
Authorization complete. Token stored securely.
```

By default, gog requests access to Gmail, Calendar, Drive, Contacts, Sheets, and Docs. If you want to limit scope to specific services:

```bash
gog auth add you@gmail.com --services gmail,calendar,drive
```

Set your default account so you do not need to specify it every time:

```bash
export GOG_ACCOUNT=you@gmail.com
```

Add that line to your shell profile (`~/.zshrc` or `~/.bashrc`) to make it permanent.

### Verify Everything Works

```bash
gog auth list
```

**Output:**

```
Account              Services                              Default
you@gmail.com        gmail,calendar,drive,contacts,...      ✓
```

Quick test -- list your Gmail labels:

```bash
gog gmail labels list
```

**Output:**

```
Name              ID                    Type
INBOX             INBOX                 system
SENT              SENT                  system
DRAFT             DRAFT                 system
...
```

If you see your labels, the connection works. Your agent can now access your Google Workspace.

## Real Employee Tasks

Open your Telegram chat with your AI Employee. These tasks use your actual data -- not practice exercises.

### Task 1: Email Summary (Gmail)

**What to type:**

```
Summarize my top 5 unread emails. For each, give me the sender,
subject, and a one-sentence summary of what they want.
```

**What to observe:** Your agent calls `gog gmail search 'is:unread' --max 5`, reads the thread content, and produces a structured summary. The data flowing through is your real inbox -- names you recognize, subjects you have been ignoring, requests that actually need your attention.

This is the moment. Not a demo email. Not sample data. Your actual unread messages, summarized by your agent, delivered to your phone.

**What the agent loop looks like here:**

| Phase       | What Happens                                                                         |
| ----------- | ------------------------------------------------------------------------------------ |
| **Parse**   | Agent understands "top 5 unread" means Gmail search with `is:unread` filter, limit 5 |
| **Plan**    | Search inbox, read each thread, extract sender/subject/intent, format as list        |
| **Execute** | Calls `gog gmail search`, reads results, synthesizes summaries                       |
| **Report**  | Delivers formatted summary to Telegram                                               |

### Task 2: Calendar Check (Calendar)

**What to type:**

```
What meetings do I have tomorrow? Include the time, title, and
who else is attending.
```

**What to observe:** The agent calls `gog calendar list-events` with tomorrow's date range and formats the results. If you have a packed schedule, you see it laid out clearly. If tomorrow is empty, the agent tells you that too -- which is itself useful information.

Notice how the agent handles time zones. It uses whatever your calendar is configured for. If an event spans multiple time zones (a meeting with overseas colleagues), the agent shows the time in your local zone.

### Task 3: File Search (Drive)

**What to type:**

```
Find the document I was working on most recently that has "budget"
or "proposal" in the name. Show me the title, last modified date,
and a link to open it.
```

**What to observe:** The agent searches Drive with query filters, finds matching files, and returns direct links you can tap to open the document. It accessed your actual Google Drive -- the same files you see when you open drive.google.com.

### What Just Happened

You delegated three tasks that would normally require you to open three different apps (Gmail, Calendar, Drive), navigate their interfaces, and manually compile the information. Your agent did all three from a single chat window on your phone.

The agent loop you learned in Lesson 3 -- parse, plan, execute, report -- is now operating on your real data. The same four phases. The same execution engine. But instead of generating practice files, it is reading your actual inbox, checking your actual calendar, and searching your actual Drive.

## The Security Reality

Stop and consider what you just did. You granted your AI Employee OAuth access to your Google account. Look at what that means through the lens of the lethal trifecta from Lesson 5:

| Component                  | Before gog                          | After gog                                                              |
| -------------------------- | ----------------------------------- | ---------------------------------------------------------------------- |
| **Private data access**    | Agent reads files it created itself | Agent reads your email, calendar, contacts, documents                  |
| **Untrusted content**      | Your typed messages only            | Incoming emails, shared documents, calendar invitations from anyone    |
| **External communication** | Agent writes files locally          | Agent can send emails, create calendar events, modify shared documents |

Every security rule from Lesson 5 applies with higher stakes now. The lethal trifecta is no longer theoretical -- it is operating on your actual data.

### Scope Awareness

gog requests broad access by default. Ask yourself which services your agent actually needs:

| If your agent only needs to... | Then limit scope to...                       |
| ------------------------------ | -------------------------------------------- |
| Summarize unread emails        | `--services gmail` (read-only)               |
| Check tomorrow's schedule      | `--services calendar` (read-only)            |
| Find recent documents          | `--services drive` (read-only)               |
| All of the above               | `--services gmail,calendar,drive`            |
| Send emails on your behalf     | Gmail with send scope -- **think carefully** |

The principle is least privilege: grant only the access your agent needs for the tasks you actually delegate. You can always add more services later with `gog auth add --services` and `--force-consent`.

### What Could Go Wrong

A malicious skill (remember ClawHavoc from Lesson 5) with gog access could:

- Read your email and extract sensitive information
- Send emails from your account without your knowledge
- Access confidential documents in your Drive
- Exfiltrate contacts to an external server

This is why Lesson 5 came before this lesson. The security checklist you learned -- read skills before installing, never bind to 0.0.0.0, enable authentication -- is not abstract best practice. It is the difference between a useful employee and a compromised account.

## What Transfers

**OAuth integration is universal.** Every productivity tool your agent will access -- Slack, GitHub, Notion, Jira -- uses the same pattern: register credentials, authorize access, scope permissions.

**Least privilege is architectural.** Granting minimum necessary access is not just a security rule for gog. It is a design principle for every agent integration you build.

**The employee threshold is tool access.** Intelligence alone does not make an agent an employee. The agent loop (Lesson 3) gives it capability. Skills (Lesson 5) give it expertise. But tool access -- connecting to the systems where your actual work lives -- is what makes the "employee" label accurate. An employee who cannot access your email, calendar, or files is not really working for you.

## Try With AI

### Prompt 1: Design a Daily Briefing

**Setup:** Use your AI Employee on Telegram or Claude Code.

```
Design a daily morning briefing for my AI Employee that combines
Gmail (unread, prioritized), Calendar (today's meetings with prep
notes), and Drive (recently modified docs). Output as a single
2-minute read with "requires action" and "FYI" sections.
My role: [YOUR ROLE]
```

**What you're learning:** Workflow composition -- combining multiple data sources into a single actionable output. This is the foundation of autonomous invocation from Lesson 3, Task 6. A morning briefing that runs on a schedule is what transforms your agent from "tool I use" to "employee that works while I sleep."

### Prompt 2: Push Notification Pipeline (Advanced Design)

**Setup:** Use Claude Code or your preferred AI assistant.

```
Design the architecture for a Gmail push notification pipeline:
detect important emails, summarize them, send to my Telegram.
I know it involves Google Pub/Sub. Give me component architecture
and data flow with an ASCII diagram, not a full implementation.
```

**What you're learning:** Event-driven agent architecture. Most agent interactions are pull-based (you ask, it answers). Push-based agents that react to external events represent the next level of autonomy. Understanding this architecture prepares you for building proactive agents.

### Prompt 3: Security Audit Your Own Setup

**Setup:** Use Claude Code or your AI Employee.

```
I just connected my AI Employee to Google Workspace via gog with
OAuth access to Gmail, Calendar, and Drive. Audit my setup: worst
realistic attack scenario, which services I actually need, and the
exact gog command to reduce scope to the minimum.
```

**What you're learning:** Applied security auditing on your own infrastructure. This is the lethal trifecta from Lesson 5 made concrete -- you are evaluating real OAuth scopes on your real account, not a hypothetical scenario. The habit of auditing your own setup after connecting new services is what separates secure deployments from vulnerable ones.

**Safety Note:** The OAuth credentials you created grant real access to your Google account. Do not share your `client_secret.json` file, your gog auth tokens, or screenshots showing your email content. If you are working through this lesson in a shared environment, consider using a dedicated test Google account rather than your primary one.
