"""
Build a hashmap where keys are pointers to nodes in the original list and values are new ListNodes.
To initialize, go through the list and add the pointer as key and set the value to ListNode(pointer.val) as the value. ie the value is a new ListNode with no next and random and the value set to the value of the corresponding node.
Do another pass through the list to edit the next and random values of the new nodes.
For each key, set the hashmap[pointer].next = hashmap[dummy.next] and same for random.
Return hashmap[head] returns the pointer to the head of the new list.

O(n) time where n is the size of list due to 2 passes over the input.
O(n) space for the hashmap
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
            return 

        hashmap = {}

        dummy = head
        while dummy:
            hashmap[dummy] = ListNode(dummy.val)
            dummy = dummy.next
        
        dummy = head
        while dummy:
            if dummy.next == None:
                hashmap[dummy].next = None
            else:
                hashmap[dummy].next = hashmap[dummy.next]
            
            if dummy.random == None:
                hashmap[dummy].random = None
            else:
                hashmap[dummy].random = hashmap[dummy.random]

            dummy = dummy.next

        return hashmap[head]
