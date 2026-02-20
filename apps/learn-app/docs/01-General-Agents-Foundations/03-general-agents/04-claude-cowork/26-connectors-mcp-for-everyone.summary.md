# Lesson 26: Connectors - MCP for Everyone

## What Connectors Are

**Connectors = Pre-built MCP servers** for common services. No code required.

| Connector    | Data Source                             |
| ------------ | --------------------------------------- |
| Google Drive | Google Workspace (Docs, Sheets, Slides) |
| Notion       | Workspace pages and databases           |
| Slack        | Messages and conversations              |
| GitHub       | Repositories, issues, discussions       |
| Jira         | Tickets and project data                |
| Salesforce   | CRM accounts and opportunities          |

## MCP vs. Connectors

**MCP (Lesson 12)**: For developers building custom integrations

- Requires programming
- You design tools and data structures
- You host and maintain
- Full control

**Connectors**: For knowledge workers using common services

- No programming required
- Pre-defined tools
- Anthropic/partners maintain
- Optimized for popular services

## The Combination Power

Connectors shine when combined with local files:

**Example**: Quarterly report pulling from:

- Google Sheets (sales figures)
- Notion (product updates)
- Slack (customer feedback)
- Local files (previous quarter template)

One request does the work of accessing four systems.

## Available Connectors

**Documents/Knowledge**: Google Drive, Notion, Confluence, SharePoint
**Communication**: Slack, Teams, Gmail
**Development**: GitHub, GitLab, Linear
**Business Data**: Salesforce, HubSpot, Jira, Airtable

## Limitations

- Rate limits on external APIs
- Periodic re-authentication required
- Not all support read-write (some are read-only)
- Service availability affects Connector functionality
