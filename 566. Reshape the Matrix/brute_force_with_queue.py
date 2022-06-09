"""
Brute force. Store elements of matrix in a queue. Then build a new matrix by building rows till len c and adding them to another list.
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # get dimensions of input matrix
        m = len(mat)
        n = len(mat[0])
        
        # if output matrix dimensions are compatible, proceed, else return original matrix
        if m*n == r*c:
            
            # build a queue of all nums in the matrix
            queue = collections.deque()
            for i in range(m):
                for j in range(n):
                    queue.append(mat[i][j])
            
            # build new matrix row by row using the elements
            new_mat = []
            curr_row = []
            
            while queue:
                num = queue.popleft()
                
                # build the row
                if len(curr_row) < c:
                    curr_row.append(num)
                # add this row to the new_mat and reset curr_row
                if len(curr_row) == c:
                    new_mat.append(curr_row)
                    curr_row = []
            
            return new_mat
        
        # else dimensions are incompatible
        return mat
    