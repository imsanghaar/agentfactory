# Envoy AI Gateway Reference

## Overview

Envoy AI Gateway is a specialized gateway for LLM traffic management, built on Envoy Gateway. It addresses unique challenges of AI traffic that traditional API gateways don't handle:

- **Token-based billing**: LLM providers charge per token, not per request
- **Variable request cost**: A single request can cost 100 or 10,000 tokens
- **Multi-provider routing**: Need fallback across OpenAI, Anthropic, Gemini, etc.
- **Model-specific policies**: Different models need different rate limits

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Tier 1 Gateway                           │
│  (Authentication, Global Routing, Cost Protection)          │
├─────────────────────────────────────────────────────────────┤
│  • Token Rate Limiting (per-user, per-model)                │
│  • Provider Fallback (OpenAI → Anthropic → Gemini)          │
│  • Response Caching & Deduplication                         │
│  • Credential Injection (secure, centralized)               │
└─────────────────────────────────────────────────────────────┘
                ↓ (External)     ↓ (Internal)
        ┌───────────────────────────────────┐
        │  OpenAI  │  Anthropic  │  Gemini  │
        └───────────────────────────────────┘
                            ↓
                ┌───────────────────────┐
                │   Tier 2 Gateway      │
                │  (Self-Hosted Models) │
                │  vLLM, KServe, etc.   │
                └───────────────────────┘
```

## Token-Based Rate Limiting

### How It Works

1. Request flows through AI Gateway to LLM provider
2. Response contains token usage (input_tokens, output_tokens)
3. AI Gateway extracts token counts (OpenAI schema format)
4. Deducts from user's token budget
5. If budget exceeded, returns 429

### Configuration

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: AIGatewayRoute
metadata:
  name: llm-route
spec:
  # Token-based rate limiting
  llmRequestCosts:
    - type: InputToken
      weight: 1        # Cost per input token
    - type: OutputToken
      weight: 3        # Output tokens cost 3x (more expensive)
    - type: TotalToken
      weight: 1        # OR just use total

  # Per-model cost multipliers
  modelCosts:
    - model: gpt-4
      multiplier: 10   # GPT-4 = 10x base cost
    - model: gpt-3.5-turbo
      multiplier: 1    # GPT-3.5 = base cost
    - model: claude-3-opus
      multiplier: 15   # Claude Opus = 15x base cost
    - model: claude-3-sonnet
      multiplier: 3    # Claude Sonnet = 3x base cost

  # Budget per user
  tokenBudget:
    perUser:
      limit: 100000    # 100K tokens per user
      period: 30d      # Per month
    perMinute:
      limit: 10000     # 10K tokens per minute burst
```

### Extracting User from Request

```yaml
# Token budget tracked per user
userIdentification:
  header: x-user-id
  # OR from JWT claim
  jwt:
    claim: sub
    provider: auth0
```

## Provider Fallback

### Priority-Based Routing

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: AIGatewayRoute
metadata:
  name: resilient-llm
spec:
  backends:
  # Primary: OpenAI GPT-4
  - name: openai-gpt4
    priority: 0
    provider: openai
    model: gpt-4
    auth:
      type: APIKey
      apiKeyRef:
        name: openai-key

  # First fallback: Anthropic Claude
  - name: anthropic-claude
    priority: 1
    provider: anthropic
    model: claude-3-opus
    modelNameOverride: gpt-4  # Unified client interface
    auth:
      type: APIKey
      apiKeyRef:
        name: anthropic-key

  # Second fallback: Google Gemini
  - name: google-gemini
    priority: 2
    provider: google-gemini
    model: gemini-pro
    modelNameOverride: gpt-4
    auth:
      type: APIKey
      apiKeyRef:
        name: gemini-key

  # Fallback triggers
  failover:
    on:
    - rateLimit         # Provider rate limited
    - timeout           # Request timeout
    - error             # 5xx error
    - budgetExceeded    # Token budget exhausted
```

### Model Name Virtualization

```yaml
# Clients always request "gpt-4"
# Gateway routes to available backend
backends:
- name: openai
  model: gpt-4
  priority: 0
- name: anthropic
  model: claude-3-opus
  modelNameOverride: gpt-4  # Appears as gpt-4 to client
  priority: 1
```

## Supported Providers

| Provider | Models | Auth Type |
|----------|--------|-----------|
| **OpenAI** | gpt-4, gpt-4-turbo, gpt-3.5-turbo | API Key |
| **Anthropic** | claude-3-opus, claude-3-sonnet, claude-3-haiku | API Key |
| **Google Gemini** | gemini-pro, gemini-ultra | API Key |
| **AWS Bedrock** | Claude, Titan, Llama | IAM Role |
| **Azure OpenAI** | GPT-4, GPT-3.5 | API Key |
| **Mistral** | mistral-large, mistral-medium | API Key |
| **Cohere** | command, command-light | API Key |
| **Groq** | llama2-70b, mixtral | API Key |
| **DeepSeek** | deepseek-chat | API Key |
| **Together AI** | Various open models | API Key |

## Cost Control Patterns

### Pattern 1: Tiered Service Plans

```yaml
# Free tier: 10K tokens/day
userTiers:
- name: free
  selector:
    header: x-plan
    value: free
  tokenBudget:
    daily: 10000
  allowedModels:
  - gpt-3.5-turbo

# Pro tier: 100K tokens/day
- name: pro
  selector:
    header: x-plan
    value: pro
  tokenBudget:
    daily: 100000
  allowedModels:
  - gpt-4
  - gpt-3.5-turbo

