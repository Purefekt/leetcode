"""
The 2d array can be though of as a 1d array. Since it is sorted we can run binary search
Need to encode 1d indexes to 2d indexes. row = 1d_index//num_cols. col = 1d_index//num_rows
O(log(m*n)) time since the search space is of size m*n on which we run binary search
O(1) space to store l,r,pivot
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m,n = len(matrix), len(matrix[0])
        
        def get_2d_index(index):
            row = index//n
            col = index%n
            return row, col
        
        l = 0
        r = m*n - 1
        
        while l<=r:
            pivot = l + (r-l)//2
            pivot_r, pivot_c = get_2d_index(pivot)
            
            if matrix[pivot_r][pivot_c] == target:
                return True
            elif matrix[pivot_r][pivot_c] > target:
                r = pivot - 1
            else:
                l = pivot + 1
        
        return False