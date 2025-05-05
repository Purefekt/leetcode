"""
Since rows and cols are sorted:
if we go right, the number increases
if we go down, the number increases
if we go left, the number decreases
if we go up, the number decreases
We start at bottom left, if its the target, return True
Else if this is smaller than target, we go right
Else if this is larger than target, we go up
If we go out of bound, we stop search
NOTE: Binary solution works by iterating through all rows and running binary search on all rows which is O(nlogm)

O(m+n) time.
O(1) space.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # a cell to the top is smaller
        # a cell to the right is larger
        # start from bottom left
        # if we find target, return True
        # if current cell is smaller than target, go right
        # if current cell is larger than target, go up
        # if out of bound, return False

        m,n = len(matrix), len(matrix[0])
        
        # start at bottom left
        i = m-1
        j = 0

        while 0<=i<m and 0<=j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        
        return False
