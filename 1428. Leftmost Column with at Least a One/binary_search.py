"""
For each row, run binary search to find the first occurance of a 1.
Some optimizations:
If the last element of a row is 0, skip this row since there are no 1s.
If the first element of a row is 1, return 0 since it cant get better.
Only run binary search if the current row has a 1 in the currently best column position. 
Only run binary search from 0 -> currently running best column position.

O(mlogn) time where we have m rows and n is the length of each row.
O(1) space since we are using pointers. 
"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        m,n = binaryMatrix.dimensions()

        res = math.inf

        for i in range(m):            
            if binaryMatrix.get(i, n-1) == 0:
                continue
            if binaryMatrix.get(i, 0) == 1:
                return 0
            if res == math.inf or binaryMatrix.get(i, res) == 1:
                l = 0
                if res == math.inf:
                    r = n-1
                else:
                    r = res
                while l<=r:
                    p = (l+r)//2

                    if binaryMatrix.get(i, p) == 0:
                        l = p+1
                    
                    else:
                        r = p-1
                
                res = min(res, l)

        if res == math.inf:
            return -1
        return res
