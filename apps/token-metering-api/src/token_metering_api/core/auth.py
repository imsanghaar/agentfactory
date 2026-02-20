"""JWT authentication with JWKS support."""

import logging
from dataclasses import dataclass
from typing import Any

import httpx
from fastapi import Depends, HTTPException, Request
from jose import JWTError, jwt

from ..config import settings
from .exceptions import MeteringAPIException

logger = logging.getLogger(__name__)


def _check_dev_mode_safety() -> None:
    """Check if dev mode is safe to use.

    Raises HTTPException if dev_mode is enabled in production environment.
    Logs a warning when dev_mode is enabled in non-production.
    """
    if settings.dev_mode:
        if settings.environment == "production":
            logger.error(
                "[Auth] SECURITY VIOLATION: dev_mode=True in production environment! "
                "Blocking request. Set ENVIRONMENT to 'development' or disable DEV_MODE."
            )
            raise HTTPException(
                status_code=401,
                detail="Authentication required",
                headers={"WWW-Authenticate": "Bearer"},
            )
        logger.warning(
            "[Auth] WARNING: Dev mode is enabled. This should ONLY be used for local development!"
        )

# JWKS cache
_jwks_cache: dict[str, Any] | None = None
_jwks_cache_time: float = 0


@dataclass
class CurrentUser:
    """Represents the current authenticated user."""

    id: str
    email: str | None = None
    name: str | None = None
    roles: list[str] | None = None

    def __init__(self, payload: dict[str, Any]):
        self.id = payload.get("sub", "")
        self.email = payload.get("email")
        self.name = payload.get("name")
        self.roles = payload.get("roles", [])

    def has_role(self, role: str) -> bool:
        """Check if user has a specific role."""
        return self.roles is not None and role in self.roles

    @property
    def is_admin(self) -> bool:
        """Check if user has admin role."""
        return self.has_role("admin")


async def get_jwks() -> dict[str, Any]:
    """Fetch JWKS from SSO service with caching."""
    import time

    global _jwks_cache, _jwks_cache_time

    now = time.time()
    if _jwks_cache and (now - _jwks_cache_time) < settings.jwks_cache_ttl:
        return _jwks_cache

    if not settings.sso_url:
        raise HTTPException(status_code=500, detail="SSO_URL not configured")

    jwks_url = f"{settings.sso_url}/api/auth/jwks"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(jwks_url, timeout=5.0)
            response.raise_for_status()
            _jwks_cache = response.json()
            _jwks_cache_time = now
            return _jwks_cache
    except Exception as e:
        logger.error(f"[Auth] Failed to fetch JWKS: {e}")
        if _jwks_cache:
            return _jwks_cache
        raise HTTPException(status_code=503, detail="Unable to verify authentication")


async def verify_jwt(token: str) -> dict[str, Any]:
    """Verify JWT token using JWKS."""
    try:
        jwks = await get_jwks()
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")

        rsa_key = None
        for key in jwks.get("keys", []):
            if key.get("kid") == kid:
                rsa_key = key
                break

        if not rsa_key:
            raise HTTPException(
                status_code=401,
                detail="Unable to find appropriate key",
                headers={"WWW-Authenticate": "Bearer"},
            )

        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=["RS256"],
            audience=settings.token_audience,
            options={"verify_aud": True},  # CRIT-002: Always verify audience
        )
        return payload

    except JWTError as e:
        logger.warning(f"[Auth] JWT verification failed: {e}")
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_user(request: Request) -> CurrentUser:
    """Dependency to get current authenticated user."""
    if settings.dev_mode:
        # CRIT-001: Check dev mode is not enabled in production
        _check_dev_mode_safety()

        # Dev mode: use X-User-ID header or fallback
        user_id = request.headers.get("X-User-ID") or settings.dev_user_id

        # CRIT-001 FIX: Dev mode does NOT automatically grant admin role
        # Admin role requires explicit X-Dev-Admin: true header
        roles: list[str] = []
        if request.headers.get("X-Dev-Admin", "").lower() == "true":
            roles = ["admin"]
            logger.debug(f"[Auth] Dev mode: granting admin role to {user_id}")

        return CurrentUser({"sub": user_id, "roles": roles})

    # Production: verify JWT
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization header",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = auth_header[7:]

    if token.count(".") != 2:
        raise HTTPException(
            status_code=401,
            detail="Invalid token format",
            headers={"WWW-Authenticate": "Bearer"},
        )

    payload = await verify_jwt(token)
    return CurrentUser(payload)


async def require_admin(user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
    """Dependency to require admin role."""
    if not user.is_admin:
        raise MeteringAPIException(
            status_code=403,
            error_code="FORBIDDEN",
            message="Admin role required",
        )
    return user
