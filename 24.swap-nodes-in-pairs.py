#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(val=0,next=head)
        current = dummy_head
        while current.next and current.next.next:
            node1 = current.next
            node2 = current.next.next


            node1.next = node2.next
            current.next = node2
            node2.next = node1

            
            current = node1

        return dummy_head.next
        
# @lc code=end

