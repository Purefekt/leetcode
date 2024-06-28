"""
Greedy sorting.
We need to assign the nodes with the highest degree the highest value.
Get the degree of each node.
Sort them through degrees.
Assign values in reverse order starting from 1.

O(n^2) time since we can have at max n^2 edges. Sorting takes nlogn time.
O(n) space since the adj list has n keys with each having a constant number of value.
"""

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        adj = {i:0 for i in range(n)}
        for a,b in roads:
            adj[a] += 1
            adj[b] += 1
        
        # sort with in degree
        degree = []
        for k,v in adj.items():
            degree.append((v,k))
        degree.sort(reverse=True)

        # assign values
        val = n
        values = {}
        for i in range(len(degree)):
            values[degree[i][1]] = n
            n -= 1
        
        res = 0
        for a,b in roads:
            res += values[a] + values[b]
        
        return res
