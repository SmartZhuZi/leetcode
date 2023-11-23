#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x : x[0])
        result = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                result += 1
                intervals[i][1] = min(intervals[i][1],intervals[i-1][1])
        return result
            
# @lc code=end

