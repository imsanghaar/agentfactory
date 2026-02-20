---
slug: /General-Agents-Foundations/general-agents/compiling-mcp-to-skills
title: "Compiling MCP to Skills"
sidebar_position: 13
chapter: 3
lesson: 13
duration_minutes: 20

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration) - using pre-compiled browsing-with-playwright skill to understand code execution pattern"
layer_1_foundation: "Completed in Lessons 05-09 (Skills) and 12 (MCP)"
layer_2_collaboration: "Experiencing token reduction through using compiled skill vs direct MCP"
layer_3_intelligence: "N/A - Advanced lessons will cover skill creation"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Code Execution Pattern Understanding"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can use compiled skills from Skills Lab, compare token usage vs direct MCP, and explain code execution pattern benefits"

learning_objectives:
  - objective: "Recognize MCP token bloat and its impact on performance"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explain token overhead using Anthropic blog examples"
  - objective: "Use browsing-with-playwright skill from Skills Lab"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successfully execute browser automation with compiled skill"
  - objective: "Use fetch-library-docs skill with content-type filtering"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Fetch documentation with different content types and observe token savings"
  - objective: "Compare token usage between direct MCP and compiled skill"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Measure and report token reduction with concrete numbers"
  - objective: "Understand code execution pattern architecture"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explain how scripts running locally save tokens"

# Cognitive load tracking
cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (code execution pattern, content-type filtering, skills as guides, decision framework) - within B1 limit of 10 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Explore other compiled skills in Skills Lab; compare multiple MCP servers"
  remedial_for_struggling: "Focus on single operation (navigate only); use guided prompts"

teaching_guide:
  lesson_type: "core"
  session_group: 4
  session_title: "Subagents, MCP, and Compilation"
  key_points:
    - "The code execution pattern (SKILL.md + local scripts) achieves 98% token reduction by running MCP operations outside Claude's context window entirely"
    - "Three-stage loading for compiled skills (discovery at 30 tokens, activation at 150 tokens, execution at 0 tokens) extends the three-level architecture from Lesson 08"
    - "Skills can contain decision logic that guides Claude on when to use Tool Search vs compiled patterns — this makes skills intelligent advisors, not just executors"
    - "The decision framework (simple/infrequent = Tool Search, complex/repeated/filtered = compile) gives students a concrete rubric for real-world choices"
  misconceptions:
    - "Students think every MCP server should be compiled into a skill — the decision framework explicitly says low-overhead, infrequent-use MCP servers are fine as-is"
    - "Students confuse token savings with functionality loss — compiled skills provide the same results as direct MCP, just through local execution instead of context-window processing"
    - "Students think they need to write mcp-client.py themselves — the Skills Lab provides pre-built compiled skills; this lesson teaches usage and understanding, not creation"
    - "Students assume Tool Search and compilation are competing approaches — they are complementary, and the 'Skills as Intelligent Guides' section shows skills orchestrating both"
  discussion_prompts:
    - "The lesson shows 98% token reduction — if you had 5 MCP servers, how would you decide which ones to compile vs leave as direct MCP?"
    - "The meta-pattern shows skills containing decision logic about when they should activate — what other kinds of 'self-awareness' could you build into skills?"
    - "Compiled skills are portable across Claude Code, OpenAI Codex, and Goose — what does cross-agent portability mean for how you invest time in building skills?"
  teaching_tips:
    - "Run Steps 2 and 3 (direct MCP vs compiled skill) back-to-back on the same task so students see the token difference in real time"
    - "Use the token comparison table (15,000-24,000 vs 150-200 tokens) as the lesson's anchor number — write it on the board and reference it throughout"
    - "The 'Skills as Intelligent Guides' SKILL.md example showing when-to-use-what logic is the most advanced concept — save it for the second half of class when students have hands-on context"
    - "Connect back to Lesson 08's three-level loading: discovery/activation/execution maps directly to compiled skills' discovery/activation/local-execution pattern"
  assessment_quick_check:
    - "What is the approximate token cost of a compiled skill's SKILL.md vs direct MCP tool definitions?"
    - "Name two criteria from the decision framework that indicate you should compile an MCP server into a skill"
    - "Explain in one sentence why Stage 3 (execution) of a compiled skill consumes zero tokens in Claude's context"

