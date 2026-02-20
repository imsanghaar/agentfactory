### Core Concept
Dapr state management provides a consistent key-value API across any state store (Redis, Postgres, Azure Cosmos), with built-in support for concurrency, transactions, and TTL.

### Key Mental Models
- **State Store Abstraction**: One API for all backends (GET/POST to /v1.0/state/{store-name})
- **ETags for Concurrency**: Optimistic locking prevents lost updates in concurrent writes
- **First-Write-Wins vs Last-Write-Wins**: Choose concurrency strategy per operation
- **Transactional State**: Atomic multi-key operations when backend supports it

### Critical Patterns
- Store state: POST to `/v1.0/state/statestore` with key-value pairs
- Retrieve state: GET from `/v1.0/state/statestore/{key}`
- Use ETags for optimistic concurrency control
- Configure TTL for automatic expiration

### AI Collaboration Keys
- Ask Claude to generate state store component YAML
- Request ETag handling examples for concurrent updates
- Have AI explain transaction semantics for different backends

### Common Mistakes
- Ignoring ETags and experiencing lost updates
- Assuming all state stores support transactions (they don't)
- Not configuring key prefix scoping for multi-tenant scenarios

### Connections
- **Builds on**: Lesson 2 - Building blocks and components
- **Leads to**: Lesson 4 - Service Invocation
