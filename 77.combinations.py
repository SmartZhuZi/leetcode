#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.path = []
        self.result = []
        self.backtracking(n,k,1)
        return self.result

    def backtracking(self,nums,k,start_index):
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        for i in range(start_index, nums+1):
            # print (i)
            # print(self.path)
            self.path.append(i)
            self.backtracking(nums,k,i+1)
            self.path.pop()

        
# @lc code=end
