"""
Sliding window and frequency hashmap.
Iterate on right side from 0 till n.
Each time add the element's frequency as part of the sliding window.
If at any point the freq goes over k, we need to shrink the window by moving left inside.
We have to move it to next index of the first occurance of nums[r].
Also make sure to decrement the frequencies of any other numbers while shrinking the window.

O(n) time, the outer loop goes till n and the inner loop ie value of l at max goes till n.
O(n) space used by frequency hashmap.
"""

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        freq = collections.defaultdict(int)

        l = 0
        res = 0

        for r in range(len(nums)):
            freq[nums[r]] += 1
            # if frequency > k, fix it by moving l past first occurance of nums[r]
            if freq[nums[r]] > k:
                while nums[l] != nums[r] and l < r:
                    freq[nums[l]] -= 1
                    l += 1
                l += 1
                freq[nums[r]] -= 1

            res = max(res, r-l+1)
        
        return res
