"""Test fixtures for progress API using PostgreSQL testcontainers."""

import asyncio
from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from progress_api.config import settings
from progress_api.main import app
from progress_api.models import SQLModel


def _docker_available() -> bool:
    """Check if Docker daemon is reachable."""
    try:
        import docker

        docker.from_env().ping()
        return True
    except Exception:
        return False


requires_docker = pytest.mark.skipif(not _docker_available(), reason="Docker is not available")


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def postgres_url():
    """Start a PostgreSQL container and return the connection URL.

    Uses testcontainers to spin up a real PostgreSQL instance.
    """
    if not _docker_available():
        pytest.skip("Docker is not available")

    from testcontainers.postgres import PostgresContainer

    with PostgresContainer("postgres:16-alpine") as postgres:
        # testcontainers returns a psycopg2-style URL; convert to asyncpg
        url = postgres.get_connection_url()
        async_url = url.replace("psycopg2", "asyncpg")
        yield async_url


@pytest_asyncio.fixture(scope="function")
async def test_engine(postgres_url: str):
    """Create test database engine and tables for each test."""
    engine = create_async_engine(
        postgres_url,
        echo=False,
    )

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    # Create materialized view
    async with engine.begin() as conn:
        # Drop the view first to ensure clean state per test
        await conn.execute(text("DROP MATERIALIZED VIEW IF EXISTS leaderboard"))
        await conn.execute(
            text("""
                CREATE MATERIALIZED VIEW leaderboard AS
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

    yield engine

    # Clean up tables after each test
    async with engine.begin() as conn:
        await conn.execute(text("DROP MATERIALIZED VIEW IF EXISTS leaderboard"))
        await conn.run_sync(SQLModel.metadata.drop_all)

    await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def test_session(test_engine) -> AsyncGenerator[AsyncSession, None]:
    """Create test database session."""
    session_factory = async_sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with session_factory() as session:
        yield session


@pytest_asyncio.fixture(scope="function")
async def client(test_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """Create test HTTP client with dependency overrides."""
    from progress_api.core.database import get_session

    async def override_get_session():
        yield test_session

    app.dependency_overrides[get_session] = override_get_session

    # Enable dev mode for tests
    original_dev_mode = settings.dev_mode
    settings.dev_mode = True

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    settings.dev_mode = original_dev_mode
    app.dependency_overrides.clear()
