# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(total, node):
            if not node:
                return False
            
            total += node.val
            # if this is a leaf node
            if not node.left and not node.right:
                if total == targetSum:
                    return True
                else:
                    return False
            
            if helper(total, node.left) is True or helper(total, node.right) is True:
                return True
            return False
        
        return helper(0, root)
        