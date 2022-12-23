"""
Run level order bfs from start node, BUT only k times (or till queue lasts)
Maintain a min_cost hashmap, at the start set src to 0 and rest all to infinity
ONLY add to queue if the path cost to get to a node is less than the min_cost being tracked, since if we reach a node with any cost larger than min_cost, it means that path will always have a larger total path cost

O(n + e*k) where n is the number of nodes, e is edges and k is numstops. 
O(n + e*k) for queue
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # make adj list
        adj = {i:[] for i in range(n)}
        for source,destination,cost in flights:
            adj[source].append((destination,cost))
        
        
        # make a track list to track min path costs for all 
        min_costs = {i:inf for i in range(n)}
        min_costs[src] = 0

        queue = [(src,0)]
        num_stops = 0
        while queue and num_stops <= k:
            num_stops += 1
            for i in range(len(queue)):
                
                node, curr_path_cost = queue.pop(0)

                for child, child_cost in adj[node]:
                    if min_costs[child] > curr_path_cost+child_cost:
                        min_costs[child] = curr_path_cost+child_cost
                        queue.append((child, curr_path_cost+child_cost))
        
        if min_costs[dst] == inf:
            return -1
        return min_costs[dst]
