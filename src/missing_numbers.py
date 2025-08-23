from unittest import TestCase


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_sum = 0
        total_sum = 0

        for i in range(0, len(nums)):
            nums_sum += nums[i]
            total_sum += i

        total_sum += len(nums)

        return total_sum - nums_sum


class Test(TestCase):
    def test_case_01(self):
        nums = [3, 0, 1]
        expected = 2

        self.assertEqual(expected, Solution().missingNumber(nums))

    def test_case_02(self):
        nums = [0, 1]
        expected = 2

        self.assertEqual(expected, Solution().missingNumber(nums))

    def test_case_03(self):
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        expected = 8

        self.assertEqual(expected, Solution().missingNumber(nums))
