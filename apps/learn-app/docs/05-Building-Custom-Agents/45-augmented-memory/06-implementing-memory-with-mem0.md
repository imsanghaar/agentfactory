---
sidebar_position: 6
title: "Implementing Memory with Mem0"
description: "Build production-ready agent memory using Mem0's open-source SDK. Learn to add, search, and filter memories, then integrate with FastAPI to create a memory-augmented Task API."
keywords: [Mem0, memory implementation, add memory, search memory, filters, metadata, FastAPI integration, Task API]
chapter: 45
lesson: 6
duration_minutes: 35

# HIDDEN SKILLS METADATA
skills:
  - name: "Mem0 SDK Usage"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can install, configure, and use Mem0 SDK for memory operations"

  - name: "Memory Add Operations"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can add memories from conversations with appropriate metadata"

  - name: "Memory Search with Filters"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can search memories using semantic queries and metadata filters"

  - name: "FastAPI Memory Integration"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can integrate Mem0 into FastAPI endpoints for the Task API"

learning_objectives:
  - objective: "Install and configure Mem0 with default settings and custom configurations"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successfully initialize Memory instance with custom config"

  - objective: "Add memories from conversation history with user scoping and metadata"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Store memories with proper user_id and metadata"

  - objective: "Search memories using semantic queries and metadata filters"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Retrieve relevant memories for given query and filters"

  - objective: "Integrate Mem0 into FastAPI Task API for memory-augmented task management"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Build endpoint that uses memory to personalize responses"

cognitive_load:
  new_concepts: 6
  assessment: "High cognitive load with 6 new concepts but extended duration (35 min). Practical code examples provide scaffolding. Builds directly on conceptual foundation from L01-L05."

differentiation:
  extension_for_advanced: "Implement custom LLM and vector store configurations; add async memory operations; build memory-aware middleware"
  remedial_for_struggling: "Focus on basic add/search first; use interactive REPL to experiment; reference the skill for patterns"
---

# Implementing Memory with Mem0

You've learned why agents need memory, how to architect memory systems, and strategies for retrieval and context management. Now it's time to build.

Mem0 is an open-source memory layer that handles the infrastructure—embeddings, vector storage, and retrieval—so you can focus on what matters: using memory to make your agents smarter. In this lesson, you'll go from zero to a working memory-augmented Task API.

## Installation and Setup

### Install Mem0

```bash
pip install mem0ai
```

### Configure OpenAI API Key

Mem0 uses OpenAI by default for embeddings and fact extraction:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

### Initialize Memory

```python
from mem0 import Memory

# Default configuration
m = Memory()
```

**Output:**
```
Memory initialized with:
- LLM: OpenAI gpt-4.1-nano-2025-04-14
- Embeddings: text-embedding-3-small (1536 dims)
- Vector Store: Qdrant (on-disk at /tmp/qdrant)
```

That's it. One line and you have a working memory system.

## Basic Memory Operations

### Adding Memories

Store conversations and let Mem0 extract the facts:

```python
from mem0 import Memory

m = Memory()

# A conversation to remember
messages = [
    {"role": "user", "content": "Hi, I'm Alex. I love basketball and gaming."},
    {"role": "assistant", "content": "Hey Alex! Great to meet you. I'll remember your interests."}
]

# Add to memory, scoped to user
result = m.add(messages, user_id="alex")
print(result)
```

**Output:**
```python
{
    'results': [
        {
            'id': 'mem_a1b2c3d4',
            'memory': 'Name is Alex. Enjoys basketball and gaming.',
            'event': 'ADD'
        }
    ]
}
```

Notice: Mem0 extracted the key facts from the conversation. You don't store raw messages—you store distilled knowledge.

### Searching Memories

Retrieve memories using natural language queries:

```python
# Search for what we know about the user
results = m.search("What do you know about me?", user_id="alex")
print(results)
```

**Output:**
```python
{
    'results': [
        {
            'id': 'mem_a1b2c3d4',
            'memory': 'Name is Alex. Enjoys basketball and gaming.',
            'user_id': 'alex',
            'score': 0.89,
            'created_at': '2025-01-20T10:30:00Z'
        }
    ]
}
```

The search is semantic—"What do you know about me?" matches memories about the user's identity and interests, not just keyword matches.

### Adding with Metadata

Attach metadata for filtered retrieval:

```python
# Add memory with category metadata
m.add(
    [
        {"role": "user", "content": "I prefer tasks scheduled in the morning."},
        {"role": "assistant", "content": "Noted! I'll prioritize morning for your tasks."}
    ],
    user_id="alex",
    metadata={
        "category": "preferences",
        "domain": "task-management"
    }
)

# Add another memory with different category
m.add(
    [
        {"role": "user", "content": "I'm working on the Phoenix project."},
        {"role": "assistant", "content": "Got it—Phoenix project is your current focus."}
    ],
    user_id="alex",
    metadata={
        "category": "projects",
        "domain": "task-management"
    }
)
```