# Generation metadata
generated_by: "content-implementer v1.0.0 (045-lesson-09-compiling-mcp-skills)"
source_spec: "specs/045-lesson-09-compiling-mcp-skills/spec.md"
created: "2025-12-19"
last_modified: "2026-01-19"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "1.2.0"

# Legacy compatibility
prerequisites:
  - "Lesson 07: Teach Claude Your Way (Skills Lab download)"
  - "Lesson 09: Agent Skills (SKILL.md format)"
  - "Lesson 12: MCP Integration"
---

# Compiling MCP to Skills

You learned in Lesson 12 that Claude Code's Tool Search automatically reduces MCP overhead by ~85%. For many workflows, that's enough.

But what if you need:

- **98% reduction** instead of 85%?
- **Local filtering** to process 1,000 items and return only 20?
- **Cross-agent portability** (Codex, Goose support Skills)?
- **Team-shareable workflows** (portable SKILL.md files)?

This lesson shows you the next level: **compile MCP servers into lean skills** that run operations locally and return only filtered results.

And here's the key insight: **skills can guide Claude on which approach to use**—automatically selecting Tool Search for simple queries and compiled patterns for complex workflows.

![skills-mcp](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-2/chapter-05/skills-mcp.png)

:::tip Industry Standard
Skills format is now supported by Claude Code, OpenAI Codex (beta), and Goose.
Skills you compile here work across all three agents.
:::

---

## The Problem: MCP Token Bloat

When Claude Code loads an MCP server, it eagerly loads ALL tool definitions upfront. Here's the real impact from Anthropic's engineering blog:

> "Tool descriptions occupy more context window space, increasing response time and costs. For agents with thousands of tools, this means processing hundreds of thousands of tokens before reading a request."
> — Anthropic, [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)

:::info Context
The quote above describes MCP behavior before Tool Search (January 2026).
Claude Code now handles 85% of this automatically via Tool Search.

This lesson covers the remaining 15%—and how to build skills that
intelligently orchestrate both approaches.
:::

**Concrete examples from the blog:**

- **Agent with 1,000 tools**: **150,000 tokens** loaded before your first request
- **2-hour meeting workflow**: Fetching transcript from Google Drive and attaching to Salesforce = **50,000 additional tokens** for repeated data processing
- **Compiled skill approach**: Reduces to **~2,000 tokens (98.7% reduction)**

**The math for a single MCP server**: Playwright MCP loads approximately 5,000-8,000 tokens of tool definitions. Use it 3 times in a session? That's 15,000-24,000 tokens of overhead—before you've accomplished anything.

#### 💬 AI Colearning Prompt

> "I have 3 MCP servers installed. Help me estimate my token overhead: For each server, how many tokens does it load at startup? What's my total context cost before I've even asked a question?"

---

## The Solution: Code Execution Pattern

Instead of calling MCP tools directly through Claude's context, compile them into **skills with executable scripts**:

### The Architecture

**SKILL.md + Scripts Model:**

```
.claude/skills/browsing-with-playwright/
├── SKILL.md                    # High-level procedures (~150 tokens)
├── references/                 # Cached tool documentation
└── scripts/
    ├── mcp-client.py          # Universal MCP client (HTTP/stdio transport)
    ├── start-server.sh        # Starts Playwright MCP on localhost:8808
    └── stop-server.sh         # Stops server gracefully
```

**How It Works:**

1. **SKILL.md** provides high-level procedures (loaded once at startup, ~150 tokens)
2. **Claude executes bash commands** calling `mcp-client.py` (runs locally, outside context)
3. **mcp-client.py** connects to Playwright MCP server via HTTP transport
4. **Server performs browser operations** (navigate, extract, screenshot)
5. **Only filtered results** returned to Claude's conversation

**Token Comparison:**

**1. Direct MCP (The Heavy Way)**

- Loads ALL tool definitions (~8,000 tokens)
- Process: `browser_navigate` (2k) → `browser_evaluate` (3k) → Return 1,000 items (10k) → Filter
- **Total Cost:** ~15,000 - 24,000 tokens

**2. Compiled Skill (The Efficient Way)**

