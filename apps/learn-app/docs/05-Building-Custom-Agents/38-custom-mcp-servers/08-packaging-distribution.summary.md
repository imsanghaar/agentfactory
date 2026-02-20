### Core Concept
Package MCP servers for one-command installation. pyproject.toml defines metadata and entry points; uv build creates wheels; Claude Desktop config registers installed servers. Users run `pip install` and immediately use your server.

### Key Mental Models
- **Entry point pattern**: `[project.scripts]` creates CLI command from main() function
- **Package structure**: Directory name (underscores) must match project name (hyphens)
- **Wheel distribution**: .whl file contains code + manifest; faster to install than source
- **Claude Desktop integration**: Config file points to installed command, not source code

### Critical Patterns
- pyproject.toml sections: `[build-system]`, `[project]`, `[project.scripts]`, `dependencies`
- Entry point: `my-server = "my_server:main"` creates `my-server` command
- Build: `uv build` creates dist/*.whl
- Install: `uv pip install dist/*.whl`
- Claude Desktop: `~/.config/Claude/claude_desktop_config.json` with `{"mcpServers": {"name": {"command": "my-server"}}}`

### AI Collaboration Keys
- Entry point main() calls mcp.run() to start server
- Test with `which my-server` after installation to verify command exists
- Restart Claude Desktop after adding server to config

### Common Mistakes
- Directory name mismatch (my-server vs my_server)
- Missing main() function in __init__.py
- Not restarting Claude Desktop after config change

### Connections
- **Builds on**: Error Handling & Recovery (Lesson 7)
- **Leads to**: Capstone: Production MCP Server (Lesson 9)
