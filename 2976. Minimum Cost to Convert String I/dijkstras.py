"""
Dijkstras.
Run this algo for each start and return the min distance at end.
Cache the run for each unique start (there can be at max 26).
Cache the entire min_dist hashmap for each start. Use this cache for future calls of start.

O(m+n) time where len of source is n and len of original is m. Creating adj list takes m time. Running dijkstras takes O((26+m)*log26) or m time. Total cost takes O(n) time.
O(m) space used by dijkstras pq. 
"""

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        adj = collections.defaultdict(list)
        all_chars = set()
        for i in range(len(original)):
            adj[original[i]].append((changed[i], cost[i]))
            all_chars.add(original[i])
            all_chars.add(changed[i])

        cache = {}
        def dijkstras(start, end):
            if start in cache:
                return cache[start][end]
            
            if start not in all_chars or end not in all_chars:
                return math.inf
            min_dist = {c:math.inf for c in all_chars}

            pq = [(0, start)]
            heapq.heapify(pq)
            visited = set()
            while pq:
                dist, node = heapq.heappop(pq)
                if node in visited:
                    continue
                min_dist[node] = min(min_dist[node], dist)
                
                for child, child_cost in adj[node]:
                    if child not in visited:
                        heapq.heappush(pq, (dist+child_cost, child))
                visited.add(node)
            
            cache[start] = min_dist
            
            return min_dist[end]
        
        res = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            cost = dijkstras(source[i], target[i])
            if cost == math.inf:
                return -1
            res += cost
        
        return res
