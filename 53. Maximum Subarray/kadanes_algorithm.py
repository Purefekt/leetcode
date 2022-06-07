"""
Keep updating the current sum of a subarray till the current sum becomes negative. If it becomes negative, then set the current sum to the next element and repeat. Keep a maxsum number and update it on every iteration, it must be the max between itself and the current sum
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # initialize max sum to the first element. Initialize curr_sum to 0 since we throw away any subarray whose sum is below 0
        max_sum = nums[0]
        curr_sum = 0
        
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum = curr_sum + n
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
            