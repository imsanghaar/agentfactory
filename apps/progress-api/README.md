# Progress API

Gamification and progress tracking service for the Agent Factory platform.

## Development

```bash
# Start local services
docker compose up -d

# Install dependencies
uv sync

# Run server
uv run uvicorn progress_api.main:app --reload --port 8002

# Run tests
uv run pytest tests/ -v
```
