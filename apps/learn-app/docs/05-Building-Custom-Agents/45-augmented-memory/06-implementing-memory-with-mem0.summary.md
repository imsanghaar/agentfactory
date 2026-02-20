### Core Concept
Mem0 is an open-source memory layer handling embeddings, vector storage, and retrieval infrastructure. One line initialization provides a working memory system that extracts facts from conversations automatically.

### Key Mental Models
- Mem0 extracts distilled knowledge from conversations, not raw messages
- User scoping with `user_id` isolates memories per user
- Metadata enables category-based filtering for targeted retrieval
- Memory persists across sessions because Mem0 stores data on disk

### Critical Patterns
- Basic operations: `m.add(messages, user_id)` stores, `m.search(query, user_id)` retrieves
- Metadata attachment: `metadata={"category": "preferences"}` enables filtered queries
- Complex filters: `{"AND": [{"user_id": ...}, {"category": ...}, {"created_at": {"gte": ...}}]}`
- FastAPI integration: `get_user_preferences()`, `get_project_context()`, `store_interaction()` functions
- GDPR deletion: iterate through `m.search()` results and `m.delete()` each memory

### AI Collaboration Keys
- Use AI to design memory lifecycle for create/complete task workflows
- Have AI create metadata schemas mapping to application domain models
- Practice conflict detection and resolution flows using Mem0's update/delete operations

### Common Mistakes
- Storing raw conversation messages instead of letting Mem0 extract facts
- Forgetting to include `user_id` in operations, causing cross-user memory leakage
- Not designing metadata schema upfront, making filtering difficult later

### Connections
- **Builds on**: Lessons 1-5 (conceptual foundation for memory systems)
- **Leads to**: Lesson 7 - Memory-Augmented Agent Patterns (production integration patterns)
