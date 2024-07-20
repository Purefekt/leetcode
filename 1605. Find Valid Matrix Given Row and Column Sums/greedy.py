"""
Greedy.
Fill the result matrix top left to bottom right.
Place the best possible number in that slot.
Maintain an array to store the sum of all numbers in a row till ith row and same for col.
Place min(rowSum[i] - cur_row_sum[i], colSum[j] - cur_col_sum[j]) in current cell and update these arrays.

O(m*n) time to create res and build res.
O(m+n) space used by both arrays.
"""

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        m,n = len(rowSum), len(colSum)

        cur_row_sum = [0] * m
        cur_col_sum = [0] * n

        res = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            res.append(row)
        
        for i in range(m):
            for j in range(n):
                cell_val = min(rowSum[i] - cur_row_sum[i], colSum[j] - cur_col_sum[j])
                res[i][j] = cell_val
                cur_row_sum[i] += cell_val
                cur_col_sum[j] += cell_val
        
        for row in res:
            print(row)
        
        return res
