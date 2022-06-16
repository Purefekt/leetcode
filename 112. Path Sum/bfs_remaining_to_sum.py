"""
Use DFS. At each node save the [node, target - node.val] in the stack. target - node.val is the remaining. If remaining becomes 0, and the node is a lead node (no right or left children) then return True. 
If the entire dfs runs and we dont return true, then return false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        stack = collections.deque()
        stack.append([root, targetSum - root.val])
        
        while stack:
            
            node, rem = stack.pop()
            
            if node.right is None and node.left is None and rem == 0:
                return True
            
            if node.right:
                stack.append([node.right, rem - node.right.val])
                
            if node.left:
                stack.append([node.left, rem - node.left.val])
            
            
        return False
    