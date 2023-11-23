#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = self.posttravesal(root,p,q)
        # print(result)
        return result
    
    def posttravesal(self,root,p,q):
        if root is None:
            return root
        if root == p or root == q:
            return root
        left = self.posttravesal(root.left,p,q)
        right = self.posttravesal(root.right,p,q)
        if left and right:
            return root
        if not left and right:
            return right
        else:
            return left
# @lc code=end

