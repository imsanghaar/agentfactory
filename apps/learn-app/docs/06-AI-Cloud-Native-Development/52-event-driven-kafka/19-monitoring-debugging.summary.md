### Core Concept
Consumer lag is the most critical Kafka metric - it reveals whether consumers keep pace with producers. Combined with under-replicated partition monitoring and Kafka CLI tools, you can diagnose and resolve production issues systematically.

### Key Mental Models
- **Lag vs throughput**: High throughput means nothing if producers write faster - lag shows the gap growing over time
- **Lag patterns**: All partitions lagging = overall slowness; one partition lagging = hot partition or stuck consumer
- **Under-replicated partitions**: ISR smaller than replication factor indicates broker health issues
- **Alert thresholds**: Lag alert when exceeding 1/3 of what you can process during retention period

### Critical Patterns
- `kafka-consumer-groups.sh --describe --group <name>`: Shows CURRENT-OFFSET, LOG-END-OFFSET, LAG per partition
- `kafka-topics.sh --describe --under-replicated-partitions`: Lists partitions where ISR &lt; RF
- `kafka-console-consumer.sh --from-beginning --max-messages N`: Read actual messages for debugging
- Lag alert tiers: warning (1000, 5min), critical (10000, 2min), emergency (100000, 1min approaching retention)
- JMX metrics: `UnderReplicatedPartitions`, `BytesInPerSec`, `TotalTimeMs` for production monitoring

### AI Collaboration Keys
- Use AI to interpret `kafka-consumer-groups.sh` output and identify asymmetric lag patterns
- Ask AI to build troubleshooting checklists for specific errors (NOT_ENOUGH_REPLICAS, REBALANCE_IN_PROGRESS)
- Leverage AI to design alert thresholds based on your SLAs, traffic rates, and topic priorities

### Common Mistakes
- Ignoring growing lag until it approaches retention limit and causes data loss
- Running modifying commands (reset offsets, delete topics) on production without understanding implications
- Setting same alert thresholds for all topics regardless of business priority and processing rates

### Connections
- **Builds on**: Lesson 18 (Production Kafka - cluster health fundamentals)
- **Leads to**: Lesson 20 (AI-Assisted Kafka Development - using AI for debugging and optimization)
