#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                
                cur = queue.popleft()
                
                if cur:
                    level.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    level.append(None)

                
            low = 0
            high = len(level) -1
            while low < high:
                if level[low] != level[high]:
                    return False
                low += 1
                high -= 1            
        return True



# @lc code=end

