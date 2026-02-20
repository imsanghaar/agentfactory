"""Caching utilities for token metering API.

Provides read-through caching for:
1. User balance - cached for fast balance checks
2. Pricing tables - cached since pricing changes are rare

Cache keys:
- metering:balance:{user_id} - User balance (TTL: 300s, invalidated on mutations)
- metering:pricing:{model} - Model pricing (TTL: 300s / 5 min)
"""

import json
import logging
from decimal import Decimal
from typing import Any

from redis.asyncio import Redis

logger = logging.getLogger(__name__)

# Cache TTLs
BALANCE_CACHE_TTL_SECONDS = 300  # 5 minutes - mutations invalidate immediately, TTL is safety net
PRICING_CACHE_TTL_SECONDS = 300  # 5 minutes - pricing changes are rare

# Cache key prefixes
BALANCE_KEY_PREFIX = "metering:balance:"
PRICING_KEY_PREFIX = "metering:pricing:"


async def get_cached_balance(redis: Redis | None, user_id: str) -> int | None:
    """Get balance from Redis cache.

    Args:
        redis: Redis client (or None if unavailable)
        user_id: User ID to look up

    Returns:
        Cached balance as int, or None on cache miss/unavailable
    """
    if redis is None:
        return None

    try:
        cached = await redis.get(f"{BALANCE_KEY_PREFIX}{user_id}")
        if cached is not None:
            return int(cached)
        return None
    except Exception as e:
        logger.warning(f"[Cache] Failed to get balance for {user_id}: {e}")
        return None


async def set_balance_cache(
    redis: Redis | None,
    user_id: str,
    balance: int,
    ttl: int = BALANCE_CACHE_TTL_SECONDS,
) -> None:
    """Cache balance with TTL.

    Args:
        redis: Redis client (or None if unavailable)
        user_id: User ID
        balance: Balance to cache
        ttl: Time-to-live in seconds (default: 60s)
    """
    if redis is None:
        return

    try:
        await redis.setex(f"{BALANCE_KEY_PREFIX}{user_id}", ttl, str(balance))
        logger.debug(f"[Cache] Cached balance for {user_id}: {balance}")
    except Exception as e:
        logger.warning(f"[Cache] Failed to cache balance for {user_id}: {e}")


async def invalidate_balance_cache(redis: Redis | None, user_id: str) -> None:
    """Invalidate cached balance data.

    Args:
        redis: Redis client (or None if unavailable)
        user_id: User ID to invalidate
    """
    if redis is None:
        return

    try:
        await redis.delete(f"{BALANCE_KEY_PREFIX}{user_id}")
        logger.debug(f"[Cache] Invalidated balance cache for {user_id}")
    except Exception as e:
        logger.warning(f"[Cache] Failed to invalidate balance for {user_id}: {e}")


async def get_cached_pricing(redis: Redis | None, model: str) -> dict[str, Any] | None:
    """Get pricing from Redis cache.

    Args:
        redis: Redis client (or None if unavailable)
        model: Model name to look up

    Returns:
        Cached pricing dict with Decimal values, or None on cache miss
    """
    if redis is None:
        return None

    try:
        cached = await redis.get(f"{PRICING_KEY_PREFIX}{model}")
        if cached is not None:
            data = json.loads(cached)
            # Convert string prices back to Decimal
            return {
                "input": Decimal(data["input"]),
                "output": Decimal(data["output"]),
                "version": data["version"],
            }
        return None
    except Exception as e:
        logger.warning(f"[Cache] Failed to get pricing for {model}: {e}")
        return None


async def set_pricing_cache(
    redis: Redis | None,
    model: str,
    pricing: dict[str, Any],
    ttl: int = PRICING_CACHE_TTL_SECONDS,
) -> None:
    """Cache pricing with TTL.

    Args:
        redis: Redis client (or None if unavailable)
        model: Model name
        pricing: Pricing dict with Decimal values
        ttl: Time-to-live in seconds (default: 300s / 5 min)
    """
    if redis is None:
        return

    try:
        # Convert Decimal to string for JSON serialization
        data = {
            "input": str(pricing["input"]),
            "output": str(pricing["output"]),
            "version": pricing.get("version", "v1"),
        }
        await redis.setex(f"{PRICING_KEY_PREFIX}{model}", ttl, json.dumps(data))
        logger.debug(f"[Cache] Cached pricing for {model}")
    except Exception as e:
        logger.warning(f"[Cache] Failed to cache pricing for {model}: {e}")
