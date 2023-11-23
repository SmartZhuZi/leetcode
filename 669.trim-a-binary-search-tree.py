#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        result = self.travelsal(root,low,high)
        return result
    def travelsal(self,root,low,high):
        if root is None:
            return None
        if root.val < low:
            right = self.travelsal(root.right,low,high)
            return right
        if root.val > high:
            left = self.travelsal(root.left,low,high)
            return left
        root.left = self.travelsal(root.left,low,high)
        root.right = self.travelsal(root.right,low,high)

        return root
            
# @lc code=end

