class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # consider 2d matrix as 1d sorted array. We will need conversion from 1d to 2d indices.
        
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1
        num_elements_row = len(matrix[0])
        
        while (left <= right):
            pivot = (left + right) // 2
            pivot_row, pivot_col = self.get_index(pivot, num_elements_row)
            
            if target == matrix[pivot_row][pivot_col]:
                return True
            elif target > matrix[pivot_row][pivot_col]:
                left = pivot + 1
            elif target < matrix[pivot_row][pivot_col]:
                right = pivot - 1
        
        return False
        
    
    def get_index(self, one_d_index, num_elements_row):
        # row will be one_d_index // num of elements per row
        row = one_d_index // num_elements_row
        # col will be one_d_index % num of elements per row
        col = one_d_index % num_elements_row
        
        return row, col
        