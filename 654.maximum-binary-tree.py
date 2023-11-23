#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maxindex = -1
        max = -1
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                maxindex = i
        left = nums[:maxindex]
        right = nums[maxindex+1:]
        root = TreeNode(nums[maxindex])
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        
        return root
# @lc code=end

