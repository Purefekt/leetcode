"""
ITERATIVE
Run inorder tree traversal.
when adding a node, see if it is smaller or eq to the previous node, if yes then false
initialize inorder list with -inf as 0th element to avoid error when adding the very first node

O(n) time
O(n) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # inorder tree traversal, if node added is larger than previous, then return false

        stack = []
        inorder = [-inf]
        curr_node = root

        while curr_node or stack:

            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            
            curr_node = stack.pop()
            inorder.append(curr_node.val)
            if inorder[-1] <= inorder[-2]:
                return False
            curr_node = curr_node.right

        return True
        