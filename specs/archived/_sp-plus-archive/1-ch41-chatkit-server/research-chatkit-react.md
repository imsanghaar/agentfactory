# ChatKit.js React Integration Research

**Research Date**: 2025-12-31
**Purpose**: Gather accurate ChatKit React patterns for Chapter 41 Lesson 7

## Official Documentation Sources

- **Main Documentation**: https://openai.github.io/chatkit-js/
- **OpenAI Platform Guide**: https://platform.openai.com/docs/guides/chatkit
- **useChatKit API Reference**: https://openai.github.io/chatkit-js/api/openai/chatkit-react/functions/usechatkit/
- **GitHub Repository**: https://github.com/openai/chatkit-js
- **NPM Package**: @openai/chatkit-react

## useChatKit Hook

The useChatKit hook manages configuration and events for the ChatKit component.

### Basic Usage

```typescript
import { useChatKit, ChatKit } from '@openai/chatkit-react';

const { control, sendUserMessage } = useChatKit({
  api: {
    url: `${backendUrl}/chatkit`,
    domainKey: domainKey,
  },
});

return <ChatKit control={control} />;
```

### Return Values

- `control`: Control object passed to ChatKit component
- `sendUserMessage`: Function to programmatically send messages

## Custom Fetch Interceptor Pattern

To inject authentication and context:

```typescript
const { control } = useChatKit({
  api: {
    url: `${backendUrl}/chatkit`,
    domainKey: domainKey,

    fetch: async (url: string, options: RequestInit) => {
      // Inject auth headers
      // Modify request body to add metadata
      // Handle authentication checks

      return fetch(url, {
        ...options,
        headers: {
          ...options.headers,
          'X-User-ID': userId,
        },
      });
    },
  },
});
```

## Page Context Injection

Extract page information to provide agent context:

```typescript
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

## Script Loading Detection

ChatKit uses a web component that must be loaded before rendering:

```typescript
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
  });
}, []);

// Only render when ready
{isOpen && scriptStatus === 'ready' && <ChatKit control={control} />}
```

## Next.js Integration Patterns

### Script Loading (app/layout.tsx)

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

### httpOnly Cookie Proxy (app/api/chatkit/route.ts)

When auth tokens are in httpOnly cookies:

```typescript
import { NextRequest, NextResponse } from "next/server";
import { cookies } from "next/headers";

export async function POST(request: NextRequest) {
  const cookieStore = await cookies();
  const idToken = cookieStore.get("auth_token")?.value;

  if (!idToken) {
    return NextResponse.json({ error: "Not authenticated" }, { status: 401 });
  }

  const response = await fetch(`${API_BASE}/chatkit`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${idToken}`,
      "Content-Type": "application/json",
    },
    body: await request.text(),
  });

  // Handle SSE streaming
  if (response.headers.get("content-type")?.includes("text/event-stream")) {
    return new Response(response.body, {
      status: response.status,
      headers: {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
      },
    });
  }

  return NextResponse.json(await response.json(), { status: response.status });
}
```

## Metadata Injection Pattern

Inject context into request body:

```typescript
// Inside custom fetch interceptor
if (modifiedOptions.body && typeof modifiedOptions.body === 'string') {
  const parsed = JSON.parse(modifiedOptions.body);
  if (parsed.params?.input) {
    parsed.params.input.metadata = {
      userId,
      userInfo: { id: userId, name: user.name },
      pageContext: getPageContext(),
      ...parsed.params.input.metadata,
    };
    modifiedOptions.body = JSON.stringify(parsed);
  }
}
```

## Common Patterns

| Pattern | Use Case |
|---------|----------|
| Custom fetch | Authentication, context injection |
| Script detection | Wait for web component load |
| httpOnly proxy | Server-side auth token access |
| Page context | Inject page information for agent |
| Metadata injection | User identity, permissions |

## Notes for Lesson 7

**Focus Areas**:
- useChatKit hook configuration
- Custom fetch interceptor for auth
- Page context extraction patterns
- Script loading detection
- Next.js integration (Script component, API route proxy)
- Metadata injection for backend consumption

**Teaching Approach**:
- Start with basic useChatKit
- Add authentication layer
- Add context injection layer
- Handle edge cases (script loading, httpOnly cookies)
- Complete integration with Chapter 40 FastAPI backend patterns
