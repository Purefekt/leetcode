"""
Create a set of memory addresses of each node. If a memory address repeats, its a cycle.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        memory_add = set()
        
        while head is not None:
            if id(head) in memory_add:
                return True
            
            memory_add.add(id(head))
            head = head.next
        
        # if while loop terminates, no cycle
        return False