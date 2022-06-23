"""
Get length of linked list. Middle node is length // 2.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # get length of the linked list:
        curr_node = head
        length = 0
        while curr_node != None:
            length += 1
            curr_node = curr_node.next

        # get middle element index
        middle_element_index = length // 2
        
        output = head
        for i in range(middle_element_index):
            output = output.next
        
        return output
    