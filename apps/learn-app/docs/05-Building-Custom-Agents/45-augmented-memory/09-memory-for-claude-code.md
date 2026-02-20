---
sidebar_position: 9
title: "Memory for Claude Code"
description: "Install and configure the claude-mem plugin to give Claude Code persistent memory. Learn to use lifecycle hooks, privacy controls, web UI, and MCP tools for memory-augmented development assistance."
keywords: [claude-mem, Claude Code, persistent memory, lifecycle hooks, privacy controls, web UI, MCP tools, development assistant]
chapter: 45
lesson: 9
duration_minutes: 35

# HIDDEN SKILLS METADATA
skills:
  - name: "Claude Code Plugin Installation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can install and configure Claude Code plugins from marketplace"

  - name: "Memory Privacy Configuration"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can configure privacy controls and exclusion patterns"

  - name: "Memory Web UI Usage"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information and Data Literacy"
    measurable_at_this_level: "Student can navigate memory web UI to inspect and manage stored observations"

  - name: "MCP Memory Tools"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use MCP tools for memory search and retrieval"

learning_objectives:
  - objective: "Install and configure the claude-mem plugin for persistent memory in Claude Code"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successfully install plugin and verify hooks are active"

  - objective: "Configure privacy controls to prevent storage of sensitive information"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Set up exclusion patterns and verify sensitive data is not stored"

  - objective: "Use the web UI to inspect, search, and manage stored memories"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Navigate web UI to view timeline and search observations"

  - objective: "Leverage MCP tools for memory search within Claude Code conversations"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Use search and timeline tools to retrieve relevant context"

cognitive_load:
  new_concepts: 5
  assessment: "Medium cognitive load with 5 new concepts. Practical installation and exploration make concepts concrete. Builds on all memory concepts from L01-L08."

differentiation:
  extension_for_advanced: "Customize hook behavior; integrate with project-specific workflows; build memory-aware skills that leverage stored context"
  remedial_for_struggling: "Focus on installation and basic usage first; use web UI for memory inspection; explore gradually"
---

# Memory for Claude Code

You've built agents with memory from scratch. Now experience memory from the other side—as the user of a memory-augmented assistant.

