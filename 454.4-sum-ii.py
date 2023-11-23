#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_a1_a2 = {}
        # sum_a3_a4 = {}
        count = 0
        for i in nums1:
            for j in nums2:
                sum = i +j
                if sum in sum_a1_a2.keys():
                    sum_a1_a2[sum] += 1
                else:
                    sum_a1_a2[sum] = 1
                
        for i in nums3:
            for j in nums4:
                diff = 0-(i+j)
                if diff in sum_a1_a2.keys():
                    count += sum_a1_a2[diff]
        return count
# @lc code=end

