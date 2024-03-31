"""
Track 3 pointers, latestMinK, latestMaxK and latestOutOfRange seen so far.
For any index i, get the above 3 data points.
For example for [5,3,7,3,4,5,4] where minK = 3 and maxK = 5. For index 6, latestMinK = 3, latestMaxK = 5 and latestOutOfRange = 2.
For index 6, we can see that we have 1 valid subarray which ends at index 6 = [3,4,5,4].
We got this by min(latestMinK, latestMaxK) - latestOutOfRange == min(3,5) - 2 == 1. This value can be nagative if latestOutOfRange is to the right of the other 2 values, so take 0 when negative.
So for each index we will see if a subarray ends at that index, does it for any valid subarray or not.

O(n) time to iterate through the array once.
O(1) space.
"""

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
         
        latestMinK = -1
        latestMaxK = -1
        latestOutOfRange = -1

        res = 0
        for i in range(len(nums)):
            if nums[i] == minK:
                latestMinK = i
            if nums[i] == maxK:
                latestMaxK = i
            if nums[i] > maxK or nums[i] < minK:
                latestOutOfRange = i
            
            # take max to avoid taking negative, this happens when latestOutOfRange is to the right of min(latestMinK, latestMaxK)
            num_valid_arrays_at_i = max(
                0,
                min(latestMinK, latestMaxK) - latestOutOfRange
            )

            res += num_valid_arrays_at_i
        
        return res
