### Core Concept
The Agentic AI Foundation (AAIF), a Linux Foundation initiative announced December 9, 2025, provides neutral governance for five open standards (MCP, AGENTS.md, goose, Agent Skills, MCP Apps Extension) that make Digital FTEs portable across AI platforms rather than locked to a single vendor. These standards solve the M*N integration problem and enable "write once, deploy everywhere" agent architecture.

### Key Mental Models
- **USB Implementers Forum Analogy**: Just as USB standardized device connections so any device works with any port, AAIF standardizes agent connections so Digital FTEs work across any AI platform. AAIF is the governance body; the standards create actual portability.
- **MCP's Three Primitives**: Resources (read-only data -- eyes), Tools (actions that change state -- hands), and Prompts (reusable templates -- playbooks). Getting the classification wrong breaks your agent.
- **Skills vs MCP Complementarity**: MCP provides connectivity (the agent's hands -- how to reach tools). Skills provide expertise (the agent's training -- what to do with tools). Without MCP, agents can't reach systems. Without Skills, agents don't know best practices.
- **Progressive Disclosure for Token Efficiency**: Skills load in three levels: Level 1 at startup (~100 tokens: name and description), Level 2 when activated (<5K tokens: full instructions), Level 3 when needed (supporting resources). This achieves 80-98% token reduction.
- **AGENTS.md as Agent-Readable Context**: README.md tells humans what a project is; AGENTS.md tells AI agents how to behave (build commands, code style, security constraints, architecture patterns). The nearest AGENTS.md file takes precedence (hierarchy rule).

### Key Facts
- **AAIF announced**: December 9, 2025, under Linux Foundation governance
- **Founding members**: OpenAI, Anthropic, Block (donated core technologies); AWS, Google, Microsoft, Bloomberg, Cloudflare as platinum members
- **MCP timeline**: Open-sourced November 2024 by Anthropic; OpenAI adopted March 2025; Google April 2025; MCP spec 2025-11-25 with OAuth 2.1; donated to AAIF December 2025
- **AGENTS.md adoption**: 60,000+ open-source projects since OpenAI introduced it August 2025; adopted by Claude Code, Cursor, GitHub Copilot, Gemini CLI, Devin, goose
- **Agent Skills timeline**: Launched by Anthropic October 16, 2025; released as open standard December 18, 2025 at agentskills.io; OpenAI adopted same SKILL.md format
- **goose stats**: 75% of Block engineers save 8-10+ hours weekly using it; Apache 2.0 licensed
- **MCP Apps Extension (SEP-1865)**: Announced November 21, 2025 for interactive UI via MCP servers
- **OpenAI Apps SDK**: Distribution to 800M+ ChatGPT users

### Critical Patterns
- The five standards map to Digital FTE capabilities: MCP (tool connectivity), AGENTS.md (client adaptability), Skills (domain expertise), goose (architecture patterns), MCP Apps (interface reach)
- MCP Host -> Client -> Server architecture uses JSON-RPC protocol for communication between AI applications and tool integrations
- goose serves dual purpose: Path A General Agent for productivity today, AND open-source blueprint for studying Path B Custom Agent patterns
- Build strategy: Use Apps SDK for ChatGPT distribution today; watch MCP Apps Extension for cross-platform portability tomorrow

### Common Mistakes
- Confusing AAIF (the governance body) with the standards themselves (AAIF governs the standards; the standards create the portability)
- Misclassifying MCP primitives -- exposing "send email" as a Resource instead of a Tool means the agent can see the option but cannot execute it
- Thinking goose and Claude Code compete when they validate the same standards from different angles (Claude Code for productivity; goose for learning Custom Agent architecture)
- Ignoring AGENTS.md hierarchy -- not understanding that the nearest file takes precedence enables monorepo support where different subprojects have different conventions

### Connections
- **Builds on**: The Five Powers (Lesson 3) especially the "Act" power that MCP enables; the Two Paths Framework (Lesson 1) that goose bridges between General and Custom Agents
- **Leads to**: Digital FTE Business Strategy (Lesson 5) where AAIF standards ensure products are portable and sellable; the practical skills-building work in later chapters where students create MCP servers, AGENTS.md files, and Agent Skills
