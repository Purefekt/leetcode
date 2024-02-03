"""
Top down DP.
Try to break into subarrays at each index and get the max.
Recursive function takes the index.
If index == len(arr), return 0.
Iterate from current index till idx + k (or len(arr), whichever is min).
Get the max of the current subarray and multiply that into the length of this subarray.
Memoiz this.

O(n*k) time since recursive function runs for n time and each has a loop of k time.
O(n) space since that is the height of the tree and the memoization table.
"""

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        memo = {}
        def helper(idx):
            if idx in memo:
                return memo[idx]

            if idx == len(arr):
                memo[idx] = 0
                return 0
            
            res = 0
            for i in range(idx, min(idx+k, len(arr))):
                res = max(res, max(arr[idx:i+1]) * len(arr[idx:i+1]) + helper(i+1))
            
            memo[idx] = res
            return res
            
        return helper(0)
