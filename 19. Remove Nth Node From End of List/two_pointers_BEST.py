# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # add dummy node
        dummy = ListNode()
        dummy.next = head
        
        # initialize left pointer to 0 and right pointer to n+1
        left = dummy
        # code to set right
        right = dummy
        right_pointer_index = n+1
        current_pointer = 0
        while current_pointer != right_pointer_index:
            right = right.next
            current_pointer += 1
        
        # increment right and left by 1 till right is None. At this point left will be the node right before the node to remove
        while right:
            left = left.next
            right = right.next
        
        # change left.next to left.next.next. This will remove the node
        left.next = left.next.next
        
        return dummy.next
    