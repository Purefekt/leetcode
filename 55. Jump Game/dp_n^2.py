"""
DYNAMIC PROGRAMMING
Maintain an array of len(nums). Last element will be True and rest will be false since we know the last element can reach itself.
Start from 2nd last element and check for each maxjump, if it can reach a next true value, mark it as true and break since we dont need to check more
If the cell doesnt reach any true cell for all values of maxjump, it remains false
If the first cell is True, this means it reached the end, else False
O(n^2) time since we check for each element in the array and for each element we check for all values of its maxjump.
O(n) space to store the dp array.

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False for i in range(len(nums))]
        dp[-1] = True
        
        # start from 2nd last element and fill dp array till first element
        for i in range(len(nums)-2, -1, -1):
            # if val is 0, then dont change
            if nums[i] == 0:
                continue
            
            # check if current num goes to ANY true cell for every jump from 1->maxjump. maxjump = nums[i]
            for j in range(1, nums[i]+1):
                if i+j < len(nums) and dp[i+j] == True:
                    dp[i] = True
                    break
            
        # answer will be at dp[0]
        return dp[0]
        