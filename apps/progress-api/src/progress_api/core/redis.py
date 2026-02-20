"""Redis connection management."""

import logging

import redis.asyncio
import redis.asyncio.retry
import redis.backoff
import redis.exceptions

from ..config import settings

logger = logging.getLogger(__name__)

_redis: redis.asyncio.Redis | None = None


async def start_redis() -> None:
    """Initialize Redis connection with retry and exponential backoff."""
    global _redis

    if not settings.redis_url or settings.redis_url.strip() == "":
        logger.warning("[Redis] REDIS_URL not provided - cache will be skipped")
        return

    try:
        _redis = redis.asyncio.Redis.from_url(
            settings.redis_url,
            password=settings.redis_password if settings.redis_password else None,
            decode_responses=True,
            retry=redis.asyncio.retry.Retry(
                backoff=redis.backoff.ExponentialBackoff(),
                retries=5,
            ),
            retry_on_error=[
                redis.exceptions.ConnectionError,
                redis.exceptions.TimeoutError,
            ],
        )
        await _redis.ping()
        logger.info("[Redis] Connected successfully!")

    except redis.exceptions.ConnectionError as e:
        logger.error(f"[Redis] Connection FAILED: {e}")
        _redis = None
    except redis.exceptions.AuthenticationError as e:
        logger.error(f"[Redis] Authentication FAILED: {e}")
        _redis = None
    except Exception as e:
        logger.error(f"[Redis] Unexpected error: {e}")
        _redis = None


async def stop_redis() -> None:
    """Close Redis connection."""
    global _redis

    if _redis:
        await _redis.aclose()
        logger.info("[Redis] Connection closed")
        _redis = None


def get_redis() -> redis.asyncio.Redis | None:
    """Get Redis client instance, returns None if not initialized."""
    return _redis
