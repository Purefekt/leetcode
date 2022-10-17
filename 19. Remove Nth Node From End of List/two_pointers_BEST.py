"""
TWO_POINTER - ONE PASS
Add a dummy node to the start of head to avoid edge cases
set a slow and fast pointer. Move the fast pointer to n+1 position
Now move slow and fast by 1 till fast is None.
At this point slow pointer will be at the node just before the node to remove. Set the next node of slow to next.next
return dummy.next (since the first node was the empty dummy node)

O(L) time. where L is the length of the linked list. We make one pass over all the nodes in L
O(1) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        # move fast to n+1
        for i in range(n+1):
            fast = fast.next
        
        # move both by 1 till fast is none
        while fast:
            slow = slow.next
            fast = fast.next
        
        # skip the next element to slow
        slow.next = slow.next.next
        
        return dummy.next
    