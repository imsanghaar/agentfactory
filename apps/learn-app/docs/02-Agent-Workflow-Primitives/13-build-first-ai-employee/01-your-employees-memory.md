---
sidebar_position: 1
title: "Your Employee's Memory"
sidebar_label: "L01: Your Employee's Memory"
description: "Set up your Personal AI Employee's memory system. Obsidian vault with AGENTS.md governance, CLAUDE.md context, and Claude Code as your operator."
keywords:
  - Obsidian vault
  - Claude Code
  - General Agent
  - AGENTS.md
  - CLAUDE.md
  - professional workspace
chapter: 10
lesson: 1
duration_minutes: 25

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation) - Setting up General Agent workspace"
layer_1_foundation: "Installing Obsidian, creating AGENTS.md, CLAUDE.md, testing with Claude Code"
layer_2_collaboration: "N/A (foundation setup)"
layer_3_intelligence: "N/A (foundation setup)"
layer_4_capstone: "N/A (foundation setup)"

# HIDDEN SKILLS METADATA
skills:
  - name: "Obsidian Vault Setup"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create Obsidian vault with governance files"
  - name: "AGENTS.md Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can create AGENTS.md with skill and agent formats"
  - name: "Claude Code Context Verification"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can verify Claude Code reads vault context"

learning_objectives:
  - objective: "Create Obsidian vault as professional workspace"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successfully create new Obsidian vault"
  - objective: "Write AGENTS.md with governance rules and formats"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "AGENTS.md contains skill and agent format specifications"
  - objective: "Create CLAUDE.md that references AGENTS.md"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "CLAUDE.md exists and references @AGENTS.md"
  - objective: "Verify Claude Code picks up vault context"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Claude Code responds with vault-specific knowledge"
  - objective: "Enable hidden files visibility in Obsidian"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Can see .claude folder in Obsidian"
  - objective: "Configure Obsidian MCP for vault access from any directory"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Claude Code can read vault notes via MCP from outside the vault"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (Obsidian vault, AGENTS.md, CLAUDE.md, hidden files plugin, Obsidian MCP) - within A2 limit"

differentiation:
  extension_for_advanced: "Add git version control; configure additional governance rules"
  remedial_for_struggling: "Use folder-only approach without Obsidian"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 1
  session_title: "Setting Up the Memory Layer"
  key_points:
    - "Memory/reasoning separation is the core insight — vault is memory (SOPs + knowledge), Claude Code is reasoning; this pattern recurs in every subsequent lesson"
    - "AGENTS.md is governance (rules of engagement), CLAUDE.md is the entry point — students must understand the difference before creating skills in L02"
    - "Obsidian MCP makes the Memory Bank location-independent — this is essential for Silver tier Watchers that run from outside the vault"
    - "The 'Without Vault vs With Vault' table is the motivating comparison — Claude without vault is amnesia, with vault is a stateful partner"
  misconceptions:
    - "Students think CLAUDE.md and AGENTS.md do the same thing — CLAUDE.md is the entry point Claude reads first, AGENTS.md is the governance rulebook it references"
    - "Students assume Claude Code remembers previous sessions automatically — it reads files each time, so the vault IS the memory mechanism"
    - "Students skip MCP setup thinking it is optional — without MCP, watchers in Silver tier cannot access the vault from outside the directory"
    - "Students confuse Obsidian (the UI tool) with the vault (the folder of markdown files) — Obsidian is just one way to edit the vault"
  discussion_prompts:
    - "What professional knowledge lives in your head right now that you re-explain to colleagues? How would encoding it as vault files change your workflow?"
    - "The lesson says Claude Code is a 'junior professional with access to your shared drive.' What are the limits of this analogy — where does it break down?"
    - "Why do you think the spec chose plain markdown files instead of a database for the Memory Bank?"
  teaching_tips:
    - "Do the MCP setup live in class — students hit configuration issues (wrong API key, Obsidian not running) that are easier to debug together"
    - "Have students test from OUTSIDE the vault directory (Step 7 Part D) before moving on — this catches MCP misconfigurations early"
    - "Emphasize the 'Without Vault vs With Vault' table as the lesson's thesis — return to it when students question why setup matters"
    - "Spend minimal time on the optional hidden files plugin (Step 8) — most students can edit via terminal and it is not needed for later lessons"
  assessment_quick_check:
    - "Ask students to explain the difference between CLAUDE.md and AGENTS.md in one sentence each"
    - "Have students run a Claude Code command from outside the vault directory using MCP — if it returns vault content, setup is correct"
    - "What are the three components of the memory/reasoning separation? (Vault=memory, Claude Code=reasoning, Skills=training)"

