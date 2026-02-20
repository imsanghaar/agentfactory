### Core Concept
Change Data Capture (CDC) with Debezium solves the dual-write problem by reading database transaction logs (WAL) directly, enabling atomic database-and-event consistency through the transactional outbox pattern.

### Key Mental Models
- **Dual-write problem**: Writing to database then Kafka separately creates crash window where data exists but event never publishes
- **WAL-based CDC**: Debezium reads PostgreSQL Write-Ahead Log as replication client - every committed change captured exactly once
- **Transactional outbox**: Write domain data + event to outbox table in same DB transaction; CDC captures outbox and publishes to Kafka
- **Operation codes**: Debezium events include `op` field: `c` (create), `u` (update), `d` (delete), `r` (snapshot read)

### Critical Patterns
- PostgreSQL setup: Enable `wal_level=logical`, create replication user with `LOGIN REPLICATION` permissions
- Debezium connector deployed via Strimzi KafkaConnector CRD with `io.debezium.connector.postgresql.PostgresConnector` class
- Use `table.include.list` to capture specific tables; use `topic.prefix` to namespace CDC topics
- Outbox Event Router transformation (`io.debezium.transforms.outbox.EventRouter`) converts outbox rows to clean domain events
- Outbox table design: `id`, `aggregate_type`, `aggregate_id`, `event_type`, `payload` (JSONB), `created_at`

### AI Collaboration Keys
- Use AI to design outbox table schema and transactional insert patterns for your specific domain events
- Ask AI for systematic debugging when Debezium connector is RUNNING but no events appear
- Leverage AI to evaluate CDC vs polling tradeoffs for your specific latency and volume requirements

### Common Mistakes
- Not enabling logical replication in PostgreSQL before deploying Debezium connector
- Capturing business tables directly instead of using outbox pattern, coupling consumers to internal schema
- Ignoring WAL disk growth when connector stops reading - replication slots hold WAL indefinitely

### Connections
- **Builds on**: Lesson 14 (Kafka Connect - KafkaConnect/KafkaConnector deployment)
- **Leads to**: Lesson 16 (Agent Event Patterns - correlation IDs, event schemas for agents)
