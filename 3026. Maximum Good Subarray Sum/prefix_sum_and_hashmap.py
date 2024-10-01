"""
Psum.
For each index, check if we have seen a num of either n-k or n+k before.
This is because we care about the absolute diff.
For [-1,-2,-3,-4] and k=2, when we get to -4: n-k = -6 which doesnt exist but n+k = -2 exists at index 1.
We also care about the prefix sum to get the best possible subarray.
Since we have negative numbers, keeping the largest subarray isnt the best idea.
For example if we have [1,2,5,-11,5,6] and k=6. The psum array is [1,3,8,-3,2,8]. Now when we reach num=6, we can either form an array with 5 at index 2 or 5 at index 4.
The one at index 4 is better since that subarray is of sum 11 but the other subarray is of sum 0.
This gives us the clue that we need to maintain the index which has the lower psum (not the higher).
And instead of maintaining index, we can just maintain the psum till that index (excluding that num) in a hashmap.

O(n) time to iterate through nums once.
O(n) space used by min_prefix hashmap.
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        res = -math.inf
        min_prefix = {}
        psum = 0
        for n in nums:
            psum += n

            target1 = n-k
            if target1 in min_prefix:
                res = max(res, psum-min_prefix[target1])
            target2 = n+k
            if target2 in min_prefix:
                res = max(res, psum-min_prefix[target2])
            
            # update to the best prefix
            psum_before_add_cur = psum - n
            if n not in min_prefix:
                min_prefix[n] = psum_before_add_cur
            else:
                min_prefix[n] = min(min_prefix[n], psum_before_add_cur)

        if res == -math.inf:
            return 0
        return res
