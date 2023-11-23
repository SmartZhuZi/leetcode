#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        self.result = []
        used = [False] * len(nums)
        nums = sorted(nums)
        self.backtracking(nums, used)
        return self.result
    
    def backtracking(self, nums, used):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1] and used[i-1] == False:
                continue
            if used[i] == True:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used)
            used[i] = False
            self.path.pop()
        
# @lc code=end

