### Core Concept
MCP client configuration defines which servers to launch, how to authenticate, and what parameters to pass. Configuration is JSON files in platform-specific locations—Claude Code uses `.claude/settings.json`, Claude Desktop uses global config, VS Code uses settings.

### Key Mental Models
- **Project vs global**: `.claude/settings.json` = project-specific (in git); global config = always available
- **Environment variable substitution**: `${VAR_NAME}` references secrets from shell environment
- **Server independence**: Each server is separate subprocess; client routes requests to appropriate server
- **Configuration structure**: `mcpServers` object with server name → command, args, env

### Critical Patterns
- Claude Code: `.claude/settings.json` in project root
- Claude Desktop: `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)
- Server config: `{"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": {"GITHUB_TOKEN": "${GITHUB_TOKEN}"}}`
- Never hardcode secrets: Use `${VAR_NAME}` syntax, store secrets in `.env` (not committed to git)

### AI Collaboration Keys
- Different projects can have different MCP servers configured
- Multi-server configs enable powerful workflows (filesystem + GitHub + database)
- Configuration files are safe to commit; secrets come from environment

### Common Mistakes
- Hardcoding secrets in configuration (compromises credentials forever if committed)
- Wrong configuration file location (client-specific paths)
- Forgetting to export environment variables before starting client

### Connections
- **Builds on**: Prompts: The User-Controlled Primitive (Lesson 5)
- **Leads to**: Using Community MCP Servers (Lesson 7)
