#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # slide window
        left,right = 0,0
        result_length = float('inf')
        temp_sum = 0
        while right < len(nums):
            temp_sum += nums[right]
            while temp_sum >= target:
                result_length = min(result_length, right - left+1)
                temp_sum -= nums[left]
                left +=1
            right +=1 

        return result_length if result_length != float('inf') else 0

# @lc code=end

