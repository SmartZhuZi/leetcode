#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                temp = stack[-1]
                if i == temp:
                    stack.pop()
                else:
                    stack.append(i)
        result = ''
        for i in stack:
            result+=i
        return result                
# @lc code=end

