---
sidebar_position: 1
title: "Promises and async/await"
description: "Master TypeScript's async model by comparing it to Python's asyncio. Learn Promise anatomy, async functions, await, and error propagation—all without event loop management."
keywords: ["TypeScript async", "Promises", "async await", "Python asyncio comparison", "JavaScript concurrency", "await"]
chapter: 74
lesson: 1
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Promise Fundamentals"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can explain Promise states (pending, fulfilled, rejected) and when each occurs"

  - name: "Async Function Declaration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can write async functions that return Promises and use await correctly"

  - name: "Python-TypeScript Async Comparison"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Technical Problem-Solving"
    measurable_at_this_level: "Student can identify differences between asyncio and TypeScript async model"

  - name: "Async Error Handling"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can handle rejected Promises using try/catch in async functions"

learning_objectives:
  - objective: "Explain the three states of a Promise and describe when each state applies"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student correctly identifies Promise states in code scenarios"

  - objective: "Write async functions that return Promises and use await to pause execution"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates working async function that awaits an async operation"

  - objective: "Compare TypeScript's async model to Python's asyncio and identify the key simplification"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student articulates why TypeScript doesn't need asyncio.run()"

  - objective: "Handle errors in async functions using try/catch blocks"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student writes error-handling code for rejected Promises"

cognitive_load:
  new_concepts: 6
  assessment: "6 new concepts (Promise, pending/fulfilled/rejected states, async keyword, await keyword, automatic Promise wrapping, try/catch for async) within A2-B1 limit of 7-10 concepts - PASS"

differentiation:
  extension_for_advanced: "Explore Promise.all, Promise.race, and Promise.allSettled for concurrent operations. Compare TypeScript's single-threaded event loop to Python's asyncio event loop internals."
  remedial_for_struggling: "Focus on the Python comparison first. If Promises feel abstract, work through the Python asyncio example then translate line-by-line to TypeScript."

generated_by: content-implementer
source_spec: chapter-62-readme
created: 2025-01-01
last_modified: 2025-01-01
version: 1.0.0
---

# Promises and async/await

Every AI application you'll build involves waiting. Waiting for API responses. Waiting for model inference. Waiting for streaming tokens to arrive. In Python, you managed this with asyncio—event loops, `await asyncio.gather()`, `asyncio.run()`. TypeScript handles the same challenge, but with a simpler model.

When a user sends a chat message to your AI interface, your code needs to call an API, wait for the response, then display it. That "wait" is what async programming manages. If you block the main thread waiting, everything freezes—the UI becomes unresponsive, other requests can't be processed. Async programming lets you start the wait, do other work, and resume when the response arrives.

You already understand this from Python's asyncio. The concepts transfer directly. But TypeScript's syntax is cleaner, and there's no event loop to manage explicitly. Let's see how.

## The Python Async Model You Know

Here's a typical Python asyncio pattern:

```python
import asyncio

async def fetch_data() -> str:
    await asyncio.sleep(1)  # Simulate API delay
    return "data from API"

async def main():
    result = await fetch_data()
    print(result)

# You MUST run this way
asyncio.run(main())
```

**Output:**
```
data from API
```

Three pieces make this work:
1. `async def` declares a coroutine function
2. `await` pauses execution until the awaited operation completes
3. `asyncio.run()` creates and runs the event loop

That last part—managing the event loop—is where Python gets verbose. You can't just call `main()` directly. You need the runtime to set up the async context.

## TypeScript's Simpler Model

TypeScript uses the same `async` and `await` keywords, but the runtime handles the event loop automatically. No `asyncio.run()` required:

```typescript
async function fetchData(): Promise<string> {
  await new Promise(resolve => setTimeout(resolve, 1000));  // Simulate API delay
  return "data from API";
}

async function main(): Promise<void> {
  const result = await fetchData();
  console.log(result);
}

// Just call it directly
main();
```

**Output:**
```
data from API
```

The key difference: **you call `main()` directly**. Node.js (and browsers) already have an event loop running. You don't create or manage it—you just write async code and it works.

| Python asyncio | TypeScript |
|----------------|------------|
| Explicit event loop management | Event loop built into runtime |
| `asyncio.run(main())` | `main()` |
| Returns coroutine object | Returns Promise object |
| `await asyncio.gather()` for concurrent | `await Promise.all()` for concurrent |

