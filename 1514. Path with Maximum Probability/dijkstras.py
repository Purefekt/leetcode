"""
Dijkstras with maxheap.
Use maxheap to find the max distance instead of min.

O(m + nlogn) time where m is the number of edges and n is number of nodes.
O(m+n) space. hashmap uses m space for all edges and maxheap takes at max n size.
"""

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = {i:[] for i in range(n)}
        for i in range(len(edges)):
            a,b = edges[i]
            prob = succProb[i]
            adj[a].append((b, prob))
            adj[b].append((a, prob))
        
        max_prob = {i:0 for i in range(n)}
        max_prob[start_node] = 1

        pq = [(-1, start_node)]
        heapq.heapify(pq)
        visited = set()
        while pq:
            dis, node = heapq.heappop(pq)
            if node in visited:
                continue
            max_prob[node] = max(max_prob[node], -dis)

            for child, child_prob in adj[node]:
                if child in visited:
                    continue
                heapq.heappush(pq, (dis*child_prob, child))
            visited.add(node)
        
        return max_prob[end_node]
        