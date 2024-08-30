"""
This code gave TLE but is logically correct, mostly bcos dijkstras can be optimized.
"""

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        
        def dijkstras(adj):
            min_dist = {i:math.inf for i in range(n)}
            visited = set()
            pq = [(0, source)]
            heapq.heapify(pq)
            while pq:
                dis, node = heapq.heappop(pq)
                if min_dist[node] <= dis:
                    continue
                min_dist[node] = min(min_dist[node], dis)
                if node in visited:
                    continue
                for child, child_dis in adj[node]:
                    if child in visited:
                        continue
                    heapq.heappush(pq, (dis+child_dis, child))
                visited.add(node)
            return min_dist

        # create a graph by omitting edges with -1
        # find shortest path on this graph, if it is < target, then there is no solution
        adj = {i:[] for i in range(n)}
        for a,b,w in edges:
            if w != -1:
                adj[a].append((b,w))
                adj[b].append((a,w))
        
        min_dist = dijkstras(adj)
        if min_dist[destination] < target:
            return []
        
        # if shortest path to destination is same as target, we can simply set all -1 edges to a large number and return since shortest path is already satisfied
        if min_dist[destination] == target:
            res = []
            for a,b,w in edges:
                if w == -1:
                    res.append([a,b,target+1])
                else:
                    res.append([a,b,w])
            return res
        
        # if the shortest path is larger than target (includes if there is NO path between source and destination), we need to modify the edges.
        # Iterate through all edges which are -1.
        # set all edges to 1 and see if shortest distance < target
        # then set the value of this edge to target - shortest distance + 1 and rerun dijkstras to see if shortest distance == target.
        # if yes, then return, else continue to next edge
        for i in range(len(edges)):
            if edges[i][2] == -1:
                new_edges = []
                for a,b,w in edges:
                    if w == -1:
                        new_edges.append([a,b,1])
                    else:
                        new_edges.append([a,b,w])
                adj = {i:[] for i in range(n)}
                for a,b,w in new_edges:
                    adj[a].append((b,w))
                    adj[b].append((a,w))
                min_dist = dijkstras(adj)
                if min_dist[destination] == target:
                    return new_edges
                edges[i][2] = max(target - min_dist[destination] + 1, 1)
        
        # run one more time if changing the very last edge made it work
        adj = {i:[] for i in range(n)}
        for a,b,w in edges:
            adj[a].append((b,w))
            adj[b].append((a,w))
        min_dist = dijkstras(adj)
        if min_dist[destination] == target:
            return edges
                