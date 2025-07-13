import unittest

FIRST = int(0)
LAST = int(-1)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        index = 0
        while index < len(strs[FIRST]) and strs[FIRST][index] == strs[LAST][index]:
            index += 1

        return "" if index == 0 else strs[FIRST][0:index]

class Tests(unittest.TestCase):
    def test_case_01(self):
        strs = ["flower","flow","flight"]
        expected = "fl"

        self.assertEqual(expected, Solution().longestCommonPrefix(strs))

    def test_case_02(self):
        strs = ["dog","racecar","car"]
        expected = ""

        self.assertEqual(expected, Solution().longestCommonPrefix(strs))

    def test_case_03(self):
        strs = ["carrace","car"]
        expected = "car"

        self.assertEqual(expected, Solution().longestCommonPrefix(strs))
