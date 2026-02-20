---
sidebar_position: 1
title: "SDK Setup & First Agent"
description: "Install OpenAI Agents SDK and build your first autonomous agent"
keywords: [openai-agents-sdk, agent, installation, alternative-providers, runner]
chapter: 34
lesson: 1
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "SDK Installation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can successfully install the OpenAI Agents SDK, configure environment variables, and verify the installation works"

  - name: "Agent Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can create an Agent instance with name, instructions, and model parameters, then execute it using Runner.run_sync()"

  - name: "Alternative Model Providers"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can configure OpenAIChatCompletionsModel to use alternative model providers (Gemini, Ollama) with the OpenAI Agents SDK"

  - name: "Response Interpretation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can explain what result.final_output contains and describe the agent execution loop"

  - name: "API Key Security"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student stores API keys in environment variables, never hardcodes them, and understands why this matters"

  - name: "Tracing Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can enable or disable tracing for different model providers using set_tracing_disabled()"

learning_objectives:
  - objective: "Install and configure OpenAI Agents SDK with environment variables"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful SDK installation and API key configuration verified by running hello world agent"

  - objective: "Run a basic agent using Runner.run_sync()"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Agent produces valid response to a simple prompt"

  - objective: "Configure OpenAIChatCompletionsModel for alternative model providers"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Agent successfully runs with Gemini or another non-OpenAI model"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (SDK installation, Agent class, Runner, final_output, OpenAIChatCompletionsModel, tracing) at B1 level - within cognitive limits for intermediate learners"

differentiation:
  extension_for_advanced: "Experiment with multiple alternative providers in sequence, compare response quality and latency"
  remedial_for_struggling: "Focus on OpenAI-only setup first, add alternative provider integration after confirming basic agent works"
---

# SDK Setup & First Agent

What if you could build an AI employee that works 24/7, never calls in sick, and costs a fraction of a human salary? That's not science fiction---it's what you'll build in this chapter using OpenAI's Agents SDK.

In Chapter 33, you learned the conceptual foundation: what agents are, how they reason, and why they're transforming software development. Now you transition from understanding to building. This lesson is the foundation for everything that follows---your first step in the **BUILD** phase of creating Digital FTEs (Digital Full-Time Equivalents).

The OpenAI Agents SDK was released in March 2025 as a lightweight, production-ready framework for building agentic applications. Unlike wrapper libraries, it's the same infrastructure OpenAI uses internally. By the end of this lesson, you'll have a working agent responding to prompts---the "Hello World" moment that unlocks everything else in this chapter.

## Installing the SDK

The OpenAI Agents SDK requires Python 3.10 or later. Let's verify your environment and install the package.

First, check your Python version:

```bash
python --version
```

**Output:**
```
Python 3.12.4
```

If your version is below 3.10, install a newer Python version before proceeding.

### Setting Up Your Project with uv

We'll use **uv**, the modern Python package manager that's 10-100x faster than pip and handles virtual environments automatically.

First, install uv if you haven't already:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Now create your project directory and initialize it:

```bash
mkdir support-desk-agent
cd support-desk-agent
uv init --python 3.12
```

**Output:**
```
Initialized project `support-desk-agent`
```

Add the OpenAI Agents SDK and dependencies:

```bash
uv add openai-agents python-dotenv
```

**Output:**
```
Resolved 12 packages in 0.8s
Prepared 12 packages in 1.2s
Installed 12 packages in 45ms
 + openai-agents==0.1.2
 + openai==1.68.2
 + python-dotenv==1.0.1
 + pydantic==2.10.0
 ...
```

Your project structure now looks like this:

```
support-desk-agent/
├── .venv/              # Virtual environment (auto-created)
├── .python-version     # Python version lock
├── pyproject.toml      # Project configuration
└── main.py             # Your code goes here
```

The SDK comes with everything you need to build agents with OpenAI models. Later in this lesson, you'll learn how to use alternative providers like Google Gemini.

## Configuring Your API Key

The SDK needs an API key to authenticate with OpenAI. **Never hardcode API keys in your code**---always use environment variables.

This section covers all major platforms so you can set up your environment regardless of your operating system.

### Getting Your API Key

