"""
All subsequences will include all the numbers when the arrays are of size 1.
And also include the highest possible sum.
For [1,2,3], the subsequences are [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].
Sums of each are: 1,2,3,4,5,6.
Keep a psum var which tracks current prefixsum. Start res at 0.
Bitwise res and psum and current num for each num.

O(n) time for one loop over nums.
O(1) space.
"""

class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        
        psum = 0
        res = 0

        for n in nums:
            psum += n
            res = res | n | psum
        
        return res
