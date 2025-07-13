import unittest

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()
    
        count = 0
        for char in string:
            if char != ' ':
                count += 1
            else:
                count = 0

        return count



class Tests(unittest.TestCase):
    def test_case_01(self):
        s = "Hello World"
        expected = 5

        self.assertEqual(expected, Solution().lengthOfLastWord(s))

    def test_case_02(self):
        s = "   fly me   to   the moon  "
        expected = 4

        self.assertEqual(expected, Solution().lengthOfLastWord(s))


    def test_case_03(self):
        s = "luffy is still joyboy"
        expected = 6

        self.assertEqual(expected, Solution().lengthOfLastWord(s))

