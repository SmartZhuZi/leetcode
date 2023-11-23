#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
        result = self.traversal(root,p,q)
        return result
    
    def traversal(self,cur,p,q):
        if cur is None:
            return cur
                                                          # 中
        if cur.val > p.val and cur.val > q.val:           # 左
            left = self.traversal(cur.left, p, q)
            if left is not None:
                return left

        if cur.val < p.val and cur.val < q.val:           # 右
            right = self.traversal(cur.right, p, q)
            if right is not None:
                return right

        return cur

        

# @lc code=end

