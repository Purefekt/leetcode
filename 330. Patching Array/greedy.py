"""
Greedy.
We track the current lowest number which cannot be formed 'miss'.
Track the index of current num in nums and track the total number of patches needed.
Iterate till miss <= n, if miss surpasses n, this means we can sum to all numbers from 1 to n.
If we have numbers left (index < len(nums)) and nums[idx] <= miss, this means we can use current numbers to create miss.
Update miss to miss += nums[idx], since this is the next number we need to see if we can make or not and move index by 1.
Else, we cannot make miss and we need to add this number to nums, thus patches += 1. When we add this number to the array, we double the miss so miss += miss.

O(n) time.
O(1) space
"""

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        miss = 1
        patches = 0
        idx = 0

        while miss <= n:
            if idx < len(nums) and nums[idx] <= miss:
                miss += nums[idx]
                idx += 1
            else:
                miss += miss
                patches += 1
        
        return patches
        