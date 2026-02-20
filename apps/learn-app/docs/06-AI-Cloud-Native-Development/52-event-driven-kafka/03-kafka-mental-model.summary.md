### Core Concept
Kafka's architecture consists of topics (named streams), partitions (parallelism units), offsets (bookmarks for position), and consumer groups (teams sharing work), with ordering guaranteed within partitions but not across them.

### Key Mental Models
- Newspaper Analogy: Topics are sections, partitions are delivery routes, consumer groups are subscriber types
- Append-Only Log: Events are never modified, only appended; retention-based cleanup
- Partition as Ordering Unit: Same key always routes to same partition; ordering within, not across
- Consumer Group Work Distribution: Each partition assigned to exactly one consumer in group

### Critical Patterns
- Message key determines partition: `hash(key) % partitions = target partition`
- Consumer scaling limit: consumers cannot exceed partition count (idle consumers)
- Offset tracking: resume after crash, replay events, skip ahead, track lag
- KRaft mode: built-in Raft consensus, no external ZooKeeper required

### AI Collaboration Keys
- Get quizzed on topic/partition/offset relationships and consumer group mechanics
- Design Kafka topology for your specific use case (topics, partitions, keys, consumer groups)
- Explore failure scenarios to understand what Kafka guarantees vs application responsibility

### Common Mistakes
- Expecting ordering across partitions (only guaranteed within single partition)
- Adding more consumers than partitions (excess consumers sit idle)
- Forgetting that multiple consumer groups read same events independently
- Not understanding that offset commit timing affects delivery semantics

### Connections
- **Builds on**: Lesson 2 - EDA concepts, events vs commands
- **Leads to**: Lesson 4 - Deploying Kafka with Strimzi
