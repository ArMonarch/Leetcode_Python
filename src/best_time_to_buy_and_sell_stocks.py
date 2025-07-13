import unittest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices:
            if buy > price:
                buy = price

            if profit < (price - buy):
                profit = price - buy

        return profit


class Tests(unittest.TestCase):
    def test_case_01(self):
        prices = [7,1,5,3,6,4]
        expected = 5

        self.assertEqual(expected, Solution().maxProfit(prices))
    
    def test_case_02(self):
        prices = [7,6,4,3,1]
        expected = 0

        self.assertEqual(expected, Solution().maxProfit(prices))
