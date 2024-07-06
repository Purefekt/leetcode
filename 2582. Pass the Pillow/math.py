"""
Math.

O(1) time.
O(1) space.
"""

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        # get the iteration of loop
        idx = math.ceil(time/(n-1))

        # if odd, it is going right, if even it is going left
        # get the number of spaces jumped in the given direction
        if idx % 2 == 1:
            # go right
            jumps = time%(n-1)
            if jumps == 0:
                return n
            return 1+jumps
        
        else:
            # go left
            jumps = time%(n-1)
            if jumps == 0:
                return 1
            return n-jumps
