### Core Concept
AI-native accounting applies the **"AI-assisted, human-governed"** model to accounting workflows. Claude reasons about transactions (classification, reconciliation, journal entries) and provides explanations; humans verify and approve before anything touches the ledger. The key principle: **Claude suggests, never posts**.

### Key Mental Models
- **Reasoning-Based Classification**: Unlike rules ("if vendor = AWS, category = Cloud"), Claude reasons ("AWS invoice for production infrastructure = operating expense, recurring, may need cost center allocation")
- **Explanation vs Execution Separation**: Claude explains what should happen and why; the accounting system executes only after human approval
- **Audit Trail by Design**: Every AI suggestion includes reasoning that becomes part of the audit documentation
- **Ledger Integrity**: The ledger is sacred. Claude can analyze it, suggest changes to it, but never modify it autonomously

### Key Facts
- **Core use cases** (from Claude_Xero.pdf): Transaction classification, bank reconciliation, journal entry generation, invoice processing, financial explanation
- **Separation of responsibilities**: Claude Code (reasoning, interpretation, classification) → Accounting System (recording, validation, compliance) → Human (approval, oversight, exceptions)
- **Quote**: "Unlike rule-based systems, Claude adapts to context and learns patterns"

### Critical Patterns
- **Transaction classification workflow**: Present transactions → Claude classifies with reasoning and confidence level → Human reviews → Human approves or corrects → Human posts to ledger
- **Reconciliation workflow**: Identify discrepancy → Claude systematically analyzes possible causes → Claude suggests reconciling entries with explanations → Human verifies and posts
- **Journal entry workflow**: Describe transaction → Claude generates entry with debits/credits and audit explanation → Human reviews accounting treatment → Human posts

### Common Mistakes
- Allowing any autonomous posting to ledgers (NEVER do this)
- Accepting classifications without reviewing reasoning (always check the "why")
- Skipping the human approval step for "small" transactions (governance applies to all)
- Not documenting AI-assisted decisions for audit trail (always capture the reasoning)

### Connections
- **Builds on**: Lesson 3 (finance Skills like transaction-classifier), Lesson 4-5 (MCP integration, intent-driven workflows)
- **Leads to**: Connecting to accounting platforms, governance and compliance frameworks, Finance Digital FTE capstone
