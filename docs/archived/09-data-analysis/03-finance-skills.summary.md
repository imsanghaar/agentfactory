### Core Concept

Skills are **reusable intelligence**—packaged expertise that can be invoked repeatedly. For finance professionals, this means encoding YOUR domain knowledge (variance analysis methodology, transaction classification logic, reconciliation procedures) into Skills that become sellable components of a Digital FTE.

### Key Mental Models

- **Skill Anatomy**: Every skill has Persona (who it acts as), Logic (step-by-step reasoning), Context (what it needs to know), and Safety (guardrails and restrictions)
- **Expertise Packaging**: Your 10 years of variance analysis experience becomes a `variance-analyzer` skill that others can use
- **Skill Composition**: Complex workflows combine multiple skills—variance-analyzer feeds into narrative-generator for board reports
- **Digital FTE Components**: Skills are the building blocks of a Finance Digital FTE that handles end-to-end workflows

### Key Facts

- **Skill components**: name, description, persona, logic, context, safety
- **Finance skill examples**: `variance-analyzer`, `transaction-classifier`, `reconciliation-assistant`, `narrative-generator`
- **Safety guardrails always include**: Never auto-post to ledger, flag low-confidence outputs, explain reasoning for audit trail

### Critical Patterns

- **variance-analyzer skill**: Persona (Senior FP&A Analyst), Logic (identify >5% or >$10K variances → categorize favorable/unfavorable → trace root causes → generate audit-ready explanation), Safety (show methodology, flag assumptions, recommend human review for material variances)
- **transaction-classifier skill**: Persona (Experienced bookkeeper), Logic (analyze vendor/description → match to chart of accounts → consider historical patterns → provide confidence level), Safety (never auto-post, flag low-confidence, explain reasoning)
- Always include confidence levels in outputs so humans know when to scrutinize more carefully

### Common Mistakes

- Missing safety guardrails (every finance skill needs explicit restrictions)
- Overly generic persona ("financial expert" vs "Senior FP&A Analyst with M&A experience")
- Not referencing CLAUDE.md context (skills should use company-specific rules)
- Creating skills that auto-execute instead of suggest-and-wait-for-approval

### Connections

- **Builds on**: Chapter 3 Lessons 9-10 (Agent Skills, Skill Factory Pattern, skill-creator tool)
- **Leads to**: Composing skills with MCP connections, orchestrating skills through subagents, building Finance Digital FTE
