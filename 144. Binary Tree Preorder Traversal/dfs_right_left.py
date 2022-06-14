"""
Use dfs. Start stack with root. Pop the root and add it to the output. Then add the right child and then the left child. Add left child second so it is on top of the stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # edge case
        if not root:
            return []
        
        output = []
        stack = collections.deque()
        
        # start with root
        stack.append(root)
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            
            # add right then left children if they exist
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return output
    