"""
The number of lazers between any two rows with atleast 1 security device will be the product of number of security devices in these 2 rows.
Thus get the number of security devices per row, ignore if 0.
Then result is sum of the product of all adjacent pairs.

O(m*n) time to go through the grid.
O(m) space to store per_row, at max we will store m number of integers. Can be optimized to use O(1) space, too lazy to code. 
"""

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        per_row = []

        for b in bank:
            num_this_row = 0
            for c in b:
                if c == '1':
                    num_this_row += 1
            if num_this_row > 0:
                per_row.append(num_this_row)
        
        res = 0
        for i in range(len(per_row)-1):
            res += per_row[i] * per_row[i+1]

        return res
