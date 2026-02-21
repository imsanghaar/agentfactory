"""User model."""

from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sa
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, func


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: str = Field(primary_key=True)
    display_name: str
    email: str | None = None
    avatar_url: str | None = None
    show_on_leaderboard: bool = Field(
        default=True,
        sa_column_kwargs={"server_default": sa.sql.true()},
    )
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            default=lambda: datetime.now(timezone.utc),
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            default=lambda: datetime.now(timezone.utc),
            onupdate=lambda: datetime.now(timezone.utc),
        )
    )

    # Relationships for selectinload
    badges: list["UserBadge"] = Relationship(back_populates="user")  # noqa: F821
    quiz_attempts: list["QuizAttempt"] = Relationship(back_populates="user")  # noqa: F821
    progress: Optional["UserProgress"] = Relationship(back_populates="user")  # noqa: F821
