"""
Create a directed graph using the bomb radius.
Bombs can be numbered from 0 -> n-1.
Go through all pairs of bombs, and construct the graph. An edge exists if bomb B is in bomb A's radius.
Now run dfs from each bomb from 0 -> n-1 and get the length of visited nodes.
The result will be the max number of visited nodes by any bomb.

O(n^3) time. There can be at most n^2 edges for n number of nodes in the graph. DFS runs in V+E time where V is n and E is n^2. We also need to run DFS for each node, thus n(n + n^2).
O(n^2) space to store the adj list. Visited and stack both use n space. 
"""

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        # for every pair of circles, create a graph edge if a bombs radius is over another bomb
        def overlap(xi, yi, ri, xj, yj):
            distance = math.sqrt((xi-xj)**2 + (yi-yj)**2)
            if distance <= ri:
                return True
            else:
                return False
        
        adj = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    xi, yi, ri = bombs[i]
                    xj, yj, rj = bombs[j]
                    if overlap(xi, yi, ri, xj, yj) is True:
                        adj[i].append(j)

        # there are no edges found ie no bombs overlap any other bomb
        if not adj:
            return 1

        def dfs(node, visited):
            visited.add(node)
            for child in adj[node]:
                if child not in visited:
                    dfs(child, visited)
            return len(visited)
        
        res = 1
        for i in range(len(bombs)):
            visited = set()
            res = max(res, dfs(i, visited))
        
        return res
