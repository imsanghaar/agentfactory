### Core Concept

CLAUDE.md provides persistent context so Claude understands your finance domain without re-explaining every session. For finance, this means encoding your **chart of accounts, fiscal year, accounting policies, and governance rules** as AI context—transforming generic Claude Code into YOUR company's financial reasoning engine.

### Key Mental Models

- **Context as Configuration**: CLAUDE.md is like configuring an ERP system—you define the rules once, and every interaction respects them
- **Domain Knowledge Transfer**: Instead of explaining "we use FIFO for inventory" every time, encode it once and Claude applies it automatically
- **Permission Hierarchy**: Read-only by default for financial data. Claude can analyze but never modify without explicit approval
- **Sandbox vs Production**: Always test AI-assisted workflows in sandbox environments before touching real financial data

### Key Facts

- **CLAUDE.md sections for finance**: Company Profile (fiscal year, currency, jurisdiction), Chart of Accounts (account ranges), Accounting Policies (revenue recognition, depreciation, inventory), Governance Rules (approval thresholds, restrictions)
- **Data classification**: Share aggregated financials, chart of accounts, transaction descriptions. Restrict SSN/Tax IDs, bank account numbers, individual salaries, raw customer PII

### Critical Patterns

- Structure CLAUDE.md with clear sections: Company Profile → Chart of Accounts → Accounting Policies → Governance Rules
- Include materiality thresholds ("flag transactions > $10,000 for review")
- Encode compliance boundaries ("never modify historical transactions")
- Reference CLAUDE.md in prompts: "Given my CLAUDE.md context, classify this transaction..."

### Common Mistakes

- Forgetting to include fiscal year (causes date-based calculations to fail)
- Missing governance rules (Claude won't know approval requirements)
- Sharing sensitive data without classification (SSN, bank accounts should never be in context)
- Using production data for testing (always sandbox first)

### Connections

- **Builds on**: Chapter 3 Lesson 8 (CLAUDE.md context files), Chapter 7 Lesson 1 (Financial Reasoning Engine concept)
- **Leads to**: Creating finance Skills that reference CLAUDE.md context, MCP connections to external systems
