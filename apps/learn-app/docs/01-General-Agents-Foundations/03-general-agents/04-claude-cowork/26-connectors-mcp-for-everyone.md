---
slug: /General-Agents-Foundations/general-agents/connectors-mcp-for-everyone
title: "Connectors: MCP for Everyone"
sidebar_position: 26
chapter: 3
lesson: 26
duration_minutes: 16
chapter_type: Concept
running_example_id: connectors-introduction

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Understanding Connectors as the Cowork interface to MCP (Model Context Protocol), enabling external data and service integration"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Claude Connectors and MCP Integration"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain what Connectors are, how they relate to MCP, and identify scenarios where external data integration would enhance Cowork workflows"

learning_objectives:
  - objective: "Understand what Connectors are and how they extend Cowork's capabilities"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explanation of Connectors as MCP interface for Cowork"
  - objective: "Distinguish between MCP (for developers) and Connectors (for knowledge workers)"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Comparison of MCP vs Connectors use cases"
  - objective: "Identify scenarios where Connectors enhance workflows"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Scenario analysis for appropriate Connector use"
  - objective: "Set up and use basic Connectors in Cowork"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful Connector configuration and first use"

# Cognitive load tracking
cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (Connectors, MCP relationship, data sources, authentication, external services, combination power) - within A2 limit of 7 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Explore how developers create new Connectors and the technical architecture of MCP server integration"
  remedial_for_struggling: "Focus on the key concept: Connectors bring external data into Cowork conversations"

# Generation metadata
generated_by: "content-implementer v2.0.0"
created: "2025-01-22"
last_modified: "2025-01-22"
git_author: "Claude Code"
workflow: "manual"
version: "1.0.0"

teaching_guide:
  lesson_type: "core"
  session_group: 9
  session_title: "External Integration and Responsible Use"
  key_points:
    - "Connectors are pre-packaged MCP servers maintained by Anthropic and partners — students do NOT write code to use them"
    - "The MCP-vs-Connectors distinction maps to developer-vs-knowledge-worker audiences, not different protocols"
    - "Combination power across multiple data sources (Google Sheets + Notion + Slack) is the real unlock, not single-source access"
    - "Principle of Least Privilege applies: start read-only, grant write access only for trusted workflows"
  misconceptions:
    - "Students think Connectors are a different technology from MCP — they are MCP servers someone else built and maintains"
    - "Students assume Connectors give real-time streaming data — they fetch current snapshots, not live streams"
    - "Students believe all Connectors support read-write — many are read-only, and write support varies by service"
  discussion_prompts:
    - "Which three data sources in your current work would save the most time if Claude could access them directly — and what task would you automate first?"
    - "What are the risks of granting an AI read-write access to your Google Drive or Slack, and how would you mitigate them?"
  teaching_tips:
    - "Walk through the quarterly report scenario in 'The Combination Power' section — have students map it to their own multi-source workflows"
    - "Use the MCP vs Connectors comparison table to reinforce that the difference is who builds and maintains the server, not the underlying protocol"
    - "Emphasize the 'Available Connectors' categories (Document, Communication, Development, Business Data) and ask students which category matters most for their role"
    - "Connect back to Lesson 12 (MCP) and Lesson 25 (browser integration) to show the progression: custom MCP → browser automation → pre-built Connectors"
  assessment_quick_check:
    - "Name two differences between MCP servers (Lesson 12) and Connectors (this lesson)."
    - "Why should you start with read-only Connector permissions?"
    - "Give one example where combining two Connectors in a single prompt creates value neither could alone."

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Completion of Lesson 12: MCP Integration (for context)"
  - "Completion of Lesson 25: Browser Integration"
  - "Claude Cowork installed and configured"
---

# Connectors: MCP for Everyone

You learned about MCP (Model Context Protocol) in Lesson 12—how developers create servers that expose tools to Claude Code. Connectors bring the same capability to Cowork, but without requiring any development work.

**Connectors are pre-built MCP integrations for knowledge workers.**

---

## What Connectors Are

MCP is a protocol that lets Claude interact with external data sources. Developers can build MCP servers that expose APIs, databases, and services as tools Claude can use.

**Connectors** are pre-packaged MCP servers that Anthropic and partners maintain for common services:

| Connector        | Data Source         | What It Provides                        |
| ---------------- | ------------------- | --------------------------------------- |
| **Google Drive** | Google Workspace    | Read, search, and modify documents      |
| **Notion**       | Notion workspace    | Access pages, databases, and docs       |
| **Slack**        | Slack workspace     | Read messages, search conversations     |
| **GitHub**       | GitHub repositories | Read code, issues, and discussions      |
| **Jira**         | Atlassian Jira      | Query tickets, update status            |
| **Salesforce**   | CRM data            | Access accounts, opportunities, reports |

You don't write code. You don't configure servers. You authenticate, grant permissions, and Claude can access the data.

---

## MCP vs. Connectors: What's the Difference?

**MCP (Lesson 12)** is for developers building custom integrations:

- Requires programming (Python, JavaScript, etc.)
- You design the tools and data structures
- You host and maintain the MCP server
- Full control over the integration
- Best for: proprietary data sources, custom APIs

**Connectors** are for knowledge workers using common services:

- No programming required
- Pre-defined tools and data structures
- Anthropic and partners handle maintenance
- Optimized for popular services
- Best for: widely-used SaaS platforms

