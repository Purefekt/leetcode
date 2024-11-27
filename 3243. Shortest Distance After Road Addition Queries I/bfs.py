"""
Build the initial adj list with all nodes having the next node as its only child.
Iterate over all queries to add that edge.
Run simple bfs to get the depth.

O(q*(n+q)) time since bfs takes n+q time and the outer loop runs for all queries.
O(n+q) space.
"""

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        adj = {i:[i+1] for i in range(n)}
        adj[n-1] = []

        def bfs():
            visited = set()
            queue = [(0,0)]
            while queue:
                node, depth = queue.pop(0)
                if node == n-1:
                    return depth
                if node in visited:
                    continue
                for child in adj[node]:
                    queue.append((child, depth+1))
                visited.add(node)

        res = []
        for a,b in queries:
            adj[a].append(b)

            # run bfs for each
            res.append(bfs())
        
        return res
        