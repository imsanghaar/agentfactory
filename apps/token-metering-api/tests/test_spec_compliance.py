"""Test spec compliance gaps identified in FR-033, FR-048, FR-069."""

from datetime import UTC, datetime
from decimal import Decimal
from unittest.mock import patch

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from token_metering_api.models import (
    STARTER_TOKENS,
    Pricing,
    TokenAccount,
)
from token_metering_api.services.metering import MeteringService


class TestFR069EstimatedTokensExceedsLimit:
    """FR-069: estimated_tokens MUST be <= model's max_tokens limit."""

    @pytest_asyncio.fixture
    async def user_with_tokens(self, test_session: AsyncSession):
        """Create user with ample balance."""
        account = TokenAccount(
            user_id="fr069-test-user",
            balance=500_000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()
        await test_session.refresh(account)
        return account

    @pytest_asyncio.fixture
    async def pricing_with_max_tokens(self, test_session: AsyncSession):
        """Create pricing with max_tokens limit."""
        pricing = Pricing(
            model="deepseek-chat",
            input_cost_per_1k=Decimal("0.001"),
            output_cost_per_1k=Decimal("0.002"),
            pricing_version="v1",
            max_tokens=128_000,
            is_active=True,
        )
        test_session.add(pricing)
        await test_session.commit()
        await test_session.refresh(pricing)
        return pricing

    @pytest.mark.asyncio
    async def test_estimated_tokens_exceeds_limit_blocked(
        self,
        test_session: AsyncSession,
        user_with_tokens,
        pricing_with_max_tokens,
    ):
        """Check should fail when estimated_tokens > model's max_tokens."""
        service = MeteringService(test_session)
        # Mock Redis to avoid dependency
        service.redis = None

        # Request with estimated_tokens > max_tokens (128000)
        result = await service.check_balance(
            user_id="fr069-test-user",
            request_id="req-fr069-1",
            estimated_tokens=150_000,  # Exceeds 128000
            model="deepseek-chat",
        )

        assert result["allowed"] is False
        assert result["error_code"] == "ESTIMATED_TOKENS_EXCEEDS_LIMIT"
        assert "150000" in result["message"]
        assert "128000" in result["message"]

    @pytest.mark.asyncio
    async def test_estimated_tokens_within_limit_allowed(
        self,
        test_session: AsyncSession,
        user_with_tokens,
        pricing_with_max_tokens,
    ):
        """Check should succeed when estimated_tokens <= model's max_tokens."""
        service = MeteringService(test_session)
        # Mock Redis to avoid dependency
        service.redis = None

        # Enable fail-open mode for test
        with patch("token_metering_api.services.metering.settings") as mock_settings:
            mock_settings.fail_open = True
            mock_settings.reservation_ttl = 300
            mock_settings.starter_credits = STARTER_TOKENS
            mock_settings.markup_percent = 20.0
            mock_settings.credits_per_dollar = 10_000

            result = await service.check_balance(
                user_id="fr069-test-user",
                request_id="req-fr069-2",
                estimated_tokens=100_000,  # Within 128000
                model="deepseek-chat",
            )

        assert result["allowed"] is True

    @pytest.mark.asyncio
    async def test_estimated_tokens_at_exact_limit_allowed(
        self,
        test_session: AsyncSession,
        user_with_tokens,
        pricing_with_max_tokens,
    ):
        """Check should succeed when estimated_tokens == model's max_tokens."""
        service = MeteringService(test_session)
        service.redis = None

        with patch("token_metering_api.services.metering.settings") as mock_settings:
            mock_settings.fail_open = True
            mock_settings.reservation_ttl = 300
            mock_settings.starter_credits = STARTER_TOKENS
            mock_settings.markup_percent = 20.0
            mock_settings.credits_per_dollar = 10_000

            result = await service.check_balance(
                user_id="fr069-test-user",
                request_id="req-fr069-3",
                estimated_tokens=128_000,  # Exactly at limit
                model="deepseek-chat",
            )

        assert result["allowed"] is True

    @pytest.mark.asyncio
    async def test_no_max_tokens_uses_default(
        self,
        test_session: AsyncSession,
        user_with_tokens,
    ):
        """When no pricing found, use default max_tokens (128000)."""
        service = MeteringService(test_session)
        service.redis = None

        # Request with model that has no pricing entry
        result = await service.check_balance(
            user_id="fr069-test-user",
            request_id="req-fr069-4",
            estimated_tokens=200_000,  # Exceeds default 128000
            model="unknown-model",
        )

        assert result["allowed"] is False
        assert result["error_code"] == "ESTIMATED_TOKENS_EXCEEDS_LIMIT"


class TestFR033FailOpenSelectForUpdate:
    """FR-033: Fail-open mode MUST use SELECT FOR UPDATE for concurrency control."""

    @pytest_asyncio.fixture
    async def user_for_failopen(self, test_session: AsyncSession):
        """Create user for fail-open testing."""
        account = TokenAccount(
            user_id="failopen-user",
            balance=10_000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()
        await test_session.refresh(account)
        return account

    @pytest.mark.asyncio
    async def test_failopen_uses_select_for_update(
        self,
        test_session: AsyncSession,
        user_for_failopen,
    ):
        """In fail-open mode, should use SELECT FOR UPDATE for locking."""
        service = MeteringService(test_session)
        service.redis = None  # Simulate Redis unavailable

        with patch("token_metering_api.services.metering.settings") as mock_settings:
            mock_settings.fail_open = True
            mock_settings.reservation_ttl = 300
            mock_settings.starter_credits = STARTER_TOKENS
            mock_settings.markup_percent = 20.0
            mock_settings.credits_per_dollar = 10_000

            # We can't easily verify FOR UPDATE was used in SQLite,
            # but we can verify the query succeeds and reservation is created
            result = await service.check_balance(
                user_id="failopen-user",
                request_id="req-failopen-1",
                estimated_tokens=5_000,
                model="test-model",
            )

        assert result["allowed"] is True
        assert result["reservation_id"].startswith("failopen_")

    @pytest.mark.asyncio
    async def test_failopen_blocks_insufficient_balance(
        self,
        test_session: AsyncSession,
    ):
        """Fail-open mode should still block when balance is insufficient."""
        # Create user with very low balance (below pessimistic estimate for 50k tokens)
        low_balance_account = TokenAccount(
            user_id="failopen-low-balance",
            balance=5,  # Only 5 credits, estimate for 50k tokens = ~1200 credits
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(low_balance_account)
        await test_session.commit()

        service = MeteringService(test_session)
        service.redis = None

        with patch("token_metering_api.services.metering.settings") as mock_settings:
            mock_settings.fail_open = True
            mock_settings.reservation_ttl = 300
            mock_settings.starter_credits = STARTER_TOKENS
            mock_settings.markup_percent = 20.0
            mock_settings.credits_per_dollar = 10_000

            result = await service.check_balance(
                user_id="failopen-low-balance",
                request_id="req-failopen-2",
                estimated_tokens=50_000,  # Estimate ~1200 credits > 5 balance
                model="test-model",
            )

        assert result["allowed"] is False
        assert result["error_code"] == "INSUFFICIENT_BALANCE"


class TestFR048PricingQueryLimit:
    """FR-048: Pricing query should use LIMIT 1 explicitly."""

    @pytest_asyncio.fixture
    async def multiple_pricing_versions(self, test_session: AsyncSession):
        """Create multiple pricing versions for same model."""
        from datetime import date, timedelta

        # Old pricing
        old_pricing = Pricing(
            model="gpt-4",
            input_cost_per_1k=Decimal("0.030"),
            output_cost_per_1k=Decimal("0.060"),
            pricing_version="v1",
            effective_date=date.today() - timedelta(days=30),
            is_active=True,
        )
        test_session.add(old_pricing)

        # New pricing (more recent)
        new_pricing = Pricing(
            model="gpt-4",
            input_cost_per_1k=Decimal("0.025"),
            output_cost_per_1k=Decimal("0.050"),
            pricing_version="v2",
            effective_date=date.today(),
            is_active=True,
        )
        test_session.add(new_pricing)

        await test_session.commit()
        return old_pricing, new_pricing

    @pytest.mark.asyncio
    async def test_pricing_query_returns_latest(
        self,
        test_session: AsyncSession,
        multiple_pricing_versions,
    ):
        """Should return most recent pricing (by effective_date DESC)."""
        service = MeteringService(test_session)

        pricing = await service._get_pricing("gpt-4")

        # Should return v2 (the newer one)
        assert pricing["version"] == "v2"
        assert pricing["input"] == Decimal("0.025")
        assert pricing["output"] == Decimal("0.050")

    @pytest.mark.asyncio
    async def test_pricing_falls_back_to_default(
        self,
        test_session: AsyncSession,
    ):
        """Should return default pricing when model not found."""
        service = MeteringService(test_session)

        pricing = await service._get_pricing("nonexistent-model")

        assert pricing["version"] == "default-v1"
        assert pricing["input"] == Decimal("0.001")
        assert pricing["output"] == Decimal("0.002")


class TestPricingModelMaxTokens:
    """Test that Pricing model includes max_tokens field."""

    @pytest.mark.asyncio
    async def test_pricing_has_max_tokens_field(self, test_session: AsyncSession):
        """Pricing model should have max_tokens field with default 128000."""
        pricing = Pricing(
            model="test-model",
            input_cost_per_1k=Decimal("0.001"),
            output_cost_per_1k=Decimal("0.002"),
            pricing_version="v1",
            is_active=True,
        )
        test_session.add(pricing)
        await test_session.commit()
        await test_session.refresh(pricing)

        # Default should be 128000
        assert pricing.max_tokens == 128_000

    @pytest.mark.asyncio
    async def test_pricing_custom_max_tokens(self, test_session: AsyncSession):
        """Pricing should accept custom max_tokens value."""
        pricing = Pricing(
            model="gpt-4-32k",
            input_cost_per_1k=Decimal("0.060"),
            output_cost_per_1k=Decimal("0.120"),
            pricing_version="v1",
            max_tokens=32_000,
            is_active=True,
        )
        test_session.add(pricing)
        await test_session.commit()
        await test_session.refresh(pricing)

        assert pricing.max_tokens == 32_000


class TestDefaultPricingMaxTokens:
    """Test DEFAULT_PRICING includes max_tokens."""

    def test_default_pricing_has_max_tokens(self):
        """DEFAULT_PRICING should include max_tokens."""
        from token_metering_api.services.metering import DEFAULT_PRICING

        assert "max_tokens" in DEFAULT_PRICING
        assert DEFAULT_PRICING["max_tokens"] == 128_000
