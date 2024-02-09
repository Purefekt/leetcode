"""
DP.
Sort the numbers, now we know for a fact that a later earlier num % later number can never be 0.
[1,2,3,4], 1%2 or 2%4 is never 0, thus we need to only check in one direction.
Create a dp array of the size of nums.
Each index at dp array stores the max divisible subset.
To find the max divisible subset, go through all indexes before the current one, see if i%j == 0 and store the size of the largest one.
Example: [4,8,10,240], suppose we have filled dp = [{4}, {4,8}, {10}, {}] now we need to fill the last index.
We iterate through and we see 240%4==0, 240%8==0 and 240%10==0, but we keep the set with the largest size which is {4,8}.
Add 240 to this set and now dp[3] = {4,8,240}.
Iterate through the dp array and return the one with the largest len.

O(n^2) time since we do go over all elements which came before current index.
O(n) space for 1D dp array.
"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()

        dp = [0] * len(nums)
        dp[0] = {nums[0]}

        for i in range(1, len(dp)):
            max_set = set()
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) > len(max_set):
                        max_set = dp[j].copy()
            
            max_set.add(nums[i])
            dp[i] = max_set

        # get max len
        max_len = 0
        res = []
        for i in range(len(dp)):
            if len(dp[i]) > max_len:
                res = dp[i]
                max_len = len(dp[i])
        
        return res
