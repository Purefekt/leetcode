"""
Calculate the maximum number of people which can go to any node.
Each node by default has 1 person and then they travel towards 0th node via other node.
So we can find the max number of people at any node.
The amount of fuel needed for people to travel from a node to the next is ceil(num people / seats).
So we do this for each node and get the result.

O(n) time to run dfs and go through each node at max once.
O(n) space to store the adj list, num_people matrix and stack space for dfs.
""" 

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        if not roads:
            return 0

        # build the graph
        adj = collections.defaultdict(list)
        for src, dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)
        
        # get max number of people at each node
        visited = set()
        num_people = {i:1 for i in range(len(adj))}
        def dfs(node):
            visited.add(node)
            for child in adj[node]:
                if child not in visited:
                    num_people[node] += dfs(child)
            
            return num_people[node]
        dfs(0)
        
        # the fuel needed at each node (other than 0th) will be ceil(num_people / seats)
        res = 0
        for i in range(1, len(num_people)):
            res += math.ceil(num_people[i]/seats)
        
        return res
