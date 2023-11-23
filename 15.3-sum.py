#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)):
            print(i)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums) - 1
            while (left<right):
                sum =  nums[i] + nums[left] + nums[right]
                # print('i',nums[i],i,'left',nums[left],left,'right',nums[right],right,'sum',sum)
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    # print(result)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                    left += 1
        return result


# @lc code=end

