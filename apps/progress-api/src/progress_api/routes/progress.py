"""Progress dashboard endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser, get_current_user
from ..core.database import get_session
from ..schemas.progress import ProgressResponse
from ..services.progress import get_progress

router = APIRouter()


@router.get("/progress/me", response_model=ProgressResponse)
async def progress_me(
    user: CurrentUser = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> ProgressResponse:
    """Get the current user's full progress dashboard.

    Returns stats, badges, chapter progress, and lesson completions.
    """
    return await get_progress(session, user)
