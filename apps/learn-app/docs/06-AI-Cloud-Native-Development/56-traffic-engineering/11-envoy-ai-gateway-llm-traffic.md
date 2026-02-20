---
sidebar_position: 11
title: "Envoy AI Gateway for LLM Traffic"
description: "AI-specific traffic management with token-based rate limiting and provider fallback"
keywords: [envoy ai gateway, llm traffic, token rate limiting, provider fallback, ai gateway, openai, anthropic, model routing, cost engineering, kubernetes]
chapter: 56
lesson: 11
duration_minutes: 45
proficiency_level: B1

skills:
  - name: "LLM Traffic Management"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student can configure AI Gateway for token-based limiting"

  - name: "Token-Based Rate Limiting"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student can configure token budgets per user and model"

  - name: "Provider Fallback Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student can implement provider fallback chains"

  - name: "AI Cost Engineering"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student can design budget allocation strategies"

learning_objectives:
  - objective: "Explain why token-based rate limiting differs from request-based"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student articulates cost implications"
    three_role_integration:
      ai_as_teacher: "Learn token economics from AI explanations"
      ai_as_student: "Guide AI with your cost concerns"
      ai_as_coworker: "Build cost model understanding together"

  - objective: "Configure token budgets per user"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Token budget enforced correctly"
    three_role_integration:
      ai_as_teacher: "Discover budget allocation patterns"
      ai_as_student: "Define user tier requirements"
      ai_as_coworker: "Tune budgets through usage analysis"

  - objective: "Implement provider fallback chain (OpenAI to Anthropic)"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Fallback triggers when primary rate limited"
    three_role_integration:
      ai_as_teacher: "Learn fallback chain best practices"
      ai_as_student: "Specify provider priorities and constraints"
      ai_as_coworker: "Test fallback scenarios together"

  - objective: "Design cost control patterns for AI agents"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student proposes budget allocation strategy"
    three_role_integration:
      ai_as_teacher: "Learn cost engineering strategies"
      ai_as_student: "Share business budget constraints"
      ai_as_coworker: "Create budget allocation design together"

cognitive_load:
  new_concepts: 6
  assessment: "AI Gateway architecture, token-based rate limiting, token budget, provider fallback, model routing, cost engineering"

differentiation:
  extension_for_advanced: "Implement model-specific routing with priority chains"
  remedial_for_struggling: "Focus on token budget concept only"
---

# Envoy AI Gateway for LLM Traffic

Your rate limiter allows 100 requests per minute. User A sends 100 requests, each with a simple "Hello" prompt consuming 10 tokens. User B sends 100 requests, each asking GPT-4 to "Write a comprehensive business plan with financial projections"—consuming 8,000 tokens per request. Both users stay within your request limit. But User A cost you $0.03 while User B cost you $240. Traditional rate limiting treats all requests equally. LLM traffic is not equal.

Envoy AI Gateway is purpose-built for this problem. Released as open source by Tetrate and Bloomberg in February 2025 and backed by the CNCF, it provides token-based rate limiting, provider fallback, and unified access across LLM providers. This lesson teaches you to protect your AI services from cost overruns using the currency that actually matters: tokens.

By the end, you will configure token-based rate limits that enforce daily budgets, implement provider fallback chains that route to Anthropic when OpenAI rate limits are hit, and design cost control patterns that give each user and team their own token budget.

---

## Why Traditional Gateways Fail for LLM Traffic

Standard API gateways count requests. LLM services charge tokens. This mismatch creates three problems:

| Problem | Traditional Gateway | AI Gateway |
|---------|-------------------|------------|
| **Cost unpredictability** | 100 requests = 100 requests | 100 requests = 1,000 to 800,000 tokens |
| **Fairness** | All users get equal request quota | Heavy prompts consume disproportionate budget |
| **Provider lock-in** | Single backend per route | Automatic failover across providers |

### The Token Economy

LLM pricing operates on tokens, not requests:

