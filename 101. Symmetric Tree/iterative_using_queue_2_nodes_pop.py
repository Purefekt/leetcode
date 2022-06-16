"""
Using a queue. Initialize queue with root,root. For each step pop two elements from the queue. If these elements are equal then add both children of both these nodes in a particular order.
First add the left child of node1, then right child of node2, then right child of node1 and finally left child of node 2.
Add checks for when both nodes are null, move on to the next iteration
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = collections.deque()
        
        # start with two roots
        queue.append(root)
        queue.append(root)
        
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            
            # check for when both nodes are null
            if node1 is None and node2 is None:
                continue
            
            # if the nodes are diff, then false. But we need to check val of nodes and None nodes do not have a val
            if node1 is not None and node2 is None:
                return False
            if node1 is None and node2 is not None:
                return False
            if node1.val != node2.val:
                return False
            
            # if nodes are the same, add their children in the order
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        
        # if while loop completes, we havea. symmetric tree
        return True
        