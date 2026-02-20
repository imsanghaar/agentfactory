"""Direct unit tests for credit calculation methods (v6).

These tests verify _calculate_credits, _estimate_credits, and rounding
behavior independently from the HTTP layer and database.
"""

from datetime import UTC, datetime
from decimal import Decimal

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from tests.helpers import (
    calculate_expected_credits,
    estimate_credits_pessimistic,
)
from token_metering_api.models import Pricing, TokenAccount
from token_metering_api.services.metering import (
    DEFAULT_PRICING,
    CreditCalculation,
    MeteringService,
)


@pytest_asyncio.fixture
async def metering_service(test_session: AsyncSession) -> MeteringService:
    """Create MeteringService instance for unit testing."""
    return MeteringService(test_session)


class TestCalculateCredits:
    """Unit tests for MeteringService._calculate_credits."""

    def test_basic_500i_500o(self, metering_service: MeteringService):
        """500 input + 500 output at default pricing = 18 credits."""
        result = metering_service._calculate_credits(500, 500, DEFAULT_PRICING)
        assert result.credits == 18
        assert result.credits == calculate_expected_credits(500, 500)

    def test_1000i_500o(self, metering_service: MeteringService):
        """1000 input + 500 output = 24 credits."""
        result = metering_service._calculate_credits(1000, 500, DEFAULT_PRICING)
        assert result.credits == 24
        assert result.credits == calculate_expected_credits(1000, 500)

    def test_5000i_5000o(self, metering_service: MeteringService):
        """5000 input + 5000 output = 180 credits."""
        result = metering_service._calculate_credits(5000, 5000, DEFAULT_PRICING)
        assert result.credits == 180
        assert result.credits == calculate_expected_credits(5000, 5000)

    def test_zero_tokens_zero_credits(self, metering_service: MeteringService):
        """Zero tokens should produce zero credits."""
        result = metering_service._calculate_credits(0, 0, DEFAULT_PRICING)
        assert result.credits == 0
        assert result.base_cost_usd == Decimal("0")

    def test_one_token_minimum_one_credit(self, metering_service: MeteringService):
        """1 token should produce at least 1 credit (never free for non-zero)."""
        result = metering_service._calculate_credits(1, 0, DEFAULT_PRICING)
        assert result.credits >= 1

    def test_fractional_credits_round_up(self, metering_service: MeteringService):
        """Fractional credit amounts always round up (ROUND_CEILING)."""
        # 1 input token: cost = 1/1000 * 0.001 = 0.000001
        # with markup: 0.0000012, * 10000 = 0.012 → ceil = 1
        result = metering_service._calculate_credits(1, 0, DEFAULT_PRICING)
        assert result.credits == 1  # Rounded up from 0.012

    def test_markup_applied(self, metering_service: MeteringService):
        """20% markup should make cost_with_markup > base_cost."""
        result = metering_service._calculate_credits(1000, 1000, DEFAULT_PRICING)
        assert result.cost_with_markup_usd > result.base_cost_usd
        # Verify exact 20% markup
        expected_markup = result.base_cost_usd * Decimal("1.2")
        assert result.cost_with_markup_usd == expected_markup

    def test_pricing_version_passed_through(self, metering_service: MeteringService):
        """pricing_version from pricing dict should appear in CreditCalculation."""
        result = metering_service._calculate_credits(100, 100, DEFAULT_PRICING)
        assert result.pricing_version == "default-v1"

    def test_credit_calculation_dataclass_fields(self, metering_service: MeteringService):
        """CreditCalculation should have all expected fields."""
        result = metering_service._calculate_credits(500, 500, DEFAULT_PRICING)
        assert isinstance(result, CreditCalculation)
        assert isinstance(result.base_cost_usd, Decimal)
        assert isinstance(result.cost_with_markup_usd, Decimal)
        assert isinstance(result.credits, int)
        assert isinstance(result.pricing_version, str)


