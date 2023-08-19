"""
Recursively. Use a helper function which accepts node1 and node2.
If both nodes are null, that means we have reached leaves, then return True
If either one of the nodes still exists whereas the other is None, then False
If the value of node1 and node2 is not equal, then return False
Now we have 2 cases, either we can choose to flip or not, and either one of these must be True.
In the no flip case, we pass the left of both nodes and right of both nodes
In the flip case, we pass alternative.
Return OR of these cases

O(min(n1, n2)) where n1 and n2 are the lengths of root1 and root2. We run for as long as the smaller tree.
O(min(h1, h2)) where h1 and h2 are heights of root1 and root2
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (node1 and not node2):
                return False
            
            if node1.val != node2.val:
                return False
            
            no_flip = helper(node1.left, node2.left) and helper(node1.right, node2.right)
            flip = helper(node1.left, node2.right) and helper(node1.right, node2.left)
            return no_flip or flip
        
        return helper(root1, root2)
        