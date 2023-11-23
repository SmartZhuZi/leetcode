#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.count = 0
        self.max_count = 0
        self.pre = None
        self.result = []
        self.search(root)
        return self.result
    
    def search(self,root):
        if not root:
            return
        self.search(root.left)
        if self.pre is None:
            self.count = 1
        elif root.val == self.pre.val:
            self.count += 1
        else:
            self.count = 1
        self.pre = root
        
        if self.count == self.max_count:
            self.result.append(root.val)
        
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [root.val]
        
        self.search(root.right)
        
        return
# @lc code=end