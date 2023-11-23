#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return (self.traversal(root,key))
    
    def traversal(self,cur,key):
        if not cur:
            return None
        if cur.val == key:
            if cur.left is None and cur.right is None:
                return None
            if cur.left and cur.right is None:
                return cur.left
            if cur.left is None and cur.right:
                return cur.right
            elif cur.left is not None and cur.right is not None:
                temp = cur.right
                while temp.left is not None:
                    temp = temp.left
                temp.left = cur.left
                return cur.right
        if key > cur.val:
            cur.right = self.traversal(cur.right,key)
        elif key < cur.val:
            cur.left = self.traversal(cur.left,key)
        return cur
            
# @lc code=end

