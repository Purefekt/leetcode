"""
Binary search
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low < high:
            pivot = int(math.ceil(low + (high-low)/2))
            
            if target > nums[pivot]:
                low = pivot
            elif target < nums[pivot]:
                high = pivot - 1
            elif target == nums[pivot]:
                return pivot
        
        if target > nums[low]:
            return low+1
        if target <= nums[low]:
            return low
        