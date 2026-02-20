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
    """
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    connect_args: dict = {}

    if "sslmode" in query_params:
        sslmode = query_params.pop("sslmode")[0]
        if sslmode in ("require", "verify-ca", "verify-full"):
            ssl_context = ssl.create_default_context()
            if sslmode == "require":
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE
            connect_args["ssl"] = ssl_context

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
    pool_size=100,
    max_overflow=70,
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
    """Initialize database schema using create_all."""
    from ..models import SQLModel

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    logger.info("[DB] Schema initialized")


async def create_materialized_views() -> None:
    """Create materialized views via raw SQL (create_all doesn't handle views)."""
    async with engine.begin() as conn:
        await conn.execute(
            text("""
                CREATE MATERIALIZED VIEW IF NOT EXISTS leaderboard AS
                SELECT u.id, u.display_name, u.avatar_url, p.total_xp,
                       RANK() OVER (ORDER BY p.total_xp DESC) AS rank,
                       p.badge_count
                FROM users u JOIN user_progress p ON u.id = p.user_id
                WHERE u.show_on_leaderboard = TRUE AND p.total_xp > 0
                ORDER BY p.total_xp DESC
            """)
        )
        await conn.execute(
            text("CREATE UNIQUE INDEX IF NOT EXISTS idx_leaderboard_id ON leaderboard(id)")
        )

    logger.info("[DB] Materialized views created")


async def close_db() -> None:
    """Close database connections."""
    await engine.dispose()
    logger.info("[DB] Connections closed")
