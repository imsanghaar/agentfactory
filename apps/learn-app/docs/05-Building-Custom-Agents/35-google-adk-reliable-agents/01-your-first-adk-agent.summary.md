### Core Concept
Google ADK uses declarative agent design—you specify agent properties (name, instructions, tools) through configuration, and ADK handles orchestration. This separates agent definition from execution, making agents reusable across environments.

### Key Mental Models
- **Declarative vs Imperative**: OpenAI SDK = code orchestrates execution; ADK = config specifies agent
- **Agent → CLI → Execution**: Define agent once, run with `adk run` or `adk web`
- **Events tab transparency**: See exactly what the agent decided and why

### Critical Patterns
- Install: `pip install google-adk`
- Scaffold: `adk create --type=code my_agent`
- Define agent: `Agent(name, model, instruction, tools=[google_search])`
- Run terminal: `adk run agent.py`
- Run web UI: `adk web` → Events tab for debugging

### AI Collaboration Keys
- Use `adk web` Events tab to understand agent reasoning—invaluable for debugging
- Declarative config separates developer concerns (define) from operator concerns (run)

### Common Mistakes
- Importing from wrong module (`google.genai.tools` instead of `google.adk.tools`)
- Missing `.env` file with `GOOGLE_API_KEY`
- Expecting instant responses (network latency compounds across tool calls)

### Connections
- **Builds on**: OpenAI SDK patterns from Chapter 34 (for comparison)
- **Leads to**: Custom Function Tools (Lesson 2)
