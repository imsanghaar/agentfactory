---
sidebar_position: 7
title: "React & Apps SDK UI"
description: "Build ChatGPT App widgets using React and the official @openai/apps-sdk-ui component library"
keywords: ["React", "apps-sdk-ui", "useWidgetState", "useOpenAiGlobal", "Tailwind", "component library"]
chapter: 42
lesson: 7
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "React Widget Development"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can build ChatGPT App widgets using React and apps-sdk-ui"

  - name: "React Hooks for Widget State"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can use useWidgetState and useOpenAiGlobal hooks"

  - name: "Widget Bundling"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can bundle React widgets for ChatGPT Apps"

learning_objectives:
  - objective: "Set up a React project with @openai/apps-sdk-ui"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successfully configure React + Tailwind + apps-sdk-ui"

  - objective: "Use useWidgetState and useOpenAiGlobal hooks for state management"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Implement stateful widget using React hooks"

  - objective: "Build widgets with apps-sdk-ui components"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Create widget using Button, Badge, and layout components"

cognitive_load:
  new_concepts: 3
  assessment: "Introduces React approach, apps-sdk-ui library, and custom hooks - builds on existing widget knowledge"

differentiation:
  extension_for_advanced: "Add custom themes, implement complex multi-component layouts"
  remedial_for_struggling: "Focus on hooks first, then introduce apps-sdk-ui components gradually"

generated_by: claude-opus-4-5
source_spec: specs/048-chapter-42-openai-apps-sdk
created: 2025-12-28
last_modified: 2025-12-28
version: 1.0.0
---

# React & Apps SDK UI

You've built TaskManager with vanilla JavaScript. It works, but as widgets grow complex, managing DOM updates becomes tedious. React solves this—and OpenAI provides an official component library that matches ChatGPT's design system.

In this lesson, you'll learn the React approach: setting up a project with `@openai/apps-sdk-ui`, using React hooks for widget state, and building polished UIs with pre-built components. This is how production ChatGPT Apps are built.

## Why React for ChatGPT Apps?

Vanilla JavaScript works for simple widgets. But consider what happens as complexity grows:

| Vanilla JS Challenge | React Solution |
|---------------------|----------------|
| Manual DOM updates | Declarative rendering |
| State scattered across variables | Centralized state with hooks |
| Event listener management | Automatic cleanup |
| Inconsistent styling | Design system components |

The official `@openai/apps-sdk-ui` library provides:
- **Design tokens** matching ChatGPT's colors, typography, spacing
- **Pre-built components**: Button, Badge, TextLink, Icons
- **Tailwind 4 integration** with zero configuration
- **Accessible components** built on Radix primitives

## Project Setup

Create a React widget project alongside your MCP server:

```
taskmanager/
├── server/
│   └── main.py          # Your FastMCP server
└── web/
    ├── package.json
    ├── tsconfig.json
    ├── src/
    │   ├── main.tsx     # Entry point
    │   ├── main.css     # Tailwind + apps-sdk-ui styles
    │   ├── TaskWidget.tsx
    │   └── hooks/
    │       ├── useOpenAiGlobal.ts
    │       └── useWidgetState.ts
    └── dist/
        └── widget.js    # Bundled output
```

### Initialize the Project

```bash
cd taskmanager
mkdir -p web/src/hooks
cd web
npm init -y
npm install react react-dom @openai/apps-sdk-ui
npm install -D typescript esbuild @types/react @types/react-dom tailwindcss
```

### Configure TypeScript

Create `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "declaration": false,
    "outDir": "./dist"
  },
  "include": ["src/**/*"]
}
```

### Configure Styles

Create `src/main.css`:

```css
@import "tailwindcss";
@import "@openai/apps-sdk-ui/css";
@source "../node_modules/@openai/apps-sdk-ui";

/* Your custom styles here */
.task-list {
  @apply space-y-2;
}
```

## The useOpenAiGlobal Hook

This hook subscribes to `window.openai` values reactively. When ChatGPT updates globals, your components re-render automatically.

Create `src/hooks/useOpenAiGlobal.ts`:

