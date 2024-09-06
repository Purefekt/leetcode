"""
Simulation with 2 pointers.
One at current valid node and other at next valid node.

O(n) time.
O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = set(nums)

        sent_head = ListNode()
        sent_head.next = head

        cur = sent_head
        dummy = head

        while dummy:
            if dummy.val not in nums:
                cur.next = dummy
                dummy = dummy.next
                cur = cur.next
            else:
                dummy = dummy.next
        cur.next = None
        
        return sent_head.next
