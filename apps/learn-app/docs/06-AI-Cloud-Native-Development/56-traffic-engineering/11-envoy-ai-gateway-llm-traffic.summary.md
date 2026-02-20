### Core Concept
Envoy AI Gateway provides token-based rate limiting for LLM traffic where request counting fails (100 requests can cost $0.03 or $240), along with unified API access across providers and automatic fallback when one provider is rate-limited.

### Key Mental Models
- **Token vs Request Economics**: GPT-4o request costs vary 100x based on prompt length; request counting cannot capture this
- **LLMRequestCost Extraction**: Gateway parses token counts (InputToken, OutputToken, TotalToken) from LLM responses
- **Priority-Based Fallback**: Route to OpenAI (priority 1), fall back to Anthropic (priority 2) on failure
- **CEL Cost Calculation**: Custom expression `input_tokens * 0.25 + output_tokens * 1.0` for accurate cost tracking

### Critical Patterns
- Set `cost.request.number: 0` so only tokens count, not requests
- Use `x-user-id: Distinct` header selector for per-user token budgets
- Apply stricter limits to expensive models (50K tokens for GPT-4o vs 500K for GPT-4o-mini)
- Store provider credentials in Kubernetes Secrets referenced by AIBackend

### AI Collaboration Keys
- Configure LLMRequestCost for token extraction from LLM responses
- Design BackendTrafficPolicy with token-based rate limits per user and model
- Set up AIGatewayRoute with provider fallback chain

### Common Mistakes
- Using request-based limits for LLM traffic (fails to control costs)
- Forgetting to configure LLMRequestCost before token-based limiting
- Setting same token budget for expensive and cheap models

### Connections
- **Builds on**: Lesson 10 (Resilience Patterns) for general traffic protection
- **Leads to**: Lesson 12 (Capstone) for complete traffic engineering integration
