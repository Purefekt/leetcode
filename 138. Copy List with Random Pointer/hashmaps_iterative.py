"""
Hashmaps, iterative.
Build 2 hashmaps. New node to old nodes and old nodes to new nodes. Currently these new nodes will have None in next and random
Next build a hashmap for next pointers. Here the key is the old node and the value is the NEW next node. We can find this using the old to copy hashmap
Next build a hashmap for random pointers in the same way
Now we can iterate over the keys in copy to old hashmap, where all keys are new nodes and edit their next and random pointers using next and random hashmaps and copy to old hashmap
return the new node head which can be found using the old to copy hashmap using the old head

O(n) time to iterate all nodes
O(n) space to store multiple hashmaps of size n
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        # build copies of all nodes and save to a hashmap, copy:old and old:copy
        hashmap_copy_to_old = {}
        hashmap_old_to_copy = {}
        dummy = head
        while dummy:
            new_node = Node(dummy.val)
            hashmap_copy_to_old[new_node] = dummy
            hashmap_old_to_copy[dummy] = new_node
            dummy = dummy.next
        
        # build hashmap for old nodes and their next node
        hashmap_next = {}
        dummy = head
        while dummy:
            if not dummy.next:
                hashmap_next[dummy] = None
            else:
                hashmap_next[dummy] = hashmap_old_to_copy[dummy.next]
            dummy = dummy.next
        
        # build hashmap for old nodes and their random node
        hashmap_random = {}
        dummy = head
        while dummy:
            if not dummy.random:
                hashmap_random[dummy] = None
            else:
                hashmap_random[dummy] = hashmap_old_to_copy[dummy.random]
            dummy = dummy.next
        
        # use these hashmaps to edit next and random values for new nodes
        for new_node in hashmap_copy_to_old.keys():
            new_node.next = hashmap_next[hashmap_copy_to_old[new_node]]
            new_node.random = hashmap_random[hashmap_copy_to_old[new_node]]
        
        # return the new root node
        return hashmap_old_to_copy[head]
            