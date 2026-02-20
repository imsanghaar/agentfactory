### Core Concept

MCP servers load ALL tool definitions at startup (5,000-8,000+ tokens each), creating token bloat. Pre-compiled skills reduce context consumption by 97-99% while preserving full functionality—SKILL.md (~150 tokens) + local script execution (0 tokens in context) replaces repeated tool definition loading.

### Key Mental Models

- **Token Bloat**: MCP eagerly loads everything; you're paying for tools you're not using. Agent with 1,000 tools = 150,000 tokens before first request. 2-hour workflow might waste 50,000+ tokens.
- **Code Execution Pattern**: Instead of calling MCP tools directly through Claude's context, compiled skills run scripts locally via bash—Claude orchestrates, `mcp-client.py` executes outside context.
- **Progressive Disclosure (3-Stage Loading)**: (1) Discovery—load description only (~30 tokens), (2) Activation—load full SKILL.md (~150 tokens), (3) Execution—run scripts locally (0 tokens).
- **Content-Type Filtering**: Skills like fetch-library-docs filter responses locally (setup, examples, api-ref), returning only relevant content for 60-90% additional savings.

### Critical Patterns

- Use pre-compiled skills from Skills Lab: `browsing-with-playwright`, `fetch-library-docs`
- Skills execute bash commands: `python mcp-client.py call -t browser_navigate ...`
- Scripts run OUTSIDE Claude's context—heavy operations consume zero tokens
- Content-type filtering: `--content-type setup` vs `--content-type examples` returns different filtered results
- Compare token usage: Direct MCP (~15,000-24,000 tokens) vs compiled skill (~150-250 tokens)

### Common Mistakes

- Using direct MCP for repeated workflows—token waste multiplies with each call
- Not specifying content-type when fetching docs—returns everything instead of filtered content
- Expecting to create skills in this lesson—skill creation is covered in advanced lessons
- Forgetting to start/stop the MCP server when using browsing-with-playwright

### Decision Framework

- **Use direct MCP**: One-off queries, low-token servers (&lt;1,500 tokens), rapidly-changing APIs, small well-formatted results
- **Use compiled skill**: Repeated workflows (3+ calls), high-token servers (5,000+), large datasets needing filtering, multi-step workflows, team sharing, privacy-sensitive data

### Connections

- **Builds on**: Skills (Lessons 08-09) for SKILL.md format and Skills Lab; MCP Integration (Lesson 12) for understanding MCP servers
- **Leads to**: Settings Hierarchy (Lesson 16) for configuration management; Advanced lessons for creating your own compiled skills
