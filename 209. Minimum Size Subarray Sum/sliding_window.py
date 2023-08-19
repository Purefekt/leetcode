"""
Sliding window
Left and right pointer at 0
Keep moving the right pointer += 1 till the subarray sum >= target
Then till the sum >= target, move the left pointer += 1 and get the shortest len array where sum >= sum

O(n) time to go through all points once
O(1) space
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        total = 0
        res = math.inf

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r-l+1)
                total -= nums[l]
                l += 1

        if res == math.inf:
            return 0
        return res
