class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        # get max for each row
        row_min = []
        for row in matrix:
            row_min.append(min(row))
        
        # get max for each col
        col_max = []
        m,n = len(matrix), len(matrix[0])
        for j in range(n):
            max_val = 0
            for i in range(m):
                max_val = max(max_val, matrix[i][j])
            col_max.append(max_val)

        # go through all elements and see if it is min
        res = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    res.append(matrix[i][j])
        
        return res
