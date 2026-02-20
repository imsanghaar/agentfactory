"""Application lifespan management for startup and shutdown."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import close_db, init_db
from .redis import get_redis, start_redis, stop_redis

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan context manager.

    Handles:
    - Redis connection initialization with Lua scripts
    - PostgreSQL connection pool initialization
    - Database schema setup
    - Graceful shutdown
    """
    try:
        logger.info("=" * 60)
        logger.info("TOKEN METERING API - STARTUP")
        logger.info("=" * 60)

        # Initialize Redis (critical for metering)
        logger.info("[INIT] Initializing Redis...")
        await start_redis()

        redis_client = get_redis()
        if redis_client:
            logger.info("[INIT] Redis connected - metering enabled")
        else:
            logger.warning("[INIT] Redis NOT available - fail-open mode active")

        # Initialize Database
        logger.info("[INIT] Initializing Database...")
        try:
            await init_db()
            logger.info("[INIT] Database initialized")
        except Exception as e:
            logger.error(f"[INIT] Database initialization failed: {e}")
            raise

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
