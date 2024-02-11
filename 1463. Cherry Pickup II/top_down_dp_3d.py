"""
Top down dp 3D.
Recursive function takes in 3 params, i,j,k.
i is the row number, j is the column of robo1 and k is the column of robo2.
Base case if if i==m, then return 0 since we cant go any more rows deeper.
Base case if j or k is out of bounds then we cant go further and return 0.
Now we have 2 cases, if j==k, we only add the value of that cell once. Else we add both the cells separately.
Robo1 can go in 3 directions and Robo2 can go in 3 directions. Combined there are 9 combinations.
Memoiz it.

O(m*n*n) time where m is number of rows and n is number of columns.
O(m*n*n) space taken by the memoization table. O(n) by the stack.
"""

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        memo = {}
        def helper(i, j, k):
            if (i,j,k) in memo:
                return memo[(i,j,k)]

            if i == m:
                memo[(i,j,k)] = 0
                return 0
            
            if j<0 or j>=n or k<0 or k>=n:
                return 0
            
            # if both are in different columns
            res = 0
            if j != k:
                res = grid[i][j] + grid[i][k] + max(
                    helper(i+1, j-1, k-1),
                    helper(i+1, j-1, k),
                    helper(i+1, j-1, k+1),
                    helper(i+1, j, k-1),
                    helper(i+1, j, k),
                    helper(i+1, j, k+1),
                    helper(i+1, j+1, k-1),
                    helper(i+1, j+1, k),
                    helper(i+1, j+1, k+1)
                )

            # if both are in same columns
            else:
                res = grid[i][j] + max(
                    helper(i+1, j-1, k-1),
                    helper(i+1, j-1, k),
                    helper(i+1, j-1, k+1),
                    helper(i+1, j, k-1),
                    helper(i+1, j, k),
                    helper(i+1, j, k+1),
                    helper(i+1, j+1, k-1),
                    helper(i+1, j+1, k),
                    helper(i+1, j+1, k+1)
                )
            
            memo[(i,j,k)] = res
            return res
        
        return helper(0, 0, n-1)
            