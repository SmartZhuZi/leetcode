#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = self.traversal(root,val)
        if cur:
            return cur
        else:return root
    def traversal(self,root,val):
        if not root:
            root= TreeNode(val)
            return root
        if val < root.val and root.left == None:
            root.left = TreeNode(val)
        elif val > root.val and root.right == None:
            root.right = TreeNode(val)
        if val < root.val:
            left = self.traversal(root.left,val)
        if val > root.val:
            right = self.traversal(root.right,val)
# @lc code=end

