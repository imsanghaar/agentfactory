"""Leaderboard endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser, get_optional_user
from ..core.database import get_session
from ..schemas.leaderboard import LeaderboardResponse
from ..services.leaderboard import get_leaderboard

router = APIRouter()


@router.get("/leaderboard", response_model=LeaderboardResponse)
async def leaderboard(
    user: CurrentUser | None = Depends(get_optional_user),
    session: AsyncSession = Depends(get_session),
) -> LeaderboardResponse:
    """Get the global leaderboard.

    Returns top 100 users ranked by XP.
    If authenticated, also includes the current user's rank.
    """
    return await get_leaderboard(session, user)
