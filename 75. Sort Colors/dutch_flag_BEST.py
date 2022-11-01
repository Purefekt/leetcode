"""
One pass. Dutch flag problem. 3 pointer
Have a L pointer which acts as the boundary for 0s, have a R pointer which acts as a boundary for the 2s.
Use a current pointer and move it along the nums and swap based on conditions.
Initialize c and l to 0 and r to len(nums)-1
If c is a 2, swap with r and move right inside. This is because r was at the right end and now it has a 2, we cannot do better
if c is a 0, swap it with l and move l and c outside. We start c and l at the left most end, once it has a 0, we cannot do better
if c is a 1, move c outside. Stop when c passes r
O(n) time since we iterate over all nums once
O(1) space to store c,l and r
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        l = 0
        r = len(nums)-1
        
        while c<=r:
            if nums[c] == 0:
                nums[c], nums[l] = nums[l], nums[c]
                c += 1
                l += 1
            elif nums[c] == 1:
                c += 1
            elif nums[c] == 2:
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1
                