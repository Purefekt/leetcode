"""
Since this is a circular array, the maximum sum subarray can either be in the middle of the array OR it can be a part of the circular array.
Example of first case -> [-1,2,3,-1].
Example of second case -> [5,5,-10,-10,-10,5,5].
Use kadanes algorithm to get the maxSum in a non circular array.
Then use kadanes algorithm but to find the minimum sum subarray in a non circular array.
To get the maximum sum subarray in a circular array, we subtract the sum of the array with the minimum sum subarray.
The result is the max of the 2.

O(n) time. 2 passes over the entire array to find the max and min
O(1) space to store values maxSum, cur_sum, minSum, maxCircularSum
"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # kadanes algorithm to find max sum subarray
        maxSum = -math.inf
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            maxSum = max(maxSum, cur_sum)
            
            if cur_sum < 0:
                cur_sum = 0
        
        # edge case where all numbers are negative
        if maxSum < 0:
            return maxSum
        
        # find the min sum subarray
        minSum = math.inf
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            minSum = min(minSum, cur_sum)

            if cur_sum > 0:
                cur_sum = 0
        
        # if we subtract the minSum subarray from the total sum, we get the maximum circular subarray sum
        maxCircularSum = sum(nums) - minSum

        return max(maxSum, maxCircularSum)
        