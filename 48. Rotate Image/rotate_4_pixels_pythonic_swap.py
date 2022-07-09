"""
Rotate 4 pixels at a time and then move to the next set of pixels.
Use 4 pointers, left = 0, right = n-1, top = 0 and bottom = n-1.
After rotating one set of pixels, move to the next ones. 
topleft moves right, topright moves bottom, bottomright moves left and bottomleft moves up. Use for loop for this.
Once an outer level is done, move all pointers inwards and repeat on the next level.

For rotation. Cache the top left and then move the pixels in clockwise motion starting from bottom left. 
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        left = 0
        right = n-1
        # when left is greater than right, we have completed the last layer
        while left < right:
            top = left
            bottom = right
            
            for i in range(right-left):
                # pythonic swap
                matrix[top][left+i], matrix[top+i][right], matrix[bottom][right-i], matrix[bottom-i][left] = matrix[bottom-i][left], matrix[top][left+i], matrix[top+i][right], matrix[bottom][right-i]
            
            # move to inward level
            left += 1
            right -= 1
    