"""
Use inorder traversal. Whenever we update the inorder output, check if the new element is larger than the last one. If not, then false, else true.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # start inorder output with -infinity so to avoid bug when adding the first element
        inorder_output = [-inf]
        stack = collections.deque()
        node = root #pointer
        
        while node or stack:
            
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            # false if the new node value is less than the last 
            if node.val <= inorder_output[-1]:
                return False
            
            inorder_output.append(node.val)
            node = node.right
        
        
        # if while loops ends, means true
        return True
    