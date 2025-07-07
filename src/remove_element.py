import unittest

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        index_i = 0

        for index_j in range(0, len(nums)):
            if nums[index_j] != val:
                # nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
                nums[index_i] = nums[index_j]
                index_i += 1

        return index_i


class Tests(unittest.TestCase):
    def test_case_01(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected = 2

        self.assertEqual(expected, Solution().removeElement(nums, val), "Not Equal")

    def test_case_02(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        expected = 5

        self.assertEqual(expected, Solution().removeElement(nums, val), "Not Equal")
