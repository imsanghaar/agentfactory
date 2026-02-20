---
sidebar_position: 9
title: "Chapter Quiz"
description: "Test your understanding of Apps SDK concepts for building ChatGPT Apps"
keywords: ["quiz", "assessment", "Apps SDK", "ChatGPT Apps", "React", "production security"]
chapter: 42
lesson: 9
---

# Chapter 42 Quiz: Apps SDK

Test your understanding of the Apps SDK concepts covered in this chapter. The quiz randomly selects 15-20 questions from a pool of 50, providing immediate feedback on each answer.

**Passing Score:** 80%

import Quiz from '@site/src/components/quiz';

<Quiz
  questions={[
    {
      question: "What are the three layers of the ChatGPT Apps architecture?",
      options: [
        "ChatGPT UI, Widget iframe, MCP Server",
        "Frontend, Backend, Database",
        "Client, API, Model",
        "Widget, Tool, Response"
      ],
      correctAnswer: 0,
      explanation: "The three-layer architecture consists of the ChatGPT UI (hosts everything), the Widget iframe (your visual code running in sandbox), and the MCP Server (your backend logic)."
    },
    {
      question: "What is the primary purpose of the Apps SDK compared to the Agents SDK?",
      options: [
        "Building backend agent logic with complex reasoning",
        "Building user-facing widgets with interactive HTML inside ChatGPT",
        "Creating multi-agent workflows and handoffs",
        "Implementing tool orchestration and chaining"
      ],
      correctAnswer: 1,
      explanation: "The Apps SDK is for building user-facing widgets that render rich HTML directly in ChatGPT, while the Agents SDK is for backend agent logic."
    },
    {
      question: "What MIME type tells ChatGPT to render HTML content as an interactive widget?",
      options: [
        "text/html",
        "application/json+widget",
        "text/html+skybridge",
        "text/widget+html"
      ],
      correctAnswer: 2,
      explanation: "The MIME type 'text/html+skybridge' is the special value that signals to ChatGPT: 'Render this content as an interactive widget, not as text.'"
    },
    {
      question: "In the Apps SDK architecture, where does the widget code run?",
      options: [
        "On your MCP server",
        "In the ChatGPT model",
        "In a sandboxed iframe within ChatGPT",
        "In the user's browser tab"
      ],
      correctAnswer: 2,
      explanation: "Widget code runs in a sandboxed iframe within ChatGPT for security. The iframe cannot access the parent ChatGPT page or other widgets."
    },
    {
      question: "What field in a tool response contains data that both the model AND the widget can see?",
      options: [
        "_meta",
        "structuredContent",
        "content",
        "widgetData"
      ],
      correctAnswer: 1,
      explanation: "structuredContent is visible to both the model (for narration) and the widget (via window.openai.toolOutput). It should contain concise summary data."
    },
    {
      question: "What field in a tool response contains data that ONLY the widget can see?",
      options: [
        "structuredContent",
        "_meta",
        "content",
        "privateData"
      ],
      correctAnswer: 1,
      explanation: "_meta is invisible to the model. Whatever you put there, the model cannot reference, summarize, or include in its response. It's ideal for large datasets or sensitive data."
    },
    {
      question: "How does a widget access data from the _meta field of a tool response?",
      options: [
        "window.openai.toolOutput",
        "window.openai.toolResponseMetadata",
        "window.openai.metaData",
        "window.openai.privateContent"
      ],
      correctAnswer: 1,
      explanation: "Data from _meta is accessed via window.openai.toolResponseMetadata, while structuredContent is accessed via window.openai.toolOutput."
    },
    {
      question: "Why should you use optional chaining (window.openai?.method) when accessing window.openai APIs?",
      options: [
        "For better performance",
        "Because window.openai doesn't exist outside ChatGPT, preventing errors during local development",
        "To enable async operations",
        "For TypeScript compatibility"
      ],
      correctAnswer: 1,
      explanation: "window.openai only exists inside ChatGPT. Using optional chaining prevents TypeError crashes when testing widgets locally in a browser where window.openai is undefined."
    },
    {
      question: "What does sendFollowUpMessage do in a widget?",
      options: [
        "Calls another MCP tool directly",
        "Inserts a message into the ChatGPT conversation as if the user typed it",
        "Saves widget state",
        "Changes the display mode"
      ],
      correctAnswer: 1,
      explanation: "sendFollowUpMessage inserts a message into the ChatGPT conversation as if the user typed it. The model then processes this message normally, potentially invoking tools or generating responses."
    },
    {
      question: "What does callTool do in a widget?",
      options: [
        "Inserts a message into the conversation",
        "Invokes another MCP tool directly, bypassing the model",
        "Saves widget state synchronously",
        "Requests a display mode change"
      ],
      correctAnswer: 1,
      explanation: "callTool invokes another MCP tool directly. Your widget talks directly to your MCP server without adding messages to the conversation or involving the model."
    },
    {
      question: "What metadata property must be set to true for a tool to be callable via window.openai.callTool?",
      options: [
        "readOnlyHint",
        "openWorldHint",
        "widgetAccessible",
        "callableFromWidget"
      ],
      correctAnswer: 2,
      explanation: "The 'openai/widgetAccessible': True metadata tells ChatGPT: 'Allow widgets to invoke this tool directly.' Without this, callTool calls fail silently."
    },
    {
      question: "When should you use sendFollowUpMessage instead of callTool?",
      options: [
        "When you need fresh data without conversation noise",
        "When the action benefits from natural language understanding or model reasoning",
        "When speed matters and you want to bypass model roundtrip",
        "When the action shouldn't appear in conversation history"
      ],
      correctAnswer: 1,
      explanation: "Use sendFollowUpMessage when you want the model to process the action (summaries, explanations, translations). Use callTool for pure data operations like refresh or load more."
    },
    {
      question: "What purpose does the ngrok tunnel serve in ChatGPT Apps development?",
      options: [
        "Compiles widget code",
        "Exposes your localhost server to the internet so ChatGPT can reach it",
        "Encrypts MCP tool responses",
        "Caches widget resources"
      ],
      correctAnswer: 1,
      explanation: "Your server runs on localhost, but ChatGPT needs a public URL. ngrok creates a secure tunnel from the internet to your local machine."
    },
    {
      question: "In ChatGPT Developer Mode, what URL path should be appended to your ngrok URL for the MCP Server URL?",
      options: [
        "/api",
        "/widget",
        "/mcp",
        "/tools"
      ],
      correctAnswer: 2,
      explanation: "The /mcp path is where FastMCP exposes its MCP protocol endpoint. Your MCP server URL should be https://[ngrok-url]/mcp."
    },
    {
      question: "What is the correct pattern for saving widget state?",
      options: [
        "Save state before triggering any action",
        "Save state immediately when it changes, before any potential reload",
        "Save state after the widget reloads",
        "Save state only when the user clicks a save button"
      ],
      correctAnswer: 1,
      explanation: "State must be saved immediately on change, not when an action triggers. The setWidgetState call must complete before any sendFollowUpMessage or other action that might cause the widget to reload."
    },
    {
      question: "How does a widget read previously saved state on initialization?",
      options: [
        "window.openai.getWidgetState()",
        "window.openai.widgetState",
        "window.openai.savedState",
        "localStorage.getItem('widgetState')"
      ],
      correctAnswer: 1,
      explanation: "When a widget initializes, it checks window.openai?.widgetState for previously saved state. This contains whatever was previously saved with setWidgetState."
    },
    {
      question: "Which display mode is typically coerced on mobile devices when fullscreen is requested?",
      options: [
        "inline",
        "pip (picture-in-picture)",
        "minimized",
        "compact"
      ],
      correctAnswer: 1,
      explanation: "Mobile devices can't truly go fullscreen within the ChatGPT app, so fullscreen requests get coerced to pip (picture-in-picture) mode."
    },
    {
      question: "What are the three display modes available for ChatGPT widgets?",
      options: [
        "small, medium, large",
        "inline, pip, fullscreen",
        "compact, normal, expanded",
        "minimized, windowed, maximized"
      ],
      correctAnswer: 1,
      explanation: "The three display modes are: inline (within conversation flow), pip (picture-in-picture, floating overlay), and fullscreen (expands to fill available space)."
    },
    {
      question: "What method is used to request a display mode change in a widget?",
      options: [
        "window.openai.setDisplayMode()",
        "window.openai.requestDisplayMode()",
        "window.openai.changeMode()",
        "window.openai.displayMode = value"
      ],
      correctAnswer: 1,
      explanation: "Use window.openai.requestDisplayMode({ mode: 'fullscreen' }) to request a display mode change. Note that the request may be coerced to a different mode based on platform constraints."
    },
    {
      question: "Why is setWidgetState synchronous rather than asynchronous?",
      options: [
        "For better performance",
        "Because it needs to complete before any action that might trigger a widget reload",
        "For compatibility with older browsers",
        "To prevent race conditions with callTool"
      ],
      correctAnswer: 1,
      explanation: "setWidgetState is synchronous so it can complete immediately after a state change, before any action (like sendFollowUpMessage) that might cause the widget to reload."
    },
    {
      question: "What should you put in structuredContent for a tool that returns a list of 500 items?",
      options: [
        "All 500 items for the model to summarize",
        "Only summary data (counts, totals, top items) for model narration",
        "Nothing - use _meta only",
        "A random sample of 50 items"
      ],
      correctAnswer: 1,
      explanation: "structuredContent should contain concise summary data for effective model narration. Put the full 500 items in _meta where only the widget can access them."
    },
    {
      question: "What property provides the current ChatGPT theme (light or dark) to a widget?",
      options: [
        "window.openai.colorScheme",
        "window.openai.theme",
        "window.openai.appearance",
        "window.openai.mode"
      ],
      correctAnswer: 1,
      explanation: "window.openai.theme returns 'light' or 'dark' indicating the current ChatGPT theme, allowing widgets to adapt their styling."
    },
    {
      question: "What is the primary purpose of the content field in a CallToolResult?",
      options: [
        "Widget-only data storage",
        "Optional text/markdown that influences model narration phrasing",
        "Large dataset storage",
        "Tool metadata configuration"
      ],
      correctAnswer: 1,
      explanation: "The content field provides optional text or markdown for the model to use in its narrative response. It's useful when you want specific phrasing."
    },
    {
      question: "Why do widgets run in sandboxed iframes?",
      options: [
        "For better performance",
        "For security - widgets cannot access the parent ChatGPT page or other widgets",
        "For compatibility with mobile devices",
        "To enable offline functionality"
      ],
      correctAnswer: 1,
      explanation: "Iframes are sandboxed for security. Your widget code runs isolated from the parent ChatGPT page, preventing potential security issues."
    },
    {
      question: "What happens when you use callTool on a tool that doesn't have widgetAccessible: true?",
      options: [
        "An error is thrown",
        "The call fails silently",
        "The tool runs but returns no data",
        "ChatGPT prompts for permission"
      ],
      correctAnswer: 1,
      explanation: "Without widgetAccessible: true metadata, callTool calls fail silently. This is a common debugging issue when buttons don't seem to work."
    },
    {
      question: "In the TaskManager implementation, which tools should have widgetAccessible: true?",
      options: [
        "Only list_tasks",
        "Only add_task and delete_task",
        "All four tools (list_tasks, add_task, complete_task, delete_task)",
        "None - widgets should only use sendFollowUpMessage"
      ],
      correctAnswer: 2,
      explanation: "All four TaskManager tools should have widgetAccessible: true so the widget can directly invoke any of them for data operations without conversation noise."
    },
    {
      question: "What is the purpose of the @mcp.resource decorator in FastMCP?",
      options: [
        "Defines a tool that can be called",
        "Registers a resource that serves widget HTML with the specified MIME type",
        "Configures authentication",
        "Sets up error handling"
      ],
      correctAnswer: 1,
      explanation: "The @mcp.resource decorator creates an MCP resource endpoint that serves widget HTML. The uri and mime_type parameters define how ChatGPT requests and renders the resource."
    },
    {
      question: "What should you check first if your ChatGPT app shows 'Disconnected' status?",
      options: [
        "Widget HTML syntax",
        "Whether ngrok is running and the URL matches what's registered in ChatGPT",
        "Tool parameter types",
        "Widget JavaScript code"
      ],
      correctAnswer: 1,
      explanation: "A 'Disconnected' status usually means ChatGPT can't reach your server. Check that ngrok is running and the registered URL matches the current ngrok URL."
    },
    {
      question: "How can you force ChatGPT to reload a cached widget during development?",
      options: [
        "Refresh the page",
        "Clear browser cache",
        "Delete and recreate the app with the new ngrok URL, then test in a new conversation",
        "Restart the MCP server"
      ],
      correctAnswer: 2,
      explanation: "ChatGPT aggressively caches widgets. The most reliable way to force reload is to delete and recreate the app with a fresh ngrok URL, then test in a new conversation."
    },
    {
      question: "What annotation indicates that a tool performs destructive operations?",
      options: [
        "readOnlyHint: false",
        "destructiveHint: true",
        "dangerousHint: true",
        "modifiesData: true"
      ],
      correctAnswer: 1,
      explanation: "The destructiveHint: true annotation marks a tool as performing destructive operations, like delete_task in the TaskManager."
    },
    {
      question: "What is the correct way to handle a button click that might fail in a widget?",
      options: [
        "Let the error propagate",
        "Use try/catch with visual feedback showing loading state and error handling",
        "Ignore errors silently",
        "Reload the widget automatically"
      ],
      correctAnswer: 1,
      explanation: "Use try/catch with visual feedback: show 'Loading...' during the operation, handle errors gracefully, and restore the button state in a finally block."
    },
    {
      question: "Why should large datasets be placed in _meta rather than structuredContent?",
      options: [
        "For better widget performance",
        "To reduce token consumption and prevent overwhelming model responses",
        "For security encryption",
        "To enable offline caching"
      ],
      correctAnswer: 1,
      explanation: "Large datasets in structuredContent consume model context tokens and may cause overwhelming responses. Putting them in _meta keeps them hidden from the model while still accessible to the widget."
    },
    {
      question: "What is the purpose of the listing_meta() function in TaskManager?",
      options: [
        "Returns all tasks as a list",
        "Provides widget information for tool discovery in ChatGPT",
        "Lists available API endpoints",
        "Returns tool usage statistics"
      ],
      correctAnswer: 1,
      explanation: "listing_meta() provides widget URI and title information so ChatGPT knows what widget to display when listing available tools."
    },
    {
      question: "What is the purpose of the response_meta() function in TaskManager?",
      options: [
        "Generates response statistics",
        "Creates the embedded widget resource to include in each tool response",
        "Validates response format",
        "Logs response data"
      ],
      correctAnswer: 1,
      explanation: "response_meta() creates the complete _meta dictionary including the embedded widget resource and full task data for widget rendering."
    },
    {
      question: "When a user clicks a checkbox in the TaskManager widget, which method is used?",
      options: [
        "sendFollowUpMessage - to let the model update the task",
        "callTool - to directly update the task without conversation noise",
        "setWidgetState - to save the checked state",
        "requestDisplayMode - to show completion animation"
      ],
      correctAnswer: 1,
      explanation: "Checkbox clicks use callTool to directly call complete_task. This updates the task without adding messages to the conversation, providing a smoother user experience."
    },
    {
      question: "What fallback does the TaskManager widget use if callTool is not available?",
      options: [
        "It disables the add button",
        "It uses sendFollowUpMessage to add tasks through conversation",
        "It stores tasks locally",
        "It shows an error message"
      ],
      correctAnswer: 1,
      explanation: "The TaskManager's addTask function checks for callTool first, but falls back to sendFollowUpMessage if it's not available, ensuring the feature still works."
    },
    {
      question: "What does the escapeHtml function in TaskManager prevent?",
      options: [
        "SQL injection",
        "XSS (cross-site scripting) attacks by escaping HTML in task titles",
        "URL encoding issues",
        "Unicode rendering problems"
      ],
      correctAnswer: 1,
      explanation: "escapeHtml prevents XSS attacks by ensuring task titles containing HTML characters are rendered as text, not executed as HTML code."
    },
    {
      question: "What happens to widget state when the user refreshes the ChatGPT page?",
      options: [
        "State persists indefinitely",
        "State is lost - widgetState only persists within a conversation session",
        "State is backed up to localStorage",
        "State is synced to the MCP server"
      ],
      correctAnswer: 1,
      explanation: "widgetState only persists within a conversation session. Refreshing the page or starting a new conversation loses the widget state. For cross-session persistence, you need server-side storage."
    },
    {
      question: "Which property provides the current display mode of a widget?",
      options: [
        "window.openai.currentMode",
        "window.openai.displayMode",
        "window.openai.viewMode",
        "window.openai.screenMode"
      ],
      correctAnswer: 1,
      explanation: "window.openai.displayMode returns the current display mode: 'inline', 'pip', or 'fullscreen'."
    },
    {
      question: "What is the recommended approach for debugging widget JavaScript issues?",
      options: [
        "Only use server-side logging",
        "Add a visual marker (like a colored div) early in the HTML to confirm loading, then use console.log",
        "Disable all JavaScript and test HTML only",
        "Use alert() statements"
      ],
      correctAnswer: 1,
      explanation: "Add a visible marker early in your HTML (like a red div) to confirm the HTML is loading. If you see it, HTML works but JavaScript is failing. Then use console.log for further debugging."
    },
    {
      question: "What should you do if tools are not appearing when you type @ in ChatGPT?",
      options: [
        "Restart your browser",
        "Check server logs for ListToolsRequest, verify ngrok URL, delete and recreate the app",
        "Update FastMCP version",
        "Clear widget state"
      ],
      correctAnswer: 1,
      explanation: "If tools don't appear, check server logs for ListToolsRequest (if absent, ChatGPT isn't connecting). Verify the ngrok URL is current, and delete/recreate the app with the correct URL."
    },
    {
      question: "What authentication method is recommended for production ChatGPT Apps with multiple users?",
      options: [
        "Basic authentication",
        "API keys in headers",
        "OAuth 2.1 with PKCE",
        "Session cookies"
      ],
      correctAnswer: 2,
      explanation: "OAuth 2.1 with PKCE is the recommended authentication method for multi-user ChatGPT Apps, providing secure user identity and session management."
    },
    {
      question: "Where should you host OAuth Protected Resource Metadata for a ChatGPT App?",
      options: [
        "/api/oauth",
        "/.well-known/oauth-protected-resource",
        "/auth/metadata",
        "/oauth/config.json"
      ],
      correctAnswer: 1,
      explanation: "OAuth Protected Resource Metadata should be hosted at /.well-known/oauth-protected-resource as per the standard."
    },
    {
      question: "What is the purpose of the annotations parameter in @mcp.tool decorator?",
      options: [
        "Adding code comments",
        "Providing tool metadata like title, hints (readOnly, destructive, openWorld), and security schemes",
        "Configuring rate limiting",
        "Setting up logging"
      ],
      correctAnswer: 1,
      explanation: "The annotations parameter provides tool metadata including title, readOnlyHint, destructiveHint, openWorldHint, and securitySchemes for ChatGPT to understand tool behavior."
    },
    {
      question: "What does openWorldHint: False indicate about a tool?",
      options: [
        "The tool requires authentication",
        "The tool only accesses controlled/internal resources, not external/public ones",
        "The tool is read-only",
        "The tool works offline"
      ],
      correctAnswer: 1,
      explanation: "openWorldHint: False indicates the tool only accesses controlled, internal resources. True would indicate it accesses external/public resources like web APIs."
    },
    {
      question: "In production deployment, what should replace the in-memory task storage?",
      options: [
        "Local file storage",
        "Browser localStorage",
        "A database (PostgreSQL, MongoDB, etc.)",
        "Session storage"
      ],
      correctAnswer: 2,
      explanation: "In production, in-memory storage should be replaced with a proper database for persistence, reliability, and multi-user support."
    },
    {
      question: "What is the recommended way to version widget URIs during development?",
      options: [
        "Add timestamps to HTML",
        "Include version in the URI (e.g., 'ui://widget/tasks-v2.html')",
        "Use query parameters",
        "Change port numbers"
      ],
      correctAnswer: 1,
      explanation: "Changing the widget URI (e.g., from tasks-v1.html to tasks-v2.html) forces ChatGPT to invalidate the cache and load the new version."
    },
    {
      question: "What is the key difference between how the model uses structuredContent vs _meta?",
      options: [
        "structuredContent is encrypted, _meta is not",
        "Model can read structuredContent for narration but cannot see _meta at all",
        "structuredContent is for errors, _meta is for success responses",
        "They are interchangeable"
      ],
      correctAnswer: 1,
      explanation: "The model reads structuredContent to generate its narrative response. _meta is completely invisible to the model - it's only accessible by the widget."
    },
    {
      question: "What should sensitive information like internal IDs, pricing logic, or business rules be placed in?",
      options: [
        "structuredContent",
        "content",
        "_meta",
        "A separate encrypted field"
      ],
      correctAnswer: 2,
      explanation: "Sensitive data should go in _meta so the model cannot reference, summarize, or include it in responses. This keeps business-sensitive information hidden from the conversation."
    },
    {
      question: "What is the purpose of the @openai/apps-sdk-ui package?",
      options: [
        "Backend API client for ChatGPT",
        "Official React component library matching ChatGPT's design system",
        "Testing framework for widgets",
        "MCP server scaffolding tool"
      ],
      correctAnswer: 1,
      explanation: "@openai/apps-sdk-ui is the official React component library providing Tailwind-integrated design tokens, buttons, badges, and layout primitives that match ChatGPT's styling."
    },
    {
      question: "What React hook subscribes to window.openai values reactively?",
      options: [
        "useState",
        "useEffect",
        "useOpenAiGlobal",
        "useContext"
      ],
      correctAnswer: 2,
      explanation: "useOpenAiGlobal subscribes to window.openai values (like toolOutput, theme, displayMode) and re-renders components when those values change."
    },
    {
      question: "What does the useWidgetState hook provide?",
      options: [
        "Server-side state management",
        "React state that automatically syncs with window.openai.widgetState for persistence",
        "Global Redux store integration",
        "URL-based state routing"
      ],
      correctAnswer: 1,
      explanation: "useWidgetState manages React state that hydrates from window.openai.widgetState and syncs changes back via setWidgetState for cross-turn persistence."
    },
    {
      question: "Which CSS framework is integrated with @openai/apps-sdk-ui?",
      options: [
        "Bootstrap 5",
        "Tailwind 4",
        "Material UI",
        "Chakra UI"
      ],
      correctAnswer: 1,
      explanation: "@openai/apps-sdk-ui is built with Tailwind 4 integration, providing pre-configured design tokens that match ChatGPT's styling."
    },
    {
      question: "What tool is recommended for bundling React widgets into a single file?",
      options: [
        "webpack",
        "rollup",
        "esbuild",
        "parcel"
      ],
      correctAnswer: 2,
      explanation: "esbuild is recommended for bundling React widgets into a single ESM file that can be embedded in MCP server responses."
    },
    {
      question: "What annotation controls which external domains a widget can make network requests to?",
      options: [
        "openai/widgetAccessible",
        "openai/widgetCSP",
        "openai/visibility",
        "openai/widgetDomain"
      ],
      correctAnswer: 1,
      explanation: "openai/widgetCSP (Content Security Policy) declares which external domains the widget can connect to via connect-src, img-src, frame-src, and redirect-src directives."
    },
    {
      question: "What does openai/widgetDomain annotation enable?",
      options: [
        "CORS restrictions",
        "Fullscreen mode, API allowlisting, and proper CORS handling",
        "Rate limiting",
        "Tool discovery"
      ],
      correctAnswer: 1,
      explanation: "openai/widgetDomain assigns a dedicated origin for your widget, enabling fullscreen mode functionality, API allowlisting, and proper CORS handling."
    },
    {
      question: "What does openai/visibility: 'private' do for a tool?",
      options: [
        "Hides the tool from all callers",
        "Makes the tool callable only from widgets, not by the model",
        "Encrypts tool responses",
        "Restricts tool to authenticated users"
      ],
      correctAnswer: 1,
      explanation: "openai/visibility: 'private' hides the tool from the model while still allowing widgets to call it via callTool. Useful for internal widget operations."
    },
    {
      question: "When should you use a private visibility tool?",
      options: [
        "For all tools to improve security",
        "For internal widget actions, bulk operations, and sensitive operations that shouldn't be model-triggered",
        "For read-only tools",
        "For tools that return large datasets"
      ],
      correctAnswer: 1,
      explanation: "Private visibility is ideal for internal widget actions (bulk delete), UI state syncing, and sensitive operations that make sense only from widget context."
    },
    {
      question: "What React primitive is @openai/apps-sdk-ui built upon?",
      options: [
        "Material UI",
        "Radix primitives",
        "Headless UI",
        "React Bootstrap"
      ],
      correctAnswer: 1,
      explanation: "@openai/apps-sdk-ui uses Radix primitives for building accessible components with consistent styling that matches ChatGPT."
    },
    {
      question: "What happens if you don't configure widgetCSP for a production widget?",
      options: [
        "Widget works normally",
        "Widget cannot make external network requests",
        "Widget loads slower",
        "Widget shows a security warning"
      ],
      correctAnswer: 1,
      explanation: "Without widgetCSP configuration, your widget cannot make external network requests in production. This is a security requirement for deployed apps."
    }
  ]}
  passingScore={80}
  randomize={true}
  batchSize={15}
