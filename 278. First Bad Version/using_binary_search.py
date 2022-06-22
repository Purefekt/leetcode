"""
Binary search
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low = 1
        high = n
        
        while low < high:
            pivot = low + (high-low)//2
            
            if isBadVersion(pivot) == True:
                high = pivot
            elif isBadVersion(pivot) == False:
                low = pivot + 1
            
        return low
    