#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0
        self.addTree(root)
        return root
    def addTree(self,root):
        if not root:
            return
        right = self.addTree(root.right)
        root.val += self.pre
        self.pre = root.val
        left = self.addTree(root.left)
# @lc code=end

