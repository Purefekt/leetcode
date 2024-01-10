"""
Naive dp will result in O(n*2^n) time complexity.
This approach uses the entire nums list as a parameter, there are 2^n subsequences of an array.
For each subsequence, we have to iterate from 0 -> n, thus the time complexity, this will give TLE.

Instead of thinking to either burst a balloon or to skip it, we can see what happens if we burst the current balloon last.
We add 1 to the left and right end of the nums array to avoid edge cases.
At a given index, we assume that we are adding it last, thus coins would be nums[l-1] * nums[i] * nums[r+1].
Then we add the max sum from left substring and max sum from right substring to it.
For each substring, we iterate from start till end.

O(n^3) time since we have n^2 different substrings and for each we iterate through it.
O(n^2) space since we store n^2 number of items in the dp cache.
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums.insert(0, 1)
        nums.append(1)
        dp = {}
        def helper(l, r):

            if l>r:
                return 0
            
            if (l,r) in dp:
                return dp[(l,r)]
            
            dp[(l,r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += helper(l, i-1) + helper(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            
            return dp[(l,r)]

        
        return helper(1, len(nums)-2)