1. Visit [platform.openai.com](https://platform.openai.com)
2. Sign in or create an account
3. Navigate to **API Keys** in the left sidebar
4. Click **Create new secret key**
5. Copy the key immediately (you won't see it again)

:::warning Never Commit API Keys
API keys are sensitive credentials. If someone obtains your key:
- They can use your account and you pay for their usage
- They could run up thousands of dollars in charges
- OpenAI may revoke your key, breaking your application

Always use environment variables and never commit `.env` files to git.
:::

### Windows (PowerShell)

For **temporary** configuration (current session only):

```powershell
$env:OPENAI_API_KEY = "sk-your-key-here"
```

For **permanent** configuration (persists across sessions):

```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-your-key-here", "User")
```

Verify it's set:

```powershell
echo $env:OPENAI_API_KEY
```

**Output:**
```
sk-your-key-here
```

:::note Restart Required for Permanent Variables
After setting a permanent environment variable, you need to restart PowerShell (or your terminal) for the change to take effect in new sessions.
:::

### Windows (Command Prompt)

For **temporary** configuration (current session only):

```cmd
set OPENAI_API_KEY=sk-your-key-here
```

For **permanent** configuration (persists across sessions):

```cmd
setx OPENAI_API_KEY "sk-your-key-here"
```

**Output:**
```
SUCCESS: Specified value was saved.
```

Verify in a **new** Command Prompt window:

```cmd
echo %OPENAI_API_KEY%
```

### macOS/Linux (Bash)

For **temporary** configuration (current session only):

```bash
export OPENAI_API_KEY="sk-your-key-here"
```

For **permanent** configuration, add to your shell profile:

**For Bash users** (`~/.bashrc`):

```bash
echo 'export OPENAI_API_KEY="sk-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**For Zsh users** (`~/.zshrc`):

```bash
echo 'export OPENAI_API_KEY="sk-your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

Verify it's set:

```bash
echo $OPENAI_API_KEY
```

**Output:**
```
sk-your-key-here
```

### Using a .env File (Recommended for Projects)

For project-based configuration, use a `.env` file with `python-dotenv`:

```bash
pip install python-dotenv
```

Create a `.env` file in your project root:

```bash
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

**Add `.env` to your `.gitignore` immediately:**

```bash
echo ".env" >> .gitignore
```

In your Python code, load the environment variables:

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")
print(f"API key loaded: {api_key[:10]}...")  # Only show first 10 chars
```

**Output:**
```
API key loaded: sk-your-ke...
```

**Why environment variables?** If you commit code with hardcoded API keys:
1. Anyone who sees your repository gains access to your account
2. You pay for their usage---potentially thousands of dollars
3. OpenAI may revoke your key, breaking your application

Environment variables keep secrets separate from code. Your code runs on any machine with the key configured, without modification.

## Your First Agent: Hello World

Let's create your first agent. This is the simplest possible example---an agent with a name, instructions, and a basic conversation.

Create a file called `hello_agent.py`:

```python
from agents import Agent, Runner

# Create an agent with a name and instructions
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant who gives brief, friendly responses."
)

# Run the agent synchronously (blocking until complete)
result = Runner.run_sync(agent, "Hello! What can you help me with today?")

# Print the agent's response
print(result.final_output)
```

Run the script:

```bash
python hello_agent.py
```

**Output:**
```
Hello! I can help you with a wide range of tasks like answering questions, writing text, explaining concepts, brainstorming ideas, or working through problems. What would you like to explore?
```

Congratulations---you've built your first AI agent. Let's understand what each part does.

## Understanding the Response

### The Agent Class

```python
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant who gives brief, friendly responses."
)
```

The `Agent` class is the core primitive. It represents an AI entity with:

| Parameter | Purpose |
|-----------|---------|
| `name` | Identifies the agent in logs and multi-agent systems |
| `instructions` | The system prompt that shapes behavior |
| `model` | The LLM to use (defaults to `gpt-4o`) |
| `tools` | Functions the agent can call (we'll add these in Lesson 2) |
| `handoffs` | Other agents this agent can transfer control to (Lesson 4) |

The `instructions` parameter is crucial. It's your specification for how the agent should behave. Clear, specific instructions produce better results than vague ones---this is where your specification skills from Part 4 pay off.

### The Runner Class

```python
result = Runner.run_sync(agent, "Hello! What can you help me with today?")
```

The `Runner` executes the agent loop. It:
1. Sends your message to the LLM
2. Receives the response
3. If the LLM requests a tool call, executes it and sends results back
4. Repeats until the LLM produces a final response

`Runner.run_sync()` is the synchronous version---it blocks until the agent finishes. For web applications or handling multiple users, you'll use `Runner.run()` (async) instead.

### The Result Object

```python
print(result.final_output)
```

The `result` object contains everything about the agent's execution:

| Attribute | Contents |
|-----------|----------|
| `final_output` | The agent's final text response |
| `last_agent` | Which agent produced the response (important for multi-agent systems) |
| `input` | Your original input message |
| `new_items` | All messages generated during execution |

For a simple conversation, `final_output` is usually what you need. As your agents become more complex with tools and handoffs, you'll use other attributes to understand what happened.

## Running with Different Models

By default, the SDK uses `gpt-4o`. You can specify a different OpenAI model:

```python
from agents import Agent, Runner

agent = Agent(
    name="Fast Assistant",
    instructions="You are a quick helper.",
    model="gpt-4o-mini"  # Faster, cheaper model
)

result = Runner.run_sync(agent, "What's 2 + 2?")
print(result.final_output)
```

**Output:**
```
2 + 2 equals 4.
```

The `gpt-4o-mini` model is faster and cheaper than `gpt-4o`, making it ideal for simple tasks. For complex reasoning, stick with `gpt-4o` or newer models.

## Using Alternative Model Providers

What if you want to use Google's Gemini, a local Ollama model, or another provider? The SDK supports this through `OpenAIChatCompletionsModel`, which connects to any provider with an OpenAI-compatible API.

### Using Google Gemini

Google provides an OpenAI-compatible endpoint for Gemini models. Here's how to use it:

First, set your Gemini API key:

**macOS/Linux:**
```bash
export GEMINI_API_KEY="your-gemini-key-here"
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY = "your-gemini-key-here"
```

Then create an agent with Gemini:

```python
import os
import openai
from agents import Agent, Runner, set_tracing_disabled
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel

# Disable OpenAI tracing when using non-OpenAI models
set_tracing_disabled(True)

# Create an OpenAI client pointing to Google's endpoint
gemini_client = openai.OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Create a model using Gemini
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client
)

agent = Agent(
    name="Gemini Assistant",
    instructions="You are a helpful assistant. Keep responses concise.",
    model=gemini_model
)

result = Runner.run_sync(agent, "Explain what an AI agent is in one sentence.")
print(result.final_output)
```

**Output:**
```
An AI agent is an autonomous system that perceives its environment and takes actions to achieve specific goals.
```

### Using Local Models with Ollama

For privacy-sensitive applications or offline development, you can run models locally using Ollama:

First, ensure Ollama is running with a model:

```bash
ollama run llama3.2
```

Then configure your agent:

```python
import openai
from agents import Agent, Runner, set_tracing_disabled
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel

# Disable tracing for non-OpenAI models
set_tracing_disabled(True)

# Create a client pointing to Ollama's local endpoint
ollama_client = openai.OpenAI(
    api_key="ollama",  # Ollama doesn't require a real key
    base_url="http://localhost:11434/v1"
)

# Create a model using local Llama
local_model = OpenAIChatCompletionsModel(
    model="llama3.2",
    openai_client=ollama_client
)

agent = Agent(
    name="Local Assistant",
    instructions="You are a helpful assistant running locally.",
    model=local_model
)

result = Runner.run_sync(agent, "What's the capital of France?")
print(result.final_output)
```

**Output:**
```
The capital of France is Paris.
```

### Why Disable Tracing for Non-OpenAI Models?

You may have noticed `set_tracing_disabled(True)` in the examples. Here's why:

```python
from agents import set_tracing_disabled

# Disable tracing when not using OpenAI
set_tracing_disabled(True)
```

The SDK includes built-in tracing that sends execution data to OpenAI's dashboard. This is valuable for debugging OpenAI-powered agents, but:

1. **It doesn't work with non-OpenAI models** (no dashboard access)
2. **It adds latency** for no benefit
3. **It may fail** if the tracing endpoint isn't accessible

When you return to using OpenAI models, you can re-enable tracing:

```python
set_tracing_disabled(False)
```

Tracing provides valuable observability---you'll learn more about it in Lesson 8 when we cover debugging production agents.

## Common Issues and Solutions

| Problem | Cause | Solution |
|---------|-------|----------|
| `AuthenticationError` | Invalid or missing API key | Verify your API key is set correctly in environment variables |
| `ModuleNotFoundError: agents` | SDK not installed | Run `uv add openai-agents` in your project |
| `RateLimitError` | Too many requests | Add delays between calls or upgrade API tier |
| `ModelNotFoundError` | Invalid model name | Check spelling and ensure model exists |
| `TimeoutError` | Model taking too long | Use a faster model or increase timeout |
| `Connection refused` (Ollama) | Ollama not running | Start Ollama with `ollama serve` |

## Progressive Project: Support Desk Assistant

Throughout this chapter, you'll build a complete **Support Desk Assistant**---a production-ready Digital FTE that handles customer inquiries. Each lesson adds new capabilities to the same project, so by the end, you'll have a sellable AI agent.

**What you'll build across all lessons:**

| Lesson | Capability Added | Your Agent Can... |
|--------|------------------|-------------------|
| L01 | Basic agent | Greet customers and answer simple questions |
| L02 | Function tools | Create tickets, look up order status |
| L03 | Sub-agents | Delegate to research and writing specialists |
| L04 | Handoffs | Route to billing, technical, or sales teams |
| L05 | Guardrails | Block inappropriate requests, detect PII |
| L06 | Sessions | Remember conversation history across turns |
| L07 | Tracing | Monitor performance and debug issues |
| L08 | MCP | Look up documentation via external tools |
| L09 | RAG | Answer questions from your knowledge base |
| L10 | Production | Complete system ready for deployment |

### Build the Foundation

Now it's your turn. Using the patterns you learned above, create a **Support Desk Agent** for a fictional company called "TechCorp."

**Step 1: Create the project file**

Create a new file called `support_desk.py` in your project folder.

**Step 2: Import the SDK**

At the top of your file, import `Agent` and `Runner` from the `agents` package---just like you saw in the [Your First Agent](#your-first-agent-hello-world) section.

**Step 3: Create your agent**

Use the `Agent()` constructor with these requirements:
- **name**: Give it a professional name like `"SupportDesk"`
- **instructions**: Write instructions that tell the agent to:
  - Greet customers warmly
  - Answer questions about TechCorp's products (make up 2-3 products)
  - Be helpful and empathetic
  - Ask if there's anything else it can help with

Look back at the examples earlier in this lesson to see how instructions are formatted.

**Step 4: Run the agent**

Use `Runner.run_sync()` to send a test message to your agent and print the response. Refer to the [Running with Different Models](#running-with-different-models) section if you need a reminder.

**Step 5: Test with multiple queries**

Create a list of test customer queries and run each one through your agent:
- A product question
- A troubleshooting request
- A general inquiry

### Success Criteria

Your agent should:
- ✅ Greet customers professionally
- ✅ Know about your fictional company's products
- ✅ Provide helpful responses to different query types
- ✅ Maintain a consistent, friendly tone

### Stuck? Check Your Work

Compare your structure to the Hello World example from earlier:

```python
# Your code should follow this pattern:
from agents import Agent, Runner

agent = Agent(
    name="...",           # Your agent's name
    instructions="..."    # Your custom instructions
)

result = Runner.run_sync(agent, "Your test message")
print(result.final_output)
```

Run your agent with:

```bash
uv run python support_desk.py
```

### What's Next

Your agent currently can only talk---it can't actually DO anything. In Lesson 2, you'll add **function tools** that let it:
- Create support tickets in your system
- Look up real order status
- Check account information

Save your `support_desk.py` file---you'll extend it in every lesson!

## Try With AI

Now that you have a working agent, use your AI companion (Claude Code, ChatGPT, or similar) to explore further.

### Prompt 1: Experiment with Instructions

```
I have an OpenAI Agents SDK agent working. Help me experiment with
different instruction styles. I want to create:
1. A pirate-themed assistant that responds in pirate speak
2. A Socratic tutor that answers questions with questions
3. A code reviewer that's constructively critical

For each, give me the Agent() configuration and a test prompt to verify
the personality works.
```

**What you're learning:** Instructions shape agent behavior. Well-crafted instructions produce consistent, predictable responses. You're practicing the specification skill---defining what you want clearly enough that the agent executes it correctly.

### Prompt 2: Compare Model Providers

```
I want to compare OpenAI and Gemini models using the Agents SDK with
OpenAIChatCompletionsModel. Help me write a script that:
1. Sends the same prompt to both providers
2. Times each response
3. Prints a comparison of response quality and speed

The prompt should be something that shows differences in reasoning style,
like "Explain the tradeoffs between microservices and monoliths for a
startup with 3 engineers."
```

**What you're learning:** Different models have different strengths. By comparing them directly, you'll develop intuition for when to use which provider---a practical skill for building cost-effective agents.

### Prompt 3: Connect to Your Domain

```
I want to build a Digital FTE for [your domain: sales, legal, healthcare,
finance, education, etc.]. Starting with the basics I learned today
(Agent, Runner, instructions), help me:
1. Design the agent's personality and instructions for my domain
2. Write a simple proof-of-concept that demonstrates the agent understands
   domain-specific queries
3. Identify what tools I'll need to add (we'll build these in Lesson 2)

My domain is [describe your expertise or industry].
```

**What you're learning:** Translating technical SDK knowledge into domain-specific applications. This is the core of building Digital FTEs---encoding your expertise into an agent's instructions and behavior.

### Safety Note

As you experiment with agents, remember:
- **API keys are sensitive.** Never share code that contains keys. Always use environment variables.
- **API calls cost money.** Each agent execution uses tokens. Monitor your usage during development.
- **Agents can produce incorrect outputs.** Always review agent responses before acting on them in production scenarios.
