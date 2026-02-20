"""ActivityDay model."""

from datetime import date, datetime

import sqlalchemy as sa
from sqlmodel import Column, DateTime, Field, SQLModel, text


class ActivityDay(SQLModel, table=True):
    __tablename__ = "activity_days"

    user_id: str = Field(sa_column=Column(sa.String, sa.ForeignKey("users.id"), primary_key=True))
    activity_date: date = Field(sa_column=Column(sa.Date, primary_key=True))
    activity_type: str = Field(sa_column=Column(sa.String, primary_key=True))
    reference_id: str = Field(sa_column=Column(sa.String, primary_key=True))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=text("NOW()"))
    )
