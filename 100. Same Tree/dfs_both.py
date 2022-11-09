"""
Use dfs to traverse both trees together.
Add nodes to the stacks in the form (node, dir). Dir is either left or right inidicating weather this is the left child or right child.
At each point, compare the node.val and also the dir, if its different, then return False.
At the start put a check for when both trees are empty, return True
Put a check for when 1 of the 2 is empty, then false
During the traversal, if one tree has been explored fully and the other isnt, this also must return False
O(n) time to traverse all nodes once
O(n) space to store the nodes in the 2 stacks
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if (p and not q) or (not p and q):
            return False
        
        stack_p = [(p,'root')]
        stack_q = [(q,'root')]
        
        while stack_p or stack_q:
            
            # if one of the trees still have nodes and the other doesnt
            if (stack_p and not stack_q) or (not stack_p and stack_q):
                return False
            
            node_p, dir_p = stack_p.pop()
            node_q, dir_q = stack_q.pop()
            
            if node_p.val != node_q.val or dir_p != dir_q:
                return False
            
            if node_p.left: stack_p.append((node_p.left, 'left'))
            if node_p.right: stack_p.append((node_p.right, 'right'))
            if node_q.left: stack_q.append((node_q.left, 'left'))
            if node_q.right: stack_q.append((node_q.right, 'right'))
        
        return True
    