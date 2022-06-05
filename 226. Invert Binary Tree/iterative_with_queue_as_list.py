# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # edge case, when tree is null
        if root is None:
            return None
        
        # iterative with queue using python list. Add a node to queue, switch its left and right and then add its left and right to the queue
        
        # start with root node
        queue = [root]
        
        # while queue not empty
        while queue:
            current_node = queue.pop(0)
            
            # swap
            current_node.left, current_node.right = current_node.right, current_node.left
            
            # add left and right to queue if they are not None
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        
        return root
            