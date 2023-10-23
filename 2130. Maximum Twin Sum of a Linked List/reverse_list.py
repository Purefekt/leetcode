"""
Reverse the second half of the list in place.
Now calculate twin sum using 2 pointers, first starts at head and second starts at head of reversed list.
Return max sum.

O(n) time. n time to find n in one pass and n//2 time to find max sum.
O(1) space since everything is in place.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # find n
        n = 0
        dummy = head
        while dummy:
            n += 1
            dummy = dummy.next
        
        # flip list from n//2 th node
        i = 0
        flip_head = head
        for _ in range(n//2):
            flip_head = flip_head.next

        # reverse
        prev = None
        while flip_head:
            next_tmp = flip_head.next
            flip_head.next = prev
            prev = flip_head
            flip_head = next_tmp
        
        # iterate n//2 times from head and prev. Prev is head of reversed list
        res = 0
        for _ in range(n//2):
            res = max(res, head.val + prev.val)
            head = head.next
            prev = prev.next

        return res 