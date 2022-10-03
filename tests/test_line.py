from unittest import TestCase

from lineswitch.core import Interchange, Line, count_feasible_trips


class TestInterChange(TestCase):
    def test_earliest_reachable(self):
        t_start = 10
        l = Line(9.25, 42, 2)
        self.assertEqual(l.earliest_reachable(t_start), 10.25)

    def test_count_trips(self):
        t_start = 9
        t_end = 11
        line_1 = Line(9, 0.5, 2)
        self.assertEqual(line_1.count_trips(t_start, t_end), 4)

        line_2 = Line(9.25, 0.5, 2)
        self.assertEqual(line_2.count_trips(t_start, t_end), 3)

        total_trips = count_feasible_trips(t_start, t_end, [line_1, line_2])
        self.assertEqual(total_trips, 7)

    def test_two_lines(self):
        service_start = 9
        service_end = 10

        l1 = Line(9, 0.5, 2)
        l2 = Line(9.25, 0.5, 2)

        i1 = Interchange(0.1, l1, True, l2, False)
