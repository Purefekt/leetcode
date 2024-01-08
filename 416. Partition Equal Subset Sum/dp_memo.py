"""
Dp with memoization.
Firstly if the sum of nums is an odd number, we cannot split it into 2 sets ever.
Get half of the sum, we will try to create an array where the total sum is this half, if this is valid, then we can split it.
Set up recursive function to take the idx of the element to either add or not add and the running total of this array.
Base case if idx == len(nums), if current total == half then return True, else return False.
Either add the current idx or skip it.
Memoiz on (idx, current total).

O(m*n) where we have n elements in array and m is the sum(nums)//2. 
O(m*n) space to store all pairs of (m*n) into the memo table.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        # can never split an odd total into 2 sets
        if total % 2 == 1:
            return False

        target = total//2
        
        memo = {}
        def helper(idx, half):

            if (idx, half) in memo:
                return memo[(idx, half)]
            
            if idx == len(nums):
                if half == target:
                    memo[(idx, half)] = True
                    return True
                else:
                    memo[(idx, half)] = False
                    return False
            
            # place current idx into this half
            if helper(idx+1, half + nums[idx]) is True:
                return True
            
            # do not place current idx into this half
            if helper(idx+1, half) is True:
                return True
            
            memo[(idx, half)] = False
            return False
        
        return helper(0, 0)
