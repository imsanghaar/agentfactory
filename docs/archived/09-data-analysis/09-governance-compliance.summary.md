### Core Concept
Financial governance is a paradox: **when properly governed, AI increases safety rather than reducing it**. The same capabilities that could cause harm when uncontrolled become powerful safeguards when channeled through appropriate checkpoints. The core pattern: **AI proposes → Human reviews → System records → Ledger updates**. This separation preserves efficiency (AI handles volume) and control (human provides oversight).

### Key Mental Models
- **Propose, Don't Post**: AI does analytical heavy lifting (drafting, explaining); humans apply judgment and take accountability
- **Minimum Necessary Permissions**: Read-only by default, write actions require explicit approval per action
- **Audit Trail as Asset**: Every AI recommendation captures data analyzed, logic applied, alternatives considered, confidence level, limitations acknowledged
- **Materiality-Based Escalation**: Different approval tiers based on transaction size and impact

### Key Facts
- **Prohibited autonomous actions**: Post to ledger, override controls, make tax decisions, modify historical entries, approve payments, change account structures
- **Five core safeguards**: Human-in-the-loop approvals, read-only access default, logged reasoning outputs, versioned changes, role-based permissions
- **Materiality thresholds (example)**: Under $1K (auto-log), $1K-$10K (single approver), $10K-$100K (manager + controller), over $100K (CFO)
- **Data classification**: Chart of accounts (share), transaction descriptions (share), individual salaries (no), SSN/tax IDs (no), bank account numbers (no)

### Critical Patterns
- **Single-approval workflow**: Routine transactions → AI proposes → single approver reviews → audit log
- **Dual-approval workflow**: Material items → AI proposes → first approver → second approver → final authority
- **Batch-approval workflow**: High volume → AI proposes batch → random sample review → exceptions flagged individually
- **Governance skill pattern**: `finance-governance-checker` validates any workflow against human approval, no autonomous posting, reasoning logged, materiality flagging, tax review, historical protection, confidence levels

### Common Mistakes
- Giving AI write access to ledgers without approval checkpoints (the "overnight posting" anti-pattern)
- Skipping governance for "small" transactions (governance applies to all, thresholds determine escalation level)
- Not capturing AI reasoning in audit trail (auditors need complete decision chain)
- Assuming restricted permissions limit AI value (proper governance enables broader deployment, not narrower)

### Connections
- **Builds on**: All previous lessons (skills, MCP, subagents all need governance), Lesson 6 (AI-native accounting principles)
- **Leads to**: Capstone where governance becomes integration layer ensuring entire Finance Digital FTE operates safely
