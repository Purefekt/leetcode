"""
Get the in degree of all nodes.
Get a list of all nodes whose in deg is 0.
If there are more than 1, return -1.
If there is just 1, return that.

O(n+m) time. n time to initialize in degree hashmap and m time to go through all m edges.
O(n) space to store in degrees of all nodes.
"""

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        # get in degrees of each node
        in_deg = {i:0 for i in range(n)}

        for src, dst in edges:
            in_deg[dst] += 1
        
        cand = []
        for k,v in in_deg.items():
            if v == 0:
                cand.append(k)
            if len(cand) > 1:
                return -1
            
        return cand[0]
