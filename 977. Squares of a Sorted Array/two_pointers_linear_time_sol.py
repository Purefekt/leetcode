"""
Two pointer in linear time.
Find the index which is 0 or positive.
The negative index is positive index -1.
if nums[pos] < nums[neg], add nums[neg]**2 to result and move neg -=1.
Else, add nums[pos]**2 to result and move pos += 1.

O(n) time.
O(1) space since output isnt taken into account.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        pos = -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                pos = i
                break
        
        # if there are no negative numbers
        if pos == 0:
            res = []
            for n in nums:
                res.append(n*n)
            return res
        
        # if there are no positive numbers
        if pos == -1:
            res = []
            for i in range(len(nums)-1, -1, -1):
                res.append(nums[i]**2)
            return res

        neg = pos-1
        res = []
        while pos < len(nums) and neg >= 0:
            if nums[pos] > abs(nums[neg]):
                res.append(nums[neg]**2)
                neg -= 1
            else:
                res.append(nums[pos]**2)
                pos += 1
        
        while pos < len(nums):
            res.append(nums[pos]**2)
            pos += 1
        
        while neg >= 0:
            res.append(nums[neg]**2)
            neg -= 1
        
        return res
            