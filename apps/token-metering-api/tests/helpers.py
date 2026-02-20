"""Test helper functions."""

import hashlib
import math
import uuid
from decimal import Decimal


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


# Default pricing constants (match DEFAULT_PRICING in metering service)
DEFAULT_INPUT_COST_PER_1K = Decimal("0.001")
DEFAULT_OUTPUT_COST_PER_1K = Decimal("0.002")
DEFAULT_MARKUP_PERCENT = Decimal("20")
DEFAULT_CREDITS_PER_DOLLAR = 10_000


def calculate_expected_credits(
    input_tokens: int,
    output_tokens: int,
    input_cost_per_1k: Decimal = DEFAULT_INPUT_COST_PER_1K,
    output_cost_per_1k: Decimal = DEFAULT_OUTPUT_COST_PER_1K,
    markup_percent: Decimal = DEFAULT_MARKUP_PERCENT,
    credits_per_dollar: int = DEFAULT_CREDITS_PER_DOLLAR,
) -> int:
    """Calculate expected credits for a given token usage with default pricing.

    Formula:
        base_cost = (input_tokens/1000 * input_rate) + (output_tokens/1000 * output_rate)
        cost_with_markup = base_cost * (1 + markup_percent/100)
        credits = ceil(cost_with_markup * credits_per_dollar)
    """
    base_cost = (
        Decimal(str(input_tokens)) / 1000 * input_cost_per_1k
        + Decimal(str(output_tokens)) / 1000 * output_cost_per_1k
    )
    cost_with_markup = base_cost * (1 + markup_percent / 100)
    credits = math.ceil(float(cost_with_markup * credits_per_dollar))
    return credits


def estimate_credits_pessimistic(
    estimated_tokens: int,
    input_cost_per_1k: Decimal = DEFAULT_INPUT_COST_PER_1K,
    output_cost_per_1k: Decimal = DEFAULT_OUTPUT_COST_PER_1K,
    markup_percent: Decimal = DEFAULT_MARKUP_PERCENT,
    credits_per_dollar: int = DEFAULT_CREDITS_PER_DOLLAR,
) -> int:
    """Calculate pessimistic credit estimate (used for reservations).

    Uses max(input_rate, output_rate) for both halves, split 50/50.
    """
    max_rate = max(input_cost_per_1k, output_cost_per_1k)
    half = estimated_tokens // 2
    other_half = estimated_tokens - half
    base_cost = (
        Decimal(str(half)) / 1000 * max_rate
        + Decimal(str(other_half)) / 1000 * max_rate
    )
    cost_with_markup = base_cost * (1 + markup_percent / 100)
    credits = math.ceil(float(cost_with_markup * credits_per_dollar))
    return credits
