"""
Use a dummy node to taverse the bst.
If the val is smaller than the node, go left else go right
Check if the direction we want to go exists of not, if it does then go else place the val there and break

O(h) where h is height. In average case it is logn and worst case it is n (suppose root is smallest and we keep adding only right children)
O(1) space since we only use constant space for dummy pointer
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        
        dummy = root
        while dummy:
            if val < dummy.val:
                if dummy.left:
                    dummy = dummy.left
                else:
                    dummy.left = TreeNode(val)
                    break
            elif val > dummy.val:
                if dummy.right:
                    dummy = dummy.right
                else:
                    dummy.right = TreeNode(val)
                    break
        
        return root
        