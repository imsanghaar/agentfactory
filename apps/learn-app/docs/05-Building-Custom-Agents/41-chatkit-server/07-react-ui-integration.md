---
sidebar_position: 7
title: "React UI Integration"
description: "Connect ChatKit UI to your backend with authentication, context injection, and Next.js integration patterns"
chapter: 41
lesson: 7
duration_minutes: 40

skills:
  - name: "useChatKit Hook Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student configures useChatKit to connect to custom backend with auth"

  - name: "Custom Fetch Interceptor"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student injects authentication headers and metadata via custom fetch"

  - name: "Page Context Extraction"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student extracts page title, headings, and metadata for agent context"

learning_objectives:
  - objective: "Configure useChatKit hook to connect React UI to custom ChatKit backend"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student's ChatKit component successfully communicates with backend"

  - objective: "Inject authentication and page context via custom fetch interceptor"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student's requests include auth headers and page metadata"

  - objective: "Handle Next.js integration patterns for script loading and httpOnly cookies"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student resolves script timing and cookie proxy issues"

cognitive_load:
  new_concepts: 9
  assessment: "Multiple integration patterns: useChatKit, custom fetch, context extraction, script loading, proxy pattern, auth injection, metadata, web components, Next.js lifecycle"

differentiation:
  extension_for_advanced: "Implement WebSocket fallback and retry logic"
  remedial_for_struggling: "Start with basic useChatKit before adding auth layers"
---

# React UI Integration

Your ChatKit server works, but users need a UI. ChatKit provides a React component—but you need to **connect it to your backend**, inject authentication, and provide page context so the agent knows what the user is viewing.

This lesson shows the complete integration: from basic setup to production authentication patterns.

---

## The Integration Challenge

Out of the box, ChatKit expects OpenAI's hosted endpoint. You need:

