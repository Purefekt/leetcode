# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # edge case when tree is null
        if root is None:
            return None
        
        # iterative with collections.deque
        queue = collections.deque()
        # start with root
        queue.append(root)
        
        # while queue is not null
        while queue:
            current_node = queue.popleft()
            
            # swap
            current_node.left, current_node.right = current_node.right, current_node.left
            
            # add left and right nodes to queue if not none
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        
        return root
            