"""
Managing pointers makes this hard.
Create a sent head which points to the start of the result list. This node will be the kth node in the original list. So set sent_head.next to this node.
Now get the total number of nodes in the list n and loop k//n times since these many groups need to be reversed.
Reverse k nodes starting with head. The head of the reversed list will be at prev and the head of the next group will be at head pointer.
The tail of the reversed node will point to None. We need it to point to the start of the next group.
The start of the next group is currently the tail of the next group. 
First move prev from start of current group to the last node. Next use a dummy node to move from head which is currently at head of next group to the tail of it, then set prev.next to dummy.
Now Repeat the reverse from head for the next k nodes.
At the end of loop, prev will be at the tail of the last reversed group and head will be either None (if n%k == 0) else it will be at the start of the last special group.
Set prev.next to head to complete the list.

O(n) time to process each node at most thrice. Once to get size of list. Once to reverse it and once to move through a group till the end of it.
O(1) space using pointers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        sent_head = ListNode()
        dummy = head
        # attach it to the start of the first reversed group
        for _ in range(k-1):
            dummy = dummy.next
        sent_head.next = dummy

        # find total number of nodes
        n = 0
        dummy = head
        while dummy:
            n += 1
            dummy = dummy.next
        
        for _ in range((n//k)):
            prev = None
            for i in range(k):
                nxt_tmp = head.next
                head.next = prev
                prev = head
                head = nxt_tmp
            # shift prev to the end of current reversed group
            for j in range(k-1):
                prev = prev.next
            # set prev (tail of currently reversed group) to the head of the next reversed group (which is the current tail)
            dummy = head
            for l in range(k-1):
                if dummy:
                    dummy = dummy.next
            prev.next = dummy
        
        # connect the tail of the last group to the head of any special group left
        prev.next = head

        return sent_head.next
