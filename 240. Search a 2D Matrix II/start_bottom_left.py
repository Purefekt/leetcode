"""
Start at the bottom left cell using two pointers, one for row and one for column.
Start the row pointer at m-1 and column pointer at 0.
If the target is found, return true. Else if the target is larger than the cell, skip to the next column. If the target is smaller than the cell, move to the above row
Keep doing this till either target it found or if the row pointer becomes less than 0 or the column pointer crosses max num of columns, then return False.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        r = m-1
        c = 0
        
        while r>=0 and c<n:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                c += 1
            elif target <= matrix[r][c]:
                r -= 1
        
        return False
    