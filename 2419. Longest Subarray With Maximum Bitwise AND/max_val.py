"""
The maximum bitwise AND is the largest number in the array.
Since X & X -> X and X & Y = -> Z, where Z < X.
Thus to get an array of maximum bitwise AND, it must be an array containing only the maximum values.

O(n) time.
O(1) space.
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        maxval = max(nums)

        max_len = 0

        cur_len = 0
        for i in range(len(nums)):
            if nums[i] == maxval:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
        
        return max_len
