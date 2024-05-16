# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node.left and not node.right:
                if node.val == 1:
                    return True
                else:
                    return False
            
            left = helper(node.left)
            right = helper(node.right)
            res = None
            if node.val == 2:
                res = left or right
            else:
                res = left and right
            return res

        return helper(root)
