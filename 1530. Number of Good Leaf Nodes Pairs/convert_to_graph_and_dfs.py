"""
Convert tree to bidirectional graph.
Store nodes as keys and children since there can be 2^10 nodes with values upto 100, this means values are repeated.
Then simply run dfs from each leaf node, if the depth > distance, then stop the search for that path.
If we encounter another leaf at any point, add to result.

O(n^2) time since we run dfs from each node. 
O(n) space used by hashmap and stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        # create rev tree using TreeNodes since repeated vals are present and cannot be stored in memory 2^10
        adj = collections.defaultdict(list)
        leaves = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node)
            
            if node.left:
                adj[node.left].append(node)
                adj[node].append(node.left)
                stack.append(node.left)
            
            if node.right:
                adj[node.right].append(node)
                adj[node].append(node.right)
                stack.append(node.right)
        
        for k,v in adj.items():
            node_val = k.val
            children = [c.val for c in v]

        # run dfs from each leave and stop when depth > distance
        res = 0
        leaves = set(leaves)
        for l in leaves:
            stack = [(l, 0)]
            visited = set()
            while stack:
                vals = [[a.val, b] for a,b in stack]
                node, depth = stack.pop()
                if depth > distance:
                    continue
                if node in visited:
                    continue
                
                if node != l and node in leaves:
                    res += 1
                for child in adj[node]:
                    if child not in visited:
                        stack.append((child, depth+1))
                visited.add(node)
        
        return res//2