## Promise Anatomy: The Three States

A **Promise** represents a value that may not exist yet. Every Promise is in exactly one of three states:

```
┌─────────────────────────────────────────────────────────────┐
│                        PROMISE                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   PENDING ────────────► FULFILLED                           │
│      │                     (with a value)                   │
│      │                                                      │
│      └─────────────────► REJECTED                           │
│                            (with an error)                  │
│                                                             │
│   A Promise starts PENDING and transitions ONCE             │
│   to either FULFILLED or REJECTED. Never both.              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Pending**: The async operation is in progress. Think of this as "the API call is in flight."

**Fulfilled**: The operation succeeded. The Promise now holds a value.

**Rejected**: The operation failed. The Promise holds an error.

Here's a Promise that demonstrates all three states:

```typescript
// Create a Promise that resolves after 1 second
const myPromise: Promise<string> = new Promise((resolve, reject) => {
  console.log("Promise state: PENDING");

  setTimeout(() => {
    const success = Math.random() > 0.5;

    if (success) {
      resolve("Operation succeeded!");  // Transitions to FULFILLED
    } else {
      reject(new Error("Operation failed!"));  // Transitions to REJECTED
    }
  }, 1000);
});

// Handle the result
myPromise
  .then(value => console.log("FULFILLED:", value))
  .catch(error => console.log("REJECTED:", error.message));
```

**Output (one of two possibilities):**
```
Promise state: PENDING
FULFILLED: Operation succeeded!
```

or

```
Promise state: PENDING
REJECTED: Operation failed!
```

## Async Functions Return Promises Automatically

When you mark a function `async`, it automatically wraps the return value in a Promise:

```typescript
// These two functions are equivalent:

// Explicit Promise
function getDataExplicit(): Promise<string> {
  return Promise.resolve("hello");
}

// Async function (automatically returns Promise)
async function getDataAsync(): Promise<string> {
  return "hello";  // Automatically wrapped in Promise.resolve()
}
```

**Output (for both):**
```
Promise { 'hello' }
```

The `async` keyword does two things:
1. Makes the function return a Promise (even if you return a plain value)
2. Enables the `await` keyword inside that function

## Await Pauses Execution

The `await` keyword pauses async function execution until a Promise resolves:

```typescript
async function sequential(): Promise<void> {
  console.log("1: Starting");

  await new Promise(resolve => setTimeout(resolve, 1000));
  console.log("2: After first wait");

  await new Promise(resolve => setTimeout(resolve, 1000));
  console.log("3: After second wait");

  console.log("4: Done");
}

sequential();
console.log("5: Function called (but not awaited at top level)");
```

**Output:**
```
1: Starting
5: Function called (but not awaited at top level)
2: After first wait
3: After second wait
4: Done
```

Notice "5: Function called..." appears before "2: After first wait". The `await` inside `sequential()` pauses *that function*, but the caller continues immediately because we didn't await `sequential()` at the top level.

This is the fundamental model: `await` pauses the current function, not the entire program. Other code can run while you wait.

## Error Propagation in Async Functions

When a Promise rejects, the error propagates through `await`. Use try/catch to handle it:

```typescript
async function fetchUserData(userId: string): Promise<{ name: string }> {
  // Simulate an API that might fail
  if (userId === "invalid") {
    throw new Error("User not found");
  }
  return { name: "Alice" };
}

async function displayUser(userId: string): Promise<void> {
  try {
    const user = await fetchUserData(userId);
    console.log(`User name: ${user.name}`);
  } catch (error) {
    if (error instanceof Error) {
      console.log(`Error: ${error.message}`);
    }
  }
}

// Test both cases
displayUser("123");    // Works
displayUser("invalid");  // Errors gracefully
```

**Output:**
```
User name: Alice
Error: User not found
```

In Python, you'd use the same try/except pattern:

```python
async def display_user(user_id: str) -> None:
    try:
        user = await fetch_user_data(user_id)
        print(f"User name: {user['name']}")
    except Exception as e:
        print(f"Error: {e}")
