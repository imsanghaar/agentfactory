### Core Concept
An agent can be converted into a tool that another agent calls. This enables **manager-specialist architecture**: the manager orchestrates workflow while specialists execute their domains, producing better results than any single agent.

### Key Mental Models
- **Agents fit the tool interface**: Agent takes input → produces output; tools do the same
- **Manager orchestrates, specialists execute**: The manager doesn't solve problems—it delegates to experts
- **Composition over complexity**: Multiple focused specialists outperform one generalist trying to do everything

### Critical Patterns
- Convert agent to tool: `specialist.as_tool(tool_name="do_x", tool_description="...")`
- Use clear, action-oriented tool names (`analyze_financials`, `assess_risks`)
- Write custom_output_extractor to filter specialist output before passing to manager
- Pass multiple specialist tools to one manager: `Agent(..., tools=[tool1, tool2, tool3])`

### AI Collaboration Keys
- Let the manager coordinate the workflow—don't micromanage specialist calls
- Use extractors to prevent information overload from verbose specialists

### Common Mistakes
- Using handoffs when agents-as-tools is needed (manager loses control of multi-step synthesis)
- Using agents-as-tools when handoffs would suffice (linear routing becomes unnecessarily complex)
- Creating specialists that are too broad (defeats the purpose of specialization)

### Connections
- **Builds on**: Function tools and context (Lesson 2)
- **Leads to**: Handoffs and filtering (Lesson 4)
