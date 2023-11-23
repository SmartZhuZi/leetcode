#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cover = 0
        target = len(nums) - 1
        i = 0
        result = 0
        while i <= cover: 
            for i in range(i, cover + 1):
                cover = max(nums[i]+i, cover)
                if cover >= target:
                    return result + 1
            result += 1
        
# @lc code=end

