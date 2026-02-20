---
sidebar_position: 1
title: "Apps SDK Architecture"
description: "Understand why Apps SDK matters and learn the three-layer architecture of ChatGPT Apps"
keywords: ["Apps SDK", "ChatGPT Apps", "widget architecture", "MCP server", "distribution", "800 million users"]
chapter: 42
lesson: 1
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Distribution Opportunity Recognition"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Business"
    measurable_at_this_level: "Student can explain why Apps SDK provides unique distribution advantages"

  - name: "Three-Layer Architecture Understanding"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can draw and explain the ChatGPT UI → Widget iframe → MCP Server flow"

  - name: "Apps SDK vs Agents SDK Differentiation"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Technical Problem-Solving"
    measurable_at_this_level: "Student can identify when to use Apps SDK vs Agents SDK"

  - name: "Widget vs Standard MCP Tool Differences"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can explain how widget-enabled tools differ from standard MCP"

learning_objectives:
  - objective: "Explain why Apps SDK offers unique distribution advantages"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Discussion of ChatGPT user base and discovery mechanisms"

  - objective: "Explain the three-layer architecture of ChatGPT Apps"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Architecture diagram drawing from memory"

  - objective: "Differentiate Apps SDK from Agents SDK by purpose"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Comparison table creation"

  - objective: "Trace data flow from user prompt to widget render"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Flow explanation in own words"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (distribution opportunity, three-layer arch, widget vs MCP, data flow, SDK comparison) within B1 limit of 10 - PASS"

differentiation:
  extension_for_advanced: "Explore oauth-protected and todo_app examples for authentication patterns"
  remedial_for_struggling: "Focus only on distribution value and three-layer diagram; skip code exploration until comfortable"

generated_by: content-implementer
source_spec: specs/048-chapter-42-openai-apps-sdk
created: 2025-12-28
last_modified: 2025-12-28
version: 1.1.0
---

# Apps SDK Architecture

You've built backend agents that reason, plan, and execute tasks. You've created MCP servers that expose tools and resources. Your agents work brilliantly—but they live on your server. How do you get them in front of users who need them?

This is the distribution problem every software builder faces. You can build the most capable agent in the world, but if users can't find and use it, it doesn't matter. Traditional distribution requires building your own interface, marketing to acquire users, and competing with millions of other apps for attention.

The Apps SDK solves this problem by putting your agents where users already are: inside ChatGPT.

## Why Apps SDK Matters

ChatGPT has over **800 million weekly active users** as of late 2024. That's not a typo—800 million people use ChatGPT every week. OpenAI also reports that over **1 million businesses** now use ChatGPT, with **92% of Fortune 500 companies** having adopted the platform. These aren't casual users; they're professionals actively looking for tools to help them work.

