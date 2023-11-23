#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque

class Myqueue:
    def __init__(self) -> None:
        self.queue = deque()
    def pop(self,value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()
    def push(self,value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    def top(self):
        return self.queue[0]
    

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = Myqueue()
        result = []
        for i in range(0,k-1):
            queue.push(nums[i])
        for i in range(k-1,len(nums)):
            queue.pop(nums[i-k])
            queue.push(nums[i])
            result.append(queue.top())
        return result
    



# @lc code=end