| Model | Input Token Cost | Output Token Cost | 100 Requests Cost Range |
|-------|-----------------|-------------------|------------------------|
| GPT-4o | $2.50/1M tokens | $10.00/1M tokens | $0.05 - $50 |
| Claude Sonnet 4 | $3.00/1M tokens | $15.00/1M tokens | $0.06 - $60 |
| GPT-4o-mini | $0.15/1M tokens | $0.60/1M tokens | $0.002 - $2 |

**Key insight**: A single GPT-4 request can cost 100x more than another. Request counting cannot capture this variance.

---

## Envoy AI Gateway Architecture

Envoy AI Gateway extends Envoy Gateway with AI-specific capabilities. It sits between your applications and LLM providers, providing a unified API regardless of which provider handles the request.

```
                    ┌────────────────────────────────────────────────┐
                    │              Envoy AI Gateway                  │
                    │  ┌─────────────────────────────────────────┐   │
                    │  │ • Token counting                        │   │
                    │  │ • Rate limiting (tokens, not requests)  │   │
                    │  │ • Provider abstraction                  │   │
                    │  │ • Fallback routing                      │   │
                    │  └─────────────────────────────────────────┘   │
                    └────────────────────────────────────────────────┘
                                          │
           ┌──────────────────────────────┼──────────────────────────────┐
           │                              │                              │
           ▼                              ▼                              ▼
    ┌──────────────┐               ┌──────────────┐               ┌──────────────┐
    │   OpenAI     │               │  Anthropic   │               │ AWS Bedrock  │
    │   API        │               │    API       │               │     API      │
    └──────────────┘               └──────────────┘               └──────────────┘
```

### Core Components

| Component | Purpose |
|-----------|---------|
| **AIGatewayRoute** | Defines routing rules to AI backends |
| **LLMRequestCost** | Configures token extraction and cost calculation |
| **BackendTrafficPolicy** | Applies token-based rate limits |
| **AIBackend** | Configures provider credentials and endpoints |

### Unified API

Applications send requests to a single endpoint. AI Gateway translates between provider formats:

```bash
# Same request format works for any provider
curl -X POST $GATEWAY_URL/v1/chat/completions \
  -H "x-user-id: user123" \
  -H "x-ai-eg-model: gpt-4o" \
  -d '{
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

The `x-ai-eg-model` header specifies which model to use. AI Gateway routes to the appropriate provider and handles format translation.

---

## Token-Based Rate Limiting

AI Gateway extracts token counts from LLM responses and uses them for rate limiting. The system supports four token types:

| Token Type | What It Counts | Use Case |
|------------|---------------|----------|
| `InputToken` | Prompt tokens | Control input costs |
| `OutputToken` | Response tokens | Control output costs |
| `TotalToken` | Input + Output | Overall budget control |
| `CEL` | Custom calculation | Weighted pricing models |

### Configuring Token Extraction

First, configure AI Gateway to extract token usage from responses:

```yaml
apiVersion: aigateway.envoyproxy.io/v1alpha1
kind: LLMRequestCost
metadata:
  name: token-tracking
  namespace: ai-services
spec:
  llmRequestCosts:
    - metadataKey: llm_input_token
      type: InputToken
    - metadataKey: llm_output_token
      type: OutputToken
    - metadataKey: llm_total_token
      type: TotalToken
```

**Apply the configuration:**

```bash
kubectl apply -f token-tracking.yaml
```

**Output:**

```
llmrequestcost.aigateway.envoyproxy.io/token-tracking created
```

AI Gateway automatically parses token counts from responses following the OpenAI schema format. For providers like AWS Bedrock, the gateway handles format translation automatically.

### Custom Cost Calculation with CEL

Different models have different pricing. Use CEL expressions for accurate cost tracking:

```yaml
spec:
  llmRequestCosts:
    - metadataKey: llm_cost_cents
      type: CEL
      cel: "input_tokens * 0.25 + output_tokens * 1.0"
