#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.path = []
        self.result = []
        self.backtracking(s,0)
        return self.result
        
    def backtracking(self,s,starindex):
        if starindex>= len(s):
            self.result.append(self.path[:])
            return
        for i in range(starindex,len(s)):
            temp = s[starindex:i+1]
            if self.is_palindrome(temp) is True:
                self.path.append(temp)
                self.backtracking(s,i+1)
                self.path.pop()
    
    def is_palindrome(self,string):
        low,high = 0, len(string) - 1
        while low < high:
            if string[low] == string[high]:
                low += 1
                high -= 1
            else: return False
        return True    
# @lc code=end

