"""Badge evaluation engine — pure functions with badge definitions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class BadgeDefinition:
    """Definition of a badge that can be earned."""

    id: str
    name: str
    description: str
    category: str


# Phase 1: 14 base badges
BADGE_DEFINITIONS: dict[str, BadgeDefinition] = {
    "first-steps": BadgeDefinition(
        id="first-steps",
        name="First Steps",
        description="Complete your first quiz",
        category="milestone",
    ),
    "perfect-score": BadgeDefinition(
        id="perfect-score",
        name="Perfect Score",
        description="Score 100% on any quiz",
        category="achievement",
    ),
    "ace": BadgeDefinition(
        id="ace",
        name="Ace",
        description="Score 100% on your first attempt",
        category="achievement",
    ),
    "on-fire": BadgeDefinition(
        id="on-fire",
        name="On Fire",
        description="Maintain a 3-day learning streak",
        category="streak",
    ),
    "week-warrior": BadgeDefinition(
        id="week-warrior",
        name="Week Warrior",
        description="Maintain a 7-day learning streak",
        category="streak",
    ),
    "dedicated": BadgeDefinition(
        id="dedicated",
        name="Dedicated",
        description="Maintain a 30-day learning streak",
        category="streak",
    ),
    "foundations-complete": BadgeDefinition(
        id="foundations-complete",
        name="Foundations Complete",
        description="Complete all quizzes in Part 1",
        category="part_completion",
    ),
    "workflows-complete": BadgeDefinition(
        id="workflows-complete",
        name="Workflows Complete",
        description="Complete all quizzes in Part 2",
        category="part_completion",
    ),
    "sdd-complete": BadgeDefinition(
        id="sdd-complete",
        name="SDD Complete",
        description="Complete all quizzes in Part 3",
        category="part_completion",
    ),
    "coding-complete": BadgeDefinition(
        id="coding-complete",
        name="Coding Complete",
        description="Complete all quizzes in Part 4",
        category="part_completion",
    ),
    "deployment-complete": BadgeDefinition(
        id="deployment-complete",
        name="Deployment Complete",
        description="Complete all quizzes in Part 5",
        category="part_completion",
    ),
    "cloud-native-complete": BadgeDefinition(
        id="cloud-native-complete",
        name="Cloud Native Complete",
        description="Complete all quizzes in Part 6",
        category="part_completion",
    ),
    "agent-factory-graduate": BadgeDefinition(
        id="agent-factory-graduate",
        name="Agent Factory Graduate",
        description="Complete all quizzes in the entire book",
        category="capstone",
    ),
    "elite": BadgeDefinition(
        id="elite",
        name="Elite",
        description="Reach the top 100 on the leaderboard",
        category="ranking",
    ),
}


def evaluate_badges(
    *,
    score_pct: int,
    attempt_number: int,
    is_first_quiz_ever: bool,
    current_streak: int,
    existing_badge_ids: set[str],
) -> list[str]:
    """Evaluate which new badges should be awarded.

    Args:
        score_pct: Score percentage (0-100)
        attempt_number: 1-indexed attempt number for this quiz
        is_first_quiz_ever: Whether this is the user's very first quiz
        current_streak: Current streak length in days (after this activity)
        existing_badge_ids: Set of badge IDs the user already has

    Returns:
        List of new badge IDs to award (excludes already-earned badges)
    """
    new_badges: list[str] = []

    def _award(badge_id: str) -> None:
        if badge_id not in existing_badge_ids:
            new_badges.append(badge_id)

    # First quiz ever
    if is_first_quiz_ever:
        _award("first-steps")

    # Perfect score
    if score_pct == 100:
        _award("perfect-score")

    # Ace: perfect score on first attempt
    if score_pct == 100 and attempt_number == 1:
        _award("ace")

    # Streak badges
    if current_streak >= 3:
        _award("on-fire")
    if current_streak >= 7:
        _award("week-warrior")
    if current_streak >= 30:
        _award("dedicated")

    # Part completion and capstone badges are evaluated elsewhere
    # (requires DB query for all chapters in part — not a pure function)

    return new_badges
