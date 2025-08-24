from unittest import TestCase


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        full_array: set[int] = set(nums)
        result: list[int] = []

        for idx in range(1, len(nums) + 1):
            if idx not in full_array:
                result.append(idx)

        return result

class Tests(TestCase):
    def test_case_01(self):
        nums = [4,3,2,7,8,2,3,1]
        expected = [5, 6]

        self.assertEqual(expected, Solution().findDisappearedNumbers(nums))

    def test_case_02(self):
        nums = [1,1]
        expected = [2]

        self.assertEqual(expected, Solution().findDisappearedNumbers(nums))

    def test_case_03(self):
        nums = [1,2,6,4,1,2]
        expected = [3,5]

        self.assertEqual(expected, Solution().findDisappearedNumbers(nums))