```

This calculates cost in cents where output tokens cost 4x input tokens—matching GPT-4o pricing ratios.

---

## Configuring Token Budgets Per User

Unlike request-based limits, token budgets reflect actual usage. A user who sends concise prompts consumes less budget than one who sends verbose requests.

### Basic Token Limit

Limit each user to 100,000 tokens per hour:

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: BackendTrafficPolicy
metadata:
  name: token-budget-per-user
  namespace: ai-services
spec:
  targetRefs:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      name: llm-route
  rateLimit:
    type: Global
    global:
      rules:
        - clientSelectors:
            - headers:
                - name: x-user-id
                  type: Distinct
          limit:
            requests: 100000
            unit: Hour
          cost:
            request:
              from: Number
              number: 0
            response:
              from: Metadata
              metadata:
                namespace: io.envoy.ai_gateway
                key: llm_total_token
```

**Key configuration points:**

| Field | Value | Purpose |
|-------|-------|---------|
| `x-user-id: Distinct` | Each user tracked separately | Per-user budgets |
| `cost.request.number: 0` | Zero request cost | Only tokens count |
| `cost.response.from: Metadata` | Read token count from response | Actual usage tracking |

**Apply and verify:**

```bash
kubectl apply -f token-budget-per-user.yaml
kubectl get backendtrafficpolicy -n ai-services
```

**Output:**

```
NAME                   AGE
token-budget-per-user   5s
```

### Testing Token Limits

Send requests until budget exhausted:

```bash
# Each request consumes approximately 100 tokens
for i in {1..1500}; do
  response=$(curl -s -w "\n%{http_code}" \
    -H "x-user-id: test-user" \
    -H "x-ai-eg-model: gpt-4o-mini" \
    $GATEWAY_URL/v1/chat/completions \
    -d '{"messages": [{"role": "user", "content": "Say hello"}]}')

  status=$(echo "$response" | tail -1)
  if [ "$status" = "429" ]; then
    echo "Rate limited at request $i"
    break
  fi
done
```

**Output:**

```
Rate limited at request 1024
```

The user hit their 100,000 token budget (approximately 100 tokens × 1,000 requests).

---

## Model-Specific Token Limits

Different models have different costs. Apply stricter limits to expensive models:

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: BackendTrafficPolicy
metadata:
  name: model-specific-limits
  namespace: ai-services
spec:
  targetRefs:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      name: llm-route
  rateLimit:
    type: Global
    global:
      rules:
        # GPT-4o: Expensive, strict limit
        - clientSelectors:
            - headers:
                - name: x-user-id
                  type: Distinct
                - name: x-ai-eg-model
                  type: Exact
                  value: gpt-4o
          limit:
            requests: 50000
            unit: Hour
          cost:
            request:
              from: Number
              number: 0
            response:
              from: Metadata
              metadata:
                namespace: io.envoy.ai_gateway
                key: llm_total_token

        # GPT-4o-mini: Cheaper, higher limit
        - clientSelectors:
            - headers:
                - name: x-user-id
                  type: Distinct
                - name: x-ai-eg-model
                  type: Exact
                  value: gpt-4o-mini
          limit:
            requests: 500000
            unit: Hour
          cost:
            request:
              from: Number
              number: 0
            response:
              from: Metadata
              metadata:
                namespace: io.envoy.ai_gateway
                key: llm_total_token
```

**Result**: Users get 50K tokens/hour for GPT-4o but 500K tokens/hour for GPT-4o-mini—reflecting the 10x price difference.

---

## Provider Fallback Chains

When one provider hits rate limits or experiences downtime, AI Gateway can automatically route to alternatives. This provides resilience and cost optimization.

### Configuring Multi-Provider Fallback

Route primarily to OpenAI, fall back to Anthropic:

```yaml
apiVersion: aigateway.envoyproxy.io/v1alpha1
kind: AIGatewayRoute
metadata:
  name: llm-with-fallback
  namespace: ai-services
spec:
  rules:
    - matches:
        - headers:
            - name: x-ai-eg-model
              value: gpt-4o
      backendRefs:
        - name: openai-backend
          weight: 100
          priority: 1
        - name: anthropic-backend
          weight: 100
          priority: 2
```

**How priority works:**

```
Request arrives with model: gpt-4o
    │
    ▼
Priority 1: Try OpenAI
    │
    ├── Success → Return response
    │
    └── Failure (rate limit, timeout, error)
            │
            ▼
        Priority 2: Try Anthropic
            │
            ├── Success → Return response
            │
            └── Failure → Return error to client
