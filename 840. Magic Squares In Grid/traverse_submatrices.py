"""
Identify all starting positions of possible 3x3 matrices.
Test each such submatrix.

O(m*n) time to traverse the grid m-2*n-2 times. For each we traverse an additional 9 times.
O(1) space since the submatrix takes O(9) space.
"""

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        if m<3 or n<3:
            return 0

        def validate_matrix(matrix):
            ideal_set = {1,2,3,4,5,6,7,8,9}
            # validate numbers
            cur_set = set()
            for i in range(3):
                for j in range(3):
                    if matrix[i][j] not in ideal_set:
                        return False
                    if matrix[i][j] in cur_set:
                        return False
                    if matrix[i][j] in ideal_set:
                        cur_set.add(matrix[i][j])
            if len(cur_set) != 9:
                return False
            
            # get sums of all rows and cols and diagnols
            base_sum = sum(matrix[0])   
            if sum(matrix[1]) != base_sum or sum(matrix[2]) != base_sum:
                return False
            col1 = 0
            col2 = 0
            col3 = 0
            for i in range(3):
                col1 += matrix[i][0]
                col2 += matrix[i][1]
                col3 += matrix[i][2]
            if col1 != base_sum or col2 != base_sum or col3 != base_sum:
                return False 
            diag1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
            diag2 = matrix[0][2] + matrix[1][1] + matrix[2][0]
            if diag1 != base_sum or diag2 != base_sum:
                return False
            return True

        res = 0
        for i in range(m-2):
            for j in range(n-2):
                # this is the top left cell in a 3x3 graph. Build a 3x3 matrix
                cur_mat = []
                for r in range(3):
                    mat_row = []
                    for c in range(3):
                        mat_row.append(grid[i+r][j+c])
                    cur_mat.append(mat_row)
                if validate_matrix(cur_mat) is True:
                    res += 1 
            
        return res