```typescript
import { useSyncExternalStore } from "react";

// Type definitions for window.openai
declare global {
  interface Window {
    openai?: {
      toolInput?: Record<string, unknown>;
      toolOutput?: Record<string, unknown>;
      toolResponseMetadata?: Record<string, unknown>;
      widgetState?: Record<string, unknown>;
      theme?: "light" | "dark";
      displayMode?: "inline" | "pip" | "fullscreen";
      locale?: string;
      setWidgetState?: (state: Record<string, unknown>) => void;
      callTool?: (name: string, args: Record<string, unknown>) => Promise<unknown>;
      sendFollowUpMessage?: (options: { prompt: string }) => void;
      requestDisplayMode?: (options: { mode: string }) => Promise<void>;
    };
  }
}

type OpenAiGlobals = NonNullable<Window["openai"]>;

export function useOpenAiGlobal<K extends keyof OpenAiGlobals>(
  key: K
): OpenAiGlobals[K] | undefined {
  return useSyncExternalStore(
    (onChange) => {
      const handleSetGlobal = (event: CustomEvent) => {
        if (event.detail?.globals?.[key] !== undefined) {
          onChange();
        }
      };
      window.addEventListener(
        "openai:set_globals",
        handleSetGlobal as EventListener
      );
      return () => {
        window.removeEventListener(
          "openai:set_globals",
          handleSetGlobal as EventListener
        );
      };
    },
    () => window.openai?.[key]
  );
}
```

**How it works:**
1. `useSyncExternalStore` is React's hook for external state
2. Listens for `openai:set_globals` events from ChatGPT
3. Returns the current value of the requested key
4. Components using this hook re-render when values change

### Using useOpenAiGlobal

```tsx
function TaskStats() {
  const toolOutput = useOpenAiGlobal("toolOutput");
  const theme = useOpenAiGlobal("theme");

  return (
    <div className={theme === "dark" ? "bg-gray-800" : "bg-white"}>
      <p>Total: {toolOutput?.total ?? 0} tasks</p>
      <p>Pending: {toolOutput?.pending ?? 0}</p>
    </div>
  );
}
```

## The useWidgetState Hook

This hook manages persistent widget state across conversation turns. It hydrates from `window.openai.widgetState` and syncs changes back.

Create `src/hooks/useWidgetState.ts`:

```typescript
import { useState, useCallback, useEffect } from "react";
import { useOpenAiGlobal } from "./useOpenAiGlobal";

export function useWidgetState<T extends Record<string, unknown>>(
  initializer: () => T
): [T, (updater: T | ((prev: T) => T)) => void] {
  // Get persisted state from host
  const hostState = useOpenAiGlobal("widgetState") as T | undefined;

  // Initialize with host state or default
  const [state, setStateInternal] = useState<T>(() => {
    return hostState ?? initializer();
  });

  // Sync with host state changes
  useEffect(() => {
    if (hostState) {
      setStateInternal(hostState);
    }
  }, [hostState]);

  // Wrapper that also persists to host
  const setState = useCallback(
    (updater: T | ((prev: T) => T)) => {
      setStateInternal((prev) => {
        const next = typeof updater === "function" ? updater(prev) : updater;
        // Persist to host
        window.openai?.setWidgetState?.(next);
        return next;
      });
    },
    []
  );

  return [state, setState];
}
```

**Key behaviors:**
- Hydrates from `window.openai.widgetState` on mount
- Calls `setWidgetState` on every update for persistence
- Works like regular React state otherwise

### Using useWidgetState

```tsx
function TaskList() {
  const [widgetState, setWidgetState] = useWidgetState(() => ({
    selectedIds: [] as number[],
    filter: "all" as "all" | "pending" | "done",
  }));

  const toggleSelection = (taskId: number) => {
    setWidgetState((prev) => ({
      ...prev,
      selectedIds: prev.selectedIds.includes(taskId)
        ? prev.selectedIds.filter((id) => id !== taskId)
        : [...prev.selectedIds, taskId],
    }));
  };

  // State persists across conversation turns!
  return (
    <div>
      <p>Selected: {widgetState.selectedIds.length}</p>
      {/* ... */}
    </div>
  );
}
```

## Using apps-sdk-ui Components

The `@openai/apps-sdk-ui` library provides components styled to match ChatGPT. Import and use them directly:

```tsx
import { Button } from "@openai/apps-sdk-ui/components/Button";
import { Badge } from "@openai/apps-sdk-ui/components/Badge";

function TaskItem({ task, onToggle, onDelete }) {
  return (
    <div className="flex items-center gap-3 p-3 border-b">
      <Button
        variant={task.done ? "secondary" : "primary"}
        size="sm"
        onClick={() => onToggle(task.id)}
      >
        {task.done ? "Undo" : "Complete"}
      </Button>

      <span className={task.done ? "line-through text-gray-400" : ""}>
        {task.title}
      </span>

      {task.done && (
        <Badge variant="success">Done</Badge>
      )}

      <Button
        variant="destructive"
        size="sm"
        onClick={() => onDelete(task.id)}
      >
        Delete
      </Button>
    </div>
  );
}
```

