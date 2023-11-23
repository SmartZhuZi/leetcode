#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.path = []
        self.result = []
        self.backtracking(k,n,sum=0,start_index=1)
        return self.result
    
    def backtracking(self,k,n,sum,start_index):
        if sum > n:
            return
        if len(self.path) == k:
            if sum == n:
                self.result.append(self.path[:])
            return
        for i in range(start_index,10):
            self.path.append(i)
            sum += i
            self.backtracking(k,n,sum,i+1)
            sum -= i
            self.path.pop()

        
# @lc code=end

