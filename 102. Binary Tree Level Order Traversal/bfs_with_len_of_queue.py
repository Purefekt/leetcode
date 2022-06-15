"""
Apply BFS. But to get nodes level wise, use a for loop for the length of current queue. These many nodes are on the same level.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = collections.deque()
        output = []
        queue.append(root)
        
        while queue:
            num_nodes_in_level = len(queue)
            
            curr_level = []
            for i in range(num_nodes_in_level):
                node = queue.popleft()
                curr_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            output.append(curr_level)
        
        return output
    