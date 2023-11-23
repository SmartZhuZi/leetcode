#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        self.result = []
        used = [False] * len(nums)
        nums = sorted(nums).copy()
        self.backtracking(nums=nums,used=used,startindex=0)
        return self.result
    
    def backtracking(self, nums, used,startindex):
        self.result.append(self.path[:])
        if startindex >= len(nums):
            return
        for i in range(startindex,len(nums)):
            if i> 0 and used[i-1] is False and nums[i] == nums[i-1]:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums,used,i+1)
            used[i] = False
            self.path.pop()
# @lc code=end

