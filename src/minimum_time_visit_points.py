from unittest import TestCase


class Solution:

    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        time = 0
        n = len(points)

        for i in range(1, n):
            pointA = points[i - 1]
            pointB = points[i]

            dx = abs(pointB[0] - pointA[0])
            dy = abs(pointB[1] - pointA[1])

            time += max(dx, dy)

        return time

class Tests(TestCase):
    def test_case_01(self) -> None:
        points = [[1,1],[3,4],[-1,0]]
        expected = 7

        self.assertEqual(expected, Solution().minTimeToVisitAllPoints(points))

    def test_case_02(self) -> None:
        points = [[3,2],[-2,2]]
        expected = 5

        self.assertEqual(expected, Solution().minTimeToVisitAllPoints(points))
