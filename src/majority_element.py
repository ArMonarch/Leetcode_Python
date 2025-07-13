import unittest

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        (num, count) = (nums[0], 1)
        for index in range(1, len(nums)):
            if count == 0:
                num = nums[index]

            if num != nums[index]:
                count -= 1
            else:
                count += 1

        return num

class Tests(unittest.TestCase):
    def test_case_01(self):
        nums = [3,2,3]
        expected = 3

        self.assertEqual(expected, Solution().majorityElement(nums))

    def test_case_02(self):
        nums = [2,2,1,1,1,2,2]
        expected = 2

        self.assertEqual(expected, Solution().majorityElement(nums))

    def test_case_03(self):
        nums = [0]
        expected = 0

        self.assertEqual(expected, Solution().majorityElement(nums))

    def test_case_04(self):
        nums = [6,5,5]
        expected = 5

        self.assertEqual(expected, Solution().majorityElement(nums))
