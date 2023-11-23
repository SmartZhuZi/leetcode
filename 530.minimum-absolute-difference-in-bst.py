#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.previous = None
        self.diff = float('inf')
        self.midtraversal(root)
        return self.diff
        
    def midtraversal(self,root):
        if not root:
            return
        left = self.midtraversal(root.left)
        if self.previous:
            temp = root.val - self.previous.val
            # print(temp)
            self.diff = min(temp,self.diff)
        self.previous = root
        right = self.midtraversal(root.right)
        

# @lc code=end

