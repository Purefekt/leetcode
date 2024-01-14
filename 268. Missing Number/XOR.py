"""
XOR of 2 same same number is 0.
XOR of any number and 0 is that number.
We have n numbers where one number is missing from 0 till n.
So we might have [0,1,3] where we shouldve had [0,1,2,3].
Thus if we XOR all the numbers in nums and all the numbers that SHOULDVE been in nums, we will be left with the missing number.
Here res = 0^1^3^0^1^2^3, here 0,0,1,1,3,3 will cancel and leave 2.

O(n) time to do 2 passes over nums.
O(1) space
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0

        for i in range(len(nums)+1):
            res ^= i
        
        for n in nums:
            res ^= n
        
        return res
