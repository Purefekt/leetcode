class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # build dp matrix of size m*n
        dp = []
        for i in range(m):
            dp_row= []
            for j in range(n):
                dp_row.append(0)
            dp.append(dp_row)
        
        # set last col and last row to 1 since the unique paths from those coordinates will be 1
        for j in range(n):
            dp[m-1][j] = 1
        for i in range(m):
            dp[i][n-1] = 1
        
        # fill the dp matrix from right to left from dp[m-2][n-2]
        # each element will be the sum of itsself + right cell + bottom cell
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i][j] + dp[i+1][j] + dp[i][j+1]   
        
        # answer will be at [0][0]
        return dp[0][0]
                