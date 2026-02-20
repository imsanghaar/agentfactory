"""Database connection management using SQLModel."""

import logging
import ssl
from collections.abc import AsyncGenerator
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import AsyncAdaptedQueuePool

from ..config import settings

logger = logging.getLogger(__name__)


def _prepare_asyncpg_url(url: str) -> tuple[str, dict]:
    """Convert psycopg2-style URL to asyncpg-compatible URL.

    asyncpg doesn't understand 'sslmode' - it uses 'ssl' instead.
    This function extracts sslmode and returns the cleaned URL
    plus any necessary connect_args.
    """
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    connect_args: dict = {}

    # Handle sslmode -> ssl conversion for asyncpg
    if "sslmode" in query_params:
        sslmode = query_params.pop("sslmode")[0]
        if sslmode in ("require", "verify-ca", "verify-full"):
            # Create SSL context for asyncpg
            ssl_context = ssl.create_default_context()
            if sslmode == "require":
                # Don't verify certificate for 'require' mode
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE
            connect_args["ssl"] = ssl_context
        # 'disable' and 'prefer' don't need ssl arg

    # Rebuild URL without sslmode
    new_query = urlencode(query_params, doseq=True)
    new_parsed = parsed._replace(query=new_query)
    clean_url = urlunparse(new_parsed)

    return clean_url, connect_args


# Prepare URL for asyncpg
_db_url, _connect_args = _prepare_asyncpg_url(settings.database_url)

# Create async engine with connection pooling
engine = create_async_engine(
    _db_url,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=100,      # Production: 100 base connections
    max_overflow=50,    # Production: 50 burst connections (150 total max)
    pool_pre_ping=True,
    echo=settings.debug,
    connect_args=_connect_args,
)

# Session factory
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting database sessions."""
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db() -> None:
    """Initialize database schema."""
    from ..models import SQLModel

    async with engine.begin() as conn:
        # Create metering schema if it doesn't exist (PostgreSQL only)
        try:
            await conn.execute(text("CREATE SCHEMA IF NOT EXISTS metering"))
        except Exception:
            # Schema creation may fail on SQLite (used for tests)
            pass
        await conn.run_sync(SQLModel.metadata.create_all)

    logger.info("[DB] Schema initialized")


async def close_db() -> None:
    """Close database connections."""
    await engine.dispose()
    logger.info("[DB] Connections closed")
