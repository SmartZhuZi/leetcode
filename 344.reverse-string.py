#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s) - 1
        while low < high:
            temp = s[low]
            s[low] = s[high]
            s[high] = temp
            low += 1
            high -= 1
# @lc code=end