**The relationship:** Connectors are MCP servers. Someone else built them, packaged them, and maintains them. You just use them.

---

## How Connectors Work

When you add a Connector to Cowork:

1. **Authentication**: You sign in to the external service (Google, Notion, etc.)
2. **Permission Grant**: You authorize what Claude can access
3. **Tool Registration**: The Connector exposes its capabilities as tools
4. **Querying**: Claude can now query, read, and sometimes modify data

From that point forward, Claude can reference data from the connected service alongside your local files.

**Example**: With the Google Drive Connector, you could ask:

> "Look at the project planning document in my Google Drive, compare it to the local project files I showed you, and tell me what's missing from the local version."

Claude reads the Google Doc via Connector, reads your local files, and performs the comparison—all without you manually copying anything.

---

## Setting Up Connectors

### Step 1: Open Connector Settings

In Claude Desktop (Cowork mode):

1. Click the settings/gear icon
2. Navigate to "Connectors" or "Integrations"
3. You'll see available Connectors

### Step 2: Add a Connector

1. Click "Add" next to the service you want to connect
2. A browser window opens for authentication
3. Sign in and authorize Claude's access
4. Return to Claude Desktop—connection confirmed

### Step 3: Configure Permissions

Each Connector has permission scopes:

- **Read-only**: Claude can view data but not modify
- **Read-write**: Claude can modify data (use with caution)
- **Specific resources**: Limit access to specific folders or workspaces

Start with read-only access. Only enable read-write when you trust the workflow and understand what Claude will do.

---

## The Combination Power

Connectors shine when combined with local file operations:

**Scenario**: You're preparing a quarterly report. The data lives in:

- Google Sheets (sales figures)
- Notion (product updates)
- Slack (customer feedback)
- Local files (previous quarter's report template)

**Without Connectors**: You download exports from each service, copy-paste into your document, and hope nothing changes.

**With Connectors**:

> "Create a quarterly report using the template in my local files. Pull sales figures from the Q4 Sales Google Sheet, include product updates from the Notion product database, summarize customer feedback from the #customers Slack channel, and compare everything to last quarter's performance."

Claude:

1. Reads the local report template
2. Queries Google Sheets for current sales data
3. Fetches Notion pages for product updates
4. Searches Slack for customer feedback
5. Analyzes everything and generates the report

**The advantage**: Live data, no manual export/import, and one request does the work of accessing four different systems.

---

## Available Connectors

**Document and Knowledge:**

- Google Drive (Docs, Sheets, Slides)
- Notion
- Confluence
- SharePoint

**Communication:**

- Slack
- Microsoft Teams
- Gmail

**Development:**

- GitHub
- GitLab
- Linear

**Business Data:**

- Salesforce
- HubSpot
- Jira
- Airtable

**New Connectors** are added regularly. The Connector marketplace shows all available integrations.

---

## Current Limitations

Connectors are powerful but have constraints:

**Rate Limits**: External APIs have usage limits. Claude queries efficiently, but massive data pulls may hit limits.

**Authentication**: Some services require re-authentication periodically. You'll be prompted when this happens.

**Read-only vs. Read-write**: Not all Connectors support modification. Check capabilities before planning write workflows.

**Service availability**: If the external service is down, the Connector won't work.

**Data freshness**: Connectors fetch current data, not real-time streams. Changes after Claude queries won't be reflected.

---

## When to Use Connectors

**Ideal for:**

- Reports combining data from multiple sources
- Research that spans across platforms
- Cross-reference analysis (e.g., GitHub issues vs. Jira tickets)
- Automated reporting from SaaS platforms

**Less ideal for:**

- Real-time monitoring (use dedicated dashboards)
- Massive data exports (use native export features)
- Complex data transformations (export, process locally)

---

## Privacy and Security

Connectors require granting Claude access to your external accounts. Consider:

**Principle of Least Privilege**: Grant only the access needed. Read-only for reporting, specific folders rather than entire workspaces.

**Regular Audits**: Periodically review which Connectors are active and revoke access you no longer need.

**Sensitive Data**: Be cautious connecting accounts with highly sensitive information (HR data, financial systems).

**Service Terms**: Ensure using Connectors complies with your organization's policies on external tool access.

---

## Try With AI

**🔍 Audit Your Data Sources:**

> "What services do I use regularly that contain data I reference in my work? Google Drive, Notion, Slack, GitHub, Jira? Which 3 services would be most valuable to connect to Claude Cowork?"

**What you're learning:** Data source inventory—understanding where your information lives and what would be valuable to integrate. This assessment guides which Connectors to prioritize.

\*\*💡 Design a Combined Workflow:"

> "Pick a task I do that involves data from multiple sources. Design a workflow that uses Connectors: What local files are involved? What external services? What would I ask Claude to do? Write the complete prompt."

**What you're learning:** Multi-source workflow design—thinking through how to combine local files with external data. This is where Connectors provide the most value.

\*\*🏗️ Test a Connector:"

> "Set up one Connector for a service I use (start with read-only). Test it with a simple query: 'Summarize the most recent documents/entries/messages from [service].' What did I learn?"

**What you're learning:** Hands-on Connector experience—moving from concept to practice. The best way to understand Connectors is to use them.

---

## What's Next

Connectors extend Cowork's reach to external data sources. But Cowork is still evolving. The next lesson covers current limitations, safety considerations, and what's coming in future updates—including Knowledge Bases that will give Claude persistent memory across sessions.
