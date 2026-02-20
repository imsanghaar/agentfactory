"""Redis connection management with Lua script support."""

import logging
from pathlib import Path
from typing import TYPE_CHECKING

import redis.asyncio
import redis.asyncio.retry
import redis.backoff
import redis.exceptions

from ..config import settings

if TYPE_CHECKING:
    from redis.commands.core import AsyncScript

logger = logging.getLogger(__name__)

_redis: redis.asyncio.Redis | None = None
_lua_scripts: dict[str, "AsyncScript"] = {}

# Directory containing Lua scripts
SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"


async def start_redis() -> None:
    """Initialize Redis connection with retry and exponential backoff."""
    global _redis

    if not settings.redis_url or settings.redis_url.strip() == "":
        logger.warning("[Redis] REDIS_URL not provided - metering will fail-open")
        return

    # Log connection attempt (mask password)
    url_parts = settings.redis_url.split("@")
    if len(url_parts) > 1:
        safe_url = f"redis://***@{url_parts[-1]}"
    else:
        safe_url = "redis://***"
    logger.info(f"[Redis] Connecting to: {safe_url}")

    try:
        _redis = redis.asyncio.Redis.from_url(
            settings.redis_url,
            password=settings.redis_password if settings.redis_password else None,
            decode_responses=False,  # Keep bytes for Lua scripts
            max_connections=settings.redis_max_connections,
            retry=redis.asyncio.retry.Retry(
                backoff=redis.backoff.ExponentialBackoff(),
                retries=5,
            ),
            retry_on_error=[
                redis.exceptions.ConnectionError,
                redis.exceptions.TimeoutError,
                redis.exceptions.ReadOnlyError,
            ],
        )
        await _redis.ping()
        logger.info("[Redis] Connected successfully!")

        # Load Lua scripts
        await _load_lua_scripts()

    except redis.exceptions.ConnectionError as e:
        logger.error(f"[Redis] Connection FAILED: {e}")
        _redis = None
    except redis.exceptions.AuthenticationError as e:
        logger.error(f"[Redis] Authentication FAILED: {e}")
        _redis = None
    except Exception as e:
        logger.error(f"[Redis] Unexpected error: {e}")
        _redis = None


async def _load_lua_scripts() -> None:
    """Load and register Lua scripts with Redis."""
    global _lua_scripts

    if not _redis:
        return

    script_files = ["reserve.lua", "finalize.lua", "release.lua"]

    for script_file in script_files:
        script_path = SCRIPTS_DIR / script_file
        if script_path.exists():
            script_content = script_path.read_text()
            script_name = script_file.replace(".lua", "")
            _lua_scripts[script_name] = _redis.register_script(script_content)
            logger.info(f"[Redis] Loaded Lua script: {script_name}")
        else:
            logger.warning(f"[Redis] Lua script not found: {script_path}")


async def stop_redis() -> None:
    """Close Redis connection."""
    global _redis, _lua_scripts

    if _redis:
        await _redis.aclose()
        logger.info("[Redis] Connection closed")
        _redis = None
        _lua_scripts = {}


def get_redis() -> redis.asyncio.Redis | None:
    """Get Redis client instance, returns None if not initialized."""
    return _redis


def get_lua_script(name: str) -> "AsyncScript | None":
    """Get a registered Lua script by name."""
    return _lua_scripts.get(name)
