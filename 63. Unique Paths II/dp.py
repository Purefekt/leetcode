"""
Dynamic programming
Create a 2d dp array of size m*n. 
Create a set of coordinates of all positions where there is an obstacle
The goal cell will be 1 and all the cells in last row and col will be the cell in front of them, so fill them left to right
While filling, avoid obstacles and if a cell in the last row has an obstacle in front of it, set its val to 0
Use the same to fill the remaining cells, right to left bottom to top by adding the number of ways in the bottom and right cell, again avoid if its an obstacle cell

O(m*n) time. To traverse all nodes
O(m*n) space to maintain dp matrix. This can be O(1) space by using the input grid as dp matrix
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # edge case if the goal itself has an obstacle
        if obstacleGrid[-1][-1] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = []
        for i in range(m):
            dp_row = [0 for i in range(n)]
            dp.append(dp_row.copy())
        
        # get the obstacles
        obstacles = set()
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacles.add((i,j))
        
        # init dp matrix last row and last col
        dp[-1][-1] = 1
        for j in range(n-2, -1, -1):
            if (m-1, j) not in obstacles:
                dp[m-1][j] = dp[m-1][j+1]
        for i in range(m-2, -1, -1):
            if (i, n-1) not in obstacles:
                dp[i][n-1] = dp[i+1][n-1]
        
        # fill the remaining cells
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if (i,j) not in obstacles:
                    dp[i][j] = dp[i][j+1]+ dp[i+1][j]
    
        return dp[0][0]
