#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = collections.deque()
        queue.append(root)
        # new_tree_root = TreeNode()
        # new_current = new_tree_root
        while  queue:
            cur = queue.popleft()    
            cur.left,cur.right = cur.right,cur.left
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root

                
# @lc code=end

