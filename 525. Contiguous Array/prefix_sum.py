"""
Prefixsum.
Track the prefix sum, if 0 decrement, if 1 increment.
Track the first seen index of each unique psum.
Initialize hashmap as psum = {0:-1}, to keep it as 0 and index as -1 at the start.
Now iterate and update total, if the psum is not seen before, add it to the hashmap at that index.
If the psum is seen before, this means this is a valid array and the size is current index - psum[total].

O(n) time to iterate nums.
O(n) space used by hashmap.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        # -1 index at start
        psum = {0:-1}
        total = 0
        res = 0

        # add 1 if 1, dec 1 if 0
        for i,n in enumerate(nums):
            if total == 0:
                total -= 1
            else:
                total += 1

            if total not in psum:
                psum[total] = i
            else:
                res = max(res, i-psum[total])
        
        return res
