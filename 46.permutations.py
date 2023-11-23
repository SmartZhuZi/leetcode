#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        self.result = []
        used = [False] * len(nums)
        self.backtracking(nums,used)
        return self.result
    
    def backtracking(self,nums,used):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        for i in range(len(nums)):
            if used[i] is True:
                continue
            self.path.append(nums[i])
            used[i] = True
            self.backtracking(nums,used)
            used[i] = False
            self.path.pop()
# @lc code=end

