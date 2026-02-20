### Core Concept
Lifespan events run code at startup (before first request) and shutdown (after last response). `@asynccontextmanager` with yield separates phases: before yield = startup, after yield = cleanup. Preload database pools, ML models, HTTP clients—no cold-start delays.

### Key Mental Models
- **Restaurant metaphor**: Prep kitchen before customers (startup), clean after they leave (shutdown)
- **Yield is the divider**: Everything before runs once at startup, everything after runs at shutdown
- **app.state for sharing**: Resources stored in `app.state`, accessed via `request.app.state`
- **Graceful cleanup**: Code after yield runs even on shutdown signal

### Critical Patterns
- Lifespan function: `@asynccontextmanager async def lifespan(app: FastAPI):`
- Pass to app: `app = FastAPI(lifespan=lifespan)`
- Share state: `app.state.async_session = async_sessionmaker(...)`
- Access in endpoint: `request.app.state.embedder.encode(text)`
- Cleanup: `await engine.dispose()` after yield

### AI Collaboration Keys
- Prompt 1: Health checks—return database/cache status from app.state
- Prompt 2: Graceful shutdown—finish pending requests with timeout
- Prompt 3: Conditional loading—skip ML model in tests for speed

### Common Mistakes
- Forgetting to yield (server never starts)
- Not passing lifespan to FastAPI() (lifespan never runs)
- Accessing app.state without request object
- Using deprecated `@app.on_event("startup")` instead of lifespan

### Connections
- **Builds on**: Middleware & CORS (Lesson 11)
- **Leads to**: Streaming with SSE (Lesson 13)
