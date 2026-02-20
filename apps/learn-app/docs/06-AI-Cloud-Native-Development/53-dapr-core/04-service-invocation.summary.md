### Core Concept
Dapr service invocation enables service-to-service calls using app IDs instead of URLs, with automatic service discovery, mTLS, retries, and observability built in.

### Key Mental Models
- **App ID Addressing**: Call services by name (order-service) not URL (http://10.0.0.5:8080)
- **Sidecar-to-Sidecar Communication**: Your sidecar finds and calls the target's sidecar
- **Automatic mTLS**: All service-to-service traffic is encrypted without code changes
- **Retry Policies**: Failed calls are automatically retried with configurable backoff

### Critical Patterns
- Invoke: POST to `/v1.0/invoke/{app-id}/method/{method-name}`
- Pass request body and headers through the Dapr sidecar
- Configure resiliency policies for retry and timeout
- Use access control policies to restrict which services can call which

### AI Collaboration Keys
- Ask Claude to generate service invocation code examples
- Request resiliency policy configurations for production
- Have AI explain mTLS certificate rotation

### Common Mistakes
- Hardcoding service URLs instead of using app IDs
- Not configuring resiliency policies for network failures
- Forgetting access control policies for sensitive services

### Connections
- **Builds on**: Lesson 3 - State management patterns
- **Leads to**: Lesson 5 - Pub/Sub Messaging
