#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = 0
        right = len(nums)
        left = 0
        if target < nums[0] or target > nums[-1]:
            return -1
        while (left < right):
            middle = (left+right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            else:
                return middle
        return -1
# @lc code=end
