#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result =   float('-inf')
        count =  float('-inf')
        for i in range(len(nums)):
            if count < 0:
                count = 0
            count += nums[i]
            result = max(count,result)
        return result
            
# @lc code=end

