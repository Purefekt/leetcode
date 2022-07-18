"""
Extra space solution. Time O(m*n), space O(m+n).
In one pass go through the matrix and make a note of the rows and columns where we have 0s.
In the next go change those rows and cols to 0s
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        rows, cols = set(), set()
        
        # get the rows and cols which need to be changed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # change all marked rows to 0s
        for row in rows:
            for c in range(n):
                matrix[row][c] = 0
        # change all marked cols to 0s
        for col in cols:
            for r in range(m):
                matrix[r][col] = 0
    