"""
Get all nodes in a stack bottom up.
Get the (left_height, right_height) for all nodes bottom up.
The (l_h, r_h) for all leaf nodes will be (0,0)
The l_h for every node will be the max(l_h,r_h)+1 of its left child and same for r_h with right child
Add the (l_h, r_h) of each node to the hashmap and continue up.
If at any point abs(l_h - r_h) > 1, this means the tree is not balanced AT THAT node thus the tree is not height balanced. Return
If we go through all nodes without returning false, means this tree is balance
O(n) time to traverse all nodes once to create bottom up stack and one more pass to build the hashmap
O(n) space to store data of all nodes in the hashmap
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
        
        stack1 = [root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left: stack1.append(node.left)
            if node.right: stack1.append(node.right)
        
        hashmap = {}
        while stack2:
            node = stack2.pop()
            
            # set all leaf nodes to having (0,0)
            if not node.left and not node.right:
                hashmap[node] = (0,0)
            else:
                left_h = 0
                right_h = 0
                if node.left and node.left in hashmap:
                    left_h = max(hashmap[node.left])+1
                if node.right and node.right in hashmap:
                    right_h = max(hashmap[node.right])+1
                if abs(left_h - right_h) > 1:
                    return False
                hashmap[node] = (left_h, right_h)
        
        return True
    