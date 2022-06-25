"""
any power of 2 looks like - 1, 10, 100, 1000, 10000 in binary
Suppose x is a power of 2 => 1000
-x = ~x + 1 (twos complement). ~x => 0111. ~x + 1 => 1000
Thus for any power of 2, its negative is the same

for powers of 2, & between it and its neg is the same as it
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        if n & -n == n:
            return True
        return False
    