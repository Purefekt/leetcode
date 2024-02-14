"""
Create a new array result and maintain pos and neg counters.
Pos is the position of the next positive integer and Neg is the position of the next negative integer.
Iterate through nums, if it is positive, place it at res[pos], and increment pos += 2.
Do the same if negative but using neg pointer.

O(n) time to iterate over nums.
O(n) space for res array.
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)

        pos = 0
        neg = 1
        for n in nums:
            if n > 0:
                res[pos] = n
                pos += 2
            else:
                res[neg] = n
                neg += 2
        
        return res
