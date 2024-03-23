#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(str.lower(s).split())
        for i in string.punctuation:
            s = s.replace(i,'')
        low = 0
        high = len(s)-1
        for _ in s:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
# @lc code=end

