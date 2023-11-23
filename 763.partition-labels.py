#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}
        for i,value in enumerate(s):
            last_occurence[value] = i
        print(last_occurence)
        result = []
        max_reach = 0
        now = 0
        for i in range(len(s)):
            max_reach = max(last_occurence[s[i]],max_reach)
            if i == max_reach:
                result.append(max_reach - now + 1)
                now = i + 1
        return result
# @lc code=end

