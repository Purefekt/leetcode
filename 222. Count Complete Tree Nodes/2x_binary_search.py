"""
Get the left end depth and right end depth. If both are equal it is a perfect binary tree, return 2**depth - 1
If the left depth > right depth we need to find number of nodes in the last level. use BINARY SEARCH
Determine the number of nodes in the last level by using 2**(depth-1)
Run binary search and see if we can find the node at the pivot. 
To find the node at the pivot we will use binary search again. Use a dummy at root and go left if pivot >= node to find else go left. This loop will run the number of height times
return the node we reach. If this node is None thus doesnt exists, we move the right pointer to pivot else we move the left pointer to pivot + 1

O(logn) time. O(d^2) where d is the height == O(logn)
O(1) space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        # get the number of complete levels
        right_end_depth = 0
        dummy = root
        while dummy:
            right_end_depth += 1
            dummy = dummy.right
        
        # get the number of levels on left end
        left_end_depth = 0
        dummy = root
        while dummy:
            left_end_depth += 1
            dummy = dummy.left
        
        # if left and right ends are same, this means its a perfect binary tree
        if right_end_depth == left_end_depth:
            return 2**right_end_depth - 1
        
        # get number of nodes in the perfect tree
        num_nodes = 2**right_end_depth
        
        # find the number of nodes in the last level using binary search
        max_nodes_last_level = 2**(left_end_depth-1)
        
        def traverse_to_node(node_pos):
            height = left_end_depth-1
            l = 1
            r = max_nodes_last_level
            dummy = root
            for i in range(height):
                p = (l+r)//2
                if p >= node_pos:
                    dummy = dummy.left
                    r = p
                else:
                    dummy = dummy.right
                    l = p+1
            return dummy
        
        l = 1
        r = max_nodes_last_level
        p = None
        while l<r:
            p = (l+r)//2

            # now try to traverse to node at p
            if traverse_to_node(p) is not None:
                l = p + 1
            else:
                r = p
        
        # if all 3 are same, correct answer at p-1 else answer at p. p-2 and p-1 since numbering was 1 indexed in this code
        if p==l:
            return num_nodes + p-2
        else:
            return num_nodes + p-1
