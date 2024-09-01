class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        res = []
        for i in range(m):
            res_row = [0 for j in range(n)]
            res.append(res_row)
        
        if m*n != len(original):
            return []
        
        idx = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = original[idx]
                idx += 1
        
        return res
