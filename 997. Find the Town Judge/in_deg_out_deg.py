class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # in deg and out deg
        in_deg = {i:0 for i in range(1, n+1)}
        out_deg = {i:0 for i in range(1, n+1)}
        for src, dst in trust:
            in_deg[dst] += 1
            out_deg[src] += 1
        
        candidate = None
        for k,v in in_deg.items():
            if v == n-1:
                candidate = k
                break
        
        if not candidate:
            return -1
        
        if out_deg[candidate] == 0:
            return candidate
        return -1
