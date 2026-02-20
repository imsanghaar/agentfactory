---
title: "Connecting to Accounting Platforms"
sidebar_position: 7
chapter: 7
lesson: 7
duration_minutes: 20

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "MCP concepts from Chapter 3, Google Sheets MCP from Lesson 4"
layer_2_collaboration: "Designing platform-agnostic workflows through iterative refinement with Claude"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Applying MCP Patterns to Accounting Platform Design"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can explain how MCP patterns apply to accounting platform integration and identify the architectural components required"

  - name: "Designing Read-Only Access Patterns for Financial Systems"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can distinguish between safe read operations and risky write operations in financial contexts, and design access patterns that preserve ledger integrity"

  - name: "Creating Platform-Agnostic Financial Workflows"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can design workflows that separate reasoning from execution, working across Xero, QuickBooks, or spreadsheet-based systems"

learning_objectives:
  - objective: "Apply MCP patterns to conceptually design accounting platform integrations"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Explanation of how the MCP architecture from Lesson 4 extends to Xero, QuickBooks, or other accounting systems"
  - objective: "Design read-only access patterns that preserve ledger integrity"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Identification of which operations should be allowed, restricted, or prohibited in an accounting platform MCP"
  - objective: "Create platform-agnostic workflows that work across Xero, QuickBooks, or any system"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Design of a financial workflow that separates platform-specific execution from platform-independent reasoning"

# Cognitive load tracking
cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (accounting platform MCP patterns, read-only access by default, platform-agnostic design, safe integration patterns, API-first architecture benefits) - within B1 limit of 10"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Research actual Xero and QuickBooks API documentation to understand specific endpoints, OAuth flows, and rate limits for real implementation"
  remedial_for_struggling: "Focus on the conceptual architecture diagram and the safe access principles table; understand WHY read-only is critical before considering implementation details"

# Generation metadata
generated_by: "content-implementer"
source_spec: "prompt-based"
created: "2026-01-01"
last_modified: "2026-01-01"
git_author: "Claude Code"
workflow: "autonomous"
version: "1.0.0"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Chapter 3, Lessons 9-10: MCP Integration and Compiling MCP to Skills"
  - "Chapter 7, Lesson 4: Connecting to Google Sheets via MCP"
  - "Chapter 7, Lesson 6: AI-Native Accounting Workflows"
---

# Connecting to Accounting Platforms

Your accounting data lives in Xero, QuickBooks, or another platform. Your transaction history, chart of accounts, reconciliation status, and financial reports all reside inside a system with its own database, its own rules, and its own access controls.

In Lesson 4, you connected Claude Code to Google Sheets via MCP. You implemented the three-layer architecture: Claude for intelligence, Sheets for execution, human for governance. The formulas Claude generated executed deterministically in your spreadsheet, and you approved every change before it affected your data.

But spreadsheets are only one piece of the financial puzzle. The official ledger, the one auditors examine and tax authorities reference, typically lives in an accounting platform. What if Claude could connect to that system the same way it connects to Google Sheets?

This lesson explores that question conceptually. You'll learn the architectural pattern for connecting Claude to accounting platforms, understand why read-only access is the default for financial integrations, and design workflows that work regardless of which platform you use.

---

## The Architecture: Multiple Platform Connections

The MCP pattern you learned in Chapter 3 and applied to Google Sheets in Lesson 4 extends naturally to accounting platforms. The principle remains the same: Claude reasons, the platform executes, you govern.

```
                    ┌──────────────────┐
                    │   Claude Code    │
                    │ (Reasoning Layer)│
                    └────────┬─────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
    ┌──────▼─────┐    ┌──────▼─────┐    ┌──────▼─────┐
    │ Sheets MCP │    │  Xero MCP  │    │   QB MCP   │
    │  (Active)  │    │(Conceptual)│    │(Conceptual)│
    └──────┬─────┘    └──────┬─────┘    └──────┬─────┘
           │                 │                 │
    ┌──────▼─────┐    ┌──────▼─────┐    ┌──────▼─────┐
    │   Google   │    │    Xero    │    │ QuickBooks │
    │   Sheets   │    │  Ledger    │    │   Online   │
    └────────────┘    └────────────┘    └────────────┘
```

Notice what this architecture enables:

**Claude becomes a universal reasoning layer.** The same financial reasoning that interprets your intent for spreadsheet formulas can interpret your intent for any connected system. "Analyze my Q3 expenses by department" works whether the data lives in Sheets, Xero, or QuickBooks.

**Execution stays platform-specific.** Each MCP server translates Claude's requests into the specific API calls that platform requires. The Google Sheets MCP uses the Sheets API. A Xero MCP would use the Xero API. Claude doesn't need to know the details.

**Governance remains with you.** Regardless of which platform executes the request, you maintain approval authority over anything that changes your financial records.

---

## Why Read-Only Access by Default

When connecting Claude to spreadsheets in Lesson 4, you saw that Claude could both read and write data. You approved changes before they executed, maintaining governance.

