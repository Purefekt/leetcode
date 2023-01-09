"""
Dynamic Programming. Initialize a dp matrix of len m*n
Since we can only move right or down, we can only move right on the last row and only move down in the last column.
Set dp[-1][-1] to grid[-1][-1] and initialize the values of last row and last column by moving left from and up respectively
Then fill out the dp array bottom to top, right to left

O(m*n) time
O(m*n) space, can do this in O(1) space
""" 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        # build dp matrix
        dp = []
        for i in range(m):
            dp_row = []
            for j in range(n):
                dp_row.append(0)
            dp.append(dp_row)

        # initialize last row and last col of dp
        dp[-1][-1] = grid[-1][-1]
        for i in range(m-2,-1,-1):
            dp[i][-1] = grid[i][-1] + dp[i+1][-1]
        for j in range(n-2,-1,-1):
            dp[-1][j] = grid[-1][j] + dp[-1][j+1]
        
        # fill the remaining cells bottom to top, right to left
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])

        return dp[0][0]
