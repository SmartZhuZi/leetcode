#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = len(nums) - 1
        max_reach = 0
        i = 0
        while i <= max_reach:
            max_reach = max(max_reach,nums[i] + i)
            i += 1
            if max_reach >= steps:
                return True
        return False

# @lc code=end

