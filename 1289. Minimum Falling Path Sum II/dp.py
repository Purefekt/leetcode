"""
DP 2d.
Create a dp matrix of size n*n.
Full first row as is.
Start filling row wise from the 2nd row.
Get the min_val from the previous row, skip if the column is same.
Update dp cell.

O(n^3) time for a nested loop in the matrix, and for each we need to loop over the previous row.
O(n^2) space used by the 2d dp matrix.
"""

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        dp = []
        for i in range(len(grid)):
            dp_row = []
            for j in range(len(grid)):
                dp_row.append(0)
            dp.append(dp_row)
        
        for j in range(len(grid)):
            dp[0][j] = grid[0][j]
        
        for i in range(1, len(grid)):
            for j in range(len(grid)):
                min_val = math.inf
                for k in range(len(grid)):
                    if j == k:
                        continue
                    min_val = min(min_val, dp[i-1][k])
                dp[i][j] = grid[i][j] + min_val
        
        return min(dp[-1])
