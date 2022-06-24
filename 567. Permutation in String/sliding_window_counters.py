"""
Sliding window.

Use a sliding window of size s1. Move it accross s2 by incrementing by 1. On each iteration check if the counter of s1 and substring_s2 are the same. If they are then return True.
If while loop completes, which means we did not find such a permutation.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter_s1 = collections.Counter(s1)

        # use sliding window of siz s1 and move it by 1 on s2. For each iteration check if the counter of s1 == substring_s2
        l = 0
        r = len(s1)
        
        while r <= len(s2):
            substring_s2 = s2[l:r]
            counter_sub_s2 = collections.Counter(substring_s2)
            
            if counter_s1 == counter_sub_s2:
                return True
            
            l += 1
            r += 1
        
        return False
    