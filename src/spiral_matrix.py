from unittest import TestCase


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result: list[int] = []

        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        
        while left <= right and top <= bottom:

            # movement from left to right in matrix[top][?]
            for i in range(left, right + 1):
                val = matrix[top][i]
                result.append(val)
            top += 1

            # movement form top to bottom in matrix[?][right]
            for j in range(top, bottom + 1):
                val = matrix[j][right]
                result.append(val)
            right -= 1

            # movement form right to left in matrix[bottom][?]
            # only if left < right
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    val = matrix[bottom][k]
                    result.append(val)
                bottom -= 1

            # movement form bottom to top in matrix[?][?]
            # only if top < bottom
            if left <= right:
                for k in range(bottom, top - 1, -1):
                    val = matrix[k][left]
                    result.append(val)
                left += 1

        return result

class Tests(TestCase):
    def test_case_01(self) -> None:
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]

        result = Solution().spiralOrder(matrix)
        self.assertEqual(len(expected), len(result))
        self.assertEqual(expected, result)

    def test_case_02(self) -> None:
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]

        result = Solution().spiralOrder(matrix)
        self.assertEqual(len(expected), len(result))
        self.assertEqual(expected, result)