# Generation metadata
generated_by: "manual creation"
created: "2026-01-03"
version: "3.0.0"
---

# Your Employee's Memory

You're setting up Claude Code as your **General Agent** for professional work. Your projects and rules aren't forgotten when you close the session. Claude reads your vault and starts with memory every time.

![ai-vault](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-2/chapter-06/ai-vault.png)

This setup separates **memory** and **reasoning**:

- 🗂 **Memory Bank** – Your vault (SOPs, knowledge base, tasks, rules)
- 🧠 **Reasoning** – Claude Code reads your Memory Bank and acts on it
- 📘 **Skills** – Teaching documents that make behavior predictable
- 🛠 **MCP** – Tool connectors for real-world actions (Gmail, Obsidian vault, etc.)

**Think of it this way**: Your vault is a **Memory Bank** — a combination of SOPs (how to do things) and Knowledge Base (what you know). Obsidian MCP makes this Memory Bank accessible to Claude Code **from anywhere**, not just when you're inside the vault folder.

---

## The Problem

Most AI usage today is:

- **Chat-based** — conversations that disappear
- **Ephemeral** — no memory between sessions
- **Prompt-heavy** — re-explaining context every time
- **Inconsistent** — different results for same requests
- **Ungoverned** — no rules, no accountability

Even advanced users copy-paste context, re-explain their rules, and lose knowledge over time.

**The question**: How do we make AI work like a **trained professional**, not a clever chat agent without context about your professional work?

**The answer**: Give it a filesystem. A folder of markdown files solves the memory limitation of chat-only models. Claude Code reads files before every conversation, so it *thinks beyond a single session*. Your vault becomes Claude's long-term memory.

---

## The Core Insight

**Separate memory from reasoning.**

| Role | Tool | What It Does |
|------|------|--------------|
| **Memory** | Obsidian Vault | Source of truth you curate (notes, rules, SOPs) |
| **Reasoning** | Claude Code | Reads memory, follows rules, produces work |
| **Training** | Skills | Explicit teaching — repeatable, reviewable, auditable |

**Mental model**: Claude Code is a junior professional with access to your shared drive. Not autonomous. Not magical. Just capable and fast — and it follows your written instructions.

**Key shift**: Skills are *teaching*, not prompting. You write what the skill does, when to use it, how to do it, what not to do. This makes behavior predictable.

---

## Why This Matters

| Aspect | Without Vault | With Vault |
|--------|---------------|------------|
| Context per session | Zero | Full |
| Re-explaining needed | Every time | Never |
| Memory | None | Persistent |
| Aligned advice | Generic | Your goals |
| Pattern detection | Impossible | Automatic |
| Institutional knowledge | Lost | Accumulated |

**Claude Code without vault** = Smart agent with amnesia

**Claude Code with vault** = Your personal operator who knows your goals, remembers your history, follows your rules, and builds on previous work.

**One sentence**: The vault turns Claude Code into a stateful partner that accumulates context, enforces your rules, and compounds knowledge over time.

---

## Step 1: Install Obsidian

