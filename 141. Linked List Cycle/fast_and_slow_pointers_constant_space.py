"""
FLOYD'S CYCLE FINDING ALGO

fast and slow pointer. Fast will move 2 steps and slow will move 1 step at a time. If fast == slow, this means there is a cycle in the list and fast has caught up to slow. If there is no cycle, fast will become None and we exit
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # edge case, if list is empty then no cycle
        if not head:
            return False
        
        # initialize slow and fast
        slow = head
        fast = head.next
        
        while slow != fast:
            
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        # if we while loop terminates, a cycle is found since slow and fast are equal
        return True
        