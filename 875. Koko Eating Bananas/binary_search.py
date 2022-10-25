"""
Binary search.
Set l=1 and r=max(piles). the pivot will be the k speed for which we check currently
Run a loop till l==r. For each k, check the hours taken. If hours taken <= k, update right to pivot, else update left to pivot + 1
The loop ends when r==l, return right

O(nlogm) time. Initial search space is 1 to m, where m is the max(piles). This is cut down to logm due to binary search. For each search we run through all piles of len n.
O(1) space. Constant space to store l,r and k
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        
        while l<r:
            h_now = 0
            k = (r+l)//2
            
            for pile in piles:
                h_now += math.ceil(pile/k)
            
            if h_now <= h:
                r = k
            else:
                l = k+1
        
        return r
    