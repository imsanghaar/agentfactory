---
sidebar_position: 3
title: "Adding a Refresh Button"
description: "Make your widget interactive with sendFollowUpMessage"
keywords: ["window.openai", "sendFollowUpMessage", "widget button", "API availability", "optional chaining"]
chapter: 42
lesson: 3
duration_minutes: 35

# HIDDEN SKILLS METADATA
skills:
  - name: "sendFollowUpMessage Usage"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can implement button that triggers conversation follow-up"

  - name: "API Availability Pattern"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student uses optional chaining for window.openai access"

  - name: "structuredContent Data Flow"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student understands how tool data reaches widget via toolOutput"

learning_objectives:
  - objective: "Add interactive buttons to widgets using sendFollowUpMessage"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Button click triggers new conversation turn"

  - objective: "Implement API availability checks with optional chaining"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Widget works in ChatGPT and doesn't error in browser preview"

  - objective: "Pass data from server to widget via structuredContent"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Widget displays dynamic data from server"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (sendFollowUpMessage, optional chaining, structuredContent) within B1 limit of 10 - PASS"

differentiation:
  extension_for_advanced: "Add multiple buttons with different prompts; implement loading state during API call"
  remedial_for_struggling: "Focus on getting one button working before adding complexity"

generated_by: content-implementer
source_spec: specs/048-chapter-42-openai-apps-sdk
created: 2025-12-28
last_modified: 2025-12-28
version: 2.0.0
---

# Adding a Refresh Button

Your widget from Lesson 2 displays static content. But real applications need interactivity—buttons that do things. In this lesson, you'll add a "Refresh" button that triggers a new conversation turn when clicked.

The pattern you'll learn here—`sendFollowUpMessage`—is how TaskManager's "Add Task" and "Complete Task" buttons will work. Master this pattern, and you've mastered widget-to-conversation communication.

## What We're Building

Starting from your Lesson 2 widget, you'll add:
1. A "Refresh" button
2. A timestamp showing when data was loaded
3. Button click that asks ChatGPT to refresh

When complete, clicking the button inserts a message into the conversation like: "Refresh the greeting".

## The window.openai API

Inside ChatGPT, your widget has access to `window.openai`—an API for communicating with the host. The method we need:

| Method | Purpose |
|--------|---------|
| `sendFollowUpMessage({prompt})` | Insert a message into the conversation |

When you call `sendFollowUpMessage`, ChatGPT receives the prompt as if the user typed it. The model processes it and may call your tools again.

### API Availability: The First Rule

Here's the catch: `window.openai` only exists inside ChatGPT. If you preview your widget HTML in a browser during development, this code crashes:

```javascript
// This crashes outside ChatGPT
window.openai.sendFollowUpMessage({ prompt: "Refresh" });
```

**Output (in browser):**
```
Uncaught TypeError: Cannot read properties of undefined
```

The fix: always use optional chaining:

```javascript
// This works everywhere
window.openai?.sendFollowUpMessage?.({ prompt: "Refresh" });
```

**Output (in browser):** No error—the call is safely skipped.

**Output (in ChatGPT):** Message appears in conversation.

## Updating Your Server

Update `main.py` to include a timestamp and pass data to the widget:

