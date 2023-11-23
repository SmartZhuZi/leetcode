#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        # self.path.append(nums[0])
        self.backtracking(nums,0)
        return self.result
        # nums = sorted(nums)
    
    def backtracking(self,nums,start_index):
        if len(self.path) > 1:
            self.result.append(self.path[:])
        if start_index > len(nums):
            return
        used = set()
        for i in range(start_index,len(nums)):
            # print(nums[i])
            
            # if i> 0 and nums[i] == nums[i-1] and used[i-1] is False:
            #     continue
            if i > 0 and nums[i] in used:
                continue
            if  start_index > 0 and nums[i] >= self.path[-1]:
                used.add(nums[i])
                self.path.append(nums[i])
                self.backtracking(nums,i+1)
                self.path.pop()
            elif start_index == 0:
                used.add(nums[i])
                self.path.append(nums[i])
                self.backtracking(nums,i+1)
                self.path.pop()

            
                


# @lc code=end

