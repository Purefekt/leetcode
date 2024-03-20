"""
Add sent head to avoid edge cases.
Get the pointer to the node just before a in list1 and pointer to the node just after b in list2.
Point a_prev to list2.
Get the pointer to the last node in list2.
Point tail_2 to b_next.
return sent.next.

O(n+m) time with multiple passes.
O(1) space since we are only using pointers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        sent = ListNode()
        sent.next = list1

        # get pointer to node before a and pointer to node after b
        a_prev = sent
        for _ in range(a):
            a_prev = a_prev.next
        b_next = sent
        for _ in range(b+2):
            b_next = b_next.next
        
        a_prev.next = list2

        # get pointer to last node in list2
        tail_2 = list2
        while tail_2.next:
            tail_2 = tail_2.next
        
        tail_2.next = b_next

        return sent.next