1. **Custom backend URL** — Point to your FastAPI server
2. **Authentication** — Inject user tokens (cookies can't be accessed from client)
3. **Page context** — Extract title, headings, URL for agent awareness
4. **Script loading** — Wait for web component before rendering
5. **Next.js compatibility** — Handle SSR, httpOnly cookies, API routes

**This lesson solves all five.**

---

## Step 1: Basic useChatKit Configuration

The `useChatKit` hook connects React to your backend.

**Installation** (if not already done):

```bash
npm install @openai/chatkit-react
```

**Basic Setup**:

```tsx
'use client';

import { useChatKit, ChatKit } from '@openai/chatkit-react';

export function ChatKitWidget() {
  const { control } = useChatKit({
    api: {
      url: 'http://localhost:8000/chatkit',  // Your backend
      domainKey: 'my-domain',                 // From Chapter 40
    },
  });

  return <ChatKit control={control} />;
}
```

**What this does**:
- Connects to your FastAPI backend at `/chatkit`
- Uses the domain key you configured in Chapter 40
- Returns a `control` object that manages the chat state

**Output** (browser):
```
Chat widget renders, but no authentication yet
```

---

## Step 2: Custom Fetch Interceptor for Authentication

ChatKit lets you override the `fetch` function to inject headers before requests.

**Problem**: Your backend expects `Authorization: Bearer <token>`, but tokens are in cookies (not accessible to JS if httpOnly).

**Solution 1: Non-httpOnly Tokens** (client-side access):

```tsx
const { control } = useChatKit({
  api: {
    url: 'http://localhost:8000/chatkit',
    domainKey: 'my-domain',

    fetch: async (url: string, options: RequestInit) => {
      // Get token from cookie (if not httpOnly)
      const token = getCookie('auth_token');

      return fetch(url, {
        ...options,
        headers: {
          ...options.headers,
          'Authorization': `Bearer ${token}`,
        },
      });
    },
  },
});

function getCookie(name: string): string | undefined {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop()?.split(';').shift();
}
```

**Output** (request headers):
```
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## Step 3: Page Context Extraction

Give your agent context about what the user is viewing.

**Pattern** (extract page metadata):

```tsx
const getPageContext = useCallback(() => {
  if (typeof window === 'undefined') return null;

  const metaDescription = document.querySelector('meta[name="description"]')
    ?.getAttribute('content') || '';

  const mainContent = document.querySelector('article') ||
                     document.querySelector('main') ||
                     document.body;

  const headings = Array.from(mainContent.querySelectorAll('h1, h2, h3'))
    .slice(0, 5)
    .map(h => h.textContent?.trim())
    .filter(Boolean)
    .join(', ');

  return {
    url: window.location.href,
    title: document.title,
    path: window.location.pathname,
    description: metaDescription,
    headings: headings,
  };
}, []);
```

**Inject into request**:

```tsx
fetch: async (url: string, options: RequestInit) => {
  const token = getCookie('auth_token');
  const pageContext = getPageContext();

  // Modify request body to include metadata
  let modifiedOptions = { ...options };

  if (modifiedOptions.body && typeof modifiedOptions.body === 'string') {
    const parsed = JSON.parse(modifiedOptions.body);

    if (parsed.params?.input) {
      parsed.params.input.metadata = {
        pageContext,
        ...parsed.params.input.metadata,
      };
      modifiedOptions.body = JSON.stringify(parsed);
    }
  }

  return fetch(url, {
    ...modifiedOptions,
    headers: {
      ...modifiedOptions.headers,
      'Authorization': `Bearer ${token}`,
    },
  });
},
```

**Backend receives** (in `metadata` field):

```json
{
  "pageContext": {
    "url": "https://example.com/docs/chapter-5",
    "title": "Understanding Decorators",
    "path": "/docs/chapter-5",
    "description": "Learn Python decorators with examples",
    "headings": "Understanding Decorators, What Are Decorators?, How Decorators Work"
  }
}
```

**Agent now knows**: User is on a Python decorators page, can tailor responses accordingly.

---

## Step 4: Next.js Script Loading Detection

ChatKit uses a web component (`<openai-chatkit>`). In Next.js, this script must load **before** rendering the component.

**Problem**: Rendering before script loads → blank widget.

**Solution** (wait for script):

```tsx
'use client';

import { useState, useEffect } from 'react';
import { useChatKit, ChatKit } from '@openai/chatkit-react';

export function ChatKitWidget() {
  const isBrowser = typeof window !== 'undefined';

  const [scriptStatus, setScriptStatus] = useState<'pending' | 'ready' | 'error'>(
    isBrowser && window.customElements?.get('openai-chatkit') ? 'ready' : 'pending'
  );

  useEffect(() => {
    if (!isBrowser || scriptStatus !== 'pending') return;

    if (window.customElements?.get('openai-chatkit')) {
      setScriptStatus('ready');
      return;
    }

    // Wait for web component to be defined
    customElements.whenDefined('openai-chatkit').then(() => {
      setScriptStatus('ready');
    }).catch(() => {
      setScriptStatus('error');
    });
  }, [isBrowser, scriptStatus]);

  const { control } = useChatKit({
    api: {
      url: 'http://localhost:8000/chatkit',
      domainKey: 'my-domain',
    },
  });

  if (scriptStatus === 'pending') return <div>Loading chat...</div>;
  if (scriptStatus === 'error') return <div>Chat unavailable</div>;

  return <ChatKit control={control} />;
}
```

**Load script in layout** (`app/layout.tsx`):

```tsx
import Script from "next/script";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        {/* MUST be beforeInteractive for web components */}
        <Script
          src="https://cdn.platform.openai.com/deployments/chatkit/chatkit.js"
          strategy="beforeInteractive"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

**Why `beforeInteractive`**: Web components must be defined before React hydration.

---

## Step 5: httpOnly Cookie Proxy (Production Pattern)

**Problem**: httpOnly cookies can't be accessed from client JavaScript (security best practice).

**Solution**: Create an API route that forwards requests with cookie-based auth.

**API Route** (`app/api/chatkit/route.ts`):

```typescript
import { NextRequest, NextResponse } from "next/server";
import { cookies } from "next/headers";

const API_BASE = process.env.BACKEND_URL || "http://localhost:8000";

export async function POST(request: NextRequest) {
  const cookieStore = await cookies();
  const idToken = cookieStore.get("auth_token")?.value;

  if (!idToken) {
    return NextResponse.json(
      { error: "Not authenticated" },
      { status: 401 }
    );
  }

  // Forward request to backend with auth
  const response = await fetch(`${API_BASE}/chatkit`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${idToken}`,
      "Content-Type": "application/json",
    },
    body: await request.text(),
  });

  // Handle SSE streaming (ChatKit uses Server-Sent Events)
  if (response.headers.get("content-type")?.includes("text/event-stream")) {
    return new Response(response.body, {
      status: response.status,
      headers: {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
      },
    });
  }

  return NextResponse.json(
    await response.json(),
    { status: response.status }
  );
}
```

**Update client to use proxy**:

```tsx
const { control } = useChatKit({
  api: {
    url: '/api/chatkit',  // Next.js API route (NOT backend directly)
    domainKey: 'my-domain',
  },
});
```

**Flow**:
1. ChatKit component → `/api/chatkit` (Next.js route)
2. API route reads httpOnly cookie
3. API route → FastAPI backend with `Authorization` header
4. Response streams back through API route to client

**Security**: Token never exposed to client JavaScript.

---

## Authentication Strategies Comparison

| Strategy | Security | Complexity | Use When |
|----------|----------|------------|----------|
| **Non-httpOnly Cookie** | Medium (XSS risk) | Low | Development, trusted environment |
| **httpOnly Proxy** | High (XSS-safe) | Medium | Production |
| **Session ID + Backend Lookup** | High | High | Enterprise (session store) |
| **OAuth Flow** | High | Very High | Multi-tenant SaaS |

**Recommended**: httpOnly proxy for production apps.

---

## Complete Integration Example

**Full component** (`components/ChatWidget.tsx`):

```tsx
'use client';

