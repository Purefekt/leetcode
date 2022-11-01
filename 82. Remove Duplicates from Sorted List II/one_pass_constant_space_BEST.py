"""
One pass with constant memory.
Create a fake head behind the head. Check for if head is none or head has 1 node.
Run a loop and check the vals of next and next.next nodes. If the vals of next and next.next nodes are the same, run a while loop with another pointer till the node AFTER the last common value.
Connect current node to the node after the last common value
Answer will be at fake_head.next
O(n) time. One pass over all nodes
O(1) space using only pointers
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        # add fake head
        fake_head = ListNode(0, head)
        dummy = fake_head
        
        # if only 1 node
        if not dummy.next.next:
            return head
        
        while dummy.next and dummy.next.next:
            if dummy.next.val != dummy.next.next.val:
                dummy = dummy.next
            else:
                check_val = dummy.next.val
                dummy_2 = dummy.next
                while dummy_2 and dummy_2.val == check_val:
                    dummy_2 = dummy_2.next
                dummy.next = dummy_2
        
        return fake_head.next
    