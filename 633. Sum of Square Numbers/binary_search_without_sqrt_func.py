"""
Binary search without using sqrt function
Create the list of options which are [0, int(sqrt(c))]
Iterate through the options and set the current element to a
b_squared will be c - a*a. We will use binary search to determine if b_squared is a perfect square
Run binary search of [0, b_squared], if at any point mid*mid == b_squared, return True,
else shift r to mid-1 if larger else l to mid+1
NOTE: we can do this with contant memory by looping from 0 till int(sqrt(c))+1

O(sqrt(c) * logc) time. O(sqrt(c)) time to iterate over all options and O(logc) to run binary search for each
O(1) space
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        options = []
        for i in range(0, int(sqrt(c))+1):
            options.append(i)
        
        for a in options:
            b_squared = c - a*a

            # find an integer mid in [0, b_squared] where m*m == b_squared
            l = 0
            r = b_squared
            while l<=r:
                mid = (l+r)//2
                
                if mid*mid == b_squared:
                    return True
                elif mid*mid > b_squared:
                    r = mid-1
                else:
                    l = mid+1
        
        return False
