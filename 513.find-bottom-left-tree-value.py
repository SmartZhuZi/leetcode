#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = -1
        self.value_left = None
        result = self.get_left(root,depth=0)
        # print(result)
        return self.value_left

    def get_left(self,root,depth):
        if not root.left and not root.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.value_left = root.val
                return
        if root.left:
            depth += 1
            self.get_left(root.left,depth)
            depth -= 1
        if root.right:
            depth += 1
            self.get_left(root.right,depth)
            depth -= 1



        # queue = collections.deque()
        # queue.append(root)
        # result = []
        # while queue:
        #     layer = []
        #     for _ in range(len(queue)):
        #         cur = queue.popleft()
        #         layer.append(cur.val)
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        #     result.append(layer)
        # return result[-1][0]


# @lc code=end

