#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = self.sum_left(root)
        return result

    def sum_left(self,root):
        if not root:
            return 0
        print(root.val)
        leftvalue = self.sum_left(root.left)
        if root.left and not root.left.left and not root.left.right:
            leftvalue = root.left.val
        rightvalue = self.sum_left(root.right)
        sum = leftvalue+rightvalue
        return sum
# @lc code=end

