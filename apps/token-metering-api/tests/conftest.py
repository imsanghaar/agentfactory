"""Test fixtures for token metering API (v6 - Credits)."""

import asyncio
import hashlib
import os
import uuid
from collections.abc import AsyncGenerator
from datetime import UTC, datetime, timedelta

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import StaticPool

# Set environment variable BEFORE importing app modules to ensure rate limiting uses memory storage
os.environ["PYTEST_CURRENT_TEST"] = "1"

from token_metering_api.config import settings
from token_metering_api.main import app
from token_metering_api.models import STARTER_CREDITS, SQLModel


def make_request_id(seed: str = "") -> str:
    """Generate a deterministic UUID from a seed string for reproducible tests.

    Usage:
        request_id = make_request_id("test-001")  # Always returns same UUID
        request_id = make_request_id()  # Random UUID
    """
    if seed:
        # Create deterministic UUID from seed using MD5 hash
        hash_bytes = hashlib.md5(seed.encode()).digest()
        return str(uuid.UUID(bytes=hash_bytes))
    return str(uuid.uuid4())

# Use in-memory SQLite for tests
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def test_engine():
    """Create test database engine."""
    engine = create_async_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=False,
    )

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    yield engine

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

    await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def test_session(test_engine) -> AsyncGenerator[AsyncSession, None]:
    """Create test database session."""
    async_session = async_sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session


@pytest_asyncio.fixture(scope="function")
async def client(test_session) -> AsyncGenerator[AsyncClient, None]:
    """Create test HTTP client with dependency overrides."""
    from token_metering_api.core.database import get_session

    async def override_get_session():
        yield test_session

    app.dependency_overrides[get_session] = override_get_session

    # Enable dev mode for tests
    original_dev_mode = settings.dev_mode
    settings.dev_mode = True

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

    settings.dev_mode = original_dev_mode
    app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def new_user(test_session: AsyncSession):
    """Create a new user with starter credits (v6).

    v6: New users start with STARTER_CREDITS (20,000).
    """
    from token_metering_api.models import AllocationType, TokenAccount, TokenAllocation

    account = TokenAccount(
        user_id="new-user-123",
        balance=STARTER_CREDITS,
        last_activity_at=datetime.now(UTC),
    )
    test_session.add(account)

    # Create starter allocation audit record
    allocation = TokenAllocation(
        user_id="new-user-123",
        allocation_type=AllocationType.STARTER,
        amount=STARTER_CREDITS,
        reason="Initial starter credits for new user",
    )
    test_session.add(allocation)

    await test_session.commit()
    await test_session.refresh(account)
    return account


@pytest_asyncio.fixture
async def user_with_balance(test_session: AsyncSession):
    """Create a user with 500k balance (has been granted credits)."""
    from token_metering_api.models import AllocationType, TokenAccount, TokenAllocation

    account = TokenAccount(
        user_id="balance-user-456",
        balance=500000,
        last_activity_at=datetime.now(UTC),
    )
    test_session.add(account)
    await test_session.commit()

    # Create audit record
    allocation = TokenAllocation(
        user_id="balance-user-456",
        allocation_type=AllocationType.GRANT,
        amount=500000,
        reason="Test grant",
    )
    test_session.add(allocation)
    await test_session.commit()

    await test_session.refresh(account)
    return account


@pytest_asyncio.fixture
async def zero_balance_user(test_session: AsyncSession):
    """Create a user who has exhausted all credits."""
    from token_metering_api.models import TokenAccount

    account = TokenAccount(
        user_id="zero-balance-789",
        balance=0,
        last_activity_at=datetime.now(UTC),
    )
    test_session.add(account)
    await test_session.commit()
    await test_session.refresh(account)
    return account


@pytest_asyncio.fixture
async def suspended_user(test_session: AsyncSession):
    """Create a suspended user account."""
    from token_metering_api.models import AccountStatus, TokenAccount

    account = TokenAccount(
        user_id="suspended-user-999",
        balance=10000,
        status=AccountStatus.SUSPENDED,
        last_activity_at=datetime.now(UTC),
    )
    test_session.add(account)
    await test_session.commit()
    await test_session.refresh(account)
    return account


@pytest_asyncio.fixture
async def inactive_user(test_session: AsyncSession):
    """Create a user inactive for 400+ days (balance expired)."""
    from token_metering_api.models import TokenAccount

    account = TokenAccount(
        user_id="inactive-user-000",
        balance=50000,  # Has balance but inactive
        last_activity_at=datetime.now(UTC) - timedelta(days=400),
    )
    test_session.add(account)
    await test_session.commit()
    await test_session.refresh(account)
    return account


@pytest_asyncio.fixture
async def negative_balance_user(test_session: AsyncSession):
    """Create a user with negative balance (streaming overage)."""
    from token_metering_api.models import TokenAccount

    account = TokenAccount(
        user_id="negative-balance-111",
        balance=-500,  # Went negative from streaming overage
        last_activity_at=datetime.now(UTC),
    )
    test_session.add(account)
    await test_session.commit()
    await test_session.refresh(account)
    return account
