"""
Top down dp.
Backtrack function takes the current pos and moves left.
If the ball goes out of bounds, return 1.
If number of moves left goes down to 0, return 0.
Go in all 4 directions and return the sum of them.
Use memoization on (i,j,moves left).

O(m*n*maxMove) time. The recursion runs for each combination of these.
O(m*n*maxMove) space to store the memoization table.
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        memo = {}
        def backtrack(i,j,moves_left):
            if (i,j,moves_left) in memo:
                return memo[(i,j,moves_left)]

            if i<0 or j<0 or i>=m or j>=n:
                memo[(i,j,moves_left)] = 1
                return 1
            
            if moves_left == 0:
                memo[(i,j,moves_left)] = 0
                return 0
            
            left = backtrack(i, j-1, moves_left-1)
            top = backtrack(i-1, j, moves_left-1)
            right = backtrack(i, j+1, moves_left-1)
            down = backtrack(i+1, j, moves_left-1)

            memo[(i,j,moves_left)] = left+top+right+down
            return left+top+right+down
        
        mod = 10**9 + 7
        return backtrack(startRow, startColumn, maxMove) % mod
