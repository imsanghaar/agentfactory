---
sidebar_position: 1
title: "Custom Models as Agent Backends"
description: "Understand how custom fine-tuned models integrate into agent architectures as reasoning engines"
chapter: 71
lesson: 1
duration_minutes: 40

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Architecture Understanding"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student explains how custom models fit as reasoning engines in agent systems"

  - name: "Backend Integration Patterns"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student identifies appropriate integration patterns for different deployment scenarios"

  - name: "Cost-Performance Trade-off Analysis"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student analyzes when custom backends provide value versus foundation models"

learning_objectives:
  - objective: "Explain how custom models serve as agent reasoning engines"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student describes the role of LLM backends in agent architectures"

  - objective: "Identify when custom backends provide value over foundation models"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Student analyzes cost, latency, and quality trade-offs for specific scenarios"

  - objective: "Recognize integration patterns for local and cloud deployments"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student matches deployment scenarios to appropriate integration approaches"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (agent architecture, reasoning engine, integration patterns, trade-offs, deployment scenarios) within B1-B2 limit (7-10 concepts)"

differentiation:
  extension_for_advanced: "Research vLLM production serving patterns and compare to Ollama"
  remedial_for_struggling: "Focus on single deployment pattern (Ollama local) before exploring alternatives"
---

# Custom Models as Agent Backends

Your Task API model runs via Ollama. But how does it become the brain of an agent system? This lesson explains how custom models integrate into agent architectures as reasoning engines.

Understanding this architecture is essential before you configure proxies, SDKs, and tool calling in the following lessons.

## The Agent Architecture

An agent system has three core components:

```
┌─────────────────────────────────────────────────────────┐
│                     AGENT SYSTEM                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   ┌──────────────┐     ┌──────────────┐     ┌─────────┐ │
│   │   TOOLS      │────▶│   REASONING  │────▶│  OUTPUT │ │
│   │              │     │    ENGINE    │     │         │ │
│   │ - APIs       │◀────│              │◀────│ Actions │ │
│   │ - Functions  │     │  (LLM Model) │     │ Results │ │
│   │ - MCP        │     └──────────────┘     └─────────┘ │
│   └──────────────┘              │                       │
│                                 │                       │
│                    ┌────────────▼────────────┐          │
│                    │      MEMORY/STATE       │          │
│                    │   Conversation History  │          │
│                    └─────────────────────────┘          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

| Component | Role | Your Custom Model's Job |
|-----------|------|------------------------|
| **Reasoning Engine** | Decides what to do, interprets results | This is where your Task API model runs |
| **Tools** | Execute actions (API calls, functions, MCP) | Model tells agent which tool to call |
| **Memory** | Maintains context across turns | Model receives history as context |
| **Output** | Final response or action result | Model generates structured output |

**Your custom model replaces the default reasoning engine.** Instead of GPT-4 or Claude deciding what actions to take, your fine-tuned Task API model makes those decisions.

## Why Replace the Default Model?

Foundation models like GPT-4 and Claude are excellent general-purpose reasoners. Why would you swap them for a custom model?

### Cost Reduction

| Model | Cost per 1M Tokens | Monthly Cost (1M requests) |
|-------|-------------------|---------------------------|
| GPT-4o | $5.00 input / $15.00 output | ~$10,000 |
| GPT-4o-mini | $0.15 input / $0.60 output | ~$375 |
| Custom (Ollama Local) | $0 | Hardware only |
| Custom (Cloud) | ~$0.10 - $0.50 | ~$100 - $500 |

For high-volume applications, custom models reduce costs by 10-100x.

### Latency Control

Foundation model APIs depend on:
- Network round-trip time (50-200ms)
- API queue wait times (variable)
- Rate limiting during high traffic

Local models provide:
- No network latency (local inference)
- Predictable response times
- No rate limits

For real-time applications (voice assistants, live coding), local latency is critical.

### Domain Specialization

Your Task API model was fine-tuned on task management conversations. It understands:
- Task creation, updates, and completion workflows
- Priority classification specific to your domain
- Your organization's task vocabulary

A foundation model needs extensive prompting to match this. Your model does it by default.

### Data Privacy

Some use cases require:
- Data never leaves your infrastructure
- No third-party API calls
- Complete audit trails

Local models satisfy these requirements by design.

## Integration Patterns

Custom models connect to agent frameworks through three main patterns:

### Pattern 1: Direct Ollama Integration

```
┌─────────────────┐         ┌───────────────────┐
│   Agent Code    │◀───────▶│   Ollama Server   │
│  (Python SDK)   │  HTTP   │  localhost:11434  │
└─────────────────┘         └───────────────────┘
```

**How it works:**
- Agent code calls Ollama's REST API directly
- No intermediate proxy
- Simplest setup for local development

**Code example:**

```python
import requests

