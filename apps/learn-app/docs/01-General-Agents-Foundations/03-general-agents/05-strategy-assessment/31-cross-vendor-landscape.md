---
slug: /General-Agents-Foundations/general-agents/cross-vendor-landscape
sidebar_position: 31
title: "The Cross-Vendor Landscape: Your Skills Are Portable"
description: "See how Claude Code concepts map to OpenAI Codex, Google Gemini CLI, and emerging industry standards — your agent-building skills transfer everywhere."
keywords: [openai codex, gemini cli, agents.md, mcp, agentic ai foundation, cross-vendor, portable skills]
chapter: 3
lesson: 31
duration_minutes: 25
chapter_type: Concept

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation) - Industry awareness and concept mapping"
layer_1_foundation: "Understanding cross-vendor equivalents, industry standards, market landscape"

# HIDDEN SKILLS METADATA
skills:
  - name: "Cross-Vendor Concept Mapping"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Student can map Claude Code concepts to their equivalents in Codex and Gemini CLI"
  - name: "Industry Standards Awareness"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Remember"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Student can name the three founding projects of the Agentic AI Foundation and explain why standards convergence matters"

learning_objectives:
  - objective: "Map every major Claude Code concept to its cross-vendor equivalent"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Concept mapping exercise"
  - objective: "Explain why MCP, AGENTS.md, and SKILL.md are converging under the Agentic AI Foundation"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Short explanation"
  - objective: "Compare the architectural philosophies of Claude Code vs Codex vs Gemini CLI"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Comparison table completion"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (cross-vendor mapping, AAIF standards convergence, SWE-bench benchmarking, poly-agentic workflows) - within A2 limit of 7"

differentiation:
  extension_for_advanced: "Install Codex CLI or Gemini CLI and compare the experience firsthand"
  remedial_for_struggling: "Focus only on the concept mapping table - the rest is enrichment"

# Generation metadata
generated_by: "content-implementer v2.0.0"
created: "2026-02-11"
last_modified: "2026-02-11"
git_author: "Claude Code"
workflow: "manual"
version: "1.0.0"

teaching_guide:
  lesson_type: "capstone"
  session_group: 11
  session_title: "Business Models and Industry Landscape"
  key_points:
    - "Every concept from Chapter 3 (CLAUDE.md, Skills, MCP, hooks, subagents, teams) has direct equivalents in Codex and Gemini CLI — the Concept Mapping Table is the proof"
    - "The Agentic AI Foundation (AAIF) governs three donated projects (MCP, AGENTS.md, goose) plus the Agent Skills spec — this is why skills are portable"
    - "The three philosophies (Claude: accuracy-first, Codex: async delegation, Gemini: open and accessible) are complementary, not competing — professionals use multiple tools"
    - "SWE-bench scores require context: different variants (Verified vs Pro) produce different numbers, making naive comparisons misleading"
  misconceptions:
    - "Students think learning Claude Code locks them into one vendor — the Concept Mapping Table shows every major concept transfers across tools"
    - "Students assume AAIF means all tools are identical — tools share standards (MCP, AGENTS.md, SKILL.md) but differ in execution model, pricing, and philosophy"
    - "Students interpret SWE-bench scores as absolute rankings — different benchmark variants (Verified, Pro, Lite) test different difficulty levels, so scores are not directly comparable across variants"
    - "Students believe 'poly-agentic' means picking the best single tool — it means using different tools for different strengths within the same workflow"
  discussion_prompts:
    - "Looking at the Concept Mapping Table, which row surprised you most — which concept did you think was Claude-specific but turns out to be an industry pattern?"
    - "If you were advising a company choosing between Claude Code, Codex, and Gemini CLI, what three questions would you ask them before making a recommendation?"
    - "Reflecting on the full Chapter 3 journey — from your first Claude Code session to cross-vendor fluency — which single concept do you think will matter most in your career five years from now?"
  teaching_tips:
    - "Project the Concept Mapping Table and walk through it row by row — for each row, connect back to the specific Chapter 3 lesson where students first learned that concept"
    - "Use the Three Philosophies table as a group exercise: assign each group a philosophy and have them argue why their tool is best for a given scenario"
    - "For the SWE-bench section, show how the same model can score differently on Verified vs Pro to teach critical benchmark literacy"
    - "As this is the chapter closer, explicitly tie the full arc together: Lesson 1 (what are agents) through Lesson 31 (your skills transfer everywhere) — the chapter thesis is that agent-building patterns are universal, not vendor-specific"
  assessment_quick_check:
    - "Name the three founding projects of the Agentic AI Foundation and what each standardizes."
    - "What is the SKILL.md directory path in Claude Code vs Codex vs Gemini CLI?"
    - "Why can you not directly compare a SWE-bench Verified score with a SWE-bench Pro score?"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Completion of Lessons 01-29 in this chapter"
  - "Understanding of Skills, MCP, CLAUDE.md, hooks, subagents, and teams"
