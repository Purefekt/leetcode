"""
Get length of the linked list. Then remove the node which is length - n
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # add dummy to the start to avoid edge cases
        dummy = ListNode()
        dummy.next = head
        
        # get length of dummy list
        length = 0
        curr = dummy
        while curr:
            curr = curr.next
            length += 1
        
        # get the node right before the node which needs to be removed
        nth_index = 1
        target_index = length - n
        curr = dummy
        while nth_index != target_index:
            curr = curr.next
            nth_index += 1
        
        # point the next of this node to its next.next
        curr.next = curr.next.next
        
        return dummy.next
    