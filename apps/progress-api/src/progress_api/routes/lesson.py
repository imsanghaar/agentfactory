"""Lesson completion endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser, get_current_user
from ..core.database import get_session
from ..schemas.lesson import LessonCompleteRequest, LessonCompleteResponse
from ..services.lesson import complete_lesson

router = APIRouter()


@router.post("/lesson/complete", response_model=LessonCompleteResponse)
async def lesson_complete(
    request: LessonCompleteRequest,
    user: CurrentUser = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> LessonCompleteResponse:
    """Mark a lesson as complete.

    Idempotent — marking the same lesson complete twice returns
    already_completed=true without creating duplicate records.
    """
    return await complete_lesson(session, user, request)