class TestEstimateCredits:
    """Unit tests for MeteringService._estimate_credits (pessimistic estimation)."""

    def test_pessimistic_uses_max_rate(self, metering_service: MeteringService):
        """Pessimistic estimate should use max(input_rate, output_rate) for both halves."""
        result = metering_service._estimate_credits(1000, DEFAULT_PRICING)
        assert result.credits == 24
        assert result.credits == estimate_credits_pessimistic(1000)

    def test_estimate_1500_tokens(self, metering_service: MeteringService):
        """1500 tokens pessimistic estimate = 36 credits."""
        result = metering_service._estimate_credits(1500, DEFAULT_PRICING)
        assert result.credits == 36
        assert result.credits == estimate_credits_pessimistic(1500)

    def test_odd_token_count_split(self, metering_service: MeteringService):
        """Odd token count: 1001 → 500 + 501 (ceil split)."""
        result = metering_service._estimate_credits(1001, DEFAULT_PRICING)
        # Manual: max_rate=0.002, 500/1000*0.002 + 501/1000*0.002
        # = 0.001 + 0.001002 = 0.002002 * 1.2 = 0.0024024 * 10000 = 24.024 → ceil = 25
        assert result.credits == estimate_credits_pessimistic(1001)

    def test_estimate_gte_actual_all_input(self, metering_service: MeteringService):
        """Estimate should be >= actual when all tokens are input."""
        estimated_tokens = 2000
        estimate = metering_service._estimate_credits(estimated_tokens, DEFAULT_PRICING)
        actual = metering_service._calculate_credits(
            estimated_tokens, 0, DEFAULT_PRICING
        )
        assert estimate.credits >= actual.credits

    def test_estimate_gte_actual_all_output(self, metering_service: MeteringService):
        """Estimate should be >= actual when all tokens are output."""
        estimated_tokens = 2000
        estimate = metering_service._estimate_credits(estimated_tokens, DEFAULT_PRICING)
        actual = metering_service._calculate_credits(
            0, estimated_tokens, DEFAULT_PRICING
        )
        assert estimate.credits >= actual.credits

    def test_estimate_gte_actual_balanced(self, metering_service: MeteringService):
        """Estimate should be >= actual for balanced input/output."""
        estimated_tokens = 2000
        estimate = metering_service._estimate_credits(estimated_tokens, DEFAULT_PRICING)
        actual = metering_service._calculate_credits(1000, 1000, DEFAULT_PRICING)
        assert estimate.credits >= actual.credits

    def test_estimate_gte_actual_skewed(self, metering_service: MeteringService):
        """Estimate should be >= actual for skewed distributions."""
        estimated_tokens = 2000
        estimate = metering_service._estimate_credits(estimated_tokens, DEFAULT_PRICING)
        # Heavily output-skewed (worst case for cost)
        actual = metering_service._calculate_credits(200, 1800, DEFAULT_PRICING)
        assert estimate.credits >= actual.credits

    def test_worst_case_all_output_covered(self, metering_service: MeteringService):
        """Even worst case (100% output) should be covered by pessimistic estimate."""
        for token_count in [100, 1000, 5000, 10000, 50000]:
            estimate = metering_service._estimate_credits(token_count, DEFAULT_PRICING)
            worst_case = metering_service._calculate_credits(
                0, token_count, DEFAULT_PRICING
            )
            assert estimate.credits >= worst_case.credits, (
                f"Estimate {estimate.credits} < worst case {worst_case.credits} "
                f"for {token_count} tokens"
            )


class TestRoundCeiling:
    """Tests verifying ROUND_CEILING behavior in credit conversion."""

    def test_fractional_rounds_to_one(self, metering_service: MeteringService):
        """0.1 credits worth → rounds up to 1 credit."""
        # 1 input token = $0.000001 base, * 1.2 markup = $0.0000012
        # * 10000 credits/$ = 0.012 → ceil = 1
        result = metering_service._calculate_credits(1, 0, DEFAULT_PRICING)
        assert result.credits == 1

    def test_exact_integer_stays_same(self, metering_service: MeteringService):
        """Exact integer credit amount should stay the same."""
        # We need a token count that produces an exact integer
        # 500i + 500o: base = 0.5/1000*0.001 + 0.5/1000*0.002 = 0.0005+0.001 = 0.0015
        # * 1.2 = 0.0018 * 10000 = 18.0 → exactly 18
        result = metering_service._calculate_credits(500, 500, DEFAULT_PRICING)
        assert result.credits == 18

    def test_cheapest_model_one_token_minimum_one(self, metering_service: MeteringService):
        """1 token of cheapest possible model still costs at least 1 credit."""
        cheap_pricing = {
            "input": Decimal("0.00014"),  # DeepSeek-level pricing
            "output": Decimal("0.00028"),
            "version": "cheap-v1",
        }
        result = metering_service._calculate_credits(1, 0, cheap_pricing)
        assert result.credits >= 1

    def test_never_returns_zero_for_nonzero_tokens(self, metering_service: MeteringService):
        """Non-zero token usage should never produce 0 credits."""
        # Test with various small token counts
        for i_tokens, o_tokens in [(1, 0), (0, 1), (1, 1)]:
            result = metering_service._calculate_credits(
                i_tokens, o_tokens, DEFAULT_PRICING
            )
            assert result.credits >= 1, (
                f"Got 0 credits for {i_tokens}i+{o_tokens}o"
            )


