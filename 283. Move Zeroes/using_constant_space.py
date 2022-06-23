"""
Using 2 pointers. Replace in place using O(1) space and O(n) time since we travese the list once.
Keep one pointer to track the first 0
Keep one pointer for current num in the list
Swap them
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p = 0 
        z = 0 # track first 0
        
        while p<len(nums):
            if nums[p] == 0:
                p += 1
            else:
                nums[p], nums[z] = nums[z], nums[p]
                z += 1
                p += 1
                