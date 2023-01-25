"""
If a is 0, then b can be at max sqrt(c), thus the valid ints are from [0, sqrt(c)]
For these numbers we set each to a and find b_squared which is c-a*a
Then we use int(sqrt(b_squared)) to get the integer square root and call it b.
If b*b == b_squared, this means a and b are both integers and return True. If we go through all valid options and find none, return False
NOTE: we can do this with contant memory by looping from 0 till int(sqrt(c))+1

O(sqrt(c)*logc) time. To loop over sqrt(c) options and each sqrt() call can take logc time in the worst case
O(1) space
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        # get potential candidates
        options = []
        for i in range(int(sqrt(c))+1):
            options.append(i)
        
        # check b values one by one
        for num in options:
            a = num
            b_squared = c - a*a
            b = int(sqrt(b_squared))
            
            # b**2 must be equal to b_squared for it to be true
            if b**2 == b_squared:
                return True
        return False
        