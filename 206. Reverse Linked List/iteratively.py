# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # using two pointers. Curr = head, start at head. Prev = None
        curr = head
        prev = None
        
        # the last node will be None. Thus stop when curr = None
        while curr != None:
            
            # store the next node of current node
            next_node = curr.next
            
            # change next node of current node to previous
            curr.next = prev
            
            # change previous to the current node
            prev = curr
            
            # change curr node to next node
            curr = next_node
        
        # now prev is the head
        return prev