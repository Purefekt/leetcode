"""
Binary Search.
If the right neighbhor to the pivot is larger than it, then there must be a peak to the right, shift l=p+1
If the left neighbhor to the pivot is larger than it, then there must be a peak to the left, shift r=p-1.
Else the pivot is larger than both left and right, return it.

O(logn) time to perform binary search.
O(1) space to track pointers
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1

        while l<=r:
            p = (l+r)//2

            # check if right neighbhor is greater
            if p+1 < len(nums) and nums[p] < nums[p+1]:
                l = p+1
            # check if left neighbhor is greater
            elif p-1 >= 0 and nums[p-1] > nums[p]:
                r = p-1
            # if none is greater, this must be a peak
            else:
                return p
