"""
Greedy.
For each row, if there is a 1 in the 0th place, it will always add more value than if the 0th place was 0 and all the others were 1s.
Thus for each row, if the 0th element is 0, flip that row.
Now for column, flip a column if there are more 0s in it than 1s.

O(m*n) time since for row flipping and column flipping, we go through the entire matrix. Same for convert to int.
O(1) space since we modify input.
"""

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        # flip each row where the first num is 0
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        
        # flip each column where the number of 0s in that column > number of 1s
        for j in range(n):
            num_zeros = 0
            num_ones = 0
            for i in range(m):
                if grid[i][j] == 0:
                    num_zeros += 1
                else:
                    num_ones += 1
            if num_zeros > num_ones:
                for i in range(m):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        
        def convert_to_int(bin_arr):
            res = 0
            power = 0
            for j in range(len(bin_arr)-1, -1, -1):
                if bin_arr[j] == 1:
                    res += 2**power
                power += 1
            return res
        
        output = 0
        for row in grid:
            output += convert_to_int(row)
        
        return output
