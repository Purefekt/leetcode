"""
In the constructor, traverse the tree in an inorder fashion and store it in an array.
Append -1 to the start of this array and set a pointer to the 0.
For next calls, increment pointer by 1 and return the value in the array.
For hasNext, return True if the pointer is < len(arr)-1.

O(n) time for the constructor. Other 2 methods run in O(1) time.
O(n) space for the inorder array.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.inorder_arr = [-1]
        self.pointer = 0
        # iterate through it and populate it
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.inorder_arr.append(node.val)
            inorder(node.right)
        
        inorder(root)


    def next(self) -> int:
        self.pointer += 1
        return self.inorder_arr[self.pointer]
        

    def hasNext(self) -> bool:
        if self.pointer < len(self.inorder_arr)-1:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()