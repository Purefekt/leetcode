"""
Dynamic Programming
Dp array will be of len(nums), set goal to the last index
Start from the 2nd last element. If its max jump val is greater or eq to idx + goal idx, set its value to 1, since in this case we only need 1 jump from this cell to reach goal
Else run a loop from 1 till its max jump val, keep a min_jump var and get the min jump for all jump values using dp cells ahead of it
Return dp[0]

O(n*k) where k is the val of maxjump
O(n) space for dp array
"""

class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = [0 for i in range(len(nums))]
        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= goal-i:
                dp[i] = 1
            else:
                min_jumps = inf
                for j in range(nums[i]):
                    min_jumps = min(min_jumps, 1+dp[i+j+1])
                dp[i] = min_jumps
        
        return dp[0]