# Enterprise: Unlimited with cost tracking
- name: enterprise
  selector:
    header: x-plan
    value: enterprise
  tokenBudget:
    unlimited: true
  costTracking:
    enabled: true
    alertThreshold: 1000  # Alert at $1000/day
```

### Pattern 2: Request Caching

```yaml
caching:
  enabled: true
  ttl: 3600s              # Cache for 1 hour
  keyComponents:
  - prompt                # Same prompt = cache hit
  - model                 # Different models = different cache
  - temperature           # Different temp = different cache
  maxSize: 10GB
  backend:
    type: redis
    address: redis:6379
```

### Pattern 3: Request Deduplication

```yaml
deduplication:
  enabled: true
  window: 5s              # Merge identical requests within 5s
  keyComponents:
  - prompt
  - model
  # 5 users asking same question = 1 LLM call
```

### Pattern 4: Retry with Cheaper Model

```yaml
retry:
  maxAttempts: 3
  fallbackStrategy: cheaperModel
  fallbackOrder:
  - gpt-4          # Try expensive first
  - gpt-3.5-turbo  # Fall back to cheap
  - gemini-flash   # Then even cheaper
```

## Security Configuration

### Credential Injection

```yaml
# Centralized API key management
backends:
- name: openai
  auth:
    type: APIKey
    apiKeyRef:
      name: llm-credentials
      key: openai-api-key
    # Key injected as Authorization header
    headerName: Authorization
    headerPrefix: "Bearer "
```

### Request Sanitization

```yaml
security:
  # Remove sensitive headers before forwarding
  stripHeaders:
  - x-internal-auth
  - x-user-password

  # Validate prompt content (PII detection)
  promptValidation:
    enabled: true
    blockPatterns:
    - "ssn:\\s*\\d{3}-\\d{2}-\\d{4}"  # SSN pattern
    - "credit_card:\\s*\\d{16}"        # Credit card
```

## Observability

### Metrics Exported

```
# Token usage per user/model
ai_gateway_tokens_total{user="...", model="gpt-4", type="input"}
ai_gateway_tokens_total{user="...", model="gpt-4", type="output"}

# Request latency per provider
ai_gateway_request_duration_seconds{provider="openai", model="gpt-4"}

# Fallback events
ai_gateway_fallback_total{from="openai", to="anthropic", reason="rate_limit"}

# Cost per user (estimated)
ai_gateway_cost_dollars{user="...", model="gpt-4"}

# Cache hit rate
ai_gateway_cache_hits_total{model="gpt-4"}
ai_gateway_cache_misses_total{model="gpt-4"}
```

### Integration with Prometheus/Grafana

```yaml
# ServiceMonitor for AI Gateway metrics
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: ai-gateway
spec:
  selector:
    matchLabels:
      app: ai-gateway
  endpoints:
  - port: metrics
    path: /stats/prometheus
    interval: 30s
```

## Complete Example: AI Agent Platform

```yaml
---
# AI Gateway configuration for multi-tenant agent platform
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: AIGatewayRoute
metadata:
  name: agent-platform
spec:
  # Multi-provider backends
  backends:
  - name: openai-primary
    priority: 0
    provider: openai
    model: gpt-4-turbo
    auth:
      apiKeyRef: {name: openai-key}

  - name: anthropic-fallback
    priority: 1
    provider: anthropic
    model: claude-3-sonnet
    modelNameOverride: gpt-4
    auth:
      apiKeyRef: {name: anthropic-key}

  # Token-based rate limiting
  tokenRateLimit:
    perUser:
      inputTokensPerMinute: 5000
      outputTokensPerMinute: 10000
      totalTokensPerDay: 100000

    # Different limits for expensive models
    perModel:
      gpt-4-turbo:
        tokensPerMinute: 2000
      gpt-3.5-turbo:
        tokensPerMinute: 10000

  # Cost control
  costControl:
    maxDailyCostPerUser: 10.00  # $10/day cap
    alertThreshold: 8.00         # Alert at 80%
    modelPricing:
      gpt-4-turbo:
        inputPer1k: 0.01
        outputPer1k: 0.03
      claude-3-sonnet:
        inputPer1k: 0.003
        outputPer1k: 0.015

  # Caching for repeated prompts
  caching:
    enabled: true
    ttl: 3600s
    backend: redis

  # Failover configuration
  failover:
    on: [rateLimit, timeout, budgetExceeded]
    retryAttempts: 2
    retryDelay: 1s

---
# User identification from JWT
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: SecurityPolicy
metadata:
  name: agent-auth
spec:
  targetRefs:
  - kind: AIGatewayRoute
    name: agent-platform
  jwt:
    providers:
    - name: agent-auth
      issuer: https://auth.agent-platform.com
      remoteJWKS:
        uri: https://auth.agent-platform.com/.well-known/jwks.json
      claimToHeaders:
      - claim: sub
        header: x-user-id
      - claim: plan
        header: x-user-plan
```

## Why AI Gateway for Agent Platforms

| Traditional Gateway | AI Gateway |
|---------------------|------------|
| 1 request = 1 unit | 1 request = N tokens (variable) |
| Fixed cost per endpoint | Dynamic cost per model/token |
| No provider awareness | Multi-provider with fallback |
| Request uniformity | Token complexity awareness |
| Single backend | Intelligent cross-backend routing |
| No model policies | Per-model rate limits/costs |

**For AI agents specifically:**
- Agents make thousands of LLM calls across providers
- Each call has different token cost
- Agent budget control is critical (runaway = massive bill)
- Multi-provider resilience prevents lock-in
- Visibility into which agents consume budget
