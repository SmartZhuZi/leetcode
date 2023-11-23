#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # # 第一步: 特殊情况讨论: 树为空. (递归终止条件)
        if not postorder:
            return None
        # 第二步: 后序遍历的最后一个就是当前的中间节点.
        mid = postorder[-1]
        root = TreeNode(mid)
        # 第三步: 找切割点.
        split_idx = inorder.index(mid)
        # print(split_idx)
        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        left = inorder[:split_idx]
        right = inorder[split_idx + 1:]
        # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
        # ⭐️ 重点1: 中序数组大小一定跟后序数组大小是相同的.
        p_left = postorder[:len(left)]
        p_right = postorder[len(left):len(postorder) - 1]
        # 第六步: 递归
        root.left = self.buildTree(left,p_left)
        root.right = self.buildTree(right,p_right)
        
        return root
        # 第七步: 返回答案
# @lc code=end

