"""
Use an extra array and add elements to it.
New index = (current index + k)%len(nums)
copy new array to original array

O(n) time to traverse the list once
O(n) space to store extra array
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_res = [0 for i in range(len(nums))]
        
        for i in range(len(nums)):
            new_index = (i+k)%len(nums)
            nums_res[new_index] = nums[i]
        
        nums[:] = nums_res
        