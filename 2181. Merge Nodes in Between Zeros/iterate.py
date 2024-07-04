"""
Iterate through the input and track the sum of nodes between 2 zeros.

O(n) time.
O(1) space. not accounting for output list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        dummy = res

        cur = 0
        size = -1
        while head:
            if head.val == 0:
                size += 1
                dummy.val = cur
                dummy.next = ListNode()
                dummy = dummy.next
                cur = 0
            cur += head.val
            head = head.next
        
        # remove last node
        dummy = res
        for i in range(size):
            dummy = dummy.next
        dummy.next = None

        return res.next
        