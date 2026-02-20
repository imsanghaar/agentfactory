# Mem0 API Reference

## Installation

```bash
pip install mem0ai
export OPENAI_API_KEY="your-key"
```

## Memory Class

```python
from mem0 import Memory

m = Memory()  # Default config
m = Memory.from_config(config)  # Custom config
```

## Core Operations

### add()

Store conversation history and facts.

```python
result = m.add(
    messages=[
        {"role": "user", "content": "Hi, I'm Alex."},
        {"role": "assistant", "content": "Hello Alex!"}
    ],
    user_id="alex",          # Required: scope to user
    agent_id="support",      # Optional: scope to agent
    session_id="sess-123",   # Optional: scope to session
    run_id="run-456",        # Optional: scope to run
    metadata={               # Optional: custom metadata
        "category": "preferences",
        "project": "task-api"
    },
    infer=True               # Default: extract facts; False: store raw
)

# Returns: {"results": [{"id": "mem_abc123", "memory": "Name is Alex"}]}
```

### search()

Retrieve relevant memories.

```python
results = m.search(
    query="What do you know about me?",
    user_id="alex",          # Required for user-scoped search
    filters={                # Optional: additional filters
        "category": "preferences"
    },
    top_k=5,                 # Number of results
    threshold=0.7,           # Minimum similarity score
    rerank=True              # Optional: enable reranking
)

# Returns: {
#   "results": [
#     {
#       "id": "mem_123abc",
#       "memory": "Name is Alex. Enjoys basketball.",
#       "user_id": "alex",
#       "categories": ["personal_info"],
#       "created_at": "2025-01-01T00:00:00Z",
#       "score": 0.89
#     }
#   ]
# }
```

### Filter Patterns

```python
# By user
filters={"user_id": "alex"}

# Multiple conditions (AND)
filters={
    "AND": [
        {"user_id": "alex"},
        {"agent_id": "chatbot"},
        {"run_id": "session-123"}
    ]
}

# Date range
filters={
    "AND": [
        {"user_id": "alex"},
        {"created_at": {"gte": "2024-07-01"}}
    ]
}

# By category
filters={
    "AND": [
        {"user_id": "alex"},
        {"categories": {"contains": "food"}}
    ]
}
```

### update()

Modify existing memory.

```python
m.update(
    memory_id="mem_123abc",
    new_content="Updated information about Alex"
)
```

### delete()

Remove memories.

```python
# Single memory
m.delete(memory_id="mem_123abc")

# Bulk delete by filter (check docs for exact API)
```

## Configuration Options

### Default Configuration

```python
# Uses:
# - LLM: OpenAI gpt-4.1-nano-2025-04-14
# - Embeddings: text-embedding-3-small (1536 dims)
# - Vector Store: Qdrant on-disk at /tmp/qdrant
# - History: SQLite at ~/.mem0/history.db
```

### Custom LLM

```python
config = {
    "llm": {
        "provider": "anthropic",  # or "openai", "ollama", "groq", etc.
        "config": {
            "model": "claude-3-5-sonnet-20241022",
            "api_key": "your-anthropic-key"
        }
    }
}
```

### Custom Vector Store

```python
config = {
    "vector_store": {
        "provider": "qdrant",  # or "chroma", "pinecone", "pgvector"
        "config": {
            "path": "./my_memories"
        }
    }
}
```

### Custom Embeddings

```python
config = {
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    }
}
```

### Full Custom Config

```python
config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4o-mini",
            "api_key": "your-key"
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "path": "./my_memories"
        }
    }
}

m = Memory.from_config(config)
```

## Supported Providers

### LLMs
- OpenAI
- Anthropic
- Azure OpenAI
- Ollama (local)
- Together
- Groq
- LiteLLM
- Mistral AI
- Google AI
- AWS Bedrock
- DeepSeek
- xAI
- vLLM

### Vector Stores
- Qdrant (default)
- Chroma
- Pinecone
- PostgreSQL (pgvector)
- MongoDB
- And 20+ more

### Embedding Models
- OpenAI (text-embedding-3-small, text-embedding-3-large)
- HuggingFace
- Custom embedders

## Common Dimension Error

```
ValueError: shapes (0,1536) and (768,) not aligned
```

**Fix**: Ensure `embedding_model_dims` matches your embedder output.

```python
config = {
    "embedder": {
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "embedding_model_dims": 384  # Match model output
        }
    }
}
```

## Platform vs OSS

| Feature | Platform | OSS |
|---------|----------|-----|
| Installation | API key | pip install |
| Infrastructure | Managed | Self-hosted |
| Graph memory | Yes | Limited |
| SOC 2 compliance | Yes | Your responsibility |
| Cost | Per-API call | Free (compute costs) |
