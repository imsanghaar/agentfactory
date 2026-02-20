"""User preferences endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser, get_current_user
from ..core.database import get_session
from ..schemas.preferences import PreferencesResponse, PreferencesUpdateRequest
from ..services.preferences import update_preferences

router = APIRouter()


@router.patch("/progress/me/preferences", response_model=PreferencesResponse)
async def patch_preferences(
    request: PreferencesUpdateRequest,
    user: CurrentUser = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> PreferencesResponse:
    """Update the current user's preferences.

    Supports toggling leaderboard visibility (GDPR opt-out).
    """
    return await update_preferences(session, user, request)
