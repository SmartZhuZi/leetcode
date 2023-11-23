#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # binary search tree 中序有序
        result = self.midtraversal(root)
        print(result)
        temp = -float('inf')
        for i in result:
            if i > temp:
                temp = i
            else:
                return False
        return True
    def midtraversal(self,root):
        if not root:
            return []
        left = self.midtraversal(root.left)
        right = self.midtraversal(root.right)
        result =  left + [root.val] + right
        return result
# @lc code=end

