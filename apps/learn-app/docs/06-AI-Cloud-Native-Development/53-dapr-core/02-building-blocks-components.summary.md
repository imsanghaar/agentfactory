### Core Concept
Dapr provides building blocks (APIs for common patterns) and components (pluggable implementations), separating what you want to do from how it's implemented.

### Key Mental Models
- **Building Blocks**: Abstract APIs (state, pub/sub, bindings) that define capabilities
- **Components**: Concrete implementations (Redis, Kafka, Azure) that fulfill building blocks
- **Component YAML**: Configuration that maps a building block to a specific implementation
- **Hot-Swappable Infrastructure**: Change components without modifying application code

### Critical Patterns
- Building blocks define the API contract (e.g., GET/POST /state)
- Components implement the contract for specific technologies
- Component metadata configures connection details and behavior
- Scopes restrict which apps can access which components

### AI Collaboration Keys
- Ask Claude to list all Dapr building blocks with use cases
- Request component comparison tables (Redis vs Postgres for state)
- Have AI generate component YAML for your infrastructure

### Common Mistakes
- Confusing building blocks (API) with components (implementation)
- Not specifying component scopes, allowing unintended access
- Forgetting to apply component YAML to the cluster

### Connections
- **Builds on**: Lesson 1 - Sidecar pattern understanding
- **Leads to**: Lesson 3 - State Management in practice
