"""
Get counts of all three colors. Iterate over the original list and first add the 0s, then 1s then 2s.
Uses extra memory and linear time.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get counts of all colors
        counter_hashmap = collections.Counter(nums)
        num_0 = counter_hashmap[0]
        num_1 = counter_hashmap[1]
        num_2 = counter_hashmap[2]
        
        # update the original list
        for i in range(0,num_0):
            nums[i] = 0
        for i in range(num_0,num_0+num_1):
            nums[i] = 1
        for i in range(num_0+num_1,num_0+num_1+num_2):
            nums[i] = 2
