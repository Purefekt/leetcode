"""
Runs in O(n) time.
Use two pointers. l on left end and r on right end.
initialize an array result of size nums.
compare l and r of nums, if r is larger than l, square of r will be the last element in result. move r left.
if l is smaller or equal to r, then square of l will be the last element in result
Full result array from end to start.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        
        for i in range(len(result)):
            
            if abs(nums[l]) <= abs(nums[r]):
                result[len(result) - i - 1] = nums[r] * nums[r]
                r -= 1
            
            elif abs(nums[l]) > abs(nums[r]):
                result[len(result) -i - 1] = nums[l] * nums[l]
                l += 1
            
        return result
        