"""
At a point, we only need to know the min boundary of either side to find the units of water to trap at an index.
We can use a left pointer and right pointer, left init at 0 and right init at right end.
Keep track of the max value at both ends
If the maxL <= maxR, then we will update the result with the index at l.
Else, update the result with the index at r.
Move the pointer we updated, l+=1 or r-=1 and update the maxL or maxR

O(n) time for 1 pass over the height array
O(1) space to store the l,r,maxL,maxR in constant space
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR = height[r]

        res = 0
        while l<r:
            if maxL <= maxR:
                water = maxL - height[l]
                if water > 0:
                    res += water
                l += 1
                maxL = max(maxL, height[l])
            else:
                water = maxR - height[r]
                if water > 0:
                    res += water
                r -= 1
                maxR = max(maxR, height[r])
        
        return res