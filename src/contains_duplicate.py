from unittest import TestCase

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_set: set[int] = set()
        for num in nums:
            if num in hash_set:
                return True
            else: 
                hash_set.add(num)

        return False

class Tests(TestCase):
    def  test_case_01(self):
        nums = [1, 2, 3, 1]
        expected = True

        self.assertEqual(expected, Solution().containsDuplicate(nums))

    def  test_case_02(self):
        nums = [1, 2, 3, 4]
        expected = False

        self.assertEqual(expected, Solution().containsDuplicate(nums))

    def  test_case_03(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected = True

        self.assertEqual(expected, Solution().containsDuplicate(nums))
