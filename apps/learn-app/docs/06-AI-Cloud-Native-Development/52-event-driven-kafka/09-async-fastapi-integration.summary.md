### Core Concept
Integrating Kafka with FastAPI requires using lifespan events for producer lifecycle management, non-blocking `produce()` with `poll(0)` for async endpoints, and background threads for blocking consumer poll loops to avoid blocking the async event loop.

### Key Mental Models
- Lifespan Pattern: Initialize producer at startup, flush and close at shutdown
- Non-Blocking Produce: `produce()` + `poll(0)` returns immediately; callbacks fire later
- Threaded Consumer: Background thread runs blocking poll loop independently from async event loop
- Global State: Single producer instance shared across all request handlers

### Critical Patterns
- `@asynccontextmanager` lifespan for producer/consumer lifecycle
- `producer.poll(0)` after produce for non-blocking callback processing
- `Thread(target=consume_loop, daemon=True)` for background consumer
- `threading.Event()` for clean consumer shutdown signaling

### AI Collaboration Keys
- Analyze async architecture decisions (one producer vs multiple, co-located vs separate consumers)
- Debug silent consumer thread death (session timeout, max.poll.interval exceeded)
- Design integration for specific domain with proper event schemas and error handling

### Common Mistakes
- Running blocking consumer poll in async function (blocks event loop)
- Forgetting `poll(0)` after produce (callbacks never fire during request)
- Not flushing producer on shutdown (messages may be lost)
- Consumer thread dying silently without health check visibility

### Connections
- **Builds on**: Lesson 8 - Consumer groups and proper offset management
- **Leads to**: Lesson 10 - Message Schemas with Avro