**Output:**
```python
# First add
{'results': [{'id': 'mem_e5f6g7h8', 'memory': 'Prefers tasks scheduled in morning.'}]}

# Second add
{'results': [{'id': 'mem_i9j0k1l2', 'memory': 'Currently working on Phoenix project.'}]}
```

### Filtering by Metadata

Search within specific categories:

```python
# Get only preferences
preferences = m.search(
    "task preferences",
    user_id="alex",
    filters={"category": "preferences"}
)
print("Preferences:", preferences['results'])

# Get only projects
projects = m.search(
    "current work",
    user_id="alex",
    filters={"category": "projects"}
)
print("Projects:", projects['results'])
```

**Output:**
```
Preferences: [{'memory': 'Prefers tasks scheduled in morning.', 'score': 0.91}]
Projects: [{'memory': 'Currently working on Phoenix project.', 'score': 0.88}]
```

### Complex Filters

Combine multiple filter conditions:

```python
# Get memories matching multiple criteria
results = m.search(
    "work patterns",
    filters={
        "AND": [
            {"user_id": "alex"},
            {"category": "preferences"},
            {"created_at": {"gte": "2025-01-01"}}
        ]
    }
)
```

### Updating Memories

Modify existing memories:

```python
# Update a memory
m.update(
    memory_id="mem_e5f6g7h8",
    data="Prefers tasks scheduled in afternoon (updated from morning)."
)
```

### Deleting Memories

Remove memories when needed:

```python
# Delete single memory
m.delete(memory_id="mem_a1b2c3d4")

# Delete all memories for a user (for GDPR compliance)
all_memories = m.search("", user_id="alex", limit=1000)
for mem in all_memories['results']:
    m.delete(mem['id'])
```

## Integrating with Task API

Now let's integrate Mem0 into the Task API from Chapter 40.

### Project Structure

```
task-api/
├── main.py           # FastAPI application
├── memory.py         # Memory integration
├── models.py         # Pydantic models
└── requirements.txt
```

### Memory Module

Create `memory.py`:

```python
from mem0 import Memory

# Initialize shared memory instance
memory = Memory()

async def get_user_preferences(user_id: str) -> dict:
    """Retrieve user preferences from memory."""
    results = memory.search(
        "task preferences and working style",
        user_id=user_id,
        filters={"category": "preferences"},
        limit=5
    )

    preferences = {}
    for mem in results.get('results', []):
        # Parse preferences from memory text
        text = mem['memory'].lower()
        if 'morning' in text:
            preferences['preferred_time'] = 'morning'
        elif 'afternoon' in text:
            preferences['preferred_time'] = 'afternoon'
        elif 'evening' in text:
            preferences['preferred_time'] = 'evening'

    return preferences

async def get_project_context(user_id: str, task_title: str) -> list:
    """Retrieve relevant project context for a task."""
    results = memory.search(
        f"projects related to {task_title}",
        user_id=user_id,
        filters={"category": "projects"},
        limit=3
    )
    return results.get('results', [])

async def store_interaction(user_id: str, messages: list, category: str = "interactions"):
    """Store a new interaction in memory."""
    return memory.add(
        messages,
        user_id=user_id,
        metadata={"category": category}
    )
```

### FastAPI Integration

Create `main.py`:

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
from memory import memory, get_user_preferences, get_project_context, store_interaction

app = FastAPI(title="Memory-Augmented Task API")

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "normal"
    category: Optional[str] = None

class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    priority: str
    scheduled_time: Optional[str]
    context: Optional[str]

# In-memory task store (use database in production)
tasks = {}
task_counter = 0

@app.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate, user_id: str):
    """Create a task with memory-augmented personalization."""
    global task_counter

    # 1. Get user preferences from memory
    preferences = await get_user_preferences(user_id)

    # 2. Get relevant project context
    context_memories = await get_project_context(user_id, task.title)
    context = None
    if context_memories:
        context = context_memories[0]['memory']

    # 3. Apply preferences to task
    scheduled_time = preferences.get('preferred_time', 'unscheduled')

    # 4. Create task
    task_counter += 1
    task_id = f"task_{task_counter}"
    tasks[task_id] = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "scheduled_time": scheduled_time,
        "context": context,
        "user_id": user_id
    }

    # 5. Store interaction in memory
    await store_interaction(
        user_id=user_id,
        messages=[
            {"role": "user", "content": f"Created task: {task.title}"},
            {"role": "assistant", "content": f"Task created and scheduled for {scheduled_time}"}
        ],
        category="task_creation"
    )

    return TaskResponse(**tasks[task_id])

