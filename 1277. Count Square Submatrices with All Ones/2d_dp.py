"""
2D dp.
Create a dp matrix of size m*n and fill first row and first col same as matrix.
Each cell in the matrix is the number of squares we can make when ending at that square.
Final result is the sum of all cells of dp matrix.
For any cell, if matrix[i][j] is 0, dp[i][j] will also be 0 since we cannot make any squares which end at this cell.
If a cell is 1, then we can make at min(left, top, diagnol) + 1 number of squares.
If this is the dp matrix and x = 1
[1,1]
[1,x]
We can make 2 squares which end at x, since one square of size 1 and one square of size 2.
If this is the dp matrix and x = 1
[1,1]
[0,x]
Then we can make 1 square which end at x, since one square of size 1.

O(m*n) time to build dp matrix and then fill it.
O(m*n) space used by dp matrix.
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        dp = []
        for i in range(m):
            dp_row = []
            for j in range(n):
                dp_row.append(0)
            dp.append(dp_row)
        
        res = 0
        for i in range(m):
            dp[i][0] = matrix[i][0]
            res += matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]
            res += matrix[0][j]
        
        # correct for taking top left cell twice
        if matrix[0][0] == 1:
            res -= 1
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res += dp[i][j]
            
        return res
