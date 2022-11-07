"""
Reverse the list in place. 
Then reverse the first k elements in place. 
Then reverse last n-k elements in place.
Make sure to truncate k by k=k%len(nums)

O(n) time. We do 3 passes. One over the entire array, one over k and one over n-k
O(1) space, in place
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        
        def reverse(l,r):
            while l<=r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # reverse entire array
        reverse(l=0, r=len(nums)-1)
        # reverse the first k-1 elements
        reverse(l=0, r=k-1)
        # reverse the last n-k elements
        reverse(l=k, r=len(nums)-1)
        