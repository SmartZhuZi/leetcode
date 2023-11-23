#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.path = []
        # self.used = [False] * len(candidates)
        used = [False] * len(candidates)
        candidates = sorted(candidates)
        self.backtracking(candidates,target,0,0,used)
        return self.result
    def backtracking(self,candidates,target,sum,star_index,used):
        if sum == target:
            self.result.append(self.path[:])
            return
        for i in range(star_index,len(candidates)):
            if sum + candidates[i] > target:
                return
            if i > star_index and candidates[i] == candidates[i-1] and used[i-1] is False:
                continue
            self.path.append(candidates[i])
            sum += candidates[i]
            used[i] = True
            self.backtracking(candidates,target,sum,star_index=i+1,used = used)
            used[i] = False
            sum -= candidates[i]
            self.path.pop()

# @lc code=end

