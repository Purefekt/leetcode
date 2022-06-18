"""
Run bfs and create a hashmap for all nodes. 
Key -> k - node.val 
Value -> node
Run another bfs and find a node.val which is in the keys of the hashmap. If the node is not the same, then return True. If BFS runs completely, means we did not find such a node, return False

This doesnt leverage the fact that is it a BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        # edge case
        if root.left is None and root.right is None:
            return False
        
        # run bfs and create a hashmap of k - node.val:node
        queue = collections.deque()
        queue.append(root)
        hashmap = {}
        
        while queue:
            node = queue.popleft()
            hashmap[k - node.val] = node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        
        # run bfs again and see if a the corresponding node is in the tree
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node.val in hashmap.keys():
                if node != hashmap[node.val]:
                    return True
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
    