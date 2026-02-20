"""UserBadge model."""

from datetime import datetime
from typing import Optional

import sqlalchemy as sa
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, text


class UserBadge(SQLModel, table=True):
    __tablename__ = "user_badges"

    user_id: str = Field(sa_column=Column(sa.String, sa.ForeignKey("users.id"), primary_key=True))
    badge_id: str = Field(sa_column=Column(sa.String, primary_key=True))
    earned_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=text("NOW()"))
    )
    trigger_ref: str | None = None

    # Relationship
    user: Optional["User"] = Relationship(back_populates="badges")  # noqa: F821