- Loads ONLY the SKILL.md (~150 tokens)
- Process: Claude runs local script → Script connects to MCP → Script filters data locally → Returns 20 items
- **Total Cost:** ~150 - 200 tokens

**Savings: ~99%**

---

### Progressive Disclosure: 3-Stage Loading

Skills use **three-level loading** (covered in Lesson 9) to minimize token consumption:

1. **Discovery** (startup): Load only `description` field (~30 tokens)
2. **Activation** (when relevant): Load full SKILL.md (~150 tokens)
3. **Execution** (when needed): Run `scripts/` locally (0 tokens in context)

**Key for compiled skills:** Stage 3 executes MCP tools outside Claude's context, so heavy operations consume zero tokens.

**Example:**

```
User: "Extract product prices from Amazon"

→ Stage 1: Match description "browser automation"
→ Stage 2: Load SKILL.md procedures
→ Stage 3: Execute script locally (filter 1000 → 20 products)
→ Return only 20 results to Claude
```

---

## Hands-On: Use browsing-with-playwright Skill from Skills Lab

You'll experience the power of compiled skills by using the pre-built **browsing-with-playwright skill** from Skills Lab, then comparing its token efficiency against direct MCP usage.

### Step 1: Download Skills Lab

If you haven't already downloaded Skills Lab from Lesson 07, do so now:

