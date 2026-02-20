### Core Concept
The skills you learned in this chapter aren't Claude Code-specific—they're industry-standard patterns that transfer across OpenAI Codex, Google Gemini CLI, and all tools converging under the Agentic AI Foundation. Your investment in learning CLAUDE.md, Skills, MCP, and agent orchestration is portable across the entire agentic coding ecosystem.

### Key Mental Models
- **Cross-Vendor Portability**: CLAUDE.md → AGENTS.md → GEMINI.md, `.claude/skills/` → `.agents/skills/` → `.gemini/skills/`—same concepts, different directory names
- **Standards Convergence**: Three founding projects (MCP, AGENTS.md, goose) plus Agent Skills spec mean tools are interoperable by design, not accident
- **Poly-Agentic Development**: Professional developers use multiple tools for different strengths (Claude Code for careful architecture, Codex for parallel tasks, Gemini CLI for large codebases)—not commitment to one tool forever
- **Industry Benchmark**: SWE-bench tests real software engineering (not artificial challenges)—but variants differ in difficulty, making direct comparisons tricky

### Critical Patterns
- **The Concept Mapping Table** (memorize this):
  - Project instructions: CLAUDE.md / AGENTS.md / GEMINI.md → AGENTS.md standard (AAIF)
  - Agent Skills: `.claude/skills/SKILL.md` → `.agents/skills/SKILL.md` → `.gemini/skills/SKILL.md` → Agent Skills spec (agentskills.io)
  - Tool connectivity: MCP servers in settings.json/config.toml → MCP standard (Linux Foundation)
  - Subagents/Teams: Claude Code and Codex both support, Gemini CLI doesn't (yet)

- **Three Philosophies**:
  - **Claude Code**: "Measure twice, cut once"—local execution, deep reasoning, accuracy-first (best for complex refactoring)
  - **OpenAI Codex**: "Move fast, iterate"—cloud sandbox + local, parallel async tasks, speed-focused (best for batch operations)
  - **Gemini CLI**: "Open and accessible"—free tier, 1M token context, open source (best for budget-conscious teams, large codebases)

- **Market Positioning (February 2026)**:
  - Tier 1 Leaders: Anthropic ($1B ARR, 4% of all GitHub commits) and OpenAI (Codex CLI open source, macOS desktop app)
  - Tier 2 Contenders: Cursor ($1B ARR), GitHub Copilot (68% developer usage), Gemini CLI (free tier)
  - Tier 3 Emerging: Amazon Q Developer, Devin (acquired Windsurf)

### Common Mistakes
- Treating learned skills as Claude Code-specific instead of recognizing them as industry patterns
- Comparing benchmark scores across different SWE-bench variants (Verified vs Pro)—always check which test was used
- Committing to one tool when poly-agentic approach (right tool for each task) is more effective
- Thinking portability is future promise—standards convergence happened in December 2025, it's live now
- Ignoring that AI writes ~30% of Microsoft code and 25%+ of Google code—this isn't experimental, it's the new baseline

### Connections
- **Builds on**: All Chapter 3 concepts (CLAUDE.md, Skills, MCP, hooks, plugins, subagents, teams) are now understood as portable industry patterns
- **Leads to**: Chapter Quiz (Lesson 32) testing understanding across all 31 lessons, then application in later chapters
- **Career Impact**: Investment in these patterns compounds across every tool you touch—learning one deeply means learning the underlying architecture of all agentic coding tools
