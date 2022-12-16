"""
Dijkstras algo
Create adj list with source as key and list of destination,costs
Create another hashmap to keep track of all nodes and their min cost. Initialize the starting node to 0 and others to inf
Start the PQ with (0,k) where 0 is the cost and k is the starting node value
Pop and add its children and their cumulative costs to the pq. At this step check if the cumulative cost is less than in min cost, if it is then update min_costs
Add the node to visited when we have added all its children
Return the max value from min costs, if it is inf, return -1

O(n + elogn) time where e is number edges and n is number vertices. O(elogn) for Dijkstra's and O(n) to find min time.
O(n+e) space. adj list takes n keys and e edges in lists
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # make adj list
        adj = {i:[] for i in range(1,n+1)}
        for src,dst,cost in times:
            adj[src].append((dst,cost))
        
        # track all min costs
        min_costs = {}
        for i in range(1,n+1):
            if i==k:
                min_costs[i] = 0
            else:
                min_costs[i] = inf
        
        # run dijkstras
        pq = [(0,k)]
        heapq.heapify(pq)
        visited = set()
        while pq:
            cost, node = heapq.heappop(pq)
            for child, cost_child in adj[node]:
                if child not in visited:
                    heapq.heappush(pq, (cost+cost_child, child))
                    if cost+cost_child < min_costs[child]:
                        min_costs[child] = cost+cost_child              
            visited.add(node)
        
        max_time = max(min_costs.values())
        if max_time == inf:
            return -1
        return max_time
