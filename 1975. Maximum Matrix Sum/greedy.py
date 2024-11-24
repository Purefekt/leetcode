"""
Greedy.
If the count of negative numbers is even, we can make all neg numbers into positive.
If the count is odd, we can make the smallest absolute value negative.

O(n^2) time to traverse the matrix to get the absolute sum, min abs int and the count of neg numbers.
O(1) space.
"""

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        # get absolute sum of the matrix
        # also get total number of negative numbers and the largest negative number
        n = len(matrix)

        total = 0
        neg_count = 0
        min_abs = math.inf
        for i in range(n):
            for j in range(n):
                total += abs(matrix[i][j])
                min_abs = min(min_abs, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    neg_count += 1
        
        if neg_count % 2 == 0:
            return total
        else:
            return total - (2*min_abs)
