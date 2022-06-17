# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # initialize node
        new_node = TreeNode(val)
        
        # edge case
        if not root:
            return new_node
        
        stack = collections.deque()
        stack.append(root)
        
        while stack:
            node = stack.pop()
            
            if new_node.val > node.val:
                if not node.right:
                    node.right = new_node
                    return root
                else:
                    stack.append(node.right)
            
            if new_node.val < node.val:
                if not node.left:
                    node.left = new_node
                    return root
                else:
                    stack.append(node.left)