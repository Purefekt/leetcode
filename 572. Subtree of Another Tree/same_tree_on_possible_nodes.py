"""
Iterative.
Traverse all nodes and put all nodes where node.val == subRoot.val in a set.
Traverse that set and for each node, run the same_tree problem on them. If they are same, return True, else check for other nodes.
If no nodes are the same, then return with False
O(m*n) time where n is the number of nodes in root and m is the number of nodes in subRoot
O(m+n) space to store 2 stacks.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # traverse the tree, at any node where node.val == subRoot.val, add it to a set.
        possible_roots = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                possible_roots.add(node)
            
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        def same_tree(test_root):
            stack_poss_root = [(test_root,'root')]
            stack_subRoot = [(subRoot, 'root')]
            
            while stack_poss_root and stack_subRoot:
                poss_node, dir_poss_node = stack_poss_root.pop()
                sub_node, dir_sub_node = stack_subRoot.pop()
                
                if poss_node.val != sub_node.val or dir_poss_node != dir_sub_node:
                    return False
                
                if poss_node.left: stack_poss_root.append((poss_node.left, 'left'))
                if poss_node.right: stack_poss_root.append((poss_node.right, 'right'))
                                                          
                if sub_node.left: stack_subRoot.append((sub_node.left, 'left'))
                if sub_node.right: stack_subRoot.append((sub_node.right,'right'))
            
            if stack_poss_root or stack_subRoot:
                return False
            
            return True
        
        res = None
        for poss_root in possible_roots:
            res = same_tree(poss_root)
            if res == True:
                return True
        
        return False
    