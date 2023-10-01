"""
Sort the array, since the subsequence remains the same since we only care about the numbers in the subsequences and not their order.
If we have [6,4,3] and target is 7, so valid subsequences are [4], [4,3], [3] if we sort we get [3,4,6] and valid subsequences is still 3-> [3], [3,4], [4].
Keep a right pointer and iterate through the sorted nums.
Decrement right till left + right <= target. Since it is sorted, this is actually min + max.
Add 2^(r-l) to the result since if we have [3,3,6,8] and target is 10. If left is at 0 = 3 and right is at 2 = 6, then we have 2^2 subsequences since the 0th index is fixed and we have 2 remaining ones.

O(nlogn) time for sorting.
O(n) space for sorting
"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        mod = 10**9 + 7
        nums.sort()

        res = 0
        r = len(nums)-1
        for i in range(len(nums)):
            while (nums[i] + nums[r]) > target and i <= r:
                r -= 1
            if i<=r:
                res += (2**(r-i))
                res %= mod
        
        return res
