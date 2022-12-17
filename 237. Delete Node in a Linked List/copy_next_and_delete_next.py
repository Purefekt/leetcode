"""
Copy val of next node and then delete it
Keep a pointer p at given node and d at the next node
Set the value of current node (the node to delete) as value of next node
Then delete the next node by setting next of p node to d.next

O(1) time
O(1) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        d = node.next
        p.val = d.val
        p.next = d.next
        