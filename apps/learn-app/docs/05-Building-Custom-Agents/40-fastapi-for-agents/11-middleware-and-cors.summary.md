### Core Concept
Middleware intercepts every request/response at the "door" of your API. CORS allows cross-origin requests from frontends on different domains/ports. Custom middleware adds timing headers, logging. `call_next(request)` passes to route, code after handles response.

### Key Mental Models
- **Single door**: Write logic once, applies to ALL endpoints
- **Stack execution**: Last added middleware is outermost (first in, last out)
- **Origin = protocol + domain + port**: `http://localhost:3000` differs from `:8000`
- **CORS preflight**: Browser sends OPTIONS before actual request

### Critical Patterns
- Timing middleware: `start = time.perf_counter()`, `await call_next(request)`, add header
- Logging: `logger.info(f"{request.method} {request.url.path}")` before and after
- CORS setup: `app.add_middleware(CORSMiddleware, allow_origins=[...], allow_credentials=True)`
- Execution order: Last added = outermost; CORS added first becomes innermost
- Expose headers: `expose_headers=["X-Process-Time"]` for client access

### AI Collaboration Keys
- Prompt 1: Error handling middleware—catch exceptions, return consistent JSON
- Prompt 2: Rate limit headers—add X-RateLimit-Remaining via middleware
- Prompt 3: Request ID tracing—UUID for distributed tracing

### Common Mistakes
- Forgetting `await call_next(request)` (blocks forever)
- Using credentials with wildcard origin (`["*"]` incompatible with `allow_credentials=True`)
- Not returning the response (returns None)
- Wrong middleware order for dependencies

### Connections
- **Builds on**: Dependency Injection (Lesson 10)
- **Leads to**: Lifespan Events (Lesson 12)
