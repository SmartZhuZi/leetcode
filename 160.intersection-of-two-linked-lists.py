#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current_a = headA
        current_b = headB
        len_a, len_b = 0,0
        while current_a:
            current_a = current_a.next
            len_a += 1
        while current_b:
            current_b = current_b.next
            len_b += 1
        current_a = headA
        current_b = headB
        if len_a > len_b:
            for i in range(len_a -len_b):
                current_a = current_a.next
        else:
            for i in range(len_b - len_a):
                current_b = current_b.next
        while current_a:
            if current_b == current_a:
                return current_a
            else:
                current_a = current_a.next
                current_b = current_b.next
        return None            
# @lc code=end

