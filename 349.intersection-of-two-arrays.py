#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set()
        result = set()
        for i in nums1:
            nums1_set.add(i)
        for i in nums2:
            if i in nums1_set:
                result.add(i)
        return result
# @lc code=end

