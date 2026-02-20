### Core Concept
Strimzi provides Kubernetes-native Kafka deployment through Custom Resource Definitions (CRDs), allowing declarative cluster configuration that operators manage automatically, using KRaft mode for simplified architecture without ZooKeeper.

### Key Mental Models
- Operator Pattern: Declare intent ("I want a 3-broker cluster"), operator achieves and maintains it
- KafkaNodePool: Define node roles (controller/broker) and resources separately from cluster config
- Topic Operator: KafkaTopic CRDs automatically synced to actual Kafka topics (GitOps-friendly)
- Bootstrap Service: Stable endpoint for client connections regardless of pod restarts

### Critical Patterns
- Helm install: `helm install strimzi-kafka-operator strimzi/strimzi-kafka-operator -n kafka`
- KafkaNodePool with dual-role for development (controller + broker in one node)
- Kafka CRD with `strimzi.io/kraft: enabled` annotation for KRaft mode
- KafkaTopic CRD for declarative, version-controlled topic management

### AI Collaboration Keys
- Review development configuration for production gaps (replicas, storage, replication factor)
- Debug operator issues using CRD status conditions and operator logs
- Understand partition count and cleanup policy trade-offs for different use cases

### Common Mistakes
- Using ephemeral storage in production (data lost on restart)
- Replication factor of 1 in production (no fault tolerance)
- Forgetting to wait for cluster Ready status before creating topics
- Not understanding the Topic Operator sync mechanism

### Connections
- **Builds on**: Lesson 3 - Kafka mental model and architecture
- **Leads to**: Lesson 5 - Your First Producer
