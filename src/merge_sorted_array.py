import unittest;

class Solution:
    def merge(self, nums_1: list[int], m: int, nums_2: list[int], n: int) -> None:
        midx = m - 1
        nidx = n - 1
        right = m + n - 1

        while nidx >= 0:
            if nums_2[nidx] >= nums_1[midx]:
                nums_1[right] = nums_2[nidx]
                nidx -= 1
            else:
                nums_1[right] = nums_1[midx]
                midx -= 1

            right -= 1

        return

class Tests(unittest.TestCase):
    def test_case_01(self):
        solution = Solution()

        nums_1 = [1,2,3,0,0,0]
        nums_2 = [2,5,6]

        expected = [1,2,2,3,5,6]

        solution.merge(nums_1, 3, nums_2, len(nums_2))
        self.assertEqual(nums_1, expected)

    def test_case_02(self):
        solution = Solution()

        nums_1 = [1]
        nums_2 = []

        expected = [1]

        solution.merge(nums_1, 3, nums_2, len(nums_2))
        self.assertEqual(nums_1, expected)
