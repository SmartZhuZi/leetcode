#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result = 1
        points.sort(key= lambda x: x[0])
        right_limit = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > points[i-1][1]:
                result += 1
            else:
                points[i][1] = min(points[i][1],points[i-1][1])
        return result

# @lc code=end