The [claude-mem](https://github.com/thedotmack/claude-mem) plugin gives Claude Code persistent memory across sessions. It remembers your preferences, project context, and past decisions, making every conversation build on what came before.

By the end of this lesson, you'll have a memory-augmented Claude Code that knows your development style.

## Installation

### From Plugin Marketplace

```bash
# In Claude Code terminal
/plugin marketplace add thedotmack/claude-mem
```

Or install directly:

```bash
/plugin install claude-mem
```

### Verify Installation

After installation, restart Claude Code and check:

```bash
/plugins
```

**Output:**
```
Installed plugins:
• claude-mem (v1.0.0) - Active
  Hooks: SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd
  MCP Tools: search, timeline, get_observations
```

### Configuration Location

The plugin stores configuration and data in:

```
~/.claude-mem/
├── settings.json      # Configuration
├── memory.db          # SQLite storage
└── chroma/            # Vector embeddings
```

## How It Works

Claude-mem uses **lifecycle hooks** to capture and retrieve memories automatically:

```
┌─────────────────────────────────────────────────────────────┐
│                    CLAUDE-MEM ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                   Claude Code                        │   │
│   │                                                      │   │
│   │   User ──→ Prompt ──→ Tools ──→ Response            │   │
│   │     │        │         │          │                 │   │
│   └─────┼────────┼─────────┼──────────┼─────────────────┘   │
│         │        │         │          │                      │
│         ▼        ▼         ▼          ▼                      │
│   ┌─────────────────────────────────────────────────────┐   │
│   │              Lifecycle Hooks                         │   │
│   │                                                      │   │
│   │   SessionStart    → Retrieve relevant context        │   │
│   │   UserPromptSubmit → Capture user intent            │   │
│   │   PostToolUse     → Observe tool results            │   │
│   │   Stop            → Extract session insights        │   │
│   │   SessionEnd      → Finalize and store              │   │
│   │                                                      │   │
│   └──────────────────────────┬──────────────────────────┘   │
│                              │                               │
│   ┌──────────────────────────▼──────────────────────────┐   │
│   │              Storage Layer                           │   │
│   │                                                      │   │
│   │   SQLite (structured) + Chroma (semantic search)    │   │
│   │                                                      │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Hook Behavior

| Hook | When | What It Captures |
|------|------|------------------|
| `SessionStart` | Conversation begins | Retrieves relevant past context |
| `UserPromptSubmit` | User sends message | User intent and questions |
| `PostToolUse` | After each tool | Tool results and patterns |
| `Stop` | Response complete | Session insights and decisions |
| `SessionEnd` | Session closes | Finalizes and indexes memories |

## Privacy Controls

### The `<private>` Tag

Anything wrapped in `<private>` tags is **never stored**:

```
Can you help me debug this API call?
<private>
API_KEY=sk-1234567890abcdef
DB_PASSWORD=supersecret123
</private>
The error is a 401 Unauthorized.
```

Claude-mem will store: "User asked for help debugging API call, getting 401 Unauthorized error."

It will **not** store: API keys, passwords, or anything between `<private>` tags.

### Configuration Settings

Edit `~/.claude-mem/settings.json`:

```json
{
  "privacy": {
    "enabled": true,
    "excluded_patterns": [
      "password",
      "api_key",
      "api-key",
      "secret",
      "token",
      "bearer",
      "credential",
      "private_key",
      "ssh_key",
      "-----BEGIN"
    ],
    "excluded_paths": [
      "**/.env*",
      "**/secrets/**",
      "**/.ssh/**",
      "**/credentials/**"
    ]
  },
  "storage": {
    "path": "~/.claude-mem",
    "max_observations": 10000,
    "retention_days": 365
  },
  "retrieval": {
    "max_results": 10,
    "relevance_threshold": 0.5,
    "recency_weight": 0.3
  }
}
```

### Privacy Audit

Run a privacy check on stored memories:

```bash
# In terminal (not Claude Code)
cd ~/.claude-mem
sqlite3 memory.db "SELECT content FROM observations WHERE content LIKE '%password%' OR content LIKE '%api_key%' OR content LIKE '%secret%';"
```

If this returns results, review and clean up:

```bash
sqlite3 memory.db "DELETE FROM observations WHERE content LIKE '%password%';"
```

## Web UI

Claude-mem includes a web interface for exploring your memories.

### Starting the Web UI

```bash
# The server starts automatically with the plugin
# Access at:
open http://localhost:37777
```

### Web UI Features

**Timeline View**
```
┌─────────────────────────────────────────────────────────────┐
│  Memory Timeline                                     🔍 Search │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📅 Today                                                    │
│  ├── 10:45 AM - Working on Phoenix authentication           │
│  ├── 10:32 AM - Prefers pytest over unittest               │
│  └── 10:15 AM - Using FastAPI + SQLModel stack             │
│                                                              │
│  📅 Yesterday                                                │
│  ├── 4:30 PM - Fixed connection pool issue                 │
│  ├── 2:15 PM - Decided to use Qdrant for vectors           │
│  └── 11:00 AM - Started Phoenix project                    │
│                                                              │
│  📅 Last Week                                                │
│  └── ...                                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Search View**

Enter natural language queries:
- "What do I prefer for testing?"
- "Phoenix project context"
- "Past debugging sessions"

**Category Filters**

Filter memories by:
- Preferences
- Projects
- Decisions
- Errors
- Patterns

**Memory Management**

- Delete individual memories
- Bulk delete by date range
- Export memories as JSON

## MCP Tools

Claude-mem adds MCP tools for memory operations within Claude Code.

### Available Tools

**`search`** - Semantic memory search
```
Use the search tool to find memories about Python testing preferences
```

**`timeline`** - Recent observations
```
Show me my memory timeline from the last 7 days
```

**`get_observations`** - Retrieve specific observations
```
Get observations about the Phoenix project
```

### Using MCP Tools in Conversation

**Example 1: Context Retrieval**

```
You: What have I been working on lately?

Claude: [Uses timeline tool]
Based on your recent activity:
- This week: Phoenix project authentication module
- Focus: FastAPI endpoints and SQLModel integration
- Testing: Using pytest with async fixtures

You mentioned yesterday that the connection pool issue was
caused by missing cleanup in the context manager.
```

**Example 2: Preference Lookup**

```
You: How do I usually structure my models?

Claude: [Uses search tool with "model structure preferences"]
From our past conversations, you prefer:
- SQLModel for FastAPI projects (combines SQLAlchemy + Pydantic)
- Repository pattern for data access
- Separate Base classes from Table classes

Here's the pattern you've used before:
[Shows code from past context]
```

### The `mem-search` Skill

Claude-mem includes a built-in skill for natural language memory queries:

```
/mem-search testing frameworks I've used

Results:
1. [2025-01-20] Uses pytest, prefers fixtures over setup/teardown
2. [2025-01-15] Tried pytest-asyncio for async test support
3. [2025-01-10] Mentioned avoiding unittest in favor of pytest
```

## Experiencing Memory-Augmented Claude Code

### First Session

```
You: Hi, I'm starting a new Python project using FastAPI.

Claude: Great! I'll remember that you're working with FastAPI.
What kind of project is it?

You: It's a task management API. I prefer using SQLModel and pytest.

Claude: Perfect! I've noted your preferences:
- Framework: FastAPI
- ORM: SQLModel (nice choice - combines SQLAlchemy with Pydantic)
- Testing: pytest

Want me to help set up the project structure?
```

### Second Session (Next Day)

```
You: Let's continue working on the project

Claude: Welcome back! I remember you're building a task management
API with FastAPI + SQLModel. Yesterday we discussed the project
structure. Where would you like to pick up?

You: I need to add user authentication

Claude: For your FastAPI project, I'd suggest using python-jose
for JWT tokens - it works well with SQLModel. Based on your
preference for clean architecture, here's a pattern:

[Shows auth structure consistent with past decisions]
```

### The Memory Difference

| Without Memory | With Memory |
|---------------|-------------|
| "What framework?" | "Your FastAPI project..." |
| Generic examples | Examples using your stack |
| Repeated explanations | Builds on past context |
| Starting fresh | Continuous relationship |

## Workflow Patterns

### Pattern 1: Project Onboarding

When starting a new project, explicitly set context:

```
I'm starting a new project called "PaymentGateway":
- Stack: FastAPI, SQLModel, Redis for caching
- Architecture: Hexagonal with ports and adapters
- Testing: pytest with 80% coverage target
- Deployment: Docker + Kubernetes

Remember this context for our future conversations.
```

### Pattern 2: Decision Documentation

When making important decisions:

```
We decided to use Stripe over PayPal for payments because:
- Better API documentation
- Native Python SDK
- Webhook reliability

Please remember this decision and the reasoning.
```

### Pattern 3: Error Patterns

After debugging:

```
Found the issue: SQLModel relationship lazy loading fails in async.
Solution: Use selectinload() for async relationship queries.

Remember this pattern - it's likely to come up again.
```

### Pattern 4: Privacy-Aware Sharing

When sharing sensitive context:

```
The payment integration uses:
<private>
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
</private>

The webhook endpoint is /api/webhooks/stripe
```

## What Makes Memory Feel Right

After using memory-augmented Claude Code, these patterns create value:

### ✅ What Works

**Preference Persistence**
```
Week 1: "I prefer async/await over .then() chains"
Week 4: Claude automatically uses async/await in suggestions
```

**Project Context**
```
"The Phoenix project uses microservices with Kafka"
Later: Claude suggests Kafka patterns for related features
```

**Error Memory**
```
"That connection pool bug was from missing cleanup"
Later: Claude proactively mentions cleanup patterns
```

### ❌ What Feels Intrusive

**Over-remembering**
```
❌ "You mentioned liking pizza last month"
   → Not relevant to coding
```

**Stale Context**
```
❌ "Based on your preference for React..."
   → You've since switched to Vue (update preferences!)
```

**Wrong Confidence**
```
❌ "You always use X pattern"
   → You used it once (memory conflates frequency)
```

### The Balance

Good memory feels like working with a colleague who knows your style.
Bad memory feels like surveillance.

The difference: **relevance** and **recency**.

## Try With AI

Use these prompts to explore memory-augmented development.

### Prompt 1: Configure Your Memory Profile

```
I just installed claude-mem and want to set up my memory profile.
Help me create initial memories for:

1. My development preferences:
   - Languages I use most
   - Frameworks I prefer
   - Testing approach
   - Code style preferences

2. Current project context:
   - What I'm building
   - Architecture decisions
   - Key constraints

3. Privacy settings I should configure:
   - Patterns to exclude
   - File paths to ignore

Walk me through each category and suggest specific memories to store.
```

**What you're learning:** Explicit initial configuration sets the foundation for useful memory. Random accumulation leads to noise.

### Prompt 2: Memory Maintenance Routine

```
I've been using claude-mem for 3 months and want to do maintenance.
Design a monthly memory hygiene routine:

1. How to identify stale memories (outdated preferences, old projects)
2. How to find and remove potentially sensitive stored data
3. How to consolidate redundant memories
4. How to update preferences that have changed
5. A checklist I can follow each month

Include the actual commands and queries I should run.
```

**What you're learning:** Memory systems need maintenance. Without periodic cleanup, they accumulate noise that degrades retrieval quality.

### Prompt 3: Project Memory Template

```
I'm about to start a new project. Create a memory template that I can
fill out at project start to give Claude Code the right context:

Template should include:
1. Project identity (name, type, goals)
2. Technical stack (languages, frameworks, databases)
3. Architecture decisions and rationale
4. Coding standards and patterns to follow
5. Testing requirements
6. Known constraints or challenges

Format it so I can copy-paste and fill in the blanks, then share
with Claude Code to establish project memory.
```

**What you're learning:** Structured project onboarding creates better memory than organic accumulation. Templates ensure consistent, useful context.

## What You've Learned

This chapter took you from understanding why agents need memory to using memory-augmented tools:

| Lesson | Key Concept |
|--------|-------------|
| L01 | Context window problem and stateless vs stateful |
| L02 | Five memory types: conversation, working, episodic, semantic |
| L03 | Relevance scoring and privacy-compliant forgetting |
| L04 | Retrieval strategies: recency, relevance, entity, hybrid |
| L05 | Context window management and summarization chains |
| L06 | Mem0 SDK implementation for Task API |
| L07 | Production patterns: injection, retrieval, conflicts |
| L08 | Building complete memory-augmented agents |
| L09 | Memory for Claude Code with claude-mem plugin |

You now understand memory from both sides—as the builder and as the user. That dual perspective is essential for creating agents that people actually want to use.

## Next Steps

With memory in place, your agents can maintain context across sessions. The next chapter explores how to evaluate whether your agents actually work—testing strategies for AI systems that don't have deterministic outputs.
