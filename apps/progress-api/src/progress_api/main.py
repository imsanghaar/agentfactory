"""Progress API — Gamification and progress tracking service."""

import logging
import traceback

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Request  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402
from fastapi.responses import JSONResponse  # noqa: E402

from .config import settings  # noqa: E402
from .core.exceptions import ProgressAPIException  # noqa: E402
from .core.lifespan import lifespan  # noqa: E402
from .routes import health, leaderboard, lesson, preferences, progress, quiz  # noqa: E402

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
            "Set DEV_MODE=false or ENVIRONMENT=development"
        )
    else:
        logger.warning(
            "WARNING: Dev mode is enabled. Authentication is bypassed. "
            "This should ONLY be used for local development!"
        )

# Create FastAPI app with lifespan
app = FastAPI(
    title="Progress API",
    description="Gamification and progress tracking service for the Agent Factory platform",
    version="1.0.0",
    lifespan=lifespan,
)


# === Custom Exception Handler ===


@app.exception_handler(ProgressAPIException)
async def progress_exception_handler(request: Request, exc: ProgressAPIException) -> JSONResponse:
    """Handle ProgressAPIException with consistent error format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": exc.error_code,
            "message": exc.message,
            **exc.extra,
        },
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Catch-all for unhandled exceptions — logs traceback, returns CORS-safe 500."""
    logger.error(
        "Unhandled exception on %s %s:\n%s",
        request.method,
        request.url.path,
        traceback.format_exc(),
    )
    return JSONResponse(
        status_code=500,
        content={
            "error_code": "INTERNAL_ERROR",
            "message": "An unexpected error occurred.",
        },
    )


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
app.include_router(quiz.router, prefix="/api/v1", tags=["Quiz"])
app.include_router(lesson.router, prefix="/api/v1", tags=["Lesson"])
app.include_router(progress.router, prefix="/api/v1", tags=["Progress"])
app.include_router(leaderboard.router, prefix="/api/v1", tags=["Leaderboard"])
app.include_router(preferences.router, prefix="/api/v1", tags=["Preferences"])


if __name__ == "__main__":
    import uvicorn

    port = settings.port
    logger.info("\n=== Progress API v1.0 ===")
    logger.info(f"Dev Mode: {settings.dev_mode}")
    logger.info(f"API: http://localhost:{port}")
    logger.info(f"Health: http://localhost:{port}/health\n")

    uvicorn.run(app, host="0.0.0.0", port=port)
