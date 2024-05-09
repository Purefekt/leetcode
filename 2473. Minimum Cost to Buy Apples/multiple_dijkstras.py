"""
Create the bidirectional graph.
Repeat the following for each node.
Run dijkstras starting from each node.
Then calulcate the best path for each node by using min_cost + k*min_cost + appleCost.
This is because the shortest path to a node is also the shortest path back.

O(n*(n+r)logn) time for n cities and r roads or n nodes and r edges. Dijkstras takes O(n+r)logn time and we run it for each node.
O(n+r) space used for the adj list.
"""

class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        
        adj = {i:[] for i in range (1, n+1)}
        for a,b,cost in roads:
            adj[a].append([b, cost])
            adj[b].append([a, cost])
        
        # run dijkstras from each node
        output = []
        for i in range(1, n+1):
            min_cost = {k:math.inf for k in range(1, n+1)}
            min_cost[i] = 0
            pq = [[0,i]]
            heapq.heapify(pq)
            visited = set()
            while pq:
                cost, node = heapq.heappop(pq)
                if node in visited:
                    continue
                min_cost[node] = min(min_cost[node], cost)
                for child, child_cost in adj[node]:
                    heapq.heappush(pq, [child_cost + cost, child])
                visited.add(node)
            
            # get the final res cost
            res = math.inf
            for j in range(1, n+1):
                res = min(
                    res,
                    min_cost[j] + (k*min_cost[j]) + appleCost[j-1] 
                )
            output.append(res)
        
        return output
        