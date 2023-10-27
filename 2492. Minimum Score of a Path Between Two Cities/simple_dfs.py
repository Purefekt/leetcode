"""
Just run DFS or BFS from 1 and explore the entire graph.
During the traversal, keep track of the minimum edge cost.

O(v+e) time where we have v nodes and e edges.
O(v+e) space. Adj list takes e space and visit array and stack take v space.
"""

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(1,n+1)}
        for src, dst, cost in roads:
            adj[src].append((dst, cost))
            adj[dst].append((src, cost))

        # run dfs from 1 and track the shortest path
        min_edge = math.inf
        stack = [1]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            for child, cost in adj[node]:
                min_edge = min(min_edge, cost)
                stack.append(child)
            visited.add(node)
        
        return min_edge
