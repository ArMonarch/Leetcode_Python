from unittest import TestCase

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map: dict[int, int] = dict()

        for (idx, num) in enumerate(nums):
            val = hash_map.get(target - num)
            if None != val:
                assert val != None
                return [val, idx]
            else:
                hash_map.update({num: idx})
    
        return []

class Tests(TestCase):
    def test_case_01(self) -> None:
        nums= [2,7,11,15]
        target = 9
        expected = [0, 1]

        self.assertEqual(expected, Solution().twoSum(nums, target))

    def test_case_02(self) -> None:
        nums= [3, 2, 4]
        target = 6
        expected = [1, 2]

        self.assertEqual(expected, Solution().twoSum(nums, target))

    def test_case_03(self) -> None:
        nums= [3, 3]
        target = 6
        expected = [0, 1]

        self.assertEqual(expected, Solution().twoSum(nums, target))
