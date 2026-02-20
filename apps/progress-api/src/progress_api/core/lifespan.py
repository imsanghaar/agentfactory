"""Application lifespan management for startup and shutdown."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import close_db, create_materialized_views, init_db
from .redis import get_redis, start_redis, stop_redis

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager.

    Handles:
    - Redis connection initialization
    - PostgreSQL connection pool initialization
    - Database schema setup
    - Materialized view creation
    - Graceful shutdown
    """
    try:
        logger.info("=" * 60)
        logger.info("PROGRESS API - STARTUP")
        logger.info("=" * 60)

        # Initialize Redis (optional - fail-open)
        logger.info("[INIT] Initializing Redis...")
        await start_redis()

        redis_client = get_redis()
        if redis_client:
            logger.info("[INIT] Redis connected - caching enabled")
        else:
            logger.warning("[INIT] Redis NOT available - caching disabled")

        # Initialize Database
        logger.info("[INIT] Initializing Database...")
        try:
            await init_db()
            logger.info("[INIT] Database initialized")
        except Exception as e:
            logger.error(f"[INIT] Database initialization failed: {e}")
            raise

        # Create materialized views
        try:
            await create_materialized_views()
            logger.info("[INIT] Materialized views created")
        except Exception as e:
            logger.warning(f"[INIT] Materialized view creation failed (may already exist): {e}")

        # Refresh materialized view on startup so it reflects current data
        try:
            from ..services.leaderboard import refresh_leaderboard
            from .database import async_session

            async with async_session() as session:
                await refresh_leaderboard(session)
            logger.info("[INIT] Leaderboard view refreshed")
        except Exception as e:
            logger.warning(f"[INIT] Leaderboard refresh on startup failed: {e}")

        logger.info("=" * 60)
        logger.info("STARTUP COMPLETE")
        logger.info("=" * 60)

        yield

    finally:
        logger.info("=" * 60)
        logger.info("SHUTDOWN")
        logger.info("=" * 60)

        await stop_redis()
        await close_db()

        logger.info("Shutdown complete")
