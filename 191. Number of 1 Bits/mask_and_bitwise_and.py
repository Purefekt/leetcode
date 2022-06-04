"""
Use a mask of value 1 (...000001). If a number is & with this mask, then the least significant bit will be 1 if the numbers LSB is 1 else it will be 0. This way we will know if the LSB is 1. Then we shift bits by 1 and repeat 31 more times for all 32 bits.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        bit_count = 0
        mask = 1
        
        for i in range(32):
            if n & mask == 1:
                bit_count = bit_count + 1
            
            # shift n to right by 1 bit
            n = n >> 1
        
        return bit_count