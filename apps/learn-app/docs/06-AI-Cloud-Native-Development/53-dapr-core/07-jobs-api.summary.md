### Core Concept
The Dapr Jobs API enables scheduled and recurring task execution with cron expressions, providing a distributed scheduler that persists across restarts and scales horizontally.

### Key Mental Models
- **Scheduled Jobs**: One-time or recurring tasks defined by cron expressions
- **Job Persistence**: Jobs survive restarts through state store backing
- **Distributed Execution**: Jobs run once even with multiple app replicas
- **Job Lifecycle**: Create, trigger, monitor, and cancel jobs via API

### Critical Patterns
- Create job: POST to `/v1.0/jobs/{job-name}` with schedule and callback
- Jobs invoke your app's endpoint when triggered
- Use state store component for job persistence
- Configure job TTL and retry policies

### AI Collaboration Keys
- Ask Claude to generate cron expressions for business schedules
- Request job handler patterns for long-running tasks
- Have AI design job monitoring and alerting

### Common Mistakes
- Not backing jobs with a persistent state store (jobs lost on restart)
- Ignoring idempotency in job handlers (jobs may re-execute)
- Using jobs for high-frequency polling (use bindings or subscriptions instead)

### Connections
- **Builds on**: Lesson 6 - Bindings for event-driven triggers
- **Leads to**: Lesson 8 - Secrets and Configuration
