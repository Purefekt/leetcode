class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # get in degree and out degree of all nodes
        in_deg = {i:0 for i in range(1, n+1)}
        out_deg = {i:0 for i in range(1, n+1)}

        for a,b in trust:
            in_deg[b] += 1
            out_deg[a] += 1
        
        # go through in degree, all nodes must have 0 in degree and 1 must have in degree n-1
        for node in in_deg:
            if in_deg[node] == n-1 and out_deg[node] == 0:
                return node

        return -1
