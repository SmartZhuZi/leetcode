#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        result = []
        intervals = sorted(intervals, key= lambda x : x[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= intervals[i-1][1]:
                left = min(intervals[i-1][0],intervals[i][0])
                right = max(intervals[i][1],intervals[i-1][1])
                intervals[i][0] = left
                intervals[i][1] = right
            else:
                result.append(intervals[i-1])
        result.append(intervals[-1])
        return result

# @lc code=end

