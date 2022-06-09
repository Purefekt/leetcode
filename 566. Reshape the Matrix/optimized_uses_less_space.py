"""
Optimized. Add elements to the new_matrix as we are going through all elements of the original matrix. Uses less space than brute force with queue.
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # get dimensions of input matrix
        m = len(mat)
        n = len(mat[0])
        
        # if output matrix dimensions are compatible, proceed, else return original matrix
        if m*n == r*c:
            
            new_mat = []
            curr_row = []
            
            for i in range(m):
                for j in range(n):
                    num = mat[i][j]
                    
                    # keep adding nums to the current row till length c
                    if len(curr_row) < c:
                        curr_row.append(num)
                    # add a full row to new matrix and reset current row
                    if len(curr_row) == c:
                        new_mat.append(curr_row)
                        curr_row = []
            
            return new_mat
                        
        # else dimensions are incompatible
        return mat
    