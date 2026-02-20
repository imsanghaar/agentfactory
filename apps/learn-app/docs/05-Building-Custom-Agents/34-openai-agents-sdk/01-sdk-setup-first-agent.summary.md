### Core Concept
Every agent follows a three-part pattern: **Agent** (what it is) → **Runner** (execute it) → **Result** (extract output). This pattern underlies everything else in agent development.

### Key Mental Models
- **Agent → Runner → Result**: Define, execute, extract—the fundamental execution loop
- **Instructions = Behavior**: Clear instructions produce reliable agents; vague instructions create unpredictable behavior
- **Tools Are Functions**: If you can write a Python function, you can create an agent

### Critical Patterns
- Install with `pip install openai-agents` and verify with `pip show openai-agents`
- Set API key via environment variable: `export OPENAI_API_KEY=sk-proj-...`
- Create agent: `Agent(name="...", instructions="...")`
- Execute: `result = Runner.run_sync(agent, "user input")`
- Extract: `print(result.final_output)`
- Use LiteLLM for free alternatives: `pip install "openai-agents[litellm]"` and `set_tracing_disabled(True)` for non-OpenAI models

### Common Mistakes
- Hardcoding API keys in source code (use environment variables)
- Using vague instructions ("Be helpful") instead of specific persona and responsibilities
- Forgetting `set_tracing_disabled(True)` when using LiteLLM with non-OpenAI models

### Connections
- **Builds on**: Agent concepts from Chapter 33 (reasoning-action-observation loop)
- **Leads to**: Function tools and context objects (Lesson 2)