```python
import mcp.types as types
from mcp.server.fastmcp import FastMCP
from datetime import datetime

MIME_TYPE = "text/html+skybridge"

# Updated widget with button and timestamp
WIDGET_HTML = '''<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: system-ui, sans-serif;
      background: linear-gradient(135deg, #667eea, #764ba2);
      min-height: 180px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0;
    }
    .card {
      background: white;
      padding: 24px 48px;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
      text-align: center;
    }
    h1 { margin: 0 0 8px 0; color: #333; }
    .time { color: #666; font-size: 14px; margin-bottom: 16px; }
    button {
      background: #667eea;
      color: white;
      border: none;
      padding: 10px 24px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 14px;
    }
    button:hover { background: #5a6fd6; }
  </style>
</head>
<body>
  <div class="card">
    <h1 id="greeting">Hello!</h1>
    <p class="time" id="time">Loading...</p>
    <button onclick="refresh()">Refresh</button>
  </div>
  <script>
    // Read data from server response
    const data = window.openai?.toolOutput;
    if (data) {
      document.getElementById('greeting').textContent = data.message;
      document.getElementById('time').textContent = 'Updated: ' + data.timestamp;
    }

    // Button handler
    function refresh() {
      window.openai?.sendFollowUpMessage?.({
        prompt: "Refresh the greeting"
      });
    }
  </script>
</body>
</html>'''

mcp = FastMCP("TaskManager")

@mcp.tool()
def show_greeting() -> types.CallToolResult:
    """Display a greeting widget with refresh capability."""
    now = datetime.now().strftime("%H:%M:%S")

    return types.CallToolResult(
        content=[types.TextContent(type="text", text=f"Greeting updated at {now}")],
        structuredContent={
            "message": "Hello, World!",
            "timestamp": now
        },
        _meta={
            "openai.com/widget": types.EmbeddedResource(
                type="resource",
                resource=types.TextResourceContents(
                    uri="ui://greeting",
                    mimeType=MIME_TYPE,
                    text=WIDGET_HTML,
                )
            )
        }
    )

if __name__ == "__main__":
    import uvicorn
    app = mcp.sse_app()
    uvicorn.run(app, host="0.0.0.0", port=8001)
```

### What Changed

**1. Added `structuredContent`:**

```python
structuredContent={
    "message": "Hello, World!",
    "timestamp": now
}
```

This data is accessible in the widget via `window.openai.toolOutput`.

**2. Widget reads dynamic data:**

```javascript
const data = window.openai?.toolOutput;
if (data) {
  document.getElementById('greeting').textContent = data.message;
  document.getElementById('time').textContent = 'Updated: ' + data.timestamp;
}
```

**3. Button triggers refresh:**

```javascript
function refresh() {
  window.openai?.sendFollowUpMessage?.({
    prompt: "Refresh the greeting"
  });
}
```

## Testing the Refresh

1. Restart your server (`uv run main.py`)
2. Make sure ngrok is running
3. In ChatGPT, invoke your tool: "Show me a greeting"
4. See the widget with timestamp
5. Click the "Refresh" button
6. Watch a new message appear: "Refresh the greeting"
7. The model calls your tool again, showing a new timestamp

Each refresh shows an updated timestamp, proving the round-trip works.

## Data Flow Summary

Here's how data flows in a widget with `sendFollowUpMessage`:

```
1. User clicks button
       ↓
2. Widget calls sendFollowUpMessage({ prompt: "..." })
       ↓
3. ChatGPT receives prompt as new conversation turn
       ↓
4. Model decides to call your tool
       ↓
5. Server returns structuredContent + widget
       ↓
6. New widget renders with fresh data from toolOutput
```

This is the foundation for TaskManager's "Add Task" button—it will send a prompt like "Add task: Buy groceries" and your server will update the task list.

## What You Built

Building on Lesson 2, you added:
- A "Refresh" button using `sendFollowUpMessage`
- Dynamic data via `structuredContent` → `window.openai.toolOutput`
- Safe API access with optional chaining

Your widget now communicates bidirectionally with ChatGPT. In the next lesson, you'll display a list of tasks and learn to separate large data from what the model sees.

## Try With AI

### Prompt 1: Add a Second Button

```
Add a "Say Hello Again" button next to the Refresh button.
When clicked, it should send a different prompt like "Say hello to me again with enthusiasm".
Style the buttons to sit side by side.
```

**What you're learning:** Multiple buttons can trigger different prompts, enabling varied interactions from a single widget.

### Prompt 2: Add Loading State

```
When the Refresh button is clicked, disable it and change its text to "Loading..." until the widget is replaced by a new one. How can I detect that the button was clicked?
```

**What you're learning:** UX patterns for async operations in widgets. Since the widget gets replaced on refresh, you'll discover why loading states work differently than in traditional SPAs.

### Prompt 3: Custom Prompt with Input

```
Replace the Refresh button with a text input and "Greet" button.
When clicked, send a prompt like "Greet me by the name: [input value]".
Update the server to accept a name parameter.
```

**What you're learning:** Collecting user input in widgets and passing it through the conversation. This is exactly how TaskManager's "Add Task" form will work.
