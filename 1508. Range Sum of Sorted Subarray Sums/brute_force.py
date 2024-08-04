"""
Brute force passes.

O(n^2*logn) time.
O(n^2) space
"""

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        arr = []
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                arr.append(cur)
        
        arr.sort()

        res = 0
        for i in range(left-1, right):
            res += arr[i]
        
        mod = 10**9 + 7
        return res%mod
