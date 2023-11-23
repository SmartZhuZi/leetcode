#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            # print(seen)
            if target - nums[i] in seen and seen[target-nums[i]] != i:
                    return [i,seen[target-nums[i]]]
            seen[nums[i]] = i


                
# @lc code=end

