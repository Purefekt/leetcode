"""
Extra Space sol.
Iterate through the matrix and find all cells where we have a 0
Store the row and col in sets. At the end we know all rows and all cols which must be set to 0
Set these rows and cols to zero
O(m*n) time since we iterate through all cells in the matrix
O(m+n) space to store two sets for row and cols. In the worst case, entire matrix is 0s and we store m elements in set row and n elements in set col
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        zero_row, zero_col = set(), set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        
        # make all rows in zero_row and all cols in zero_col 0
        for r in zero_row:
            for j in range(n):
                matrix[r][j] = 0
        for c in zero_col:
            for i in range(m):
                matrix[i][c] = 0
            