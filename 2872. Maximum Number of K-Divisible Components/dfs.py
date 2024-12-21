"""
Create a tree with a simple adj list.
Now run dfs, go to a leaf.
If the leaf node value is divisible by k, this can be its own component and we cut it off.
If the lead node is not divisible by k, this needs to be added to the parent and now its parent value is its value + this child.
We can simply run from 0th node assuming that is the root.

O(n) time since edges are n-1. One pass over edges to create tree and one pass over the tree.
O(n) space used by adj list and stack.
"""

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        # create adj list
        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        res = 0
        # root at 0 and run dfs
        visited = set()
        def dfs(node):
            nonlocal res

            if node in visited:
                return 0

            visited.add(node)

            total = values[node]
            for child in adj[node]:
                if child not in visited:
                    total += dfs(child)
            
            if total % k == 0:
                res += 1
                return 0
            else:
                return total
        
        dfs(0)
        return res 
