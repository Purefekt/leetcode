"""
Two pointers. l at 0 and r at len-1
Add nums[l] and nums[r], if it is larger than target, move r left. If it is smaller than move l right.
If we find the target, return l+1,r+1
O(n) time to traverse the list once
O(1) space to store l and r
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers)-1
        
        while l<r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
        