def generate(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "task-api-model",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]
```

**Output:**
```
>>> generate("Create a task for reviewing Q4 budget")
"I'll create a high-priority task for reviewing the Q4 budget..."
```

**Best for:** Simple agents, prototyping, learning

### Pattern 2: LiteLLM Proxy

```
┌─────────────────┐         ┌───────────────────┐         ┌───────────────────┐
│   Agent Code    │◀───────▶│   LiteLLM Proxy   │◀───────▶│   Ollama Server   │
│  (OpenAI SDK)   │  HTTP   │  localhost:4000   │  HTTP   │  localhost:11434  │
└─────────────────┘         └───────────────────┘         └───────────────────┘
```

**How it works:**
- LiteLLM provides OpenAI-compatible API
- Agent code uses standard OpenAI SDK
- Proxy translates requests to Ollama format

**Why use a proxy?**

| Benefit | Explanation |
|---------|-------------|
| SDK Compatibility | Use OpenAI SDK without code changes |
| Model Switching | Change backend without changing code |
| Fallback Support | Auto-fallback to GPT-4 if local fails |
| Unified Interface | Same API for Ollama, vLLM, cloud models |

**Best for:** Production agents, SDK compatibility, multi-model setups

### Pattern 3: Cloud Deployment

```
┌─────────────────┐         ┌───────────────────┐
│   Agent Code    │◀───────▶│   Cloud Endpoint  │
│  (OpenAI SDK)   │  HTTPS  │   your-api.com    │
└─────────────────┘         └───────────────────┘
```

**How it works:**
- Custom model deployed on cloud infrastructure
- Exposes OpenAI-compatible endpoint
- Agent code connects via HTTPS

**When to use:**
- Multiple clients need access
- Scaling beyond single machine
- Geographic distribution

**Best for:** Production services, team access, high availability

## Choosing Your Integration Pattern

Use this decision framework:

```
Are you developing locally?
├── Yes ──▶ Pattern 1 (Direct Ollama) for prototyping
│           Pattern 2 (LiteLLM) when adding SDK features
│
└── No ───▶ Do you need OpenAI SDK compatibility?
            ├── Yes ──▶ Pattern 2 (LiteLLM Proxy) or Pattern 3 (Cloud)
            └── No ───▶ Pattern 1 with custom client
```

For this chapter, we use **Pattern 2 (LiteLLM Proxy)** because:
1. It provides OpenAI SDK compatibility
2. It enables the OpenAI Agents SDK integration
3. It supports fallback to foundation models
4. It's the standard for production agent systems

## The Agent Loop with Custom Backend

Here's how your custom model fits into the agent execution loop:

```
1. User Input
   │
   ▼
2. Agent receives input + conversation history
   │
   ▼
3. Agent calls YOUR MODEL via LiteLLM proxy
   │
   ▼
4. Your model reasons about the task:
   - What does the user want?
   - Which tool should I call?
   - What parameters should I pass?
   │
   ▼
5. Your model returns structured output:
   {
     "tool": "create_task",
     "arguments": {
       "title": "Review Q4 budget",
       "priority": "high"
     }
   }
   │
   ▼
6. Agent executes tool with provided arguments
   │
   ▼
7. Tool returns result
   │
   ▼
8. Agent calls YOUR MODEL again with tool result
   │
   ▼
9. Your model generates final response
   │
   ▼
10. User receives response
```

Your model participates in steps 3-4, 8-9. It decides which tools to use and how to respond.

## What Makes Custom Backends Different

When you use GPT-4 as your reasoning engine, Anthropic or OpenAI handles:
- Model hosting and scaling
- API availability
- Response quality
- Tool calling format

When you use a custom backend, **you** handle:
- Model deployment (Ollama, vLLM)
- Response quality (your fine-tuning)
- Tool calling accuracy (structured output training)
- Fallback strategies (error handling)

This chapter teaches you to handle all four.

## Update Your Skill

After completing this lesson, update your agent-integration skill with:

```
Add a section on "Integration Pattern Selection" with:
- Decision framework for choosing patterns
- Comparison table of direct vs proxy vs cloud
- When to use each pattern
```

## Try With AI

### Prompt 1: Analyze Your Setup

```
I have my Task API model running on Ollama at localhost:11434. I'm building
a task management agent that needs:
- Tool calling for CRUD operations
- Sub-500ms latency for real-time UX
- Fallback to GPT-4o-mini when my model fails

Which integration pattern should I use and why? Walk me through the trade-offs.
```

**What you're learning**: Applying decision frameworks to your specific requirements.

### Prompt 2: Map the Agent Loop

```
Trace through the 10-step agent loop for this scenario:

User says: "Create a task to review the marketing proposal by Friday"

My Task API model is the reasoning engine. Show me:
1. What the model receives at each step
2. What it outputs
3. How the tool execution works

Be specific about the JSON structures involved.
```

**What you're learning**: Understanding agent execution flow with concrete examples.

### Prompt 3: Compare Cost Models

```
Help me calculate the monthly cost comparison for my task management agent:
- Expected volume: 50,000 requests/month
- Average request: 500 input tokens, 200 output tokens
- Currently using GPT-4o-mini

Compare costs for:
1. Staying with GPT-4o-mini
2. Switching to local Ollama (include hardware costs)
3. Hybrid: Custom model with GPT-4 fallback (10% fallback rate)

Which makes financial sense for my use case?
```

**What you're learning**: Quantifying the value proposition of custom backends.
