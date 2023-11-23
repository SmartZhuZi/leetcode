#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # print(people)
        # people.sort(key = lambda x: x[0])
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        result = []
        for i in range(len(people)):
            result.insert(people[i][1],people[i])
        # print(people)
        return(result)
            
# @lc code=end

