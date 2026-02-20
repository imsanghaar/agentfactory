"""Tests for balance endpoints (v5 - Balance Only)."""

from datetime import UTC, datetime

from httpx import AsyncClient

from token_metering_api.models import (
    STARTER_TOKENS,
    AllocationType,
    TokenAccount,
    TokenAllocation,
)


async def test_get_balance_new_user_with_starter_tokens(client: AsyncClient, new_user):
    """Test getting balance for a new user with starter tokens (v5)."""
    response = await client.get(
        "/api/v1/balance",
        headers={"X-User-ID": new_user.user_id},
    )

    assert response.status_code == 200
    data = response.json()

    assert data["user_id"] == new_user.user_id
    assert data["status"] == "active"
    assert data["balance"] == STARTER_TOKENS
    assert data["effective_balance"] == STARTER_TOKENS
    assert data["is_expired"] is False


async def test_get_balance_user_with_granted_tokens(client: AsyncClient, user_with_balance):
    """Test getting balance for a user with granted tokens (v5)."""
    response = await client.get(
        "/api/v1/balance",
        headers={"X-User-ID": user_with_balance.user_id},
    )

    assert response.status_code == 200
    data = response.json()

    assert data["user_id"] == user_with_balance.user_id
    assert data["status"] == "active"
    assert data["balance"] == 500000
    assert data["effective_balance"] == 500000
    assert data["is_expired"] is False


async def test_get_balance_zero_balance_user(client: AsyncClient, zero_balance_user):
    """Test getting balance for a user with zero balance (v5)."""
    response = await client.get(
        "/api/v1/balance",
        headers={"X-User-ID": zero_balance_user.user_id},
    )

    assert response.status_code == 200
    data = response.json()

    assert data["user_id"] == zero_balance_user.user_id
    assert data["balance"] == 0
    assert data["effective_balance"] == 0
    assert data["is_expired"] is False


async def test_get_balance_inactive_user_shows_expired(client: AsyncClient, inactive_user):
    """Test that inactive user shows is_expired=true and effective_balance=0 (v5)."""
    response = await client.get(
        "/api/v1/balance",
        headers={"X-User-ID": inactive_user.user_id},
    )

    assert response.status_code == 200
    data = response.json()

    assert data["user_id"] == inactive_user.user_id
    assert data["balance"] == 50000  # Balance is preserved
    assert data["effective_balance"] == 0  # But effective is 0 due to inactivity
    assert data["is_expired"] is True


async def test_get_balance_missing_user_header(client: AsyncClient):
    """Test that missing X-User-ID header falls back to dev_user_id.

    In dev mode, missing X-User-ID falls back to settings.dev_user_id.
    Since that user doesn't exist in test DB, returns 404.
    """
    response = await client.get("/api/v1/balance")

    # Dev mode falls back to dev_user_id which doesn't exist in test DB
    assert response.status_code == 404


async def test_get_allocations_returns_audit_records(client: AsyncClient, test_session):
    """Test that allocations endpoint returns audit records (v5).

    v5: Allocations are audit-only, includes STARTER type.
    """
    # Create user first
    account = TokenAccount(
        user_id="alloc-test-user",
        balance=STARTER_TOKENS + 1500,
        last_activity_at=datetime.now(UTC),
    )
    test_session.add(account)
    await test_session.commit()

    # Create allocation audit records (v5 style)
    starter_alloc = TokenAllocation(
        user_id="alloc-test-user",
        allocation_type=AllocationType.STARTER,
        amount=STARTER_TOKENS,
        reason="Initial starter tokens",
    )
    grant_alloc = TokenAllocation(
        user_id="alloc-test-user",
        allocation_type=AllocationType.GRANT,
        amount=1000,
        reason="Test grant",
    )
    topup_alloc = TokenAllocation(
        user_id="alloc-test-user",
        allocation_type=AllocationType.TOPUP,
        amount=500,
        reason="Test topup",
    )

    test_session.add_all([starter_alloc, grant_alloc, topup_alloc])
    await test_session.commit()

    response = await client.get(
        "/api/v1/allocations",
        headers={"X-User-ID": "alloc-test-user"},
    )

    assert response.status_code == 200
    data = response.json()

    assert data["user_id"] == "alloc-test-user"
    assert len(data["allocations"]) == 3

    # v5: Allocations are audit records with amount
    amounts = {a["reason"]: a["amount"] for a in data["allocations"]}
    assert amounts["Initial starter tokens"] == STARTER_TOKENS
    assert amounts["Test grant"] == 1000
    assert amounts["Test topup"] == 500


async def test_get_balance_returns_404_for_nonexistent_user(client: AsyncClient):
    """Test that getting balance for a non-existent user returns 404.

    BalanceService.get_balance returns None for non-existent users.
    Account creation happens via MeteringService.check_balance (on first request).
    """
    new_user_id = "brand-new-user-999"

    response = await client.get(
        "/api/v1/balance",
        headers={"X-User-ID": new_user_id},
    )

    # Balance endpoint does NOT auto-create accounts
    assert response.status_code == 404


async def test_get_transactions_filter_by_thread_id(
    client: AsyncClient, test_session, user_with_balance
):
    """Test filtering transactions by thread_id."""
    from token_metering_api.services.metering import MeteringService

    # Create transactions with different thread_ids
    service = MeteringService(test_session)

    # Transaction 1 - thread A
    await service.finalize_usage(
        user_id=user_with_balance.user_id,
        request_id="req-tx-filter-001",
        reservation_id="res_test123",
        input_tokens=100,
        output_tokens=100,
        model="deepseek-chat",
        thread_id="thread_A",
    )

    # Transaction 2 - thread A
    await service.finalize_usage(
        user_id=user_with_balance.user_id,
        request_id="req-tx-filter-002",
        reservation_id="res_test123",
        input_tokens=200,
        output_tokens=200,
        model="deepseek-chat",
        thread_id="thread_A",
    )

    # Transaction 3 - thread B
    await service.finalize_usage(
        user_id=user_with_balance.user_id,
        request_id="req-tx-filter-003",
        reservation_id="res_test123",
        input_tokens=300,
        output_tokens=300,
        model="deepseek-chat",
        thread_id="thread_B",
    )

    # Filter by thread_A
    response = await client.get(
        "/api/v1/transactions",
        headers={"X-User-ID": user_with_balance.user_id},
        params={"thread_id": "thread_A"},
    )

    assert response.status_code == 200
    data = response.json()

    # Should only return 2 transactions (thread_A)
    assert data["total"] == 2
    assert len(data["transactions"]) == 2
    for tx in data["transactions"]:
        assert tx["thread_id"] == "thread_A"

    # Filter by thread_B
    response_b = await client.get(
        "/api/v1/transactions",
        headers={"X-User-ID": user_with_balance.user_id},
        params={"thread_id": "thread_B"},
    )

    assert response_b.status_code == 200
    data_b = response_b.json()

    # Should only return 1 transaction (thread_B)
    assert data_b["total"] == 1
    assert len(data_b["transactions"]) == 1
    assert data_b["transactions"][0]["thread_id"] == "thread_B"
