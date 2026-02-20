### Core Concept

MCP (Model Context Protocol) servers connect Claude Code to external systems. For finance, **Google Sheets MCP** implements the three-layer architecture: Claude reasons about financial questions, Sheets performs deterministic computation, and humans govern the results. This separation ensures transparency, auditability, and reliability.

### Key Mental Models

- **Intelligence + Execution Separation**: Claude is the reasoning layer (interprets intent, designs models, explains results); Sheets is the execution layer (computes formulas, stores data, provides version history)
- **Intent → Formula → Result**: You express "model 15% monthly revenue growth," Claude generates the SUMIFS/VLOOKUP formulas, Sheets executes them deterministically
- **MCP as Bridge**: MCP servers are the connective tissue between Claude's reasoning and external system capabilities
- **Determinism Matters**: Spreadsheet formulas always produce the same output for the same input—critical for audit trails

### Key Facts

- **Google Sheets MCP capabilities**: Read cells/ranges, write to cells, create formulas, access multiple sheets, version history
- **Three-layer architecture** (from Agentic_Financial_Planning.pdf): Intelligence layer (AI) → Logic layer (Sheets) → Interface layer (Users)
- **Why Sheets**: Deterministic computation, transparency (human-readable formulas), collaboration (real-time multi-user), APIs (programmatic control via MCP), versioning (audit trail), accessibility (universal familiarity)

### Critical Patterns

- **Workflow**: User intent → Claude interprets and designs model → Claude generates formulas via MCP → Sheets executes → Claude interprets results → Human reviews and approves
- Always ask Claude to explain generated formulas before executing
- Use cell references explicitly ("put the result in cell B5") for traceability
- Version control spreadsheet changes through Sheets' built-in history

### Common Mistakes

- Letting Claude modify production spreadsheets without sandbox testing first
- Not understanding the formulas Claude generates (always ask for explanation)
- Assuming MCP connection means Claude can do everything (read-only is safer default)
- Forgetting that Sheets is the execution layer, not Claude (Claude reasons, Sheets computes)

### Connections

- **Builds on**: Chapter 3 Lessons 6-7 (MCP servers, external integration patterns)
- **Leads to**: Intent-driven financial modeling, connecting to accounting platforms via MCP, building complete Finance Digital FTE
