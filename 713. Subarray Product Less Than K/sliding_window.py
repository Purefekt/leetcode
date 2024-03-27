"""
Sliding window.
Keep a sliding window and the current product in that window.
Increase the window by shifting right.
If product >= k, we can shrink the window by incrementing left and diving nums[l] from the product.
For each window where product < k, the number of valid subarrays are (r-l+1).
Iterate using right pointer from 0 till n.
Update the product.
First fix the product by shifting left till product < k, make sure not to move l past r.
Update res and continue.

O(n) time for one pass over nums.
O(1) space.
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            return 0

        l = 0
        product = 1
        res = 0

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k and l <= r:
                product //= nums[l]
                l += 1
            
            res += (r-l+1)
        
        return res
