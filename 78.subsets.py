#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backtracking(nums,0)
        return self.result

    def backtracking(self,nums,start_index):
        self.result.append(self.path[:])
        if start_index > len(nums):
            return
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums,i+1)
            self.path.pop()
            



# @lc code=end

