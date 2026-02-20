### Core Concept
Claude Agent SDK provides 9 battle-tested tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch, Task. Tool selection follows "deny by default" principle—grant only what's necessary.

### Key Mental Models
- **Read-only vs Modification**: Read/Glob/Grep/WebSearch/WebFetch safe; Write/Edit/Bash dangerous
- **Bash is most dangerous**: Can delete files, access system, exfiltrate data
- **Task for orchestration**: Spawn subagents with reduced tool access

### Critical Patterns
- Read-only agent: `allowed_tools=["Read", "Glob", "Grep"]`
- Development agent: `["Read", "Write", "Edit", "Bash"]` + hooks to block dangerous patterns
- Research agent: `["WebSearch", "WebFetch"]` only—no local file access
- Parallel subagents via Task: each with minimal necessary tools

### AI Collaboration Keys
- Block dangerous Bash patterns: `rm -rf`, `sudo`, `curl | bash`
- Protect sensitive paths: `/etc/`, `/.aws/`, `/.ssh/`

### Common Mistakes
- Granting Bash without restriction hooks
- Not using Task to reduce subagent scope
- Allowing Write to system directories

### Connections
- **Builds on**: First Agent with query() (Lesson 2)
- **Leads to**: Permission Modes and Security (Lesson 4)
