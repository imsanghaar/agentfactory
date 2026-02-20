### Core Concept
AgentTool wraps agents as callable tools, letting coordinators invoke specialists while maintaining control. Unlike OpenAI handoffs (control transfer), ADK AgentTool keeps coordinator in charge of workflow. Pydantic schemas enforce structured output across the system.

### Key Mental Models
- **Coordinator stays in control**: Call specialist → get result → decide next step
- **AgentTool vs Handoff**: ADK = tool invocation (returns result); OpenAI = control transfer (loses visibility)
- **Pydantic = type safety**: Schemas validate outputs, prevent free-form text ambiguity

### Critical Patterns
- Wrap specialist: `AgentTool(agent=specialist_agent)`
- Define schema: `class AINewsReport(BaseModel): stories: List[NewsStory]`
- Enforce output: `Agent(output_schema=AINewsReport)`
- Graceful degradation: `Field(default="N/A")` for missing data

### AI Collaboration Keys
- Each specialist owns one domain (focused instructions, specific tools)
- Coordinator combines outputs and handles failures

### Common Mistakes
- Using OpenAI handoff pattern in ADK (loses coordinator control)
- Halting workflow on component failure (use placeholders instead)
- Missing Pydantic schemas (free-form text causes parsing issues)

### Connections
- **Builds on**: Callbacks & Guardrails (Lesson 5)
- **Leads to**: Workflow Agents (Lesson 7)
