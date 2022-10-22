"""
DYNAMIC PROGRAMMING
Initialize dp array of length nums + 1. Each cell in the array tells us the max money after robbing houses till the index
Set first element to 0 and second element to nums[0]. First element means when we have 0 houses and second element means when we have 1 house.
Fill the dp array for houses nums[1] -> len(nums)
Recurrance equation = max(nums[i]+dp[i-1], dp[i]). Either we rob the next house which means the max will be itself and the max till the last to last house. Or we do NOT rob the house which means the max will be the previous max.
Answer will be at the last array index

O(n) time since we iterate through all houses once
O(n) space to store dp array
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * (len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        
        #fill dp
        for i in range(1, len(nums)):
            dp[i+1] = max(nums[i]+dp[i-1], dp[i])
        
        return dp[-1]
    