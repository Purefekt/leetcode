"""
Run Binary Search twice.
Run binary search, if we find the target then dont exit. Set it to the start and search towards the left of the pivot by setting right to pivot-1. This way if the target exists in the array, we are gauranteed to find the first occurance of it.
Similarly run binary search to find the target. When we find it, set it to end and search for it again in the array to the right of pivot by setting left to pivot+1.
Also keep a boolean to detect if target was found.

O(logn) time to run binary search twice
O(1) space.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        target_found = False

        # binary search to find start
        l = 0
        r = len(nums)-1
        start = 0
        while l<=r:
            p = (l+r)//2
            if nums[p] == target:
                target_found = True
                start = p
                r = p-1
            elif nums[p] > target:
                r = p-1
            else:
                l = p+1
        

        # binary search to find end
        l = 0
        r = len(nums)-1
        end = 0
        while l<=r:
            p = (l+r)//2
            if nums[p] == target:
                target_found = True
                end = p
                l = p+1
            elif nums[p] > target:
                r = p-1
            else:
                l = p+1
        
        if not target_found:
            return [-1,-1]
        return [start,end]

        