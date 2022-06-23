"""
Reverse the linked list.
Remove the element
Reverse the linked list, thats the output
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # reverse the linked list
        curr = head
        prev = None
        
        while curr:
            # save next node
            next_temp = curr.next
            # point curr.next to prev
            curr.next = prev
            # update prev
            prev = curr
            # update curr
            curr = next_temp
        # prev is the reversed linked list
        
        # remove the node and edit the linked list 'prev'
        if n == 1:
            prev = prev.next
        elif n != 1:
            curr = prev
            node_pointer = 1
            
            while node_pointer != n-1:
                curr = curr.next
                node_pointer += 1
            curr.next = curr.next.next
        
        # reverse the linked list 'prev' which will be the output
        curr = prev
        output = None
        
        while curr:
            next_temp = curr.next
            curr.next = output
            output = curr
            curr = next_temp
        
        return output