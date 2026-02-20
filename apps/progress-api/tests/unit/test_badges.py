"""Tests for badge evaluation engine."""

from progress_api.services.engine.badges import BADGE_DEFINITIONS, evaluate_badges


class TestBadgeDefinitions:
    """Verify badge definitions are complete."""

    def test_fourteen_badges_defined(self):
        assert len(BADGE_DEFINITIONS) == 14

    def test_all_badges_have_required_fields(self):
        for badge_id, badge in BADGE_DEFINITIONS.items():
            assert badge.id == badge_id
            assert badge.name
            assert badge.description
            assert badge.category


class TestFirstStepsBadge:
    """first-steps: awarded on first quiz ever."""

    def test_first_quiz_awards_badge(self):
        badges = evaluate_badges(
            score_pct=50,
            attempt_number=1,
            is_first_quiz_ever=True,
            current_streak=1,
            existing_badge_ids=set(),
        )
        assert "first-steps" in badges

    def test_not_first_quiz_no_badge(self):
        badges = evaluate_badges(
            score_pct=100,
            attempt_number=1,
            is_first_quiz_ever=False,
            current_streak=1,
            existing_badge_ids=set(),
        )
        assert "first-steps" not in badges


class TestPerfectScoreBadge:
    """perfect-score: awarded on 100% score."""

    def test_perfect_score_awards_badge(self):
        badges = evaluate_badges(
            score_pct=100,
            attempt_number=1,
            is_first_quiz_ever=False,
            current_streak=1,
            existing_badge_ids=set(),
        )
        assert "perfect-score" in badges

    def test_ninety_nine_no_badge(self):
        badges = evaluate_badges(
            score_pct=99,
            attempt_number=1,
            is_first_quiz_ever=False,
            current_streak=1,
            existing_badge_ids=set(),
        )
        assert "perfect-score" not in badges


class TestAceBadge:
    """ace: 100% on first attempt."""

    def test_perfect_first_attempt(self):
        badges = evaluate_badges(
            score_pct=100,
            attempt_number=1,
            is_first_quiz_ever=False,
            current_streak=1,
            existing_badge_ids=set(),
        )
        assert "ace" in badges

    def test_perfect_second_attempt_no_ace(self):
        badges = evaluate_badges(
            score_pct=100,
            attempt_number=2,
            is_first_quiz_ever=False,
            current_streak=1,
            existing_badge_ids=set(),
        )
        assert "ace" not in badges

    def test_ninety_nine_first_attempt_no_ace(self):
        badges = evaluate_badges(
            score_pct=99,
            attempt_number=1,
            is_first_quiz_ever=False,
            current_streak=1,
            existing_badge_ids=set(),
        )
        assert "ace" not in badges


class TestStreakBadges:
    """Streak badges at 3, 7, 30 days."""

    def test_three_day_streak(self):
        badges = evaluate_badges(
            score_pct=50,
            attempt_number=1,
            is_first_quiz_ever=False,
            current_streak=3,
            existing_badge_ids=set(),
        )
        assert "on-fire" in badges
        assert "week-warrior" not in badges

    def test_seven_day_streak(self):
        badges = evaluate_badges(
            score_pct=50,
            attempt_number=1,
            is_first_quiz_ever=False,
            current_streak=7,
            existing_badge_ids=set(),
        )
        assert "on-fire" in badges
        assert "week-warrior" in badges
        assert "dedicated" not in badges

    def test_thirty_day_streak(self):
        badges = evaluate_badges(
            score_pct=50,
            attempt_number=1,
            is_first_quiz_ever=False,
            current_streak=30,
            existing_badge_ids=set(),
        )
        assert "on-fire" in badges
        assert "week-warrior" in badges
        assert "dedicated" in badges

    def test_two_day_streak_no_badges(self):
        badges = evaluate_badges(
            score_pct=50,
            attempt_number=1,
            is_first_quiz_ever=False,
            current_streak=2,
            existing_badge_ids=set(),
        )
        assert "on-fire" not in badges


class TestIdempotency:
    """Badges already earned are not re-awarded."""

    def test_all_badges_already_earned(self):
        badges = evaluate_badges(
            score_pct=100,
            attempt_number=1,
            is_first_quiz_ever=True,
            current_streak=30,
            existing_badge_ids={
                "first-steps",
                "perfect-score",
                "ace",
                "on-fire",
                "week-warrior",
                "dedicated",
            },
        )
        assert badges == []

    def test_partial_existing_badges(self):
        badges = evaluate_badges(
            score_pct=100,
            attempt_number=1,
            is_first_quiz_ever=True,
            current_streak=3,
            existing_badge_ids={"first-steps"},
        )
        # first-steps already earned, but perfect-score, ace, on-fire are new
        assert "first-steps" not in badges
        assert "perfect-score" in badges
        assert "ace" in badges
        assert "on-fire" in badges


class TestCombinedBadges:
    """Multiple badges can be earned simultaneously."""

    def test_first_quiz_perfect_with_streak(self):
        badges = evaluate_badges(
            score_pct=100,
            attempt_number=1,
            is_first_quiz_ever=True,
            current_streak=7,
            existing_badge_ids=set(),
        )
        assert set(badges) == {"first-steps", "perfect-score", "ace", "on-fire", "week-warrior"}
