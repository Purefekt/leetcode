"""
Use math.gcd to get gcd of two integers.
Iterate through the list and keep adding these nodes.

O(n) time.
O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = head
        while dummy.next:
            gcd = math.gcd(dummy.val, dummy.next.val)
            gcd_node = ListNode(gcd)
            nxt_tmp = dummy.next
            dummy.next = gcd_node
            gcd_node.next = nxt_tmp
            dummy = nxt_tmp
        
        return head
