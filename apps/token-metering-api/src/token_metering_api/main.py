"""
Token Metering API v6 - Cost-weighted credits metering service.

Features:
- Pre-request balance checks with reservation pattern (<5ms)
- Cost-weighted credit deductions (1 credit = $0.0001)
- Administrative credits management (grant, topup, tier)
- Single unified credits balance system
- JWT/JWKS authentication with dev mode bypass
"""

import logging

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Request  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402
from fastapi.responses import JSONResponse  # noqa: E402
from slowapi.errors import RateLimitExceeded  # noqa: E402

from .config import settings  # noqa: E402
from .core.exceptions import MeteringAPIException  # noqa: E402
from .core.lifespan import lifespan  # noqa: E402
from .core.rate_limit import limiter, rate_limit_exceeded_handler  # noqa: E402
from .routes import admin, balance, health, metering, metrics  # noqa: E402

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Security warning for dev mode
if settings.dev_mode:
    if settings.environment == "production":
        logger.critical(
            "SECURITY VIOLATION: dev_mode=True in production! "
            "This is a critical misconfiguration. Set DEV_MODE=false or ENVIRONMENT=development"
        )
    else:
        logger.warning(
            "WARNING: Dev mode is enabled. Authentication is bypassed. "
            "This should ONLY be used for local development!"
        )

# Create FastAPI app with lifespan
app = FastAPI(
    title="Token Metering API",
    description="Freemium token tracking and metering service for the Agent Factory platform",
    version="6.0.0",
    lifespan=lifespan,
)


# === Custom Exception Handler ===


@app.exception_handler(MeteringAPIException)
async def metering_exception_handler(
    request: Request, exc: MeteringAPIException
) -> JSONResponse:
    """Handle MeteringAPIException with consistent error format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": exc.error_code,
            "message": exc.message,
            **exc.extra,
        },
    )

# HIGH-001: Add rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["Health"])
app.include_router(metrics.router, tags=["Metrics"])
app.include_router(metering.router, prefix="/api/v1/metering", tags=["Metering"])
app.include_router(balance.router, prefix="/api/v1", tags=["Balance"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Token Metering API",
        "version": "6.0.0",
        "endpoints": {
            "metering": {
                "check": "POST /api/v1/metering/check",
                "deduct": "POST /api/v1/metering/deduct",
                "release": "POST /api/v1/metering/release",
            },
            "balance": {
                "get": "GET /api/v1/balance",
                "transactions": "GET /api/v1/transactions",
            },
            "admin": {
                "grant": "POST /api/v1/admin/grant",
                "topup": "POST /api/v1/admin/topup",
                "tier": "PATCH /api/v1/admin/tier",
            },
            "health": "GET /health",
            "metrics": "GET /metrics",
        },
    }


if __name__ == "__main__":
    import uvicorn

    port = settings.port
    logger.info("\n=== Token Metering API v6.0 ===")
    logger.info(f"Dev Mode: {settings.dev_mode}")
    logger.info(f"Fail Open: {settings.fail_open}")
    logger.info(f"API: http://localhost:{port}")
    logger.info(f"Health: http://localhost:{port}/health\n")

    uvicorn.run(app, host="0.0.0.0", port=port)
