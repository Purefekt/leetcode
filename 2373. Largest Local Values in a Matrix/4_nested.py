class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)

        res = []
        for i in range(n-2):
            row = []
            for j in range(n-2):
                max_val = 0
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        max_val = max(max_val, grid[k][l])
                row.append(max_val)
            res.append(row)
        
        return res
        