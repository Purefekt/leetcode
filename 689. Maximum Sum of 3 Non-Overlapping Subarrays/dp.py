"""
Use a dp function to get the max sum when picking 3 subarrays, similar to target sum.
Then create a while loop where we iterate over the indexes and get the 3 best subarrays.
At each index, we either keep subarray starting at idx or skip it.
If we keep, then we update result array with that index.

O(n) time. n time to pre compute all subarray sums. The dp helper func runs in n time and calling it in the while loop runs in constant time due to caching.
O(n) space used by k sums array and memoization table and stack.
"""

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        # get all subarray sums of size k
        k_sums = [sum(nums[:k])]
        l = 0
        cur = sum(nums[:k])
        for r in range(k, len(nums)):
            cur -= nums[l]
            cur += nums[r]
            l += 1
            k_sums.append(cur)
        
        # recursive function to get the max sum
        memo = {}
        def helper(idx, count):
            if (idx, count) in memo:
                return memo[(idx, count)]
            if count == 3 or idx > len(nums) - k:
                return 0
            
            keep = k_sums[idx] + helper(idx+k, count+1)
            
            skip = helper(idx+1, count)

            memo[(idx, count)] = max(keep, skip)
            return memo[(idx, count)]
        
        # get best indices
        idx = 0
        res = []

        while idx <= len(nums)-k and len(res) < 3:
            keep = k_sums[idx] + helper(idx+k, len(res)+1)
            skip = helper(idx+1, len(res))

            # keep earlier index if both are same
            if keep >= skip:
                res.append(idx)
                idx += k
            else:
                idx += 1
        
        return res
