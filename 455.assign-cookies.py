#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        result = 0
        index = len(s) -1
        for i in range(len(g)-1,-1,-1):
            if index >= 0 and g[i] <= s[index]:
                result += 1
                index -= 1
        return result
        
             
# @lc code=end

