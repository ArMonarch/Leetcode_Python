import unittest


class Solution:
    def romanToInt(self, s:str) -> int:
        if len(s) == 0:
            return 0
        
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        integer = 0
        for index in range(0, len(s) - 1):
            if roman.get(s[index], 0) < roman.get(s[index + 1], 0):
                integer -= roman.get(s[index], 0)
            else:
                integer += roman.get(s[index], 0)
        integer += roman.get(s[-1], 0)
            
        return integer

class Tests(unittest.TestCase):
    def test_case_01(self):
        s = "III"
        expected = 3

        self.assertEqual(expected, Solution().romanToInt(s))

    def test_case_02(self):
        s = "LVIII"
        expected = 58

        self.assertEqual(expected, Solution().romanToInt(s))

    def test_case_03(self):
        s = "MCMXCIV"
        expected = 1994

        self.assertEqual(expected, Solution().romanToInt(s))
