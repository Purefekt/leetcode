"""
Iteratively using a pointer. Go deep to the left side. If left side is empty, add that node to the output and then go right, then repeat deep to left side
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []
        curr_node = root
        
        while curr_node or stack:
            
            # go deep to the left side till its None
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            
            curr_node = stack.pop()
            output.append(curr_node.val)
            curr_node = curr_node.right
        
        return output
    