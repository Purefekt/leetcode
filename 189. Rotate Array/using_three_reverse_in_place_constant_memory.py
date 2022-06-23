"""
O(n) time and O(1) space
reverse the entire list
then reverse 0:k-1 of the list and k:len(nums)-1
This will be the rotated array
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # to avoid situations where we have nums = [1] and k = 2. K could be larger than the len of nums
        k = k%len(nums)
        
        # reverse the entire list
        l = 0
        r = len(nums) - 1 
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        
        # reverse [0:k-1]
        l = 0
        r = k-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        # revese [k:len(nums)-1]
        l = k
        r = len(nums) - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        