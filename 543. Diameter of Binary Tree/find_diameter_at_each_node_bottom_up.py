"""
Get all the nodes from the bottom layer to the top, bottom up in a stack
Keep popping from the stack and getting nodes.
Create a hashmap, key=node :: value=(diameter, height)
We will get the diameter and max_height at the current node for all nodes
At the end we will have a hashmap of all nodes with the diameter at that node and their max_height
Keep a max_diameter variable and update it everytime we get a new height.
Each node can have 2 children, and each child will have its own height. Diameter = 2 + left_height + right_height
If a node is a leaf node, then its left child and right childs heights are -1, thus its diameter is 0 cos 2 + (-1) + (-1)

O(n) time to traverse all nodes to build bottom up stack. Then traverse all nodes again to build the hashmap.
O(n) space to store details of all nodes in a hashmap
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # get all the nodes bottom up in a stack
        stack1 = [root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left: stack1.append(node.left)
            if node.right: stack1.append(node.right)
        
        # build the hashmap
        max_diameter = 0
        hashmap = {}
        while stack2:
            node = stack2.pop()
            
            # if a node has a left child or right child in the hashmap, then update its height.
            # otherwise a node is a leaf node and wont have a left or right child. We set def heights to -1 and add +1 to the max for the edge
            left_h = -1
            right_h = -1
            if node.left and node.left in hashmap:
                left_h = hashmap[node.left][1]
            if node.right and node.right in hashmap:
                right_h = hashmap[node.right][1]
            
            height = max(left_h,right_h) + 1
            
            # every node has 2 children with 2 edges. The diameter at every node is 2+left_h+right_h. For leaf node this becomes 0
            diameter = 2 + left_h + right_h
            max_diameter = max(max_diameter, diameter)
            
            # update this node
            hashmap[node] = (diameter, height)
        
        return max_diameter
    