"""
Sliding window with frequency hashmap.
Keep a hashmap to maintain frequency of nums in current subarray.
Also track the total.
Inc count on right pointer and dec count on left pointer.
If the count of any num becomes 0, remove it from the hashmap.
If the hashmap size == k, update result.

O(n) time for sliding window.
O(k) space used by counts hashmap.
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        counts = collections.defaultdict(int)

        # get the first subarray
        total = 0
        for i in range(k):
            counts[nums[i]] += 1
            total += nums[i]
        
        res = 0
        if len(counts) == k:
            res = total

        l = 0
        r = k
        while r<len(nums):
            total += nums[r]
            total -= nums[l]

            counts[nums[l]] -= 1
            if counts[nums[l]] == 0:
                del counts[nums[l]]
            
            counts[nums[r]] += 1

            if len(counts) == k:
                res = max(res, total)

            r += 1
            l += 1
        
        return res
