#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.map = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        self.result = []
        self.path = ''
        if len(digits) == 0:
            return self.result
        # print(self.map[2])
        self.backtracking(digits,0)
        return self.result
    
    def backtracking(self,digits,index):
        print(index,len(digits))
        if index == len(digits):
            # print(self.path)
            self.result.append(self.path[:])
            return
        order = int(digits[index])
        search_str = self.map[order]
        # print(search_str)
        for i in search_str:
            self.path += i
            self.backtracking(digits,index+1)
            self.path = self.path[:-1]

# @lc code=end

