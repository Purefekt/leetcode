"""
Preorder traversal but include Null nodes as 'N', so [1,2,3,null,null,4,5] will have the traversal [1,2,N,N,3,4,N,N,5,N,N].
Pass this to the deserialize function as a comma separated string.
To deserialize, use a helper function. Keep a nonlocal idx which iterates through the traversal.
If data[idx] == 'N', increment idx and return None.
Else create a new node, set the node.val to data[idx] and increment idx.
Then call helper on node.left and node.right.

O(n) time for both methods since we traverse all nodes at most once.
O(n) space to store the nodes in an array.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # serialize with preorder traversal but include null nodes as well
        res = []
        def preorder(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        idx = 0

        def helper():
            nonlocal idx
            if data[idx] == 'N':
                idx += 1
                return None
            
            node = TreeNode()
            node.val = int(data[idx])
            idx += 1
            node.left = helper()
            node.right = helper()
            return node
        
        root = helper()
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))