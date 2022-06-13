"""
go through the nodes, if val = val, then point the previous node to current nodes next node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # create a dummy node before the list
        dummy = ListNode()
        dummy.next = head
        
        # initialize current and previous
        curr_node = dummy.next
        prev = dummy
        
        while curr_node is not None:
            print(curr_node.val, prev.val)
            
            if curr_node.val == val:
                prev.next = curr_node.next
                
                curr_node = curr_node.next
            else:
                prev = curr_node
                curr_node = curr_node.next
        
        return dummy.next
    