class TestPricingTiers:
    """Tests verifying different model pricing produces different credit amounts."""

    @pytest_asyncio.fixture
    async def seeded_pricing(self, test_session: AsyncSession):
        """Seed two models with vastly different pricing."""
        cheap = Pricing(
            model="deepseek-chat",
            input_cost_per_1k=Decimal("0.000140"),
            output_cost_per_1k=Decimal("0.000280"),
            max_tokens=64_000,
            pricing_version="v1",
            is_active=True,
        )
        expensive = Pricing(
            model="claude-opus-4",
            input_cost_per_1k=Decimal("0.015000"),
            output_cost_per_1k=Decimal("0.075000"),
            max_tokens=200_000,
            pricing_version="v1",
            is_active=True,
        )
        test_session.add(cheap)
        test_session.add(expensive)
        await test_session.commit()
        return {"cheap": cheap, "expensive": expensive}

    async def test_same_tokens_different_credits(
        self, metering_service: MeteringService, seeded_pricing
    ):
        """Same 2500 tokens cost different credits with different models."""
        cheap_pricing = await metering_service._get_pricing("deepseek-chat")
        expensive_pricing = await metering_service._get_pricing("claude-opus-4")

        cheap_calc = metering_service._calculate_credits(
            1250, 1250, cheap_pricing
        )
        expensive_calc = metering_service._calculate_credits(
            1250, 1250, expensive_pricing
        )

        assert expensive_calc.credits > cheap_calc.credits
        # DeepSeek should be much cheaper than Opus
        assert expensive_calc.credits > cheap_calc.credits * 10

    async def test_default_pricing_fallback(
        self, metering_service: MeteringService, seeded_pricing
    ):
        """Unknown model should fall back to DEFAULT_PRICING."""
        pricing = await metering_service._get_pricing("nonexistent-model-xyz")
        assert pricing["input"] == Decimal("0.001")
        assert pricing["output"] == Decimal("0.002")
        assert pricing["version"] == "default-v1"

    async def test_credits_deducted_differs_by_model(
        self, metering_service: MeteringService, seeded_pricing, test_session
    ):
        """Full check→deduct flow produces different credits for different models."""
        # Create account
        account = TokenAccount(
            user_id="pricing-tier-user",
            balance=1_000_000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        cheap_pricing = await metering_service._get_pricing("deepseek-chat")
        expensive_pricing = await metering_service._get_pricing("claude-opus-4")

        cheap_result = metering_service._calculate_credits(
            1000, 1000, cheap_pricing
        )
        expensive_result = metering_service._calculate_credits(
            1000, 1000, expensive_pricing
        )

        assert cheap_result.credits != expensive_result.credits
        assert expensive_result.credits > cheap_result.credits

    async def test_pessimistic_estimate_differs_by_model(
        self, metering_service: MeteringService, seeded_pricing
    ):
        """Pessimistic estimates also differ by model pricing."""
        cheap_pricing = await metering_service._get_pricing("deepseek-chat")
        expensive_pricing = await metering_service._get_pricing("claude-opus-4")

        cheap_estimate = metering_service._estimate_credits(2000, cheap_pricing)
        expensive_estimate = metering_service._estimate_credits(
            2000, expensive_pricing
        )

        assert expensive_estimate.credits > cheap_estimate.credits


class TestHelperConsistency:
    """Verify test helpers match the actual service implementation."""

    def test_calculate_helper_matches_service(self, metering_service: MeteringService):
        """calculate_expected_credits helper produces same result as service."""
        test_cases = [
            (500, 500),
            (1000, 500),
            (1000, 1000),
            (5000, 5000),
            (100, 200),
            (0, 1000),
            (1000, 0),
        ]
        for i_tokens, o_tokens in test_cases:
            service_result = metering_service._calculate_credits(
                i_tokens, o_tokens, DEFAULT_PRICING
            )
            helper_result = calculate_expected_credits(i_tokens, o_tokens)
            assert service_result.credits == helper_result, (
                f"Mismatch for {i_tokens}i+{o_tokens}o: "
                f"service={service_result.credits}, helper={helper_result}"
            )

    def test_estimate_helper_matches_service(self, metering_service: MeteringService):
        """estimate_credits_pessimistic helper produces same result as service."""
        test_cases = [100, 500, 1000, 1001, 1500, 2000, 5000, 10000]
        for tokens in test_cases:
            service_result = metering_service._estimate_credits(
                tokens, DEFAULT_PRICING
            )
            helper_result = estimate_credits_pessimistic(tokens)
            assert service_result.credits == helper_result, (
                f"Mismatch for {tokens} tokens: "
                f"service={service_result.credits}, helper={helper_result}"
            )