For accounting platforms, the stakes are higher. Your general ledger is a legal document. Entries affect your tax liability, your financial statements, your audit trail. An error that's trivial to fix in a spreadsheet can be serious in an accounting system.

**The principle: Read-only access by default.**

This isn't a limitation of AI capability. It's a deliberate architectural choice that matches how finance professionals actually work.

### What Read-Only Enables

With read-only access to your accounting platform, Claude can:

- **Retrieve transaction history** for analysis
- **Query account balances** for variance reports
- **Fetch invoice details** for collections workflows
- **Access chart of accounts** for classification guidance
- **Pull reconciliation status** for audit preparation
- **Generate reports** based on actual ledger data

These capabilities cover the vast majority of what you'd want Claude to do with your accounting data. Analysis, interpretation, pattern recognition, anomaly detection, narrative generation, all require reading data, not modifying it.

### What Read-Only Prevents

With read-only access, Claude cannot:

- Post transactions to the ledger
- Modify historical entries
- Delete records
- Change account configurations
- Alter reconciliation status
- Modify vendor or customer records

This matters because these actions have immediate, real consequences. A posted transaction affects your trial balance. A modified historical entry creates audit complications. A deleted record may violate retention requirements.

---

## Safe Access Principles

When designing an accounting platform MCP, these principles guide what operations should be available:

| Access Type | Allow                                              | Restrict           |
| ----------- | -------------------------------------------------- | ------------------ |
| **Read**    | Chart of accounts, transactions, reports, balances | N/A                |
| **Write**   | Draft entries (pending approval)                   | Direct posting     |
| **Delete**  | Never                                              | Everything         |
| **Modify**  | Never without human approval                       | Historical entries |

### The Draft Pattern

Notice the distinction between writing and posting. A well-designed integration might allow Claude to create draft entries, entries that exist in a pending state but don't affect your ledger until you explicitly approve them.

This mirrors how many accounting platforms already work. You don't post journal entries directly; you create them, review them, and then post them. Claude can participate in the creation step while you retain exclusive control over posting.

**Example workflow:**

1. Claude analyzes transactions and suggests journal entries
2. Claude creates draft entries in the platform (via MCP)
3. You review drafts in your accounting platform's normal interface
4. You approve or reject each entry through the platform's approval workflow
5. Approved entries post to the ledger with your authorization on the audit trail

The audit trail shows your approval, not autonomous AI posting. This satisfies compliance requirements while still benefiting from AI assistance.

---

## Platform-Agnostic Workflow Design

Here's the powerful insight: if you design your workflows around the reasoning, not around the platform, you can work with any system.

### The Platform-Independent Pattern

Every financial workflow has two components:

**Reasoning (platform-independent):** What are we trying to accomplish? What decisions need to be made? What analysis is required?

**Execution (platform-specific):** How do we retrieve the data? How do we format the output? What API calls are needed?

When you separate these cleanly, the same reasoning works across platforms.

### Example: Vendor Invoice Processing

**The reasoning (same everywhere):**

1. Identify the vendor from the invoice
2. Match to existing vendor record or flag as new
3. Validate invoice against purchase order (if applicable)
4. Determine correct expense category
5. Check for duplicate invoices
6. Route for approval based on amount threshold
7. Create entry for posting (pending approval)

**The execution (platform-specific):**

| Step                | Google Sheets              | Xero                   | QuickBooks            |
| ------------------- | -------------------------- | ---------------------- | --------------------- |
| Vendor lookup       | VLOOKUP on vendor table    | GET /Contacts          | GET /vendors          |
| Duplicate check     | COUNTIF on invoice numbers | Query by InvoiceNumber | Query by DocNumber    |
| Category assignment | Match to category column   | Map to AccountCode     | Map to AccountRef     |
| Entry creation      | Append to journal tab      | POST /Invoices (draft) | POST /bills (pending) |

**What this means for you:** If you document your vendor invoice workflow as a reasoning process (the steps, the decisions, the validation rules), Claude can help you execute that workflow regardless of which platform stores your data.

---

## The Implementation Reality

This lesson presents the conceptual architecture for accounting platform integrations. Actual implementation requires additional technical work:

**API credentials and authentication.** Xero uses OAuth 2.0. QuickBooks Online uses OAuth 2.0. Both require registering an application, obtaining client credentials, and managing token refresh cycles.

**MCP server development.** While Google Sheets MCP exists as a ready-to-use server, accounting platform MCPs may require building custom servers that wrap the platform APIs.

**Rate limits and quotas.** Accounting platforms limit API calls per minute and per day. A production integration needs to handle these constraints gracefully.

**Error handling and recovery.** API calls fail. Network connections drop. A robust integration handles these scenarios without losing data or creating inconsistent states.

**Security and data protection.** Financial data requires careful handling. Access credentials, data in transit, and data at rest all need appropriate protection.

These implementation details are beyond the scope of this lesson, but understanding that they exist helps you evaluate the effort required for real integration versus the conceptual patterns you're learning here.

---

## API-First Architecture Benefits

