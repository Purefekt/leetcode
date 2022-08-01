"""
Binary search
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        
        # edge case
        if x == 1:
            return 1
                       
        l = 0
        r = x
        
        while l < r-1:
            pivot = l + (r-l)//2
            
            if pivot*pivot == x:
                return pivot
            elif pivot*pivot > x:
                r = pivot
            elif pivot*pivot <= x:
                l = pivot
        
        return l
        