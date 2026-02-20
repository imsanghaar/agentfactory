### Core Concept
The capstone integrates all Dapr building blocks into the Task API, demonstrating state management, service invocation, pub/sub, and secrets in a cohesive production-ready application.

### Key Mental Models
- **Building Block Composition**: Combine multiple Dapr features in one application
- **Event-Driven Architecture**: Tasks publish events on state changes; subscribers react
- **Infrastructure Abstraction**: The same code works with different backends via components
- **Production Patterns**: Health checks, graceful shutdown, observability integration

### Critical Patterns
- State management for task persistence with ETags
- Pub/sub for task created/completed events
- Service invocation for inter-service calls
- Secrets for database credentials and API keys

### AI Collaboration Keys
- Ask Claude to review your Dapr integration architecture
- Request error handling patterns for distributed operations
- Have AI generate component YAML for production deployment

### Common Mistakes
- Not handling Dapr sidecar unavailability gracefully
- Missing health check endpoints for Kubernetes liveness probes
- Forgetting to configure resiliency policies for production

### Connections
- **Builds on**: Lessons 1-8 covering all Dapr building blocks
- **Leads to**: Lesson 10 - Finalize Dapr Skill
