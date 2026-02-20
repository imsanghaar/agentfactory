### Core Concept
Dapr pub/sub enables asynchronous messaging between services with a unified API across message brokers (Redis Streams, Kafka, RabbitMQ), supporting at-least-once delivery and CloudEvents format.

### Key Mental Models
- **Topic-Based Messaging**: Publishers send to topics; subscribers receive from topics
- **CloudEvents Format**: Standard envelope for event metadata (source, type, time)
- **At-Least-Once Delivery**: Messages are delivered at least once; handle duplicates
- **Declarative Subscriptions**: Define subscriptions in YAML or programmatically

### Critical Patterns
- Publish: POST to `/v1.0/publish/{pubsub-name}/{topic}`
- Subscribe: Expose endpoint that matches topic subscription
- Configure dead-letter topics for failed message handling
- Use message TTL for time-sensitive events

### AI Collaboration Keys
- Ask Claude to design event-driven architecture with pub/sub
- Request CloudEvents schema examples for your domain
- Have AI generate dead-letter handling strategies

### Common Mistakes
- Not handling duplicate messages (at-least-once means duplicates possible)
- Forgetting to configure dead-letter topics for poison messages
- Using pub/sub for request-response patterns (use service invocation instead)

### Connections
- **Builds on**: Lesson 4 - Service invocation for sync calls
- **Leads to**: Lesson 6 - Bindings and Triggers
