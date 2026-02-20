### Core Concept
The sidecar pattern runs Dapr as a separate container alongside your application, handling infrastructure concerns (state, messaging, observability) so your code stays focused on business logic.

### Key Mental Models
- **Sidecar Container**: A helper container that runs alongside your main app, intercepting all infrastructure calls
- **App Channel**: Your app talks to localhost:3500 (HTTP) or :50001 (gRPC); Dapr translates to actual infrastructure
- **Separation of Concerns**: Application code never imports SDKs for Redis, Kafka, or cloud services directly
- **Runtime Portability**: Switch from Redis to Postgres by changing config, not code

### Critical Patterns
- Application calls localhost:3500 for all Dapr operations
- Dapr sidecar handles service discovery, retries, and protocol translation
- Component YAML files define which infrastructure backs each building block
- Sidecar injects observability (traces, metrics) automatically

### AI Collaboration Keys
- Ask Claude to explain sidecar architecture with diagrams
- Request comparison between direct SDK calls vs Dapr abstraction
- Have AI generate sidecar deployment YAML

### Common Mistakes
- Calling external services directly instead of through Dapr sidecar
- Forgetting the sidecar needs to start before the application
- Not understanding that Dapr runs as a separate process/container

### Connections
- **Builds on**: Lesson 0 - Your Dapr skill foundation
- **Leads to**: Lesson 2 - Building Blocks and Components
