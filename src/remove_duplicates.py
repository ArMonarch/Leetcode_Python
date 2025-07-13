import unittest

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index_i = 0

        for index_j in range(1, len(nums)):
            if nums[index_i] != nums[index_j]:
                index_i += 1
                nums[index_i] = nums[index_j]

        return index_i + 1

class Tests(unittest.TestCase):
    def test_case_01(self):
        nums = [1,1,2]
        expected = 2
        
        self.assertEqual(expected, Solution().removeDuplicates(nums))

    def test_case_02(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected = 5
        
        self.assertEqual(expected, Solution().removeDuplicates(nums))
