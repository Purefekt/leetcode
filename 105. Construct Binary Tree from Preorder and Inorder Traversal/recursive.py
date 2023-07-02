"""
The first element of the preorder list will be the root of the tree.
The elements to the left of this element in the "inorder" list will lie in its left subtree, and the elements to the right of this element in "inorder" list will lie in its right subtree.
preorder = [3,9,20,15,7], the root is 3.
inorder = [9,3,15,20,7], [9] lies in the left subtree and [15,20,7] lie in the right.
Repeat this recursively for each node. Helper function can take the preorder list, inorder list and current node.
Set the node.val to preorder[0].
Find the index of preorder[0] in inorder, and create left_preorder, left_inorder, right_preorder, right_inorder lists.

O(n) time to go over all nodes
O(n) space, since implicit stack will take O(n) in worst case and O(logn) in best case
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(p, i, node):
            node.val = p[0]

            idx = i.index(p[0])

            left_p = p[1:1+idx]
            left_i = i[:idx]

            right_p = p[1+idx:]
            right_i = i[idx+1:]

            if left_p:
                node.left = TreeNode()
                helper(left_p, left_i, node.left)
            if right_p:
                node.right = TreeNode()
                helper(right_p, right_i, node.right)
        
        root = TreeNode()
        helper(preorder, inorder, root)
        return root
