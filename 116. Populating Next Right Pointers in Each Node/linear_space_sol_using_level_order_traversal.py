"""
Create a level order list of all the nodes. For ex -> [[1], [2,3], [4,5,6,7]]
Then go through list and set the next pointer of each element to the next, except the last element, thus each loop for each list will be till range(len(list)-1)

Linear space solution
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        
        # get level order traversal
        level_order = []
        queue = collections.deque()
        queue.append(root)
        level_size = 1
        
        while queue:       
            current_level = []
            for i in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_order.append(current_level)
            level_size *= 2
        
        
        for level in level_order:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        
        return root
        