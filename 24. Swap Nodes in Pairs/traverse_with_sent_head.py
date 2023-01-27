"""
Use a sentinel node. Start from this and run a loop till dummy.next and dummy.next.next are not None
In each iteration, set a pointer to the next node, next.next node and next.next.next node (the last one can be None and that is valid)
Set dummy to next.next pointer, set dummy.next to next pointer and set dummy.next.next.next to next.next.next pointer
Now move dummy 2 positions to next.next

O(n) time to go over all nodes once
O(1) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        
        sent = ListNode(0, head)

        dummy = sent
        while dummy.next and dummy.next.next:
            d_next_next_next = dummy.next.next.next
            d_next_next = dummy.next.next
            d_next = dummy.next

            dummy.next = d_next_next
            dummy.next.next = d_next
            dummy.next.next.next = d_next_next_next

            dummy = dummy.next.next
        
        return sent.next
        