When you build a ChatGPT App using the Apps SDK, your application becomes available in the **ChatGPT App Directory** at [chatgpt.com/apps](https://chatgpt.com/apps). Users can discover your app, add it to their ChatGPT, and start using it immediately—no separate website, no mobile app download, no user account creation on your end.

But here's what makes this truly different: **AI-powered discovery**. When a ChatGPT Plus user describes a task, ChatGPT can recommend relevant apps from the directory. Your app doesn't just sit in a catalog waiting to be found—the AI actively suggests it to users who need it.

### The Distribution Advantage

Consider the traditional path to reach users:

1. Build your application
2. Build a web interface or mobile app
3. Set up hosting and infrastructure
4. Create marketing materials
5. Run ads or content marketing
6. Convert visitors to users
7. Handle user authentication
8. Maintain the entire stack

With Apps SDK:

1. Build your MCP server (you already know how from Chapter 38)
2. Add widget responses for visual interfaces
3. Deploy and register in ChatGPT's App Directory
4. Users discover and use your app inside ChatGPT

The launch partners for ChatGPT Apps include **Canva, Figma, DoorDash, Expedia, and Spotify**—companies that already have massive user bases chose to build ChatGPT Apps anyway. Why? Because being where users already work creates frictionless adoption.

### What Problem Does It Solve?

You've built agents that can reason. Now make them visual and accessible.

The Apps SDK transforms your MCP servers into visual applications that render rich HTML widgets directly in ChatGPT. Instead of getting a text list of tasks, users see an interactive Kanban board. Instead of receiving JSON data, they see charts, tables, and action buttons. The conversation becomes a visual workspace—and it's available to 800 million potential users.

This lesson establishes the mental model you need before writing any code. You'll understand how ChatGPT, widgets, and your server communicate—the foundation for everything you build in this chapter.

## The Three-Layer Architecture

ChatGPT Apps consist of three distinct layers that work together:

```
┌─────────────────────────────────────────────────────────────────┐
│                        LAYER 1: ChatGPT UI                      │
│   - Renders conversation messages                               │
│   - Hosts widget iframes                                        │
│   - Routes tool calls to MCP servers                            │
├─────────────────────────────────────────────────────────────────┤
│                        LAYER 2: Widget (iframe)                 │
│   - Your HTML/CSS/JS running in sandboxed iframe                │
│   - Communicates with ChatGPT via window.openai API             │
│   - Displays rich UI: charts, forms, buttons, tables            │
├─────────────────────────────────────────────────────────────────┤
│                        LAYER 3: MCP Server                      │
│   - Your FastMCP/Node server (just like Chapter 38)             │
│   - Exposes tools with special widget metadata                  │
│   - Returns structuredContent for widgets + text for model      │
└─────────────────────────────────────────────────────────────────┘
```

**Layer 1: ChatGPT UI** is OpenAI's interface that users interact with. It handles the conversation, invokes your MCP tools, and creates sandboxed iframes to display your widgets.

**Layer 2: Widget** is your HTML/CSS/JavaScript code running inside an iframe. The iframe is sandboxed for security, but your widget can communicate with ChatGPT through the `window.openai` API. This is where your visual UI lives.

**Layer 3: MCP Server** is the backend you already know how to build from Chapters 37-38. The difference? Your tool responses include special metadata that tells ChatGPT to render a widget instead of just showing text.

### Why Three Layers?

This architecture provides security through isolation. Your widget code runs in a sandboxed iframe—it cannot access the parent ChatGPT page or other widgets. Your MCP server runs on your infrastructure, keeping sensitive data and API keys secure. ChatGPT acts as the trusted intermediary.

## Data Flow: From Prompt to Widget

Understanding the data flow is essential for debugging and design. Here's what happens when a user asks your app to show data:

**Step 1: User Prompt**
```
User: "Show me the task board for Project Alpha"
```

**Step 2: Model Tool Call**

ChatGPT's model decides to call your tool. It sends a request to your MCP server:

```
Tool call: show_kanban_board
Arguments: { "project": "Project Alpha" }
```

**Step 3: Server Response**

Your MCP server fetches data and returns a structured response:

```python
return CallToolResult(
    content=[TextContent(type="text", text="Here's your board.")],
    structuredContent={
        "columns": [
            {"id": "todo", "tasks": [...]},
            {"id": "in-progress", "tasks": [...]},
            {"id": "done", "tasks": [...]}
        ]
    },
    _meta={
        "openai.com/widget": embedded_widget_resource
    }
)
```

**Step 4: Widget Render**

ChatGPT sees the widget metadata in `_meta` and creates an iframe. Your widget HTML loads and accesses the data through `window.openai.toolOutput`.

**Step 5: Model Narration**

The model reads `structuredContent` and generates a natural language response: "I've loaded the Kanban board for Project Alpha. You have 5 tasks in progress."

**Complete Flow Diagram:**

```
User Prompt
    │
    ▼
ChatGPT Model (decides which tool to call)
    │
    ▼
MCP Server (your code: fetches data, returns response)
    │
    ▼
ChatGPT (creates iframe, loads widget HTML)
    │
    ▼
Widget (reads window.openai.toolOutput, renders UI)
    │
    ▼
Model Narration (summarizes what happened)
```

## Apps SDK vs Agents SDK

Both SDKs come from OpenAI, but they solve different problems:

| Aspect | Agents SDK (Chapter 34) | Apps SDK (This Chapter) |
|--------|-------------------------|-------------------------|
| **Purpose** | Build backend agent logic | Build user-facing widgets |
| **Where it runs** | Your server (Python/Node) | ChatGPT interface (iframe) |
| **User interaction** | Through conversation text | Direct clicks, inputs, buttons |
| **Output type** | Text and tool results | Interactive HTML widgets |
| **Primary skill** | Agent orchestration, tools, handoffs | Widget design, window.openai API |
| **When to use** | Complex reasoning, multi-agent workflows | Visual dashboards, interactive forms |

**The Key Insight**: These SDKs complement each other. You might use Agents SDK to build a sophisticated backend agent, then use Apps SDK to give that agent a visual interface inside ChatGPT.

**Example Scenario**: Your Agents SDK agent analyzes sales data and produces recommendations. Your Apps SDK widget displays those recommendations as an interactive chart with drill-down capabilities.

## Widget vs Standard MCP Tool

You already know how to build MCP tools from Chapter 38. Widget-enabled tools differ in three key ways:

### 1. Response MIME Type

Standard MCP tools return text or JSON that the model summarizes:

```python
# Standard MCP tool
return CallToolResult(
    content=[TextContent(type="text", text="Found 15 tasks")]
)
```

Widget-enabled tools include HTML with a special MIME type:

```python
# Widget-enabled tool
MIME_TYPE = "text/html+skybridge"  # This is the magic

return CallToolResult(
    content=[TextContent(type="text", text="Loading board...")],
    _meta={
        "openai.com/widget": EmbeddedResource(
            type="resource",
            resource=TextResourceContents(
                uri="ui://widget/kanban.html",
                mimeType=MIME_TYPE,  # Tells ChatGPT: render this as widget
                text=WIDGET_HTML,
                title="Kanban Board"
            )
        )
    }
)
```

The `text/html+skybridge` MIME type signals to ChatGPT: "Don't show this as text—render it as an interactive widget."

### 2. Dual Response Channels

Standard tools have one output channel (text for the model). Widget tools have two:

| Channel | Visibility | Purpose |
|---------|------------|---------|
| `structuredContent` | Model + Widget | Concise data for model narration |
| `_meta` | Widget only | Large/sensitive data hidden from model |

Why separate channels? The model has limited context. If you pass a 10,000-task dataset through `structuredContent`, the model tries to process it all. By putting large data in `_meta`, your widget can access it while the model only sees a summary.

### 3. Bidirectional Communication

Standard MCP tools are one-way: server responds, conversation continues.

Widget-enabled tools are bidirectional:

- **Widget to ChatGPT**: `window.openai.sendFollowUpMessage()` inserts messages
- **Widget to Server**: `window.openai.callTool()` invokes other MCP tools
- **ChatGPT to Widget**: Data flows through `window.openai.toolOutput`

This enables real interaction. A button in your widget can trigger a new conversation turn or refresh data from your server.

## Exploring Official Examples

OpenAI provides a repository of example ChatGPT Apps at:

```
https://github.com/openai/openai-apps-sdk-examples
```

The `kitchen_sink` example demonstrates most Apps SDK features in one project:

### kitchen_sink Structure

```
kitchen_sink/
├── server/
│   └── main.py          # FastMCP server with widget tools
├── widgets/
│   ├── index.html       # Widget HTML with window.openai usage
│   └── styles.css       # Widget styling
├── pyproject.toml       # Python dependencies (managed by uv)
└── README.md            # Setup instructions
```

### Key Files to Examine

**server/main.py** - Look for these patterns:

1. **Widget resource registration**: How the server defines widget HTML as an MCP resource
2. **Tool metadata**: The `_meta` dictionary with `openai/outputTemplate`
3. **Response structure**: How `structuredContent` and `_meta` are used

**widgets/index.html** - Look for these patterns:

1. **window.openai access**: How the widget reads `toolOutput`
2. **API availability checks**: Defensive `window.openai?.methodName` patterns
3. **Button handlers**: How clicks trigger `sendFollowUpMessage` or `callTool`

### What Each Example Teaches

| Example | Primary Concept |
|---------|-----------------|
| `kitchen_sink` | All core features: tools, widgets, state, display modes |
| `todo_app` | CRUD operations with widget state persistence |
| `oauth-protected` | Authentication flow with protected resources |
| `file-upload` | Handling user file uploads in widgets |

For this chapter, start with `kitchen_sink`. It's comprehensive and well-documented.

## What You Need to Remember

Before building your first ChatGPT App, internalize these concepts:

**Three Layers**:
1. ChatGPT UI (hosts everything)
2. Widget iframe (your visual code)
3. MCP Server (your backend logic)

**Data Flow**:
- User prompt triggers model tool call
- Server returns structured data + widget HTML
- ChatGPT renders widget in iframe
- Model narrates what happened

**Key Differences from Standard MCP**:
- MIME type: `text/html+skybridge`
- Dual channels: `structuredContent` (model sees) + `_meta` (widget only)
- Bidirectional: widgets can call tools and send messages

## Try With AI

### Prompt 1: Explore the Distribution Opportunity

```
I'm building an AI agent that helps users manage their tasks.
Compare these two distribution strategies:

1. Building a standalone web app with my own user acquisition
2. Building a ChatGPT App using the Apps SDK

What are the advantages and trade-offs of each approach?
Consider: user acquisition cost, maintenance burden, and user experience.
```

**What you're learning:** This prompt helps you articulate the business case for Apps SDK to stakeholders. Understanding the distribution advantage is as important as understanding the technical architecture.

### Prompt 2: Understand the Three-Layer Architecture

```
Explain the three-layer architecture of ChatGPT Apps:
- ChatGPT UI (Layer 1)
- Widget iframe (Layer 2)
- MCP Server (Layer 3)

For each layer, explain:
1. What runs there
2. Who controls it (OpenAI vs developer)
3. How it communicates with adjacent layers

Then explain why this separation exists from a security perspective.
```

**What you're learning:** This prompt reinforces the architectural model you'll use throughout the chapter. Understanding *why* the layers are separated (security isolation) helps you make better design decisions.

### Prompt 3: Compare SDK Options

```
I'm confused about OpenAI's different SDKs. Compare:
- OpenAI Agents SDK (what we learned in Chapter 34)
- OpenAI Apps SDK (what we're learning now)

When would I use each? Can they work together?
Give me a concrete example of an application that uses both.
```

**What you're learning:** This prompt clarifies the relationship between SDKs you've already learned and the new one. Many developers confuse these—you won't.

## Activities

### Activity 1: Pitch the Distribution Advantage

Imagine you're explaining Apps SDK to a non-technical colleague. Write a 2-3 sentence pitch that explains:

1. The problem it solves (distribution)
2. The opportunity (800M+ users, AI-powered discovery)
3. Why this matters for your specific domain

Test your pitch: Would this convince someone to invest time learning the Apps SDK?

### Activity 2: Draw the Architecture

Without looking at this lesson, draw the three-layer architecture from memory:

1. Draw three boxes representing the three layers
2. Label each layer with its name and primary responsibility
3. Draw arrows showing how data flows between layers
4. Label each arrow with what data travels through it

Check your diagram against the architecture section above. What did you remember? What did you miss?

### Activity 3: Complete the Comparison Table

Fill in this comparison table from memory:

| Aspect | Agents SDK | Apps SDK |
|--------|------------|----------|
| Purpose | ? | ? |
| Where it runs | ? | ? |
| User interaction | ? | ? |
| Output type | ? | ? |

Then check your answers against the comparison table in this lesson.

### Activity 4: Clone and Explore kitchen_sink

Clone the official examples repository and explore the kitchen_sink example:

```bash
git clone https://github.com/openai/openai-apps-sdk-examples.git
cd openai-apps-sdk-examples/kitchen_sink
```

Answer these questions by exploring the code:

1. In `server/main.py`, find where the widget MIME type is defined. What is the exact string?
2. In `widgets/index.html`, find at least two `window.openai` methods being used. What are they?
3. How many tool definitions are in the server? List their names.

Write your answers down before moving to the next lesson.
