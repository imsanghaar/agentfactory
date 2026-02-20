### Core Concept
Cloud persistence requires secure credential handling, connection pooling, and health checks.

### Continuity Bridge
From local transaction safety (L5) to cloud persistence that survives machine restarts.

### Key Mental Models
- DATABASE_URL in .env, .env in .gitignore -- never in source code.
- Connection pool reuses connections instead of creating new ones per query.
- pool_pre_ping catches stale connections before your query fails.
- pool_recycle=3600 prevents Neon from dropping idle connections.

### Critical Patterns
- 4-step secret management: .env file, .gitignore, python-dotenv, os.getenv().
- QueuePool with pool_pre_ping=True and pool_recycle=3600.
- SELECT 1 health check before trusting the connection.
- Deterministic error triage: work through causes in order, not random guessing.

### Common Mistake
Hardcoding DATABASE_URL in source code. Also: random troubleshooting instead of sequential diagnostics tied to exact error text.
