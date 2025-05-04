# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        def dfs(node, combo):
            
            combo.append(str(node.val))
            if not node.left and not node.right:
                res.append('->'.join(combo.copy()))
            if node.left:
                dfs(node.left, combo)
            if node.right:
                dfs(node.right,combo)
            combo.pop()
        
        dfs(root, [])
        return res