```

### Backend Configuration

Define credentials and endpoints for each provider:

```yaml
apiVersion: aigateway.envoyproxy.io/v1alpha1
kind: AIBackend
metadata:
  name: openai-backend
  namespace: ai-services
spec:
  provider: OpenAI
  auth:
    apiKeySecretRef:
      name: openai-credentials
      key: api-key
---
apiVersion: aigateway.envoyproxy.io/v1alpha1
kind: AIBackend
metadata:
  name: anthropic-backend
  namespace: ai-services
spec:
  provider: Anthropic
  auth:
    apiKeySecretRef:
      name: anthropic-credentials
      key: api-key
```

**Store credentials securely:**

```bash
kubectl create secret generic openai-credentials \
  --from-literal=api-key=$OPENAI_API_KEY \
  -n ai-services

kubectl create secret generic anthropic-credentials \
  --from-literal=api-key=$ANTHROPIC_API_KEY \
  -n ai-services
```

**Output:**

```
secret/openai-credentials created
secret/anthropic-credentials created
```

### Testing Fallback Behavior

Simulate OpenAI rate limiting:

```bash
# Exhaust OpenAI quota
for i in {1..100}; do
  curl -s -H "x-user-id: fallback-test" \
    -H "x-ai-eg-model: gpt-4o" \
    $GATEWAY_URL/v1/chat/completions \
    -d '{"messages": [{"role": "user", "content": "Test fallback"}]}'
done

# Check headers for routing info
curl -v -H "x-user-id: fallback-test" \
  -H "x-ai-eg-model: gpt-4o" \
  $GATEWAY_URL/v1/chat/completions \
  -d '{"messages": [{"role": "user", "content": "Which provider?"}]}' 2>&1 | grep x-ai-provider
```

**Output (after fallback):**

```
< x-ai-provider: anthropic
```

The request was served by Anthropic after OpenAI reached its limit.

---

## Cost Engineering Patterns

Effective AI cost control requires organizational-level policies, not just per-user limits.

### Pattern 1: Team Budgets

Allocate monthly token budgets per team:

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: BackendTrafficPolicy
metadata:
  name: team-budgets
  namespace: ai-services
spec:
  targetRefs:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      name: llm-route
  rateLimit:
    type: Global
    global:
      rules:
        # Engineering team: 10M tokens/day
        - clientSelectors:
            - headers:
                - name: x-team-id
                  type: Exact
                  value: engineering
          limit:
            requests: 10000000
            unit: Day
          cost:
            request:
              from: Number
              number: 0
            response:
              from: Metadata
              metadata:
                namespace: io.envoy.ai_gateway
                key: llm_total_token

        # Marketing team: 2M tokens/day
        - clientSelectors:
            - headers:
                - name: x-team-id
                  type: Exact
                  value: marketing
          limit:
            requests: 2000000
            unit: Day
          cost:
            request:
              from: Number
              number: 0
            response:
              from: Metadata
              metadata:
                namespace: io.envoy.ai_gateway
                key: llm_total_token
```

### Pattern 2: Cost Tiers with Fallback

Route expensive requests to cheaper models when budget runs low:

| Budget Remaining | Routing Strategy |
|-----------------|------------------|
| > 50% | GPT-4o (highest quality) |
| 20-50% | GPT-4o-mini (cost-efficient) |
| &lt; 20% | Reject or queue |

This requires application-level logic to check remaining budget and adjust the `x-ai-eg-model` header accordingly.

### Pattern 3: Daily Spending Caps

Convert token limits to dollar amounts:

| Daily Budget | GPT-4o Tokens | GPT-4o-mini Tokens |
|--------------|---------------|-------------------|
| $10/day | ~800,000 | ~13,000,000 |
| $100/day | ~8,000,000 | ~130,000,000 |
| $1,000/day | ~80,000,000 | ~1,300,000,000 |

Set token limits that match your dollar budget.

---

## Exercises

### Exercise 1: Configure Token Tracking

Set up token extraction for your AI Gateway:

