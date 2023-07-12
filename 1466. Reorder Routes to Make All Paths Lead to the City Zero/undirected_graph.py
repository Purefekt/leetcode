"""
Treat the graph as undirected and run dfs on it.
For each edge encountered, check if it exists in the input connections.
If it does, then it means it must be flipped, add 1 to res.
Convert the connections list to a set for fast access.

O(n) time to go over each node once.
O(n) space to store the adj list
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        for src, dst in connections:
            adj[src].append(dst)
            adj[dst].append(src)
        
        connections_set = set()
        for conn in connections:
            connections_set.add(tuple(conn))
        
        stack = [0]
        visited = set()
        res = 0

        while stack:
            node = stack.pop()

            for child in adj[node]:
                if child not in visited:
                    edge = (node, child)
                    if edge in connections_set:
                        res += 1
                    stack.append(child)
            visited.add(node)
        
        return res