---

# The Cross-Vendor Landscape: Your Skills Are Portable

You've spent this entire chapter learning Claude Code. Here's the secret: **you weren't just learning one tool.**

Every concept you mastered -- CLAUDE.md project instructions, Skills, MCP servers, hooks, subagents, agent teams -- is part of an emerging industry standard. OpenAI's Codex CLI has its own version of each. Google's Gemini CLI has its own version. And in December 2025, several of these vendors created the Agentic AI Foundation (AAIF) under the Linux Foundation, donating key projects to seed open, vendor-neutral standards for agentic AI.

MIT Technology Review named "Generative Coding" one of its 10 Breakthrough Technologies of 2026. AI now writes approximately 30% of Microsoft's code and more than 25% of Google's. The tools you learned in this chapter are not a niche experiment. They are the new baseline for how software gets built.

---

## The Market in February 2026

The agentic coding market has consolidated into two leaders and several strong contenders.

### Tier 1: The Two Leaders

**Anthropic (Claude Code)**
Analyst estimates put Claude Code at ~$1B annual recurring revenue as of early February 2026 ([Sacra](https://sacra.com/c/anthropic/)). SemiAnalysis estimated Claude Code accounts for ~4% of all public GitHub commits ([SemiAnalysis, Feb 5, 2026](https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point)). Claude Opus 4.5 holds the top spot on SWE-bench Verified at 80.9%. Philosophy: developer-in-the-loop, local terminal execution, accuracy-first.

**OpenAI (Codex)**
Codex CLI is open source, built in Rust, installable via `npm i -g @openai/codex` ([GitHub](https://github.com/openai/codex)). OpenAI launched a macOS desktop app on February 2, 2026, and released GPT-5.3-Codex on February 5, 2026. Codex supports cloud sandbox execution (default for delegated tasks) and also provides local CLI modes. Philosophy: parallel, asynchronous, fire-and-forget delegation.

### Tier 2: Strong Contenders

| Tool | Key Stat | Positioning |
|------|----------|-------------|
| **Cursor** | ~$1B ARR, ~$29.3B valuation (analyst est., [Sacra](https://sacra.com/c/cursor/)) | Fastest SaaS growth in history ([SaaStr](https://www.saastr.com/cursor-hit-1b-arr-in-17-months-the-fastest-b2b-to-scale-ever-and-its-not-even-close/)). IDE-first experience. |
| **GitHub Copilot** | 68% developer usage, ~$400M revenue 2025 ([a16z](https://a16z.com/the-trillion-dollar-ai-software-development-stack/)) | Agent mode GA. Massive distribution via GitHub ecosystem. |
| **Google Gemini CLI** | Open source (Apache 2.0), free tier (1,000 req/day), 1M token context | Accessible, open, enormous context window. |

### Tier 3: Emerging Players

Amazon Q Developer and Devin (which acquired the Windsurf product and brand) round out the landscape.

---

## The Concept Mapping Table

This is the most important table in this lesson. Everything you learned in Chapter 3 has equivalents across the industry:

| What You Learned | Claude Code | OpenAI Codex | Google Gemini CLI | Open Standard |
|---|---|---|---|---|
| Project instructions | CLAUDE.md | AGENTS.md | GEMINI.md | AGENTS.md (AAIF) |
| Agent Skills | `.claude/skills/SKILL.md` | `.agents/skills/SKILL.md` | `.gemini/skills/SKILL.md` | Agent Skills spec (agentskills.io) |
| Tool connectivity | MCP servers in settings.json | MCP servers in config.toml | MCP servers in settings.json | MCP (Linux Foundation) |
| Human-in-the-loop control | allowedTools, permissions | Approval modes (suggest / auto-edit / full-auto) | Tool approval prompts | Vendor-specific (no standard yet) |
| Context hierarchy | Global, Project, Directory | Global, Project | Global, Project, Directory | Vendor-specific (no standard yet) |
| Subagents | Task tool with subagent_type | Cloud sandbox tasks | Not yet available | Vendor-specific (no standard yet) |
| Agent Teams | TeamCreate, TaskCreate, SendMessage | macOS app parallel agents | Not yet available | Vendor-specific (no standard yet) |
| Hooks | Pre/Post tool hooks in settings.json | Not yet available | Not yet available | Vendor-specific (no standard yet) |
| IDE integration | VS Code extension | VS Code extension | VS Code extension | Vendor-specific (no standard yet) |
| Desktop app | Claude Desktop / Cowork | Codex macOS app | Not yet available | Vendor-specific (no standard yet) |

The pattern: what you know transfers. The directory name changes (`.claude/` vs `.agents/` vs `.gemini/`), but the concepts are the same.

---

## Standards Convergence: The Agentic AI Foundation

In December 2025, the biggest companies in AI did something unusual: they agreed on shared standards.

The **Agentic AI Foundation (AAIF)** formed under the [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) with platinum members including Anthropic, OpenAI, Google, Microsoft, AWS, Block, Bloomberg, and Cloudflare. The foundation governs three founding projects:

| Project | Created By | What It Standardizes | Adoption |
|---------|-----------|---------------------|----------|
| [**MCP**](https://modelcontextprotocol.io/) (Model Context Protocol) | Anthropic ([donated](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)) | Tool connectivity -- how agents talk to external services | 10,000+ active public servers, 97M monthly SDK downloads |
| [**AGENTS.md**](https://agents.md/) | OpenAI (donated) | Project instructions -- how agents understand your codebase | 60,000+ open source projects |
| **goose** | Block (donated) | Open agent runtime -- reference implementation for agentic workflows | Open source agent framework |

A fourth standard, **Agent Skills** (the SKILL.md format), was created by Anthropic on December 18, 2025, and has been adopted by OpenAI, Microsoft (GitHub Copilot), Cursor, Atlassian, and Figma. The specification lives at [agentskills.io](https://agentskills.io/).

**What this means for you**: The Skills you built in this chapter using `.claude/skills/` follow the same specification that Codex uses in `.agents/skills/` and Gemini CLI uses in `.gemini/skills/`. Different directory names, same format. Your Skills are largely portable where the SKILL.md spec is followed; vendor-specific metadata and directory paths may differ slightly.

---

## Three Philosophies, One Ecosystem

Each tool reflects a different design philosophy. None is universally "best" -- they excel at different work.

| | Claude Code | OpenAI Codex | Gemini CLI |
|---|---|---|---|
| **Philosophy** | "Measure twice, cut once" | "Move fast, iterate" | "Open and accessible" |
| **Execution** | Local terminal | Cloud sandbox + local | Local CLI + cloud inference |
| **Strengths** | Deep reasoning, accuracy, self-correction | Parallel tasks, async delegation, speed | Free tier, 1M context, open source |
| **Best for** | Complex refactoring, architecture work | Batch operations, exploration | Budget-conscious teams, large codebases |
| **Pricing** | $20+/month subscription | $20-$200/month (via ChatGPT) | Free (1,000 req/day) |
| **Open source** | No | CLI is open source (Rust) | Yes (Apache 2.0) |

Professional developers increasingly use multiple tools for different strengths. Claude Code for the careful architecture work. Codex for parallelized bulk tasks. Gemini CLI for quick queries against massive codebases. This is "poly-agentic" development -- choosing the right tool for each task, not committing to one forever.

---

## SWE-bench: The Coding Benchmark

SWE-bench is a benchmark that tests whether AI can solve real software engineering problems pulled from open source GitHub repositories. Unlike artificial coding challenges, SWE-bench tasks require reading existing code, understanding project context, and producing working fixes.

Multiple variants exist with different difficulty levels. **SWE-bench Verified** uses human-validated problems. **SWE-bench Pro** is harder, with more complex multi-file problems.

### SWE-bench Verified Leaderboard (February 2026, [source](https://www.marc0.dev/en/leaderboard))

| Rank | Model | Score |
|------|-------|-------|
| 1 | Claude Opus 4.5 | 80.9% |
| 2 | Claude Opus 4.6 | 80.8% |
| 3 | GPT-5.2 | 80.0% |
| 4 | Gemini 3 Flash | 78.0% |
| 5 | Claude Sonnet 4.5 | 77.2% |
| 6 | Gemini 3 Pro | 76.2% |

**Important caveat**: Companies report scores on different benchmark variants, making direct comparisons tricky. GPT-5.3-Codex scores 56.8% on SWE-bench Pro -- which is a harder test, not a worse score. When comparing models, always check which variant was used.

---

## Why This Matters for Your Career

The patterns you learned in this chapter are not Claude Code patterns. They are **industry patterns**.

When you write a CLAUDE.md file, you are practicing the same skill as writing an AGENTS.md file for Codex or a GEMINI.md file for Gemini CLI. When you build a Skill in `.claude/skills/`, you can port it to Codex or Gemini CLI by moving the SKILL.md file to a different directory. When you connect an MCP server, that same server works with every tool that supports the protocol.

This portability exists because the industry converged. The AAIF ensures that MCP servers, AGENTS.md files, and Agent Skills work the same way regardless of which coding agent you choose. Your investment in learning these patterns compounds across every tool you touch.

The developers who will thrive are not the ones who master one tool. They are the ones who understand the underlying patterns -- context files, skills, tool connectivity, orchestration -- and apply them wherever the work demands. That is what you built in this chapter.

---

## A Note on Security

MCP and agentic tool connectivity expand what agents can do -- but they also expand the attack surface. When an agent can call external servers, read files, and execute commands, the consequences of a compromised or malicious tool server are significant: prompt injection, data exfiltration, and unintended code execution are all real risks.

As you work across tools and connect MCP servers, apply the same caution you would when installing any third-party dependency: review the server code before trusting it, run MCP servers in isolated environments where possible, and prefer servers from verified publishers. The MCP specification includes transport-level security, but the responsibility for evaluating trust ultimately rests with you.

---

## Try With AI

```
What are the architectural differences between you (Claude Code)
and OpenAI's Codex CLI? Be specific about execution model,
sandboxing, and where each tool runs code.
```

**What you're learning:** How to use an AI agent to analyze its own competitive landscape. Claude Code has direct knowledge of its own architecture and can reason about public information on competitors. This develops your ability to gather technical intelligence through AI conversation.

```
I have a skill at .claude/skills/my-skill/SKILL.md. Show me how
to create an equivalent for OpenAI Codex (in .agents/skills/)
and for Gemini CLI (in .gemini/skills/). What changes are needed
in each version?
```

**What you're learning:** Cross-vendor skill porting. The answer reveals how much of the SKILL.md format is universal (most of it) versus vendor-specific (directory path and minor configuration). This is the practical proof that your skills are portable.

```
Search the web for the latest SWE-bench Verified leaderboard.
How do Claude, GPT, and Gemini models compare? What should I
consider beyond benchmark scores when choosing a coding agent?
```

**What you're learning:** Critical evaluation of AI benchmarks. Scores matter, but so do execution model, pricing, context window, and workflow fit. This prompt teaches you to make tool decisions based on multiple factors, not just a single number.

---

## Further Reading

- [Agentic AI Foundation (Linux Foundation)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) -- AAIF founding announcement
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) -- official specification
- [Agent Skills specification](https://agentskills.io/) -- SKILL.md format
- [AGENTS.md](https://agents.md/) -- cross-vendor project instructions standard
- [OpenAI Codex CLI](https://github.com/openai/codex) -- open source repository
- [Google Gemini CLI](https://github.com/google-gemini/gemini-cli) -- open source repository
- [SWE-bench Verified leaderboard](https://www.marc0.dev/en/leaderboard) -- February 2026 snapshot

:::info Snapshot disclaimer
The AI model and market landscape change rapidly. Figures in this lesson reflect snapshots from February 2026 and are cited to specific public sources. Check the linked references for the latest numbers. Benchmark scores are self-reported by model providers unless independently verified, and different evaluation variants (Verified, Pro, Lite) produce different results for the same models.
:::

---

## What's Next

You've completed the full Chapter 3 journey -- from your first Claude Code session through skills, MCP, hooks, plugins, agent teams, and now cross-vendor fluency. Next up: the **Chapter Quiz** (Lesson 32) to test your understanding across all 31 lessons.
