"""
Using constant extra space. Use the first row and first column as flags. Set elements in that row and col to 0s when we find an element in the matrix to be 0. 
Use 1 extra variable to keep track of the 0 in the first column (since it overlaps with first element of first row at matrix[0][0])
First set all columns from the 2nd column to 0s where we find a 0 in the first column
Then set all rows from the 2nd row to 0s where we find a 0 in the first row
Finally if both matrix[0][0] (for row) and cell_extra_col are 0, then set both first row and col to 0, else set the row OR col OR none to 0s.
O(m*n) time since we iterate through all cells in the matrix
O(1) space since we use constant space to store the flag for the first col
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        m,n = len(matrix), len(matrix[0])
        
        cell_extra_col = None #for matrix[0][0] for rows
        
        # go through the matrix and set the flags in the first row and column and the extra cell which overlaps at [0][0]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # set column flag
                    matrix[0][j] = 0
                    # set row flag
                    if i == 0:
                        cell_extra_col = 0
                    else:
                        matrix[i][0] = 0
        
        # change all columns to 0s acc to the flags in first row (except first column)
        for c in range(1,n):
            if matrix[0][c] == 0:
                for r in range(m):
                    matrix[r][c] = 0
        # change all rows to 0s acc to the flags in first column (except first row)
        for r in range(1,m):
            if matrix[r][0] == 0:
                for c in range(n):
                    matrix[r][c] = 0
        
        # if [0][0] for both row and col are 0, then set first row and col to 0s. Else set only the row or col
        if cell_extra_col == matrix[0][0] and cell_extra_col == 0:
            for c in range(n):
                matrix[0][c] = 0
            for r in range(m):
                matrix[r][0] = 0
        elif cell_extra_col == 0: # only first row
            for c in range(n):
                matrix[0][c] = 0
        elif matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0
                