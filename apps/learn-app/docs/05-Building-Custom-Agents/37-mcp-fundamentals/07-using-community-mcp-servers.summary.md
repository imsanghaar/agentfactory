### Core Concept
The MCP ecosystem has official servers (Anthropic/Linux Foundation maintained), community servers (developer-created), and enterprise servers (company-maintained). Evaluate quality and security before use; combine multiple servers for powerful multi-service workflows.

### Key Mental Models
- **Trust tiers**: Official (highest trust) → Enterprise (company accountability) → Community (evaluate carefully)
- **Evaluation criteria**: Maintenance activity, security review, documentation quality, community adoption
- **Installation methods**: npx for Node.js (`npx -y @modelcontextprotocol/server-github`), uvx for Python (`uvx mcp-sqlite`)
- **Tool routing**: Agent sees ALL tools from ALL connected servers; client routes to correct server automatically

### Critical Patterns
- Official registry: registry.modelcontextprotocol.io for canonical server discovery
- GitHub server: requires `GITHUB_TOKEN` with `repo`, `read:org` scopes
- Multi-server config: filesystem + GitHub + SQLite + Brave Search = unified development environment
- Security checklist: Last commit date, open issues, permissions required, code transparency

### AI Collaboration Keys
- Start with official servers (filesystem, GitHub, fetch) before community
- Combine servers for complex workflows (search → create issue → update database)
- Each server is independent—agent requests capabilities, client routes to right server

### Common Mistakes
- Installing community servers without evaluation (security risk)
- Granting excessive permissions (violates least privilege)
- Using abandoned servers (no security updates)

### Connections
- **Builds on**: Configuring MCP Clients (Lesson 6)
- **Leads to**: Debugging and Troubleshooting (Lesson 8)
