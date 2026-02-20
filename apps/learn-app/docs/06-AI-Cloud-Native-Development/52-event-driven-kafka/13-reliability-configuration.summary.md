### Core Concept
Kafka reliability depends on In-Sync Replicas (ISR), replication factor, and min.insync.replicas working together to guarantee durability, with producer batching settings controlling the latency-throughput tradeoff.

### Key Mental Models
- **Durability formula**: To tolerate N broker failures, need `replication.factor >= N+1` AND `min.insync.replicas >= N+1`
- **ISR dynamics**: Replicas fall out of sync when lag exceeds `replica.lag.time.max.ms` (default 30s)
- **acks=all with ISR**: Producer waits for ALL in-sync replicas, not all replicas in cluster
- **Batching tradeoff**: `linger.ms` controls wait time, `batch.size` controls max batch - either triggers send

### Critical Patterns
- Production baseline: `replication.factor=3`, `min.insync.replicas=2` tolerates single broker failure
- NOT_ENOUGH_REPLICAS error protects data by refusing writes when ISR &lt; min.insync.replicas
- JVM heap sizing: Set `-Xmx` to half memory limit, leave other half for OS page cache
- Low latency config: `linger.ms=0`, `batch.size=16KB` - send immediately
- High throughput config: `linger.ms=50-500`, `batch.size=512KB-1MB`, `compression.type=lz4`

### AI Collaboration Keys
- Ask AI to help map business requirements (critical vs analytics events) to durability configurations
- Use AI to diagnose NOT_ENOUGH_REPLICAS errors by correlating with broker health indicators
- Leverage AI to calculate optimal batching settings for specific latency and throughput requirements

### Common Mistakes
- Assuming `acks=all` guarantees durability when ISR has shrunk to just the leader
- Setting `unclean.leader.election.enable=true` for business-critical data, risking data loss
- Using same producer configuration for real-time events and batch data pipelines

### Connections
- **Builds on**: Lesson 12 (Transactions - read_committed isolation, ISR acknowledgment)
- **Leads to**: Lesson 14 (Kafka Connect - production data pipelines)
