#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        else:
            result = self.get_path(root,targetSum - root.val)
        return result
        
    
    def get_path(self,root,sum):
        if not root.left and not root.right and sum == 0:
            return True
        if not root.left and not root.right:
            return False
        if root.left:
            sum -= root.left.val
            result = self.get_path(root.left,sum)
            if result == True:
                return True
            else: sum += root.left.val
        if root.right:
            sum -= root.right.val
            result = self.get_path(root.right,sum)
            if result == True:
                return True
            else: sum += root.right.val
        return False
# @lc code=end

