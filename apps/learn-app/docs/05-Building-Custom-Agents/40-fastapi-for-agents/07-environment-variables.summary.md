### Core Concept
Configuration lives outside code via environment variables. pydantic-settings provides type-safe configuration: automatic type conversion, validation at startup, documented requirements. `.env` files for local development, `.gitignore` to protect secrets, `@lru_cache` for efficiency.

### Key Mental Models
- **Secrets never in code**: `DATABASE_URL` in `.env`, not hardcoded—enables rotation without redeployment
- **Fail fast validation**: Missing variables error at startup, not mid-request
- **Type conversion**: `"30"` becomes `30`, `"true"` becomes `True` automatically
- **Dependency injection**: `Settings = Depends(get_settings)` provides config to endpoints

### Critical Patterns
- BaseSettings class: `class Settings(BaseSettings):` with `class Config: env_file = ".env"`
- Cache settings: `@lru_cache` on `get_settings()` reads file once
- Gitignore pattern: `.env` excluded, `.env.example` committed for documentation
- Inject via Depends: `def endpoint(settings: Settings = Depends(get_settings))`

### AI Collaboration Keys
- Prompt 1: Environment-specific settings—multiple .env files vs conditional logic
- Prompt 2: Validate formats—enforce PostgreSQL URL patterns with validators
- Prompt 3: Production secrets—Railway/Fly.io secrets management

### Common Mistakes
- Committing `.env` with real secrets (use `git rm --cached .env`)
- Wrong variable names (pydantic expects `DATABASE_URL` for `database_url`)
- Forgetting `class Config` (won't read from `.env`)
- Not caching settings (reads file on every call)

### Connections
- **Builds on**: Error Handling (Lesson 5)
- **Leads to**: SQLModel + Neon Setup (Lesson 7)
