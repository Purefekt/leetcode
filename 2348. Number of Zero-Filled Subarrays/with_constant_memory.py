"""
The pattern is, number of zeros: number of subarrays.
1:1, 2:3, 3:6.
Suppose we have the array [0,0,0]. When we reach the first 0, we have a subarray of 1 zeros.
The count is 1. When we reach the next 0, we add a zero to the current subarray, ie adding 2 to the count.
Then we reach the next 0, we add another zero to current subarray, ie adding 3 to the count.
Thus we maintain a count var and increment it by 1 for every consecutive addition of 0, and add that to the result.
If we reach an index != 0, then we reset count to 0.

O(n) time
O(1) space
"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        res = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count = 0
            
            res += count
        
        return res
        