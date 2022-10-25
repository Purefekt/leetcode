"""
BRUTE FORCE (TLE)
Check all from 1 till the first possible answer.

O(n*m) time. We iterate over all the piles in pile of len n. For each pile we check from speed 1 till m, where m is the largest number of bananas in a pile.
O(1) space to store value of k and h_now in constant sapce.
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = 1
        h_now = 0
        
        while True:
            h_now = 0
            
            for pile in piles:
                h_now += pile//k
                if pile%k != 0:
                    h_now += 1
                if h_now > h:
                    break
            print(h_now)
            if h_now <= h:
                return k
            k += 1
            