---
slug: /General-Agents-Foundations/general-agents/mcp-integration
title: "MCP Integration"
sidebar_position: 12
chapter: 3
lesson: 12
duration_minutes: 14

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "MCP protocol basics, external system concepts"
layer_2_collaboration: "Co-exploring MCP servers with AI (AI suggests use cases, student provides application context, convergence on safe integration patterns)"
layer_3_intelligence: "N/A (MCP servers themselves are reusable, but lesson teaches usage not creation)"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Configuring MCP Servers for External Access"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can understand MCP as standardized external access protocol, install and configure MCP servers (Playwright for web browsing, Context7 for documentation), execute workflows integrating external data, and apply security best practices when enabling external access"

learning_objectives:
  - objective: "Understand Model Context Protocol (MCP) as safe external system access for Claude Code"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of how MCP enables Claude Code to access web, databases, APIs safely vs direct access"
  - objective: "Install and configure Playwright MCP for web browsing capabilities"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful installation and test of Playwright MCP with web browsing task"
  - objective: "Install and configure Context7 MCP for up-to-date documentation retrieval"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful installation and retrieval of current library documentation"
  - objective: "Execute practical workflows: browsing websites and fetching current docs"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Completion of workflow combining MCP with Claude Code task execution"
  - objective: "Apply security best practices when enabling external MCP server access"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Explanation of MCP security model and appropriate vs inappropriate MCP uses"

# Cognitive load tracking
cognitive_load:
  new_concepts: 8
  assessment: "8 concepts (MCP protocol, external access, Playwright MCP, Context7 MCP, security model, workflow integration, Tool Search, configuration) - within B1 limit of 10 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Create custom MCP server for team-specific needs (database access, internal APIs), explore GitHub MCP, Filesystem MCP, configure multiple MCP servers with different security profiles"
  remedial_for_struggling: "Focus on single MCP server (Playwright only), use pre-configured examples, skip Context7 initially"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 4
  session_title: "Subagents, MCP, and Compilation"
  key_points:
    - "MCP completes the three-pillar architecture: CLAUDE.md (project context) + Skills (procedures) + MCP (external access) = Digital FTE"
    - "The phone directory analogy (approved contacts for specific expertise) is the key mental model for understanding MCP's role as safe, standardized external access"
    - "Tool Search (auto since Claude Code 2.1.7+) reduces MCP overhead by 85% automatically — students should know this is built-in before worrying about optimization"
    - "The 'When NOT to use MCP' section is as important as 'When to use' — security boundaries around private data and untrusted servers are non-negotiable"
  misconceptions:
    - "Students think MCP replaces skills — use the expertise packs vs data pipes table to show they are complementary layers, not alternatives"
    - "Students assume all MCP servers are safe to install — the security section explicitly warns against untrusted npm packages and requires source verification"
    - "Students think MCP gives Claude unrestricted internet access — MCP provides structured, permission-controlled access through specific approved servers"
    - "Students confuse MCP overhead with MCP usefulness — Tool Search handles baseline efficiency automatically, so overhead is not a reason to avoid MCP"
  discussion_prompts:
    - "The lesson shows Claude browsing Amazon and fetching docs — what external system would you connect to first in your work, and what would you use it for?"
    - "The security section says 'never paste secrets into files' — why is this especially important when MCP servers can access external systems?"
    - "CLAUDE.md gives context, Skills give procedures, MCP gives access — which of the three would be hardest to replace with the other two?"
  teaching_tips:
    - "Run the two MCP installation commands live at the start of class — students seeing 'claude mcp add' succeed removes installation anxiety"
    - "Demo Workflow 1 (Amazon shopping) first because it produces visually interesting output that students immediately recognize as useful"
    - "Use the Expert Insight box (Three Pillars) as a recap moment — draw the CLAUDE.md > Skills > MCP > Digital FTE diagram on the board"
    - "For the security discussion, show a concrete example: 'claude mcp add mystery-tool some-random-npm-package' vs the verified Playwright command — make the risk tangible"
  assessment_quick_check:
    - "Complete this sentence: Skills provide ___, MCP provides ___"
    - "What command lists all MCP servers currently installed in your Claude Code?"
    - "Name one scenario where you should NOT use MCP and explain why"