import { useState, useEffect, useCallback } from 'react';
import { useChatKit, ChatKit } from '@openai/chatkit-react';

export function ChatWidget() {
  const isBrowser = typeof window !== 'undefined';

  const [scriptStatus, setScriptStatus] = useState<'pending' | 'ready' | 'error'>(
    isBrowser && window.customElements?.get('openai-chatkit') ? 'ready' : 'pending'
  );

  useEffect(() => {
    if (!isBrowser || scriptStatus !== 'pending') return;

    if (window.customElements?.get('openai-chatkit')) {
      setScriptStatus('ready');
      return;
    }

    customElements.whenDefined('openai-chatkit').then(() => {
      setScriptStatus('ready');
    }).catch(() => {
      setScriptStatus('error');
    });
  }, [isBrowser, scriptStatus]);

  const getPageContext = useCallback(() => {
    if (typeof window === 'undefined') return null;

    const metaDescription = document.querySelector('meta[name="description"]')
      ?.getAttribute('content') || '';

    const mainContent = document.querySelector('article') ||
                       document.querySelector('main') ||
                       document.body;

    const headings = Array.from(mainContent.querySelectorAll('h1, h2, h3'))
      .slice(0, 5)
      .map(h => h.textContent?.trim())
      .filter(Boolean)
      .join(', ');

    return {
      url: window.location.href,
      title: document.title,
      path: window.location.pathname,
      description: metaDescription,
      headings: headings,
    };
  }, []);

  const { control } = useChatKit({
    api: {
      url: '/api/chatkit',  // Proxy route
      domainKey: 'my-domain',

      fetch: async (url: string, options: RequestInit) => {
        const pageContext = getPageContext();
        let modifiedOptions = { ...options };

        if (modifiedOptions.body && typeof modifiedOptions.body === 'string') {
          const parsed = JSON.parse(modifiedOptions.body);

          if (parsed.params?.input) {
            parsed.params.input.metadata = {
              pageContext,
              ...parsed.params.input.metadata,
            };
            modifiedOptions.body = JSON.stringify(parsed);
          }
        }

        return fetch(url, modifiedOptions);
      },
    },
  });

  if (scriptStatus === 'pending') return <div>Loading chat...</div>;
  if (scriptStatus === 'error') return <div>Chat unavailable</div>;

  return <ChatKit control={control} />;
}
```

**Backend receives**:

```python
@app.post("/chatkit")
async def chatkit_endpoint(request: Request):
    data = await request.json()

    # Access page context
    metadata = data.get("params", {}).get("input", {}).get("metadata", {})
    page_context = metadata.get("pageContext", {})

    print(f"User on page: {page_context.get('title')}")
    # "Understanding Decorators"
