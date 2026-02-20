### Core Concept
Production Kafka requires separate controller and broker node pools for independent failure domains, TLS encryption for all traffic, SCRAM-SHA-512 authentication with topic-level ACLs, and proper resource limits for predictable performance.

### Key Mental Models
- **Controller vs broker separation**: Controllers handle metadata via Raft consensus; brokers handle message I/O - separate pools enable independent scaling and failure isolation
- **TLS + SCRAM layering**: TLS encrypts traffic (prevents eavesdropping); SCRAM authenticates clients (prevents unauthorized access)
- **ACL patterns**: Prefix patterns (`topic: task-*`) enable fine-grained access control without per-topic configuration
- **JVM heap sizing rule**: Set `-Xmx` to HALF of memory limit; leave other half for OS page cache critical for read performance

### Critical Patterns
- Controller pool: 3 replicas (odd number for Raft quorum), 10Gi storage, 2Gi memory limit
- Broker pool: 3+ replicas, 100Gi+ storage, 8Gi memory limit, roles: [broker] only
- TLS listener on port 9093 with `authentication.type: scram-sha-512`
- KafkaUser CRD: Define ACLs with resource type (topic/group), pattern (prefix/literal), operations (Write/Read/Describe)
- Critical Kafka config: `auto.create.topics.enable: false`, `min.insync.replicas: 2`, `default.replication.factor: 3`

### AI Collaboration Keys
- Use AI to perform security audits identifying remaining attack vectors and ACL improvements
- Ask AI to help with capacity planning calculations (throughput x retention x RF / broker count)
- Leverage AI to troubleshoot production issues like NotEnoughReplicasException or asymmetric disk usage

### Common Mistakes
- Running dual-role nodes (controller + broker) in production, creating blast radius for failures
- Setting JVM heap to full memory limit, starving OS page cache and degrading read performance
- Using development settings (`replication.factor=1`) that provide no fault tolerance

### Connections
- **Builds on**: Lesson 17 (Saga Pattern - production patterns requiring reliable Kafka)
- **Leads to**: Lesson 19 (Monitoring and Debugging - validating production cluster health)