Download from [obsidian.md](https://obsidian.md)

---

## Step 2: Create Your Vault

1. Open Obsidian
2. Select **"Create new vault"**
3. Name your vault: `ai-vault` (or any name you prefer)
4. Choose location: `~/projects/ai-vault`
5. Click **Create**

Obsidian opens with an empty vault.

---

## Step 3: Create AGENTS.md

This file contains all the governance rules for how Claude Code should operate in your vault.

In Obsidian, create a new note called `AGENTS` and paste:

```markdown
# AGENTS - General Agent Governance

## Purpose

This vault is where I (human) and Claude Code (General Agent) work together on business workflows.

## Workspace Structure

ai-vault/
├── .claude/
│   ├── skills/        # Reusable expertise (SKILL.md format)
│   └── agents/        # Autonomous workers
├── references/        # Supporting documents
├── CLAUDE.md          # Project context (references this file)
└── AGENTS.md          # This file (governance)

## Governance Rules

1. **Skills go in `.claude/skills/{name}/SKILL.md`**
2. **Agents go in `.claude/agents/{name}.md`**
3. **Skills for guidance (2-4 decisions), agents for reasoning (5+)**
4. **Always read this file before operating**

## Active Projects

| Project | Series | Status |
|---------|--------|--------|
| Email Assistant | Email-1 to Email-7 | Starting |
```

Save the file. Now if you open vault folder you will notice an AGENTS.md file there. See direct markdown without any abstractions.

---

## What Goes In Your Vault?

Your vault isn't just governance files. It's your **professional memory**:

| Content Type | Example | How Claude Uses It |
|--------------|---------|-------------------|
| **SOPs** | `sops/client-onboarding.md` | Follows your documented process |
| **Client Notes** | `clients/acme-corp.md` | Knows context when writing emails |
| **Task Lists** | `tasks/this-week.md` | Prioritizes based on your priorities |
| **Templates** | `templates/weekly-report.md` | Uses your established formats |
| **Meeting Notes** | `meetings/2026-01-03-standup.md` | Remembers decisions and action items |
| **Reference Docs** | `references/pricing-tiers.md` | Gives accurate answers about your business |

**Start simple**: Begin with just governance files (AGENTS.md, CLAUDE.md). Add knowledge as you work. Every note you add makes Claude smarter about your specific domain.

**The accumulation effect**: Each piece of knowledge you add compounds. Client notes help with emails. Meeting notes inform task priorities. SOPs ensure consistent execution. Over months, your vault becomes institutional knowledge that makes Claude increasingly effective.

---

## Step 4: Create CLAUDE.md

This is the entry point Claude Code reads first. Create `CLAUDE` Note in the vault root:

```markdown
# Skills Lab

This is my professional Claude Code workspace.

Read @AGENTS.md for governance rules, formats, and structure.

## Current Focus

- **Email-N series**: Building an Email Assistant
```

Save the file.

### Personalizing Your CLAUDE.md

The example above is minimal. As you use your vault, personalize it to reflect how you work:

```markdown
# Skills Lab

This is my professional Claude Code workspace.

Read @AGENTS.md for governance rules, formats, and structure.

## About Me

- **Role**: Marketing consultant for SaaS startups
- **Timezone**: PST (working hours 9am-5pm)
- **Communication style**: Direct, no fluff, bullet points over paragraphs

## My Preferences

- Use American English spelling
- When drafting emails, match the formality of the recipient
- Default to concise (3 paragraphs max) unless I ask for detail
- Always include next steps at the end of client communications

## Current Focus

- **Email-N series**: Building an Email Assistant
- **Priority client**: Acme Corp (see `clients/acme-corp.md`)

## What I'm NOT Working On

- Internal company communications (use templates from `templates/internal/`)
- Social media (handled separately)
```

**Why this matters**: Claude Code reads this file first. The more it knows about your preferences, role, and working style, the less you need to re-explain. Your CLAUDE.md becomes your professional profile that shapes every interaction.

---

## Step 5: Open in Claude Code

Now test that Claude Code picks up your context.

```bash
cd ~/projects/ai-vault
claude
```

**Test prompt 1:**

```
What is this workspace and what governance rules should you follow?
```

**Expected**: Claude Code reads `CLAUDE.md`, follows the `@AGENTS.md` reference, and explains your workspace structure and governance rules.

If Claude Code responds with your vault-specific information, **your General Agent is configured**.

---

## Step 6: Create the Folder Structure

Now that Claude Code understands your workspace, create the folders:

```bash
mkdir -p .claude/skills
mkdir -p .claude/agents
mkdir -p references
```

---

## Step 7: Connect Memory Bank via MCP

This is the most important step. Without MCP, Claude Code only accesses your vault when you `cd` into it. With MCP, your Memory Bank is accessible **from anywhere**.

**Why this matters for the architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│              PERSONAL AI EMPLOYEE ARCHITECTURE              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PERCEPTION (Watchers)     REASONING (Claude)     ACTION   │
│  ┌─────────────────┐      ┌─────────────────┐    (MCP)    │
│  │ Gmail Watcher   │─────▶│                 │             │
│  │ runs from       │      │   Claude Code   │─────▶ Gmail │
│  │ /scripts/       │      │   (anywhere)    │             │
│  └─────────────────┘      │        │        │             │
│                           │        ▼        │             │
│                           │  ┌───────────┐  │             │
│                           │  │Memory Bank│◀─┼── Obsidian  │
│                           │  │via MCP    │  │     MCP     │
│                           │  └───────────┘  │             │
│                           └─────────────────┘             │
└─────────────────────────────────────────────────────────────┘
```

Watchers (Silver tier) run from `/scripts/`, not inside your vault. When they trigger Claude Code, Claude needs MCP to access your Memory Bank (SOPs, rules, knowledge).

### Part A: Install Obsidian REST API Plugin

The most popular Obsidian MCP server ([2.7k+ stars](https://github.com/MarkusPfundstein/mcp-obsidian)) uses Obsidian's REST API.

1. In Obsidian, go to **Settings** → **Community plugins**
2. Click **Browse** and search for "**Local REST API**"
3. Install and enable **Local REST API** by Adam Coddington
4. Go to the plugin settings and copy your **API Key**

**Default settings:**
- Host: `127.0.0.1`
- Port: `27124`
- Protocol: HTTPS (the MCP handles this automatically)

**Verify plugin is working:** Open `https://127.0.0.1:27124/` in your browser — you should see a JSON response with `"status": "OK"`.

### Part B: Install Obsidian MCP

```bash
claude mcp add mcp-obsidian --scope user -- uvx mcp-obsidian
```

Then set the environment variables. Edit `~/.claude.json`:

```json
{
  "mcpServers": {
    "mcp-obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "your-api-key-from-plugin",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27124"
      }
    }
  }
}
```

**Replace** `your-api-key-from-plugin` with the API key from the plugin settings.

### Part C: Verify Connection

```bash
claude mcp list
```

**Expected output:**
```
mcp-obsidian: connected
  Transport: stdio
  Tools: 12 tools
```

### What Obsidian MCP Provides

| Tool | What It Does |
|------|--------------|
| `list_files_in_vault` | List all files in vault |
| `get_file_contents` | Read any note |
| `search` | Search across all notes |
| `patch_content` | Update specific sections |
| `append_content` | Add to existing notes |
| `delete_file` | Remove notes |

:::info Vault Switching
The MCP connects to **whichever vault is currently open in Obsidian** — not to a specific vault path. To access a different vault:

1. In Obsidian, switch vaults (click vault icon or **File → Open vault**)
2. The MCP automatically connects to the new vault (no config change needed)

The REST API plugin must be enabled in each vault you want to access via MCP.
:::

### Part D: Test From Another Directory

```bash
cd ~/Desktop
claude
```

Then ask:
```
Using mcp-obsidian, get the contents of AGENTS.md and tell me my governance rules.
```

If Claude responds with your vault's governance rules, **your Memory Bank is accessible from anywhere**.

:::tip Why MCP is Essential
Without MCP, your AI Employee is "stuck" in the vault directory. With MCP, Claude Code becomes location-independent — the foundation for watchers, scheduled tasks, and autonomous operation.
:::

:::warning Obsidian Must Be Running
The REST API plugin requires Obsidian to be open. For always-on access (Silver tier watchers), keep Obsidian running in the background.
:::

---

## Step 8: Enable Hidden Files in Obsidian (Optional)

The `.claude` folder is hidden by default in Obsidian. This step lets you see and edit skills directly in Obsidian's file explorer.

**Skip this if**: You prefer editing `.claude/skills/` via terminal or VS Code.

### Part A: Enable Hidden Folders

1. In Obsidian, click **Settings** (gear icon, bottom-left)
2. Click **"Files and links"**
3. Enable **"Show hidden folders"**

### Part B: Install the Plugin

1. Go to [github.com/polyipseity/obsidian-show-hidden-files/releases/tag/2.5.0](https://github.com/polyipseity/obsidian-show-hidden-files/releases/tag/2.5.0)
2. Download: `main.js`, `manifest.json`, `styles.css`
3. Open your vault folder in Finder/Explorer
4. Create: `.obsidian/plugins/show-hidden-files/`
5. Copy the 3 downloaded files into that folder
6. Create `data.json` in the same folder:

```json
{
  "errorNoticeTimeout": 0,
  "language": "",
  "noticeTimeout": 5,
  "openChangelogOnUpdate": true,
  "showConfigurationFolder": true,
  "showHiddenFiles": true,
  "showingRules": [
    "+/",
    "-/\\.git(?:\\/|$)/u",
    "-/\\.venv(?:\\/|$)/u"
  ]
}
```

### Part C: Enable the Plugin

1. Go to **Settings** → **Community plugins**
2. Click **"Turn on community plugins"**
3. Toggle **"Show Hidden Files"** ON
4. Restart Obsidian

**Result**: You can now see `.claude/skills/` and `.claude/agents/` in Obsidian's file explorer.

---

## (Optional) Git Version Control

If you want institutional memory — tracking every change to your skills and agents:

```bash
cd ~/projects/ai-vault
git init
git add .
git commit -m "Initialize ai-vault workspace"
```

This is good practice but not required for the Email series.

---

## Your Setup Complete

```
ai-vault/                        (Your Employee's Memory Bank)
├── .claude/
│   ├── skills/         ← Ready for L02
│   └── agents/         ← Ready for L05
├── .obsidian/          (optional: show-hidden-files plugin)
├── references/
├── AGENTS.md           ← Governance rules (SOPs)
└── CLAUDE.md           ← Entry point for Claude Code

~/.claude.json          (MCP configuration)
└── mcpServers.obsidian ← Memory Bank accessible from anywhere
```

**What you have:**

| Component | Role | Why It Matters |
|-----------|------|----------------|
| **Obsidian** | Human interface | Edit Memory Bank visually |
| **Memory Bank** | SOPs + Knowledge Base | Your employee's long-term memory |
| **Obsidian MCP** | Location-independent access | Watchers can trigger Claude from anywhere |
| **AGENTS.md** | Governance rules | Your employee follows your SOPs |
| **Claude Code** | Reasoning engine | Reads Memory Bank, executes actions |

**The architecture in one sentence**: Watchers (perception) trigger Claude Code (reasoning) which reads your Memory Bank via MCP and takes actions via other MCP servers (Gmail, browser, etc.).

---

## Try With AI

**From inside your vault** (`cd ~/projects/ai-vault && claude`):

**Prompt 1: Verify Governance**

```
Read my AGENTS.md and tell me: What are my governance rules? What format should skills use?
```

**What you're practicing**: Confirming Claude Code reads your governance file when inside the vault.

**Prompt 2: Create First Structure**

```
Based on my AGENTS.md, create the folder structure I need for skills and agents if it doesn't exist.
```

**What you're practicing**: Having Claude Code execute based on your governance rules.

---

**From OUTSIDE your vault** (`cd ~/Desktop && claude`):

**Prompt 3: Verify MCP Access**

```
Using mcp-obsidian, get the contents of AGENTS.md and summarize my governance rules.
```

**What you're practicing**: Confirming your Memory Bank is accessible from anywhere via MCP — this is the foundation for watchers.

**Prompt 4: Skill Preview (from anywhere)**

```
Using mcp-obsidian to read my vault, I'm about to create an email-drafter skill. Based on my AGENTS.md governance, show me exactly what the file should look like and where it should go.
```

**What you're practicing**: Verifying Claude Code understands your skill conventions AND can access them from any directory.
