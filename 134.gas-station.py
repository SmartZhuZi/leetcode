#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_sum = 0
        total_sum = 0
        start = 0
        for i in range(len(gas)):
            current_sum += (gas[i] - cost[i])
            total_sum += (gas[i] - cost[i])
            if current_sum < 0:
                start = i+1
                current_sum = 0
        if total_sum < 0:
            return -1
        else:return start
# @lc code=end

