from __future__ import annotations

import dataclasses as dtc
import re


@dtc.dataclass
class Timestamp:
    hours: int = 0
    minutes: int = 0
    seconds: int = 0

    def __post_init__(self):
        if self.seconds > 60:
            extra_min, self.seconds = divmod(self.seconds, 60)
            self.minutes += extra_min

        if self.minutes > 60:
            extra_hours, self.minutes = divmod(self.minutes, 60)
            self.hours += extra_hours

    @classmethod
    def from_str(cls, timestamp: str) -> Timestamp:
        try:
            hours = int(next(re.finditer(r"(\d+)h", timestamp)).group(1))
        except StopIteration:
            hours = 0

        try:
            minutes = int(next(re.finditer(r"(\d+)min", timestamp)).group(1))
        except StopIteration:
            minutes = 0

        try:
            seconds = int(next(re.finditer(r"(\d+)s", timestamp)).group(1))
        except StopIteration:
            seconds = 0

        return cls(hours=hours, minutes=minutes, seconds=seconds)

    @property
    def all_seconds(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def calculate_mean(self, nof_timestamps: int) -> Timestamp:
        return Timestamp(
            seconds=self.all_seconds // nof_timestamps
        )

    def __str__(self) -> str:
        if self.hours == 0:
            if self.minutes == 0:
                return f"{self.seconds}s"
            return f"{self.minutes}min {self.seconds}s"
        return f"{self.hours}h {self.minutes}min {self.seconds}s"

    def __add__(self, other: Timestamp | int) -> Timestamp | int:
        if isinstance(other, int):
            return self.all_seconds + other
        return Timestamp(
            hours=self.hours + other.hours,
            minutes=self.minutes + other.minutes,
            seconds=self.seconds + other.seconds,
        )

    def __radd__(self, other: Timestamp | int) -> Timestamp | int:
        return self + other

