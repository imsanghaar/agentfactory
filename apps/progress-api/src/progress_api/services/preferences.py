"""Preferences service — user privacy controls."""

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser
from ..schemas.preferences import PreferencesResponse, PreferencesUpdateRequest
from .shared import invalidate_user_cache, upsert_user_from_jwt

logger = logging.getLogger(__name__)


async def update_preferences(
    session: AsyncSession,
    user: CurrentUser,
    request: PreferencesUpdateRequest,
) -> PreferencesResponse:
    """Update user preferences (e.g., leaderboard opt-out).

    Steps:
    1. Ensure user exists
    2. Update show_on_leaderboard flag
    3. Commit
    4. Invalidate caches
    """
    db_user = await upsert_user_from_jwt(session, user)

    db_user.show_on_leaderboard = request.show_on_leaderboard

    session.add(db_user)
    await session.commit()

    # Invalidate caches (progress + leaderboard)
    await invalidate_user_cache(user.id)

    return PreferencesResponse(
        show_on_leaderboard=db_user.show_on_leaderboard,
    )
