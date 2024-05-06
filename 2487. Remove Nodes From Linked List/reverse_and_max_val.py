"""
Reverse the list.
Now maintain a max_val seen so far.
Any node which is less than max_val, skip it.
Then reverse again and return.

O(n) time for 3 passes over the linked list.
O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        while head:
            nxt_tmp = head.next
            head.next = prev
            prev = head
            head = nxt_tmp
        
        sent_head = ListNode(0)
        sent_head.next = prev
        max_val = 0
        dummy = sent_head
        while dummy:
            if dummy.next:
                if dummy.next.val >= max_val:
                    max_val = dummy.next.val
                    dummy = dummy.next
                else:
                    dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        
        # reverse it again
        head = sent_head.next
        prev = None
        while head:
            nxt_tmp = head.next
            head.next = prev
            prev = head
            head = nxt_tmp
        
        return prev
