"""
Get the root by creating reverse edge adj list.
Only root will not have any children since we are guarenteed a valid binary tree.
Then create a hashmap of left and right nodes of all nodes.
Run bfs with the root Tree node, add to queue for any children.

O(n) time for multiple passes over the tree.
O(n) space for adj list.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        # get the root by reverse creating. Add all nodes which are values to a set
        values = set()
        adj = collections.defaultdict(list)
        for p,c,_ in descriptions:
            adj[c].append(p)
            values.add(p)
        
        # start will be the node which doesnt appear in keys
        keys = set(adj.keys())
        
        root_val = list(values - keys)[0]

        # go through all nodes and get left and right
        hashmap = {}
        for p,c,l in descriptions:
            if p not in hashmap:
                hashmap[p] = [None, None]
            if l == 1:
                hashmap[p][0] = c
            else:
                hashmap[p][1] = c
        
        root = TreeNode(root_val)
        dummy = root
        queue = [dummy]
        
        while queue:
            dummy = queue.pop(0)
            if dummy.val in hashmap and hashmap[dummy.val][0]:
                dummy.left = TreeNode(hashmap[dummy.val][0])
                queue.append(dummy.left)
            if dummy.val in hashmap and hashmap[dummy.val][1]:
                dummy.right = TreeNode(hashmap[dummy.val][1])
                queue.append(dummy.right)
        
        return root
            