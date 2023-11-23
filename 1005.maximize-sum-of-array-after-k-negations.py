#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key= lambda x:abs(x), reverse = True)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
            if k == 0:
                break
        while k > 0:
            nums[-1] = -nums[-1]
            k -= 1
        result = sum(nums)
        return result
# @lc code=end

