"""
Connect the tail of the list to the head to form a circular list
Now the new head will be at position n-k and new tail will be just behind it at n-k-1
Run for loops for both to shift the pointers to the correct node and then set the new_tail.next to None

O(n) time to go over all nodes
O(1) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return
        
        n = 0
        dummy = head
        while dummy.next:
            n += 1
            dummy = dummy.next
        n += 1
        dummy.next = head

        # truncate k
        k %= n

        # new head will be at n - k
        new_head = head
        for _ in range(n-k):
            new_head = new_head.next
        
        # new tail will be 1 behind new head. Set it to None
        new_tail = head
        for _ in range(n-k-1):
            new_tail = new_tail.next
        new_tail.next = None

        return new_head
