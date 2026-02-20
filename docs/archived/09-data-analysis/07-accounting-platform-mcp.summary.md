### Core Concept
Just as Google Sheets connects via MCP, accounting platforms (Xero, QuickBooks, etc.) can connect via MCP servers—enabling Claude to reason about your actual financial data. The key principle: **read-only access by default**, with write operations requiring explicit human approval through the platform's native controls.

### Key Mental Models
- **Platform-Agnostic Design**: Build workflows that work regardless of whether you use Xero, QuickBooks, or just Google Sheets. The reasoning layer (Claude) stays the same; only the execution layer changes
- **Read-Only Safety**: Claude should be able to read chart of accounts, transactions, and reports—but never write directly to the ledger
- **API-First Architecture**: Modern accounting platforms expose APIs; MCP servers bridge those APIs to Claude's reasoning capabilities
- **Conceptual vs Implementation**: This lesson teaches the PATTERN; actual MCP server setup for specific platforms may require technical implementation

### Key Facts
- **Safe access principles**: Read (chart of accounts, transactions, reports) = Allow; Write (draft entries pending approval) = Allow with governance; Delete = Never; Modify historical = Never
- **Platform capabilities via MCP**: Read transactions, access chart of accounts, generate reports, create draft entries (pending approval), query balances
- **Architecture**: Claude Code (reasoning) → Platform MCP (bridge) → Xero/QuickBooks/Sheets (execution)

### Critical Patterns
- Design workflows as platform-agnostic: "Classify these transactions" works the same whether data comes from Xero or QuickBooks
- Always implement read-only access first; add write capabilities only with explicit governance
- Use platform's native approval workflows for any entries Claude suggests
- Test with exported data before connecting to live accounting system

### Common Mistakes
- Giving Claude write access to production accounting systems without governance layer
- Assuming MCP connection means full platform control (always scope to minimum necessary access)
- Building platform-specific workflows when platform-agnostic patterns would work
- Skipping the conceptual design phase and jumping to implementation

### Connections
- **Builds on**: Lesson 4 (Google Sheets MCP as reference implementation), Lesson 6 (AI-native accounting workflows)
- **Leads to**: Finance subagents that orchestrate across multiple data sources, complete Finance Digital FTE with full system integration
