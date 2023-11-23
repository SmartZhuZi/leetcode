#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre_diff = 0
        current_diff = 0
        last = None
        result = 1
        if len(nums) == 1:
            return len(nums)
        for i in range(len(nums)):
            if last != None:
                current_diff = nums[i] - last
            if current_diff > 0 and pre_diff <= 0:
                result += 1
                pre_diff = current_diff 
            elif current_diff < 0 and pre_diff >= 0:
                result += 1
                pre_diff = current_diff 
            last = nums[i]
        return result

# @lc code=end

