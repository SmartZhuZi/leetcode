#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.path = []
        self.trackback(candidates,target,sum=0,start_index=0)
        return self.result
    
    def trackback(self,candidates,target,sum,start_index):
        if sum > target:
            return
        if sum == target:
            self.result.append(self.path[:])
            return
        for i in range(start_index,len(candidates)):
            self.path.append(candidates[i])
            sum += candidates[i]
            self.trackback(candidates,target,sum,i)
            sum -= candidates[i]
            self.path.pop()
            
# @lc code=end

