### Core Concept
Kafka Connect is a framework for building standardized, scalable data pipelines using pre-built connectors instead of custom code, deployed on Kubernetes via Strimzi's KafkaConnect and KafkaConnector CRDs.

### Key Mental Models
- **Workers vs Connectors vs Tasks**: Workers are JVM processes hosting tasks; connectors define the job; tasks do actual data movement
- **Source vs Sink**: Source connectors pull data INTO Kafka; sink connectors push data OUT OF Kafka
- **Configuration over code**: 200+ pre-built connectors mean most integrations are YAML configuration, not custom producers/consumers
- **Internal topics for state**: Connect uses offset-storage, config-storage, and status-storage topics for coordination

### Critical Patterns
- Enable `strimzi.io/use-connector-resources: "true"` annotation to manage connectors via KafkaConnector CRDs
- Build connector images using Strimzi's `build.plugins` to include connector JARs from Maven
- Key converter settings: `key.converter`, `value.converter` control message serialization (JSON, Avro, String)
- Link KafkaConnector to KafkaConnect via `strimzi.io/cluster` label matching the connect cluster name
- Monitor connector state: RUNNING (healthy), PAUSED (stopped), FAILED (crashed), UNASSIGNED (no worker)

### AI Collaboration Keys
- Use AI to design pipeline topology and identify which connectors you need for your integration
- Ask AI to help troubleshoot connector failures with systematic debugging steps
- Leverage AI to evaluate when Kafka Connect fits vs when custom code is needed for your specific constraints

### Common Mistakes
- Writing custom producer/consumer code for integrations where a pre-built connector exists
- Forgetting to set replication factor for Connect internal topics in production
- Using source connectors with write permissions on production databases without read-only replicas

### Connections
- **Builds on**: Lesson 13 (Reliability Configuration - production Kafka setup)
- **Leads to**: Lesson 15 (CDC with Debezium - specialized source connector for database changes)
