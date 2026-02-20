"""Caching utilities for progress API.

Provides caching for:
1. User progress data (TTL: configurable, default 300s)
2. Leaderboard data (TTL: configurable, default 300s)

Cache keys:
- progress:user:{user_id} - User progress (invalidated on mutations)
- progress:leaderboard - Leaderboard data (invalidated on refresh)

Fail-open: if redis is None, all operations skip silently (A3).
"""

import json
import logging
from typing import Any

from redis.asyncio import Redis

from ..config import settings

logger = logging.getLogger(__name__)

# Cache key prefixes
PROGRESS_KEY_PREFIX = "progress:user:"
LEADERBOARD_KEY = "progress:leaderboard"


async def get_cached_progress(redis: Redis | None, user_id: str) -> dict[str, Any] | None:
    """Get user progress from Redis cache."""
    if redis is None:
        return None

    try:
        cached = await redis.get(f"{PROGRESS_KEY_PREFIX}{user_id}")
        if cached is not None:
            return json.loads(cached)
        return None
    except Exception as e:
        logger.warning(f"[Cache] Failed to get progress for {user_id}: {e}")
        return None


async def set_progress_cache(
    redis: Redis | None,
    user_id: str,
    data: dict[str, Any],
    ttl: int | None = None,
) -> None:
    """Cache user progress with TTL."""
    if redis is None:
        return

    if ttl is None:
        ttl = settings.cache_ttl_progress

    try:
        await redis.setex(f"{PROGRESS_KEY_PREFIX}{user_id}", ttl, json.dumps(data))
    except Exception as e:
        logger.warning(f"[Cache] Failed to cache progress for {user_id}: {e}")


async def invalidate_progress_cache(redis: Redis | None, user_id: str) -> None:
    """Invalidate cached progress data for a user."""
    if redis is None:
        return

    try:
        await redis.delete(f"{PROGRESS_KEY_PREFIX}{user_id}")
    except Exception as e:
        logger.warning(f"[Cache] Failed to invalidate progress for {user_id}: {e}")


async def get_cached_leaderboard(redis: Redis | None) -> list[dict[str, Any]] | None:
    """Get leaderboard from Redis cache."""
    if redis is None:
        return None

    try:
        cached = await redis.get(LEADERBOARD_KEY)
        if cached is not None:
            return json.loads(cached)
        return None
    except Exception as e:
        logger.warning(f"[Cache] Failed to get leaderboard: {e}")
        return None


async def set_leaderboard_cache(
    redis: Redis | None,
    data: list[dict[str, Any]],
    ttl: int | None = None,
) -> None:
    """Cache leaderboard data with TTL."""
    if redis is None:
        return

    if ttl is None:
        ttl = settings.cache_ttl_leaderboard

    try:
        await redis.setex(LEADERBOARD_KEY, ttl, json.dumps(data))
    except Exception as e:
        logger.warning(f"[Cache] Failed to cache leaderboard: {e}")


async def invalidate_leaderboard_cache(redis: Redis | None) -> None:
    """Invalidate cached leaderboard data."""
    if redis is None:
        return

    try:
        await redis.delete(LEADERBOARD_KEY)
    except Exception as e:
        logger.warning(f"[Cache] Failed to invalidate leaderboard: {e}")
