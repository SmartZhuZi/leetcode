#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        # print(freq)
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for key,value in count.items():
            freq[value].append(key)
        result = []
        # print(freq)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
# @lc code=end

