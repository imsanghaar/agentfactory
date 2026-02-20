### Core Concept
Production servers never crash on user errors. Catch exceptions with structured try/except, return JSON-RPC errors, distinguish transient (retry) from permanent (fail) errors, design idempotent operations for retry safety.

### Key Mental Models
- **JSON-RPC error format**: {code, message, data} with standard codes (-32700 to -32000)
- **Transient vs permanent**: Timeout → retry with backoff; 404 → fail immediately
- **Graceful degradation**: Batch operations return partial results, not total failure
- **Idempotency**: Same request twice = same result; use idempotency keys for state changes

### Critical Patterns
- Error structure: `{"code": -32000, "message": "...", "data": {"is_transient": true}}`
- Catch specific first: `except FileNotFoundError` before `except Exception`
- Retry with backoff: `await asyncio.sleep(2 ** attempt)` for exponential backoff
- Idempotency key: Check for duplicate before processing; cache result for retries
- Resource cleanup: `finally:` block ensures cleanup even on error

### AI Collaboration Keys
- Log context before raising exceptions for debuggability
- Return partial results from batch operations when some items fail
- Never log sensitive data (passwords, tokens, PII)

### Common Mistakes
- Letting exceptions propagate uncaught (crashes server)
- Retrying permanent errors forever (wastes resources)
- Not using idempotency keys for state-changing operations (duplicates on retry)

### Connections
- **Builds on**: Stateful vs Stateless Servers (Lesson 6)
- **Leads to**: Packaging & Distribution (Lesson 8)
