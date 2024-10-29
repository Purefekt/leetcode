"""
2D dp.
Important thing to remember is that we need a path which starts from the first column.
Any random path which doesnt start at 0th column is not considered.
For this create a 2d dp array of size m*n.
We need to propogate a boolean True if the path started at column 0.
Set first column to (0, True).
We also need to travel column first top to bottom then next column.
Try all valid previous nodes for a given node ONLY if the previous node was True and it is smaller than current.

O(m*n) time to build dp array and then traverse it.
O(m*n) space used by dp array.
"""

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dp = []
        for i in range(m):
            dp_row = []
            for j in range(n):
                dp_row.append(0)
            dp.append(dp_row)
        
        # fill first col with True NOTE: we cannot move down in the first row
        for i in range(m):
            dp[i][0] = (0, True)
        
        res = 0
        # fill remaining
        for j in range(1,n):
            for i in range(m):
                max_prev = 0
                flag = False
                if i-1>=0 and j-1>=0 and grid[i-1][j-1] < grid[i][j] and dp[i-1][j-1][1] is True:
                    max_prev = max(max_prev, dp[i-1][j-1][0] + 1)
                    flag = True
                if j-1>=0 and grid[i][j-1] < grid[i][j] and dp[i][j-1][1] is True:
                    max_prev = max(max_prev, dp[i][j-1][0] + 1)
                    flag = True
                if i+1<m and j-1>=0 and grid[i+1][j-1] < grid[i][j] and dp[i+1][j-1][1] is True:
                    max_prev = max(max_prev, dp[i+1][j-1][0] + 1)
                    flag = True

                dp[i][j] = (max_prev, flag)
                res = max(res, max_prev)
           
        return res
