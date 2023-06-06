"""
use PREFIXSUM
Create a matrix where each cell is the sum of the matrix with its topleft position at (0,0) and bottomright at that cell.
This matrix will be used to calculate sumRegion in constant time.
For sumRegion:
The value in the matrix at bottomleft will be the sum where topleft is at 0,0
So we need to remove the matrixes above and to the left of the asked matrix
And then we need to add the overlapping part since it has been removed twice

O(1) time for sumRegion. O(m*n) to build the matrix.
O(m*n) space to store the matrix
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # build the matrix
        self.mat = []
        
        m = len(matrix)
        n = len(matrix[0])

        # init the matrix with all 0s
        for i in range(m):
            mat_row = []
            for j in range(n):
                mat_row.append(0)
            self.mat.append(mat_row)
        
        self.mat[0][0] = matrix[0][0]
        
        # fill the first row and col
        for j in range(1,n):
            self.mat[0][j] = matrix[0][j] + self.mat[0][j-1]
        for i in range(1,m):
            self.mat[i][0] = matrix[i][0] + self.mat[i-1][0]
        
        # fill other cells using the formula -> left self.mat + top self.mat + current matrix - topleft self.mat
        for i in range(1,m):
            for j in range(1,n):
                self.mat[i][j] = self.mat[i][j-1] + self.mat[i-1][j] + matrix[i][j] - self.mat[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # each cell in self.mat is the sum of all cells in a matrix where topleft is (0,0) and bottomright is that cell
        # use this logic to remove matrices and get the sum of region
        # sumregion = (row2,col2) - (row2,col1-1) - (row1-1,col2) + (row1-1,col1-1)
        # call them op1, op2, op3, op4
        op1 = self.mat[row2][col2]
        op2 = 0
        if col1-1 >= 0:
            op2 = self.mat[row2][col1-1]
        op3 = 0
        if row1-1 >= 0:
            op3 = self.mat[row1-1][col2]
        op4 = 0
        if row1-1 >= 0 and col1-1 >= 0:
            op4 = self.mat[row1-1][col1-1]
        
        return op1 - op2 - op3 + op4        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)