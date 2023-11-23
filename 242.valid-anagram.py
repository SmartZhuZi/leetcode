#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_record = [0] * 26
        for i in s:
            hash_record[ord(i) - ord('a')] += 1
        for i in t:
            hash_record[ord(i) - ord('a')] -= 1
        for i in hash_record:
            if i == 0:
                None
            else:return False
        return True
                
# @lc code=end

