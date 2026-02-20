---
sidebar_position: 11
title: "Chapter 34: OpenAI Agents SDK Quiz"
---

# Chapter 34 Quiz

Test your understanding of the OpenAI Agents SDK concepts covered in this chapter. Each question tests your ability to apply the concepts, not just recall definitions.

<Quiz
  title="OpenAI Agents SDK Assessment"
  questions={[    {
      question: "You need an agent that greets users differently based on time of day. Which approach correctly implements this?",
      options: [
        "Use hardcoded greeting in instructions",
        "Create separate agents for each period",
        "Pass time in instructions dynamically",
        "Modify agent name based on time"
      ],
      correctOption: 2,
      explanation: "Passing time dynamically in instructions is correct because Agent instructions can include runtime values using f-strings, allowing behavior customization without creating multiple agents. Creating separate agents is wasteful when only the greeting logic changes. Hardcoded instructions cannot adapt to time changes. Agent name doesn't affect behavior - only instructions do.",
      source: "Lesson 1: SDK Setup and First Agent"
    },
    {
      question: "Your agent returns unstructured text but you need JSON. Which SDK feature enforces structured output?",
      options: [
        "Use output_type with Pydantic model",
        "Add JSON instruction in prompts",
        "Parse the text response manually",
        "Use a custom output formatter"
      ],
      correctOption: 0,
      explanation: "Using output_type with a Pydantic model is correct because the SDK automatically validates and enforces the structure. Adding JSON instructions relies on the model following them, which is unreliable. Manual parsing happens after generation and can't enforce structure. Custom formatters process output but don't guarantee valid JSON from the model.",
      source: "Lesson 2: Function Tools and Context Objects"
    },
    {
      question: "A tool needs to track how many times a user has called it. Where should you store this count?",
      options: [
        "In the agent's instructions string",
        "In a global variable outside the tool",
        "In the tool's docstring metadata",
        "In RunContextWrapper's context object"
      ],
      correctOption: 3,
      explanation: "RunContextWrapper's context object is correct because it persists across tool calls within a session and is type-safe with Pydantic. Global variables work but aren't isolated per user and aren't recommended. Docstrings are read-only metadata for schema generation. Instructions are static text, not runtime state storage.",
      source: "Lesson 2: Function Tools and Context Objects"
    },
    {
      question: "Your @function_tool has parameters but the agent can't call it. What's the most likely cause?",
      options: [
        "Function name is too long",
        "Missing type hints on parameters",
        "Tool returns wrong data type",
        "Agent instructions don't mention it"
      ],
      correctOption: 1,
      explanation: "Missing type hints is correct because the SDK uses type hints to generate the tool schema - without them, parameters aren't visible to the model. Function name length doesn't affect tool discovery. Return type mismatches cause runtime errors, not tool visibility issues. Agents automatically see all tools in their tools list without instruction mentions.",
      source: "Lesson 2: Function Tools and Context Objects"
    },
    {
      question: "You have a ResearchAgent that should be callable by an OrchestratorAgent. Which pattern is correct?",
      options: [
        "Import ResearchAgent into orchestrator file",
        "Add research_agent to handoffs list",
        "Use research_agent.as_tool() in orchestrator",
        "Pass research_agent in instructions text"
      ],
      correctOption: 2,
      explanation: "Using as_tool() is correct because it exposes the agent as a callable tool while the orchestrator maintains conversation control. Handoffs transfer conversation ownership, which isn't needed here. File imports don't create callable relationships. Instructions can't reference agent objects directly.",
      source: "Lesson 3: Agents as Tools and Orchestration"
    },
    {
      question: "When should you use agent.clone() instead of creating a new Agent?",
      options: [
        "When creating variants with shared base config",
        "When you need completely different behavior",
        "When reducing memory usage is critical",
        "When deploying to production environments"
      ],
      correctOption: 0,
      explanation: "Using clone() for variants with shared base config is correct because it creates a copy where you only override specific properties. Completely different behavior needs a new Agent, not a clone. Clone doesn't reduce memory - it creates a new object. Production deployment doesn't require cloning over new creation.",
      source: "Lesson 3: Agents as Tools and Orchestration"
    },
    {
      question: "Your orchestrator needs structured data from a sub-agent. Which as_tool() parameter helps?",
      options: [
        "tool_description with JSON format request",
        "custom_output_extractor function parameter",
        "tool_name with 'structured' prefix",
        "output_type on the orchestrator agent"
      ],
      correctOption: 1,
      explanation: "custom_output_extractor is correct because it lets you define how to extract structured data from the sub-agent's response. Tool description is informational for the model, not for extraction logic. Tool name prefixes have no special meaning. Output_type on orchestrator affects its own output, not sub-agent responses.",
      source: "Lesson 3: Agents as Tools and Orchestration"
    },
    {
      question: "Your support bot should transfer billing questions to BillingAgent. Which approach correctly implements this?",
      options: [
        "Create a separate billing endpoint route",
        "Use billing_agent.as_tool() in tools list",
        "Include billing logic in main instructions",
        "Add handoff(billing_agent) to handoffs list"
      ],
      correctOption: 3,
      explanation: "Using handoff() is correct because it transfers full conversation control to BillingAgent, appropriate for specialized handling. as_tool() keeps control with the main agent, wrong for transfer scenarios. Adding billing logic defeats the purpose of specialist agents. Endpoint routing is infrastructure, not agent architecture.",
      source: "Lesson 4: Handoffs and Message Filtering"
    },
    {
      question: "After a handoff, the receiving agent sees confusing tool call history. How do you fix this?",
      options: [
        "Add explanation in receiving instructions",
        "Clear the conversation before handoff",
        "Use input_filter with remove_all_tools",
        "Disable tool calling during handoff"
      ],
      correctOption: 2,
      explanation: "Using input_filter with remove_all_tools is correct because it strips tool call messages from history before the receiving agent sees them. Clearing conversation loses important context. Instructions can't hide message history from the model. Tool calling settings don't affect historical message visibility.",
      source: "Lesson 4: Handoffs and Message Filtering"
    },
    {
      question: "Your handoff callback needs to log which agent is taking over. Which parameter provides this?",
      options: [
        "The on_handoff callback receives agent info",
        "Check global state after handoff completes",
        "Parse the handoff return value string",
        "Query the runner for current agent"
      ],
      correctOption: 0,
      explanation: "The on_handoff callback is correct because it executes at handoff time and can access the target agent information. Global state checking happens too late and is unreliable. Handoff doesn't return a parseable string with agent info. Runner queries aren't available within handoff flow.",
      source: "Lesson 4: Handoffs and Message Filtering"
    },
    {
      question: "You want TechnicalAgent to return to TriageAgent after resolution. Which enables this?",
      options: [
        "Use return statement in technical agent",
        "Add handoff back to triage in technical",
        "Set auto_return flag on the handoff",
        "Configure triage as parent in hierarchy"
      ],
      correctOption: 1,
      explanation: "Adding a handoff back to triage is correct because bidirectional handoffs require explicit configuration in both directions. Return statements don't control agent routing. There's no auto_return flag in the SDK. Agent hierarchies don't exist - handoffs are explicit transfers.",
      source: "Lesson 4: Handoffs and Message Filtering"
    },
    {
      question: "A user tries to access another user's data. Which SDK feature should block this?",
      options: [
        "Tool-level permission in each function",
        "Output filtering after agent responds",
        "Instructions telling agent to refuse",
        "An @input_guardrail checking user context"
      ],
      correctOption: 3,
      explanation: "An @input_guardrail is correct because it validates input before the agent processes it, preventing unauthorized access attempts early. Output filtering is too late - data may already be exposed. Instructions can be bypassed through prompt injection. Tool-level checks miss requests that don't use tools.",
      source: "Lesson 5: Guardrails and Agent-Based Validation"
    },
    {
      question: "Your guardrail needs complex classification logic. Which implementation pattern is recommended?",
      options: [
        "Use an agent within the guardrail function",
        "Add multiple if-else conditions in code",
        "Call external classification API directly",
        "Use regex patterns for all detection"
      ],
      correctOption: 0,
      explanation: "Using an agent within the guardrail is correct because agent-based guardrails leverage LLM capabilities for nuanced classification. Complex if-else becomes unmaintainable and misses edge cases. External APIs add latency and failure points. Regex can't handle semantic content analysis.",
      source: "Lesson 5: Guardrails and Agent-Based Validation"
    },
    {
      question: "Your output guardrail detects PII in the response. What should the GuardrailFunctionOutput contain?",
      options: [
        "Error message for the user display",
        "Modified response with PII removed",
        "tripwire_triggered set to True value",
        "Logging call to record the incident"
      ],
      correctOption: 2,
      explanation: "Setting tripwire_triggered to True is correct because it stops execution and prevents the PII-containing response from reaching the user. Guardrails don't modify responses - they approve or reject. Error messages are handled by exception handlers. Logging is a side effect, not the guardrail's return value.",
      source: "Lesson 5: Guardrails and Agent-Based Validation"
    },
    {
      question: "InputGuardrailTripwireTriggered is raised. Where should you handle this exception?",
      options: [
        "Inside the guardrail function itself",
        "In try/except around Runner.run() call",
        "In the agent's instructions handling",
        "Through a global exception middleware"
      ],
      correctOption: 1,
      explanation: "Wrapping Runner.run() in try/except is correct because the exception propagates from the guardrail through the runner. Guardrails raise exceptions, they don't catch them. Agent instructions can't handle Python exceptions. Global middleware doesn't integrate with the SDK's exception flow.",
      source: "Lesson 5: Guardrails and Agent-Based Validation"
    },
    {
      question: "Your agent needs to remember the previous conversation turn. Which approach is correct?",
      options: [
        "Use context object for message storage",
        "Store messages in a global list variable",
        "Add conversation to agent instructions text",
        "Pass SQLiteSession to Runner.run() session param"
      ],
      correctOption: 3,
      explanation: "SQLiteSession is correct because it's the SDK's built-in mechanism for conversation persistence across turns. Global lists work but aren't thread-safe or persistent. Instructions are static, not conversation storage. Context objects store tool state, not conversation history.",
      source: "Lesson 6: Sessions and Conversation Memory"
    },
    {
      question: "You want conversation history to survive application restarts. Which SQLiteSession configuration is needed?",
      options: [
        "Call session.save() after each interaction",
        "Set persist=True in the constructor",
        "Provide a file path as second argument",
        "Use SQLiteSession.persistent() factory method"
      ],
      correctOption: 2,
      explanation: "Providing a file path is correct because SQLiteSession(id, 'file.db') stores data in a file instead of memory. There's no persist parameter or save() method. No persistent() factory exists - the file path argument enables persistence.",
      source: "Lesson 6: Sessions and Conversation Memory"
    },
    {
      question: "Your session has grown large and you need only the last 10 messages. Which method retrieves this?",
      options: [
        "session.get_items(limit=10) returns recent items"
      ],
      correctOption: 0,
      explanation: "get_items(limit=10) is correct because it's the SDK's method to retrieve a limited number of recent items. Direct slicing assumes messages is a public attribute, which it isn't. truncate() doesn't exist. filter() isn't a session method.",
      source: "Lesson 6: Sessions and Conversation Memory"
    },
    {
      question: "Multiple users interact with your agent simultaneously. How should you manage their sessions?",
      options: [
        "Use a single shared session for all users",
        "Create unique session_id per user value",
        "Store user_id in the session metadata field",
        "Create separate Agent instances per user"
      ],
      correctOption: 1,
      explanation: "Unique session_id per user is correct because SQLiteSession isolates conversations by ID. Shared sessions mix conversations inappropriately. Session metadata stores data within a session, not user separation. Agent instances don't need to be per-user - sessions handle isolation.",
      source: "Lesson 6: Sessions and Conversation Memory"
    },
    {
      question: "You want to undo the last message in a session. Which operation accomplishes this?",
      options: [
        "session.clear_last() removes recent item",
        "session.undo() reverses last addition",
        "session.delete(-1) removes by index value",
        "session.pop_item() removes last message"
      ],
      correctOption: 3,
      explanation: "pop_item() is correct because it's the SDK method to remove the last message from session history. undo(), delete(), and clear_last() don't exist as session methods. pop_item() is the only removal method for the most recent item.",
      source: "Lesson 6: Sessions and Conversation Memory"
    },
    {
      question: "You need to log every time an agent starts processing. Which RunHooks method should you implement?",
      options: [
        "on_agent_start receives agent and context",
        "before_agent logs before any processing",
        "agent_init fires when agent is created",
        "pre_run executes before the runner starts"
      ],
      correctOption: 0,
      explanation: "on_agent_start is correct because it's the lifecycle hook that fires when an agent begins processing a request. before_agent, agent_init, and pre_run aren't valid RunHooks method names. The SDK uses on_agent_start/on_agent_end naming convention.",
      source: "Lesson 7: Tracing, Hooks and Observability"
    },
    {
      question: "Your monitoring needs to track token usage per request. Where is this data available?",
      options: [
        "Agent.token_count property after run",
        "Runner.run() returns usage in result",
        "ctx.usage in RunHooks callback methods",
        "Global metrics from the openai package"
      ],
      correctOption: 2,
      explanation: "ctx.usage in RunHooks is correct because the context wrapper provides usage statistics accessible in lifecycle callbacks. Runner.run() result doesn't include usage directly. Agents don't have token_count properties. The openai package doesn't track agent-level metrics.",
      source: "Lesson 7: Tracing, Hooks and Observability"
    },
    {
      question: "You want to link multiple conversation turns in the tracing dashboard. Which parameter accomplishes this?",
      options: [
        "Add turn metadata to each span",
        "Use same trace_id for all turns",
        "Set conversation_id in Runner.run() params",
        "Pass group_id to trace() context manager"
      ],
      correctOption: 3,
      explanation: "group_id is correct because it links related traces in the dashboard while keeping individual trace_ids unique. Same trace_id would merge turns incorrectly. conversation_id isn't a Runner parameter. Span metadata doesn't provide dashboard grouping.",
      source: "Lesson 7: Tracing, Hooks and Observability"
    },
    {
      question: "You need to measure latency for a database query within a tool. Which tracing feature should you use?",
      options: [
        "Add timing to the tool's docstring",
        "Wrap the query in custom_span() block",
        "Use gen_trace_id() before the query",
        "Log start and end times manually"
      ],
      correctOption: 1,
      explanation: "custom_span() is correct because it creates a child span that tracks duration and appears in the trace hierarchy. Docstrings don't capture runtime metrics. gen_trace_id() creates IDs but doesn't measure time. Manual logging isn't integrated with the tracing system.",
      source: "Lesson 7: Tracing, Hooks and Observability"
    },
    {
      question: "gen_trace_id() returns a value. What is the primary use of this value?",
      options: [
        "Construct dashboard URL for debugging",
        "Store as primary key in database",
        "Pass to external logging service API",
        "Include in response to end user"
      ],
      correctOption: 0,
      explanation: "Constructing dashboard URL is correct because trace IDs let you view the specific execution in OpenAI's tracing dashboard. Database storage and logging are secondary uses. Exposing trace IDs to users is generally not needed and may leak internal details.",
      source: "Lesson 7: Tracing, Hooks and Observability"
    },
    {
      question: "Your agent needs tools from a remote MCP server. Which class configures this connection?",
      options: [
        "RemoteToolServer with connection string",
        "MCPClient connecting to server endpoint",
        "MCPServerStreamableHttp with server URL",
        "AgentToolProvider with MCP configuration"
      ],
      correctOption: 2,
      explanation: "MCPServerStreamableHttp is correct because it's the SDK's class for HTTP-based MCP server connections. MCPClient, RemoteToolServer, and AgentToolProvider aren't valid SDK classes. The SDK uses MCPServerStreamableHttp for remote MCP integration.",
      source: "Lesson 8: MCP Integration"
    },
    {
      question: "You've configured an MCP server. How do you make its tools available to your agent?",
      options: [
        "Set agent.external_tools to server instance",
        "Import tools directly from server module",
        "Call server.register_with(agent) method",
        "Add server to mcp_servers list param"
      ],
      correctOption: 3,
      explanation: "Adding to mcp_servers list is correct because Agent accepts mcp_servers parameter that integrates MCP tools. Direct imports don't work for remote servers. register_with() isn't an MCP server method. external_tools isn't a valid Agent parameter.",
      source: "Lesson 8: MCP Integration"
    },
    {
      question: "Your MCP server connection should stay open across multiple agent runs. What pattern achieves this?",
      options: [
        "Set keep_alive=True in server constructor",
        "Use async context manager around all runs",
        "Call server.connect() once at startup",
        "Enable connection pooling in server config"
      ],
      correctOption: 1,
      explanation: "Async context manager is correct because MCPServerStreamableHttp uses 'async with' to manage lifecycle, and keeping the context open maintains the connection. keep_alive, connect(), and connection pooling aren't MCPServerStreamableHttp features.",
      source: "Lesson 8: MCP Integration"
    },
    {
      question: "MCP tool definitions are stable and rarely change. Which configuration improves performance?",
      options: [
        "Increase timeout for tool discovery calls",
        "Store tool schemas in local JSON file",
        "Set cache_tools_list=True in server config",
        "Use synchronous instead of async client"
      ],
      correctOption: 2,
      explanation: "cache_tools_list=True is correct because it caches tool definitions and avoids repeated discovery requests. Local JSON files bypass the MCP protocol entirely. Timeout doesn't cache results. Sync vs async doesn't affect caching.",
      source: "Lesson 8: MCP Integration"
    },
    {
      question: "Your agent should answer questions from a document library. Which OpenAI feature enables this?",
      options: [
        "FileSearchTool with vector store attachment",
        "DocumentLoader importing files as context",
        "RAGAgent specialized for document queries",
        "KnowledgeBase configured with file paths"
      ],
      correctOption: 0,
      explanation: "FileSearchTool with vector store is correct because it's OpenAI's hosted RAG tool that handles document retrieval. DocumentLoader, RAGAgent, and KnowledgeBase aren't SDK components. FileSearchTool is the built-in retrieval solution.",
      source: "Lesson 9: RAG with FileSearchTool"
    },
    {
      question: "You need to create a vector store for your documents. Which API call initiates this?",
      options: [
        "Agent.attach_vector_store() method call",
        "VectorStore.new() factory method call",
        "openai.create_embedding_store() function",
        "client.vector_stores.create() with name"
      ],
      correctOption: 3,
      explanation: "client.vector_stores.create() is correct because it's the OpenAI API method to create a new vector store. VectorStore.new(), create_embedding_store(), and attach_vector_store() aren't valid methods in the OpenAI SDK.",
      source: "Lesson 9: RAG with FileSearchTool"
    },
    {
      question: "Your RAG agent should cite sources in its answers. Which aspect of FileSearchTool provides this?",
      options: [
        "Custom post-processing of search results",
        "Citations included in tool response automatically",
        "Agent instructions requesting source citation",
        "Metadata attached to vector store entries"
      ],
      correctOption: 1,
      explanation: "Automatic citations in tool response is correct because FileSearchTool returns citation information with retrieved content. Post-processing and instruction requests are workarounds, not the native mechanism. Metadata doesn't automatically produce citations in responses.",
      source: "Lesson 9: RAG with FileSearchTool"
    },
    {
      question: "Documents need to be indexed before searching. Which step uploads files to the vector store?",
      options: [
        "FileSearchTool.index() with file paths",
        "vector_store.add_documents() method call",
        "client.vector_stores.files.create() call",
        "openai.files.embed() for each document"
      ],
      correctOption: 2,
      explanation: "client.vector_stores.files.create() is correct because it's the API method to upload and index files in a vector store. add_documents(), FileSearchTool.index(), and files.embed() aren't valid methods in the OpenAI SDK.",
      source: "Lesson 9: RAG with FileSearchTool"
    },
    {
      question: "Your vector store has sensitive internal documents. How should you control access?",
      options: [
        "Create separate stores per access level",
        "Set document permissions in vector store",
        "Use input guardrails to filter queries",
        "Encrypt documents before uploading them"
      ],
      correctOption: 0,
      explanation: "Separate stores per access level is correct because vector stores don't have per-document permissions - isolation requires separate stores. Document-level permissions don't exist. Guardrails filter inputs, not search results. Encryption prevents searching, not access control.",
      source: "Lesson 9: RAG with FileSearchTool"
    },
    {
      question: "You're building a Customer Support Digital FTE. Which architecture pattern is most appropriate?",
      options: [
        "Single agent handling all query types",
        "Triage agent with specialist handoffs",
        "Parallel agents for each query type",
        "Pipeline of sequential processing agents"
      ],
      correctOption: 1,
      explanation: "Triage with specialist handoffs is correct because it routes queries to appropriate experts while maintaining conversation context. Single agents become complex and hard to maintain. Parallel agents don't maintain conversation flow. Sequential pipelines don't match interactive support patterns.",
      source: "Lesson 10: Capstone - Customer Support Digital FTE"
    },
    {
      question: "Your FTE needs to handle billing, technical, and general queries. How should specialists be organized?",
      options: [
        "Agent clones with different model configs",
        "One agent with conditional instructions",
        "Tools for each domain in single agent",
        "Separate agents with triage routing logic"
      ],
      correctOption: 3,
      explanation: "Separate agents with triage routing is correct because it allows specialized instructions, tools, and potentially different models per domain. Conditional instructions become unwieldy. Domain tools in one agent miss instruction specialization. Clone variants don't provide the needed separation.",
      source: "Lesson 10: Capstone - Customer Support Digital FTE"
    },
    {
      question: "A Digital FTE should not reveal internal system details. Which layer should enforce this?",
      options: [
        "Output guardrail checking response content",
        "Input guardrail blocking system questions",
        "Agent instructions to avoid topics only",
        "Post-processing filter on all responses"
      ],
      correctOption: 0,
      explanation: "Output guardrail is correct because it checks what the agent actually says, catching accidental leaks regardless of input. Input guardrails can't predict all leak-inducing queries. Instructions can be bypassed. Post-processing outside the SDK loses integration benefits.",
      source: "Lesson 10: Capstone - Customer Support Digital FTE"
    },
    {
      question: "Your production FTE needs to maintain conversation context across user sessions. Which components should you combine?",
      options: [
        "Agent instructions with conversation summary",
        "Context objects with regular serialization",
        "SQLiteSession with file-based persistence",
        "MCP server storing conversation state"
      ],
      correctOption: 2,
      explanation: "SQLiteSession with file persistence is correct because it's the SDK's native mechanism for durable conversation storage. Context objects store tool state, not conversation history. Instructions can't hold dynamic data. MCP servers provide tools, not session management.",
      source: "Lesson 10: Capstone - Customer Support Digital FTE"
    },
    {
      question: "You want to charge customers per resolved support ticket. Which monetization model does this represent?",
      options: [
        "Freemium with premium escalation features",
        "Subscription model with unlimited tickets",
        "Per-seat licensing for support agents",
        "Usage-based pricing per resolution achieved"
      ],
      correctOption: 3,
      explanation: "Usage-based per resolution is correct because it charges for successful outcomes (resolved tickets). Subscription is flat-fee regardless of usage. Per-seat applies to human agents. Freemium involves free and paid tiers, not outcome-based charging.",
      source: "Lesson 10: Capstone - Customer Support Digital FTE"
    },
    {
      question: "After building your FTE, what's the next step in the Digital FTE journey?",
      options: [
        "Adding more specialist agent handoffs",
        "Distribution through marketplace or API",
        "Optimizing model selection for costs",
        "Implementing additional guardrail layers"
      ],
      correctOption: 1,
      explanation: "Distribution is correct because the BUILD phase (this chapter) is followed by DISTRIBUTE (Ch42 Apps SDK) and then DEPLOY (Part 7). More features, optimization, and guardrails are BUILD phase activities, not the next journey phase.",
      source: "Lesson 10: Capstone - Customer Support Digital FTE"
    },
    {
      question: "Your agent runs on non-OpenAI models. Which configuration prevents tracing errors?",
      options: [
        "Set model_provider='external' on agent",
        "Remove tracing import from the module",
        "Call set_tracing_disabled(True) before runs",
        "Configure null tracing endpoint in settings"
      ],
      correctOption: 2,
      explanation: "set_tracing_disabled(True) is correct because it prevents the SDK from attempting to send traces to OpenAI's dashboard for non-OpenAI models. Removing imports breaks other functionality. model_provider and null endpoints aren't valid configurations.",
      source: "Lesson 1: SDK Setup and First Agent"
    },
    {
      question: "You're using Gemini through the SDK. Which class enables this integration?",
      options: [
        "OpenAIChatCompletionsModel with base_url",
        "GeminiAgent from agents.providers module",
        "Agent with model='gemini-pro' string",
        "ExternalModelWrapper around Gemini client"
      ],
      correctOption: 0,
      explanation: "OpenAIChatCompletionsModel with custom base_url is correct because it uses OpenAI-compatible API format with Gemini's endpoint. GeminiAgent and ExternalModelWrapper don't exist. Direct model string doesn't configure the endpoint URL needed.",
      source: "Lesson 1: SDK Setup and First Agent"
    },
    {
      question: "A function tool's docstring is incomplete. What's the primary impact?",
      options: [
        "SDK refuses to register the tool",
        "Python raises documentation error",
        "Tool execution fails silently always",
        "Agent may misuse or ignore the tool"
      ],
      correctOption: 3,
      explanation: "Agent misuse is correct because docstrings generate tool descriptions that guide the model's usage decisions. Python doesn't require docstrings. Tools still execute if called. SDK registers tools regardless of docstring quality.",
      source: "Lesson 2: Function Tools and Context Objects"
    },
    {
      question: "Your tool returns a complex object. How should you type hint the return?",
      options: [
        "Return the object with Any type hint",
        "Use str and serialize the object",
        "Define Pydantic model for the return",
        "Use dict without type specification"
      ],
      correctOption: 1,
      explanation: "Returning str with serialization is correct because tools should return strings that the model can interpret. Any type loses schema information. Pydantic returns need serialization anyway. Untyped dicts cause schema generation issues.",
      source: "Lesson 2: Function Tools and Context Objects"
    },
    {
      question: "An orchestrator needs to run sub-agents in parallel. Which approach achieves this?",
      options: [
        "Call multiple as_tool() agents concurrently",
        "Use asyncio.gather() on agent.run() calls",
        "Set parallel=True on orchestrator agent",
        "Create ThreadPoolExecutor for sub-agents"
      ],
      correctOption: 0,
      explanation: "Concurrent as_tool() calls is correct because the model can invoke multiple tools in one turn when orchestrator has multiple agent-tools. asyncio.gather with run() bypasses orchestration. parallel flag doesn't exist. ThreadPoolExecutor doesn't integrate with agent architecture.",
      source: "Lesson 3: Agents as Tools and Orchestration"
    },
    {
      question: "Handoff vs as_tool(): When should you prefer handoff?",
      options: [
        "When orchestrator needs intermediate results",
        "When sub-agent returns structured data",
        "When transferring full conversation control",
        "When minimizing latency is the priority"
      ],
      correctOption: 2,
      explanation: "Full conversation control transfer is correct because handoffs change which agent owns the conversation, ideal for escalation. Structured data and intermediate results favor as_tool() where orchestrator maintains control. Latency considerations favor as_tool() for simpler interactions.",
      source: "Lesson 3: Agents as Tools and Orchestration"
    },
    {
      question: "Your input_filter receives HandoffInputData. What can you modify in it?",
      options: [
        "The target agent's instructions directly",
        "The messages list before receiving agent",
        "The handoff callback function reference",
        "The originating agent's tool definitions"
      ],
      correctOption: 1,
      explanation: "Modifying messages list is correct because input_filter transforms the conversation history passed to the receiving agent. Instructions, callbacks, and tool definitions aren't part of HandoffInputData - only the messages being transferred.",
      source: "Lesson 4: Handoffs and Message Filtering"
    },
    {
      question: "A guardrail agent determines if content is appropriate. What should it return?",
      options: [
        "Tuple of (approved, reason) values",
        "Boolean True or False for approval",
        "String explaining the classification decision",
        "Pydantic model with classification result"
      ],
      correctOption: 3,
      explanation: "Pydantic model is correct because output_type on guardrail agents enforces structured classification results that the guardrail function can inspect reliably. Booleans, strings, and tuples lack the structured enforcement needed.",
      source: "Lesson 5: Guardrails and Agent-Based Validation"
    },
    {
      question: "Your session data should expire after 30 minutes. Which approach implements this?",
      options: [
        "Implement custom session with TTL logic",
        "Set SQLiteSession(ttl=1800) parameter value",
        "Schedule periodic session.clear() calls using task",
        "Configure database-level row expiration on table"
      ],
      correctOption: 0,
      explanation: "Custom session with TTL is correct because SQLiteSession doesn't have built-in TTL - you need to implement expiration logic. ttl parameter doesn't exist. Scheduled clearing loses precision. Database expiration requires custom session implementation anyway.",
      source: "Lesson 6: Sessions and Conversation Memory"
    },
    {
      question: "RunHooks.on_tool_end receives the tool result. What type is this result typically?",
      options: [
        "Pydantic model matching tool return type",
        "Original return value from the function",
        "String representation of tool output",
        "Dict with result and metadata combined"
      ],
      correctOption: 2,
      explanation: "String representation is correct because tools return strings to the model, and that's what on_tool_end receives. Original return values are converted. Pydantic models are serialized. The result isn't wrapped in metadata dicts.",
      source: "Lesson 7: Tracing, Hooks and Observability"
    }
  ]}
  questionsPerBatch={18}
/>