```

---

## Safety Note: httpOnly Cookies Prevent XSS Token Theft

**Without httpOnly**:
```javascript
// Malicious script can steal token
const token = document.cookie.match(/auth_token=([^;]+)/)[1];
sendToAttacker(token);
```

**With httpOnly**:
```javascript
// Returns empty string (cookie invisible to JavaScript)
const token = document.cookie.match(/auth_token=([^;]+)/); // null
```

**httpOnly cookies** prevent Cross-Site Scripting (XSS) attacks from stealing authentication tokens. The API route pattern lets you use httpOnly cookies while still authenticating backend requests.

---

## Try With AI

### Prompt 1: Inject User Authentication Headers

**Setup**: Your backend expects `X-User-ID` header.

**Prompt**:
```
Help me modify the custom fetch interceptor to inject a user ID header.
I have userId from useAuth() hook. The backend expects header: X-User-ID.
```

**Expected Outcome**:
```tsx
const { userId } = useAuth();

fetch: async (url, options) => {
  return fetch(url, {
    ...options,
    headers: {
      ...options.headers,
      'X-User-ID': userId,
    },
  });
},
```

**What you're learning**: Authentication patterns for custom backends.

---

### Prompt 2: Extract Page Context for Agent

**Setup**: Agent should know current page for contextual responses.

**Prompt**:
```
Extract page title, headings, and URL to inject into ChatKit requests.
I need to add this to the metadata field so my agent knows what page
the user is on.
```

**Expected Outcome**:
```tsx
const pageContext = {
  title: document.title,
  url: window.location.href,
  headings: Array.from(document.querySelectorAll('h1, h2')).map(h => h.textContent),
};

// Inject into metadata
parsed.params.input.metadata = { pageContext, ...metadata };
```

**What you're learning**: Context injection for agent awareness.

---

### Prompt 3: Debug Script Loading Issues in Next.js

**Setup**: ChatKit component renders blank.

**Prompt**:
```
My ChatKit component renders blank in Next.js. I suspect the web component
script hasn't loaded yet. How do I wait for customElements.whenDefined
before rendering?
```

**Expected Outcome**:
```tsx
const [ready, setReady] = useState(false);

useEffect(() => {
  customElements.whenDefined('openai-chatkit').then(() => setReady(true));
}, []);

return ready ? <ChatKit control={control} /> : <div>Loading...</div>;
```

**What you're learning**: Web component lifecycle in React frameworks.

---

## Validation Checklist

- [ ] useChatKit hook configured with custom backend URL
- [ ] Custom fetch interceptor injects authentication headers
- [ ] Page context extracted (title, headings, URL)
- [ ] Script loading detection waits for web component
- [ ] Next.js Script component loads ChatKit with `beforeInteractive`
- [ ] httpOnly cookie proxy route forwards auth to backend (if using httpOnly)
- [ ] Metadata injection visible in backend logs
- [ ] ChatKit component renders and connects successfully

---

## Next Steps

**Lesson 8**: State Management & Display Modes — Control when the widget appears and manage conversation state.

Your React UI now connects to your backend with authentication, context, and production-ready patterns. Next, you'll control **when and how** the widget appears.
