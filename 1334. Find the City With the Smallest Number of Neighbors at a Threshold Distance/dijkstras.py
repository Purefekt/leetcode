"""
Run dijkstras from each node as start.
Use logic to stop search if distance has exceeded threshold.
Get number of cities where distance is less than threshold for each city.
Create candidates list for all with number of cities same as min value.
Return the max of these.

O(n^3*logn) time. The dijkstras algorithm takes O(mlogn) time where m is number of edges and n is the number of nodes. Since m can be n^2 at max, the algorithms complexity becomes n^2*logn. We run this n times for each node.
O(n^2) space used by m number of edges which is n^2.
"""

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        adj = {i:[] for i in range(n)}
        for a,b,w in edges:
            adj[a].append((b,w))
            adj[b].append((a,w))

        def dijkstras(start):
            min_dist = {i:math.inf for i in range(n)}
            min_dist[start] = 0

            pq = [(0, start)]
            heapq.heapify(pq)
            visited = set()
            while pq:
                dist, node = heapq.heappop(pq)
                min_dist[node] = min(min_dist[node], dist)
                if node in visited:
                    continue
                if dist >= distanceThreshold:
                    continue
                for child, w in adj[node]:
                    if child not in visited and dist+w <= distanceThreshold:
                        heapq.heappush(pq, (dist+w, child))
                visited.add(node)
            
            num_cities = 0
            del min_dist[start]
            for v in min_dist.values():
                if v <= distanceThreshold:
                    num_cities += 1
            
            return num_cities
        
        num_cities = {}
        for i in range(n):
            num_cities[i] = dijkstras(i)

        candidates = []
        min_val = min(num_cities.values())
        for k,v in num_cities.items():
            if v == min_val:
                candidates.append(k)
        
        return max(candidates)
