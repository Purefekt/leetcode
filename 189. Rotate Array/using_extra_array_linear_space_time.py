"""
O(n) time and space.

create a new array of 0s of len nums called result
take each element of nums and place it to i+k places in result
if i+k is going out of bounds, place it in i+k % len(nums). The remainder will be the correct index
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # initialize result
        result = [0] * len(nums)
        
        
        for i in range(len(result)):
            new_index = (i+k) % len(result)
            result[new_index] = nums[i]
        
        nums[:] = result
        