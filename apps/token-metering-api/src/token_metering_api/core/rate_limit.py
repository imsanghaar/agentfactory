"""Rate limiting for the Token Metering API (HIGH-001)."""

import logging
import os
from collections.abc import Callable

from fastapi import Request, Response
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.responses import JSONResponse

from ..config import settings

logger = logging.getLogger(__name__)


def get_user_identifier(request: Request) -> str:
    """Get user identifier for rate limiting.

    Uses X-User-ID header if available (for authenticated requests),
    otherwise falls back to IP address.
    """
    user_id = request.headers.get("X-User-ID")
    if user_id:
        return f"user:{user_id}"
    return f"ip:{get_remote_address(request)}"


def _get_storage_uri() -> str:
    """Get storage URI for rate limiting.

    Uses in-memory storage for tests (when pytest is running),
    Redis if configured, otherwise falls back to in-memory storage.
    slowapi uses a sync Redis client, so we must embed the password
    in the URL (unlike the async client which accepts it separately).
    """
    # Check if we're running in a test environment
    if "PYTEST_CURRENT_TEST" in os.environ:
        return "memory://"

    if settings.redis_url:
        url = settings.redis_url
        # Inject password into URL for slowapi's sync Redis client
        if settings.redis_password and "@" not in url:
            # rediss://host:port → rediss://:password@host:port
            scheme_end = url.index("://") + 3
            url = f"{url[:scheme_end]}:{settings.redis_password}@{url[scheme_end:]}"
        return url

    # Use in-memory storage when Redis is not configured
    return "memory://"


# Create limiter with user-based key function
limiter = Limiter(
    key_func=get_user_identifier,
    default_limits=[f"{settings.rate_limit_requests}/minute"],
    storage_uri=_get_storage_uri(),
)


def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded) -> Response:
    """Handle rate limit exceeded errors."""
    logger.warning(
        f"[RateLimit] Rate limit exceeded for {get_user_identifier(request)}: {exc.detail}"
    )
    return JSONResponse(
        status_code=429,
        content={
            "error_code": "RATE_LIMIT_EXCEEDED",
            "message": "Too many requests. Please try again later.",
            "detail": str(exc.detail),
        },
    )


def get_standard_limit() -> str:
    """Get standard rate limit string."""
    return f"{settings.rate_limit_requests}/{settings.rate_limit_window} seconds"


def get_admin_limit() -> str:
    """Get admin rate limit string (stricter)."""
    return f"{settings.admin_rate_limit_requests}/{settings.rate_limit_window} seconds"


# Decorators for different endpoint types
def standard_rate_limit() -> Callable:
    """Apply standard rate limit to an endpoint."""
    return limiter.limit(get_standard_limit())


def admin_rate_limit() -> Callable:
    """Apply stricter admin rate limit to an endpoint."""
    return limiter.limit(get_admin_limit())
