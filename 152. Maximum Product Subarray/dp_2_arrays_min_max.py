"""
Dynamic Programming.
Create 2 dp arrays, min and max. Initialize 0th index with nums[0]
Each element in min will be the min(itself, itself*prev_min, itself*prev_max). Max for max
The solution will be the max of the max_dp array

O(n) time to iterate over all elements and one linear pass to get max from dp_max
O(n) space to keep track of dp_min and dp_max
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dp_min = [0 for i in range(len(nums))]
        dp_max = [0 for i in range(len(nums))]
        
        # initialize
        dp_min[0] = nums[0]
        dp_max[0] = nums[0]
        
        for i in range(1,len(nums)):
            dp_min[i] = min(nums[i], nums[i]*dp_min[i-1], nums[i]*dp_max[i-1])
            dp_max[i] = max(nums[i], nums[i]*dp_min[i-1], nums[i]*dp_max[i-1])
        
        return max(dp_max)
    