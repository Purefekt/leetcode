"""
Swap 4 cells at a time and move inward. 
Use 4 pointers. Set l and r to 0 and len(matrix)-1. 
Run a while loop till l<r. For each iteration of the while loop,set top=l and bot=r. run a for loop from 0 till r-l and swap the topleft, topright, botleft, botright.
Update l and r at the end of the for loop to move to an inward level

O(m) where m is the number of cells in the matrix. Each cell will be read and written to once.
O(1) in place swaps

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1
        
        while l<r:
            top = l
            bot = r
            for i in range(r-l):
                matrix[top+i][r], matrix[bot][r-i], matrix[bot-i][l], matrix[top][l+i] = matrix[top][l+i], matrix[top+i][r], matrix[bot][r-i], matrix[bot-i][l]
                
            l += 1
            r -= 1
        