/>

## Quiz Coverage

This quiz covers all eight lessons in Chapter 42:

| Topic Area | Questions | Lessons |
|------------|-----------|---------|
| Architecture Concepts | 10 | Lesson 1 |
| Widget Development | 15 | Lessons 2, 6 |
| window.openai API | 10 | Lesson 3 |
| Response Payloads | 5 | Lesson 4 |
| State and Display Modes | 5 | Lesson 5 |
| React & Apps SDK UI | 6 | Lesson 7 |
| Production Security | 6 | Lesson 8 |
| Integration and Debugging | 5 | Lessons 6, 8 |

## After the Quiz

If you scored below 80%, review the lessons where you struggled:

- **Architecture questions**: Review Lesson 1 on three-layer architecture
- **Widget development**: Review Lessons 2 and 6 on FastMCP setup and TaskManager
- **API usage**: Review Lesson 3 on sendFollowUpMessage and callTool
- **Payload design**: Review Lesson 4 on structuredContent vs _meta
- **State/display**: Review Lesson 5 on widgetState and requestDisplayMode
- **React questions**: Review Lesson 7 on apps-sdk-ui and React hooks
- **Security questions**: Review Lesson 8 on widgetCSP, widgetDomain, and visibility
- **Debugging**: Review Lesson 8 on common issues and solutions

**Next Steps**: After passing the quiz, apply these concepts by building your own ChatGPT App for your domain using the TaskManager as a template.
