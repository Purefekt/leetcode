"""
using 2 stacks. Start stack1 with root. Pop from stack1 and add the current node to stack2. Add left and right children of this node to stack1 and repeat. At the end stack2 will have the correct postorder, keep popping and form an output list.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # edge case
        if not root:
            return []
        
        stack1 = collections.deque()
        stack2 = collections.deque()
        
        stack1.append(root)
        
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        # get the output list
        output = []
        while stack2:
            node = stack2.pop()
            output.append(node)
        
        return output
    """
using 2 stacks. Start stack1 with root. Pop from stack1 and add the current node to stack2. Add left and right children of this node to stack1 and repeat. At the end stack2 will have the correct postorder, keep popping and form an output list.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # edge case
        if not root:
            return []
        
        stack1 = collections.deque()
        stack2 = collections.deque()
        
        stack1.append(root)
        
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        # get the output list
        output = []
        while stack2:
            node = stack2.pop()
            output.append(node)
        
        return output
    