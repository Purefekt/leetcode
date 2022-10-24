"""
Kadanes algorithms
Maintain a maxsum and cur_sum.
Loop over all the numbers and keep adding them to cur_sum. Everytime check if the cur_sum > max_sum, in this case update max_sum
At any point if cur_sum becomes negative, reset it to 0
O(n) time since we iterate through the list once
O(1) space since we use constant space to store max_sum and cur_sum
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = -math.inf
        cur_sum = 0
        for n in nums:
            cur_sum += n
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        
        return max_sum
    