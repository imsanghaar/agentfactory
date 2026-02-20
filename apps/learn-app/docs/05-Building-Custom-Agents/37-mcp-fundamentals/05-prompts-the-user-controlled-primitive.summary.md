### Core Concept
Prompts are user-controlled instruction templates encoding domain expertise. Unlike tools (model decides) and resources (app decides), prompts let users explicitly select when to apply expert-crafted guidance—like slash commands capturing tacit knowledge.

### Key Mental Models
- **User-controlled**: Human consciously chooses when to apply template (vs autonomous tools/resources)
- **Expertise distribution**: Domain expert designs prompt once; thousands use it with consistent quality
- **Static vs dynamic**: Static prompts are fixed; dynamic prompts accept arguments for customization
- **Three control models**: Tools = LLM decides, Resources = App decides, Prompts = User decides

### Critical Patterns
- Discovery: `prompts/list` returns available prompts with name, description, arguments
- Retrieval: `prompts/get` with name and arguments returns ready-to-use message template
- Arguments: `{"name": "contract_type", "description": "...", "required": true}`
- FastMCP: `@mcp.prompt()` decorator with `Field()` descriptions for arguments

### AI Collaboration Keys
- Prompts capture tacit knowledge (how experts think about problems)
- Encode expertise into questions that guide systematic analysis
- Quality is consistent—expert creates once, users apply thousands of times

### Common Mistakes
- Using prompts for autonomous actions (that's what tools are for)
- Forgetting prompts are instruction templates, not computational functions
- Not testing prompts with edge cases before distribution

### Connections
- **Builds on**: Resources: The App-Controlled Primitive (Lesson 4)
- **Leads to**: Configuring MCP Clients (Lesson 6)
