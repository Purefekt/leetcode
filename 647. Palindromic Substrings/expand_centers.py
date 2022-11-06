"""
Expand around centers. For any string of len n, we will have 2n-1 centers. n number of odd centers and n-1 even centers.
Run a for loop for length of n
for each iteration expand around the centers of i itself, which is off
and expand around i,i+1 as even
For every valid expansion (iteration of the while loop), increment the count

O(n^2) time. For loop for len n and while loop for each element
O(1) space to store left and right
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # expand around centers. 2n-1 centers
        if len(s) < 2:
            return 1
        
        count = 0
        for i in range(len(s)):
            # odd
            left = i
            right = i
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1
                count += 1
            
            # even
            left = i
            right = i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1
                count += 1
        
        return count
                   