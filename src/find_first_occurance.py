import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for index in range(0, len(haystack) - len(needle) + 1):
            if haystack[index:index + len(needle)] == needle:
                return index

        return -1

class Tests(unittest.TestCase):
    def test_case_01(self):
        haystack = "sadbutsad"
        needle = "sad"

        expected = 0

        self.assertEqual(expected, Solution().strStr(haystack, needle))

    def test_case_02(self):
        haystack = "leetcode"
        needle = "leeto"

        expected = -1

        self.assertEqual(expected, Solution().strStr(haystack, needle))
