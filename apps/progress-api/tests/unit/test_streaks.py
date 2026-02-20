"""Tests for streak calculation engine."""

from datetime import date

from progress_api.services.engine.streaks import calculate_streak


class TestEmptyDates:
    def test_no_dates(self):
        current, longest = calculate_streak([], today=date(2026, 2, 12))
        assert current == 0
        assert longest == 0


class TestSingleDay:
    def test_today(self):
        today = date(2026, 2, 12)
        current, longest = calculate_streak([today], today=today)
        assert current == 1
        assert longest == 1

    def test_yesterday(self):
        today = date(2026, 2, 12)
        current, longest = calculate_streak([date(2026, 2, 11)], today=today)
        assert current == 1
        assert longest == 1

    def test_two_days_ago(self):
        today = date(2026, 2, 12)
        current, longest = calculate_streak([date(2026, 2, 10)], today=today)
        assert current == 0
        assert longest == 1


class TestConsecutiveDays:
    def test_three_consecutive_ending_today(self):
        today = date(2026, 2, 12)
        dates = [date(2026, 2, 10), date(2026, 2, 11), date(2026, 2, 12)]
        current, longest = calculate_streak(dates, today=today)
        assert current == 3
        assert longest == 3

    def test_five_consecutive_ending_yesterday(self):
        today = date(2026, 2, 12)
        dates = [date(2026, 2, d) for d in range(7, 12)]  # 7,8,9,10,11
        current, longest = calculate_streak(dates, today=today)
        assert current == 5
        assert longest == 5


class TestGapInMiddle:
    def test_gap_breaks_current_streak(self):
        today = date(2026, 2, 12)
        # 3-day streak, gap, then 2-day ending today
        dates = [
            date(2026, 2, 5),
            date(2026, 2, 6),
            date(2026, 2, 7),
            # gap on 8-10
            date(2026, 2, 11),
            date(2026, 2, 12),
        ]
        current, longest = calculate_streak(dates, today=today)
        assert current == 2
        assert longest == 3

    def test_old_streak_longer_than_current(self):
        today = date(2026, 2, 12)
        dates = [
            date(2026, 2, 1),
            date(2026, 2, 2),
            date(2026, 2, 3),
            date(2026, 2, 4),
            date(2026, 2, 5),
            # gap
            date(2026, 2, 12),
        ]
        current, longest = calculate_streak(dates, today=today)
        assert current == 1
        assert longest == 5


class TestTodayNotInList:
    def test_streak_from_yesterday(self):
        today = date(2026, 2, 12)
        dates = [date(2026, 2, 10), date(2026, 2, 11)]
        current, longest = calculate_streak(dates, today=today)
        assert current == 2
        assert longest == 2

    def test_no_recent_activity(self):
        today = date(2026, 2, 12)
        dates = [date(2026, 1, 1), date(2026, 1, 2), date(2026, 1, 3)]
        current, longest = calculate_streak(dates, today=today)
        assert current == 0
        assert longest == 3


class TestMonthBoundary:
    def test_crossing_month_boundary(self):
        today = date(2026, 3, 2)
        dates = [date(2026, 2, 27), date(2026, 2, 28), date(2026, 3, 1), date(2026, 3, 2)]
        current, longest = calculate_streak(dates, today=today)
        assert current == 4
        assert longest == 4


class TestDuplicateDates:
    def test_duplicates_dont_inflate_streak(self):
        today = date(2026, 2, 12)
        dates = [
            date(2026, 2, 12),
            date(2026, 2, 12),
            date(2026, 2, 11),
            date(2026, 2, 11),
        ]
        current, longest = calculate_streak(dates, today=today)
        assert current == 2
        assert longest == 2
