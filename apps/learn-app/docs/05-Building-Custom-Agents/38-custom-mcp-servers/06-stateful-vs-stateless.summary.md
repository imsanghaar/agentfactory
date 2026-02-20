### Core Concept
Horizontal scaling behind load balancers breaks stateful features (sampling, progress, subscriptions). Choose stateless_http=True for simple scaling, or stateful with sticky sessions for full features. Decision depends on feature needs vs scaling requirements.

### Key Mental Models
- **Horizontal scaling problem**: Request goes to Server B, but session exists on Server A
- **Stateless tradeoff**: No sampling, no progress, no subscriptions—but trivial scaling
- **Feature loss matrix**: Stateful+Streaming (all features) → Stateless+JSON (horizontal scaling)
- **Decision framework**: Need sampling? → stateful. Need 1000+ clients? → stateless

### Critical Patterns
- Stateless mode: `FastMCP(name="...", stateless_http=True)`
- JSON response: `FastMCP(name="...", json_response=True)`
- Full simple: Both True for maximum simplicity, minimum features
- Sticky sessions: Load balancer routes same client to same server (ops complexity)

### AI Collaboration Keys
- Stateless = simpler ops, fewer features; Stateful = more features, more complexity
- Don't design for sampling then deploy stateless (sampling breaks)
- Scale requirements often conflict with feature requirements—choose early

### Common Mistakes
- Using sampling in stateless mode (fails silently or with session errors)
- Not understanding feature loss when enabling stateless
- Assuming sticky sessions are simple (they add significant ops complexity)

### Connections
- **Builds on**: StreamableHTTP Transport (Lesson 5)
- **Leads to**: Error Handling & Recovery (Lesson 7)
