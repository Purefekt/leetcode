"""
For a pair of nodes, first from root and second from subRoot, run sameTree recursively to find if they are the same.
If they are then return True.
Else compare the root.left to subRoot and root.right to subRoot. If either is true, return True.

O(m*n) where there are m nodes in root and n nodes in subRoot. Since we have to check for all pairs of nodes.
O(m+n) space for the 2 stacks used.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(first, second):
            if not first and not second:
                return True
            
            if first and not second:
                return False
            
            if not first and second:
                return False
            
            if first.val == second.val:
                return sameTree(first.left, second.left) and sameTree(first.right, second.right)
            
            else:
                return False
        

        # if subRoot is null, it is always true since we can go to the children of any leaf node of root.
        if not subRoot: return True
        # if root itself is null but subRoot is not, then it is false
        if not root and subRoot: return False

        if sameTree(root, subRoot) is True:
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
