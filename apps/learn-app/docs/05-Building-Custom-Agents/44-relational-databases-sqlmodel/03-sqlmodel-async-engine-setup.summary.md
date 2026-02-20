### Core Concept
Configure async database engines with `create_async_engine`, proper connection pooling, URL conversion from sync to async format, and secure credential handling for production reliability.

### Key Mental Models
- Engine is connection manager: Create once at startup, manages pool
- Pool prevents overhead: Reuse connections instead of opening new ones
- `pool_pre_ping=True` is essential: Detects stale connections before use
- Never hardcode credentials: Use environment variables or secret managers

### Critical Patterns
- URL conversion: `postgresql://` to `postgresql+asyncpg://`, `sqlite:///` to `sqlite+aiosqlite:///`
- Pool configuration: `pool_size=5`, `max_overflow=10`, `pool_pre_ping=True`, `pool_recycle=300`
- Use SQLite async for testing: `sqlite+aiosqlite:///:memory:`
- Table creation: `await conn.run_sync(SQLModel.metadata.create_all)`
- FastAPI lifespan: Create tables on startup, dispose engine on shutdown

### AI Collaboration Keys
- Debug connection issues by checking URL format (missing +asyncpg)
- Configure for cloud databases with pool_recycle for idle timeout handling
- Structure environment-based configuration for dev/test/prod

### Common Mistakes
- Using sync drivers (`postgresql://`) with async engine
- Missing `pool_pre_ping` causes "connection closed" errors after idle
- Pool exhaustion from long-running transactions or leaked sessions
- Hardcoding credentials in source code

### Connections
- **Builds on**: L02 - Database design and normalization
- **Leads to**: L04 - Implementing data models
