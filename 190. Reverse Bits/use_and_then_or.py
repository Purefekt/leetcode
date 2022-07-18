"""
Use & between the input and 1. If the input has 0 in the LSB, then itll give a 0, else a 1. 
| (or) this with result.
Shift input to the right to move towards MSB and shift result to the left. Repeat this 32 times for 32 bits.
Output will be result shifted to the right by 1 since we move the result 33 times.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        
        result = 0
        
        for _ in range(32):
            bit = n & 1
            result = result | bit
            n = n>>1
            result = result << 1
        
        return result >> 1
    