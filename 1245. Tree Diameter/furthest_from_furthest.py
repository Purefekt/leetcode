"""
Start from any node A and get the furthest node from it B.
Now get the furthest node from B which is C.
The distance between B and C is the tree diameter.

O(n) time where n is the number of edges.
O(n) space used by queue and stack and adj list.
"""

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        if not edges:
            return 0
        
        # adj list
        adj = {i:[] for i in range(len(edges)+1)}

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        # get the furthest node from 0
        queue = [0]
        visited = set()
        furthest_from_zero = None
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            furthest_from_zero = node
            for child in adj[node]:
                queue.append(child)
            visited.add(node)
        
        # get the dist b/w this node and the node furthest to it
        res = 0
        stack = [(furthest_from_zero, 0)]
        visited = set()
        while stack:
            node, dist = stack.pop()
            res = max(res, dist)
            if node in visited:
                continue
            for child in adj[node]:
                stack.append((child, dist+1))
            visited.add(node)
        
        return res-1
