"""
Use input array to mark elements.
Iterate through the elements, for any x = nums[i], negate nums[abs(x)-1].
This action means we are seeing an element appear for the first time.
If we see that x is already a negative number, this means we have already negated it once before, which means it IS a duplicate.
In this case, add this to result.

O(n) time for one pass over nums.
O(1) space since res is not used for space calculation and we are modifying the input array.
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = []
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                res.append(n)
            else:
                nums[n-1] = -nums[n-1]
        
        return res
