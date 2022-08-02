"""
Iterate over the list and create a hashmap of counts of all nodes.
Create a list of nodes which only occur once
Create a new linked list which ONLY has the elements from the unique list 

Can be simpler and better to use less memory
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count_map = {}
        dummy = ListNode()
        dummy = head
        
        while dummy:
            if dummy.val not in count_map.keys():
                count_map[dummy.val] = 1
            else:
                count_map[dummy.val] += 1
            
            dummy = dummy.next
        
        # create hashset of only nodes which occur once
        unique_nodes = []
        for k,v in count_map.items():
            if v == 1:
                unique_nodes.append(k)
        
        # create a new linked list with only elements from the unique nodes list
        # case where there arent any unique nodes at all
        if not unique_nodes:
            return None
        # create the first node
        new_head = ListNode()
        dummy = new_head
        for i in range(len(unique_nodes)):
            dummy.val = unique_nodes[i]
            dummy.next = ListNode()
            
            dummy = dummy.next
        
        # remove the last element
        dummy = new_head
        for _ in range(len(unique_nodes)-1):
            dummy = dummy.next
        dummy.next = None
        
        return new_head
                 