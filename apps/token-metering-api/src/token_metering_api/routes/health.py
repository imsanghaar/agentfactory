"""Health check endpoint."""

import logging

from fastapi import APIRouter
from sqlalchemy import text

from ..core.database import async_session
from ..core.redis import get_redis

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint with database and Redis status."""
    status = {
        "status": "healthy",
        "version": "6.0.0",
        "services": {},
    }

    # Check PostgreSQL
    try:
        async with async_session() as session:
            await session.execute(text("SELECT 1"))
        status["services"]["database"] = "connected"
    except Exception as e:
        logger.error(f"[Health] Database check failed: {e}")
        status["services"]["database"] = "disconnected"
        status["status"] = "degraded"

    # Check Redis
    redis_client = get_redis()
    if redis_client:
        try:
            await redis_client.ping()
            status["services"]["redis"] = "connected"
        except Exception as e:
            logger.error(f"[Health] Redis check failed: {e}")
            status["services"]["redis"] = "disconnected"
            status["status"] = "degraded"
    else:
        status["services"]["redis"] = "disconnected"
        status["status"] = "degraded"

    return status
