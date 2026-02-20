### Core Concept
Resources are app-controlled read-only data the application decides when to expose. Unlike tools where model decides invocation, resources are pre-authorized data the app explicitly provides—perfect for document mentions (@file) and context injection.

### Key Mental Models
- **App-controlled**: Application decides what data is exposed and when (vs model-controlled tools)
- **Read-only access**: Resources provide data without side effects—use tools for modifications
- **Direct vs templated**: Direct URIs point to specific data; templated URIs (`docs://documents/{doc_id}`) match patterns
- **Pre-authorized**: Application has already made security decision—model just reads what's available

### Critical Patterns
- Discovery: `resources/list` returns available resources with URI, name, description, mimeType
- Reading: `resources/read` with URI returns content with appropriate MIME type
- URI patterns: `scheme://path` (e.g., `docs://documents/quarterly-report-2024`)
- MIME types: `text/plain`, `text/markdown`, `application/json`, `application/pdf`

### AI Collaboration Keys
- Use resources for @document mentions (user explicitly referenced data)
- Combine resources (browsing) with tools (actions) for complete workflows
- MIME types tell model how to interpret content

### Common Mistakes
- Using resources for actions (they're read-only—use tools instead)
- Exposing sensitive data without access control (resources are pre-authorized)
- Wrong MIME types (losing structure information)

### Connections
- **Builds on**: Tools: The Model-Controlled Primitive (Lesson 3)
- **Leads to**: Prompts: The User-Controlled Primitive (Lesson 5)