```

The TypeScript version is nearly identical—`try/catch` instead of `try/except`, `instanceof Error` for type narrowing.

## Side-by-Side: Python vs TypeScript

Here's a complete comparison showing equivalent async patterns:

| Concept | Python | TypeScript |
|---------|--------|------------|
| Declare async function | `async def foo():` | `async function foo():` |
| Return type annotation | `-> str` | `: Promise<string>` |
| Await a coroutine/Promise | `await fetch()` | `await fetch()` |
| Sleep/delay | `await asyncio.sleep(1)` | `await new Promise(r => setTimeout(r, 1000))` |
| Run top-level | `asyncio.run(main())` | `main()` |
| Handle errors | `try/except` | `try/catch` |
| Concurrent execution | `await asyncio.gather(a(), b())` | `await Promise.all([a(), b()])` |

The key simplification: TypeScript has no equivalent to `asyncio.run()`. The runtime manages the event loop for you.

## Practical Example: Simulated API Call

Let's build something closer to real AI development—a function that simulates calling an API with variable latency:

```typescript
// Simulate an AI API call with random latency
async function callAI(prompt: string): Promise<string> {
  const latency = Math.random() * 2000 + 500;  // 500-2500ms
  console.log(`Calling AI with prompt: "${prompt}" (will take ${Math.round(latency)}ms)`);

  await new Promise(resolve => setTimeout(resolve, latency));

  // Simulate response
  return `AI response to: ${prompt}`;
}

async function chat(): Promise<void> {
  console.log("Starting chat session...\n");

  // Sequential calls (each waits for the previous)
  const response1 = await callAI("Hello");
  console.log(`Received: ${response1}\n`);

  const response2 = await callAI("How are you?");
  console.log(`Received: ${response2}\n`);

  console.log("Chat session complete.");
}

chat();
```

**Output:**
```
Starting chat session...

Calling AI with prompt: "Hello" (will take 1247ms)
Received: AI response to: Hello

Calling AI with prompt: "How are you?" (will take 892ms)
Received: AI response to: How are you?

Chat session complete.
```

This pattern—sequential await calls—is exactly how you'll structure multi-turn AI conversations. Each message waits for the previous response before sending the next.

## What TypeScript Async Gives You

Compared to Python's asyncio:

**Simpler**: No event loop management. No `asyncio.run()`. Just write async code and run it.

**Same concepts**: If you understand coroutines and await from Python, you understand Promises and await in TypeScript. The mental model transfers.

**Better for UI**: In browsers and Node.js, the event loop integrates with the rendering/request cycle automatically. Your async code meshes with the environment.

**Trade-off**: Less control. Python's explicit event loop lets you do advanced things (custom executors, multiple loops). TypeScript's model is simpler but less flexible for edge cases.

For AI interfaces—streaming responses, handling API calls, managing user interactions—TypeScript's simpler model is usually what you want.

## Try With AI

### Prompt 1: Convert Python to TypeScript

```
I have this Python asyncio code:

import asyncio

async def fetch_weather(city: str) -> dict:
    await asyncio.sleep(1)  # Simulate API
    return {"city": city, "temp": 72}

async def main():
    result = await fetch_weather("Seattle")
    print(result)

asyncio.run(main())

Convert this to TypeScript. Explain what changes and what stays the same.
```

**What you're learning:** Direct translation between Python asyncio and TypeScript async patterns—identifying the 1:1 mappings and the key difference (no asyncio.run needed).

### Prompt 2: Promise State Exploration

```
Create a TypeScript function called observePromise that:
1. Takes a Promise as input
2. Logs when the Promise starts (pending)
3. Logs when it resolves or rejects (with the value or error)
4. Returns the original Promise

Show how Promise states transition over time.
```

**What you're learning:** Deep understanding of Promise lifecycle by observing state transitions in real code.

### Prompt 3: Error Handling Patterns

```
I'm building an AI chat function that calls an API.
Sometimes the API times out or returns errors.

Write an async function that:
- Calls a simulated AI API
- Has a 30% chance of throwing an error
- Uses try/catch to handle failures gracefully
- Returns either the response or a fallback message

What's the TypeScript best practice for typing the error in the catch block?
```

**What you're learning:** Practical error handling in async contexts—a pattern you'll use constantly when building AI interfaces that call external APIs.

---

**Safety note**: When working with Promises in production AI code, always handle rejections. Unhandled Promise rejections can crash Node.js processes and leave users with broken interfaces. The try/catch patterns in this lesson are not optional—they're essential for reliable AI applications.