### Available Components

| Component | Use Case |
|-----------|----------|
| `Button` | Primary actions, variants: primary, secondary, destructive |
| `Badge` | Status indicators, task categories |
| `TextLink` | Navigation within widget |
| `ButtonLink` | Link styled as button |
| `Icon` sets | Calendar, Phone, Maps, Members, Invoice |

## Complete React TaskManager

Here's TaskManager rewritten in React:

```tsx
// src/TaskWidget.tsx
import { useOpenAiGlobal } from "./hooks/useOpenAiGlobal";
import { useWidgetState } from "./hooks/useWidgetState";
import { Button } from "@openai/apps-sdk-ui/components/Button";
import { Badge } from "@openai/apps-sdk-ui/components/Badge";
import { useState } from "react";

interface Task {
  id: number;
  title: string;
  done: boolean;
}

interface WidgetState {
  selectedIds: number[];
}

export function TaskWidget() {
  const toolOutput = useOpenAiGlobal("toolOutput") as { total: number; pending: number } | undefined;
  const metadata = useOpenAiGlobal("toolResponseMetadata") as { tasks: Task[] } | undefined;
  const theme = useOpenAiGlobal("theme");

  const [widgetState, setWidgetState] = useWidgetState<WidgetState>(() => ({
    selectedIds: [],
  }));

  const [newTaskTitle, setNewTaskTitle] = useState("");

  const tasks = metadata?.tasks ?? [];

  const toggleSelection = (taskId: number) => {
    setWidgetState((prev) => ({
      ...prev,
      selectedIds: prev.selectedIds.includes(taskId)
        ? prev.selectedIds.filter((id) => id !== taskId)
        : [...prev.selectedIds, taskId],
    }));
  };

  const handleComplete = async (taskId: number) => {
    await window.openai?.callTool?.("complete_task", { task_id: taskId });
    refresh();
  };

  const handleDelete = async (taskId: number) => {
    setWidgetState((prev) => ({
      ...prev,
      selectedIds: prev.selectedIds.filter((id) => id !== taskId),
    }));
    await window.openai?.callTool?.("delete_task", { task_id: taskId });
    refresh();
  };

  const handleAddTask = () => {
    if (!newTaskTitle.trim()) return;
    window.openai?.sendFollowUpMessage?.({ prompt: `Add task: ${newTaskTitle}` });
    setNewTaskTitle("");
  };

  const handleBulkDelete = async () => {
    for (const id of widgetState.selectedIds) {
      await window.openai?.callTool?.("delete_task", { task_id: id });
    }
    setWidgetState((prev) => ({ ...prev, selectedIds: [] }));
    refresh();
  };

  const refresh = () => {
    window.openai?.sendFollowUpMessage?.({ prompt: "Show my tasks" });
  };

  return (
    <div className={`p-4 rounded-xl ${theme === "dark" ? "bg-gray-800 text-white" : "bg-white"}`}>
      <h2 className="text-xl font-semibold mb-2">TaskManager</h2>

      {toolOutput && (
        <p className="text-sm text-gray-500 mb-4">
          {toolOutput.total} tasks ({toolOutput.pending} pending)
        </p>
      )}

      {/* Add Task Form */}
      <div className="flex gap-2 mb-4">
        <input
          type="text"
          value={newTaskTitle}
          onChange={(e) => setNewTaskTitle(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleAddTask()}
          placeholder="Add a task..."
          className="flex-1 px-3 py-2 border rounded-md"
        />
        <Button onClick={handleAddTask}>Add</Button>
      </div>

      {/* Bulk Actions */}
      {widgetState.selectedIds.length > 0 && (
        <div className="mb-4">
          <Button variant="destructive" onClick={handleBulkDelete}>
            Delete {widgetState.selectedIds.length} Selected
          </Button>
        </div>
      )}

      {/* Task List */}
      <div className="space-y-2">
        {tasks.length === 0 ? (
          <p className="text-gray-400 text-center py-4">No tasks yet</p>
        ) : (
          tasks.map((task) => (
            <div
              key={task.id}
              className={`flex items-center gap-3 p-3 rounded-lg border ${
                widgetState.selectedIds.includes(task.id)
                  ? "bg-blue-50 border-blue-200"
                  : "border-gray-200"
              }`}
            >
              {/* Selection checkbox */}
              <button
                onClick={() => toggleSelection(task.id)}
                className={`w-5 h-5 rounded-full border-2 flex items-center justify-center ${
                  widgetState.selectedIds.includes(task.id)
                    ? "border-blue-500 bg-blue-100"
                    : "border-gray-300"
                }`}
              >
                {widgetState.selectedIds.includes(task.id) && "●"}
              </button>

              {/* Complete button */}
              <Button
                variant={task.done ? "secondary" : "primary"}
                size="sm"
                onClick={() => handleComplete(task.id)}
              >
                {task.done ? "Undo" : "✓"}
              </Button>

              {/* Task title */}
              <span className={`flex-1 ${task.done ? "line-through text-gray-400" : ""}`}>
                {task.title}
              </span>

              {/* Status badge */}
              {task.done && <Badge variant="success">Done</Badge>}

              {/* Delete button */}
              <Button
                variant="destructive"
                size="sm"
                onClick={() => handleDelete(task.id)}
              >
                ×
              </Button>
            </div>
          ))
        )}
      </div>

      {/* Refresh button */}
      <Button className="mt-4 w-full" onClick={refresh}>
        Refresh
      </Button>
    </div>
  );
}
```

