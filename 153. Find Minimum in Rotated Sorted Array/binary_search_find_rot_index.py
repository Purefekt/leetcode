"""
Find the rotation index (min val) using binary search. 
Set left and right pointers. If the array is not sorted then nums[l]<nums[r] and return nums[l]
Otherwise run binary search. If the current pivot value is greater than the next element, this means the next element is the rot index, return
Otherwise if pivot is greater than left element, then set left to pivot+1, else right to pivot.
O(logn) time due to binary search
O(1) space to store l,r and pivot
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # edge case
        if len(nums)<2: return nums[0]
        
        l = 0
        r = len(nums)-1
        
        if nums[l]<nums[r]: return nums[l]
        
        while l<=r:
            pivot = (l+r)//2
            
            if nums[pivot] > nums[pivot+1]:
                return nums[pivot+1]
            
            else:
                if nums[pivot] > nums[l]:
                    l = pivot+1
                else:
                    r = pivot
                    