#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        last_day = None
        for i in range(len(prices)):
            if last_day is not None:
                if prices[i] - last_day > 0:
                    profit += prices[i] - last_day
            last_day = prices[i]
        return profit
# @lc code=end

