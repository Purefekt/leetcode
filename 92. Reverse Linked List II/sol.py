"""
Get the pointer to the node just before the one to reverse
Get the pointer to the node after the one to reverse
Use a sentinal head to avoid edge cases
Reverse the given nodes
Attach the left node to the head of the reverse list and the tail of it to the right node

O(n) time to go over all nodes atleast once in worst case
O(1) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # add sent head to linkedlist
        sent = ListNode()
        sent.next = head

        # get node left of the window
        left_node = sent
        for _ in range(left-1):
            left_node = left_node.next
        
        # get node to the right of the window
        right_node = sent
        for _ in range(right+1):
            right_node = right_node.next
        
        # reverse the given part
        prev = None
        left_p = left_node.next
        
        for _ in range(right-left+1):
            next_tmp = left_p.next
            left_p.next = prev
            prev = left_p
            left_p = next_tmp
        
        # get the tail of the reversed list
        tail = prev
        while tail.next:
            tail = tail.next
        
        # connect left_node to head of reversed list(prev) and right_node to tail
        left_node.next = prev
        tail.next = right_node

        return sent.next
