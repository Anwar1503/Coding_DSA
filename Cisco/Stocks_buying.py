##https://leetcode.com/problems/best-time-to-buy-and-sell-stock/



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value  = prices[0]
        for price in prices:
            min_value = min(min_value,price)
            max_profit = max(max_profit,(price - min_value))
        return max_profit  