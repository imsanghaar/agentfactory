### Core Concept
15-question assessment covering all 8 MCP Fundamentals lessons. Tests conceptual understanding (what MCP is, why it exists) and practical knowledge (configuration, debugging, three primitives). Mastery threshold: 14-15 for Chapter 38 readiness.

### Key Mental Models
- **Architecture recall**: Host-Client-Server, JSON-RPC 2.0, integration explosion O(n×m) → O(n+m)
- **Three control models**: Tools (model-controlled), Resources (app-controlled), Prompts (user-controlled)
- **Transport selection**: stdio for local/single-client; HTTP for remote/multi-client
- **Configuration syntax**: `${VAR_NAME}` for environment variable substitution

### Critical Patterns
- Quiz targets: MCP problem solved, control model distinctions, transport selection, configuration locations
- Multi-select questions test debugging patterns (stdout/stderr, env vars, process monitoring)
- Practical knowledge: Inspector usage, server evaluation criteria, multi-server composition
- Scoring: 14-15 = Mastery, 12-13 = Proficient, 10-11 = Competent, &lt;10 = Review needed

### AI Collaboration Keys
- Use quiz to identify weak areas before building MCP servers
- Focus on control model distinction (tools/resources/prompts)—most frequently confused
- Review transport debugging if scoring low on Lessons 2 and 8

### Common Mistakes
- Confusing who controls each primitive (model vs app vs user)
- Mixing up stdio vs HTTP debugging approaches
- Forgetting environment variable syntax (`${VAR}` not `$VAR`)

### Connections
- **Builds on**: Debugging and Troubleshooting (Lesson 8)
- **Leads to**: Chapter 38 (Building MCP Servers with FastMCP)
