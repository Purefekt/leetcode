# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_node = head
        
        
        while curr_node is not None and curr_node.next is not None:        
            
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        
        return head
    