#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        low = ListNode(val=0,next=head)
        current = head
        pre = None
        while current:
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        return pre

            
            
# @lc code=end

