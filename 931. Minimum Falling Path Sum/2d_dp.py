"""
2D DP.
Create dp matrix of n*n.
Last row is same as matrix.
Starting filling from 2nd last row till first row.
Fill from left to right, at each cell dp[i][j] = matrix[i][j] * min(left diag, bottom, right diag).
Return min from first row.

O(n^2) time for 2d matrix dp.
O(n^2) space for dp matrix.
"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        dp = []
        for i in range(n):
            dp_row = []
            for j in range(n):
                dp_row.append(0)
            dp.append(dp_row)
        
        for j in range(n):
            dp[-1][j] = matrix[-1][j]
        
        for i in range(n-2, -1, -1):
            for j in range(n):
                left = math.inf
                if j > 0:
                    left = dp[i+1][j-1]
                down = dp[i+1][j]
                right = math.inf
                if j<n-1:
                    right = dp[i+1][j+1]
                
                dp[i][j] = matrix[i][j] + min(left, down, right)
        
        return min(dp[0])
        