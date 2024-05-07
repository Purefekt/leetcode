"""
Cannot store as a string since string to int conversion is capped.
Reverse the list.
Go through it and double each node, taking into account carry.
Re reverse the list.
If carry == 0, this is the result, else add a new head with value carry and return that.

O(n) time for 3 total passes over the list.
O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # reverse and double
        prev = None
        while head:
            nxt_tmp = head.next
            head.next = prev
            prev = head
            head = nxt_tmp
        
        carry = 0
        dummy = prev
        while dummy:
            double_val = (dummy.val * 2) + carry
            dummy.val = double_val % 10
            if double_val > 9:
                carry = double_val // 10
            else:
                carry = 0
            dummy = dummy.next
        
        # reverse again
        head = prev
        prev = None
        while head:
            nxt_tmp = head.next
            head.next = prev
            prev = head
            head = nxt_tmp
        
        if carry > 0:
            new_head = ListNode(carry)
            new_head.next = prev
            return new_head
        return prev
        