### Core Concept
Apache Avro provides schema-based binary serialization with Schema Registry for centralized schema management, enabling backward-compatible schema evolution through optional fields with defaults while blocking incompatible changes that would break consumers.

### Key Mental Models
- Schema as Contract: Explicit structure documentation vs implicit JSON agreements
- Binary Efficiency: Field names not in payload; 50-70% smaller than JSON
- Schema Registry Workflow: Register schema, get ID, embed ID in message, consumer fetches schema by ID
- Compatibility Modes: BACKWARD (new reads old), FORWARD (old reads new), FULL (both)

### Critical Patterns
- Union types for optional fields: `["null", "int"]` with `default: null`
- AvroSerializer/AvroDeserializer with SchemaRegistryClient
- `test_compatibility()` before registering schema changes
- Subject naming: `<topic>-<key|value>` by default

### AI Collaboration Keys
- Design event schemas with required vs optional fields for future evolution
- Plan schema evolution identifying which changes are backward compatible
- Debug compatibility errors understanding that rename = delete + add

### Common Mistakes
- Adding required field without default (breaks backward compatibility)
- Renaming fields (treated as remove + add, breaks compatibility)
- Overusing union types defeating schema's contract value
- Coupling event schema to consumer needs rather than producer's domain

### Connections
- **Builds on**: Lesson 9 - FastAPI integration with JSON serialization
- **Leads to**: Lesson 11 - Delivery Semantics Deep Dive
