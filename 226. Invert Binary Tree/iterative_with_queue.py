# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # iterative with collections.deque
        queue = collections.deque()
        # start with root
        queue.append(root)
        
        # while queue is not null
        while queue:
            node = queue.popleft()
            
            if node:
                # swap
                node.left, node.right = node.right, node.left
                
                # add next children to queue
                queue.append(node.left)
                queue.append(node.right)
        
        return root
            