# Generation metadata
generated_by: "content-implementer v1.0.0 (029-chapter-5-refinement)"
source_spec: "specs/029-chapter-5-refinement/spec.md"
created: "2025-01-17"
last_modified: "2026-01-19"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "2.1.0"

# Legacy compatibility
prerequisites:
  - "Lessons 01-09: Claude Code working, skills, CLAUDE.md understanding"
  - "Basic understanding of APIs (REST/JSON)"
  - "Playwright or Context7 account (optional but recommended)"
---

# MCP Integration: Connecting to External Systems

Right now, Claude Code can only see **files on your computer**.

But what if you need Claude to:

- Browse a website to find information?
- Check the latest documentation for a library?
- Query a database?
- Access an API?

**Skills (Lessons 5-9) taught Claude _how_ to do things. MCP teaches Claude _where_ to find outside information.**

All of that data lives **outside your computer**. Claude Code can't reach it... yet.

**Model Context Protocol (MCP)** solves this problem. It's like giving Claude Code safe, approved access to the outside world.

![skills-mcp-complementarity](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-2/chapter-05/skills-mcp-complementarity.png)

---

## Think of MCP Like This

Imagine Claude Code is a brilliant assistant who works in your office (your computer).

**Without MCP**: Your assistant can only use what's in the office—files on your desk, folders in your cabinet. That's it.

**With MCP**: You give your assistant a **phone directory** with approved contacts—a web browser expert, a documentation specialist, a database consultant. Now when your assistant needs outside information, they can call the right expert and get answers safely.

**MCP is that phone directory.** It connects Claude Code (your AI agent) to external tools and data sources in a **standardized, safe way**.

---

## In This Lesson

You will:

1. Add two beginner-friendly MCP servers to Claude Code
2. Try real workflows: browse Amazon, fetch docs
3. Understand when you need external access

No programming experience required. Just copy, paste, and see it work.

---

## A Note on Security (Read This First)

**Why security matters with MCP**: Unlike working with local files, MCP servers can access the internet, APIs, and external systems. This is powerful but requires trust.

**Stay safe**:

- Use trusted MCP servers. In this lesson we'll use two widely used, reputable servers: Playwright MCP and Context7 MCP.
- Your tokens and secrets are stored in your system keychain (not plain text).
- Never paste secrets into files; use prompts when Claude asks or environment variables.

---

## Hands-On: Add Two Helpful MCP Servers

We'll add two servers using simple commands.

```bash
# 1) Playwright MCP (browse the web)
claude mcp add --transport stdio playwright npx @playwright/mcp@latest

# 2) Context7 MCP (get up-to-date docs)
claude mcp add --transport stdio context7 npx @upstash/context7-mcp
```

**What's happening**: You're telling Claude Code about two external helpers it can use. Each command registers an MCP server that Claude can invoke when relevant.

---

## Workflow 1: Shop Together — Find a Shirt on Amazon (Playwright MCP)

Goal: Ask Claude to browse Amazon and find a shirt that matches your preferences. No code—just a plain request.

In Claude Code, say:

```
Use the Playwright MCP to browse Amazon. Find 3 men's casual shirts under $30 with good reviews. Share links, prices, main features, and any sizing notes. Prefer neutral colors.
```

What happens:

- Claude launches the Playwright MCP to visit Amazon
- It navigates pages, extracts details, and returns a neat summary with links
- You can iterate naturally: "filter to long-sleeve" or "show only Prime-eligible"

**Expected Output Example:**

