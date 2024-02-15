"""
Sort the input and create a prefixsum array using that input.
Now iterate from the end till the third element.
At any point if nums[i] < psum[i-1], this means we can create a polygon using all numbers till this number.
Thus return the psum[i] since that is the perimeter of a polygon using all nums including current.

O(nlogn) time for sorting. Then linear scan.
O(n) space for sorting and psum array.
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        psum = []
        cur = 0
        for n in nums:
            cur += n
            psum.append(cur)
        
        for i in range(len(psum)-1, 1, -1):
            if nums[i] < psum[i-1]:
                return psum[i]

        return -1
