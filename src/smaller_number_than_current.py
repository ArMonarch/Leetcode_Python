from unittest import TestCase


class Solution:

    # Method 01: Brute Force
    # def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    #     n = len(nums)
    #     result: list[int] = [0 for _ in range(n)]
    #     for i in range(n):
    #         for j in range(n):
    #             if nums[i] > nums[j]:
    #                 result[i]  += 1
    #     return result

    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        bucket = [0] * 102

        for num in nums:
            bucket[num + 1] += 1
        
        for i in range(1, 100 + 2):
            bucket[i] += bucket[i - 1]

        return [bucket[num] for num in nums]

class Tests(TestCase):
    def test_case_01(self) -> None:
        nums = [8,1,2,2,3]
        expected = [4,0,1,1,3]

        self.assertEqual(expected, Solution().smallerNumbersThanCurrent(nums))

    def test_case_02(self) -> None:
        nums = [6,5,4,8]
        expected = [2,1,0,3]

        self.assertEqual(expected, Solution().smallerNumbersThanCurrent(nums))
        
    def test_case_03(self) -> None:
        nums = [7, 7, 7, 7]
        expected = [0, 0, 0, 0]

        self.assertEqual(expected, Solution().smallerNumbersThanCurrent(nums))

    def test_case_04(self) -> None:
        nums = [5,0,10,0,10,6]
        expected = [2,0,4,0,4,3]

        self.assertEqual(expected, Solution().smallerNumbersThanCurrent(nums))