## Entry Point and Bundling

Create the entry point that renders your widget:

```tsx
// src/main.tsx
import { createRoot } from "react-dom/client";
import { TaskWidget } from "./TaskWidget";
import "./main.css";

const container = document.getElementById("root");
if (container) {
  createRoot(container).render(<TaskWidget />);
}
```

### Build Script

Add to `package.json`:

```json
{
  "scripts": {
    "build": "esbuild src/main.tsx --bundle --format=esm --outfile=dist/widget.js --loader:.css=css",
    "watch": "esbuild src/main.tsx --bundle --format=esm --outfile=dist/widget.js --loader:.css=css --watch"
  }
}
```

Build the bundle:

```bash
npm run build
```

This creates `dist/widget.js`—a single file containing React, your components, and styles.

## Serving the React Widget

Update your FastMCP server to serve the bundled widget:

```python
from pathlib import Path

# Read the bundled widget
WIDGET_JS = Path("../web/dist/widget.js").read_text()

WIDGET_HTML = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <div id="root"></div>
  <script type="module">{WIDGET_JS}</script>
</body>
</html>'''
```

Or serve the JS file separately and reference it:

```python
WIDGET_HTML = '''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
</head>
<body>
  <div id="root"></div>
  <script type="module" src="https://your-domain.com/widget.js"></script>
</body>
</html>'''
```

## Vanilla JS vs React: When to Use Each

| Scenario | Recommendation |
|----------|----------------|
| Simple display widget | Vanilla JS |
| Complex state management | React |
| Team project | React (consistent patterns) |
| Quick prototype | Vanilla JS |
| Production app | React + apps-sdk-ui |
| Learning ChatGPT Apps | Start with Vanilla JS, then React |

Both approaches use the same `window.openai` API. React just provides better organization for complex widgets.

## Summary

You learned the React approach to ChatGPT Apps:

| Concept | Purpose |
|---------|---------|
| `@openai/apps-sdk-ui` | Official component library matching ChatGPT design |
| `useOpenAiGlobal` | Subscribe to `window.openai` values reactively |
| `useWidgetState` | Persistent state across conversation turns |
| esbuild bundling | Single-file output for widget embedding |

The underlying architecture remains the same—MCP server returning `text/html+skybridge` widgets. React is just a better way to build complex widget UIs.

## Try With AI

### Prompt 1: Add Dark Mode Support

```
The TaskWidget has a theme variable from useOpenAiGlobal("theme"). Update all components to properly support dark mode. Use Tailwind's dark: prefix classes. The widget should automatically match ChatGPT's current theme.
```

**What you're learning:** Responsive theming using ChatGPT's theme signal.

### Prompt 2: Create a Custom Hook

```
Create a useTaskActions hook that encapsulates all the task operations (complete, delete, add, refresh). It should return { completeTask, deleteTask, addTask, refresh } functions. Update TaskWidget to use this hook instead of inline handlers.
```

**What you're learning:** Custom hooks for reusable logic—a React best practice.

### Prompt 3: Add Display Mode Toggle

```
Add a button that toggles between inline and fullscreen display modes using window.openai.requestDisplayMode. Show different UI layouts based on the current displayMode from useOpenAiGlobal("displayMode").
```

**What you're learning:** Integrating display mode controls with React state.
