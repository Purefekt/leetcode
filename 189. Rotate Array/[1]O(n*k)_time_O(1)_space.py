"""
Rotate the array in place for k number of time. set k = k%len(nums) to get the min number of rotations needed
O(n*k) time 
O(1) space
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) #get lowest num of rotations
        
        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]
        