from dataclasses import dataclass
from math import ceil
from typing import Iterable, Set


@dataclass
class Line:
    start: float
    duration: float
    period: float

    def earliest_reachable(self, t_start):
        if t_start <= self.start:
            return self.start

        runs_before_start = ceil((t_start - self.start) * self.period)
        return self.start + runs_before_start / self.period

    def count_trips(self, t_start, t_end):
        t_start = self.earliest_reachable(t_start)
        return (t_end - t_start) // self.duration

    @property
    def starts_every(self):
        return 1 / self.period


@dataclass
class Interchange:
    duration: float
    line_1: Line
    start_1: bool
    line_2: Line
    start_2: bool

def count_feasible_trips(t_start: float, t_end: float, lines: Iterable[Line]):
    return sum(line.count_trips(t_start, t_end) for line in lines)


def solve_greedy(t_start: float, t_end: float, lines: Set[Line], Set[Interchange]) -> NoneType:
    pass
