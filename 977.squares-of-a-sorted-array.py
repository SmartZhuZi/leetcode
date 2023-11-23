#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        low,high = 0,length-1
        result,key = [0] * length,length-1
        
        for i in range(length):
            if nums[low] ** 2 > nums[high] ** 2:
                result[key] = nums[low] ** 2
                key -= 1
                low += 1
            else:
                result[key] = nums[high] ** 2
                key -= 1
                high -= 1
        return result
            
        # return nums
# @lc code=end

