#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if flag := self.get_hight(root=root) != -1:
            return True
        else:return False 
        
    def get_hight(self,root) -> int:
        if not root:return 0
        left_hight = self.get_hight(root.left)
        if left_hight == -1:
            return -1
        right_hight = self.get_hight(root.right)
        if right_hight == -1:
            return -1
        # print(left_hight,right_hight)
        if abs(left_hight - right_hight) > 1:
            return -1
        else: return 1 + max(left_hight,right_hight)

# @lc code=end