```bash
kubectl apply -f - <<EOF
apiVersion: aigateway.envoyproxy.io/v1alpha1
kind: LLMRequestCost
metadata:
  name: exercise-tokens
  namespace: default
spec:
  llmRequestCosts:
    - metadataKey: llm_input_token
      type: InputToken
    - metadataKey: llm_output_token
      type: OutputToken
    - metadataKey: llm_total_token
      type: TotalToken
EOF
```

**Verify:**

```bash
kubectl get llmrequestcost -n default
```

**Expected Output:**

```
NAME              AGE
exercise-tokens   5s
```

### Exercise 2: Create Per-User Token Budget

Limit users to 10,000 tokens per hour:

```bash
kubectl apply -f - <<EOF
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: BackendTrafficPolicy
metadata:
  name: exercise-token-budget
  namespace: default
spec:
  targetRefs:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      name: llm-route
  rateLimit:
    type: Global
    global:
      rules:
        - clientSelectors:
            - headers:
                - name: x-user-id
                  type: Distinct
          limit:
            requests: 10000
            unit: Hour
          cost:
            request:
              from: Number
              number: 0
            response:
              from: Metadata
              metadata:
                namespace: io.envoy.ai_gateway
                key: llm_total_token
EOF
```

**Test with requests:**

```bash
curl -s -o /dev/null -w "%{http_code}\n" \
  -H "x-user-id: exercise-user" \
  $GATEWAY_URL/v1/chat/completions \
  -d '{"messages": [{"role": "user", "content": "Hello"}]}'
```

**Expected Output:**

```
200
```

### Exercise 3: Model-Specific Limits

Apply different limits for different models:

```bash
kubectl apply -f - <<EOF
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: BackendTrafficPolicy
metadata:
  name: exercise-model-limits
  namespace: default
spec:
  targetRefs:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      name: llm-route
  rateLimit:
    type: Global
    global:
      rules:
        - clientSelectors:
            - headers:
                - name: x-user-id
                  type: Distinct
                - name: x-ai-eg-model
                  type: Exact
                  value: gpt-4o
          limit:
            requests: 5000
            unit: Hour
          cost:
            request:
              from: Number
              number: 0
            response:
              from: Metadata
              metadata:
                namespace: io.envoy.ai_gateway
                key: llm_total_token
        - clientSelectors:
            - headers:
                - name: x-user-id
                  type: Distinct
                - name: x-ai-eg-model
                  type: Exact
                  value: gpt-4o-mini
          limit:
            requests: 100000
            unit: Hour
          cost:
            request:
              from: Number
              number: 0
            response:
              from: Metadata
              metadata:
                namespace: io.envoy.ai_gateway
                key: llm_total_token
EOF
```

**Verify:**

```bash
kubectl get backendtrafficpolicy exercise-model-limits -o yaml | grep -A 5 "limit:"
```

**Expected Output:**

```yaml
          limit:
            requests: 5000
            unit: Hour
...
          limit:
            requests: 100000
            unit: Hour
```

### Exercise 4: Configure Provider Fallback

Set up fallback from OpenAI to Anthropic:

```bash
kubectl apply -f - <<EOF
apiVersion: aigateway.envoyproxy.io/v1alpha1
kind: AIGatewayRoute
metadata:
  name: exercise-fallback
  namespace: default
spec:
  rules:
    - matches:
        - headers:
            - name: x-ai-eg-model
              value: gpt-4o
      backendRefs:
        - name: openai-backend
          priority: 1
        - name: anthropic-backend
          priority: 2
EOF
```

**Verify:**

```bash
kubectl get aigatewayroute exercise-fallback -o yaml | grep -A 10 "backendRefs:"
```

**Expected Output:**

```yaml
      backendRefs:
        - name: openai-backend
          priority: 1
        - name: anthropic-backend
          priority: 2
```

---

## Reflect on Your Skill

You built a `traffic-engineer` skill in Lesson 0. Based on what you learned about LLM traffic patterns:

### Add AI Gateway Decision Logic

Your skill should now include:

