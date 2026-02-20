### Core Concept
Consumer groups distribute partitions across consumers for parallel processing, but rebalancing (triggered by consumer join/leave/timeout) can cause duplicate processing unless offsets are committed synchronously in the `on_revoke` callback before partition reassignment.

### Key Mental Models
- Partition Assignment Rules: One partition per consumer, consumer can have multiple partitions, excess consumers idle
- Rebalance Triggers: Consumer join/leave, timeout (missed heartbeat), subscription change, partition count change
- Revoke Window: Time between receiving revoke and partition reassignment where uncommitted messages will duplicate
- Static Membership: Persistent consumer identity prevents unnecessary rebalances during restarts

### Critical Patterns
- `on_revoke` callback with synchronous commit: `consumer.commit(asynchronous=False)`
- Cooperative rebalancing: `partition.assignment.strategy: cooperative-sticky` for minimal disruption
- Static membership: `group.instance.id` prevents rebalance during rolling updates
- Consumer lag monitoring: `CURRENT-OFFSET` vs `LOG-END-OFFSET` indicates processing health

### AI Collaboration Keys
- Analyze rebalance scenarios to understand duplicate processing causes
- Debug asymmetric consumer lag (one partition falling behind others)
- Design consumer configuration for Kubernetes with autoscaling and no-duplicate requirements

### Common Mistakes
- Auto-commit without rebalance callbacks (duplicates on scale events)
- Asynchronous commit in `on_revoke` (may not complete before reassignment)
- Too short `session.timeout.ms` causing false death detection
- Processing taking longer than `max.poll.interval.ms` triggering rebalance

### Connections
- **Builds on**: Lesson 7 - Basic consumer with manual commit
- **Leads to**: Lesson 9 - Async FastAPI Integration
