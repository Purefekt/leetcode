"""
Inorder traversal and then build.
Use inorder traversal to first get all the node vals in increasing order.
Now to perfectly balance this tree, we can pick the middle element, set it as the node and then send all elements to the left of it to the left subtree and all elements to the right of it to the right subtree.
Recursively repeat this for all subtree.
Do this by passing l and r pointers. Return None if l>r.

O(n) time to do a pass to get inorder traversal and another pass to build the result.
O(n) space used by the inorder array.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # get all the nodes in increasing order
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        inorder(root)
        
        def helper(l,r):
            if l>r:
                return None

            p = (l+r)//2
            node = TreeNode(nodes[p])
            node.left = helper(l, p-1)
            node.right = helper(p+1, r)
            return node
        
        return helper(0, len(nodes)-1)
