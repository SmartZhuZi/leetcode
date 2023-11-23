#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_list =[0] * 26
        for i in magazine:
            hash_list[ord(i) - ord('a')] += 1
        for i in ransomNote:
            hash_list[ord(i) - ord('a')] -= 1
        for i in hash_list:
            if i < 0:
                return False
        return True
# @lc code=end