| Question | If Yes | If No |
|----------|--------|-------|
| Managing LLM/AI traffic? | Use Envoy AI Gateway | Use standard Envoy Gateway |
| Need token-based limits? | Configure LLMRequestCost + BackendTrafficPolicy | Use request-based limits |
| Multiple LLM providers? | Configure AIGatewayRoute with fallback | Single backend |
| Per-user cost control? | Add x-user-id header + Distinct selector | Global limits |

### Add LLM Traffic Templates

**Token budget template:**

```yaml
# Template: token-budget
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: BackendTrafficPolicy
metadata:
  name: {{ service }}-token-budget
  namespace: {{ namespace }}
spec:
  targetRefs:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      name: {{ route }}
  rateLimit:
    type: Global
    global:
      rules:
        - clientSelectors:
            - headers:
                - name: x-user-id
                  type: Distinct
          limit:
            requests: {{ token_limit | default(100000) }}
            unit: {{ unit | default("Hour") }}
          cost:
            request:
              from: Number
              number: 0
            response:
              from: Metadata
              metadata:
                namespace: io.envoy.ai_gateway
                key: llm_total_token
```

**Provider fallback template:**

```yaml
# Template: provider-fallback
apiVersion: aigateway.envoyproxy.io/v1alpha1
kind: AIGatewayRoute
metadata:
  name: {{ route }}-fallback
  namespace: {{ namespace }}
spec:
  rules:
    - matches:
        - headers:
            - name: x-ai-eg-model
              value: {{ model }}
      backendRefs:
        - name: {{ primary_provider }}-backend
          priority: 1
        - name: {{ fallback_provider }}-backend
          priority: 2
```

### Update Cost Calculation Guidance

| Model | Input Cost (per 1M) | Output Cost (per 1M) | Suggested Daily Limit ($10 budget) |
|-------|--------------------|--------------------|-----------------------------------|
| GPT-4o | $2.50 | $10.00 | 800K tokens |
| GPT-4o-mini | $0.15 | $0.60 | 13M tokens |
| Claude Sonnet 4 | $3.00 | $15.00 | 650K tokens |

---

## Try With AI

You want to configure AI Gateway for your Task API's LLM features. The API uses GPT-4o for complex reasoning and GPT-4o-mini for simple tasks. You have a $100/day budget to protect.

Ask your traffic-engineer skill:

```
Using my traffic-engineer skill, configure Envoy AI Gateway for my Task API:

- Daily budget: $100 across all users
- Per-user limit: 100,000 tokens/hour for GPT-4o, 500,000 for GPT-4o-mini
- Fallback: Route to Anthropic when OpenAI rate limits hit
- Track input and output tokens separately
```

Review AI's configuration. Check these specifics:

- Does the LLMRequestCost resource extract both input and output tokens?
- Are the BackendTrafficPolicy limits set with `cost.request.number: 0` to count only tokens?
- Does the AIGatewayRoute have proper priority settings for fallback?
- Are the token limits realistic for your $100 budget?

If the token math seems off, provide your constraint:

```
$100/day with GPT-4o pricing ($2.50 input, $10 output per million) means roughly 8M total tokens. Please recalculate the per-user limits so that 10 users sharing equally get 800K tokens each.
```

Now extend to include model-specific routing:

```
Add routing logic:
- Requests with "priority: high" header go to GPT-4o
- All other requests go to GPT-4o-mini
- Both models should fall back to Anthropic on failure
```

Verify the complete configuration before applying:

```bash
# Validate all resources
kubectl apply --dry-run=client -f ai-gateway-config.yaml

# Check for missing secrets
kubectl get secrets -n ai-services | grep credentials

# Verify route priorities
kubectl get aigatewayroute -o yaml | grep priority
```

Compare your first request to the final configuration. The initial approach likely missed either the cost calculation details or the proper header matching. Through iteration, you specified the budget constraint, the token-to-dollar conversion, and the routing requirements—producing a configuration that actually protects your $100 daily budget rather than just counting requests.

### Safety Note

Token-based rate limiting requires the AI Gateway to parse LLM responses. Ensure your gateway has sufficient resources to handle this processing overhead. Start with conservative limits (lower than calculated) and adjust based on observed usage. Monitor `x-ai-gateway-tokens-used` response headers to verify token counting accuracy before enforcing strict limits.
