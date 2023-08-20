"""
Nodes with in degree 0 can not be reached by any other node except themselves.
Nodes with in degree > 0 can be reached by some other node.
Thus we just need all the nodes with in degree == 0

O(n+e) time. e time to go over e number of edges to build in degree hashmap. Then iterate over that hashmap which has size n to find all nodes with in degree == 0.
O(n) space for the hashmap/
"""

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        # count in degrees of each node
        in_deg = {i:0 for i in range(n)}
        for src, dst in edges:
            in_deg[dst] += 1
        
        res = []
        for k,v in in_deg.items():
            if v == 0:
                res.append(k)
        
        return res
        