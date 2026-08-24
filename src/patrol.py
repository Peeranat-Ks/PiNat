"""Patrol/rest duty cycle and restricted-hours logic.

Kept separate from main.py so the scheduling rules (when the robot is
actively patrolling vs resting, and when alerts are allowed) are easy to
read, test, and adjust independently of the camera/detection loop.
"""

import time
from datetime import datetime


class PatrolScheduler:
    def __init__(self, patrol_minutes: int, rest_minutes: int):
        self.patrol_minutes = patrol_minutes
        self.rest_minutes = rest_minutes
        self._phase_started_at = time.monotonic()
        self.resting = False

    def update_intervals(self, patrol_minutes: int, rest_minutes: int):
        self.patrol_minutes = patrol_minutes
        self.rest_minutes = rest_minutes

    def tick(self) -> bool:
        """Advance the duty cycle if the current phase has elapsed.
        Returns True if the robot is currently resting."""
        phase_length_minutes = self.rest_minutes if self.resting else self.patrol_minutes
        elapsed_minutes = (time.monotonic() - self._phase_started_at) / 60.0

        if phase_length_minutes > 0 and elapsed_minutes >= phase_length_minutes:
            self.resting = not self.resting
            self._phase_started_at = time.monotonic()

        return self.resting


def within_restricted_hours(start_hour: int, end_hour: int, always_alert: bool) -> bool:
    if always_alert:
        return True

    hour = datetime.now().hour
    if start_hour == end_hour:
        return True  # 24-hour patrol window
    if start_hour < end_hour:
        return start_hour <= hour < end_hour
    return hour >= start_hour or hour < end_hour  # wraps past midnight, e.g. 22 -> 6
