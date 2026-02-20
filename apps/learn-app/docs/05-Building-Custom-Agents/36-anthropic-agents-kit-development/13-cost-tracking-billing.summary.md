### Core Concept
Track total_cost_usd from result messages to understand agent economics. Extract per-message token usage, aggregate by customer, design pricing models (subscription, usage-based, success-fee) that ensure 60%+ margin.

### Key Mental Models
- **Cost drivers**: per-message tokens, model selection (Haiku 2-3x cheaper), context window size, max_turns
- **Margin math**: Price = Cost / (1 - Target Margin %). Example: $1 cost, 70% margin = $3.33 price
- **Billing models**: Subscription (predictable), usage-based (scales), success-fee (value-aligned)

### Critical Patterns
- Extract cost: `if message.type == "result": cost = message.total_cost_usd`
- Customer tracking: Aggregate costs by customer_id, calculate monthly profitability
- Budget enforcement: Stop execution if total_cost_usd exceeds threshold
- Cost optimization: max_turns limits, Haiku for simple tasks, context pruning

### AI Collaboration Keys
- Track costs per-operation to identify expensive features worth optimizing
- Use model selection (Haiku vs Sonnet) strategically based on task complexity
- Design pricing that covers worst-case high-usage customers

### Common Mistakes
- Shipping product without cost visibility (loses money on every customer)
- Pricing based on value without understanding cost basis
- Using Opus for simple classification (Haiku is 10x cheaper)

### Connections
- **Builds on**: ClaudeSDKClient and Streaming (Lesson 12)
- **Leads to**: Production Patterns (Lesson 14)
