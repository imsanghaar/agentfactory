"""UserBadge model."""

from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sa
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, func


class UserBadge(SQLModel, table=True):
    __tablename__ = "user_badges"

    user_id: str = Field(sa_column=Column(sa.String, sa.ForeignKey("users.id"), primary_key=True))
    badge_id: str = Field(sa_column=Column(sa.String, primary_key=True))
    earned_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            default=lambda: datetime.now(timezone.utc),
        )
    )
    trigger_ref: str | None = None

    # Relationship
    user: Optional["User"] = Relationship(back_populates="badges")  # noqa: F821
