"""Quiz submission endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser, get_current_user
from ..core.database import get_session
from ..schemas.quiz import QuizSubmitRequest, QuizSubmitResponse
from ..services.quiz import submit_quiz

router = APIRouter()


@router.post("/quiz/submit", response_model=QuizSubmitResponse)
async def quiz_submit(
    request: QuizSubmitRequest,
    user: CurrentUser = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> QuizSubmitResponse:
    """Submit a quiz score.

    Processes XP calculation, badge evaluation, streak tracking,
    and returns the full gamification payload.
    """
    return await submit_quiz(session, user, request)
