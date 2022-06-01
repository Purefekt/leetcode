class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # use a right and left pointer and a pivot which will be the midpoint of l and r
        left = 0
        right = len(nums) - 1
        
        # left cannot cross right
        while left <= right:
            
            # pivot is the midpoint
            pivot = (left + right) // 2
            
            # if the target is nums[pivot], return pivot
            if target == nums[pivot]:
                return pivot
            
            # if target is larget than nums[pivot], all nums before and including nums[pivot] are smaller than target. Thus move left pointer to pivot + 1
            if target > nums[pivot]:
                left = pivot + 1
            
            # similar if target is less than pivot
            if target < nums[pivot]:
                right = pivot - 1
        
        # if we exit loop, we couldnt find the number
        return -1
            