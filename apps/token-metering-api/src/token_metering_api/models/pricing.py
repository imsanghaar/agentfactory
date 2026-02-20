"""Pricing model for LLM cost calculation."""

from datetime import UTC, date, datetime
from decimal import Decimal

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel


class Pricing(SQLModel, table=True):
    """Model pricing configuration for cost calculation."""

    __tablename__ = "pricing"

    id: int | None = Field(default=None, primary_key=True)
    model: str = Field(max_length=100, index=True)
    pricing_version: str = Field(max_length=20)
    effective_date: date = Field(default_factory=lambda: date.today())

    # Cost per 1000 tokens
    input_cost_per_1k: Decimal = Field(max_digits=10, decimal_places=6)
    output_cost_per_1k: Decimal = Field(max_digits=10, decimal_places=6)

    # Maximum tokens allowed per request for this model (FR-069)
    max_tokens: int = Field(
        default=128_000, description="Maximum tokens per request for this model"
    )

    is_active: bool = Field(default=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )
