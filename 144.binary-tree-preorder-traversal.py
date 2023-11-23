#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # 前序遍历
        # if not root:
        #     return []
        # left = self.preorderTraversal(root = root.left)
        # right = self.preorderTraversal(root = root.right)
        # result = [root.val] + left +  right
        # print(result)
        # return result
        if not root:
            return []
        print(root.val)
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left +right
        
     # @lc code=end

