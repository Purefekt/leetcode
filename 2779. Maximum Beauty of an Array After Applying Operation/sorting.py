"""
Sort the array.
Now we need to find the max subarray in which the first and last elements have a max diff of 2*k.
Use sliding window to find this array.

O(nlogn) time for sorting and then n time for sliding window.
O(n) space used by sorting.
"""

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        l = 0
        res = 0
        for r in range(len(nums)):
            while l<=r and nums[r] - nums[l] > k*2:
                l += 1
            res = max(res, r-l+1)
        
        return res