Modern accounting platforms are built API-first, meaning their web interfaces use the same APIs that external integrations use. This creates opportunities:

**Feature parity.** Anything you can do in the web interface, you can potentially do via API. The platforms publish the same capabilities externally that they use internally.

**Real-time data.** API access gives you current data, not yesterday's export. When Claude queries your receivables aging, it gets the actual current state.

**Automation potential.** Workflows that currently require manual login, navigation, and data entry can potentially be automated through API calls (with appropriate governance).

**Integration ecosystem.** Platforms like Xero and QuickBooks have extensive app marketplaces. Understanding the API patterns helps you evaluate which third-party integrations might complement your Claude workflows.

### Current Platform API Capabilities

Both major platforms offer comprehensive APIs:

| Capability          | Xero API           | QuickBooks API     |
| ------------------- | ------------------ | ------------------ |
| Chart of accounts   | Full read/write    | Full read/write    |
| Transactions        | Full CRUD          | Full CRUD          |
| Invoices/Bills      | Full lifecycle     | Full lifecycle     |
| Contacts/Vendors    | Full CRUD          | Full CRUD          |
| Bank reconciliation | Read status, match | Read status, match |
| Reports             | Standard reports   | Standard reports   |

The APIs exist. The question is how to wrap them in MCP servers that maintain the governance principles you've learned throughout this chapter.

---

## Designing Your Integration Strategy

If you're considering real integration between Claude and your accounting platform, think through these questions:

**What data do you need to access?**
Start with read-only access to the specific data types that enable your highest-value workflows. Transaction history for variance analysis? Invoices for collections? Accounts for reconciliation support?

**What's your approval workflow?**
Even with read-only access to the accounting platform, you'll likely want Claude to create artifacts that eventually become ledger entries. Where do drafts live? Who approves them? How does the audit trail work?

**Who builds and maintains the integration?**
MCP server development requires engineering resources. Can you use existing servers? Do you need custom development? Who maintains the integration as platform APIs evolve?

**What's your fallback when the integration fails?**
APIs have downtime. Tokens expire. Rate limits trigger. When the real-time integration isn't available, what's your manual workflow?

---

## The Three-Layer Principle, Extended

Throughout this chapter, you've seen the three-layer architecture applied to different contexts:

- **Lesson 4:** Claude (intelligence) + Sheets (execution) + Human (governance)
- **Lesson 6:** Claude (reasoning) + Accounting System (recording) + Human (approval)
- **This lesson:** Claude (universal reasoning) + Any Platform (specific execution) + Human (final authority)

The pattern is consistent because the principle is fundamental: intelligence and execution serve different purposes and require different capabilities. Claude excels at reasoning about financial intent, interpreting context, and generating explanations. Accounting platforms excel at reliable data storage, deterministic computation, and audit trail maintenance.

Neither replaces the other. Together, governed by human judgment, they create workflows more capable than either alone.

---

## Try With AI

Explore platform-agnostic workflow design and safe access principles through these collaborative exercises.

**Prompt 1: Design a Platform-Agnostic Invoice Workflow**

```
Design a workflow for processing vendor invoices that works whether I use
Xero, QuickBooks, or just Google Sheets. What are the common steps that
don't depend on the platform? Where are the platform-specific decision
points? Show me the complete reasoning process, then indicate which
steps would need different execution based on the platform.
```

**What you're learning**: This prompt helps you identify the reasoning-versus-execution boundary in financial workflows. The vendor validation logic, approval thresholds, and categorization rules are platform-independent. The API calls, data formats, and posting mechanisms are platform-specific. Understanding this separation lets you document workflows that survive platform migrations.

**Prompt 2: Define Safe Access Boundaries**

```
What safeguards should an accounting platform MCP server have to ensure
Claude can read data but cannot accidentally modify the ledger? List
the specific restrictions for each operation type: read, create draft,
post/approve, modify historical, and delete. Explain why each restriction
matters for audit and compliance.
```

**What you're learning**: This prompt makes explicit the safety architecture that should govern any accounting integration. The restrictions aren't arbitrary limitations; they map to specific audit requirements and compliance controls. Understanding why each restriction exists helps you evaluate whether a proposed integration maintains appropriate governance.

**Prompt 3: Identify High-Value Read-Only Use Cases**

```
If I had read-only API access to my accounting system via MCP, what
analysis could Claude perform? Give me 5 high-value use cases that
don't require write access. For each, explain what data Claude would
read, what reasoning Claude would apply, and what output I'd receive.
```

**What you're learning**: This prompt demonstrates that read-only access unlocks enormous value without the risks of write access. Most of what you'd want an AI assistant to do with your accounting data involves reading, analyzing, and interpreting, not modifying the ledger. By starting with read-only use cases, you can prove value before taking on the governance complexity of write access.

Note: When discussing accounting platform integrations, you're designing conceptual architectures. Actual implementation requires careful attention to API credentials, data security, and your organization's policies for AI access to financial systems. Test conceptual workflows with sample data before considering production integration.
