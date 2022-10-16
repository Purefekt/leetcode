"""
Initialize a new linked list and use dummy to update it
Run while loop till either l1 or l2 is not None
get the single digit val, if its greater than 9, then subtract 10
update this val to the new linked list. Here if there is a carry and the val is 9, then we need to maintain carry as 1 and set the value to 0. If there is a carry and the val is <= 8, then add the carry and update the node and reset carry to 0
Once updated the node, check for carry for the next iteration.
Once the while loop ends, check if there is a remaining carry, if yes then add it to the linkedlist and return.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        dummy = head
        
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            if val1 + val2 > 9:
                val = val1 + val2 -10
            else:
                val = val1 + val2
            
            if carry == 1:
                val = val + carry
                if val > 9:
                    val = val-10
                    carry = 1
                else:
                    carry = 0
                dummy.next = ListNode(val)
            else:
                dummy.next = ListNode(val)
            
            if val1 + val2 > 9:
                carry = 1
            
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry == 1:
            dummy.next = ListNode(1)
            
        return head.next