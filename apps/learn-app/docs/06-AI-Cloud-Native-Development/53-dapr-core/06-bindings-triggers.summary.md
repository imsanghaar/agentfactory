### Core Concept
Dapr bindings connect your application to external systems (databases, queues, cloud services) through input triggers (events coming in) and output operations (actions going out).

### Key Mental Models
- **Input Bindings (Triggers)**: External events call your app (e.g., new file in S3 triggers handler)
- **Output Bindings (Operations)**: Your app calls external systems (e.g., send email, write to blob)
- **Bidirectional Support**: Some bindings support both input and output (e.g., Kafka)
- **Component Abstraction**: Switch from AWS S3 to Azure Blob by changing YAML, not code

### Critical Patterns
- Input binding: Expose POST endpoint matching binding name
- Output binding: POST to `/v1.0/bindings/{binding-name}` with operation and data
- Configure binding metadata for connection and behavior
- Use scopes to restrict which apps can use which bindings

### AI Collaboration Keys
- Ask Claude to list available bindings for your cloud provider
- Request input binding handler examples for cron schedules
- Have AI generate output binding configurations for notifications

### Common Mistakes
- Confusing bindings with pub/sub (bindings are for external systems, pub/sub for inter-service)
- Not handling binding errors and dead-letter scenarios
- Forgetting that input bindings require exposed HTTP endpoints

### Connections
- **Builds on**: Lesson 5 - Pub/sub for internal messaging
- **Leads to**: Lesson 7 - Jobs API