1. Go to [github.com/imsanghaar/claude-code-skills-lab](https://github.com/imsanghaar/claude-code-skills-lab)
2. Click the green **Code** button
3. Select **Download ZIP**
4. Extract the ZIP file
5. Open the extracted folder in your terminal

**If you already downloaded Skills Lab in Lesson 07**, navigate to that folder.

### Step 2: Baseline - Try Playwright MCP Directly

First, let's see the token overhead WITHOUT compilation. If you have Playwright MCP configured in Claude Code, start Claude:

```bash
claude
```

Ask Claude to use Playwright MCP directly:

```
Use the Playwright MCP server to navigate to https://example.com
and extract the main heading text.
```

**What happens:**

- Claude loads ALL Playwright MCP tool definitions (~5,000-8,000 tokens)
- Calls `browser_navigate` tool through context
- Calls `browser_evaluate` or `browser_snapshot` through context
- Full tool schemas processed for each call
- Returns result

**Observe**: This works, but notice the initial loading overhead when Claude loads tool definitions.

### Step 3: Now Use browsing-with-playwright Skill

Exit Claude (Ctrl+C) and restart for a fresh session in the Skills Lab folder:

```bash
claude
```

Now ask using the compiled skill:

```
Use browsing-with-playwright skill to navigate to https://example.com
and extract the main heading text.
```

**What happens:**

```
⏺ Skill(browsing-with-playwright)
  ⎿  Loading…

────────────────────────────────────────────────────────────────────
 Use skill "browsing-with-playwright"?
 Claude may use instructions, code, or files from this Skill.

   Browser automation using Playwright MCP. Navigate websites, fill forms,
   click elements, take screenshots, and extract data.

 Do you want to proceed?
 ❯ 1. Yes
  2. Yes, and don't ask again for browsing-with-playwright in this directory
  3. No
```

Select **1. Yes**.

**What happens now:**

1. Claude loads browsing-with-playwright SKILL.md (~150 tokens only)
2. Skill tells Claude to run: `bash scripts/start-server.sh` (starts Playwright MCP on localhost:8808)
3. Claude executes bash commands:
   ```bash
   python mcp-client.py call -u http://localhost:8808 -t browser_navigate \
     -p '{"url": "https://example.com"}'
   ```
4. **Script runs OUTSIDE Claude's context** (0 tokens consumed)
5. Only the result comes back: page snapshot showing heading "Example Domain"
6. Claude runs another command to extract heading:
   ```bash
   python mcp-client.py call -u http://localhost:8808 -t browser_evaluate \
     -p '{"function": "() => document.querySelector('h1').textContent"}'
   ```
7. Result returned: `"Example Domain"` (~100 tokens)
8. Claude stops server: `bash scripts/stop-server.sh`

**Key Difference**: Tool definitions NEVER loaded into Claude's context. All browser operations happen locally via HTTP calls.

### Step 4: Compare Token Usage

Ask Claude:

```
Compare the token usage between:
1. Using Playwright MCP directly (what we did in Step 2)
2. Using browsing-with-playwright skill (what we just did in Step 3)

Estimate the tokens consumed in each approach and
show me the percentage reduction.
```

**Expected explanation:**

```
Direct Playwright MCP:
- Tool definitions loaded at startup: ~5,000-8,000 tokens
- browser_navigate call in context: ~2,000 tokens
- browser_evaluate call in context: ~2,000 tokens
- Result processing: ~500 tokens
- Total: ~9,500-12,500 tokens

browsing-with-playwright skill:
- SKILL.md loaded: ~150 tokens
- Bash commands executed: 0 tokens (runs locally)
- Only final results returned: ~100 tokens
- Total: ~250 tokens

Reduction: ~97-98% token savings
```

### Step 5: Test Different Browser Operations

Try various automation tasks to see the skill in action:

```
1. Use browsing-with-playwright to take a screenshot of https://github.com and save it
2. Use browsing-with-playwright to extract the page title from https://news.ycombinator.com
3. Use browsing-with-playwright to check if example.com contains the text "documentation"
```

**Observe:**

- Each operation runs bash commands locally
- You see: `python mcp-client.py call -t <tool_name> ...`
- Server starts once, handles multiple operations
- Only filtered results come back to conversation
- Claude doesn't reload tool definitions

### Step 6: Explore How browsing-with-playwright Works Internally

After trying the skill, explore its structure:

```bash
# Look at the skill structure
ls -la .claude/skills/browsing-with-playwright/
```

You'll see:

```
SKILL.md           # Procedures Claude follows (~150 tokens)
references/        # Cached tool documentation
scripts/           # Scripts Claude executes locally
```

**This is the code execution pattern**: Heavy operations happen in local HTTP server, outside Claude's token-counted context.

#### 💬 AI Colearning Prompt

> "I've used browsing-with-playwright skill. Explain: (1) How does running mcp-client.py via bash save tokens vs calling MCP tools through Claude's context? (2) What happens when Claude executes 'python mcp-client.py call -t browser_navigate'? (3) If I performed 10 browser operations, what would be the token difference between direct MCP vs browsing-with-playwright skill?"

---

## Hands-On 2: Use fetch-library-docs Skill

Let's try a second compiled skill that demonstrates a different use case: **fetching library documentation with intelligent filtering**. This skill wraps the Context7 MCP server and reduces tokens by 60-90% through content-type filtering.

:::note No Programming Required
You don't need to understand the code in the documentation—you're learning how **token reduction** works, not React or Next.js. Focus on the numbers: how many tokens before vs after.
:::

### What fetch-library-docs Does

When developers need documentation, they typically ask questions like:

- "How do I install Next.js?"
- "Show me examples of useState"
- "What's the API for fetch in JavaScript?"

**Without the skill**: Context7 MCP returns everything—examples, explanations, API references, troubleshooting—consuming thousands of tokens.

**With the skill**: You specify what you need (`setup`, `examples`, `api-ref`), and the skill filters locally, returning only relevant content.

### Step 1: Try fetch-library-docs Skill

In your Skills Lab folder, start Claude:

```bash
claude
```

Ask Claude to fetch installation instructions:

```
Use fetch-library-docs skill to look up "getting started" for Next.js.
I only need setup instructions, not code examples.
```

**What happens:**

1. Claude loads fetch-library-docs SKILL.md (~150 tokens)
2. Skill executes bash command locally:
   ```bash
   bash scripts/fetch-docs.sh --library nextjs --topic "getting started" --content-type setup
   ```
3. Script calls Context7 MCP via subprocess (outside Claude's context)
4. **Filters response locally** to extract only terminal commands and setup instructions
5. Returns filtered content (~50-100 tokens instead of ~500-800)

**You'll see output like:**

```
## Setup Instructions

### Installation
npm create next-app@latest my-app

### Run Development Server
cd my-app
npm run dev

[Token savings: 81%]
```

### Step 2: Compare Content Types

Now try the same library but requesting code examples:

```
Use fetch-library-docs skill to look up "data fetching" for Next.js.
I want code examples only.
```

**Different content type = different filtering:**

```bash
bash scripts/fetch-docs.sh --library-id /vercel/next.js --topic "data fetching" --content-type examples
```

**You'll see:**

```
## Code Examples

### Example 1
export default async function Page() {
  let data = await fetch('https://api.vercel.app/blog')
  let posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}

[Token savings: 92%]
```

### Step 3: Understand the Token Savings

Ask Claude to explain what just happened:

```
Compare the token usage between:
1. Calling Context7 MCP directly for "Next.js data fetching"
2. Using fetch-library-docs skill with --content-type examples

Show me the savings breakdown.
```

### Step 4: Explore the Skill Structure

Ask Claude to show you the internal structure of fetch-library-docs skill:

You'll see:

```
SKILL.md           # Decision logic for when/how to fetch docs
references/        # Library IDs, patterns, API details
scripts/           # Shell scripts that call Context7 MCP locally
  ├── fetch-docs.sh      # Main orchestrator
  ├── fetch-raw.sh       # Calls Context7 MCP
  ├── filter-by-type.sh  # Routes to content extractors
  └── extract-*.sh       # Content-type specific filters
```

**Key insight**: The filtering happens in shell scripts (local execution), not in Claude's context. This is why tokens are saved—heavy processing stays outside the conversation.

#### 💬 AI Colearning Prompt

> "I used fetch-library-docs skill with two different content types: setup and examples. Explain: (1) Why does 'setup' have higher token savings than 'examples'? (2) What happens locally when the skill filters content? (3) If I needed both examples AND API reference, how would I request that?"

---

## Skills as Intelligent Guides

Here's a powerful pattern: your SKILL.md can include logic that helps Claude decide when to use Tool Search vs compiled patterns.

### Example: Smart Browser Automation Skill

```markdown
# SKILL.md for browsing-with-playwright

## When to Use This Skill

**Use compiled pattern (this skill) when:**

- Extracting data from 50+ elements (local filtering needed)
- Running multi-step workflows (navigate → extract → transform)
- Need consistent, repeatable automation
- Sharing workflows with team (portable SKILL.md)

**Let Tool Search handle it when:**

- Single page navigation
- Quick element check
- One-off screenshot
- Simple form interaction

## Procedure

If this is a simple single-action task:
→ Suggest using Playwright MCP directly (Tool Search will handle efficiency)

If this requires filtering or multi-step workflows:
→ Use compiled scripts below...
```

### The Meta-Pattern: Skills That Know When They're Needed

Notice what's happening: the skill itself contains decision logic. Claude reads the SKILL.md and determines the best approach based on:

1. **Task complexity**: Simple → Tool Search; Complex → Compiled
2. **Output requirements**: Raw data → Tool Search; Filtered → Compiled
3. **Team needs**: Personal → Either; Shared workflow → Compiled (portable)

**This is intelligent orchestration**: Your skills become advisors, not just executors.

### Try It: Ask Claude About Approach Selection

```
I have browsing-with-playwright skill and Playwright MCP installed.
For each task, tell me which approach you'd use and why:

1. Take a screenshot of example.com
2. Extract all product prices from an e-commerce page (100+ items)
3. Fill out a contact form
4. Scrape competitor pricing daily and compare to our database
```

**Expected**: Claude uses the skill's guidance to recommend the right approach.

---

## When to Compile MCP Servers

Not every MCP server benefits from compilation. Use this decision framework:

### Compile to Skill When:

✅ **High token overhead** (>5,000 tokens per query)

- Example: Playwright, Google Drive, Database MCP, Context7 (documentation)

✅ **Frequent use** (3+ times per session or across projects)

- Repeated calls multiply token waste

✅ **Large datasets returned** (need filtering/transformation)

- Processing 1,000 items → returning 20 relevant ones

✅ **Multi-step workflows** (chaining operations)

- Navigate → extract → transform → filter

### Use Direct MCP When:

❌ **Low token overhead** (&lt;1,500 tokens per query)

- MCP already efficient, compilation overhead not worth it

❌ **Infrequent use** (once per month or less)

- Setup cost > token savings

❌ **Small, well-formatted results** (no transformation needed)

- Results already optimal for Claude

❌ **Rapidly changing API** (MCP tools frequently updated)

- Skill scripts would need constant maintenance

---

## Decision Framework: Automatic vs Compiled

Now you have three approaches. Here's when to use each:

| Scenario             | Approach           | Why                                |
| -------------------- | ------------------ | ---------------------------------- |
| Simple query         | Tool Search (auto) | Built-in efficiency, zero effort   |
| Multi-step workflow  | Compile to skill   | Local execution, better control    |
| Need local filtering | Compile to skill   | Process 1000 → return 20           |
| Cross-agent work     | Compile to skill   | Skills format is portable          |
| Team workflow        | Compile to skill   | Shareable SKILL.md                 |
| One-off query        | Direct MCP         | Overhead acceptable for single use |

**The smart approach**: Build skills with decision logic (like the example above). Let the skill guide Claude on which pattern to use.

**Decision shortcut**:

- Simple, infrequent? → Let Tool Search handle it
- Complex, repeated? → Compile to skill
- Need filtering? → Compile to skill
- Team workflow? → Compile to skill (portable)

---

## What's Ahead

You've experienced compiled skills and their massive token reduction—up to 98% savings while preserving full functionality. You understand the code execution pattern and why it works.

**Lesson 14: Settings Hierarchy** introduces the three-level configuration system that lets you control permissions, share team standards, and customize Claude Code across projects—tying together all the features you've learned (CLAUDE.md, skills, subagents, MCP) into a cohesive, configurable system.

**In advanced lessons**, you'll learn to create your own compiled skills using skill-creator, compiling other MCP servers (Google Drive, Database, etc.) and designing custom workflows. The skills you use from Skills Lab now become templates for creating your own later.

---

## Sources

Research and tools supporting this lesson:

- [Anthropic: Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Architecture for local execution + context reduction
- [Armin Ronacher: Skills vs Dynamic MCP Loadouts](https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/) — Token efficiency analysis and pattern recommendations
- [SmartScope: MCP Code Execution Deep Dive](https://smartscope.blog/en/blog/mcp-code-execution-agent-design/) — Detailed compilation workflow examples
- [Claude Code Documentation: MCP Integration](https://docs.anthropic.com/claude-code/mcp) — Official MCP protocol reference

---

## Try With AI

### browsing-with-playwright Skill

> "I've downloaded the Skills Lab. Guide me through using the browsing-with-playwright skill to extract product names from an e-commerce site. Show me the token savings compared to direct MCP."

**What you're learning:** How compiled skills execute locally, reducing round-trips and token overhead. The skill does what MCP would do—but more efficiently.

**Measure Token Reduction:**

> "I used browsing-with-playwright skill for 3 browser operations. Calculate the token savings: (1) Estimate tokens if I used Playwright MCP directly, (2) Estimate tokens with browsing-with-playwright skill, (3) Show percentage reduction with explanation."

**What you're learning:** Quantifying efficiency gains—the skill of measuring token consumption. This matters when you're optimizing production workflows for cost.

### fetch-library-docs Skill

**Fetch Different Content Types:**

> "Use fetch-library-docs skill to look up React useState. First fetch with --content-type examples, then with --content-type api-ref. Compare the outputs and explain why they're different sizes."

**What you're learning:** Content-type filtering as a token optimization technique—get exactly what you need, not everything available.

**Compare Token Savings:**

> "I need to look up 'routing' for Next.js. Show me the token difference between: (1) Using fetch-library-docs with --content-type setup, (2) Using fetch-library-docs with --content-type all (no filtering). Calculate the percentage saved."

**What you're learning:** The concrete cost of over-fetching. Small decisions about filtering compound into significant savings at scale.

**Decide When to Use:**

> "I have these MCP servers installed: [list]. For each, should I look for a compiled skill or use direct MCP? Use the decision framework to recommend."

**What you're learning:** The decision framework in practice—when compilation helps vs. when it's overkill. Not every MCP needs a skill.

**Compare Direct MCP vs Compiled Skill:**

> "I want to understand the difference: (1) Run a browser automation task using Playwright MCP directly, (2) Run the same task using browsing-with-playwright skill, (3) Show me the exact token difference and explain where savings come from."