@app.get("/tasks/{task_id}")
async def get_task(task_id: str, user_id: str):
    """Get a task with memory-augmented context."""
    if task_id not in tasks:
        return {"error": "Task not found"}

    task = tasks[task_id]

    # Get any relevant memories about this task
    memories = memory.search(
        task["title"],
        user_id=user_id,
        limit=3
    )

    return {
        **task,
        "related_memories": [m['memory'] for m in memories.get('results', [])]
    }

@app.post("/preferences")
async def set_preference(user_id: str, preference: str):
    """Store a user preference."""
    await store_interaction(
        user_id=user_id,
        messages=[
            {"role": "user", "content": preference},
            {"role": "assistant", "content": "I'll remember that preference."}
        ],
        category="preferences"
    )
    return {"status": "stored", "preference": preference}
```

### Testing the Integration

Create `test_memory_api.py`:

```python
import httpx
import asyncio

async def test_memory_workflow():
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        user_id = "alex"

        # 1. Set a preference
        print("Setting preference...")
        response = await client.post(
            "/preferences",
            params={"user_id": user_id, "preference": "I prefer tasks in the morning"}
        )
        print(f"  Result: {response.json()}")

        # 2. Create a task (should be scheduled for morning)
        print("\nCreating task...")
        response = await client.post(
            "/tasks",
            params={"user_id": user_id},
            json={"title": "Review PR #123", "priority": "high"}
        )
        task = response.json()
        print(f"  Task created: {task['title']}")
        print(f"  Scheduled: {task['scheduled_time']}")  # Should be "morning"

        # 3. Create another task
        print("\nCreating second task...")
        response = await client.post(
            "/tasks",
            params={"user_id": user_id},
            json={"title": "Phoenix project standup", "category": "meetings"}
        )
        task2 = response.json()
        print(f"  Task created: {task2['title']}")
        print(f"  Context: {task2.get('context', 'None')}")

asyncio.run(test_memory_workflow())
```

**Output:**
```
Setting preference...
  Result: {'status': 'stored', 'preference': 'I prefer tasks in the morning'}

Creating task...
  Task created: Review PR #123
  Scheduled: morning

Creating second task...
  Task created: Phoenix project standup
  Context: Currently working on Phoenix project.
```

The agent remembered the user's preference and automatically scheduled the task for morning. It also connected the new task to existing project context.

## Testing Memory Across Sessions

The key test: does memory persist across application restarts?

```python
# Session 1: Store preference
from mem0 import Memory
m = Memory()
m.add(
    [{"role": "user", "content": "My name is Alex and I'm a senior engineer."}],
    user_id="alex"
)
print("Session 1: Stored preference")

# Simulate restart by creating new Memory instance
# (In production, restart your application)

# Session 2: Retrieve preference
from mem0 import Memory
m2 = Memory()  # Fresh instance
results = m2.search("Who is Alex?", user_id="alex")
print(f"Session 2: {results['results'][0]['memory']}")
```

**Output:**
```
Session 1: Stored preference
Session 2: Name is Alex. Senior engineer.
```

Memory persists across sessions because Mem0 stores data on disk (in `/tmp/qdrant` by default).

## Try With AI

Use these prompts to practice Mem0 integration with Claude or your preferred AI assistant.

### Prompt 1: Memory Lifecycle Design

```
I'm building a Task API with Mem0 integration. Design the memory lifecycle:

When a user creates a task:
1. What memories should we retrieve before creating?
2. What memories should we store after creating?
3. What metadata should we attach?

When a user completes a task:
1. What memories should we update?
2. What patterns should we extract?
3. How do we store duration/effort data for future estimates?

Show example code for both operations using Mem0's add() and search().
```

**What you're learning:** Memory isn't just about storing—it's about the full lifecycle. Creating a task triggers retrieval (for context) and storage (for history). Completing a task triggers pattern extraction.

### Prompt 2: Schema Design

```
Design a memory metadata schema for the Task API.

Memory categories needed:
- User preferences
- Project context
- Task patterns
- Interaction history

For each category:
1. What metadata fields should we store?
2. How would we filter for this category?
3. What's an example memory in this category?
4. How does this category connect to Task API endpoints?

Provide the complete schema and example queries.
```

**What you're learning:** Schema design determines how effectively you can filter and retrieve memories. Good categories map to your application's domain model.

### Prompt 3: Conflict Resolution

```
A user with existing memories says something that contradicts stored information:

Existing memory: "Prefers tasks in the morning"
New statement: "Actually, evenings work better for me now"

Using Mem0:
1. How do we detect this contradiction?
2. How do we update the old memory?
3. Should we keep history of the change?
4. How do we confirm the update with the user?

Show the complete code flow from detecting the contradiction to resolving it.
```

**What you're learning:** Real-world memory systems must handle contradictions gracefully. Mem0's update() and delete() operations enable conflict resolution, but the detection logic is your responsibility.