Claude will return something similar to this (content varies by what's available):

```
Found 3 men's casual shirts under $30 with good reviews:

1. **Amazon Essentials Oxford Button-Down**
   - Price: $19.99 (Prime eligible)
   - Rating: 4.2/5 stars (2,341 reviews)
   - Colors: Navy, Gray, White
   - Sizing: Runs true to size; machine washable
   - URL: https://amazon.com/dp/B0XXXXXX
   - Why it matches: Great price, neutral colors, solid reviews

2. **Goodthreads Casual Oxford**
   - Price: $24.99
   - Rating: 4.5/5 stars (1,892 reviews)
   - Colors: Light Blue, Khaki, Navy
   - Sizing: Consider sizing up one size
   - URL: https://amazon.com/dp/B0YYYYYY
   - Why it matches: Excellent reviews, price under budget

3. **J.Crew Factory Essential Shirt**
   - Price: $29.99
   - Rating: 4.6/5 stars (3,204 reviews)
   - Colors: Sage Green, White, Cream
   - Sizing: True to size
   - URL: https://amazon.com/dp/B0ZZZZZZ
   - Why it matches: Highest rated option, neutral earth tones
```

**Note**: Real results vary by region, availability, and when you run this. Amazon changes its page structure frequently, so Claude adapts its browsing steps. The format (links, prices, ratings) stays consistent.

If you get an error:

- Ensure `playwright` MCP is registered: `claude mcp list`
- Try again; websites change often, so Claude may adjust its browsing steps
- Verify your internet connection is stable

---

## Workflow 2: Learn What's New — Ask for MCP Docs (Context7 MCP)

Goal: Ask Claude to use Context7 to fetch and summarize the latest resources about MCP in Claude Code.

In Claude Code, say:

```
Use the Context7 MCP to fetch the latest official documentation and articles about MCP support in Claude Code. Summarize what MCP is, how to add a server, and any recent changes or best practices. Include links and short quotes for key points.
```

What happens:

- Claude queries Context7's knowledge sources for up-to-date docs
- You get a short, current summary with citations and links
- Ask follow-ups: "show the exact CLI command to add a server via stdio" or "compare Context7 MCP vs GitHub MCP"

**Expected Output Example:**

Claude returns something like (real docs are current, not from memory):

````
## Model Context Protocol (MCP) - Latest Summary

**What is MCP?**
An open standard that allows Claude Code to safely access external tools, APIs, and data sources. The official docs (modelcontextprotocol.io) define MCP as "a unified protocol for connecting language models to external systems."

**How to Add an MCP Server**

Using the stdio transport (current standard in 2026):
```bash
claude mcp add --transport stdio <name> <command>
````

Example—Playwright:

```bash
claude mcp add --transport stdio playwright npx @playwright/mcp@latest
```

Verify installation:

```bash
claude mcp list
```

**Recent Changes (2026)**

- Stdio transport is now the default (network-based was beta in 2025)
- Permission model: Explicit allow-list per server in CLAUDE.md
- Context7 expanded to 200+ library documentation sources (50 in 2025)
- GitHub MCP now supports searching PRs and issues

**Best Practices (from official docs)**

1. Use allow-list configuration—only approve servers you trust
2. Test MCP servers in isolated projects before production
3. Keep servers updated: `claude mcp update --all`
4. Never store secrets in MCP commands—use environment variables

**Official Resources**

- Main docs: https://modelcontextprotocol.io/docs
- Getting started: https://modelcontextprotocol.io/docs/getting-started
- Server implementations: https://github.com/modelcontextprotocol

**Note**: Context7 fetches live documentation, so you always get the most current information. This beats searching Google and sifting through 10 outdated blog posts.

**Tip**: This is your "know about anything new" button. Use it anytime you need the latest docs without hunting across websites.

---

## Understanding MCP: The Bigger Picture

Now that you've tried MCP in action, let's understand the concepts more deeply.

### Skills + MCP: Expertise Packs Meet Data Pipes

Here's a powerful mental model from Anthropic:

| Component  | Role                           | Analogy                             |
| ---------- | ------------------------------ | ----------------------------------- |
| **Skills** | The "How-To" — expertise packs | Teaching Claude a specific workflow |
| **MCP**    | The "With-What" — data pipes   | Connecting skills to live data      |

**Skills are Expertise Packs**: They encode your procedures, your quality criteria, your domain knowledge. "How to analyze financial statements according to our Q4 risk framework."

**MCP provides Data Pipes**: They connect those expertise packs to live data sources. Your SQL database. Your Jira board. The web.

**Together**: Claude knows HOW to do something (skill) and has access to WHAT it needs (MCP).

**Example**: A skill encodes your company's financial reporting procedures. An MCP server connects Claude to your accounting database. Result: automated reports that follow your exact standards using real-time data.

### What MCP Unlocks

| Task                                   | Without MCP                                               | With MCP                                                                      |
| -------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Browse Amazon for products**         | Can't—no web access. You do the shopping.                 | Playwright MCP: Claude navigates, extracts prices/reviews, summarizes results |
| **Check React docs for latest API**    | Uses training data (outdated). May hallucinate.           | Context7 MCP: Fetches current docs. Real examples. Live citations.            |
| **Query your production database**     | Can't—no database access. You run queries, paste results. | Database MCP: Claude executes queries safely, analyzes results                |
| **Post updates to your Slack channel** | Can't—no API access. You copy-paste manually.             | Slack MCP: Claude sends messages, threads, reactions automatically            |
| **Analyze a GitHub repo structure**    | Can't—no GitHub access. You clone locally.                | GitHub MCP: Claude clones, analyzes, answers questions about code             |

**The pattern**: Without MCP, you're the bottleneck. With MCP, Claude Code becomes your autonomous partner.

#### 💬 AI Colearning Prompt

> "Explain how MCP provides safe external access compared to direct API calls. What security model does MCP use to protect user data?"

---

## How Claude Code Manages MCP Tools

When you add MCP servers, Claude Code doesn't just connect to them—it **intelligently manages** how tool definitions are loaded.

### The Challenge: Tool Definition Overhead

Each MCP server comes with tool definitions—descriptions of what each tool does, its parameters, and expected outputs. With multiple servers, these definitions can consume significant context:

- Playwright MCP: ~5,000-8,000 tokens of tool definitions
- Context7 MCP: ~3,000-5,000 tokens
- GitHub MCP: ~8,000-12,000 tokens

**With 5 servers installed**: 25,000-40,000 tokens before you've asked a question.

### The Solution: MCP Tool Search (Built-In)

Since January 2026, Claude Code 2.1.7+ includes **MCP Tool Search**—automatic lazy loading that defers tool definitions until needed.

**How it works:**

1. Claude Code monitors your installed MCP servers
2. When tool definitions exceed 10% of context, Tool Search activates
3. Instead of loading all tools upfront, Claude searches for relevant tools on-demand
4. Only the tools you actually use get loaded

**Result**: ~85% automatic reduction in MCP overhead.

### Control and Configuration

**Requirements:** Claude Code 2.1.7+ (auto-updates by default)

**Control it manually:**

```bash
# Default: activates when MCP tools exceed 10% of context
ENABLE_TOOL_SEARCH=auto claude

# Custom threshold (activate at 5%)
ENABLE_TOOL_SEARCH=auto:5 claude

# Always on (useful for testing)
ENABLE_TOOL_SEARCH=true claude

# Always off (legacy behavior, loads all tools upfront)
ENABLE_TOOL_SEARCH=false claude
```

Or set in `settings.json`:

```json
{
  "env": {
    "ENABLE_TOOL_SEARCH": "auto:5"
  }
}
```

### What This Means for You

**For most users**: You don't need to do anything. Tool Search works automatically.

**For power users**: Lesson 13 shows how to achieve even greater efficiency (98% reduction) through compilation—and how skills can intelligently guide which approach to use.

#### 💬 AI Colearning Prompt

> "I have 4 MCP servers installed. Help me understand: (1) How much context overhead am I generating? (2) Is Tool Search active for me? (3) What's my actual token consumption with Tool Search enabled vs disabled?"

---

## When to Use MCP (And When NOT To)

MCP is powerful, but it's not the right tool for everything. This section shows you the boundaries.

### ✅ When to Use MCP

**Use MCP when you need:**

- **Current information** (docs change frequently, your training data is outdated)
- **Real-time data** (stock prices, database queries, API responses)
- **Web interaction** (browsing, testing, scraping)
- **Safe external integration** (calling trusted APIs with permission controls)

**Example**: You're building a financial dashboard. Use MCP with a database server to fetch real-time trading data. Skills handle calculations. MCP handles data access.

### ❌ When NOT to Use MCP

**Don't use MCP for private/sensitive data:**

- Company financial records, personal keys, SSH credentials
- Confidential customer data, proprietary algorithms
- **Better approach**: Use local file access or store secrets in environment variables, then prompt Claude to retrieve them locally

**Example wrong**: "Use MCP to fetch our accounting database"  
**Example right**: "Here's the database dump (local file). Analyze using this skill."

**Don't use MCP for real-time high-frequency queries:**

- If you need 1000 database queries/second, use direct connections
- MCP adds latency per call (network roundtrip + Claude reasoning)
- **Appropriate workflow**: ~10 queries/minute with MCP; real-time streaming needs direct connections

**Example wrong**: "Continuously monitor 500 database records every second"  
**Example right**: "Check production health metrics every 5 minutes and alert me"

**Don't use MCP from untrusted servers:**

- Only use MCP servers from: Anthropic's official list, Modelcontextprotocol.io, verified npm packages
- A malicious MCP server could expose your system, read your files, access your tokens
- **Check before installing**: Read source code on GitHub, verify maintainer reputation, check recent commits

**Example wrong**: `claude mcp add mystery-tool some-random-npm-package`  
**Example right**: `claude mcp add playwright npx @playwright/mcp@latest` (widely used, verified source)

**Don't build custom MCP servers before you understand the basics:**

- Master Playwright and Context7 first (this lesson)
- Understand the security model (permission allow-lists, token storage)
- **Advanced topic**: Building custom MCP servers for databases, internal APIs (Part 7, Chapter 38)

**Example wrong**: "I'll build a custom MCP to access our Jira board today"  
**Example right**: "I'll try Playwright/Context7 first, then explore custom MCP next quarter"

---

#### 🎓 Expert Insight: The Three Pillars of AI-Native Development

**You've now learned the complete architecture.**

Remember **Lesson 05 (CLAUDE.md)**? You taught Claude your project: files, folder structure, coding standards, team practices. That gave Claude Code _context_.

Then **Lesson 09 (Skills)**? You taught Claude your domain procedures: workflows, decision trees, quality standards. That gave Claude Code _procedures_.

Now **Lesson 12 (MCP)** teaches Claude where to find the world's knowledge and tools. That gives Claude Code _reach_.

**Together, these three pillars form the foundation of AI-native development:**

```
CLAUDE.md  → Claude knows YOUR PROJECT
   ↓
Skills     → Claude knows YOUR PROCEDURES
   ↓
MCP        → Claude knows THE WORLD'S TOOLS
   ↓
Result: A Digital FTE that understands your goals, knows how you work, and can access any external system safely
```

**Why this matters**: Without CLAUDE.md, Claude is generic. Without skills, Claude repeats itself. Without MCP, Claude is blind to the outside world. With all three, Claude becomes truly autonomous.

This is the thesis of AI-native development: **Context + Procedures + Access = Digital FTE**.

---

## What's Ahead

MCP extends Claude Code's reach from your local filesystem to the entire world of external systems. Tool Search handles the baseline efficiency automatically.

But what if you need even more control?

**Lesson 13: Compiling MCP to Skills** teaches advanced optimization—achieving 98% token reduction through compilation. You'll learn how skills can intelligently guide Claude on when to use Tool Search vs compiled patterns, combining the subagent orchestration you learned in Lesson 11 with MCP's external access.

---

## Try With AI

Let's explore MCP integration through hands-on practice with external system access.

**🔍 Explore MCP Capabilities:**

> "I've successfully added the Playwright MCP for web browsing. Show me 3 specific web testing tasks I could accomplish with this MCP right now. For each task, give me the exact prompt I should use and explain what Playwright will do."

**What you're learning:** Discovering MCP capability boundaries—what becomes possible with external access that wasn't possible with filesystem alone.

**🎯 Practice Building Workflows:**

> "I need to test [describe your specific web application or research goal]. Walk me through building a complete workflow using Playwright MCP (for web browsing) and Context7 MCP (for documentation). Include: which MCP handles which part, exact prompts I should use, and how to verify everything works."

**What you're learning:** Multi-MCP orchestration—combining external capabilities into coherent workflows. This is the "data pipes" concept from the architecture.

**🧪 Troubleshoot Integration Issues:**

> "I'm trying to add an MCP server and it's not working. I ran [paste your installation command]. The error says [paste error message]. Walk me through troubleshooting: What's the most likely cause? What should I check? Give me 3 diagnostic commands to run with expected outputs."

**What you're learning:** MCP debugging methodology—the systematic approach to integration problems. This skill transfers to any external system connection.

**🛡️ Establish Security Boundaries:**

> "The lesson emphasizes MCP security. I'm nervous about giving Claude Code external access. Help me establish safe boundaries: What types of MCP servers should I avoid as a beginner? What permissions are risky? How do I audit what an MCP server can access? Create an MCP safety checklist I can follow."

**What you're learning:** Security-first thinking for AI external access—essential for production use where trust and verification matter.
