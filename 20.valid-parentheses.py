#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '{':
                stack.append('}')
            elif s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif len(stack) < 1 or stack[-1] != s[i]:
                return False
            else:
                stack.pop()
        if len(stack) > 0:
            return False 
        else:
            return True
            
# @lc code=end

